#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
from pathlib import Path

VOLUMES = {
    "vol01_linear_algebra": ("I", "Linear Algebra", [
        ("I/01--I/06", "Axler; Halmos; Hoffman--Kunze", "Vector spaces, bases, linear maps, kernels, images, and isomorphisms."),
        ("I/07--I/12", "Hoffman--Kunze; Gantmacher", "Matrix representations, determinants, eigenstructure, triangularization, minimal polynomials, and canonical forms."),
        ("I/13--I/18", "Horn--Johnson; Golub--Van Loan; Eckart--Young", "Inner products, orthogonality, the spectral theorem, quadratic forms, and singular-value decomposition."),
    ]),
    "vol02_real_analysis": ("II", "Real Analysis and Topological Foundations", [
        ("II/01--II/06", "Dedekind; Cantor; Rudin", "Completeness, Euclidean/normed structures, metrics, and topological foundations."),
        ("II/07--II/12", "Cauchy; Weierstrass; Rudin", "Sequences, continuity, differentiation, compactness, and convergence."),
        ("II/13--II/18", "Riemann; Lebesgue; Folland", "Integration and the transition from Riemann to measure-theoretic viewpoints."),
        ("II/19--II/25", "Baire; Banach; Rudin", "Function spaces, convergence principles, approximation, and later real-analysis structures."),
    ]),
    "vol03_fourier_distributions_pde": ("III", "Measure, Fourier Analysis, Distributions and PDE", [
        ("III/01--III/08", "Lebesgue; Radon; Folland", "Measure, measurable functions, integration, and convergence theorems."),
        ("III/09--III/17", "Fourier; Plancherel; Stein--Shakarchi", "Fourier series/transforms, orthogonality, spectral viewpoints, and harmonic analysis."),
        ("III/18--III/23", "Schwartz; Hörmander", "Distributions, weak derivatives, convolution, and Fourier analysis of generalized functions."),
        ("III/24--III/28", "Evans; Hörmander", "Weak formulations, fundamental PDE examples, and analytic estimates."),
    ]),
    "vol04_complex_analysis": ("IV", "Complex Analysis and Riemann Surfaces", [
        ("IV/01--IV/14", "Cauchy; Riemann; Ahlfors", "Holomorphicity, Cauchy theory, residues, argument principle, and branches."),
        ("IV/15--IV/23", "Weierstrass; Riemann; Forster", "Analytic continuation, Möbius/conformal geometry, and passage to Riemann surfaces."),
        ("IV/24--IV/31", "Riemann; Weierstrass; Forster; Farkas--Kra", "Branched coverings, compact surfaces, lattices, elliptic functions, and elliptic curves as Riemann surfaces."),
    ]),
    "vol05_commutative_algebra": ("V", "Commutative Algebra and Homological Methods", [
        ("V/01--V/14", "Noether; Atiyah--Macdonald; Matsumura", "Ideals, localization, modules, Noetherian methods, dimension, and structural commutative algebra."),
        ("V/15--V/21", "Hilbert; Artin--Rees; Matsumura", "Finiteness, primary methods, dimension, and local algebra."),
        ("V/22--V/28", "Cartan--Eilenberg; Grothendieck 1957; Mac Lane", "Chain complexes, exactness, derived functors, Ext, Tor, and foundations of homological algebra."),
    ]),
    "vol06_algebraic_geometry": ("VI", "Algebraic Geometry and Sheaf Theory", [
        ("VI/01--VI/11", "Hilbert; Hartshorne; Stacks Project", "Affine algebraic sets/schemes, spectra, morphisms, and field-dependent point questions."),
        ("VI/12--VI/20", "Serre FAC; Grothendieck--Dieudonné EGA I; Hartshorne", "Sheaves, locally ringed spaces, scheme gluing, and quasi-coherent structures."),
        ("VI/21--VI/38", "Grothendieck--Dieudonné EGA; Hartshorne; Stacks Project", "Fiber products, base change, dimension, divisors, and scheme-theoretic constructions."),
        ("VI/39--VI/49", "Serre FAC; EGA; Hartshorne; Stacks Project", "Cohomological and advanced geometric structures; verify exact hypotheses against authoritative modern formulations."),
    ]),
    "vol07_differential_geometry": ("VII", "Differential, Riemannian and Hyperbolic Geometry", [
        ("VII/01--VII/19", "Gauss; do Carmo; Lee", "Smooth manifolds, bundles/forms, curves, surfaces, and classical surface geometry."),
        ("VII/20--VII/30", "Riemann; Levi-Civita; Hopf--Rinow; do Carmo; Lee", "Riemannian/Lorentzian metrics, connections, geodesics, curvature, completeness, and global metric geometry."),
        ("VII/31--VII/37", "Poincaré; Beardon; Ratcliffe", "Hyperbolic models, Möbius actions, Fuchsian/Kleinian groups, and boundary geometry."),
        ("VII/38--VII/39", "Mitchell--Mount--Papadimitriou 1987; Surazhsky et al. 2005", "Exact and approximate geodesics on polyhedral and triangle meshes."),
        ("VII/40", "Crane--Weischedel--Wardetzky 2013", "The heat method for geodesic distance; DOI 10.1145/2516971.2516977."),
        ("VII/41", "Meyer et al. 2003; discrete differential-operator literature", "Discrete differential operators and Laplace--Beltrami discretization."),
        ("VII/42", "Pinkall--Polthier 1993; differential-geometry references", "Discrete curvature structures, feature lines, ridges, valleys, and numerical interpretation."),
    ]),
    "vol08_algebraic_topology": ("VIII", "Algebraic Topology", [
        ("VIII/01--VIII/14", "Poincaré; Hurewicz; Hatcher", "Fundamental groups, coverings, group actions, and classical homotopy foundations."),
        ("VIII/15--VIII/27", "Eilenberg--Steenrod; Hatcher; Spanier", "Simplicial/singular/cellular homology, exact sequences, coefficients, and Künneth/UCT structures."),
        ("VIII/28--VIII/30", "Eilenberg--Steenrod; Hatcher; Milnor--Stasheff", "Cohomology, cup products, and vector bundles."),
        ("VIII/31--VIII/35", "Thom 1954; Milnor--Stasheff; Lefschetz", "Thom classes, Euler classes, Poincaré duality, intersection forms, and Lefschetz theory."),
    ]),
}

BIB = r'''% C03 series-level source ledger.
% Current reader-facing notes are plain TeX to avoid changing bibliography packages.

@book{AxlerLinearAlgebra,
  author={Sheldon Axler},
  title={Linear Algebra Done Right},
  publisher={Springer}
}
@book{HalmosFiniteDimensional,
  author={Paul R. Halmos},
  title={Finite-Dimensional Vector Spaces},
  publisher={Springer}
}
@book{HoffmanKunze,
  author={Kenneth Hoffman and Ray Kunze},
  title={Linear Algebra},
  publisher={Prentice-Hall}
}
@book{HornJohnsonMatrixAnalysis,
  author={Roger A. Horn and Charles R. Johnson},
  title={Matrix Analysis},
  publisher={Cambridge University Press}
}
@article{EckartYoung1936,
  author={Carl Eckart and Gale Young},
  title={The Approximation of One Matrix by Another of Lower Rank},
  journal={Psychometrika},
  volume={1},
  year={1936},
  pages={211--218}
}
@book{RudinPMA,
  author={Walter Rudin},
  title={Principles of Mathematical Analysis},
  publisher={McGraw-Hill}
}
@book{FollandRealAnalysis,
  author={Gerald B. Folland},
  title={Real Analysis: Modern Techniques and Their Applications},
  publisher={Wiley}
}
@book{Lebesgue1902,
  author={Henri Lebesgue},
  title={Intégrale, longueur, aire},
  year={1902},
  note={Doctoral thesis}
}
@book{SchwartzDistributions,
  author={Laurent Schwartz},
  title={Théorie des distributions},
  publisher={Hermann},
  year={1950}
}
@book{HormanderLinearPDE,
  author={Lars Hörmander},
  title={The Analysis of Linear Partial Differential Operators},
  publisher={Springer}
}
@book{EvansPDE,
  author={Lawrence C. Evans},
  title={Partial Differential Equations},
  publisher={American Mathematical Society}
}
@book{AhlforsComplex,
  author={Lars V. Ahlfors},
  title={Complex Analysis},
  publisher={McGraw-Hill}
}
@book{ForsterRiemannSurfaces,
  author={Otto Forster},
  title={Lectures on Riemann Surfaces},
  publisher={Springer}
}
@book{Riemann1851,
  author={Bernhard Riemann},
  title={Grundlagen für eine allgemeine Theorie der Functionen einer veränderlichen complexen Grösse},
  year={1851}
}
@book{AtiyahMacdonald1969,
  author={M. F. Atiyah and I. G. Macdonald},
  title={Introduction to Commutative Algebra},
  publisher={Addison-Wesley},
  year={1969}
}
@book{CartanEilenberg1956,
  author={Henri Cartan and Samuel Eilenberg},
  title={Homological Algebra},
  publisher={Princeton University Press},
  year={1956}
}
@article{GrothendieckTohoku1957,
  author={Alexander Grothendieck},
  title={Sur quelques points d'algèbre homologique},
  journal={Tohoku Mathematical Journal},
  volume={9},
  year={1957},
  pages={119--183},
  doi={10.2748/tmj/1178244839}
}
@article{SerreFAC1955,
  author={Jean-Pierre Serre},
  title={Faisceaux algébriques cohérents},
  journal={Annals of Mathematics},
  volume={61},
  number={2},
  year={1955},
  pages={197--278},
  doi={10.2307/1969915}
}
@article{EGAI1960,
  author={Alexander Grothendieck and Jean Dieudonné},
  title={Éléments de géométrie algébrique I},
  journal={Publications Mathématiques de l'IHÉS},
  volume={4},
  year={1960}
}
@book{Hartshorne1977,
  author={Robin Hartshorne},
  title={Algebraic Geometry},
  publisher={Springer},
  year={1977}
}
@misc{StacksProject,
  author={The Stacks Project Authors},
  title={The Stacks Project},
  howpublished={https://stacks.math.columbia.edu/}
}
@book{Gauss1827,
  author={Carl Friedrich Gauss},
  title={Disquisitiones generales circa superficies curvas},
  year={1827}
}
@book{LeeRiemannian,
  author={John M. Lee},
  title={Riemannian Manifolds: An Introduction to Curvature},
  publisher={Springer}
}
@book{doCarmoRiemannian,
  author={Manfredo P. do Carmo},
  title={Riemannian Geometry},
  publisher={Birkhäuser}
}
@article{MitchellMountPapadimitriou1987,
  author={Joseph S. B. Mitchell and David M. Mount and Christos H. Papadimitriou},
  title={The Discrete Geodesic Problem},
  journal={SIAM Journal on Computing},
  volume={16},
  number={4},
  year={1987},
  pages={647--668},
  doi={10.1137/0216045}
}
@article{Surazhsky2005,
  author={Vitaly Surazhsky and Tatiana Surazhsky and Danil Kirsanov and Steven J. Gortler and Hugues Hoppe},
  title={Fast Exact and Approximate Geodesics on Meshes},
  journal={ACM Transactions on Graphics},
  volume={24},
  number={3},
  year={2005},
  pages={553--560},
  doi={10.1145/1073204.1073228}
}
@article{CraneWeischedelWardetzky2013,
  author={Keenan Crane and Clarisse Weischedel and Max Wardetzky},
  title={Geodesics in Heat: A New Approach to Computing Distance Based on Heat Flow},
  journal={ACM Transactions on Graphics},
  volume={32},
  number={5},
  year={2013},
  doi={10.1145/2516971.2516977}
}
@article{PinkallPolthier1993,
  author={Ulrich Pinkall and Konrad Polthier},
  title={Computing Discrete Minimal Surfaces and Their Conjugates},
  journal={Experimental Mathematics},
  volume={2},
  number={1},
  year={1993},
  pages={15--36},
  doi={10.1080/10586458.1993.10504266}
}
@incollection{MeyerDesbrunSchroderBarr2003,
  author={Mark Meyer and Mathieu Desbrun and Peter Schröder and Alan H. Barr},
  title={Discrete Differential-Geometry Operators for Triangulated 2-Manifolds},
  booktitle={Visualization and Mathematics III},
  publisher={Springer},
  year={2003}
}
@book{Hatcher2002,
  author={Allen Hatcher},
  title={Algebraic Topology},
  publisher={Cambridge University Press},
  year={2002}
}
@book{EilenbergSteenrod1952,
  author={Samuel Eilenberg and Norman Steenrod},
  title={Foundations of Algebraic Topology},
  publisher={Princeton University Press},
  year={1952}
}
@article{Thom1954,
  author={René Thom},
  title={Quelques propriétés globales des variétés différentiables},
  journal={Commentarii Mathematici Helvetici},
  volume={28},
  year={1954},
  pages={17--86},
  doi={10.1007/BF02566923}
}
@book{MilnorStasheff1974,
  author={John W. Milnor and James D. Stasheff},
  title={Characteristic Classes},
  publisher={Princeton University Press},
  year={1974}
}
@book{Lefschetz1942,
  author={Solomon Lefschetz},
  title={Algebraic Topology},
  publisher={American Mathematical Society},
  year={1942}
}
'''

DETAILS = {
"I":[("Axler; Halmos; Hoffman--Kunze","Structural and classical finite-dimensional linear algebra."),
     ("Horn--Johnson","Matrix analysis and spectral structure."),
     ("Eckart--Young (1936)","Classical low-rank approximation result underlying the optimality interpretation of the SVD.")],
"II":[("Rudin","Modern rigorous real analysis."),
      ("Lebesgue (1902); Folland","Primary and modern references for measure and Lebesgue integration.")],
"III":[("Schwartz; Hörmander","Distributions and generalized-function analysis."),
       ("Evans","Modern PDE reference.")],
"IV":[("Cauchy and Riemann","Historical foundations of complex function theory."),
      ("Ahlfors; Forster","Modern complex analysis and Riemann-surface references.")],
"V":[("Atiyah--Macdonald; Matsumura","Commutative algebra."),
     ("Cartan--Eilenberg (1956)","Foundational systematic homological algebra."),
     ("Grothendieck (1957)",r"Derived-functor/abelian-category foundations; DOI \texttt{10.2748/tmj/1178244839}.")],
"VI":[("Serre, FAC (1955)",r"Coherent algebraic sheaves; DOI \texttt{10.2307/1969915}."),
      ("Grothendieck--Dieudonné, EGA","Foundational scheme language and constructions."),
      ("Hartshorne; Stacks Project","Modern verification of exact theorem statements and hypotheses.")],
"VII":[("Mitchell--Mount--Papadimitriou (1987)",r"Exact polyhedral geodesics; DOI \texttt{10.1137/0216045}."),
       ("Surazhsky et al. (2005)",r"Practical exact/approximate mesh geodesics; DOI \texttt{10.1145/1073204.1073228}."),
       ("Crane--Weischedel--Wardetzky (2013)",r"Heat method; DOI \texttt{10.1145/2516971.2516977}."),
       ("Meyer et al. (2003)","Discrete differential-geometric operators."),
       ("Pinkall--Polthier (1993)",r"Discrete minimal surfaces; DOI \texttt{10.1080/10586458.1993.10504266}.")],
"VIII":[("Eilenberg--Steenrod; Hatcher","Axiomatic and modern algebraic topology."),
        ("Thom (1954)",r"Thom-space/class foundations; DOI \texttt{10.1007/BF02566923}."),
        ("Milnor--Stasheff; Lefschetz","Characteristic classes, duality, and Lefschetz viewpoints.")]
}

def make_tex(roman, title, ranges):
    lines = [
        r"\chapter*{Sources and Further Reading}",
        r"\phantomsection",
        r"\addcontentsline{toc}{chapter}{Sources and Further Reading}",
        "",
        f"This guide records primary or authoritative sources relevant to \\emph{{Volume {roman}: {title}}}.",
        "It is a reading and attribution guide; the volume's own hypotheses and conventions remain authoritative.",
        "",
        r"\section*{Chapter guide}",
        r"\begin{description}",
    ]
    for rng, refs, focus in ranges:
        lines += [f"\\item[{rng}.] {focus}", f"\\textbf{{Suggested sources:}} {refs}.", ""]
    lines += [r"\end{description}", "", r"\section*{Selected bibliographic notes}", r"\begin{description}"]
    for label, note in DETAILS[roman]:
        lines += [f"\\item[{label}.] {note}", ""]
    lines += [
        r"\end{description}",
        "",
        r"\section*{Reference policy}",
        "Historical attribution and modern theorem verification serve different roles.",
        "Where precise hypotheses matter, use an authoritative modern source in addition to historical attribution.",
        r"The maintained series bibliography is stored at \texttt{references/series\_primary\_sources.bib}.",
        "",
    ]
    return "\n".join(lines)

def update_book(book):
    raw = book.read_text(encoding="utf-8-sig")
    marker = r"\input{backmatter/sources-and-further-reading.tex}"
    if marker in raw:
        return
    if r"\backmatter" in raw:
        new = raw.replace(r"\backmatter", r"\backmatter" + "\n" + marker, 1)
    else:
        new = raw.replace(r"\end{document}", "\\backmatter\n" + marker + "\n\\end{document}", 1)
    book.write_text(new, encoding="utf-8", newline="\n")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", required=True)
    a = ap.parse_args()
    repo = Path(a.repo).resolve()

    refs = repo/"references"
    refs.mkdir(parents=True, exist_ok=True)
    (refs/"series_primary_sources.bib").write_text(BIB, encoding="utf-8", newline="\n")

    rows = []
    for d,(roman,title,ranges) in VOLUMES.items():
        v = repo/"books"/d
        back = v/"backmatter"
        back.mkdir(parents=True, exist_ok=True)
        (back/"sources-and-further-reading.tex").write_text(
            make_tex(roman,title,ranges), encoding="utf-8", newline="\n")
        update_book(v/"book.tex")
        for rng,sources,focus in ranges:
            rows.append((roman,rng,focus,sources,"reader-facing backmatter"))

    editorial = repo/"editorial"
    editorial.mkdir(parents=True, exist_ok=True)
    with (editorial/"C03_PRIMARY_SOURCE_LEDGER.tsv").open("w",encoding="utf-8",newline="") as f:
        w=csv.writer(f,delimiter="\t",lineterminator="\n")
        w.writerow(["volume","chapter_range","focus","primary_or_authoritative_sources","presentation"])
        w.writerows(rows)

    policy = '''# C03 bibliography policy

Historical attribution and theorem verification are distinct tasks.

- Cite a primary source when crediting the origin of a theorem, construction, or algorithm.
- Cite an authoritative modern source when exact hypotheses, notation, or conventions must be verified.
- For modern computational algorithms, cite the original paper directly.

High-priority anchors include Cartan–Eilenberg and Grothendieck for V/22–V/28; Serre FAC, EGA, Hartshorne and the Stacks Project for VI; Mitchell–Mount–Papadimitriou, Surazhsky et al., Crane–Weischedel–Wardetzky, Meyer et al., and Pinkall–Polthier for VII/38–VII/42; and Thom, characteristic-class references, and Lefschetz sources for VIII/31–VIII/35.

`references/series_primary_sources.bib` is the maintained source ledger. The current books render source guides as plain TeX so C03 does not force a new bibliography package into the build.
'''
    (editorial/"C03_BIBLIOGRAPHY_POLICY.md").write_text(policy,encoding="utf-8",newline="\n")

    print("C03 bibliography and eight source guides created.")
    return 0

if __name__=="__main__":
    raise SystemExit(main())
