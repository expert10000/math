#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import re
from collections import Counter
from pathlib import Path

ATLAS_FIELDS = [
    "companion_problem_id","semantic_unit_id","representative_problem_id","companion_part",
    "thematic_section","related_volume","related_chapters","related_sections","source_files",
    "source_problem_ids","has_solution","problem_type","difficulty","figure_requirement",
    "figure_type","figure_status","migration_status","editorial_status","notes"
]
VALID_VOLUMES = {"I":"01","II":"02","III":"03","IV":"04","V":"05","VI":"06","VII":"07","VIII":"08"}
VALID_EDITORIAL = {"READY_FOR_COMPANION_MIGRATION","PLACEMENT_REVIEW_REQUIRED"}

def read(path: Path):
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        r = csv.DictReader(f, delimiter="\t")
        return list(r.fieldnames or []), [dict(x) for x in r]

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", type=Path, default=Path.cwd())
    a = ap.parse_args()
    repo = a.repo.resolve()
    inv = repo/"imports"/"problem_inventory"
    base = repo/"books"/"companion_problems_solutions"/"metadata"
    sem = inv/"SEMANTIC_PROBLEM_UNITS.tsv"
    atlas = base/"COMPANION_PROBLEM_ATLAS.tsv"
    review = base/"COMPANION_PLACEMENT_REVIEW.tsv"
    summary = base/"COMPANION_ATLAS_SUMMARY.md"
    errors=[]

    for p in (sem,atlas,review,summary):
        if not p.exists(): errors.append(f"missing required output/input: {p.relative_to(repo)}")
    if errors:
        print("COMPANION ATLAS VALIDATION FAILED")
        for e in errors: print("  -",e)
        return 1

    sf, semrows = read(sem)
    af, rows = read(atlas)
    _, reviewrows = read(review)
    if af != ATLAS_FIELDS:
        errors.append("atlas header differs from scaffold contract")

    sem_id_field = "semantic_problem_id" if "semantic_problem_id" in sf else "semantic_unit_id"
    expected = {r.get(sem_id_field,"") for r in semrows if r.get(sem_id_field,"")}
    actual = {r.get("semantic_unit_id","") for r in rows if r.get("semantic_unit_id","")}

    if len(actual) != len(rows):
        errors.append("duplicate semantic_unit_id in Companion atlas")
    if actual != expected:
        errors.append(f"semantic coverage mismatch: source={len(expected)} atlas={len(actual)} missing={len(expected-actual)} extra={len(actual-expected)}")

    ids = [r.get("companion_problem_id","") for r in rows]
    if len(set(ids)) != len(ids):
        errors.append("duplicate companion_problem_id")
    if any(not re.fullmatch(r"CP-(?:I|II|III|IV|V|VI|VII|VIII)-\d{4}", x) for x in ids):
        errors.append("invalid Companion problem ID format")

    review_ids = {r.get("semantic_unit_id","") for r in reviewrows}
    expected_review = {r.get("semantic_unit_id","") for r in rows if r.get("editorial_status")=="PLACEMENT_REVIEW_REQUIRED"}
    if review_ids != expected_review:
        errors.append(f"placement review mismatch: expected={len(expected_review)} actual={len(review_ids)}")

    for r in rows:
        vol=r.get("related_volume","")
        if vol not in VALID_VOLUMES:
            errors.append(f"{r.get('semantic_unit_id')}: invalid related_volume {vol}")
            continue
        if r.get("companion_part") != VALID_VOLUMES[vol]:
            errors.append(f"{r.get('semantic_unit_id')}: Part/Volume mismatch")
        if not r.get("thematic_section"):
            errors.append(f"{r.get('semantic_unit_id')}: blank thematic_section")
        if not r.get("related_chapters"):
            errors.append(f"{r.get('semantic_unit_id')}: blank related_chapters")
        if r.get("migration_status") != "ATLAS_CLASSIFIED":
            errors.append(f"{r.get('semantic_unit_id')}: unexpected migration_status")
        if r.get("editorial_status") not in VALID_EDITORIAL:
            errors.append(f"{r.get('semantic_unit_id')}: invalid editorial_status {r.get('editorial_status')}")

    if errors:
        print("COMPANION ATLAS VALIDATION FAILED")
        for e in errors[:100]: print("  -",e)
        if len(errors)>100: print(f"  ... {len(errors)-100} more")
        return 1

    counts=Counter(r["related_volume"] for r in rows)
    print("COMPANION ATLAS VALIDATION PASSED")
    print(f"  semantic units: {len(rows)}")
    print(f"  placement review: {len(reviewrows)}")
    for v in ("I","II","III","IV","V","VI","VII","VIII"):
        print(f"  Volume {v}: {counts.get(v,0)}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
