#!/usr/bin/env python3
from __future__ import annotations
import argparse, csv, shutil
from collections import Counter
from pathlib import Path

SAFE_DIAGNOSES={
    "NESTED_SUBEXAMPLES_OR_SUBOBJECTS",
    "LONG_OBJECT_PLUS_EXPOSITION",
    "LONG_SINGLE_PROBLEM_WITH_SOLUTION",
}
SOURCE_REVIEWED_NESTED_FAMILIES={
    "PRF-014": "Nested 'Example at the north pole' is a local tangent-space illustration inside the same differential-geometry exposition.",
    "PRF-045": "Nested Example A/B/C and Green-function examples are worked illustrations inside the same analysis exposition, not sibling problems.",
    "PRF-036": "Nested paragraph Example is an illustrative calculation inside the same analysis object, not a sibling problem.",
}
UNSAFE_DIAGNOSES={
    "MISSED_SIBLING_OBJECTS",
    "POST_SOLUTION_EMBEDDED_OBJECTS",
    "LONG_SINGLE_OBJECT_NO_TERMINAL",
}

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
        if x not in out:out.append(x)
    return out

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--repo",type=Path,required=True)
    ap.add_argument("--apply",action="store_true")
    args=ap.parse_args()

    repo=args.repo.resolve()
    inv=repo/"imports"/"problem_inventory"
    afields,audit=read_tsv(inv/"LONG_CHILD_REVIEW_AUDIT.tsv")
    lfields,ledger=read_tsv(inv/"PROBLEM_LEDGER.tsv")

    audit_by={r["problem_id"]:r for r in audit}
    current=[r for r in ledger if r.get("structural_review_flag")=="LONG_CHILD_REVIEW"]

    decisions=[]
    unresolved=[]
    errors=[]
    clear_ids=set()

    for row in current:
        pid=row["problem_id"]
        a=audit_by.get(pid)
        if not a:
            errors.append(f"{pid}: no LONG_CHILD_REVIEW_AUDIT row")
            continue
        diag=a.get("diagnosis","")
        fid=a.get("risk_family_id","")
        if fid in SOURCE_REVIEWED_NESTED_FAMILIES:
            disposition="CONFIRMED_SINGLE_OBJECT_WITH_NESTED_EXAMPLES"
            rationale=SOURCE_REVIEWED_NESTED_FAMILIES[fid]
            clear=True
        elif diag in SAFE_DIAGNOSES:
            disposition="CONFIRMED_SINGLE_LONG_OBJECT"
            rationale=f"Audit diagnosis {diag} does not indicate a sibling problem boundary."
            clear=True
        else:
            disposition="RETAIΝ_LONG_CHILD_REVIEW"
            rationale=f"Audit diagnosis {diag} requires targeted/manual review."
            clear=False

        d={
            "problem_id":pid,
            "risk_family_id":fid,
            "source_file":row.get("source_file",""),
            "source_line_range":row.get("source_line_range",""),
            "line_span":a.get("line_span",""),
            "diagnosis":diag,
            "disposition":disposition,
            "clear_review_flag":"YES" if clear else "NO",
            "rationale":rationale,
        }
        decisions.append(d)
        if clear:
            clear_ids.add(pid)
        else:
            unresolved.append(d)

    new_fields=extend(lfields,[
        "structural_review_flag",
        "structural_review_disposition",
        "structural_review_rationale",
    ])
    shadow=[]
    for r0 in ledger:
        r=dict(r0)
        pid=r.get("problem_id","")
        if pid in clear_ids:
            d=next(x for x in decisions if x["problem_id"]==pid)
            r["structural_review_flag"]=""
            r["structural_review_disposition"]=d["disposition"]
            r["structural_review_rationale"]=d["rationale"]
            # Keep existing structural_status; this is a review closure, not a new segmentation.
        shadow.append(r)

    write_tsv(
        inv/"LONG_CHILD_REVIEW_DISPOSITIONS.tsv",
        ["problem_id","risk_family_id","source_file","source_line_range","line_span",
         "diagnosis","disposition","clear_review_flag","rationale"],
        decisions,
    )
    write_tsv(
        inv/"LONG_CHILD_REVIEW_UNRESOLVED.tsv",
        ["problem_id","risk_family_id","source_file","source_line_range","line_span",
         "diagnosis","disposition","clear_review_flag","rationale"],
        unresolved,
    )
    write_tsv(inv/"PROBLEM_LEDGER_LONG_CHILD_DISPOSITION_SHADOW.tsv",new_fields,shadow)

    c=Counter(d["diagnosis"] for d in decisions)
    summary=[
        "# Long-child review dispositions","",
        f"- Mode: **{'APPLY' if args.apply else 'DRY RUN'}**",
        f"- Current LONG_CHILD_REVIEW rows: **{len(current)}**",
        f"- Review flags cleared: **{len(clear_ids)}**",
        f"- Review flags retained: **{len(unresolved)}**",
        f"- Validation errors: **{len(errors)}**","",
        "## Diagnosis counts",
    ]
    for k,v in sorted(c.items()):
        summary.append(f"- {k}: **{v}**")
    summary += ["",
        "Clearing a flag does not alter statement ranges, hashes, semantic units, or solution links.",
        "Unsafe/ambiguous diagnoses remain flagged for later targeted review."
    ]
    if errors:
        summary += ["","## Validation errors",""]+[f"- {e}" for e in errors]
    (inv/"LONG_CHILD_REVIEW_DISPOSITION_SUMMARY.md").write_text("\n".join(summary)+"\n",encoding="utf-8")

    if errors:
        print("LONG CHILD DISPOSITION VALIDATION FAILED")
        for e in errors:print(" -",e)
        return 1

    print(f"LONG CHILD DISPOSITION DRY RUN PASSED: current={len(current)} cleared={len(clear_ids)} retained={len(unresolved)}")
    if not args.apply:
        print("No master files changed.")
        return 0

    src=inv/"PROBLEM_LEDGER.tsv"
    snap=inv/"PROBLEM_LEDGER_PRE_LONG_CHILD_DISPOSITIONS.tsv"
    if not snap.exists():
        shutil.copy2(src,snap)
    write_tsv(inv/"PROBLEM_LEDGER.tsv",new_fields,shadow)
    print(f"LONG CHILD DISPOSITIONS APPLIED: cleared={len(clear_ids)} retained={len(unresolved)}")
    return 0

if __name__=="__main__":
    raise SystemExit(main())
