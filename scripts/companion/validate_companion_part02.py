#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import re
from collections import Counter
from pathlib import Path

VOLUME = "II"
PART = "02"

EXPECTED_READER_PROBLEMS = 570
EXPECTED_READER_SOLUTIONS = 570
EXPECTED_SOURCE_BACKED_SOLUTIONS = 165
EXPECTED_CANONICAL_AUTHORED_SOLUTIONS = 405
EXPECTED_EDITORIAL_HOLDS = 0

THEMES = (
    "Metric and Topological Foundations",
    "Calculus",
    "Sequences of Functions",
    "Fixed Points and Differential Equations",
    "Approximation",
)


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        return [dict(r) for r in csv.DictReader(f, delimiter="\t")]


def find_brace_depth_issues(text: str) -> tuple[list[int], int]:
    """Return lines where brace depth goes negative and final positive depth.

    This is intentionally structural, not stylistic.  A line containing only
    "}" can be a perfectly valid close of a multiline TeX argument, so the
    validator must not reject such lines merely by their visual shape.
    """
    bad: list[int] = []
    depth = 0
    line_no = 1
    i = 0
    in_comment = False

    while i < len(text):
        ch = text[i]

        if ch == "\n":
            line_no += 1
            in_comment = False
            i += 1
            continue

        if in_comment:
            i += 1
            continue

        # Unescaped % starts a TeX comment.
        if ch == "%":
            in_comment = True
            i += 1
            continue

        # Escaped braces, percent signs, etc. are literal characters.
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

    return bad, depth


def extract_problem_pairing(tex: str) -> tuple[list[str], dict[str, str], list[str]]:
    """Return problem IDs, paired solution blocks, and pairing errors."""
    errors: list[str] = []
    starts = list(re.finditer(r"\\begin\{problem\}\[(CP-II-\d{4})\]", tex))
    ids = [m.group(1) for m in starts]
    paired: dict[str, str] = {}

    for idx, start in enumerate(starts):
        pid = start.group(1)
        next_start = starts[idx + 1].start() if idx + 1 < len(starts) else len(tex)
        block_window = tex[start.start():next_start]

        end_match = re.search(r"\\end\{problem\}", block_window)
        if not end_match:
            errors.append(f"{pid}: missing \\end{{problem}} before next problem")
            continue

        problem_body = block_window[:end_match.end()]
        labels = re.findall(r"\\label\{prob:(cp-ii-\d{4})\}", problem_body, re.I)
        expected_label = pid.lower()
        if labels != [expected_label]:
            errors.append(
                f"{pid}: expected exactly label prob:{expected_label}, found {labels}"
            )

        gap = block_window[end_match.end():]
        solution_blocks = re.findall(
            r"\\begin\{solution\}.*?\\end\{solution\}", gap, re.S
        )
        if len(solution_blocks) != 1:
            errors.append(
                f"{pid}: expected exactly one paired solution before next problem, "
                f"found {len(solution_blocks)}"
            )
        elif pid in paired:
            errors.append(f"{pid}: duplicate problem ID encountered during pairing")
        else:
            paired[pid] = solution_blocks[0]

    return ids, paired, errors


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", type=Path, default=Path.cwd())
    args = ap.parse_args()

    repo = args.repo.resolve()
    base = repo / "books" / "companion_problems_solutions"
    atlas_path = base / "metadata" / "COMPANION_PROBLEM_ATLAS.tsv"
    migration_path = base / "metadata" / "PART_II_MIGRATION.tsv"
    summary_path = base / "metadata" / "PART_II_MIGRATION_SUMMARY.md"
    chapter_path = base / "chapters" / "part02_volume_ii" / "chapter.tex"

    errors: list[str] = []

    for p in (atlas_path, migration_path, summary_path, chapter_path):
        if not p.exists():
            errors.append(f"missing file: {p.relative_to(repo)}")

    if errors:
        print("COMPANION PART II VALIDATION FAILED")
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
            f"migration row count mismatch: atlas={len(part_rows)} "
            f"migration={len(migration_rows)}"
        )
    if len(migration_rows) != EXPECTED_READER_PROBLEMS:
        errors.append(
            f"Part II migration ledger row count: expected "
            f"{EXPECTED_READER_PROBLEMS}, got {len(migration_rows)}"
        )
    if len(actual_ids) != len(migration_rows):
        errors.append("duplicate semantic_unit_id in PART_II_MIGRATION.tsv")
    if actual_ids != expected_ids:
        errors.append(
            f"semantic coverage mismatch: missing={len(expected_ids-actual_ids)} "
            f"extra={len(actual_ids-expected_ids)}"
        )

    cpids = [r.get("companion_problem_id", "") for r in migration_rows]
    if len(set(cpids)) != len(cpids):
        duplicates = sorted({cp for cp in cpids if cpids.count(cp) > 1})
        errors.append(
            "duplicate companion_problem_id in PART_II_MIGRATION.tsv: "
            + ", ".join(duplicates)
        )

    for row in migration_rows:
        cp = row.get("companion_problem_id", "")
        if not re.fullmatch(r"CP-II-\d{4}", cp):
            errors.append(f"invalid Part II Companion ID: {cp}")
        status = row.get("migration_status", "")
        if status not in {"MIGRATED_TO_COMPANION", "EDITORIAL_HOLD"}:
            errors.append(f"{cp}: invalid migration_status {status}")
        if status == "MIGRATED_TO_COMPANION" and row.get("statement_status") != "MIGRATED":
            errors.append(f"{cp}: migrated row lacks MIGRATED statement_status")

    source_backed_solutions = sum(
        1
        for r in migration_rows
        if r.get("solution_status", "").startswith("MIGRATED_PRIMARY_SOLUTION")
    )
    if source_backed_solutions != EXPECTED_SOURCE_BACKED_SOLUTIONS:
        errors.append(
            f"source-backed solution provenance mismatch: expected "
            f"{EXPECTED_SOURCE_BACKED_SOLUTIONS}, got {source_backed_solutions}"
        )

    holds = sum(
        1 for r in migration_rows if r.get("migration_status") == "EDITORIAL_HOLD"
    )
    if holds != EXPECTED_EDITORIAL_HOLDS:
        errors.append(
            f"editorial hold count mismatch: expected {EXPECTED_EDITORIAL_HOLDS}, got {holds}"
        )

    tex = chapter_path.read_text(encoding="utf-8")
    tex_lines = tex.splitlines()

    rendered = {
        r.get("companion_problem_id", "").upper()
        for r in migration_rows
        if r.get("migration_status") == "MIGRATED_TO_COMPANION"
    }
    if len(rendered) != EXPECTED_READER_PROBLEMS:
        errors.append(
            f"reader-facing migration disposition count: expected "
            f"{EXPECTED_READER_PROBLEMS}, got {len(rendered)}"
        )

    problem_ids, paired_solutions, pairing_errors = extract_problem_pairing(tex)
    errors.extend(pairing_errors)

    problem_set = set(problem_ids)
    if len(problem_ids) != EXPECTED_READER_PROBLEMS:
        errors.append(
            f"Problem environment count mismatch: expected "
            f"{EXPECTED_READER_PROBLEMS}, got {len(problem_ids)}"
        )
    if len(problem_set) != len(problem_ids):
        duplicates = sorted({pid for pid in problem_ids if problem_ids.count(pid) > 1})
        errors.append("duplicate canonical problem IDs: " + ", ".join(duplicates))
    if problem_set != rendered:
        errors.append(
            f"reader-facing problem ID coverage mismatch: "
            f"missing={len(rendered-problem_set)} extra={len(problem_set-rendered)}"
        )

    labels = re.findall(r"\\label\{prob:(cp-ii-\d{4})\}", tex, re.I)
    label_set = {x.upper() for x in labels}
    if len(labels) != EXPECTED_READER_PROBLEMS:
        errors.append(
            f"problem label count mismatch: expected {EXPECTED_READER_PROBLEMS}, "
            f"got {len(labels)}"
        )
    if len(label_set) != len(labels):
        errors.append("duplicate Part II problem labels")
    if {x.upper() for x in labels} != rendered:
        errors.append(
            f"reader-facing label coverage mismatch: expected={len(rendered)} "
            f"actual={len(label_set)}"
        )

    solution_count = len(re.findall(r"\\begin\{solution\}", tex))
    solution_end_count = len(re.findall(r"\\end\{solution\}", tex))
    problem_end_count = len(re.findall(r"\\end\{problem\}", tex))
    if problem_end_count != EXPECTED_READER_PROBLEMS:
        errors.append(
            f"Problem end-environment count mismatch: expected "
            f"{EXPECTED_READER_PROBLEMS}, actual={problem_end_count}"
        )
    if solution_end_count != EXPECTED_READER_SOLUTIONS:
        errors.append(
            f"Solution end-environment count mismatch: expected "
            f"{EXPECTED_READER_SOLUTIONS}, actual={solution_end_count}"
        )
    if solution_count != EXPECTED_READER_SOLUTIONS:
        errors.append(
            f"Solution environment count mismatch: expected "
            f"{EXPECTED_READER_SOLUTIONS}, actual={solution_count}"
        )
    if len(paired_solutions) != EXPECTED_READER_SOLUTIONS:
        errors.append(
            f"exact problem/solution pairing count mismatch: expected "
            f"{EXPECTED_READER_SOLUTIONS}, got {len(paired_solutions)}"
        )

    canonical_authored_solutions = solution_count - source_backed_solutions
    if canonical_authored_solutions != EXPECTED_CANONICAL_AUTHORED_SOLUTIONS:
        errors.append(
            f"canonical authored solution provenance mismatch: expected "
            f"{EXPECTED_CANONICAL_AUTHORED_SOLUTIONS}, got "
            f"{canonical_authored_solutions}"
        )

    # Regression gate for the reconciled CP-II-0494 solution.
    cp0494 = paired_solutions.get("CP-II-0494", "")
    for required in (
        r"x_{2^k}",
        r"\frac{k}{2^k}",
        "does not define a map",
        r"\|Te_N\|_\infty=N",
    ):
        if required not in cp0494:
            errors.append(
                "CP-II-0494: reconciliation signature missing from paired solution: "
                + required
            )

    summary = summary_path.read_text(encoding="utf-8")
    summary_checks = (
        ("reader-facing solutions", r"Reader-facing solutions:\s*\*\*570\*\*"),
        ("source-backed solutions", r"Source-backed migrated solutions:\s*\*\*165\*\*"),
        ("canonical authored solutions", r"Canonical authored solutions:\s*\*\*405\*\*"),
        ("zero reader-facing missing", r"Reader-facing problems without a solution:\s*\*\*0\*\*"),
    )
    for name, pattern in summary_checks:
        if not re.search(pattern, summary, re.I):
            errors.append(f"PART_II_MIGRATION_SUMMARY.md missing reconciled {name} fact")

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
        errors.append("unfinished workflow marker in reader-facing Part II chapter")

    for lineno, line in enumerate(tex_lines, 1):
        if re.search(
            r"\\(?:begin|end)\{(?:itemize|enumerate|description)\*?\}",
            line,
        ):
            errors.append(
                f"legacy list environment survived flattening at line {lineno}: {line!r}"
            )
        if re.search(r"(^|\s)\\item(?:\[|\s|$)", line):
            errors.append(
                f"legacy \\item survived flattening at line {lineno}: {line!r}"
            )
        if re.search(r"\\tr\b", line):
            errors.append(
                f"legacy undefined operator \\tr survived at line {lineno}: {line!r}"
            )
        if re.search(r"\\gap\b", line):
            errors.append(
                f"legacy undefined spacing macro \\gap survived at line {lineno}: {line!r}"
            )
        if re.search(r"\\Bbb\b", line):
            errors.append(
                f"obsolete \\Bbb survived normalization at line {lineno}: {line!r}"
            )
        if re.search(
            r"\\(?:chapter|section|subsection|subsubsection|paragraph)\*?\s*"
            r"\{\s*(?:Solution|Answer|Proof)\s*[.:;!?-]?\s*\}",
            line,
            re.I,
        ):
            errors.append(
                f"nested source solution heading survived at line {lineno}: {line!r}"
            )
        if re.search(r"\\qed(?:here)?\b", line):
            errors.append(
                f"source QED command survived at line {lineno}: {line!r}"
            )
        if "\x00" in line:
            errors.append(f"NUL control byte survived at line {lineno}")

    negative_brace_lines, final_brace_depth = find_brace_depth_issues(tex)
    for lineno in negative_brace_lines:
        errors.append(
            f"unmatched closing brace drives local TeX brace depth negative "
            f"at reader-facing line {lineno}"
        )
    if final_brace_depth:
        errors.append(
            f"unclosed TeX brace groups at end of chapter: depth={final_brace_depth}"
        )

    if errors:
        print("COMPANION PART II VALIDATION FAILED")
        for e in errors[:140]:
            print("  -", e)
        if len(errors) > 140:
            print(f"  ... {len(errors)-140} more")
        return 1

    counts = Counter(
        r.get("thematic_section", "")
        for r in migration_rows
        if r.get("migration_status") == "MIGRATED_TO_COMPANION"
    )

    print("COMPANION PART II VALIDATION PASSED")
    print(f"  atlas units/dispositions: {len(migration_rows)}")
    print(f"  reader-facing problems: {len(problem_ids)}")
    print(f"  solutions: {solution_count}")
    print(f"  exact problem/solution pairs: {len(paired_solutions)}")
    print(f"  source-backed migrated solutions: {source_backed_solutions}")
    print(f"  canonical authored solutions: {canonical_authored_solutions}")
    print(f"  editorial holds: {holds}")
    print("  CP-II-0494 reconciliation: PASS")
    for theme in THEMES:
        print(f"  {theme}: {counts.get(theme,0)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
