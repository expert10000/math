#!/usr/bin/env python3
import argparse,csv,re
from pathlib import Path

VOLS=[
"vol01_linear_algebra","vol02_real_analysis","vol03_fourier_distributions_pde",
"vol04_complex_analysis","vol05_commutative_algebra","vol06_algebraic_geometry",
"vol07_differential_geometry","vol08_algebraic_topology"]

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--repo",required=True); a=ap.parse_args()
    repo=Path(a.repo).resolve(); fail=[]; chapters=[]

    for d in VOLS:
        v=repo/"books"/d
        g=v/"frontmatter"/"chapter-structure-guide.tex"
        if not g.exists(): fail.append(f"{d}: missing chapter structure guide")
        b=(v/"book.tex").read_text(encoding="utf-8-sig")
        if r"\input{frontmatter/chapter-structure-guide.tex}" not in b:
            fail.append(f"{d}: structure guide not included")
        chapters += list((v/"chapters").glob("*/chapter.tex"))

    deprecated=["\\section{Solved dossiers}","\\section{Solved problem dossiers}","\\section{Extended solved problems}"]
    for p in chapters:
        t=p.read_text(encoding="utf-8")
        for x in deprecated:
            if x in t: fail.append(f"{p.relative_to(repo)}: deprecated heading {x}")

    audit=repo/"reports"/"series"/"C05_CHAPTER_STRUCTURE_AUDIT.tsv"
    if not audit.exists():
        fail.append("missing C05 chapter structure audit")
    else:
        rows=list(csv.DictReader(audit.open(encoding="utf-8"),delimiter="\t"))
        if len(rows)!=len(chapters):
            fail.append(f"audit row count {len(rows)} != canonical chapter count {len(chapters)}")

    contract=repo/"editorial"/"C05_CHAPTER_CONTRACT.md"
    if not contract.exists(): fail.append("missing C05 chapter contract")

    if fail:
        print("C05 QA FAIL")
        for x in fail: print("  "+x)
        return 1
    print(f"C05 QA PASS — {len(chapters)} canonical chapters audited; deprecated solved-dossier headings eliminated.")
    return 0

if __name__=="__main__": raise SystemExit(main())
