#!/usr/bin/env python3
from __future__ import annotations
import argparse, csv, hashlib, json, re
from pathlib import Path
from collections import Counter

VOL=Path("books/vol01_linear_algebra/chapters")
REPORT=Path("reports/series")
LABEL=re.compile(r"\\label\{([^}]+)\}")

def hfile(p):
    h=hashlib.sha256()
    with p.open("rb") as f:
        for b in iter(lambda:f.read(1<<20),b""): h.update(b)
    return h.hexdigest()

def envcount(t,e): return len(re.findall(rf"\\begin\{{{e}\}}",t))

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--repo",required=True)
    ap.add_argument("--pdf",required=True)
    ap.add_argument("--log",required=True)
    a=ap.parse_args(); repo=Path(a.repo).resolve()
    pdf=Path(a.pdf); log=Path(a.log)
    outdir=repo/REPORT; outdir.mkdir(parents=True,exist_ok=True)

    rows=[]; hashes=[]; labels=[]
    for i,p in enumerate(sorted((repo/VOL).glob("ch*/chapter.tex")),1):
        t=p.read_text(encoding="utf-8-sig")
        row={"chapter":f"I/{i:02d}",
             "examples":envcount(t,"example"),"exercises":envcount(t,"exercise"),
             "hints":envcount(t,"hint"),"problems":envcount(t,"problem"),
             "solutions":envcount(t,"solution"),
             "labels":len(LABEL.findall(t))}
        rows.append(row)
        hashes.append({"chapter":row["chapter"],"path":str(p.relative_to(repo)).replace("\\","/"),"sha256":hfile(p)})
        labels += LABEL.findall(t)

    logtext=log.read_text(encoding="utf-8",errors="replace") if log.exists() else ""
    fatal_patterns=["Fatal error occurred","Emergency stop","! LaTeX Error","!  ==> Fatal error"]
    undefined_refs=("There were undefined references" in logtext or
                    "Rerun to get cross-references right" in logtext)
    fatal=[p for p in fatal_patterns if p in logtext]
    dup=[k for k,v in Counter(labels).items() if v>1]
    blockers=[]
    if not pdf.exists(): blockers.append("PDF_MISSING")
    if fatal: blockers += [f"TEX_FATAL:{x}" for x in fatal]
    if undefined_refs: blockers.append("UNDEFINED_REFERENCES_OR_RERUN_WARNING")
    if dup: blockers += [f"DUPLICATE_LABEL:{x}" for x in dup]

    totals={k:sum(r[k] for r in rows) for k in ["examples","exercises","hints","problems","solutions","labels"]}
    status="PASS" if not blockers else "FAIL"
    pdf_info={"path":str(pdf),"sha256":hfile(pdf) if pdf.exists() else None,
              "bytes":pdf.stat().st_size if pdf.exists() else None}

    result={"status":status,"chapters":rows,"totals":totals,"pdf":pdf_info,"blocking":blockers}
    (outdir/"VOLUME01_EXAMPLE_EXERCISE_RECONCILIATION.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")

    with (outdir/"VOLUME01_EXAMPLE_EXERCISE_COUNTS.tsv").open("w",encoding="utf-8",newline="") as f:
        w=csv.DictWriter(f,fieldnames=["chapter","examples","exercises","hints","problems","solutions","labels"],delimiter="\t")
        w.writeheader(); w.writerows(rows)
    with (outdir/"VOLUME01_EXAMPLE_EXERCISE_HASHES.tsv").open("w",encoding="utf-8",newline="") as f:
        w=csv.DictWriter(f,fieldnames=["chapter","path","sha256"],delimiter="\t")
        w.writeheader(); w.writerows(hashes)

    md=["# Volume I pedagogy reconciliation after example/exercise expansion","",
        f"**Result:** {status}","",
        "## Totals",""]
    for k,v in totals.items(): md.append(f"- {k}: **{v}**")
    md += ["","## Canonical PDF","",
           f"- path: `{pdf_info['path']}`",
           f"- bytes: `{pdf_info['bytes']}`",
           f"- SHA-256: `{pdf_info['sha256']}`",
           "","## Blocking findings",""]
    md += [f"- {x}" for x in blockers] if blockers else ["None."]
    (outdir/"VOLUME01_EXAMPLE_EXERCISE_RECONCILIATION.md").write_text("\n".join(md)+"\n",encoding="utf-8")

    print(json.dumps({"status":status,"totals":totals,"pdf":pdf_info,"blocking":blockers},indent=2))
    raise SystemExit(0 if status=="PASS" else 13)
if __name__=="__main__": main()
