#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import re
from collections import Counter
from pathlib import Path

VOLUME = "IV"
PART = "04"

THEMES = (
    "Holomorphic Functions",
    "Singularities and Residues",
    "Global Complex Analysis",
    "Special Functions",
    "Riemann Surfaces",
    "Elliptic Functions",
)

def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        return [dict(r) for r in csv.DictReader(f, delimiter="\t")]

def find_negative_brace_depth(text: str) -> list[int]:
    bad = []
    depth = 0
    line_no = 1
    i = 0
    while i < len(text):
        ch = text[i]
        if ch == "\n":
            line_no += 1
            i += 1
            continue
        if ch == "\\":
            i += 2 if i + 1 < len(text) else 1
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
    migration_path = base / "metadata" / "PART_IV_MIGRATION.tsv"
    summary_path = base / "metadata" / "PART_IV_MIGRATION_SUMMARY.md"
    chapter_path = base / "chapters" / "part04_volume_iv" / "chapter.tex"
    designed_manifest_path = base / "metadata" / "PART_IV_CANDIDATE_FIGURE_MANIFEST.tsv"

    errors: list[str] = []

    for p in (atlas_path, migration_path, summary_path, chapter_path):
        if not p.exists():
            errors.append(f"missing file: {p.relative_to(repo)}")
    if errors:
        print("COMPANION PART IV VALIDATION FAILED")
        for e in errors:
            print("  -", e)
        return 1

    atlas_rows = read_tsv(atlas_path)
    migration_rows = read_tsv(migration_path)
    part_rows = [r for r in atlas_rows if r.get("related_volume") == VOLUME]

    expected_ids = {
        r.get("semantic_unit_id", "")
        for r in part_rows
        if r.get("semantic_unit_id")
    }
    actual_ids = {
        r.get("semantic_unit_id", "")
        for r in migration_rows
        if r.get("semantic_unit_id")
    }

    if len(migration_rows) != len(part_rows):
        errors.append(
            f"migration row count mismatch: atlas={len(part_rows)} migration={len(migration_rows)}"
        )
    if len(actual_ids) != len(migration_rows):
        errors.append("duplicate semantic_unit_id in PART_IV_MIGRATION.tsv")
    if actual_ids != expected_ids:
        errors.append(
            f"semantic coverage mismatch: missing={len(expected_ids-actual_ids)} extra={len(actual_ids-expected_ids)}"
        )

    cpids = [r.get("companion_problem_id", "") for r in migration_rows]
    if len(set(cpids)) != len(cpids):
        errors.append("duplicate companion_problem_id in PART_IV_MIGRATION.tsv")

    for row in migration_rows:
        cp = row.get("companion_problem_id", "")
        if not re.fullmatch(r"CP-IV-\d{4}", cp):
            errors.append(f"invalid Part IV Companion ID: {cp}")
        status = row.get("migration_status", "")
        if status not in {"MIGRATED_TO_COMPANION", "EDITORIAL_HOLD"}:
            errors.append(f"{cp}: invalid migration_status {status}")
        if status == "MIGRATED_TO_COMPANION" and row.get("statement_status") != "MIGRATED":
            errors.append(f"{cp}: migrated row lacks MIGRATED statement_status")

    tex = chapter_path.read_text(encoding="utf-8")
    tex_lines = tex.splitlines()

    labels = re.findall(r"\\label\{prob:(cp-iv-\d{4})\}", tex, re.I)
    rendered = {
        r.get("companion_problem_id", "").lower()
        for r in migration_rows
        if r.get("migration_status") == "MIGRATED_TO_COMPANION"
    }
    label_set = {x.lower() for x in labels}

    if label_set != rendered:
        errors.append(
            f"reader-facing label coverage mismatch: expected={len(rendered)} actual={len(label_set)}"
        )
    if len(labels) != len(label_set):
        errors.append("duplicate Part IV problem labels")

    problem_count = len(re.findall(r"\\begin\{problem\}", tex))
    if problem_count != len(rendered):
        errors.append(
            f"Problem environment count mismatch: expected={len(rendered)} actual={problem_count}"
        )

    expected_solutions = sum(
        1 for r in migration_rows
        if r.get("solution_status", "").startswith("MIGRATED_PRIMARY_SOLUTION")
    )
    source_backed_solutions = expected_solutions
    expected_solutions = len(rendered)
    solution_count = len(re.findall(r"\\begin\{solution\}", tex))
    if solution_count != expected_solutions:
        errors.append(
            f"Solution environment count mismatch: expected={expected_solutions} actual={solution_count}"
        )

    # Completed Part IV problem/solution pairing.
    problem_blocks = list(re.finditer(
        r"\\begin\{problem\}\[(CP-IV-\d{4})\].*?\\end\{problem\}",
        tex,
        re.S,
    ))
    for idx, match in enumerate(problem_blocks):
        next_start = (
            problem_blocks[idx + 1].start()
            if idx + 1 < len(problem_blocks)
            else len(tex)
        )
        gap = tex[match.end():next_start]
        paired = len(re.findall(r"\\begin\{solution\}", gap))
        if paired != 1:
            errors.append(
                f"{match.group(1)}: expected exactly one paired solution before "
                f"the next problem, found {paired}"
            )

    # Designed figure placement.
    if designed_manifest_path.exists():
        manifest = read_tsv(designed_manifest_path)
        expected_fig_inputs = {
            r.get("companion_problem_id", "").lower(): r.get("file", "").replace("\\", "/")
            for r in manifest
            if r.get("companion_problem_id")
        }
        migrated_upper = {
            r.get("companion_problem_id", "") for r in migration_rows
            if r.get("migration_status") == "MIGRATED_TO_COMPANION"
        }
        expected_files = {
            path for cid, path in expected_fig_inputs.items()
            if cid.upper() in migrated_upper and path
        }
        actual_files = set(
            re.findall(r"\\input\{(figures/part04/designed/[^}]+\.tex)\}", tex)
        )
        if actual_files != expected_files:
            errors.append(
                f"designed figure input coverage mismatch: expected={len(expected_files)} actual={len(actual_files)}"
            )
        for rel in expected_files:
            if not (base / rel).exists():
                errors.append(f"designed figure input missing on disk: {rel}")

    for forbidden in (
        r"\documentclass",
        r"\usepackage",
        r"\begin{document}",
        r"\end{document}",
    ):
        if forbidden in tex:
            errors.append(f"imported preamble/document command leaked into chapter: {forbidden}")

    if re.search(r"\b(TODO|FIXME|TBD|PLACEHOLDER)\b", tex, re.I):
        errors.append("unfinished workflow marker in reader-facing Part IV chapter")

    for lineno, line in enumerate(tex_lines, 1):
        if re.search(r"\\(?:begin|end)\{(?:itemize|enumerate|description)\*?\}", line):
            errors.append(f"legacy list environment survived at line {lineno}: {line!r}")
        if re.search(r"(^|\s)\\item(?:\[|\s|$)", line):
            errors.append(f"legacy \\item survived at line {lineno}: {line!r}")
        if re.search(r"\\tr\b", line):
            errors.append(f"legacy undefined \\tr survived at line {lineno}")
        if re.search(r"\\gap\b", line):
            errors.append(f"legacy undefined \\gap survived at line {lineno}")
        if re.search(r"\\Bbb\b", line):
            errors.append(f"obsolete \\Bbb survived at line {lineno}")
        if re.search(
            r"\\(?:chapter|section|subsection|subsubsection|paragraph)\*?\s*"
            r"\{\s*(?:Solution|Answer|Proof)\s*[.:;!?-]?\s*\}",
            line, re.I
        ):
            errors.append(f"nested source solution heading survived at line {lineno}")
        if re.search(r"\\qed(?:here)?\b", line):
            errors.append(f"source QED command survived at line {lineno}")
        if "\x00" in line:
            errors.append(f"NUL control byte survived at line {lineno}")

    for lineno in find_negative_brace_depth(tex):
        errors.append(
            f"unmatched closing brace drives local TeX brace depth negative at reader-facing line {lineno}"
        )

    if errors:
        print("COMPANION PART IV VALIDATION FAILED")
        for e in errors[:120]:
            print("  -", e)
        if len(errors) > 120:
            print(f"  ... {len(errors)-120} more")
        return 1

    counts = Counter(
        r.get("thematic_section", "")
        for r in migration_rows
        if r.get("migration_status") == "MIGRATED_TO_COMPANION"
    )
    holds = sum(
        1 for r in migration_rows if r.get("migration_status") == "EDITORIAL_HOLD"
    )

    print("COMPANION PART IV VALIDATION PASSED")
    print(f"  atlas units/dispositions: {len(migration_rows)}")
    print(f"  reader-facing problems: {len(rendered)}")
    print(f"  solutions: {expected_solutions}")
    print(f"  source-backed migrated solutions: {source_backed_solutions}")
    print(f"  canonical authored solutions: {expected_solutions - source_backed_solutions}")
    print(f"  editorial holds: {holds}")
    for theme in THEMES:
        print(f"  {theme}: {counts.get(theme,0)}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
