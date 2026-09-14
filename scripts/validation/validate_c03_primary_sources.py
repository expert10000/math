#!/usr/bin/env python3
import argparse
from pathlib import Path

VOLS=[
"vol01_linear_algebra","vol02_real_analysis","vol03_fourier_distributions_pde",
"vol04_complex_analysis","vol05_commutative_algebra","vol06_algebraic_geometry",
"vol07_differential_geometry","vol08_algebraic_topology"]

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--repo",required=True); a=ap.parse_args()
    repo=Path(a.repo).resolve(); fail=[]
    bib=repo/"references"/"series_primary_sources.bib"
    if not bib.exists():
        fail.append("missing series bibliography")
    else:
        txt=bib.read_text(encoding="utf-8")
        for k in ["GrothendieckTohoku1957","SerreFAC1955","EGAI1960","MitchellMountPapadimitriou1987","Surazhsky2005","CraneWeischedelWardetzky2013","PinkallPolthier1993","Thom1954"]:
            if "{"+k+"," not in txt:
                fail.append("bibliography missing "+k)

    for d in VOLS:
        v=repo/"books"/d
        p=v/"backmatter"/"sources-and-further-reading.tex"
        if not p.exists():
            fail.append(f"{d}: missing source guide")
            continue
        if "Sources and Further Reading" not in p.read_text(encoding="utf-8"):
            fail.append(f"{d}: malformed source guide")
        b=(v/"book.tex").read_text(encoding="utf-8-sig")
        if r"\input{backmatter/sources-and-further-reading.tex}" not in b:
            fail.append(f"{d}: source guide not included")

    checks=[
      ("books/vol04_complex_analysis/backmatter/sources-and-further-reading.tex","IV/24--IV/31"),
      ("books/vol05_commutative_algebra/backmatter/sources-and-further-reading.tex","Cartan--Eilenberg"),
      ("books/vol06_algebraic_geometry/backmatter/sources-and-further-reading.tex","Serre, FAC"),
      ("books/vol06_algebraic_geometry/backmatter/sources-and-further-reading.tex","Stacks Project"),
      ("books/vol07_differential_geometry/backmatter/sources-and-further-reading.tex","VII/40"),
      ("books/vol07_differential_geometry/backmatter/sources-and-further-reading.tex","10.1145/2516971.2516977"),
      ("books/vol07_differential_geometry/backmatter/sources-and-further-reading.tex","VII/41"),
      ("books/vol08_algebraic_topology/backmatter/sources-and-further-reading.tex","Thom (1954)")
    ]
    for rel,phrase in checks:
        p=repo/rel
        if not p.exists() or phrase not in p.read_text(encoding="utf-8"):
            fail.append(f"{rel}: missing '{phrase}'")

    for rel in ["editorial/C03_PRIMARY_SOURCE_LEDGER.tsv","editorial/C03_BIBLIOGRAPHY_POLICY.md"]:
        if not (repo/rel).exists(): fail.append("missing "+rel)

    if fail:
        print("C03 QA FAIL")
        for x in fail: print("  "+x)
        return 1
    print("C03 QA PASS — bibliography and source guides present across I-VIII.")
    return 0

if __name__=="__main__": raise SystemExit(main())
