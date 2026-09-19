#!/usr/bin/env python3
from __future__ import annotations
import argparse, csv, re, hashlib
from collections import Counter, defaultdict
from pathlib import Path

LINE_RANGE_RE=re.compile(r"L?(\d+)\s*-\s*L?(\d+)")
COMMENT_RE=re.compile(r"(?<!\\)%.*$")
HEAD_RE=re.compile(r"^\s*\\(?:section|subsection|subsubsection)\*?\{(?P<title>[^{}]+)\}\s*$",re.I)
OBJ_RE=re.compile(r"^\s*(Problem|Exercise|Example|Question|Task|Challenge)\b",re.I)

def read_tsv(path):
    with path.open("r",encoding="utf-8-sig",newline="") as f:
        r=csv.DictReader(f,delimiter="\t")
        return list(r.fieldnames or []),[dict(x) for x in r]

def write_tsv(path,fields,rows):
    path.parent.mkdir(parents=True,exist_ok=True)
    with path.open("w",encoding="utf-8",newline="") as f:
        w=csv.DictWriter(f,fieldnames=fields,delimiter="\t",lineterminator="\n",extrasaction="ignore")
        w.writeheader()
        for r in rows:w.writerow({k:r.get(k,"") for k in fields})

def parse_range(s):
    m=LINE_RANGE_RE.search(s or "")
    return (int(m.group(1)),int(m.group(2))) if m else None

def safe_lines(path):
    for enc in ("utf-8-sig","utf-8","cp1252","latin-1"):
        try:return path.read_text(encoding=enc).splitlines()
        except UnicodeDecodeError:pass
    return path.read_text(encoding="utf-8",errors="replace").splitlines()

def strip_comment(s):return COMMENT_RE.sub("",s)

def count_internal_object_heads(lines,a,b):
    n=0
    for i in range(a,b+1):
        m=HEAD_RE.match(strip_comment(lines[i-1]))
        if m and OBJ_RE.match(m.group("title").strip()):
            n+=1
    return n

def family_name(path):
    stem=Path(path).stem.lower()
    stem=re.sub(r"\s*\(\d+\)\s*$","",stem)
    stem=re.sub(r"\s*-\s*copy$","",stem)
    return stem

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

    rows=[]
    counts=Counter()
    for r in ledger:
        rr=parse_range(r.get("source_line_range",""))
        if not rr:
            continue
        span=rr[1]-rr[0]+1
        src=r.get("source_file","")
        p=srcroot/src
        heads=""
        if p.exists():
            lines=safe_lines(p)
            heads=count_internal_object_heads(lines,*rr)
        flags=[]
        if span>=500: flags.append("SPAN_GE_500")
        elif span>=250: flags.append("SPAN_GE_250")
        elif span>=120: flags.append("SPAN_GE_120")
        if isinstance(heads,int) and heads>=2: flags.append("MULTIPLE_INTERNAL_OBJECT_HEADINGS")
        status=r.get("structural_status","")
        if status.startswith("ACTIVE_"):
            counts["resegmented_active"]+=1
        if flags:
            severity="HIGH" if ("SPAN_GE_500" in flags or "MULTIPLE_INTERNAL_OBJECT_HEADINGS" in flags) else "MEDIUM"
            counts[severity]+=1
            rows.append({
                "problem_id":r.get("problem_id",""),
                "source_file":src,
                "source_family":family_name(src),
                "source_line_range":r.get("source_line_range",""),
                "line_span":span,
                "internal_object_headings":heads,
                "problem_type":r.get("problem_type",""),
                "source_problem_number":r.get("source_problem_number",""),
                "structural_status":status,
                "severity":severity,
                "flags":";".join(flags),
            })

    rows.sort(key=lambda x:(0 if x["severity"]=="HIGH" else 1,-int(x["line_span"]),x["source_file"],x["problem_id"]))

    # Collapse active risk rows by source family + line-span/head profile for review prioritization.
    groups=defaultdict(list)
    for r in rows:
        key=(r["source_family"],r["line_span"],r["internal_object_headings"],r["flags"])
        groups[key].append(r)

    famrows=[]
    for i,(key,members) in enumerate(sorted(groups.items(),key=lambda kv:(-max(int(x["line_span"]) for x in kv[1]),kv[0][0])),1):
        rep=sorted(members,key=lambda r:(0 if r["source_file"].startswith("Downloads/") else 1,r["source_file"]))[0]
        famrows.append({
            "risk_family_id":f"PRF-{i:03d}",
            "representative_problem_id":rep["problem_id"],
            "representative_source_file":rep["source_file"],
            "member_count":len(members),
            "member_problem_ids":";".join(r["problem_id"] for r in members),
            "source_family":rep["source_family"],
            "line_span":rep["line_span"],
            "internal_object_headings":rep["internal_object_headings"],
            "flags":rep["flags"],
            "severity":rep["severity"],
            "recommended_next_action":(
                "RESEGMENT_EXPLICIT_OBJECTS" if int(rep["internal_object_headings"])>=2
                else ("INSPECT_LONG_NONSTANDARD_OBJECT" if int(rep["line_span"])>=250
                      else "REVIEW_MEDIUM_SPAN")
            ),
        })

    # Link integrity.
    active_ids={r["problem_id"] for r in ledger}
    dangling=[]
    for s in links:
        pid=s.get("linked_problem_id","")
        if pid and pid not in active_ids:
            dangling.append({
                "solution_id":s.get("solution_id",""),
                "linked_problem_id":pid,
                "solution_source_file":s.get("solution_source_file",""),
                "solution_line_range":s.get("solution_line_range",""),
            })

    write_tsv(inv/"POST_REPAIR_STRUCTURAL_RISK_ROWS.tsv",
              ["problem_id","source_file","source_family","source_line_range","line_span",
               "internal_object_headings","problem_type","source_problem_number",
               "structural_status","severity","flags"],rows)
    write_tsv(inv/"POST_REPAIR_STRUCTURAL_RISK_FAMILIES.tsv",
              ["risk_family_id","representative_problem_id","representative_source_file",
               "member_count","member_problem_ids","source_family","line_span",
               "internal_object_headings","flags","severity","recommended_next_action"],famrows)
    write_tsv(inv/"POST_REPAIR_DANGLING_LINKS.tsv",
              ["solution_id","linked_problem_id","solution_source_file","solution_line_range"],dangling)

    span120=sum(1 for r in rows if int(r["line_span"])>=120)
    span250=sum(1 for r in rows if int(r["line_span"])>=250)
    span500=sum(1 for r in rows if int(r["line_span"])>=500)
    multi=sum(1 for r in rows if int(r["internal_object_headings"])>=2)

    summary=[
        "# Post-repair structural status","",
        f"- Active ledger rows: **{len(ledger)}**",
        f"- Active structurally resegmented rows: **{counts['resegmented_active']}**",
        f"- Active rows still >=120 lines: **{span120}**",
        f"- Active rows still >=250 lines: **{span250}**",
        f"- Active rows still >=500 lines: **{span500}**",
        f"- Active rows containing >=2 internal explicit object headings: **{multi}**",
        f"- Remaining structural risk rows: **{len(rows)}**",
        f"- Unique structural risk families: **{len(famrows)}**",
        f"- High-severity risk rows: **{counts['HIGH']}**",
        f"- Medium-severity risk rows: **{counts['MEDIUM']}**","",
        "## Link/orphan integrity",
        f"- Dangling direct problem/solution links: **{len(dangling)}**",
        f"- Active orphan semantic units: **{len(orphans)}**","",
        "This report is authoritative for the current repaired master ledger. Older v3 SAFE/REVIEW/INSUFFICIENT counts should now be treated as historical diagnostics."
    ]
    (inv/"POST_REPAIR_STRUCTURAL_STATUS.md").write_text("\n".join(summary)+"\n",encoding="utf-8")
    print(
        f"POST-REPAIR STRUCTURAL STATUS: ledger={len(ledger)} risk_rows={len(rows)} "
        f"risk_families={len(famrows)} ge250={span250} ge500={span500} "
        f"multi_heads={multi} dangling={len(dangling)} orphans={len(orphans)}"
    )
    return 0

if __name__=="__main__":
    raise SystemExit(main())
