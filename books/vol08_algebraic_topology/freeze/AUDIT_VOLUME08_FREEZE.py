#!/usr/bin/env python3
from __future__ import annotations
import argparse, csv, json, re, sys
from pathlib import Path

def read(p): return p.read_text(encoding="utf-8-sig",errors="replace")

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--repo",required=True)
    args=ap.parse_args()
    repo=Path(args.repo).resolve()
    vol=repo/"books/vol08_algebraic_topology"
    statusp=repo/"editorial/CHAPTER_STATUS.tsv"
    with statusp.open("r",encoding="utf-8-sig",newline="") as f:
        rows=[r for r in csv.DictReader(f,delimiter="\t") if r.get("volume")=="VIII"]
    errors=[]
    if len(rows)!=35: errors.append(f"status_rows={len(rows)} expected=35")
    book=read(vol/"book.tex")
    inc_re=re.compile(r"(?m)^[ \t]*\\include\{(chapters/ch(\d\d)_[^}]+/chapter)\}")
    inc_matches=list(inc_re.finditer(book))
    includes=[m.group(1) for m in inc_matches]
    if len(includes)!=35: errors.append(f"active_includes={len(includes)} expected=35")
    book_map={f"VIII/{int(m.group(2)):02d}": vol/(m.group(1)+".tex") for m in inc_matches}

    labels=[]
    total_problem=total_exercise=0
    for r in rows:
        p=book_map.get(r["chapter_code"])
        if p is None or not p.exists():
            errors.append(f"missing_chapter={r['chapter_code']}:{p}"); continue
        t=read(p)
        labels += re.findall(r"\\label\{([^}]+)\}",t)
        # Pair within local span until next Problem/Exercise/section.
        block_re=re.compile(r"\\begin\{(problem|exercise)\}(?:\[[^\]]*\])?(.*?)\\end\{\1\}",re.S|re.I)
        ms=list(block_re.finditer(t))
        for i,m in enumerate(ms):
            kind=m.group(1).lower()
            if kind=="problem": total_problem+=1
            else: total_exercise+=1
            after=t[m.end():ms[i+1].start() if i+1<len(ms) else len(t)]
            sec=re.search(r"\\(?:sub)?section\*?\{",after)
            if sec: after=after[:sec.start()]
            if not re.search(r"\\begin\{solution\}.*?\\end\{solution\}",after,re.S|re.I):
                lab=re.search(r"\\label\{([^}]+)\}",m.group(2))
                errors.append(f"unpaired_{kind}={lab.group(1) if lab else p.name}")
    dups=sorted({x for x in labels if labels.count(x)>1})
    if dups: errors.append("duplicate_labels="+",".join(dups[:20]))

    sm=vol/"reconciliation/VOLUME08_RECONCILIATION_SUMMARY.json"
    if not sm.exists():
        errors.append("missing_reconciliation_summary")
    else:
        s=json.loads(read(sm))
        if s.get("status")!="PASS": errors.append("reconciliation_status_not_PASS")
        if s.get("unresolved_count",1)!=0: errors.append(f"reconciliation_unresolved={s.get('unresolved_count')}")

    # Freeze-ready before metadata mutation; frozen/complete after mutation are both acceptable.
    badstatus=[]
    for r in rows:
        if r.get("status") not in ("DRAFTED","FROZEN"):
            badstatus.append(r.get("chapter_code","")+"="+r.get("status",""))
        if r.get("status")=="DRAFTED" and r.get("next_action")!="FREEZE_READY":
            badstatus.append(r.get("chapter_code","")+" next="+r.get("next_action",""))
        if r.get("status")=="FROZEN" and r.get("next_action")!="COMPLETE":
            badstatus.append(r.get("chapter_code","")+" next="+r.get("next_action",""))
    if badstatus: errors.append("status_semantics:"+",".join(badstatus[:20]))

    print(f"chapters={len(rows)} includes={len(includes)} labels={len(labels)} problems={total_problem} exercises={total_exercise}")
    if errors:
        print("FREEZE AUDIT FAILED")
        for e in errors: print("BLOCK:",e)
        return 2
    print("VOLUME VIII FREEZE AUDIT PASSED")
    return 0

if __name__=="__main__":
    raise SystemExit(main())
