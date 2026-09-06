#!/usr/bin/env python3
import argparse,csv,hashlib,json,re,subprocess
from collections import Counter
from pathlib import Path
VOL=Path("books/vol06_algebraic_geometry/chapters"); REPORT=Path("reports/series"); LAB=re.compile(r"\\label\{([^}]+)\}")
def hfile(p):
    h=hashlib.sha256()
    with p.open("rb") as f:
        for b in iter(lambda:f.read(1<<20),b""): h.update(b)
    return h.hexdigest()
def cnt(t,e): return len(re.findall(rf"\\begin\{{{e}\}}",t))
def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--repo",required=True); ap.add_argument("--pdf",required=True); ap.add_argument("--log",required=True); a=ap.parse_args()
    repo=Path(a.repo).resolve(); pdf=Path(a.pdf).resolve(); log=Path(a.log).resolve(); out=repo/REPORT; out.mkdir(parents=True,exist_ok=True)
    rows=[]; hashes=[]; labels=[]; blockers=[]; observations=[]
    fs=sorted((repo/VOL).glob("ch*/chapter.tex"))
    if len(fs)!=49: blockers.append(f"CHAPTER_COUNT:{len(fs)}!=49")
    for i,p in enumerate(fs,1):
        t=p.read_text(encoding="utf-8-sig"); row={"chapter":f"VI/{i:02d}","examples":cnt(t,"example"),"exercises":cnt(t,"exercise"),"hints":cnt(t,"hint"),"problems":cnt(t,"problem"),"solutions":cnt(t,"solution"),"labels":len(LAB.findall(t))}
        rows.append(row); labels+=LAB.findall(t); hashes.append({"chapter":row["chapter"],"path":p.relative_to(repo).as_posix(),"sha256":hfile(p)})
        if row["exercises"]!=row["hints"]: observations.append(f"{row['chapter']}:LEGACY_EXERCISE_HINT_IMBALANCE:{row['exercises']}!={row['hints']}")
        if row["solutions"]<row["exercises"]+row["problems"]: observations.append(f"{row['chapter']}:LEGACY_SOLUTION_COVERAGE")
    logtext=log.read_text(encoding="utf-8",errors="replace") if log.exists() else ""
    if not pdf.exists(): blockers.append("PDF_MISSING")
    for pat in ["Fatal error occurred","Emergency stop","! LaTeX Error","!  ==> Fatal error","Undefined control sequence"]:
        if pat in logtext: blockers.append(f"TEX_FATAL:{pat}")
    if "There were undefined references" in logtext: blockers.append("UNDEFINED_REFERENCES")
    if "Rerun to get cross-references right" in logtext: blockers.append("RERUN_WARNING_AFTER_THREE_PASSES")
    for lab,n in Counter(labels).items():
        if n>1: blockers.append(f"DUPLICATE_LABEL:{lab}")
    tracked=subprocess.run(["git","-C",str(repo),"ls-files","scripts/volume06"],stdout=subprocess.PIPE,text=True,encoding="utf-8",errors="replace").stdout.splitlines()
    cache=[x for x in tracked if "/__pycache__/" in x or x.endswith(".pyc")]
    if cache: blockers += [f"TRACKED_PYTHON_CACHE:{x}" for x in cache]
    totals={k:sum(r[k] for r in rows) for k in ["examples","exercises","hints","problems","solutions","labels"]}
    pdfinfo={"path":str(pdf),"bytes":pdf.stat().st_size if pdf.exists() else None,"sha256":hfile(pdf) if pdf.exists() else None}
    status="PASS" if not blockers else "FAIL"; result={"status":status,"chapters":rows,"totals":totals,"pdf":pdfinfo,"tracked_python_cache":cache,"blocking":blockers,"legacy_observations":observations}
    (out/"VOLUME06_EXAMPLE_EXERCISE_RECONCILIATION.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
    with (out/"VOLUME06_EXAMPLE_EXERCISE_COUNTS.tsv").open("w",encoding="utf-8",newline="") as f:
        w=csv.DictWriter(f,fieldnames=["chapter","examples","exercises","hints","problems","solutions","labels"],delimiter="\t"); w.writeheader(); w.writerows(rows)
    with (out/"VOLUME06_EXAMPLE_EXERCISE_HASHES.tsv").open("w",encoding="utf-8",newline="") as f:
        w=csv.DictWriter(f,fieldnames=["chapter","path","sha256"],delimiter="\t"); w.writeheader(); w.writerows(hashes)
    md=["# Volume VI pedagogy reconciliation after example/exercise expansion","",f"**Result:** {status}","","## Totals",""]
    for k,v in totals.items(): md.append(f"- {k}: **{v}**")
    md += ["","## Canonical PDF","",f"- path: `{pdfinfo['path']}`",f"- bytes: `{pdfinfo['bytes']}`",f"- SHA-256: `{pdfinfo['sha256']}`","","## Python-cache hygiene","",f"- tracked cache files: **{len(cache)}**","","## Blocking findings",""]
    md += [f"- {b}" for b in blockers] if blockers else ["None."]
    md += ["","## Legacy baseline observations (non-blocking)",""]+([f"- {b}" for b in observations] if observations else ["None."])
    (out/"VOLUME06_EXAMPLE_EXERCISE_RECONCILIATION.md").write_text("\n".join(md)+"\n",encoding="utf-8")
    print(json.dumps({"status":status,"totals":totals,"pdf":pdfinfo,"tracked_python_cache":cache,"blocking":blockers},indent=2))
    return 0 if status=="PASS" else 13
if __name__=="__main__":
    raise SystemExit(main())
