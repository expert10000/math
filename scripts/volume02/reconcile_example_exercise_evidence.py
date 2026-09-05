#!/usr/bin/env python3
from __future__ import annotations
import argparse, csv, hashlib, json, re
from pathlib import Path
from collections import Counter

VOL=Path("books/vol02_real_analysis/chapters")
REPORT=Path("reports/series")
LABEL=re.compile(r"\\label\{([^}]+)\}")

def hfile(p):
    h=hashlib.sha256()
    with p.open("rb") as f:
        for b in iter(lambda:f.read(1<<20),b""): h.update(b)
    return h.hexdigest()
def cnt(t,e): return len(re.findall(rf"\\begin\{{{e}\}}",t))

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--repo",required=True)
    ap.add_argument("--pdf",required=True)
    ap.add_argument("--log",required=True)
    a=ap.parse_args(); repo=Path(a.repo).resolve(); pdf=Path(a.pdf); log=Path(a.log)
    out=repo/REPORT; out.mkdir(parents=True,exist_ok=True)

    rows=[]; hashes=[]; labels=[]
    for i,p in enumerate(sorted((repo/VOL).glob("ch*/chapter.tex")),1):
        t=p.read_text(encoding="utf-8-sig")
        row={"chapter":f"II/{i:02d}","examples":cnt(t,"example"),"exercises":cnt(t,"exercise"),
             "hints":cnt(t,"hint"),"problems":cnt(t,"problem"),"solutions":cnt(t,"solution"),
             "labels":len(LABEL.findall(t))}
        rows.append(row); labels += LABEL.findall(t)
        hashes.append({"chapter":row["chapter"],"path":str(p.relative_to(repo)).replace("\\","/"),"sha256":hfile(p)})

    logtext=log.read_text(encoding="utf-8",errors="replace") if log.exists() else ""
    blockers=[]
    if not pdf.exists(): blockers.append("PDF_MISSING")
    for pat in ["Fatal error occurred","Emergency stop","! LaTeX Error","!  ==> Fatal error"]:
        if pat in logtext: blockers.append(f"TEX_FATAL:{pat}")
    if "There were undefined references" in logtext:
        blockers.append("UNDEFINED_REFERENCES")
    if "Rerun to get cross-references right" in logtext:
        blockers.append("RERUN_WARNING_AFTER_THREE_PASSES")
    for label,n in Counter(labels).items():
        if n>1: blockers.append(f"DUPLICATE_LABEL:{label}")

    totals={k:sum(r[k] for r in rows) for k in ["examples","exercises","hints","problems","solutions","labels"]}
    pdfinfo={"path":str(pdf),"bytes":pdf.stat().st_size if pdf.exists() else None,
             "sha256":hfile(pdf) if pdf.exists() else None}
    status="PASS" if not blockers else "FAIL"
    result={"status":status,"chapters":rows,"totals":totals,"pdf":pdfinfo,"blocking":blockers}

    (out/"VOLUME02_EXAMPLE_EXERCISE_RECONCILIATION.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
    with (out/"VOLUME02_EXAMPLE_EXERCISE_COUNTS.tsv").open("w",encoding="utf-8",newline="") as f:
        w=csv.DictWriter(f,fieldnames=["chapter","examples","exercises","hints","problems","solutions","labels"],delimiter="\t")
        w.writeheader(); w.writerows(rows)
    with (out/"VOLUME02_EXAMPLE_EXERCISE_HASHES.tsv").open("w",encoding="utf-8",newline="") as f:
        w=csv.DictWriter(f,fieldnames=["chapter","path","sha256"],delimiter="\t")
        w.writeheader(); w.writerows(hashes)

    md=["# Volume II pedagogy reconciliation after example/exercise expansion","",
        f"**Result:** {status}","","## Totals",""]
    for k,v in totals.items(): md.append(f"- {k}: **{v}**")
    md += ["","## Canonical PDF","",f"- path: `{pdfinfo['path']}`",f"- bytes: `{pdfinfo['bytes']}`",
           f"- SHA-256: `{pdfinfo['sha256']}`","","## Blocking findings",""]
    md += [f"- {b}" for b in blockers] if blockers else ["None."]
    (out/"VOLUME02_EXAMPLE_EXERCISE_RECONCILIATION.md").write_text("\n".join(md)+"\n",encoding="utf-8")
    print(json.dumps({"status":status,"totals":totals,"pdf":pdfinfo,"blocking":blockers},indent=2))
    raise SystemExit(0 if status=="PASS" else 13)

if __name__=="__main__": main()
