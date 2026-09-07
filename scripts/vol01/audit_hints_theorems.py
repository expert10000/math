#!/usr/bin/env python3
from __future__ import annotations
import argparse, csv, json, re
from pathlib import Path

CH = {
    1: "books/vol01_linear_algebra/chapters/ch01_scalars_vectors_and_linear_combinations/chapter.tex",
    2: "books/vol01_linear_algebra/chapters/ch02_subspaces_span_and_linear_independence/chapter.tex",
    3: "books/vol01_linear_algebra/chapters/ch03_bases_and_dimension/chapter.tex",
    4: "books/vol01_linear_algebra/chapters/ch04_coordinates_and_change_of_basis/chapter.tex",
    5: "books/vol01_linear_algebra/chapters/ch05_linear_transformations/chapter.tex",
    6: "books/vol01_linear_algebra/chapters/ch06_kernels_images_and_isomorphisms/chapter.tex",
    7: "books/vol01_linear_algebra/chapters/ch07_matrix_representation_of_linear_maps/chapter.tex",
    8: "books/vol01_linear_algebra/chapters/ch08_determinants_and_trace/chapter.tex",
    9: "books/vol01_linear_algebra/chapters/ch09_eigenvalues_and_eigenvectors/chapter.tex",
    10: "books/vol01_linear_algebra/chapters/ch10_invariant_subspaces_and_triangularization/chapter.tex",
    11: "books/vol01_linear_algebra/chapters/ch11_diagonalization_and_minimal_polynomials/chapter.tex",
    12: "books/vol01_linear_algebra/chapters/ch12_canonical_forms/chapter.tex",
    13: "books/vol01_linear_algebra/chapters/ch13_inner_products_and_orthogonality/chapter.tex",
    14: "books/vol01_linear_algebra/chapters/ch14_gram_schmidt_and_orthogonal_projection/chapter.tex",
    15: "books/vol01_linear_algebra/chapters/ch15_orthogonal_and_unitary_operators/chapter.tex",
    16: "books/vol01_linear_algebra/chapters/ch16_the_spectral_theorem/chapter.tex",
    17: "books/vol01_linear_algebra/chapters/ch17_quadratic_forms/chapter.tex",
    18: "books/vol01_linear_algebra/chapters/ch18_singular_value_decomposition/chapter.tex",
}
THEOREMS = [
    (11,"thm:i11-03","Cayley--Hamilton theorem"),
    (13,"thm:i13-03","Finite-dimensional orthogonal decomposition"),
    (16,"thm:i16-03","Normal spectral theorem"),
    (18,"thm:i18-03","Eckart--Young--Mirsky theorem"),
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
    ap=argparse.ArgumentParser();ap.add_argument("--repo",required=True);ap.add_argument("--spec",required=True)
    a=ap.parse_args();repo=Path(a.repo).resolve();reports=repo/"reports/vol01";reports.mkdir(parents=True,exist_ok=True)
    spec=json.loads(Path(a.spec).read_text(encoding="utf-8"))
    texts={n:read(repo,n) for n in CH}; blocking=[]; rows=[]
    for label,expected in spec.items():
        m=re.match(r"exr:i(\d\d)-",label)
        if not m:
            blocking.append(f"bad spec label {label}");continue
        n=int(m.group(1)); actual=extract_hint(texts[n],label)
        ok=(actual==expected)
        rows.append({"label":label,"chapter":f"I/{n:02d}","status":"PASS" if ok else "FAIL","hint":actual or ""})
        if not ok: blocking.append(f"hint mismatch: {label}")
    write_tsv(reports/"VOL01_HINT_RECONCILIATION.tsv",rows,["label","chapter","status","hint"])

    trows=[]
    for n,label,title in THEOREMS:
        ok=(f"\\label{{{label}}}" in texts[n] and title in texts[n])
        trows.append({"chapter":f"I/{n:02d}","label":label,"theorem":title,"status":"PASS" if ok else "FAIL"})
        if not ok: blocking.append(f"missing theorem coverage: {label}")
    # Supporting claims should now be backed explicitly.
    if "By the Cayley--Hamilton theorem" not in texts[11]: blocking.append("I11 minimal-polynomial divisibility not tied to Cayley--Hamilton")
    if "V=U\\oplus U^\\perp" not in texts[13]: blocking.append("I13 orthogonal decomposition theorem statement missing")
    if "normal if and only if it is unitarily" not in texts[16]: blocking.append("I16 normal spectral theorem statement missing")
    if "minimizes both the operator and Frobenius" not in texts[18]: blocking.append("I18 Eckart--Young--Mirsky statement missing")
    write_tsv(reports/"VOL01_THEOREM_COVERAGE.tsv",trows,["chapter","label","theorem","status"])

    obj={"schema":1,"status":"PASS" if not blocking else "FAIL","hints_checked":len(rows),"theorems_added":len(trows),"blocking":blocking}
    (reports/"VOL01_HINT_THEOREM_AUDIT.json").write_text(json.dumps(obj,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    md=["# Volume I — hint and theorem coverage audit","",f"**Status:** {obj['status']}","",f"- Curated hints checked: **{len(rows)}**",f"- Structural theorems checked: **{len(trows)}**","","## Blocking findings",""]
    md += ["None."] if not blocking else [f"- {x}" for x in blocking]
    (reports/"VOL01_HINT_THEOREM_AUDIT.md").write_text("\n".join(md)+"\n",encoding="utf-8")
    print(json.dumps(obj,indent=2,ensure_ascii=False))
    return 0 if obj["status"]=="PASS" else 5
if __name__=="__main__":raise SystemExit(main())
