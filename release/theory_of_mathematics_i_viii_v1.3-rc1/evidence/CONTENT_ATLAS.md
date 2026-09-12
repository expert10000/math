# CONTENT ATLAS

**Status:** Architecture Freeze v1.0
**Repository:** `expert10000/math`
**Source scope:** `chapters/tex/*.tex`
**Freeze date:** 2026-08-16

## Purpose

This file is the canonical editorial architecture for rebuilding the legacy TeX archive as a coherent multi-volume mathematics series. Historical filenames and numbering are provenance only; they do not determine future chapter order.

The companion file `SOURCE_MIGRATION.tsv` is the normative migration map. It covers all 169 current `.tex` paths in the working inventory and assigns substantive thematic blocks, theorem-like descendants, and problem/exercise descendants to canonical chapter destinations or explicit archive/support classifications.

## Frozen editorial rules

1. Existing filenames and historical numbering have no editorial authority.
2. A legacy `.tex` file is a source container, not automatically a future chapter.
3. Each mathematical concept has one canonical home; other occurrences become merge sources or cross-references.
4. Original sources are preserved for provenance and diffing; nothing is silently deleted.
5. Exercises, hints, solutions, and figures move beside the chapter they support.
6. Provenance variants (`--math-alls-*`, `_Copy`, professional revisions) are compared before archiving; only unique mathematics migrates.
7. Merged exercise snapshots never participate directly in the new build.
8. Rewrites modify canonical chapter sources in place; do not create new `*_corrected_vN` lineages.
9. Chapter prose, exercise counts, and exact chapter lengths remain editable; the eight-volume subject split and major dependency order are frozen.

## Migration-map semantics

`SOURCE_MIGRATION.tsv` uses precedence-based selectors so that every legacy block has a deterministic disposition:

- **precedence 110** — raw-source-verified targeted override for a theme that would otherwise collide with a broader selector;
- **precedence 105** — theorem-like and problem/exercise descendants inherit a targeted override;
- **precedence 100** — explicit thematic section/subsection selector;
- **precedence 90** — theorem-like and problem/exercise descendants inherit the matched section destination;
- **precedence 10** — file-level safety-net for any unmatched substantive block;
- **precedence 1000** — whole-file archive classification for duplicates, provenance variants, templates, and merged lineages.

Specific selectors override fallbacks. During reconstruction, if an individual theorem/problem is discovered to belong elsewhere, add a higher-precedence explicit override before removing the legacy source.

### Block kinds covered

- section / subsection thematic blocks;
- definitions, theorems, lemmas, propositions, corollaries, remarks, warnings, examples;
- problems, exercises, solutions, worked problems;
- support figures/diagram snippets;
- whole-file duplicate, variant, template, and merged-snapshot classifications.

## Inventory accounting

| Class | Files | Editorial disposition |
|---|---:|---|
| Substantive primary/compare manuscripts | 101 | Migrate or compare-and-migrate |
| Support/exercise/figure sources | 17 | Attach to canonical chapters |
| Provenance variants / duplicates | 30 | Archive after diff |
| Merged-exercise lineage | 21 | Archive source-only |
| **Total** | **169** | Fully represented in `SOURCE_MIGRATION.tsv` |

The TSV currently contains **1,460 migration-rule rows**.

## Frozen eight-volume architecture

# Volume I — Linear Algebra

## Part I — Vector Spaces

1. **I/01 — Scalars, Vectors and Linear Combinations**
2. **I/02 — Subspaces, Span and Linear Independence**
3. **I/03 — Bases and Dimension**
4. **I/04 — Coordinates and Change of Basis**
5. **I/05 — Linear Transformations**
6. **I/06 — Kernels, Images and Isomorphisms**

## Part II — Matrices and Operators

7. **I/07 — Matrix Representation of Linear Maps**
8. **I/08 — Determinants and Trace**
9. **I/09 — Eigenvalues and Eigenvectors**
10. **I/10 — Invariant Subspaces and Triangularization**
11. **I/11 — Diagonalization and Minimal Polynomials**
12. **I/12 — Canonical Forms**

## Part III — Euclidean and Hilbert-Space Geometry

13. **I/13 — Inner Products and Orthogonality**
14. **I/14 — Gram–Schmidt and Orthogonal Projection**
15. **I/15 — Orthogonal and Unitary Operators**
16. **I/16 — The Spectral Theorem**
17. **I/17 — Quadratic Forms**
18. **I/18 — Singular-Value Decomposition**

# Volume II — Real Analysis and Topological Foundations

## Part I — Metric Foundations

1. **II/01 — The Real Number System and Completeness**
2. **II/02 — Euclidean and Normed Spaces**
3. **II/03 — Sequences and Cauchy Sequences**
4. **II/04 — Open and Closed Sets**
5. **II/05 — Metric Spaces and Continuity**
6. **II/06 — Compactness**
7. **II/07 — Connectedness and Path Connectedness**

## Part II — Calculus

8. **II/08 — Differentiability in Several Variables**
9. **II/09 — Inverse and Implicit Function Principles**
10. **II/10 — Riemann Integration**

## Part III — Sequences of Functions

11. **II/11 — Pointwise and Uniform Convergence**
12. **II/12 — Interchanging Limits, Derivatives and Integrals**
13. **II/13 — Infinite Series of Functions**
14. **II/14 — Trigonometric Series**
15. **II/15 — Pathological and Nowhere-Differentiable Functions**

## Part IV — Fixed Points and Differential Equations

16. **II/16 — Contraction Mappings**
17. **II/17 — Brouwer-Type Fixed-Point Ideas**
18. **II/18 — Integral Equations**
19. **II/19 — Elementary Existence Theory for ODEs**

## Part V — Approximation

20. **II/20 — Polynomial Interpolation**
21. **II/21 — Polynomial Approximation**
22. **II/22 — Chebyshev and Minimax Approximation**
23. **II/23 — The Alternation Principle**
24. **II/24 — Numerical Quadrature**
25. **II/25 — Continued Fractions and Approximation Topics**

# Volume III — Measure, Fourier Analysis, Distributions and PDE

## Part I — Measure and Integration

1. **III/01 — Sigma-Algebras and Measures**
2. **III/02 — Measurable Functions**
3. **III/03 — The Lebesgue Integral**
4. **III/04 — Convergence Theorems**
5. **III/05 — Product Measures and Fubini Theory**
6. **III/06 — Lp Spaces**
7. **III/07 — Hölder, Minkowski and Interpolation**
8. **III/08 — Egorov, Vitali and Weak-Lp Ideas**

## Part II — Fourier Analysis

9. **III/09 — Fourier Series**
10. **III/10 — Convolution and Approximate Identities**
11. **III/11 — The Fourier Transform**
12. **III/12 — The Gaussian and Transform Calculus**
13. **III/13 — Plancherel and L2 Fourier Theory**
14. **III/14 — The Schwartz Space**

## Part III — Distribution Theory

15. **III/15 — Test-Function Spaces**
16. **III/16 — Distributions and Distributional Derivatives**
17. **III/17 — Support and Singular Distributions**
18. **III/18 — Tempered Distributions**
19. **III/19 — Fourier Transform of Distributions**

## Part IV — Sobolev and PDE Methods

20. **III/20 — Weak Derivatives**
21. **III/21 — Sobolev Spaces**
22. **III/22 — Approximation and Density**
23. **III/23 — Weak Boundary-Value Problems**
24. **III/24 — Fundamental Solutions**
25. **III/25 — Green Functions**
26. **III/26 — Sturm–Liouville Green Kernels**
27. **III/27 — Elliptic Operators and Maximum Principles**
28. **III/28 — Spectral and Transform Methods for PDE**

# Volume IV — Complex Analysis and Riemann Surfaces

## Part I — Holomorphic Functions

1. **IV/01 — Complex Differentiability**
2. **IV/02 — Cauchy–Riemann Equations**
3. **IV/03 — Power Series and Analytic Functions**
4. **IV/04 — Complex Integration**
5. **IV/05 — Cauchy's Theorem**
6. **IV/06 — Cauchy's Integral Formula**

## Part II — Singularities and Residues

7. **IV/07 — Zeros and the Identity Theorem**
8. **IV/08 — Laurent Series**
9. **IV/09 — Isolated Singularities**
10. **IV/10 — Residues and the Residue Theorem**
11. **IV/11 — Evaluation of Real Integrals**

## Part III — Global Complex Analysis

12. **IV/12 — Winding Numbers and the Argument Principle**
13. **IV/13 — Rouché's Theorem**
14. **IV/14 — Branches of the Logarithm and Roots**
15. **IV/15 — Analytic Continuation**
16. **IV/16 — Möbius Transformations**
17. **IV/17 — Conformal Mapping**
18. **IV/18 — Schwarz–Christoffel Transformations**

## Part IV — Special Functions

19. **IV/19 — The Gamma Function**
20. **IV/20 — Beta and Gamma Identities**
21. **IV/21 — Keyhole Contours and Branch-Cut Integrals**

## Part V — Riemann Surfaces

22. **IV/22 — From Analytic Continuation to Riemann Surfaces**
23. **IV/23 — Covering Maps and Monodromy**
24. **IV/24 — Branched Coverings**
25. **IV/25 — Construction by Gluing**
26. **IV/26 — Compactification and Genus**

## Part VI — Elliptic Functions

27. **IV/27 — Lattices and Complex Tori**
28. **IV/28 — Elliptic Functions**
29. **IV/29 — The Weierstrass ℘-Function**
30. **IV/30 — Addition Formulas**
31. **IV/31 — Elliptic Curves as Riemann Surfaces**

# Volume V — Commutative Algebra and Homological Methods

## Part I — Rings and Ideals

1. **V/01 — Rings, Ideals and Quotients**
2. **V/02 — Prime and Maximal Ideals**
3. **V/03 — Radicals and Nilpotents**
4. **V/04 — Chinese Remainder Theory**

## Part II — Localization

5. **V/05 — Multiplicative Systems**
6. **V/06 — Localization of Rings**
7. **V/07 — Localization of Modules**
8. **V/08 — Local Rings and Localization at Primes**

## Part III — Modules and Tensor Products

9. **V/09 — Modules and Exact Sequences**
10. **V/10 — Tensor Products**
11. **V/11 — Quotients and Base Change**
12. **V/12 — Hom and Finitely Presented Modules**
13. **V/13 — Free and Projective Modules**
14. **V/14 — Flat Modules**

## Part IV — Noetherian Algebra

15. **V/15 — Noetherian Rings and Modules**
16. **V/16 — Support**
17. **V/17 — Associated Primes**
18. **V/18 — Completion and I-Adic Topology**

## Part V — Integral and Valuation Theory

19. **V/19 — Integral Dependence**
20. **V/20 — Integral Closure and Normalization**
21. **V/21 — Valuation Rings**

## Part VI — Homological Algebra

22. **V/22 — Chain Complexes**
23. **V/23 — Free Resolutions**
24. **V/24 — Syzygies**
25. **V/25 — Minimal Resolutions**
26. **V/26 — The Tor Functor**
27. **V/27 — The Ext Functor**
28. **V/28 — Derived-Functor Viewpoint**

# Volume VI — Algebraic Geometry and Sheaf Theory

## Part I — Classical Affine Geometry

1. **VI/01 — Algebraic Sets**
2. **VI/02 — The Zariski Topology**
3. **VI/03 — Coordinate Rings**
4. **VI/04 — Morphisms of Affine Algebraic Sets**
5. **VI/05 — Irreducibility, Components and Connectedness**

## Part II — Prime Spectra

6. **VI/06 — Prime Ideals as Geometric Points**
7. **VI/07 — The Spectrum of a Ring**
8. **VI/08 — Basic Open Sets D(f)**
9. **VI/09 — Generic and Closed Points**
10. **VI/10 — Reduced and Nonreduced Geometry**
11. **VI/11 — Local Rings and Residue Fields**

## Part III — Sheaves

12. **VI/12 — Presheaves**
13. **VI/13 — Sheaves and Stalks**
14. **VI/14 — Sheafification**
15. **VI/15 — Kernels, Images and Quotients of Sheaves**
16. **VI/16 — Exact Sequences of Sheaves**
17. **VI/17 — The Structure Sheaf**

## Part IV — Affine and General Schemes

18. **VI/18 — Affine Schemes**
19. **VI/19 — Morphisms of Affine Schemes**
20. **VI/20 — Gluing Affine Schemes**
21. **VI/21 — Schemes and Their Points**
22. **VI/22 — Open and Closed Subschemes**

## Part V — Morphisms and Families

23. **VI/23 — Fiber Products**
24. **VI/24 — Base Change**
25. **VI/25 — Fibers and Geometric Fibers**
26. **VI/26 — Finite-Type and Noetherian Morphisms**
27. **VI/27 — Integral Schemes and Function Fields**
28. **VI/28 — Normalization**

## Part VI — Dimension

29. **VI/29 — Krull Dimension**
30. **VI/30 — Dimension of Schemes**
31. **VI/31 — Codimension**
32. **VI/32 — Tangent Spaces and Local Geometry**

## Part VII — Projective Geometry

33. **VI/33 — Graded Rings**
34. **VI/34 — Proj**
35. **VI/35 — Projective Space**
36. **VI/36 — Projective Schemes**
37. **VI/37 — Projective Morphisms and Closed Embeddings**
38. **VI/38 — Coherent and Quasi-Coherent Sheaves**

## Part VIII — Divisors and Birational Geometry

39. **VI/39 — Weil Divisors**
40. **VI/40 — Cartier Divisors**
41. **VI/41 — Divisor Class Groups**
42. **VI/42 — Line Bundles and Picard Groups**
43. **VI/43 — Plane Cubics**
44. **VI/44 — Cremona Transformations**
45. **VI/45 — Blow-Ups**

## Part IX — Sheaf Cohomology

46. **VI/46 — Flabby Sheaves**
47. **VI/47 — Čech Cohomology**
48. **VI/48 — Exact Sequences and Cohomology**
49. **VI/49 — Basic Vanishing Results**

# Volume VII — Differential, Riemannian and Hyperbolic Geometry

## Part I — Smooth Manifolds

1. **VII/01 — Topological Manifolds**
2. **VII/02 — Smooth Structures and Atlases**
3. **VII/03 — Smooth Maps and Diffeomorphisms**
4. **VII/04 — Tangent Spaces**
5. **VII/05 — Cotangent Spaces**
6. **VII/06 — Submanifolds and Products**

## Part II — Bundles and Forms

7. **VII/07 — Vector Bundles**
8. **VII/08 — Principal and Frame Bundles**
9. **VII/09 — Differential Forms**
10. **VII/10 — Orientation and Integration**
11. **VII/11 — Stokes' Theorem**

## Part III — Curves and Surfaces

12. **VII/12 — Regular Curves**
13. **VII/13 — Frenet Frames, Curvature and Torsion**
14. **VII/14 — Regular Surfaces**
15. **VII/15 — First and Second Fundamental Forms**
16. **VII/16 — The Gauss Map and Shape Operator**
17. **VII/17 — Principal, Gaussian and Mean Curvature**
18. **VII/18 — Ruled and Developable Surfaces**
19. **VII/19 — Minimal Surfaces**

## Part IV — Riemannian Geometry

20. **VII/20 — Riemannian Metrics**
21. **VII/21 — Connections**
22. **VII/22 — The Levi–Civita Connection**
23. **VII/23 — Geodesics**
24. **VII/24 — Parallel Transport**
25. **VII/25 — Holonomy**
26. **VII/26 — The Riemann Curvature Tensor**
27. **VII/27 — Ricci and Scalar Curvature**
28. **VII/28 — Weyl Curvature**

## Part V — Lorentzian Geometry

29. **VII/29 — Indefinite Metrics**
30. **VII/30 — Riemannian versus Lorentzian Geometry**

## Part VI — Hyperbolic Geometry

31. **VII/31 — Hyperbolic Plane Models**
32. **VII/32 — The Poincaré Metric**
33. **VII/33 — Möbius Transformations and PSL(2,R)**
34. **VII/34 — Hyperbolic Isometries**
35. **VII/35 — Fuchsian Groups**
36. **VII/36 — Hyperbolic Three-Space and PSL(2,C)**
37. **VII/37 — Kleinian Groups and Boundary Geometry**

## Part VII — Computational Geometry

38. **VII/38 — Discrete Geodesic Problems**
39. **VII/39 — Graph and Exact Mesh Geodesics**
40. **VII/40 — The Heat Method**
41. **VII/41 — Discrete Laplacians**
42. **VII/42 — Curvature Lines, Ridges and Valleys**

# Volume VIII — Algebraic Topology

## Part I — Homotopy

1. **VIII/01 — Homotopies of Maps**
2. **VIII/02 — Homotopy Equivalence and Contractibility**
3. **VIII/03 — Degree of Maps**
4. **VIII/04 — Spheres and Antipodal Maps**

## Part II — CW Complexes

5. **VIII/05 — Cell Attachments**
6. **VIII/06 — CW Complexes**
7. **VIII/07 — Mapping Cones**
8. **VIII/08 — Homotopic Attaching Maps**

## Part III — Fundamental Groups and Coverings

9. **VIII/09 — Paths and Fundamental Groups**
10. **VIII/10 — Covering Spaces**
11. **VIII/11 — Lifting Properties**
12. **VIII/12 — Deck Transformations and Group Actions**
13. **VIII/13 — SU(2) to SO(3)**
14. **VIII/14 — Free Groups and Covering Graphs**

## Part IV — Homology

15. **VIII/15 — Simplicial Complexes**
16. **VIII/16 — Chain Complexes**
17. **VIII/17 — Simplicial and Singular Homology**
18. **VIII/18 — Cellular Homology**
19. **VIII/19 — Relative Homology and Exact Sequences**
20. **VIII/20 — Homotopy Invariance**
21. **VIII/21 — Euler Characteristic**

## Part V — Homological Machinery

22. **VIII/22 — Chain Homotopies**
23. **VIII/23 — Chain Contractions**
24. **VIII/24 — Mapping Cones of Chain Maps**
25. **VIII/25 — Homology with Coefficients**
26. **VIII/26 — The Universal Coefficient Theorem**
27. **VIII/27 — Products and the Künneth Theorem**

## Part VI — Cohomology, Bundles and Manifolds

28. **VIII/28 — Cohomology**
29. **VIII/29 — Cup Products**
30. **VIII/30 — Vector Bundles and Clutching**
31. **VIII/31 — Thom Classes**
32. **VIII/32 — Sphere Bundles and Euler Classes**
33. **VIII/33 — Poincaré Duality**
34. **VIII/34 — Intersection Forms**
35. **VIII/35 — Lefschetz Theory**

# Cross-volume source-family normalization

| Legacy source family | Canonical home | Editorial rule |
|---|---|---|
| `theory-of-linear-algebra-*` | Volume I | Primary source family |
| `theory-of-real-analysis`, `theory-of-analysis*` | Volumes II–III | Split by topology/real analysis vs measure/Fourier/distribution content |
| `theory-of-complex-analysis*` | Volume IV | Composite `all*` branches are comparison sources, not separate chapters |
| `theory-of-commutative-algebra-*` | Volume V, with scheme spillover to VI | Algebraic proofs stay in V; scheme geometry migrates to VI |
| `theory-of-algebraic-geometry-1..11` | Volume VI | Core schemes/sheaves/projective/divisor/cohomology material |
| `theory-of-algebraic-geometry-12..19` | Volume IV | Reclassified as Riemann-surface / elliptic-function material |
| `theory-of-algebraic-geometry-20..22` | Volume VII | Reclassified as differential/Riemannian/Lorentzian geometry |
| `theory-of-differential-geometry-3` | Volume I | Mislabelled linear algebra |
| `theory-of-differential-geometry-4..5` | Volume VI | Mislabelled algebraic geometry |
| `theory-of-differential-geometry-*`, `theory-of-geometry*` | Volume VII | Merge overlapping manifold/surface/connection streams |
| `theory-of-algebraic-topology-*` | Volume VIII | Reorder as homotopy → CW → coverings → homology → machinery → bundles/duality |
| `wiki-green`, distributions/Fourier sources | Volume III | PDE/Green/distribution material |
| exercise/figure snippets | Destination chapter assets | Never standalone chapters |
| merged exercise snapshots | Archive | Never direct build inputs |

# Canonical repository target

```text
math/
├── archive/
│   └── legacy_tex/
├── books/
│   ├── vol01_linear_algebra/
│   ├── vol02_real_analysis/
│   ├── vol03_fourier_distributions_pde/
│   ├── vol04_complex_analysis/
│   ├── vol05_commutative_algebra/
│   ├── vol06_algebraic_geometry/
│   ├── vol07_differential_geometry/
│   └── vol08_algebraic_topology/
├── shared/
│   ├── preamble.tex
│   ├── macros.tex
│   ├── theorem_styles.tex
│   ├── notation.tex
│   ├── bibliography.bib
│   └── figures/
├── editorial/
│   ├── CONTENT_ATLAS.md
│   ├── SOURCE_MIGRATION.tsv
│   ├── CHAPTER_STATUS.tsv
│   └── DUPLICATE_MAP.tsv
└── build/
```

Recommended chapter layout:

```text
books/vol06_algebraic_geometry/chapters/ch08_basic_open_sets/
├── chapter.tex
├── examples.tex
├── exercises.tex
├── hints.tex
├── solutions.tex
└── figures/
```

# Reconstruction order

Two safe starting choices are now available:

1. **Volume I / Chapter 1** — best if the goal is to rebuild the series from prerequisites upward.
2. **Volume VI / Chapter 1–8 block** — best if the goal is to exploit the richest existing source pool first and establish the new editorial workflow on mature algebraic-geometry material.

For either route, reconstruction must follow the same rule: resolve the relevant `SOURCE_MIGRATION.tsv` rows, copy/mine unique mathematics into the canonical chapter, record provenance in the chapter status ledger, run a diff/check against all compare sources, then freeze the canonical chapter before proceeding.

# Freeze boundary

**Frozen now:** eight-volume division; major Parts; chapter dependency order; legacy-source classification rules; archive/variant policy; migration precedence semantics.

**Not frozen:** final prose; exact theorem numbering; exercise counts; page design; exact chapter length; whether a large chapter later splits into A/B; LaTeX-vs-Quarto publishing orchestration.

# Coverage audit

The current migration ledger contains **1,460 mapping rows** across **169 current `.tex` paths**. Every inventoried source file has either a whole-file archive/support disposition or a file-level fallback, while substantive files also carry thematic selectors and inherited theorem/problem rules.

Of the **256 frozen canonical chapter codes**, **255 currently have at least one legacy-source migration selector**. The remaining source-light chapter is:

- **II/09 — Inverse and Implicit Function Principles** — retain in the frozen architecture, but plan a fresh canonical treatment unless a later instance-level audit uncovers suitable legacy material.

This distinction is deliberate: the atlas is allowed to contain pedagogically necessary chapters even when the old archive does not provide a sufficiently clean source.

The TSV should be interpreted as a deterministic migration program: targeted overrides win over broad thematic selectors; theorem/problem descendants inherit their matched thematic destination; any still-unmatched legacy block receives its file fallback and must be resolved during the chapter-level source diff before the legacy source is retired.

# Provenance

Prepared from the public `expert10000/math` repository, its `chapters/tex` tree, and `chapters/manifest.tsv` as inspected on 2026-08-16. The manifest records historical import provenance; the migration TSV treats current-path files as the editorial units and preserves provenance variants explicitly.
