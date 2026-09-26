#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
from pathlib import Path

EXPECTED_IDS = [f"CP-III-{i:04d}" for i in range(1, 26)]
EXPECTED_SOURCE_BACKED = {"CP-III-0006", "CP-III-0016", "CP-III-0023"}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", required=True, type=Path)
    args = ap.parse_args()
    repo = args.repo.resolve()

    audit = repo / "books" / "companion_problems_solutions" / "metadata" / "PART_III_SOLUTION_QUALITY_AUDIT.tsv"
    migration = repo / "books" / "companion_problems_solutions" / "metadata" / "PART_III_MIGRATION.tsv"

    errors: list[str] = []
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
        errors.append("duplicate IDs in Part III quality audit")

    non_strong = [
        r.get("companion_problem_id", "")
        for r in rows
        if r.get("quality_status") != "A_STRONG"
    ]
    if non_strong:
        errors.append("non-A_STRONG rows remain: " + ", ".join(non_strong))

    non_p3 = [
        r.get("companion_problem_id", "")
        for r in rows
        if r.get("priority") != "P3"
    ]
    if non_p3:
        errors.append("non-P3 editorial rows remain: " + ", ".join(non_p3))

    with migration.open("r", encoding="utf-8-sig", newline="") as f:
        mrows = list(csv.DictReader(f, delimiter="\t"))
    source_backed = {
        r.get("companion_problem_id", "")
        for r in mrows
        if (r.get("has_solution") or "").upper() == "YES"
    }
    if source_backed != EXPECTED_SOURCE_BACKED:
        errors.append(
            "source-backed provenance changed: " + repr(sorted(source_backed))
        )

    audited_source_backed = {
        r.get("companion_problem_id", "")
        for r in rows
        if r.get("solution_provenance") == "SOURCE_BACKED"
    }
    if audited_source_backed != source_backed:
        errors.append(
            "audit provenance does not match migration ledger: "
            + repr(sorted(audited_source_backed))
        )

    if errors:
        print("COMPANION PART III SOLUTION-QUALITY AUDIT VALIDATION FAILED")
        for e in errors:
            print("  -", e)
        return 1

    print("COMPANION PART III SOLUTION-QUALITY AUDIT VALIDATION PASSED")
    print("  audited solutions: 25")
    print("  A_STRONG: 25")
    print("  B_POLISH: 0")
    print("  C_REWRITE: 0")
    print("  D_BLOCKING: 0")
    print("  P0/P1/P2 queues: empty")
    print("  source-backed migrated: 3")
    print("  canonical authored: 22")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
