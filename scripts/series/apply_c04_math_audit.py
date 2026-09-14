#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import re
from pathlib import Path

FRONTMATTER = {
"vol04_complex_analysis": r"""\chapter*{Hypotheses and Conventions Audit}
\phantomsection
\addcontentsline{toc}{chapter}{Hypotheses and Conventions Audit}

\section*{Branches and logarithms}
A branch of the logarithm is always understood on an explicitly specified
domain admitting a continuous argument.  Statements involving powers
\(z^\alpha=\exp(\alpha\operatorname{Log} z)\) inherit that branch choice.  Branch-cut
identities are not treated as global identities on \(\mathbb C^\times\).

\section*{Orientation and winding number}
Positively oriented simple closed contours are counterclockwise unless stated
otherwise.  The winding number is
\[
\operatorname{Ind}(\gamma,a)=\frac{1}{2\pi i}\int_\gamma\frac{dz}{z-a}.
\]
Residue-theorem signs follow this orientation convention.

\section*{Riemann-surface conventions}
Compactification, genus, divisor, and elliptic-function statements are to be
read with the hypotheses stated in the corresponding theorem.  Local
holomorphic coordinates are complex-oriented, and lattice quotients
\(\mathbb C/\Lambda\) use full rank-two lattices unless explicitly generalized.
""",
"vol05_commutative_algebra": r"""\chapter*{Hypotheses and Conventions Audit}
\phantomsection
\addcontentsline{toc}{chapter}{Hypotheses and Conventions Audit}

\section*{Modules and sidedness}
Unless explicitly stated otherwise, rings are unital and modules are left
modules.  For commutative rings the left/right distinction is suppressed.

\section*{Complexes and grading}
Chain complexes are homologically graded:
\[
\cdots\longrightarrow C_{n+1}\xrightarrow{d_{n+1}}C_n
\xrightarrow{d_n}C_{n-1}\longrightarrow\cdots,
\qquad d_n d_{n+1}=0.
\]
Cochain complexes are cohomologically graded with differential of degree \(+1\).
Connecting morphisms and long exact sequences use these conventions.

\section*{Tensor, Hom, Ext, and Tor}
Variance and module structures must be checked before applying adjunction,
derived-functor, or base-change statements.  Flatness/projectivity/injectivity
hypotheses are not to be silently omitted.
""",
"vol06_algebraic_geometry": r"""\chapter*{Hypotheses and Conventions Audit}
\phantomsection
\addcontentsline{toc}{chapter}{Hypotheses and Conventions Audit}

\section*{Base fields and points}
Claims about rational points, closed points, maximal ideals, irreducibility, or
the Nullstellensatz must state the relevant hypothesis on the base field.
In particular, algebraically closed, infinite, finite, and arbitrary fields are
not interchangeable.

\section*{Sheaf epimorphisms}
An epimorphism of sheaves is understood categorically (equivalently, stalkwise
surjective for sheaves of sets/groups/modules in the usual settings).  It need
not be surjective on sections over every open set.

\section*{Quasi-coherence and finiteness}
Statements about quasi-coherent or coherent sheaves, direct images, cohomology,
and base change are read with the stated quasi-compactness, quasi-separatedness,
Noetherian, finite-type, flatness, or properness hypotheses.  Such hypotheses
must not be inferred from notation alone.
""",
"vol07_differential_geometry": r"""\chapter*{Hypotheses and Conventions Audit}
\phantomsection
\addcontentsline{toc}{chapter}{Hypotheses and Conventions Audit}

\section*{Riemannian and Lorentzian signatures}
Riemannian metrics are positive definite.  Lorentzian metrics use one timelike
direction; any local sign convention used in a Lorentzian chapter is stated
there explicitly.

\section*{Curvature convention}
The Riemann tensor convention is
\[
R(X,Y)Z=\nabla_X\nabla_Y Z-\nabla_Y\nabla_X Z-\nabla_{[X,Y]}Z.
\]
The Ricci tensor is the trace \( \operatorname{Ric}(Y,Z)=
\operatorname{tr}(X\mapsto R(X,Y)Z)\).  Sectional, Gaussian, scalar, and mean
curvature signs are interpreted consistently with the definitions in their
chapters.

\section*{Numerical geometry}
Discrete and numerical statements require the mesh regularity, boundary
conditions, discretization, solver tolerance, and refinement assumptions stated
in the corresponding computational chapter.  Numerical agreement is not a
substitute for the smooth theorem being approximated.
"""
}

AUDIT_ROWS = [
("IV","IV/14--IV/15","branches/logarithm","branch domain and chosen argument","changing branch changes powers/logarithms","Ahlfors; Forster","CONVENTION_FIXED"),
("IV","IV/04--IV/13","contour orientation/residue","positive orientation and winding-number sign","orientation reversal changes signs","Ahlfors","CONVENTION_FIXED"),
("IV","IV/24--IV/31","compactification/genus/elliptic normalization","compact Riemann surface and full lattice assumptions where used","dropping compactness/full lattice changes theorem","Forster; Farkas--Kra","AUDIT_GATED"),
("V","V/22--V/28","complex grading","homological differential degree -1; cohomological degree +1","wrong grading reverses connecting-map signs","Cartan--Eilenberg; Mac Lane","CONVENTION_FIXED"),
("V","V/09--V/28","module sidedness","left modules unless commutative context suppresses distinction","noncommutative tensor/Hom formulas can fail","Cartan--Eilenberg","CONVENTION_FIXED"),
("VI","VI/01--VI/11","base-field dependence","state algebraically closed/infinite/finite/arbitrary field hypotheses","finite/nonclosed fields change point/maximal-ideal claims","Hartshorne; Stacks Project","NEGATIVE_TEST_REQUIRED"),
("VI","VI/12--VI/17","sheaf epimorphism","categorical/stalkwise surjectivity, not sectionwise surjectivity","global/open-section surjectivity can fail","Stacks Project","CONVENTION_FIXED"),
("VI","VI/18--VI/49","qc/coherent/cohomology hypotheses","record qcqs/Noetherian/proper/flat hypotheses theorem-by-theorem","dropping finiteness/separation hypotheses can break conclusions","EGA; Hartshorne; Stacks Project","AUDIT_GATED"),
("VII","VII/20--VII/30","curvature/sign convention","R(X,Y)Z convention fixed series-wide","opposite convention flips curvature tensors/signs","do Carmo; Lee","CONVENTION_FIXED"),
("VII","VII/23","Hopf--Rinow","connected Riemannian manifold; metric/geodesic completeness equivalence","without completeness global minimizers need not exist","Hopf--Rinow; do Carmo; Lee","FIXED"),
("VII","VII/38--VII/42","numerical assumptions","state boundary, mesh regularity, discretization and tolerance assumptions","poor meshes/boundaries can invalidate convergence claims","primary computational references","AUDIT_GATED"),
]

HOPF_SECTION = r"""\section{Geodesic completeness and Hopf--Rinow}

\begin{definition}[Geodesically complete]\label{def:vii23-complete}
A Riemannian manifold is geodesically complete if every maximal geodesic is
defined for all \(t\in\mathbb R\).
\end{definition}

\begin{theorem}[Hopf--Rinow]\label{thm:vii23-hopf-rinow}
Let \((M,g)\) be a connected Riemannian manifold, with Riemannian distance \(d_g\).
The following conditions are equivalent:
\begin{enumerate}
\item \((M,d_g)\) is a complete metric space;
\item \(M\) is geodesically complete;
\item for some (equivalently every) \(p\in M\), the exponential map
      \(\exp_p\) is defined on all of \(T_pM\).
\end{enumerate}
When these conditions hold, every two points of \(M\) can be joined by a
length-minimizing geodesic.
\end{theorem}

\begin{remark}
The theorem is global: the local existence of geodesics and local normal
coordinates proved earlier do not by themselves imply global minimizing
geodesics.  Completeness is the additional hypothesis that closes this gap.
\end{remark}
"""

def ensure_include(book: Path):
    raw = book.read_text(encoding="utf-8-sig")
    marker = r"\input{frontmatter/c04-hypotheses-and-conventions.tex}"
    if marker in raw:
        return
    anchor = r"\input{frontmatter/publication-and-scope.tex}"
    if anchor in raw:
        raw = raw.replace(anchor, anchor + "\n" + marker, 1)
    elif r"\tableofcontents" in raw:
        raw = raw.replace(r"\tableofcontents", r"\tableofcontents" + "\n" + marker, 1)
    else:
        raise RuntimeError(f"No frontmatter insertion point: {book}")
    book.write_text(raw, encoding="utf-8", newline="\n")

def replace_hopf(path: Path):
    raw = path.read_text(encoding="utf-8")
    if r"\begin{theorem}[Hopf--Rinow]" in raw:
        return
    rx = re.compile(
        r"\\section\{Geodesic completeness preview\}.*?"
        r"(?=\\section\{Exercises\})",
        re.S,
    )
    new, n = rx.subn(lambda _m: HOPF_SECTION + "\n", raw, count=1)
    if n != 1:
        raise RuntimeError("Could not uniquely replace VII/23 completeness preview.")
    path.write_text(new, encoding="utf-8", newline="\n")

def field_scan(repo: Path):
    out = repo/"reports"/"series"
    out.mkdir(parents=True, exist_ok=True)
    target = out/"C04_VI_FIELD_DEPENDENCE_SCAN.tsv"
    keys = re.compile(
        r"\b(algebraically closed|infinite field|finite field|closed point|rational point|maximal ideal|geometrically irreducible|geometric irreducibility)\b",
        re.I,
    )
    rows=[]
    base=repo/"books"/"vol06_algebraic_geometry"/"chapters"
    for ch in sorted(base.glob("ch*/**/*.tex")):
        m=re.match(r"ch(\d+)_", ch.parts[-3] if len(ch.parts)>=3 else "")
        # simpler path filter via first chapter directory under chapters
        rel=ch.relative_to(base).as_posix()
        cm=re.match(r"ch(\d+)_", rel)
        if not cm or int(cm.group(1))>11:
            continue
        for i,line in enumerate(ch.read_text(encoding="utf-8").splitlines(),1):
            if keys.search(line):
                rows.append((ch.relative_to(repo).as_posix(),i,line.strip()))
    with target.open("w",encoding="utf-8",newline="") as f:
        w=csv.writer(f,delimiter="\t",lineterminator="\n")
        w.writerow(["file","line","field_dependent_text"])
        w.writerows(rows)
    return len(rows)

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--repo",required=True); a=ap.parse_args()
    repo=Path(a.repo).resolve()

    for d,content in FRONTMATTER.items():
        v=repo/"books"/d
        fm=v/"frontmatter"
        fm.mkdir(parents=True,exist_ok=True)
        (fm/"c04-hypotheses-and-conventions.tex").write_text(content,encoding="utf-8",newline="\n")
        ensure_include(v/"book.tex")

    replace_hopf(repo/"books"/"vol07_differential_geometry"/"chapters"/"ch23_geodesics"/"chapter.tex")

    editorial=repo/"editorial"
    editorial.mkdir(parents=True,exist_ok=True)
    with (editorial/"C04_THEOREM_AUDIT.tsv").open("w",encoding="utf-8",newline="") as f:
        w=csv.writer(f,delimiter="\t",lineterminator="\n")
        w.writerow(["volume","location","topic","hypotheses_or_convention","negative_test","reference","status"])
        w.writerows(AUDIT_ROWS)

    neg = """# C04 negative-test protocol

The theorem audit is not complete until hypotheses are tested against failure cases.

## Volume IV
- Reverse contour orientation and verify winding/residue signs.
- Change a logarithm branch and identify which power/log identities cease to be global.
- Drop compactness or the full-lattice assumption in Riemann-surface/elliptic statements.

## Volume V
- Switch homological/cohomological grading and track the connecting-map sign.
- Test tensor/Hom statements over a noncommutative ring where left/right module structure matters.
- Remove flat/projective/injective hypotheses from derived-functor shortcuts.

## Volume VI
- Replace an algebraically closed field by R or a finite field.
- Test rational point = closed point / maximal ideal claims under that change.
- Compare sheaf epimorphism with sectionwise surjectivity on open sets.
- Remove qcqs/Noetherian/proper/flat hypotheses from sheaf/cohomology statements and record the failure.

## Volume VII
- Reverse the Riemann tensor sign convention and track Ricci/sectional consequences.
- Remove metric/geodesic completeness from global minimizing-geodesic claims.
- Vary mesh boundary conditions, scale, noise, and triangle quality in computational statements.
"""
    (editorial/"C04_NEGATIVE_TESTS.md").write_text(neg,encoding="utf-8",newline="\n")

    n=field_scan(repo)
    print(f"C04 applied. VI/01--VI/11 field-dependence scan recorded {n} candidate lines.")
    return 0

if __name__=="__main__":
    raise SystemExit(main())
