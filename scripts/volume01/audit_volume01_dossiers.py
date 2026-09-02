#!/usr/bin/env python3
from __future__ import annotations
import argparse,csv,json,re
from pathlib import Path
def tsv(p):
    with p.open("r",encoding="utf-8-sig",newline="") as f:return list(csv.DictReader(f,delimiter="\t"))
def write_tsv(p,rows,fields):
    lines=["\t".join(fields)]
    for r in rows:lines.append("\t".join(str(r.get(f,"-") or "-") for f in fields))
    p.write_text("\n".join(lines)+"\n",encoding="utf-8")
def main():
    ap=argparse.ArgumentParser();ap.add_argument("--repo",required=True);args=ap.parse_args()
    repo=Path(args.repo).resolve();vol=repo/"books/vol01_linear_algebra";prov=tsv(vol/"dossiers/VOLUME01_DOSSIER_PROVENANCE.tsv")
    rows=[];block=[];labels=[];total=0
    for n in range(1,19):
        code=f"I/{n:02d}";cp=next((repo/r["canonical_path"] for r in tsv(repo/"editorial/CHAPTER_STATUS.tsv") if r.get("chapter_code")==code),None)
        if not cp or not cp.exists():block.append(f"MISSING_CHAPTER:{code}");continue
        text=cp.read_text(encoding="utf-8-sig")
        probs=re.findall(r"\\begin\{problem\}\[[^\]]*\]\\label\{(prob:i\d\d-dossier-\d\d)\}",text)
        sols=len(re.findall(r"\\begin\{solution\}",text))
        ex=len(re.findall(r"\\begin\{exercise\}",text));hints=len(re.findall(r"\\begin\{hint\}",text))
        dossier_solutions=sols-ex
        prow=[r for r in prov if r.get("chapter_code")==code]
        cg=sum(r.get("origin")=="CORPUS_GUIDED" for r in prow);dv=sum(r.get("origin")=="DEVISED_TO_COMPLETE_COVERAGE" for r in prow)
        ok=(len(probs)==12 and dossier_solutions==12 and ex==8 and hints==8 and len(prow)==12)
        if not ok:block.append(f"DOSSIER_COUNTS:{code}:problems={len(probs)} dossier_solutions={dossier_solutions} exercises={ex} hints={hints} provenance={len(prow)}")
        rows.append({"chapter_code":code,"dossiers":len(probs),"dossier_solutions":dossier_solutions,"existing_exercises":ex,"existing_hints":hints,
                     "provenance_rows":len(prow),"corpus_guided":cg,"devised":dv,"status":"PASS" if ok else "FAIL"})
        labels+=probs;total+=len(probs)
    dup=sorted({x for x in labels if labels.count(x)>1})
    if dup:block.append("DUPLICATE_DOSSIER_LABELS:"+",".join(dup[:20]))
    missing_source=[]
    for r in prov:
        if r.get("origin")=="CORPUS_GUIDED":
            name=r.get("source_file","")
            if not ((repo/name).exists() or (repo/"chapters/tex"/name).exists()):
                missing_source.append(f"{r.get('dossier_label')}:{name}")
    if missing_source:block.append("MISSING_PROVENANCE_SOURCE:"+",".join(missing_source[:20]))
    out=vol/"dossiers";write_tsv(out/"VOLUME01_DOSSIER_AUDIT.tsv",rows,["chapter_code","dossiers","dossier_solutions","existing_exercises","existing_hints","provenance_rows","corpus_guided","devised","status"])
    summary={"status":"PASS" if not block else "FAIL","dossiers":total,"expected":216,"corpus_guided":sum(r.get("origin")=="CORPUS_GUIDED" for r in prov),
             "devised":sum(r.get("origin")=="DEVISED_TO_COMPLETE_COVERAGE" for r in prov),"unresolved_count":len(block),"unresolved":block}
    (out/"VOLUME01_DOSSIER_AUDIT.json").write_text(json.dumps(summary,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    md=["# Volume I — Solved Dossier Audit","",f"**Result:** {summary['status']}","",f"- Solved dossiers: **{total} / 216**",
        f"- Corpus-guided topics: **{summary['corpus_guided']}**",f"- Devised coverage dossiers: **{summary['devised']}**",
        "- Existing short exercise layer preserved: **8 exercises + 8 hints + 8 solutions per chapter**",
        "", "A `CORPUS_GUIDED` dossier uses an explicit mapped legacy rule to choose or emphasize the topic; its canonical problem statement and solution are newly written rather than copied verbatim.",
        "","## Blockers",""]
    md += [f"- {b}" for b in block] if block else ["None."]
    (out/"VOLUME01_DOSSIER_AUDIT.md").write_text("\n".join(md)+"\n",encoding="utf-8")
    print(json.dumps(summary,indent=2,ensure_ascii=False))
    return 0 if not block else 3
if __name__=="__main__":raise SystemExit(main())
