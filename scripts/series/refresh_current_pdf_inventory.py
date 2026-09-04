#!/usr/bin/env python3
from __future__ import annotations
import argparse,csv,hashlib,re,shutil,subprocess
from pathlib import Path

VOLS=[
("I","vol01_linear_algebra"),
("II","vol02_real_analysis"),
("III","vol03_fourier_distributions_pde"),
("IV","vol04_complex_analysis"),
("V","vol05_commutative_algebra"),
("VI","vol06_algebraic_geometry"),
("VII","vol07_differential_geometry"),
("VIII","vol08_algebraic_topology"),
]

def read_tsv(path):
    with Path(path).open("r",encoding="utf-8-sig",newline="") as f:
        return list(csv.DictReader(f,delimiter="\t"))

def write_tsv(path,rows,fields):
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    with path.open("w",encoding="utf-8",newline="") as f:
        w=csv.DictWriter(f,fieldnames=fields,delimiter="\t",lineterminator="\n",extrasaction="ignore")
        w.writeheader();w.writerows(rows)

def sha(path):
    h=hashlib.sha256()
    with Path(path).open("rb") as f:
        for b in iter(lambda:f.read(1024*1024),b""):
            h.update(b)
    return h.hexdigest()

def pages(pdf):
    pdf=Path(pdf)
    pdfinfo=shutil.which("pdfinfo")
    if pdfinfo:
        cp=subprocess.run([pdfinfo,str(pdf)],capture_output=True,text=True,errors="replace")
        if cp.returncode==0:
            m=re.search(r"(?m)^Pages:\s+(\d+)\s*$",cp.stdout)
            if m:return int(m.group(1))
    data=pdf.read_bytes()
    n=len(re.findall(rb"/Type\s*/Page(?!s)\b",data))
    if n>0:return n
    raise RuntimeError(f"Unable to determine PDF page count: {pdf}")

def main():
    ap=argparse.ArgumentParser();ap.add_argument("--repo",required=True);args=ap.parse_args()
    repo=Path(args.repo).resolve()
    build_path=repo/"reports/series/BUILD_I_VIII.tsv"
    pdf_path=repo/"reports/series/PDF_INVENTORY.tsv"
    build=read_tsv(build_path)
    by_vol={(r.get("volume"),r.get("target"),r.get("kind")):r for r in build}

    pdfrows=[]
    for v,dirname in VOLS:
        p=repo/"books"/dirname/"book.pdf"
        if not p.exists():
            raise RuntimeError(f"Missing canonical PDF for Volume {v}: {p}")
        digest=sha(p);size=p.stat().st_size;pc=pages(p)
        pdfrows.append({
            "volume":v,"pdf_path":p.relative_to(repo).as_posix(),"exists":"YES",
            "pages":pc,"bytes":size,"sha256":digest
        })
        key=(v,"book.tex","canonical")
        if key not in by_vol:
            raise RuntimeError(f"BUILD_I_VIII missing canonical row for Volume {v}")
        r=by_vol[key]
        r["status"]="PASS"
        r["pdf"]=p.relative_to(repo).as_posix()
        r["bytes"]=str(size)
        r["sha256"]=digest
        r["error"]="-"

    fields=["volume","volume_dir","target","kind","status","pdf","bytes","sha256","error"]
    write_tsv(build_path,build,fields)
    write_tsv(pdf_path,pdfrows,["volume","pdf_path","exists","pages","bytes","sha256"])

    # Refresh the human build summary deterministically.
    canon=[r for r in build if r.get("target")=="book.tex" and r.get("kind")=="canonical"]
    body=["# I-VIII Canonical Build Inventory","",
          f"- PASS: **{sum(r.get('status')=='PASS' for r in canon)}**",
          f"- FAIL: **{sum(r.get('status')=='FAIL' for r in canon)}**",
          f"- NO_WRAPPER: **{sum(r.get('status')=='NO_WRAPPER' for r in canon)}**","",
          "| Volume | Target | Status | Detail |","|---|---|---|---|"]
    order={v:i for i,(v,_) in enumerate(VOLS)}
    for r in sorted(canon,key=lambda x:order.get(x.get("volume"),99)):
        detail=r.get("pdf","") if r.get("status")=="PASS" else r.get("error","")
        body.append(f"| {r.get('volume')} | {r.get('target')} | {r.get('status')} | {detail} |")
    (repo/"reports/series/BUILD_I_VIII.md").write_text("\n".join(body).rstrip()+"\n",encoding="utf-8")

    print("Refreshed canonical PDF/build inventory for 8 volumes.")
    for r in pdfrows:
        print(f"{r['volume']}: {r['pages']} pages, {r['bytes']} bytes, {r['sha256']}")
    return 0

if __name__=="__main__":
    raise SystemExit(main())
