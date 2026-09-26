#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import re
from collections import Counter
from pathlib import Path

ALLOWED_STATUS = {"A_STRONG", "B_POLISH", "C_REWRITE", "D_BLOCKING"}
ALLOWED_PRIORITY = {"P0", "P1", "P2", "P3"}

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", required=True, type=Path)
    args = ap.parse_args()
    repo = args.repo.resolve()

    base = repo / "books" / "companion_problems_solutions"
    chapter = base / "chapters" / "part02_volume_ii" / "chapter.tex"
    migration = base / "metadata" / "PART_II_MIGRATION.tsv"
    audit = base / "metadata" / "PART_II_SOLUTION_QUALITY_AUDIT.tsv"
    standard = base / "metadata" / "COMPANION_SOLUTION_EDITORIAL_STANDARD.md"

    errors = []
    for p in (chapter, migration, audit, standard):
        if not p.exists():
            errors.append(f"missing required file: {p}")
    if errors:
        print("COMPANION PART II SOLUTION-QUALITY AUDIT VALIDATION FAILED")
        for e in errors:
            print("  -", e)
        return 1

    text = chapter.read_text(encoding="utf-8")
    ids = re.findall(r"\\begin\{problem\}\[(CP-II-\d{4})\]", text)

    with audit.open("r", encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f, delimiter="\t"))
    audit_ids = [r.get("companion_problem_id","") for r in rows]

    if len(ids) != 570:
        errors.append(f"reader-facing problem count: expected 570, got {len(ids)}")
    if len(rows) != 570:
        errors.append(f"audit row count: expected 570, got {len(rows)}")
    if set(audit_ids) != set(ids):
        errors.append(
            f"audit ID coverage mismatch: missing={len(set(ids)-set(audit_ids))} "
            f"extra={len(set(audit_ids)-set(ids))}"
        )
    if len(audit_ids) != len(set(audit_ids)):
        errors.append("duplicate IDs in quality audit")

    for r in rows:
        pid = r.get("companion_problem_id","")
        if r.get("quality_status") not in ALLOWED_STATUS:
            errors.append(f"{pid}: invalid quality_status")
        if r.get("priority") not in ALLOWED_PRIORITY:
            errors.append(f"{pid}: invalid priority")
        if not (r.get("finding") or "").strip():
            errors.append(f"{pid}: missing finding")
        if not (r.get("required_action") or "").strip():
            errors.append(f"{pid}: missing required_action")

    with migration.open("r", encoding="utf-8-sig", newline="") as f:
        mrows = list(csv.DictReader(f, delimiter="\t"))
    source_backed = {
        r.get("companion_problem_id","")
        for r in mrows
        if (r.get("solution_status") or "").startswith("MIGRATED_PRIMARY_SOLUTION")
    }
    audited_source_backed = {
        r.get("companion_problem_id","")
        for r in rows
        if r.get("solution_provenance") == "SOURCE_BACKED"
    }
    if len(source_backed) != 165:
        errors.append(
            f"migration ledger source-backed count: expected 165, got {len(source_backed)}"
        )
    if audited_source_backed != source_backed:
        errors.append(
            f"source-backed provenance mismatch: audit={len(audited_source_backed)} "
            f"migration={len(source_backed)}"
        )

    canonical_authored = {
        r.get("companion_problem_id","")
        for r in rows
        if r.get("solution_provenance") == "CANONICAL_AUTHORED"
    }
    if len(canonical_authored) != 405:
        errors.append(
            f"canonical-authored audit count: expected 405, got {len(canonical_authored)}"
        )

    if errors:
        print("COMPANION PART II SOLUTION-QUALITY AUDIT VALIDATION FAILED")
        for e in errors[:100]:
            print("  -", e)
        if len(errors) > 100:
            print(f"  ... {len(errors)-100} more")
        return 1

    counts = Counter(r["quality_status"] for r in rows)
    pcounts = Counter(r["priority"] for r in rows)
    print("COMPANION PART II SOLUTION-QUALITY AUDIT VALIDATION PASSED")
    print("  audited pairs: 570")
    print("  source-backed: 165")
    print("  canonical-authored: 405")
    print(f"  A_STRONG: {counts.get('A_STRONG',0)}")
    print(f"  B_POLISH: {counts.get('B_POLISH',0)}")
    print(f"  C_REWRITE: {counts.get('C_REWRITE',0)}")
    print(f"  D_BLOCKING: {counts.get('D_BLOCKING',0)}")
    print(
        "  P0/P1/P2/P3: "
        f"{pcounts.get('P0',0)}/{pcounts.get('P1',0)}/"
        f"{pcounts.get('P2',0)}/{pcounts.get('P3',0)}"
    )
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
