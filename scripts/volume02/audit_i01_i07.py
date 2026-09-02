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
    probs=exs=hints=sols=0
    for n in range(1,26):
        code=f"II/{n:02d}";r=next((x for x in status if x.get("chapter_code")==code),None)
        if not r:block.append(f"MISSING_STATUS:{code}");continue
        p=repo/r["canonical_path"]
        if not p.exists():block.append(f"MISSING_CHAPTER:{code}");continue
        t=p.read_text(encoding="utf-8-sig")
        pr=len(re.findall(r"\\begin\{problem\}",t));ex=len(re.findall(r"\\begin\{exercise\}",t))
        hi=len(re.findall(r"\\begin\{hint\}",t));so=len(re.findall(r"\\begin\{solution\}",t))
        scaffold="Reconstruction scaffold" in t
        if n<=7:
            if scaffold:block.append(f"UNEXPECTED_SCAFFOLD:{code}")
            if (pr,ex,hi,so)!=(12,8,8,20):block.append(f"PAIRING:{code}:{pr}/{ex}/{hi}/{so}")
            if r.get("status")!="DRAFTED":block.append(f"STATUS:{code}:{r.get('status')}")
        else:
            if not scaffold:block.append(f"EXPECTED_SCAFFOLD:{code}")
        labels += re.findall(r"\\label\{([^}]+)\}",t)
        probs+=pr;exs+=ex;hints+=hi;sols+=so
    dup=sorted({x for x in labels if labels.count(x)>1})
    if dup:block.append("DUPLICATE_LABELS:"+",".join(dup[:20]))
    includes=len(re.findall(r"\\include\{chapters/",(vol/"book.tex").read_text(encoding="utf-8")))
    if includes!=25:block.append(f"BOOK_INCLUDES:{includes}")
    prov=tsv(vol/"reconstruction/VOLUME02_I01_I07_DOSSIER_PROVENANCE.tsv")
    if len(prov)!=84:block.append(f"PROVENANCE_ROWS:{len(prov)}")
    inv=tsv(vol/"reconstruction/VOLUME02_SOURCE_INVENTORY.tsv")
    def as_int(value):
        text=str(value if value is not None else "").strip()
        return 0 if text in ("","-") else int(text)
    missing=sum(as_int(r.get("missing_sources")) for r in inv if int(r["chapter_code"].split("/")[1])<=7)
    if missing:block.append(f"MISSING_CORPUS_SOURCES:{missing}")
    summary={"status":"PASS" if not block else "FAIL","developed_chapters":7,"book_includes":includes,
        "solved_dossiers":probs,"exercises":exs,"hints":hints,"solutions":sols,"provenance_rows":len(prov),
        "corpus_guided":sum(r.get("origin")=="CORPUS_GUIDED" for r in prov),
        "devised":sum(r.get("origin")=="DEVISED_TO_COMPLETE_COVERAGE" for r in prov),
        "missing_corpus_sources":missing,"duplicate_labels":len(dup),
        "unresolved_count":len(block),"unresolved":block}
    out=vol/"reconstruction"
    (out/"VOLUME02_I01_I07_AUDIT.json").write_text(json.dumps(summary,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    md=["# Volume II — II/01–II/07 Reconstruction Audit","",f"**Result:** {summary['status']}","",
        f"- Developed chapters: **7**",f"- Book includes: **{includes} / 25**",
        f"- Solved dossiers: **{probs} / 84**",f"- Exercises: **{exs} / 56**",
        f"- Hints: **{hints} / 56**",f"- Total solutions: **{sols} / 140**",
        f"- Corpus-guided dossier topics: **{summary['corpus_guided']}**",
        f"- Fresh completion dossiers: **{summary['devised']}**",
        f"- Missing mapped sources: **{missing}**",f"- Duplicate labels: **{len(dup)}**","",
        "## Blockers",""]
    md += [f"- {b}" for b in block] if block else ["None."]
    (out/"VOLUME02_I01_I07_AUDIT.md").write_text("\n".join(md)+"\n",encoding="utf-8")
    print(json.dumps(summary,indent=2,ensure_ascii=False))
    return 0 if not block else 3
if __name__=="__main__":raise SystemExit(main())
