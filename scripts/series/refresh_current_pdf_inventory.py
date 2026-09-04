#!/usr/bin/env python3
from __future__ import annotations
import argparse,csv,hashlib,re,shutil,subprocess
from pathlib import Path

VOLS=[
("I","vol01_linear_algebra"),("II","vol02_real_analysis"),("III","vol03_fourier_distributions_pde"),
("IV","vol04_complex_analysis"),("V","vol05_commutative_algebra"),("VI","vol06_algebraic_geometry"),
("VII","vol07_differential_geometry"),("VIII","vol08_algebraic_topology"),
]
def read_tsv(p):
    with Path(p).open("r",encoding="utf-8-sig",newline="") as f:return list(csv.DictReader(f,delimiter="\t"))
def write_tsv(p,rows,fields):
    p=Path(p);p.parent.mkdir(parents=True,exist_ok=True)
    with p.open("w",encoding="utf-8",newline="") as f:
        w=csv.DictWriter(f,fieldnames=fields,delimiter="\t",lineterminator="\n",extrasaction="ignore");w.writeheader();w.writerows(rows)
def sha(p):
    h=hashlib.sha256()
    with Path(p).open("rb") as f:
        for b in iter(lambda:f.read(1024*1024),b""):h.update(b)
    return h.hexdigest()
def pages(p):
    p=Path(p);info=shutil.which("pdfinfo")
    if info:
        cp=subprocess.run([info,str(p)],capture_output=True,text=True,errors="replace")
        if cp.returncode==0:
            m=re.search(r"(?m)^Pages:\s+(\d+)\s*$",cp.stdout)
            if m:return int(m.group(1))
    n=len(re.findall(rb"/Type\s*/Page(?!s)\b",p.read_bytes()))
    if n:return n
    raise RuntimeError(f"Cannot determine page count: {p}")
def main():
    ap=argparse.ArgumentParser();ap.add_argument("--repo",required=True);a=ap.parse_args()
    repo=Path(a.repo).resolve()
    bp=repo/"reports/series/BUILD_I_VIII.tsv";pp=repo/"reports/series/PDF_INVENTORY.tsv"
    build=read_tsv(bp);index={(r.get("volume"),r.get("target"),r.get("kind")):r for r in build}
    pdf=[]
    for v,d in VOLS:
        p=repo/"books"/d/"book.pdf"
        if not p.exists():raise RuntimeError(f"Missing Volume {v} book.pdf")
        r={"volume":v,"pdf_path":p.relative_to(repo).as_posix(),"exists":"YES","pages":pages(p),"bytes":p.stat().st_size,"sha256":sha(p)}
        pdf.append(r)
        br=index.get((v,"book.tex","canonical"))
        if br is None:raise RuntimeError(f"Missing BUILD_I_VIII canonical row for {v}")
        br.update({"status":"PASS","pdf":r["pdf_path"],"bytes":str(r["bytes"]),"sha256":r["sha256"],"error":"-"})
    write_tsv(bp,build,["volume","volume_dir","target","kind","status","pdf","bytes","sha256","error"])
    write_tsv(pp,pdf,["volume","pdf_path","exists","pages","bytes","sha256"])
    print("Refreshed current canonical PDF inventory for 8 volumes.")
    return 0
if __name__=="__main__":raise SystemExit(main())
