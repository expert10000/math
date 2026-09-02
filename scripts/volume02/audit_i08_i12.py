#!/usr/bin/env python3
from __future__ import annotations
import argparse,csv,json,re
from pathlib import Path

def tsv(p):
    with p.open("r",encoding="utf-8-sig",newline="") as f:return list(csv.DictReader(f,delimiter="\t"))

def main():
    ap=argparse.ArgumentParser();ap.add_argument("--repo",required=True);args=ap.parse_args()
    repo=Path(args.repo).resolve();vol=repo/"books/vol02_real_analysis";block=[];labels=[]
    status=tsv(repo/"editorial/CHAPTER_STATUS.tsv")
    for n in range(1,26):
        code=f"II/{n:02d}";r=next((x for x in status if x.get("chapter_code")==code),None)
        if not r:block.append(f"MISSING_STATUS:{code}");continue
        p=repo/r["canonical_path"]
        if not p.exists():block.append(f"MISSING_CHAPTER:{code}");continue
        t=p.read_text(encoding="utf-8-sig")
        pr=len(re.findall(r"\\begin\{problem\}",t));ex=len(re.findall(r"\\begin\{exercise\}",t))
        hi=len(re.findall(r"\\begin\{hint\}",t));so=len(re.findall(r"\\begin\{solution\}",t))
        scaffold="Reconstruction scaffold" in t
        if n<=12:
            if scaffold:block.append(f"UNEXPECTED_SCAFFOLD:{code}")
            if (pr,ex,hi,so)!=(12,8,8,20):block.append(f"PAIRING:{code}:{pr}/{ex}/{hi}/{so}")
            if r.get("status")!="DRAFTED":block.append(f"STATUS:{code}:{r.get('status')}")
        else:
            if not scaffold:block.append(f"EXPECTED_SCAFFOLD:{code}")
        labels += re.findall(r"\\label\{([^}]+)\}",t)
    dup=sorted({x for x in labels if labels.count(x)>1})
    if dup:block.append("DUPLICATE_LABELS:"+",".join(dup[:20]))
    prov=tsv(vol/"reconstruction/VOLUME02_I08_I12_DOSSIER_PROVENANCE.tsv")
    if len(prov)!=60:block.append(f"PROVENANCE_ROWS:{len(prov)}")
    ii09=[r for r in prov if r.get("chapter_code")=="II/09"]
    if len(ii09)!=12 or any(r.get("origin")!="FRESH_CANONICAL" for r in ii09):
        block.append("II09_NOT_FULLY_FRESH")
    src=tsv(repo/"editorial/SOURCE_MIGRATION.tsv")
    if any(r.get("destination")=="II/09" for r in src):
        block.append("II09_SOURCE_MAP_UNEXPECTEDLY_NONZERO")
    summary={"status":"PASS" if not block else "FAIL","developed_through":"II/12",
             "new_chapters":5,"new_dossiers":60,"ii09_fresh_dossiers":len(ii09),
             "duplicate_labels":len(dup),"unresolved_count":len(block),"unresolved":block}
    out=vol/"reconstruction"
    (out/"VOLUME02_I08_I12_AUDIT.json").write_text(json.dumps(summary,indent=2)+"\n",encoding="utf-8")
    md=["# Volume II — II/08–II/12 Audit","",f"**Result:** {summary['status']}","",
        "- New developed chapters: **5**","- New solved dossiers: **60**",
        f"- II/09 fresh canonical dossiers: **{len(ii09)} / 12**",
        f"- Duplicate labels: **{len(dup)}**","", "## Blockers",""]
    md += [f"- {b}" for b in block] if block else ["None."]
    (out/"VOLUME02_I08_I12_AUDIT.md").write_text("\n".join(md)+"\n",encoding="utf-8")
    print(json.dumps(summary,indent=2))
    return 0 if not block else 3
if __name__=="__main__":raise SystemExit(main())
