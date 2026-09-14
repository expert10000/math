#!/usr/bin/env python3
import argparse
from pathlib import Path

VOLS = [
"vol01_linear_algebra","vol02_real_analysis","vol03_fourier_distributions_pde",
"vol04_complex_analysis","vol05_commutative_algebra","vol06_algebraic_geometry",
"vol07_differential_geometry","vol08_algebraic_topology"
]

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--repo",required=True); a=ap.parse_args()
    repo=Path(a.repo).resolve(); fail=[]
    for rel in [
        "editorial/PUBLICATION_METADATA.yml",
        "editorial/SOURCE_AND_PROVENANCE_POLICY.md",
        "editorial/C02_PUBLICATION_METADATA.md",
        "docs/PUBLICATION_AND_CITATION.md",
    ]:
        if not (repo/rel).exists():
            fail.append("missing "+rel)

    for d in VOLS:
        v=repo/"books"/d
        note=v/"frontmatter"/"publication-and-scope.tex"
        if not note.exists():
            fail.append(f"{d}: missing publication note")
            continue
        t=note.read_text(encoding="utf-8")
        for p in ["Publication, Scope, and Source Note","Audience and prerequisites","Rights and citation status","Source and provenance policy"]:
            if p not in t:
                fail.append(f"{d}: missing {p}")
        b=(v/"book.tex").read_text(encoding="utf-8-sig")
        if r"\input{frontmatter/publication-and-scope.tex}" not in b:
            fail.append(f"{d}: note not included")
        if r"\date{}" in b:
            fail.append(f"{d}: empty date")
        if "Canonical reconstructed mathematics series" in b:
            fail.append(f"{d}: old pdfsubject remains")

    if fail:
        print("C02 QA FAIL")
        for x in fail:
            print("  "+x)
        return 1
    print("C02 QA PASS — all eight volumes have publication/scope metadata.")
    return 0

if __name__=="__main__":
    raise SystemExit(main())
