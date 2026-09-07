#!/usr/bin/env python3
from __future__ import annotations
import argparse, csv, json, re
from pathlib import Path

CH = {
    1: "books/vol02_real_analysis/chapters/ch01_the_real_number_system_and_completeness/chapter.tex",
    2: "books/vol02_real_analysis/chapters/ch02_euclidean_and_normed_spaces/chapter.tex",
    3: "books/vol02_real_analysis/chapters/ch03_sequences_and_cauchy_sequences/chapter.tex",
    4: "books/vol02_real_analysis/chapters/ch04_open_and_closed_sets/chapter.tex",
    5: "books/vol02_real_analysis/chapters/ch05_metric_spaces_and_continuity/chapter.tex",
    6: "books/vol02_real_analysis/chapters/ch06_compactness/chapter.tex",
    7: "books/vol02_real_analysis/chapters/ch07_connectedness_and_path_connectedness/chapter.tex",
    8: "books/vol02_real_analysis/chapters/ch08_differentiability_in_several_variables/chapter.tex",
    9: "books/vol02_real_analysis/chapters/ch09_inverse_and_implicit_function_principles/chapter.tex",
    10: "books/vol02_real_analysis/chapters/ch10_riemann_integration/chapter.tex",
    11: "books/vol02_real_analysis/chapters/ch11_pointwise_and_uniform_convergence/chapter.tex",
    12: "books/vol02_real_analysis/chapters/ch12_interchanging_limits_derivatives_and_integrals/chapter.tex",
    13: "books/vol02_real_analysis/chapters/ch13_infinite_series_of_functions/chapter.tex",
    14: "books/vol02_real_analysis/chapters/ch14_trigonometric_series/chapter.tex",
    15: "books/vol02_real_analysis/chapters/ch15_pathological_and_nowhere_differentiable_functions/chapter.tex",
    16: "books/vol02_real_analysis/chapters/ch16_contraction_mappings/chapter.tex",
    17: "books/vol02_real_analysis/chapters/ch17_brouwer_type_fixed_point_ideas/chapter.tex",
    18: "books/vol02_real_analysis/chapters/ch18_integral_equations/chapter.tex",
    19: "books/vol02_real_analysis/chapters/ch19_elementary_existence_theory_for_odes/chapter.tex",
    20: "books/vol02_real_analysis/chapters/ch20_polynomial_interpolation/chapter.tex",
    21: "books/vol02_real_analysis/chapters/ch21_polynomial_approximation/chapter.tex",
    22: "books/vol02_real_analysis/chapters/ch22_chebyshev_and_minimax_approximation/chapter.tex",
    23: "books/vol02_real_analysis/chapters/ch23_the_alternation_principle/chapter.tex",
    24: "books/vol02_real_analysis/chapters/ch24_numerical_quadrature/chapter.tex",
    25: "books/vol02_real_analysis/chapters/ch25_continued_fractions_and_approximation_topics/chapter.tex",
}

THEOREMS = [
    (6,"thm:ii06-04","Heine--Borel theorem","added"),
    (6,"thm:ii06-05","Compact metric criterion","added"),
    (7,"thm:ii07-04","Connected subsets of the real line","added"),
    (8,"thm:ii08-04","Continuous first partials imply differentiability","added"),
    (10,"thm:ii10-04","Monotone functions are Riemann integrable","added"),
    (11,"thm:ii11-04","Completeness of the sup-norm function space","added"),
    (13,"thm:ii13-04","Termwise differentiation of a function series","added"),
    (14,"thm:ii14-04","Finite Fourier projection","added"),
    (15,"thm:ii15-03","Hölder roughness principle","repaired"),
    (17,"thm:ii17-02","Brouwer fixed-point theorem","proof-scope clarified"),
    (18,"thm:ii18-01","Neumann-series inversion","Banach hypothesis repaired"),
    (19,"thm:ii19-04","Peano local existence theorem","added"),
    (25,"thm:ii25-04","Lagrange continued-fraction theorem","added"),
]


def read(repo: Path,n:int):
    return (repo/CH[n]).read_text(encoding="utf-8-sig",errors="replace")


def extract_hint(text,label):
    pat=rf"\\begin\{{exercise\}}(?:\[[^\]]*\])?\\label\{{{re.escape(label)}\}}.*?\\end\{{exercise\}}\s*\\begin\{{hint\}}\n(.*?)\n\\end\{{hint\}}"
    m=re.search(pat,text,flags=re.S)
    return m.group(1).strip() if m else None


def write_tsv(path,rows,fields):
    path.parent.mkdir(parents=True,exist_ok=True)
    with path.open("w",encoding="utf-8",newline="") as f:
        w=csv.DictWriter(f,fieldnames=fields,delimiter="\t",lineterminator="\n");w.writeheader();w.writerows(rows)


def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--repo",required=True); ap.add_argument("--spec",required=True)
    args=ap.parse_args(); repo=Path(args.repo).resolve(); reports=repo/"reports/vol02"; reports.mkdir(parents=True,exist_ok=True)
    overrides=json.loads(Path(args.spec).read_text(encoding="utf-8"))
    texts={n:read(repo,n) for n in CH}; blocking=[]; rows=[]

    # All 25 x 8 preserved core exercise hints must exist and must have had the
    # mechanically appended second-hint tail removed.
    contamination=re.compile(r"[.!?]\s+(?:Use|For|To|Check|Compute|Apply|Write|Estimate|Compare|Recall|Choose|Try|Keep|Start|When|If)\b")
    for n in range(1,26):
        for k in range(1,9):
            label=f"exr:ii{n:02d}-{k:02d}"
            actual=extract_hint(texts[n],label)
            status="PASS"
            if actual is None:
                blocking.append(f"missing core hint: {label}"); status="FAIL"; actual=""
            else:
                compact=" ".join(actual.split())
                if len(compact)>320:
                    blocking.append(f"overlong core hint: {label}"); status="FAIL"
                if contamination.search(compact):
                    blocking.append(f"possible concatenated hint remains: {label}"); status="FAIL"
                if label in overrides and actual.strip()!=overrides[label].strip():
                    blocking.append(f"curated hint mismatch: {label}"); status="FAIL"
            rows.append({"label":label,"chapter":f"II/{n:02d}","status":status,"hint":actual})
    write_tsv(reports/"VOL02_HINT_RECONCILIATION.tsv",rows,["label","chapter","status","hint"])

    trows=[]
    for n,label,title,kind in THEOREMS:
        ok=(f"\\label{{{label}}}" in texts[n] and title in texts[n])
        trows.append({"chapter":f"II/{n:02d}","label":label,"theorem":title,"coverage":kind,"status":"PASS" if ok else "FAIL"})
        if not ok: blocking.append(f"missing theorem coverage: {label}")
    if "no uniform bound on difference quotients" not in texts[15]: blocking.append("II15 Holder theorem precision missing")
    if "Proof sketch." not in texts[17]: blocking.append("II17 Brouwer proof is not explicitly scoped as a sketch")
    if "Let $X$ be a Banach space" not in texts[18]: blocking.append("II18 Neumann Banach hypothesis missing")
    if "Continuity alone does not guarantee uniqueness" not in texts[19]: blocking.append("II19 Peano existence/uniqueness distinction missing")
    if "eventually periodic simple continued fraction" not in texts[25]: blocking.append("II25 Lagrange periodicity theorem missing")
    write_tsv(reports/"VOL02_THEOREM_COVERAGE.tsv",trows,["chapter","label","theorem","coverage","status"])

    obj={
        "schema":1,
        "status":"PASS" if not blocking else "FAIL",
        "hints_checked":len(rows),
        "curated_hint_overrides":len(overrides),
        "theorem_coverage_rows":len(trows),
        "blocking":blocking,
    }
    (reports/"VOL02_HINT_THEOREM_AUDIT.json").write_text(json.dumps(obj,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    md=["# Volume II — hint and theorem coverage audit","",f"**Status:** {obj['status']}","",f"- Core hints checked: **{len(rows)}**",f"- Curated overrides: **{len(overrides)}**",f"- Theorem-coverage rows: **{len(trows)}**","","## Blocking findings",""]
    md += ["None."] if not blocking else [f"- {x}" for x in blocking]
    (reports/"VOL02_HINT_THEOREM_AUDIT.md").write_text("\n".join(md)+"\n",encoding="utf-8")
    print(json.dumps(obj,indent=2,ensure_ascii=False))
    return 0 if obj["status"]=="PASS" else 5

if __name__=="__main__": raise SystemExit(main())
