#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import re
from collections import Counter
from pathlib import Path


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        return [dict(r) for r in csv.DictReader(f, delimiter="\t")]


def find_negative_brace_depth(text: str) -> list[int]:
    """Return line numbers where an unescaped closing brace makes depth negative."""
    bad: list[int] = []
    depth = 0
    line_no = 1
    i = 0

    while i < len(text):
        ch = text[i]

        if ch == "\n":
            line_no += 1
            i += 1
            continue

        # For grouping purposes, skip escaped literal next characters.
        if ch == "\\":
            if i + 1 < len(text):
                i += 2
            else:
                i += 1
            continue

        if ch == "{":
            depth += 1
        elif ch == "}":
            if depth == 0:
                bad.append(line_no)
            else:
                depth -= 1

        i += 1

    return bad


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", type=Path, default=Path.cwd())
    args = ap.parse_args()

    repo = args.repo.resolve()
    base = repo / "books" / "companion_problems_solutions"

    atlas_path = base / "metadata" / "COMPANION_PROBLEM_ATLAS.tsv"
    migration_path = base / "metadata" / "PART_I_MIGRATION.tsv"
    summary_path = base / "metadata" / "PART_I_MIGRATION_SUMMARY.md"
    chapter_path = base / "chapters" / "part01_volume_i" / "chapter.tex"

    errors: list[str] = []

    # ------------------------------------------------------------------
    # 1. Required files
    # ------------------------------------------------------------------
    for p in (atlas_path, migration_path, summary_path, chapter_path):
        if not p.exists():
            errors.append(f"missing file: {p.relative_to(repo)}")

    if errors:
        print("COMPANION PART I VALIDATION FAILED")
        for e in errors:
            print("  -", e)
        return 1

    # ------------------------------------------------------------------
    # 2. Load machine-readable ledgers
    # ------------------------------------------------------------------
    atlas_rows = read_tsv(atlas_path)
    migration_rows = read_tsv(migration_path)

    part_rows = [r for r in atlas_rows if r.get("related_volume") == "I"]

    expected_semantic_ids = {
        r.get("semantic_unit_id", "") for r in part_rows if r.get("semantic_unit_id")
    }
    actual_semantic_ids = {
        r.get("semantic_unit_id", "")
        for r in migration_rows
        if r.get("semantic_unit_id")
    }

    if len(migration_rows) != len(part_rows):
        errors.append(
            f"migration row count mismatch: "
            f"atlas={len(part_rows)} migration={len(migration_rows)}"
        )

    if len(actual_semantic_ids) != len(migration_rows):
        errors.append("duplicate semantic_unit_id in PART_I_MIGRATION.tsv")

    if actual_semantic_ids != expected_semantic_ids:
        errors.append(
            f"semantic coverage mismatch: "
            f"missing={len(expected_semantic_ids-actual_semantic_ids)} "
            f"extra={len(actual_semantic_ids-expected_semantic_ids)}"
        )

    cpids = [r.get("companion_problem_id", "") for r in migration_rows]
    if len(set(cpids)) != len(cpids):
        errors.append("duplicate companion_problem_id in PART_I_MIGRATION.tsv")

    valid_dispositions = {"MIGRATED_TO_COMPANION", "EDITORIAL_HOLD"}

    for row in migration_rows:
        cp = row.get("companion_problem_id", "")
        disposition = row.get("migration_status", "")

        if disposition not in valid_dispositions:
            errors.append(f"{cp}: invalid migration_status {disposition}")

        if (
            disposition == "MIGRATED_TO_COMPANION"
            and row.get("statement_status") != "MIGRATED"
        ):
            errors.append(f"{cp}: migrated row lacks MIGRATED statement_status")

    # ------------------------------------------------------------------
    # 3. NOW load reader-facing TeX.
    #    Nothing below this point can reference `tex` before assignment.
    # ------------------------------------------------------------------
    tex = chapter_path.read_text(encoding="utf-8")
    tex_lines = tex.splitlines()

    # ------------------------------------------------------------------
    # 4. Problem and solution coverage
    # ------------------------------------------------------------------
    labels = re.findall(r"\\label\{prob:(cp-i-\d{4})\}", tex, re.I)

    rendered = {
        r.get("companion_problem_id", "").lower()
        for r in migration_rows
        if r.get("migration_status") == "MIGRATED_TO_COMPANION"
    }

    label_set = {x.lower() for x in labels}

    if label_set != rendered:
        errors.append(
            f"reader-facing label coverage mismatch: "
            f"expected={len(rendered)} actual={len(label_set)}"
        )

    if len(labels) != len(label_set):
        errors.append("duplicate Part I problem labels")

    problem_count = len(re.findall(r"\\begin\{problem\}", tex))
    if problem_count != len(rendered):
        errors.append(
            f"Problem environment count mismatch: "
            f"expected={len(rendered)} actual={problem_count}"
        )

    expected_solutions = sum(
        1
        for r in migration_rows
        if r.get("solution_status", "").startswith("MIGRATED_PRIMARY_SOLUTION")
    )
    solution_count = len(re.findall(r"\\begin\{solution\}", tex))

    if solution_count != expected_solutions:
        errors.append(
            f"Solution environment count mismatch: "
            f"expected={expected_solutions} actual={solution_count}"
        )

    # ------------------------------------------------------------------
    # 5. Reader-facing hygiene
    # ------------------------------------------------------------------
    for forbidden in (
        r"\documentclass",
        r"\usepackage",
        r"\begin{document}",
        r"\end{document}",
    ):
        if forbidden in tex:
            errors.append(
                f"imported preamble/document command leaked into chapter: {forbidden}"
            )

    if re.search(r"\b(TODO|FIXME|TBD|PLACEHOLDER)\b", tex, re.I):
        errors.append("unfinished workflow marker in reader-facing Part I chapter")

    # Bare standalone grouping braces.
    for lineno, line in enumerate(tex_lines, 1):
        if re.fullmatch(r"\s*[{}]\s*", line):
            errors.append(
                f"standalone orphan brace line at reader-facing line "
                f"{lineno}: {line!r}"
            )

    # Legacy lists should have been flattened.
    for lineno, line in enumerate(tex_lines, 1):
        if re.search(
            r"\\(?:begin|end)\{(?:itemize|enumerate|description)\*?\}",
            line,
        ):
            errors.append(
                f"legacy list environment survived flattening at "
                f"reader-facing line {lineno}: {line!r}"
            )

        if re.search(r"(^|\s)\\item(?:\[|\s|$)", line):
            errors.append(
                f"legacy \\item survived flattening at "
                f"reader-facing line {lineno}: {line!r}"
            )

    # Unsupported confirmed legacy macro.
    for lineno, line in enumerate(tex_lines, 1):
        if re.search(r"\\tr\b", line):
            errors.append(
                f"legacy undefined operator \\tr survived at "
                f"reader-facing line {lineno}: {line!r}"
            )

    # Attached unmatched closing-brace residue.
    negative_lines = find_negative_brace_depth(tex)
    for lineno in negative_lines:
        errors.append(
            f"unmatched closing brace drives local TeX brace depth negative "
            f"at reader-facing line {lineno}"
        )

    # ------------------------------------------------------------------
    # 6. Final result
    # ------------------------------------------------------------------
    if errors:
        print("COMPANION PART I VALIDATION FAILED")
        for e in errors[:100]:
            print("  -", e)
        if len(errors) > 100:
            print(f"  ... {len(errors)-100} more")
        return 1

    counts = Counter(
        r.get("thematic_section", "")
        for r in migration_rows
        if r.get("migration_status") == "MIGRATED_TO_COMPANION"
    )

    holds = sum(
        1
        for r in migration_rows
        if r.get("migration_status") == "EDITORIAL_HOLD"
    )

    print("COMPANION PART I VALIDATION PASSED")
    print(f"  atlas units/dispositions: {len(migration_rows)}")
    print(f"  reader-facing problems: {len(rendered)}")
    print(f"  solutions: {expected_solutions}")
    print(f"  editorial holds: {holds}")

    for theme in (
        "Vector Spaces",
        "Matrices and Operators",
        "Euclidean and Hilbert-Space Geometry",
    ):
        print(f"  {theme}: {counts.get(theme, 0)}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
