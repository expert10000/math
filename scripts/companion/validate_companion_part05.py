#!/usr/bin/env python3
from pathlib import Path
import csv, re, sys

chapter = Path(sys.argv[1])
migration = Path(sys.argv[2])
disposition = Path(sys.argv[3])

text = chapter.read_text(encoding="utf-8")
pids = re.findall(r"\\begin\{problem\}\[(CP-V-\d{4})\]", text)
labels = re.findall(r"\\label\{prob:(cp-v-\d{4})\}", text)
solutions = text.count(r"\begin{solution}")

errors = []

expected = [f"CP-V-{i:04d}" for i in range(1, 105)]
if pids != expected:
    errors.append(f"expected continuous CP-V-0001..CP-V-0104, found {len(pids)} IDs")

if solutions != 104:
    errors.append(f"expected 104 solutions, found {solutions}")

if len(labels) != 104:
    errors.append(f"expected 104 labels, found {len(labels)}")

if len(set(labels)) != 104:
    errors.append("duplicate canonical labels found")

with migration.open(encoding="utf-8", newline="") as fh:
    mrows = list(csv.DictReader(fh, delimiter="\t"))
mids = [r["companion_problem_id"] for r in mrows]
if mids != expected:
    errors.append("migration ledger does not match CP-V-0001..CP-V-0104 in order")

with disposition.open(encoding="utf-8", newline="") as fh:
    drows = list(csv.DictReader(fh, delimiter="\t"))

unresolved = [
    r for r in drows
    if r["disposition"] in {"MIGRATE_QUEUE","MIGRATE_QUEUE_UNSOLVED","HOLD_REVIEW"}
]
if unresolved:
    errors.append(f"{len(unresolved)} unresolved disposition rows remain")

valid = set(expected)
bad = []
for r in drows:
    refs = [x.strip() for x in r.get("represented_cps","").split(";") if x.strip()]
    for ref in refs:
        if ref not in valid:
            bad.append((r["problem_id"], ref))
if bad:
    errors.append(f"{len(bad)} invalid represented_cps references")

if errors:
    print("COMPANION PART V VALIDATION FAILED")
    for e in errors:
        print("  -", e)
    raise SystemExit(1)

print("COMPANION PART V RECONCILIATION PASSED")
print("  problems: 104")
print("  solutions: 104")
print("  labels: 104")
print("  migration rows: 104")
print("  disposition rows:", len(drows))
print("  unresolved candidates: 0")
