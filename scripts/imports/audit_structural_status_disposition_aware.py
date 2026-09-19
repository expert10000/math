#!/usr/bin/env python3
from __future__ import annotations
import argparse, csv, re
from collections import Counter, defaultdict
from pathlib import Path

LINE_RANGE_RE=re.compile(r"L?(\d+)\s*-\s*L?(\d+)")
COMMENT_RE=re.compile(r"(?<!\\)%.*$")
HEAD_RE=re.compile(r"^\s*\\(?:section|subsection|subsubsection)\*?\{(?P<title>[^{}]+)\}\s*$",re.I)
OBJ_RE=re.compile(r"^\s*(Problem|Exercise|Example|Question|Task|Challenge)\b",re.I)

# These metadata states mean the row has already been explicitly reviewed and
# accepted as a single object despite mechanical heading/length heuristics.
SAFE_STATUSES={
    "ACTIVE_SINGLE_OBJECT_CONFIRMED",
}
SAFE_REVIEW_DISPOSITIONS={
    "CONFIRMED_SINGLE_LONG_OBJECT",
    "CONFIRMED_SINGLE_OBJECT_WITH_NESTED_EXAMPLES",
    "NO_ACTIONABLE_NONSTANDARD_BOUNDARY",
    "OPENING_HEADING_FALSE_BOUNDARY",
    "RECONCILED_PREVIOUSLY_APPROVED_CLOSURE",
    "TRIMMED_POST_SOLUTION_EXPOSITION",
}
SAFE_REVIEW_FLAGS={
    "NO_SPLIT_EDITORIAL_DISPOSITION",
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
        for row in rows:
            w.writerow({k:row.get(k,"") for k in fields})

def parse_range(s):
    m=LINE_RANGE_RE.search(s or "")
    return (int(m.group(1)),int(m.group(2))) if m else None

def safe_lines(path):
    for enc in ("utf-8-sig","utf-8","cp1252","latin-1"):
        try:return path.read_text(encoding=enc).splitlines()
        except UnicodeDecodeError:pass
    return path.read_text(encoding="utf-8",errors="replace").splitlines()

def strip_comment(s): return COMMENT_RE.sub("",s)

def count_internal_heads(lines,a,b):
    n=0
    for i in range(a,b+1):
        m=HEAD_RE.match(strip_comment(lines[i-1]))
        if m and OBJ_RE.match(m.group("title").strip()):
            n+=1
    return n

def accepted_by_disposition(r):
    if r.get("structural_status","") in SAFE_STATUSES:
        return True
    if r.get("structural_review_disposition","") in SAFE_REVIEW_DISPOSITIONS:
        return True
    if r.get("structural_review_flag","") in SAFE_REVIEW_FLAGS:
        return True
    return False

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--repo",type=Path,required=True)
    args=ap.parse_args()

    repo=args.repo.resolve()
    inv=repo/"imports"/"problem_inventory"
    srcroot=repo/"imports"/"ALL_TEX_AND_FIGURES"/"tex"

    _,ledger=read_tsv(inv/"PROBLEM_LEDGER.tsv")
    _,links=read_tsv(inv/"PROBLEM_SOLUTION_LINKS.tsv")
    _,orphans=read_tsv(inv/"ORPHAN_SEMANTIC_UNITS.tsv")

    actionable=[]
    dispositioned=[]
    raw_multi=0
    actionable_multi=0
    raw_long120=raw_long250=raw_long500=0
    act_long120=act_long250=act_long500=0

    for r in ledger:
        rr=parse_range(r.get("source_line_range",""))
        if not rr: continue
        span=rr[1]-rr[0]+1
        src=r.get("source_file","")
        p=srcroot/src
        heads=0
        if p.exists():
            lines=safe_lines(p)
            heads=count_internal_heads(lines,*rr)

        if span>=120: raw_long120+=1
        if span>=250: raw_long250+=1
        if span>=500: raw_long500+=1
        if heads>=2: raw_multi+=1

        flags=[]
        if span>=500: flags.append("SPAN_GE_500")
        elif span>=250: flags.append("SPAN_GE_250")
        elif span>=120: flags.append("SPAN_GE_120")
        if heads>=2: flags.append("MULTIPLE_INTERNAL_OBJECT_HEADINGS")
        if not flags: continue

        row={
            "problem_id":r.get("problem_id",""),
            "source_file":src,
            "source_line_range":r.get("source_line_range",""),
            "line_span":span,
            "internal_object_headings":heads,
            "problem_type":r.get("problem_type",""),
            "source_problem_number":r.get("source_problem_number",""),
            "structural_status":r.get("structural_status",""),
            "structural_review_flag":r.get("structural_review_flag",""),
            "structural_review_disposition":r.get("structural_review_disposition",""),
            "structural_review_rationale":r.get("structural_review_rationale",""),
            "flags":";".join(flags),
        }

        if accepted_by_disposition(r):
            row["risk_status"]="CLOSED_BY_EDITORIAL_DISPOSITION"
            dispositioned.append(row)
        else:
            row["risk_status"]="ACTIONABLE_STRUCTURAL_RISK"
            actionable.append(row)
            if span>=120: act_long120+=1
            if span>=250: act_long250+=1
            if span>=500: act_long500+=1
            if heads>=2: actionable_multi+=1

    actionable.sort(key=lambda x:(-int(x["internal_object_headings"]),-int(x["line_span"]),x["source_file"]))
    dispositioned.sort(key=lambda x:(-int(x["internal_object_headings"]),-int(x["line_span"]),x["source_file"]))

    # direct-link integrity
    ids={r["problem_id"] for r in ledger}
    dangling=[]
    for s in links:
        pid=s.get("linked_problem_id","")
        if pid and pid not in ids:
            dangling.append({
                "solution_id":s.get("solution_id",""),
                "linked_problem_id":pid,
                "solution_source_file":s.get("solution_source_file",""),
                "solution_line_range":s.get("solution_line_range",""),
            })

    fields=["problem_id","source_file","source_line_range","line_span","internal_object_headings",
            "problem_type","source_problem_number","structural_status","structural_review_flag",
            "structural_review_disposition","structural_review_rationale","flags","risk_status"]
    write_tsv(inv/"STRUCTURAL_STATUS_ACTIONABLE_RISKS.tsv",fields,actionable)
    write_tsv(inv/"STRUCTURAL_STATUS_CLOSED_BY_DISPOSITION.tsv",fields,dispositioned)
    write_tsv(inv/"STRUCTURAL_STATUS_DANGLING_LINKS.tsv",
              ["solution_id","linked_problem_id","solution_source_file","solution_line_range"],dangling)

    summary=[
        "# Disposition-aware structural status","",
        f"- Active ledger rows: **{len(ledger)}**",
        "",
        "## Raw heuristic counts",
        f"- Rows >=120 lines: **{raw_long120}**",
        f"- Rows >=250 lines: **{raw_long250}**",
        f"- Rows >=500 lines: **{raw_long500}**",
        f"- Rows with >=2 internal explicit object headings: **{raw_multi}**",
        "",
        "## After editorial dispositions",
        f"- Actionable rows >=120 lines: **{act_long120}**",
        f"- Actionable rows >=250 lines: **{act_long250}**",
        f"- Actionable rows >=500 lines: **{act_long500}**",
        f"- Actionable rows with >=2 internal explicit object headings: **{actionable_multi}**",
        f"- Total actionable structural-risk rows: **{len(actionable)}**",
        f"- Heuristic-risk rows closed by explicit editorial disposition: **{len(dispositioned)}**",
        "",
        "## Integrity",
        f"- Dangling direct problem/solution links: **{len(dangling)}**",
        f"- Active orphan semantic units: **{len(orphans)}**",
        "",
        "Interpretation: long rows alone are not treated as structural defects after they have been explicitly reviewed. "
        "The key remaining structural blocker is the actionable multi-heading count."
    ]
    (inv/"STRUCTURAL_STATUS_DISPOSITION_AWARE.md").write_text("\n".join(summary)+"\n",encoding="utf-8")

    print(
        f"DISPOSITION-AWARE STRUCTURAL STATUS: ledger={len(ledger)} "
        f"raw_multi={raw_multi} actionable_multi={actionable_multi} "
        f"actionable_rows={len(actionable)} dispositioned={len(dispositioned)} "
        f"dangling={len(dangling)} orphans={len(orphans)}"
    )
    return 0

if __name__=="__main__":
    raise SystemExit(main())
