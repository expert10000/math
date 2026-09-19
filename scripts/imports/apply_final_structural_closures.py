#!/usr/bin/env python3
from __future__ import annotations
import argparse, csv, shutil
from pathlib import Path

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

    _,target=read_tsv(inv/"LONG_CHILD_RETAINED_TARGETED_REVIEW.tsv")
    _,families=read_tsv(inv/"LONG_CHILD_UNRESOLVED_FAMILIES.tsv")
    lfields,ledger=read_tsv(inv/"PROBLEM_LEDGER.tsv")

    fam_by={r["long_review_family_id"]:r for r in families}
    ledger_by={r["problem_id"]:r for r in ledger}

    # Safe close rules:
    # A) retained CONFIRM_SINGLE_LONG_OBJECT / FINAL_CONFIRM_SINGLE_OBJECT;
    # B) prior RESEGMENT label but targeted pass found no true boundary;
    # C) LCR-001 special case: sole candidate line equals current object's start.
    closable=[]
    retained=[]
    for r in target:
        fid=r["long_review_family_id"]
        action=r["current_action"]
        targeted=r["targeted_review_action"]
        cands=[x for x in (r.get("candidate_boundary_lines") or "").split(";") if x]
        fam=fam_by.get(fid,{})
        range_s=fam.get("source_line_range","")
        start=""
        if range_s.startswith("L") and "-" in range_s:
            start=range_s.split("-",1)[0][1:]

        safe=False
        disposition=""
        rationale=""

        if action=="CONFIRM_SINGLE_LONG_OBJECT" and targeted=="FINAL_CONFIRM_SINGLE_OBJECT":
            safe=True
            disposition="CONFIRMED_SINGLE_LONG_OBJECT"
            rationale="Targeted review found no secondary structural boundary; candidate line is only opening/inspection context."
        elif action=="RESEGMENT_NONSTANDARD_BOUNDARY" and targeted=="KEEP_FOR_MANUAL_REVIEW" and not cands:
            safe=True
            disposition="NO_ACTIONABLE_NONSTANDARD_BOUNDARY"
            rationale="Earlier resegmentation label was not reproduced by targeted review; no internal candidate boundary remains."
        elif action=="RESEGMENT_NONSTANDARD_BOUNDARY" and len(cands)==1 and start and cands[0]==start:
            safe=True
            disposition="OPENING_HEADING_FALSE_BOUNDARY"
            rationale="The only candidate boundary is the current object's own opening line, not a nested sibling object."

        if safe:
            row=dict(r)
            row["closure_disposition"]=disposition
            row["closure_rationale"]=rationale
            closable.append(row)
        else:
            retained.append(r)

    errors=[]
    close_ids=set()
    closure_rows=[]
    for r in closable:
        fid=r["long_review_family_id"]
        fam=fam_by.get(fid)
        if not fam:
            errors.append(f"{fid}: missing unresolved-family metadata")
            continue
        mids=split_ids(fam.get("member_problem_ids","")) or [fam["representative_problem_id"]]
        valid=[]
        for pid in mids:
            lr=ledger_by.get(pid)
            if not lr:
                errors.append(f"{fid}/{pid}: ledger row missing")
                continue
            if lr.get("structural_review_flag")!="LONG_CHILD_REVIEW":
                errors.append(f"{fid}/{pid}: expected LONG_CHILD_REVIEW, got {lr.get('structural_review_flag','')}")
                continue
            valid.append(pid)
            close_ids.add(pid)
        closure_rows.append({
            "long_review_family_id":fid,
            "representative_problem_id":fam["representative_problem_id"],
            "representative_source_file":fam["representative_source_file"],
            "member_count":len(valid),
            "member_problem_ids":";".join(valid),
            "line_span":fam.get("line_span",""),
            "closure_disposition":r["closure_disposition"],
            "closure_rationale":r["closure_rationale"],
        })

    new_fields=extend(lfields,[
        "structural_review_flag",
        "structural_review_disposition",
        "structural_review_rationale",
    ])
    shadow=[]
    close_by_pid={}
    for c in closure_rows:
        for pid in split_ids(c["member_problem_ids"]):
            close_by_pid[pid]=c

    for r0 in ledger:
        r=dict(r0)
        pid=r.get("problem_id","")
        if pid in close_by_pid:
            c=close_by_pid[pid]
            r["structural_review_flag"]=""
            r["structural_review_disposition"]=c["closure_disposition"]
            r["structural_review_rationale"]=c["closure_rationale"]
        shadow.append(r)

    remaining_flags=sum(1 for r in shadow if r.get("structural_review_flag")=="LONG_CHILD_REVIEW")

    write_tsv(
        inv/"FINAL_STRUCTURAL_CLOSURES.tsv",
        ["long_review_family_id","representative_problem_id","representative_source_file",
         "member_count","member_problem_ids","line_span","closure_disposition","closure_rationale"],
        closure_rows
    )
    write_tsv(
        inv/"FINAL_STRUCTURAL_RETAINED_FAMILIES.tsv",
        list(target[0].keys()) if target else [],
        retained
    )
    write_tsv(inv/"PROBLEM_LEDGER_FINAL_STRUCTURAL_CLOSURE_SHADOW.tsv",new_fields,shadow)

    summary=[
        "# Final structural closure","",
        f"- Mode: **{'APPLY' if args.apply else 'DRY RUN'}**",
        f"- Retained targeted-review families before closure: **{len(target)}**",
        f"- Families closed: **{len(closable)}**",
        f"- Ledger rows whose LONG_CHILD_REVIEW flag is cleared: **{len(close_ids)}**",
        f"- Families retained for final review: **{len(retained)}**",
        f"- LONG_CHILD_REVIEW rows remaining after closure: **{remaining_flags}**",
        f"- Validation errors: **{len(errors)}**","",
        "The closure changes review metadata only; statement ranges, hashes, semantic units, and problem/solution links are unchanged.",
        "Only post-solution trim-review cases (or any unexpected non-closable cases) remain."
    ]
    if errors:
        summary += ["","## Validation errors",""]+[f"- {e}" for e in errors]
    (inv/"FINAL_STRUCTURAL_CLOSURE_SUMMARY.md").write_text("\n".join(summary)+"\n",encoding="utf-8")

    if errors:
        print("FINAL STRUCTURAL CLOSURE VALIDATION FAILED")
        for e in errors: print(" -",e)
        return 1

    print(
        f"FINAL STRUCTURAL CLOSURE DRY RUN PASSED: families={len(closable)} "
        f"rows={len(close_ids)} retained={len(retained)} remaining_flags={remaining_flags}"
    )
    if not args.apply:
        print("No master files changed.")
        return 0

    src=inv/"PROBLEM_LEDGER.tsv"
    snap=inv/"PROBLEM_LEDGER_PRE_FINAL_STRUCTURAL_CLOSURE.tsv"
    if not snap.exists():
        shutil.copy2(src,snap)
    write_tsv(inv/"PROBLEM_LEDGER.tsv",new_fields,shadow)

    print(
        f"FINAL STRUCTURAL CLOSURE APPLIED: families={len(closable)} "
        f"rows={len(close_ids)} retained={len(retained)} remaining_flags={remaining_flags}"
    )
    return 0

if __name__=="__main__":
    raise SystemExit(main())
