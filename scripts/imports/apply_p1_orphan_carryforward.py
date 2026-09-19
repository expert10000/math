#!/usr/bin/env python3
from __future__ import annotations
import argparse, csv, shutil
from collections import defaultdict
from pathlib import Path

TERMINAL_NOT_A_PROBLEM="RESOLVED_NOT_A_PROBLEM"

def read_tsv(path):
    with path.open("r",encoding="utf-8-sig",newline="") as f:
        r=csv.DictReader(f,delimiter="\t")
        return list(r.fieldnames or []),[dict(x) for x in r]

def write_tsv(path,fields,rows):
    path.parent.mkdir(parents=True,exist_ok=True)
    with path.open("w",encoding="utf-8",newline="") as f:
        w=csv.DictWriter(f,fieldnames=fields,delimiter="\t",lineterminator="\n",extrasaction="ignore")
        w.writeheader()
        for r in rows:
            w.writerow({k:r.get(k,"") for k in fields})

def extend(fields,extras):
    out=list(fields)
    for x in extras:
        if x not in out: out.append(x)
    return out

def split_ids(s):
    return [x for x in (s or "").split(";") if x]

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--repo",type=Path,required=True)
    ap.add_argument("--apply",action="store_true")
    args=ap.parse_args()

    repo=args.repo.resolve()
    inv=repo/"imports"/"problem_inventory"

    _,priority=read_tsv(inv/"ORPHAN_PRIORITY_RECONCILIATION.tsv")
    lfields,links=read_tsv(inv/"PROBLEM_SOLUTION_LINKS.tsv")
    _,ledger=read_tsv(inv/"PROBLEM_LEDGER.tsv")

    active={r["problem_id"] for r in ledger}

    p1=[r for r in priority if int(r.get("priority") or 99)==1]
    if len(p1)!=4:
        raise SystemExit(f"Expected 4 P1 units, found {len(p1)}")

    links_by_unit=defaultdict(list)
    for s in links:
        uid=s.get("solution_semantic_unit_id","") or s.get("orphan_semantic_unit_id","")
        if uid:
            links_by_unit[uid].append(s)

    # Fallback: group by solution ids if semantic-unit id is absent in links.
    priority_by_solution={}
    _,units=read_tsv(inv/"ORPHAN_SEMANTIC_UNITS.tsv")
    unit_by={r["orphan_semantic_unit_id"]:r for r in units}
    for p in p1:
        u=unit_by.get(p["orphan_semantic_unit_id"],{})
        for sid in split_ids(u.get("member_solution_ids","")):
            priority_by_solution[sid]=p["orphan_semantic_unit_id"]

    decisions=[]
    errors=[]
    remap=[]
    applied_units=set()

    new_lfields=extend(lfields,[
        "previous_linked_problem_id",
        "reconciliation_status",
        "editorial_decision",
        "editorial_rationale",
    ])
    shadow=[]

    for s0 in links:
        s=dict(s0)
        uid=s.get("solution_semantic_unit_id","")
        if not uid:
            uid=priority_by_solution.get(s.get("solution_id",""),"")
        p=next((x for x in p1 if x["orphan_semantic_unit_id"]==uid),None)
        if not p:
            shadow.append(s)
            continue

        pd=p.get("prior_decision","")
        target=p.get("prior_target_problem_id","")
        rationale=p.get("prior_rationale","")

        if pd=="PRIOR_NOT_A_PROBLEM":
            s["linked_problem_id"]=""
            s["candidate_problem_ids"]=""
            s["reconciliation_status"]=TERMINAL_NOT_A_PROBLEM
            s["editorial_decision"]="NOT_A_PROBLEM"
            s["editorial_rationale"]=rationale
            applied_units.add(uid)
        elif pd=="PRIOR_ACCEPT_LINK":
            if target and target in active:
                s["previous_linked_problem_id"]=s.get("linked_problem_id","")
                s["linked_problem_id"]=target
                s["candidate_problem_ids"]=target
                s["reconciliation_status"]="RESOLVED_PRIOR_EDITORIAL_LINK"
                s["editorial_decision"]="ACCEPT_PRIOR_LINK"
                s["editorial_rationale"]=rationale
                applied_units.add(uid)
            else:
                remap.append({
                    "orphan_semantic_unit_id":uid,
                    "solution_id":s.get("solution_id",""),
                    "prior_target_problem_id":target,
                    "current_top1_problem_id":p.get("top1_problem_id",""),
                    "current_top1_score":p.get("top1_score",""),
                    "reason":"PRIOR_TARGET_NOT_ACTIVE",
                })
        else:
            errors.append(f"{uid}: unexpected P1 prior decision {pd}")

        shadow.append(s)

    # Ensure each terminal/accepted unit actually touched at least one link block.
    for p in p1:
        uid=p["orphan_semantic_unit_id"]
        if p.get("prior_decision")=="PRIOR_NOT_A_PROBLEM" and uid not in applied_units:
            errors.append(f"{uid}: no solution-link rows found for terminal disposition")

    # Rebuild remaining orphans / units from shadow, excluding resolved rows.
    active_ids={r["problem_id"] for r in ledger}
    hby={r["problem_id"]:r.get("statement_hash","") for r in ledger}
    rem_rows=[]
    for s in shadow:
        if s.get("linked_problem_id"):
            continue
        status=s.get("reconciliation_status") or s.get("link_status") or "UNRESOLVED"
        if status in {"RESOLVED_NOT_A_PROBLEM","MISSING_COMPANION_STATEMENT","RESOLVED_PRIOR_EDITORIAL_LINK"}:
            continue
        pids=split_ids(s.get("candidate_problem_ids",""))
        hashes=sorted({hby.get(x,"") for x in pids if hby.get(x,"")})
        rem_rows.append({
            "solution_id":s.get("solution_id",""),
            "solution_semantic_unit_id":s.get("solution_semantic_unit_id",""),
            "solution_kind":s.get("solution_kind",""),
            "solution_source_file":s.get("solution_source_file",""),
            "solution_line_range":s.get("solution_line_range",""),
            "source_problem_number":s.get("source_problem_number",""),
            "status":status,
            "candidate_problem_ids":s.get("candidate_problem_ids",""),
            "candidate_statement_hashes":";".join(hashes),
            "editorial_action":"CHOOSE_AMONG_DISTINCT_STATEMENTS" if pids else "LOCATE_COMPANION_STATEMENT_OR_MARK_ORPHAN",
        })

    grouped=defaultdict(list)
    for r in rem_rows:
        key=r.get("solution_semantic_unit_id") or r["solution_id"]
        grouped[key].append(r)
    orphan_units=[]
    for k,m in sorted(grouped.items()):
        pids=sorted({x for r in m for x in split_ids(r["candidate_problem_ids"])})
        hs=sorted({x for r in m for x in split_ids(r["candidate_statement_hashes"])})
        orphan_units.append({
            "orphan_semantic_unit_id":k,
            "member_count":len(m),
            "member_solution_ids":";".join(sorted(r["solution_id"] for r in m)),
            "source_files":";".join(sorted({r["solution_source_file"] for r in m})),
            "statuses":";".join(sorted({r["status"] for r in m})),
            "candidate_problem_ids":";".join(pids),
            "candidate_statement_hashes":";".join(hs),
            "distinct_candidate_statement_count":len(hs),
            "editorial_action":"CHOOSE_AMONG_DISTINCT_STATEMENTS" if hs else "LOCATE_COMPANION_STATEMENT_OR_MARK_ORPHAN",
        })

    # Recompute problem solution flags for accepted links only minimally.
    # We preserve existing ledger content; semantic-unit rebuild will happen in a later consolidation.
    decisions=[]
    for p in p1:
        uid=p["orphan_semantic_unit_id"]
        target=p.get("prior_target_problem_id","")
        if p.get("prior_decision")=="PRIOR_NOT_A_PROBLEM":
            status="RESTORED_NOT_A_PROBLEM"
        elif target in active:
            status="RESTORED_PRIOR_LINK"
        else:
            status="NEEDS_TARGET_REMAP"
        decisions.append({
            "orphan_semantic_unit_id":uid,
            "prior_decision":p.get("prior_decision",""),
            "prior_target_problem_id":target,
            "prior_target_active":"YES" if target in active else ("NO" if target else ""),
            "decision_status":status,
            "current_top1_problem_id":p.get("top1_problem_id",""),
            "current_top1_score":p.get("top1_score",""),
            "rationale":p.get("prior_rationale",""),
        })

    write_tsv(inv/"P1_ORPHAN_CARRYFORWARD_DECISIONS.tsv",
              ["orphan_semantic_unit_id","prior_decision","prior_target_problem_id","prior_target_active",
               "decision_status","current_top1_problem_id","current_top1_score","rationale"],decisions)
    write_tsv(inv/"P1_ORPHAN_TARGET_REMAP_REVIEW.tsv",
              ["orphan_semantic_unit_id","solution_id","prior_target_problem_id",
               "current_top1_problem_id","current_top1_score","reason"],remap)
    write_tsv(inv/"PROBLEM_SOLUTION_LINKS_P1_CARRYFORWARD_SHADOW.tsv",new_lfields,shadow)

    rem_fields=["solution_id","solution_semantic_unit_id","solution_kind","solution_source_file","solution_line_range",
                "source_problem_number","status","candidate_problem_ids","candidate_statement_hashes","editorial_action"]
    unit_fields=["orphan_semantic_unit_id","member_count","member_solution_ids","source_files","statuses",
                 "candidate_problem_ids","candidate_statement_hashes","distinct_candidate_statement_count","editorial_action"]
    write_tsv(inv/"REMAINING_ORPHANS_P1_CARRYFORWARD_SHADOW.tsv",rem_fields,rem_rows)
    write_tsv(inv/"ORPHAN_SEMANTIC_UNITS_P1_CARRYFORWARD_SHADOW.tsv",unit_fields,orphan_units)

    summary=[
        "# P1 orphan carry-forward","",
        f"- Mode: **{'APPLY' if args.apply else 'DRY RUN'}**",
        f"- P1 units: **{len(p1)}**",
        f"- Prior NOT_A_PROBLEM units restored: **{sum(1 for d in decisions if d['decision_status']=='RESTORED_NOT_A_PROBLEM')}**",
        f"- Prior accepted links restored to active exact target: **{sum(1 for d in decisions if d['decision_status']=='RESTORED_PRIOR_LINK')}**",
        f"- Prior accepted links requiring target remap: **{sum(1 for d in decisions if d['decision_status']=='NEEDS_TARGET_REMAP')}**",
        f"- Remaining orphan semantic units after carry-forward: **{len(orphan_units)}**",
        f"- Validation errors: **{len(errors)}**",
        "",
        "No score-only link is applied. Prior accepted links are restored only when the exact prior target remains active."
    ]
    if errors:
        summary += ["","## Validation errors",""]+[f"- {e}" for e in errors]
    (inv/"P1_ORPHAN_CARRYFORWARD_SUMMARY.md").write_text("\n".join(summary)+"\n",encoding="utf-8")

    if errors:
        print("P1 ORPHAN CARRY-FORWARD VALIDATION FAILED")
        for e in errors: print(" -",e)
        return 1

    print(
        f"P1 ORPHAN CARRY-FORWARD DRY RUN PASSED: "
        f"restored_not_problem={sum(1 for d in decisions if d['decision_status']=='RESTORED_NOT_A_PROBLEM')} "
        f"restored_links={sum(1 for d in decisions if d['decision_status']=='RESTORED_PRIOR_LINK')} "
        f"remap={sum(1 for d in decisions if d['decision_status']=='NEEDS_TARGET_REMAP')} "
        f"remaining_units={len(orphan_units)}"
    )
    if not args.apply:
        print("No master files changed.")
        return 0

    for name in ("PROBLEM_SOLUTION_LINKS.tsv","REMAINING_ORPHANS.tsv","ORPHAN_SEMANTIC_UNITS.tsv"):
        src=inv/name
        dst=inv/name.replace(".tsv","_PRE_P1_CARRYFORWARD.tsv")
        if src.exists() and not dst.exists():
            shutil.copy2(src,dst)

    write_tsv(inv/"PROBLEM_SOLUTION_LINKS.tsv",new_lfields,shadow)
    write_tsv(inv/"REMAINING_ORPHANS.tsv",rem_fields,rem_rows)
    write_tsv(inv/"ORPHAN_SEMANTIC_UNITS.tsv",unit_fields,orphan_units)

    print(f"P1 ORPHAN CARRY-FORWARD APPLIED: remaining_units={len(orphan_units)}")
    return 0

if __name__=="__main__":
    raise SystemExit(main())
