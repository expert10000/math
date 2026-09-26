#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
from collections import Counter
from pathlib import Path

EXPECTED_IDS = [f"CP-III-{i:04d}" for i in range(1, 26)]
ALLOWED_STATUS = {"A_STRONG", "B_POLISH", "C_REWRITE", "D_BLOCKING"}
ALLOWED_PRIORITY = {"P0", "P1", "P2", "P3"}
EXPECTED_SOURCE_BACKED = {"CP-III-0006", "CP-III-0016", "CP-III-0023"}
EXPECTED_COUNTS = {
    "A_STRONG": 11,
    "B_POLISH": 8,
    "C_REWRITE": 4,
    "D_BLOCKING": 2,
}

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", required=True, type=Path)
    args = ap.parse_args()
    repo = args.repo.resolve()

    audit = (
        repo / "books" / "companion_problems_solutions" / "metadata"
        / "PART_III_SOLUTION_QUALITY_AUDIT.tsv"
    )
    migration = (
        repo / "books" / "companion_problems_solutions" / "metadata"
        / "PART_III_MIGRATION.tsv"
    )

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
    if len(rows) != 25:
        errors.append(f"audit row count: expected 25, got {len(rows)}")
    if set(ids) != set(EXPECTED_IDS):
        errors.append(
            f"audit ID coverage mismatch: missing={sorted(set(EXPECTED_IDS)-set(ids))}, "
            f"extra={sorted(set(ids)-set(EXPECTED_IDS))}"
        )
    if len(ids) != len(set(ids)):
        errors.append("duplicate Part III IDs in solution-quality audit")

    for r in rows:
        pid = r.get("companion_problem_id", "")
        if r.get("quality_status") not in ALLOWED_STATUS:
            errors.append(f"{pid}: invalid quality_status={r.get('quality_status')!r}")
        if r.get("priority") not in ALLOWED_PRIORITY:
            errors.append(f"{pid}: invalid priority={r.get('priority')!r}")
        if not (r.get("finding") or "").strip():
            errors.append(f"{pid}: missing finding")
        if not (r.get("required_action") or "").strip():
            errors.append(f"{pid}: missing required_action")

    counts = Counter(r.get("quality_status", "") for r in rows)
    for status, expected in EXPECTED_COUNTS.items():
        if counts.get(status, 0) != expected:
            errors.append(
                f"{status}: expected {expected}, got {counts.get(status,0)}"
            )

    with migration.open("r", encoding="utf-8-sig", newline="") as f:
        mrows = list(csv.DictReader(f, delimiter="\t"))
    source_backed = {
        r.get("companion_problem_id", "")
        for r in mrows
        if (r.get("has_solution") or "").upper() == "YES"
    }
    if source_backed != EXPECTED_SOURCE_BACKED:
        errors.append(
            "source-backed set changed: "
            f"expected={sorted(EXPECTED_SOURCE_BACKED)}, actual={sorted(source_backed)}"
        )

    audited_source_backed = {
        r.get("companion_problem_id", "")
        for r in rows
        if r.get("solution_provenance") == "SOURCE_BACKED"
    }
    if audited_source_backed != source_backed:
        errors.append(
            "audit provenance does not match migration ledger: "
            f"audit={sorted(audited_source_backed)}, migration={sorted(source_backed)}"
        )

    p0 = sorted(
        r["companion_problem_id"]
        for r in rows
        if r.get("priority") == "P0"
    )
    if p0 != ["CP-III-0006", "CP-III-0023"]:
        errors.append(f"P0 queue changed unexpectedly: {p0}")

    if errors:
        print("COMPANION PART III SOLUTION-QUALITY AUDIT VALIDATION FAILED")
        for e in errors:
            print("  -", e)
        return 1

    print("COMPANION PART III SOLUTION-QUALITY AUDIT VALIDATION PASSED")
    print("  audited solutions: 25")
    print("  A_STRONG: 11")
    print("  B_POLISH: 8")
    print("  C_REWRITE: 4")
    print("  D_BLOCKING: 2")
    print("  source-backed migrated: 3")
    print("  canonical authored: 22")
    print("  P0 blocking queue: CP-III-0006, CP-III-0023")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
