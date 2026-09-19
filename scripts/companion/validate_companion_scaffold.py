#!/usr/bin/env python3
from __future__ import annotations
import argparse, csv, re
from pathlib import Path

EXPECTED = [
    ("01","I","I/01--I/18"),
    ("02","II","II/01--II/25"),
    ("03","III","III/01--III/28"),
    ("04","IV","IV/01--IV/31"),
    ("05","V","V/01--V/28"),
    ("06","VI","VI/01--VI/49"),
    ("07","VII","VII/01--VII/42"),
    ("08","VIII","VIII/01--VIII/35"),
]
ATLAS_FIELDS = [
    "companion_problem_id","semantic_unit_id","representative_problem_id","companion_part",
    "thematic_section","related_volume","related_chapters","related_sections","source_files",
    "source_problem_ids","has_solution","problem_type","difficulty","figure_requirement",
    "figure_type","figure_status","migration_status","editorial_status","notes"
]

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", type=Path, default=Path.cwd())
    a = ap.parse_args()
    repo = a.repo.resolve()
    base = repo / "books" / "companion_problems_solutions"
    errors = []

    required = [
        base/"book.tex", base/"README.md", base/"BUILD_WINDOWS.ps1",
        base/"frontmatter"/"publication-and-scope.tex",
        base/"frontmatter"/"how-to-use-companion.tex",
        base/"frontmatter"/"problem-reference-convention.tex",
        base/"backmatter"/"integration-notes.tex",
        base/"metadata"/"COMPANION_PROBLEM_ATLAS.tsv",
        base/"metadata"/"COMPANION_PART_MAP.tsv",
        base/"figures"/"README.md",
    ]
    for p in required:
        if not p.exists():
            errors.append(f"missing required file: {p.relative_to(repo)}")

    for num, roman, _ in EXPECTED:
        p = base/"chapters"/f"part{num}_volume_{roman.lower()}"/"chapter.tex"
        if not p.exists():
            errors.append(f"missing Part chapter: {p.relative_to(repo)}")

    if errors:
        print("COMPANION SCAFFOLD VALIDATION FAILED")
        for e in errors: print("  -", e)
        return 1

    book = (base/"book.tex").read_text(encoding="utf-8")
    if len(re.findall(r"\\part\{", book)) != 8:
        errors.append("book.tex must contain exactly 8 Part declarations")
    if len(re.findall(r"\\include\{chapters/part\d\d_volume_", book)) != 8:
        errors.append("book.tex must contain exactly 8 Part chapter includes")

    with (base/"metadata"/"COMPANION_PROBLEM_ATLAS.tsv").open("r", encoding="utf-8-sig", newline="") as f:
        r = csv.DictReader(f, delimiter="\t")
        if list(r.fieldnames or []) != ATLAS_FIELDS:
            errors.append("COMPANION_PROBLEM_ATLAS.tsv header does not match the canonical scaffold schema")
        if list(r):
            errors.append("COMPANION_PROBLEM_ATLAS.tsv must be header-only in the scaffold commit")

    with (base/"metadata"/"COMPANION_PART_MAP.tsv").open("r", encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f, delimiter="\t"))
    if len(rows) != 8:
        errors.append(f"COMPANION_PART_MAP.tsv expected 8 rows, found {len(rows)}")
    else:
        for row, (num, roman, rng) in zip(rows, EXPECTED):
            if row.get("companion_part") != num or row.get("related_volume") != roman or row.get("canonical_chapter_range") != rng:
                errors.append(f"invalid Part map row for expected Part {num} / Volume {roman}")

    forbidden = re.compile(r"\b(TODO|FIXME|TBD|PLACEHOLDER)\b", re.I)
    for p in base.rglob("*.tex"):
        txt = p.read_text(encoding="utf-8")
        if forbidden.search(txt):
            errors.append(f"forbidden unfinished marker in {p.relative_to(repo)}")

    if errors:
        print("COMPANION SCAFFOLD VALIDATION FAILED")
        for e in errors: print("  -", e)
        return 1

    print("COMPANION SCAFFOLD VALIDATION PASSED")
    print("  Parts: 8")
    print("  Main-volume correspondence: I--VIII")
    print("  Atlas rows: 0 (header-only scaffold)")
    print("  Reader structure: thematic sections with textual main-chapter references")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
