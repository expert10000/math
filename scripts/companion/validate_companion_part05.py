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
if len(pids) != solutions:
    errors.append(f"problem/solution mismatch: {len(pids)} / {solutions}")
if len(pids) != len(set(pids)):
    errors.append("duplicate problem IDs")
if len(labels) != len(set(labels)):
    errors.append("duplicate labels")
if len(labels) != len(pids):
    errors.append(f"problem/label mismatch: {len(pids)} / {len(labels)}")

expected = [f"CP-V-{i:04d}" for i in range(1, len(pids)+1)]
if pids != expected:
    errors.append("problem IDs are not continuous/in order")

with migration.open(encoding="utf-8", newline="") as fh:
    mrows = list(csv.DictReader(fh, delimiter="\t"))
mids = [r["companion_problem_id"] for r in mrows]
if mids != pids:
    errors.append("migration ledger does not match chapter IDs/order")

with disposition.open(encoding="utf-8", newline="") as fh:
    drows = list(csv.DictReader(fh, delimiter="\t"))
unresolved = [
    r for r in drows
    if r["disposition"] in {"MIGRATE_QUEUE","MIGRATE_QUEUE_UNSOLVED","HOLD_REVIEW"}
]
if unresolved:
    errors.append(f"{len(unresolved)} unresolved disposition rows remain")

if errors:
    print("COMPANION PART V RECONCILIATION FAILED")
    for e in errors:
        print("  -", e)
    raise SystemExit(1)

print("COMPANION PART V RECONCILIATION PASSED")
print("  problems:", len(pids))
print("  solutions:", solutions)
print("  labels:", len(labels))
print("  migration rows:", len(mrows))
print("  disposition rows:", len(drows))
print("  unresolved candidates:", len(unresolved))
