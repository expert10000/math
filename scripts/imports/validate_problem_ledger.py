#!/usr/bin/env python3
"""Validate structural invariants of imports/problem_inventory/PROBLEM_LEDGER.tsv."""
from __future__ import annotations
import argparse
import csv
import re
import sys
from collections import Counter
from pathlib import Path

REQUIRED = [
    "problem_id", "source_id", "source_collection", "source_file", "source_location",
    "source_line_range", "problem_type", "statement_hash", "migration_status", "review_status",
]
LINE_RE = re.compile(r"^L(\d+)-L(\d+)$")


def read_tsv(path: Path):
    with path.open("r", encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f, delimiter="\t"))


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", type=Path, default=Path.cwd())
    args = ap.parse_args()
    repo = args.repo.resolve()
    base = repo / "imports" / "problem_inventory"
    ledger = base / "PROBLEM_LEDGER.tsv"
    sources = base / "SOURCE_FILES.tsv"
    links = base / "PROBLEM_SOLUTION_LINKS.tsv"
    dups = base / "DUPLICATE_GROUPS.tsv"
    detached = base / "DETACHED_SOLUTION_ITEMS.tsv"
    rejected = base / "REJECTED_STRUCTURAL_ITEMS.tsv"

    missing_files = [p for p in (ledger, sources, links, dups, detached, rejected) if not p.exists()]
    if missing_files:
        for p in missing_files:
            print(f"ERROR missing: {p}")
        return 2

    rows = read_tsv(ledger)
    source_rows = read_tsv(sources)
    link_rows = read_tsv(links)
    detached_rows = read_tsv(detached)
    rejected_rows = read_tsv(rejected)
    errors = []

    if not rows:
        errors.append("ledger contains zero rows")
    if rows:
        for col in REQUIRED:
            if col not in rows[0]:
                errors.append(f"missing required column: {col}")

    ids = [r.get("problem_id", "") for r in rows]
    for pid, n in Counter(ids).items():
        if not pid:
            errors.append("blank problem_id")
        elif n > 1:
            errors.append(f"duplicate problem_id: {pid} ({n})")

    source_ids = {r.get("source_id", "") for r in source_rows}
    for r in rows:
        pid = r.get("problem_id", "<blank>")
        if r.get("source_id") not in source_ids:
            errors.append(f"{pid}: dangling source_id {r.get('source_id')}")
        m = LINE_RE.match(r.get("source_line_range", ""))
        if not m or int(m.group(1)) > int(m.group(2)):
            errors.append(f"{pid}: invalid source_line_range {r.get('source_line_range')!r}")
        if not r.get("statement_hash"):
            errors.append(f"{pid}: blank statement_hash")
        if not r.get("migration_status"):
            errors.append(f"{pid}: blank migration_status")
        if not r.get("review_status"):
            errors.append(f"{pid}: blank review_status")

    row_ids = set(ids)
    detached_ids = {r.get("problem_id", "") for r in detached_rows}
    rejected_ids = {r.get("problem_id", "") for r in rejected_rows}
    overlap = (row_ids & detached_ids) | (row_ids & rejected_ids) | (detached_ids & rejected_ids)
    for pid in sorted(x for x in overlap if x):
        errors.append(f"structural classification overlap for problem_id: {pid}")

    solution_ids = {lr.get("solution_id", "") for lr in link_rows}
    for lr in link_rows:
        pid = lr.get("linked_problem_id", "")
        if pid and pid not in row_ids:
            errors.append(f"solution {lr.get('solution_id')}: dangling linked_problem_id {pid}")
    for dr in detached_rows:
        for sid in filter(None, dr.get("linked_solution_ids", "").split(";")):
            if sid not in solution_ids:
                errors.append(f"detached marker {dr.get('problem_id')}: dangling solution_id {sid}")

    if errors:
        print("PROBLEM LEDGER VALIDATION FAILED")
        for e in errors[:200]:
            print(f"  - {e}")
        if len(errors) > 200:
            print(f"  ... {len(errors)-200} more")
        return 1

    print("PROBLEM LEDGER VALIDATION PASSED")
    print(f"  rows: {len(rows)}")
    print(f"  sources: {len(source_rows)}")
    print(f"  solution/hint links: {len(link_rows)}")
    print(f"  detached solution headings: {len(detached_rows)}")
    print(f"  rejected structural markers: {len(rejected_rows)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
