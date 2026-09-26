#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
from collections import Counter
from pathlib import Path

EXPECTED_IDS = [f"CP-III-{i:04d}" for i in range(1, 26)]
ALLOWED_STATUS = {"A_STRONG", "B_POLISH", "C_REWRITE", "D_BLOCKING"}
EXPECTED_COUNTS = {"A_STRONG": 17, "B_POLISH": 8, "C_REWRITE": 0, "D_BLOCKING": 0}
EXPECTED_SOURCE_BACKED = {"CP-III-0006", "CP-III-0016", "CP-III-0023"}

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", required=True, type=Path)
    args = ap.parse_args()
    repo = args.repo.resolve()

    audit = repo / "books" / "companion_problems_solutions" / "metadata" / "PART_III_SOLUTION_QUALITY_AUDIT.tsv"
    migration = repo / "books" / "companion_problems_solutions" / "metadata" / "PART_III_MIGRATION.tsv"

    errors = []
    for p in (audit, migration):
        if not p.exists():
            errors.append(f"missing required file: {p}")
    if errors:
        print("COMPANION PART III SOLUTION-QUALITY AUDIT VALIDATION FAILED")
        for e in errors:
            print("  -", e)
        return 1

    with audit.open("r", encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f, delimiter="\t"))
    ids = [r.get("companion_problem_id", "") for r in rows]

    if len(rows) != 25 or set(ids) != set(EXPECTED_IDS):
        errors.append("audit must contain exactly the 25 canonical Part III IDs")
    if len(ids) != len(set(ids)):
        errors.append("duplicate IDs in audit")

    counts = Counter(r.get("quality_status", "") for r in rows)
    for status, expected in EXPECTED_COUNTS.items():
        if counts.get(status, 0) != expected:
            errors.append(f"{status}: expected {expected}, got {counts.get(status,0)}")

    p0 = [r["companion_problem_id"] for r in rows if r.get("priority") == "P0"]
    p1 = [r["companion_problem_id"] for r in rows if r.get("priority") == "P1"]
    if p0:
        errors.append(f"P0 queue not empty: {p0}")
    if p1:
        errors.append(f"P1 queue not empty: {p1}")

    with migration.open("r", encoding="utf-8-sig", newline="") as f:
        mrows = list(csv.DictReader(f, delimiter="\t"))
    source_backed = {
        r.get("companion_problem_id", "")
        for r in mrows
        if (r.get("has_solution") or "").upper() == "YES"
    }
    if source_backed != EXPECTED_SOURCE_BACKED:
        errors.append(
            f"source-backed provenance changed: {sorted(source_backed)}"
        )

    audited_source_backed = {
        r.get("companion_problem_id", "")
        for r in rows
        if r.get("solution_provenance") == "SOURCE_BACKED"
    }
    if audited_source_backed != source_backed:
        errors.append(
            f"audit provenance mismatch: {sorted(audited_source_backed)}"
        )

    if errors:
        print("COMPANION PART III SOLUTION-QUALITY AUDIT VALIDATION FAILED")
        for e in errors:
            print("  -", e)
        return 1

    print("COMPANION PART III SOLUTION-QUALITY AUDIT VALIDATION PASSED")
    print("  audited solutions: 25")
    print("  A_STRONG: 17")
    print("  B_POLISH: 8")
    print("  C_REWRITE: 0")
    print("  D_BLOCKING: 0")
    print("  P0/P1 queues: empty")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
