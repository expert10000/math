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
expected = {f"CP-V-{i:04d}" for i in range(1,115)}

if len(pids) != 114:
    errors.append(f"expected 114 problems, found {len(pids)}")
if set(pids) != expected:
    missing = sorted(expected - set(pids))
    extra = sorted(set(pids) - expected)
    errors.append(f"problem ID set mismatch; missing={missing[:10]} extra={extra[:10]}")
if len(pids) != len(set(pids)):
    errors.append("duplicate problem IDs")
if solutions != 114:
    errors.append(f"expected 114 solutions, found {solutions}")
if len(labels) != 114 or len(set(labels)) != 114:
    errors.append(f"label count/uniqueness failure: {len(labels)}")
for pid in pids:
    if pid.lower() not in labels:
        errors.append(f"missing canonical label for {pid}")

with migration.open(encoding="utf-8", newline="") as fh:
    mrows = list(csv.DictReader(fh, delimiter="\t"))
mids = [r["companion_problem_id"] for r in mrows]
if len(mrows) != 114 or set(mids) != expected:
    errors.append("migration ledger does not contain exactly CP-V-0001..CP-V-0114")

# exact chapter coverage
counts = {f"V/{i:02d}":0 for i in range(1,29)}
for r in mrows:
    ch = r["target_chapter"]
    if ch in counts:
        counts[ch] += 1
    else:
        errors.append(f"non-exact target chapter remains: {r['companion_problem_id']} -> {ch}")
sparse = {k:v for k,v in counts.items() if v < 2}
if sparse:
    errors.append(f"chapters below minimum coverage: {sparse}")

with disposition.open(encoding="utf-8", newline="") as fh:
    drows = list(csv.DictReader(fh, delimiter="\t"))
unresolved = [
    r for r in drows
    if r["disposition"] in {"MIGRATE_QUEUE","MIGRATE_QUEUE_UNSOLVED","HOLD_REVIEW"}
]
if unresolved:
    errors.append(f"{len(unresolved)} unresolved source-disposition rows remain")

if errors:
    print("COMPANION PART V VALIDATION FAILED")
    for e in errors:
        print("  -", e)
    raise SystemExit(1)

print("COMPANION PART V VALIDATION PASSED")
print("  problems: 114")
print("  solutions: 114")
print("  labels: 114")
print("  migration rows: 114")
print("  disposition rows:", len(drows))
print("  unresolved source candidates: 0")
print("  exact chapter mappings: 114")
print("  chapters with <2 problems: 0")
