#!/usr/bin/env python3
from __future__ import annotations
import argparse, csv, sys
from collections import defaultdict
from pathlib import Path


def read(path: Path):
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        r=csv.DictReader(f, delimiter="\t"); return list(r.fieldnames or []), [dict(x) for x in r]


def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--repo", type=Path, default=Path.cwd()); a=ap.parse_args()
    inv=a.repo.resolve()/"imports"/"problem_inventory"
    required=["PROBLEM_LEDGER.tsv","PROBLEM_SOLUTION_LINKS.tsv","DUPLICATE_GROUPS.tsv","EXACT_DUPLICATE_COLLAPSE.tsv",
              "SOLUTION_RECONCILIATION.tsv","DETACHED_SOLUTION_RECONCILIATION.tsv","NUMBERING_MISMATCHES.tsv","REMAINING_ORPHANS.tsv","SEMANTIC_PROBLEM_UNITS.tsv","RECONCILIATION_SUMMARY.md"]
    errors=[]
    for n in required:
        if not (inv/n).exists(): errors.append(f"missing output: {n}")
    if errors:
        print("PROBLEM RECONCILIATION VALIDATION FAILED"); [print("  -",e) for e in errors]; return 1
    lf, ledger=read(inv/"PROBLEM_LEDGER.tsv"); sf, links=read(inv/"PROBLEM_SOLUTION_LINKS.tsv"); df, dups=read(inv/"DUPLICATE_GROUPS.tsv"); _, orphans=read(inv/"REMAINING_ORPHANS.tsv"); _, units=read(inv/"SEMANTIC_PROBLEM_UNITS.tsv")
    _, mismatches=read(inv/"NUMBERING_MISMATCHES.tsv"); _, sources=read(inv/"SOURCE_FILES.tsv")
    sha_by_file={r.get("source_file",""):r.get("sha256","") for r in sources if r.get("source_file")}
    ids={r.get("problem_id","") for r in ledger}
    if len(ids)!=len(ledger): errors.append("duplicate problem_id in PROBLEM_LEDGER.tsv")
    for req in ["representative_problem_id","duplicate_role","local_solution_ids","propagated_solution_ids","solution_link_status","reconciliation_status"]:
        if req not in lf: errors.append(f"ledger missing reconciliation field {req}")
    for req in ["reconciliation_status","reconciliation_method","reconciliation_confidence","candidate_problem_ids"]:
        if req not in sf: errors.append(f"solution links missing reconciliation field {req}")
    solution_by_id={r.get("solution_id",""):r for r in links}
    for s in links:
        pid=s.get("linked_problem_id","")
        if pid and pid not in ids: errors.append(f"{s.get('solution_id')}: dangling linked_problem_id {pid}")
        if not s.get("reconciliation_status"): errors.append(f"{s.get('solution_id')}: blank reconciliation_status")
    # Recompute expected solution IDs including duplicate propagation.
    direct=defaultdict(set)
    for s in links:
        if s.get("solution_kind")=="SOLUTION" and s.get("linked_problem_id") in ids:
            direct[s["linked_problem_id"]].add(s["solution_id"])
    by_hash=defaultdict(list)
    for r in ledger: by_hash[r.get("statement_hash","")].append(r)
    group_sols=defaultdict(set)
    for h, rs in by_hash.items():
        for r in rs: group_sols[h].update(direct[r["problem_id"]])
    for r in ledger:
        expected=sorted(group_sols[r.get("statement_hash","")])
        actual=sorted(x for x in r.get("solution_id","").split(";") if x)
        if expected!=actual: errors.append(f"{r['problem_id']}: solution_id does not match reconciled duplicate-group union")
        if (r.get("has_solution")=="YES") != bool(expected): errors.append(f"{r['problem_id']}: has_solution inconsistent with solution_id")
        rep=r.get("representative_problem_id","")
        if rep not in ids: errors.append(f"{r['problem_id']}: invalid representative_problem_id {rep}")
    # Duplicate groups: all members same hash and representative included.
    ledger_by={r['problem_id']:r for r in ledger}
    for d in dups:
        members=[x for x in d.get("problem_ids","").split(";") if x]
        rep=d.get("representative_problem_id","")
        if rep not in members: errors.append(f"{d.get('duplicate_group')}: representative not member")
        hashes={ledger_by[x].get("statement_hash","") for x in members if x in ledger_by}
        if len(hashes)!=1: errors.append(f"{d.get('duplicate_group')}: members do not share one statement hash")
        if len(members)!=int(d.get("member_count") or 0): errors.append(f"{d.get('duplicate_group')}: member_count mismatch")
    expected_unit_count=len({r.get("statement_hash","") for r in ledger if r.get("statement_hash")})
    if len(units)!=expected_unit_count: errors.append(f"SEMANTIC_PROBLEM_UNITS.tsv count mismatch: expected={expected_unit_count} actual={len(units)}")
    unit_hashes={u.get("statement_hash","") for u in units}
    if len(unit_hashes)!=len(units): errors.append("SEMANTIC_PROBLEM_UNITS.tsv contains duplicate statement hashes")
    # Numbering mismatch rows must represent genuine cross-file, non-identical
    # companion candidates. Exact copies belong in duplicate reconciliation.
    for m in mismatches:
        sf=m.get("solution_source_file",""); pf=m.get("candidate_problem_file","")
        if sf == pf:
            errors.append(f"{m.get('mismatch_group','?')}: numbering mismatch self-pair {sf}")
        ssha=sha_by_file.get(sf,""); psha=sha_by_file.get(pf,"")
        if ssha and psha and ssha == psha:
            errors.append(f"{m.get('mismatch_group','?')}: numbering mismatch uses byte-identical files {sf} / {pf}")
        eqs=[x for x in m.get("equivalent_solution_source_files","").split(";") if x]
        eqp=[x for x in m.get("equivalent_candidate_problem_files","").split(";") if x]
        if sf and sf not in eqs:
            errors.append(f"{m.get('mismatch_group','?')}: representative solution file missing from equivalence set")
        if pf and pf not in eqp:
            errors.append(f"{m.get('mismatch_group','?')}: representative problem file missing from equivalence set")
        if eqs:
            vals={sha_by_file.get(x,"") or f"PATH:{x}" for x in eqs}
            if len(vals) != 1:
                errors.append(f"{m.get('mismatch_group','?')}: solution equivalence set is not exact-copy consistent")
        if eqp:
            vals={sha_by_file.get(x,"") or f"PATH:{x}" for x in eqp}
            if len(vals) != 1:
                errors.append(f"{m.get('mismatch_group','?')}: problem equivalence set is not exact-copy consistent")

    unresolved_ids={s["solution_id"] for s in links if not s.get("linked_problem_id")}
    reported_ids={r.get("solution_id","") for r in orphans}
    if unresolved_ids!=reported_ids:
        errors.append(f"REMAINING_ORPHANS.tsv mismatch: unresolved={len(unresolved_ids)} reported={len(reported_ids)}")
    if errors:
        print("PROBLEM RECONCILIATION VALIDATION FAILED")
        for e in errors[:100]: print("  -",e)
        if len(errors)>100: print(f"  ... {len(errors)-100} more")
        return 1
    print("PROBLEM RECONCILIATION VALIDATION PASSED")
    print(f"  ledger rows: {len(ledger)}")
    print(f"  solution/hint links: {len(links)}")
    print(f"  exact duplicate groups: {len(dups)}")
    print(f"  semantic problem units: {len(units)}")
    print(f"  remaining explicit orphans: {len(orphans)}")
    return 0

if __name__=="__main__": raise SystemExit(main())
