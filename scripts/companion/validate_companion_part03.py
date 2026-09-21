#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import re
from collections import Counter
from pathlib import Path

EXPECTED = [f"CP-III-{i:04d}" for i in range(1, 26)]
THEMES = [
    "Measure and Integration",
    "Fourier Analysis",
    "Distribution Theory",
    "Sobolev and PDE Methods",
]

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", type=Path, required=True)
    args = ap.parse_args()
    repo = args.repo.resolve()

    chapter = (
        repo / "books" / "companion_problems_solutions" / "chapters"
        / "part03_volume_iii" / "chapter.tex"
    )
    ledger = (
        repo / "books" / "companion_problems_solutions" / "metadata"
        / "PART_III_MIGRATION.tsv"
    )

    errors = []
    if not chapter.exists():
        print("COMPANION PART III VALIDATION FAILED")
        print("  - missing chapter:", chapter)
        return 1

    text = chapter.read_text(encoding="utf-8")
    problems = re.findall(r"\\begin\{problem\}\[(CP-III-\d+)\]", text)
    solutions = len(re.findall(r"\\begin\{solution\}", text))
    labels = re.findall(r"\\label\{prob:(cp-iii-\d+)\}", text)

    expected_set = set(EXPECTED)
    actual_set = set(problems)

    if len(problems) != 25 or actual_set != expected_set:
        missing = sorted(expected_set - actual_set)
        unexpected = sorted(actual_set - expected_set)
        errors.append(
            "problem ID completeness mismatch: "
            f"count={len(problems)}, missing={missing}, unexpected={unexpected}"
        )

    if len(problems) != len(actual_set):
        duplicates = sorted({
            pid for pid in problems if problems.count(pid) > 1
        })
        errors.append("duplicate canonical problem IDs: " + ", ".join(duplicates))

    if len(labels) != 25 or len(set(labels)) != 25:
        errors.append(f"problem labels: expected 25 unique, got {len(set(labels))}")

    residue = {
        "qed": r"\\qed(?:here)?\b",
        "probheader": r"\\probheader\b",
        "statement": r"\\(?:begin|end)\{statement\}",
        "spacy": r"\\(?:begin|end)\{spacy\}",
        "tighthrule": r"\\tighthrule\b",
        "sectioning_in_problem_body": r"\\(?:section|subsection|subsubsection|paragraph|subparagraph)\*?\{",
    }
    # The chapter's own canonical \section commands are expected. Ignore the
    # first four canonical thematic section commands when checking residue.
    body_without_theme_sections = re.sub(
        r"\\section\{(?:Measure and Integration|Fourier Analysis|Distribution Theory|Sobolev and PDE Methods)\}",
        "",
        text,
    )
    body_without_theme_sections = re.sub(
        r"\\paragraph\{Main-text correspondence\.\}",
        "",
        body_without_theme_sections,
        count=1,
    )

    for name, pat in residue.items():
        n = len(re.findall(pat, body_without_theme_sections))
        if n:
            errors.append(f"legacy residue {name}: {n}")

    if re.search(r"\\begin\{figure\*?\}", text):
        errors.append("source figure environment survived content migration")

    with ledger.open("r", encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f, delimiter="\t"))

    if len(rows) != 25:
        errors.append(f"ledger rows: expected 25, got {len(rows)}")

    non_exact = [
        r.get("companion_problem_id", "")
        for r in rows
        if r.get("resolution_status") != "RESOLVED_EXACT_RANGE"
    ]
    if non_exact:
        errors.append("non-exact source rows: " + ", ".join(non_exact))

    expected_solution_rows = [
        r for r in rows if (r.get("has_solution") or "").upper() == "YES"
    ]
    unresolved_solution_ranges = [
        r.get("companion_problem_id", "")
        for r in expected_solution_rows
        if r.get("solution_resolution_status") != "RESOLVED_EXACT_SOLUTION_RANGE"
    ]
    if unresolved_solution_ranges:
        errors.append(
            "unresolved solution ranges: " + ", ".join(unresolved_solution_ranges)
        )

    reviews = [
        r.get("companion_problem_id", "")
        for r in rows
        if (r.get("generated_status") or "").startswith("REVIEW_REQUIRED")
    ]
    if reviews:
        errors.append("review-required generated rows: " + ", ".join(reviews))

    expected_solutions = len(expected_solution_rows)
    if solutions != expected_solutions:
        errors.append(
            f"solution count mismatch: expected {expected_solutions}, got {solutions}"
        )

    themes = Counter(r.get("thematic_section", "") for r in rows)

    if errors:
        print("COMPANION PART III VALIDATION FAILED")
        for err in errors:
            print("  -", err)
        return 1

    print("COMPANION PART III VALIDATION PASSED")
    print("  atlas units/dispositions:", len(rows))
    print("  reader-facing problems:", len(problems))
    print("  solutions:", solutions)
    print("  editorial holds: 0")
    for theme in THEMES:
        print(f"  {theme}: {themes.get(theme, 0)}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
