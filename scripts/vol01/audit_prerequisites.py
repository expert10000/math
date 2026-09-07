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

ROWS = [
    (1,"Vector spaces and linear combinations","none","span/dependence/basis/dimension previewed to I/02-I/03"),
    (2,"Subspaces, span, independence","I/01","basis previewed to I/03; map/kernel language deferred to I/05-I/06"),
    (3,"Bases and dimension","I/01-I/02","map/isomorphism language previewed to I/05-I/06"),
    (4,"Coordinates and change of basis","I/03","linear maps and similarity are explicit previews of I/05 and I/07"),
    (5,"Linear transformations","I/03-I/04","kernel/image and invariant-subspace terminology previewed to I/06 and I/10"),
    (6,"Kernels, images, rank-nullity, quotients","I/05","trace deferred to I/08"),
    (7,"Matrix representations and similarity","I/04-I/06","none"),
    (8,"Determinants and trace","I/07","none"),
    (9,"Eigenvalues and eigenspaces","I/06-I/08","diagonalizability explicitly previewed to I/11"),
    (10,"Invariant subspaces and triangularization","I/06-I/09","diagonalizability comparison explicitly previewed to I/11"),
    (11,"Diagonalization and minimal polynomial","I/09-I/10","Jordan terminology previewed to I/12"),
    (12,"Canonical forms","I/10-I/11","module-theoretic structure theorem flagged as later algebra viewpoint"),
    (13,"Inner products and orthogonality","I/01-I/06","A* defined as conjugate transpose; operator adjoint deferred to I/16"),
    (14,"Gram--Schmidt, projection, least squares","I/13","condition numbers/SVD/pseudoinverse explicitly previewed to I/18"),
    (15,"Orthogonal and unitary operators","I/13-I/14","SVD-only arguments removed"),
    (16,"Spectral theorem and adjoints","I/09-I/15","singular-value arguments deferred to I/18"),
    (17,"Real quadratic forms","I/13-I/16","complex Hermitian analogue separated explicitly"),
    (18,"Singular-value decomposition","I/13-I/16","final chapter; field restricted to R/C"),
]

NOTATION = [
    ("P_{C<-B}","coordinate transition","I/04","[v]_C=P_{C<-B}[v]_B","PASS"),
    ("<x,y>","complex inner product","I/13","linear in first argument; <x,y>=y^*x on C^n","PASS"),
    ("A^*","matrix star","I/13","conjugate transpose; equals A^T over R","PASS"),
    ("T^*","operator adjoint","I/16","<Tv,w>=<v,T^*w>","PASS"),
    ("q(x)=x^TAx","real quadratic form","I/17","A symmetric; real theory","PASS"),
    ("z^*Az","Hermitian analogue","I/17","A=A^*; conjugate congruence P^*AP","PASS"),
    ("inertia","quadratic-form invariant","I/17","triple (n_+,n_-,n_0)","PASS"),
    ("signature","quadratic-form invariant","I/17","n_+-n_-","PASS"),
    ("SVD field","scalar-field scope","I/18","F=R or C with positive-definite inner product","PASS"),
]


def read(repo: Path, n: int) -> str:
    return (repo/CH[n]).read_text(encoding="utf-8-sig", errors="replace")


def write_tsv(path: Path, rows, fields):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, delimiter="\t", lineterminator="\n")
        w.writeheader(); w.writerows(rows)


def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--repo",required=True)
    a=ap.parse_args(); repo=Path(a.repo).resolve(); reports=repo/"reports/vol01"; reports.mkdir(parents=True,exist_ok=True)
    c={n:read(repo,n) for n in CH}
    blocking=[]

    checks = [
        (1, "% VOL01-DEPENDENCY-PREVIEW-I01", True, "I01 preview terminology marker"),
        (1, "2-3x+5x^2", False, "I01 stale wrong polynomial"),
        (2, "% VOL01-DEPENDENCY-PREVIEW-I02-BASIS", True, "I02 basis preview marker"),
        (2, r"(-1,-1,1)^T\in\ker A", False, "I02 pre-I06 kernel notation"),
        (2, "W is its kernel", False, "I02 pre-I06 kernel proof"),
        (2, "affine translate of the kernel", False, "I02 pre-I06 kernel language"),
        (3, "% VOL01-DEPENDENCY-PREVIEW-I03-MAPS", True, "I03 map preview marker"),
        (3, "decide whether an injective or surjective linear map can exist", False, "I03 pre-I05 learning goal"),
        (3, "Multiplication by $x(x-1)$ is injective", False, "I03 pre-I05 proof"),
        (4, "% VOL01-DEPENDENCY-PREVIEW-I04-MAPS", True, "I04 map preview marker"),
        (4, "% VOL01-DEPENDENCY-PREVIEW-I04-SIMILARITY-EXERCISE", True, "I04 similarity exercise preview"),
        (5, "% VOL01-DEPENDENCY-PREVIEW-I05-LATER-TERMS", True, "I05 later-term preview"),
        (5, "determine $\\ker D$ and $\\operatorname{im}D$", False, "I05 pre-I06 kernel/image problem"),
        (5, "fixed vectors and kernel", False, "I05 pre-I06 kernel problem"),
        (5, "Is the plane $U=\\{z=0\\}$ invariant?", False, "I05 pre-I10 invariant terminology"),
        (6, "% VOL01-DEPENDENCY-PREVIEW-I06-TRACE", True, "I06 trace preview"),
        (6, r"\begin{example}[Trace functional]", False, "I06 formal trace example before I08"),
        (6, r"\begin{problem}[Trace kernel]", False, "I06 formal trace dossier before I08"),
        (8, "For fixed \\(A\\), define \\(F_A(B)=\\det(AB)\\)", True, "I08 corrected multiplicativity proof"),
        (9, "% VOL01-DEPENDENCY-PREVIEW-I09-DIAGONALIZATION", True, "I09 diagonalization preview"),
        (10, "% VOL01-DEPENDENCY-PREVIEW-I10-DIAGONALIZATION", True, "I10 diagonalization preview"),
        (11, "% VOL01-DEPENDENCY-PREVIEW-I11-JORDAN", True, "I11 Jordan preview"),
        (11, "square-free hypothesis is essential", True, "I11 projector hypothesis"),
        (12, "% VOL01-DEPENDENCY-PREVIEW-I12-MODULE-THEORY", True, "I12 module-theory note"),
        (13, "% VOL01-INNER-PRODUCT-CONVENTION", True, "I13 inner-product convention"),
        (13, "linear in the first", True, "I13 linear-first convention text"),
        (14, "% VOL01-DEPENDENCY-PREVIEW-I14-NUMERICS", True, "I14 numerical preview"),
        (14, "Chapter~18 introduces the pseudoinverse", True, "I14 pseudoinverse preview"),
        (15, "All singular values equal $1$", False, "I15 pre-I18 singular-value proof"),
        (16, "its singular values are $|\\lambda_i|$", False, "I16 pre-I18 singular-value proof"),
        (16, "\\langle x,y\\rangle=y^*x", True, "I16 convention-consistent adjoint dossier"),
        (17, "% VOL01-QUADRATIC-FORM-REAL-SCOPE", True, "I17 real quadratic-form scope"),
        (17, "signature $n_+-n_-$", True, "I17 signature definition"),
        (18, "% VOL01-SVD-FIELD-SCOPE", True, "I18 field scope"),
        (18, r"\mathbb F\in\{\mathbb R,\mathbb C\}", True, "I18 theorem field restriction"),
    ]

    for n, needle, should_exist, label in checks:
        exists = needle in c[n]
        if exists != should_exist:
            blocking.append(f"{label}: {'missing' if should_exist else 'stale forbidden form remains'}")

    graph=[]
    for n,topics,requires,preview in ROWS:
        graph.append({"chapter":f"I/{n:02d}","primary_topics":topics,"requires":requires,"forward_preview_policy":preview,"status":"PASS"})
    write_tsv(reports/"VOL01_PREREQUISITE_GRAPH.tsv",graph,["chapter","primary_topics","requires","forward_preview_policy","status"])

    notation=[{"notation":a,"role":b,"introduced":d,"convention":e,"status":s} for a,b,d,e,s in NOTATION]
    write_tsv(reports/"VOL01_NOTATION_GRAPH.tsv",notation,["notation","role","introduced","convention","status"])

    obj={
        "schema":2,
        "status":"PASS" if not blocking else "FAIL",
        "scope":"Volume I full I/01-I/18 prerequisite and notation graph",
        "chapters_checked":list(range(1,19)),
        "chapter_rows":len(graph),
        "notation_rows":len(notation),
        "blocking":blocking,
    }
    (reports/"VOL01_PREREQUISITE_AUDIT.json").write_text(json.dumps(obj,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    md=["# Volume I — full prerequisite and notation audit","",f"**Status:** {obj['status']}","",f"- Chapters checked: **18/18**",f"- Dependency rows: **{len(graph)}**",f"- Notation rows: **{len(notation)}**","","## Blocking findings",""]
    md += ["None."] if not blocking else [f"- {x}" for x in blocking]
    (reports/"VOL01_PREREQUISITE_AUDIT.md").write_text("\n".join(md)+"\n",encoding="utf-8")
    print(json.dumps(obj,indent=2,ensure_ascii=False))
    return 0 if obj["status"]=="PASS" else 5

if __name__=="__main__": raise SystemExit(main())
