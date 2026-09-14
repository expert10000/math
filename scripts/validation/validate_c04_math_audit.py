#!/usr/bin/env python3
import argparse, csv, re
from pathlib import Path

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--repo",required=True); a=ap.parse_args()
    repo=Path(a.repo).resolve(); fail=[]

    for d in ["vol04_complex_analysis","vol05_commutative_algebra","vol06_algebraic_geometry","vol07_differential_geometry"]:
        v=repo/"books"/d
        fm=v/"frontmatter"/"c04-hypotheses-and-conventions.tex"
        if not fm.exists():
            fail.append(f"{d}: missing C04 convention note")
        else:
            fmtxt=fm.read_text(encoding="utf-8")
            if r"\\Log" in fmtxt:
                fail.append(f"{d}: undefined \\Log command remains in C04 convention note")
        b=(v/"book.tex").read_text(encoding="utf-8-sig")
        if r"\input{frontmatter/c04-hypotheses-and-conventions.tex}" not in b:
            fail.append(f"{d}: C04 convention note not included")

    vii=repo/"books"/"vol07_differential_geometry"/"chapters"/"ch23_geodesics"/"chapter.tex"
    t=vii.read_text(encoding="utf-8")
    for phrase in [r"\begin{theorem}[Hopf--Rinow]", "complete metric space", "length-minimizing geodesic"]:
        if phrase not in t: fail.append(f"VII/23 missing {phrase}")
    if "Hopf--Rinow theorem later links" in t:
        fail.append("VII/23 stale Hopf--Rinow forward reference remains")

    audit=repo/"editorial"/"C04_THEOREM_AUDIT.tsv"
    if not audit.exists():
        fail.append("missing C04 theorem audit")
    else:
        rows=list(csv.DictReader(audit.open(encoding="utf-8"),delimiter="\t"))
        if len(rows)<10: fail.append("C04 theorem audit too small")
        required={"IV","V","VI","VII"}
        got={r["volume"] for r in rows}
        if not required.issubset(got): fail.append("C04 theorem audit missing target volumes")

    scan=repo/"reports"/"series"/"C04_VI_FIELD_DEPENDENCE_SCAN.tsv"
    if not scan.exists(): fail.append("missing VI field-dependence scan")
    neg=repo/"editorial"/"C04_NEGATIVE_TESTS.md"
    if not neg.exists(): fail.append("missing negative-test protocol")

    if fail:
        print("C04 QA FAIL")
        for x in fail: print("  "+x)
        return 1
    print("C04 QA PASS — conventions, theorem audit, negative tests, VI field scan, and Hopf--Rinow integration present.")
    return 0

if __name__=="__main__": raise SystemExit(main())
