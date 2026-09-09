# Volume I — Mathematical Navigation

This map records the internal prerequisite flow of Volume I and the most useful
bridges from linear algebra into later volumes. The chapter text remains
authoritative for formal hypotheses; the arrows below are editorial navigation.

## Internal flow

### Part I — Vector Spaces

- **I/01 Scalars, Vectors and Linear Combinations** → basic scalar/vector language.
- **I/02 Subspaces, Span and Linear Independence** depends on I/01.
- **I/03 Bases and Dimension** depends on I/01–I/02.
- **I/04 Coordinates and Change of Basis** depends on I/03.
- **I/05 Linear Transformations** depends on I/01–I/03.
- **I/06 Kernels, Images and Isomorphisms** depends on I/05 and dimension.

### Part II — Matrices and Operators

- **I/07 Matrix Representation of Linear Maps** depends on I/04–I/06.
- **I/08 Determinants and Trace** depends on matrix representation and finite dimension.
- **I/09 Eigenvalues and Eigenvectors** depends on I/05, I/07–I/08.
- **I/10 Invariant Subspaces and Triangularization** depends on I/09.
- **I/11 Diagonalization and Minimal Polynomials** depends on I/09–I/10.
- **I/12 Canonical Forms** depends on I/10–I/11 and polynomial/operator methods.

### Part III — Euclidean and Hilbert-Space Geometry

- **I/13 Inner Products and Orthogonality** depends on I/01–I/03.
- **I/14 Gram–Schmidt and Orthogonal Projection** depends on I/13.
- **I/15 Orthogonal and Unitary Operators** depends on I/07 and I/13–I/14.
- **I/16 The Spectral Theorem** depends on I/09–I/11 and I/13–I/15.
- **I/17 Quadratic Forms** depends on I/08, I/13 and I/16.
- **I/18 Singular Value Decomposition** depends on I/07, I/13–I/16.

## Standing references inside Volume I

- The scalar-field, finite-dimensional, complex-inner-product, star, and adjoint
  conventions are centralized in
  `frontmatter/notation-and-conventions.tex`.
- The reader-facing bibliography and series transitions are centralized in
  `frontmatter/references-and-series-bridges.tex`.
- Chapter-local reminders should point back to those front-matter conventions
  instead of silently introducing a competing notation.

## Curated cross-volume bridges

### Algebraic generalization

- **I/01 → V/09 — Modules and Exact Sequences** (`CONTINUATION`):
  vector spaces over fields generalize to modules over rings; basis and
  dimension cease to behave uniformly.
- **I/05 → V/09 — Modules and Exact Sequences** (`SEE_ALSO`):
  linear maps generalize to module homomorphisms, with kernels, images, and
  exact sequences becoming the organizing language.

### Analysis

- **I/05 → II/08 — Differentiability in Several Variables** (`FOUNDATION`):
  the derivative is a linear map; Jacobian matrices are its coordinate
  representatives.
- **I/13 → II/05 — Metric Spaces and Continuity** (`FOUNDATION`):
  an inner product induces a norm and the norm induces a metric.
- **I/16–I/18 → III — Measure, Fourier Analysis, Distributions and PDE**
  (`SEE_ALSO`): orthogonal modes, spectral decomposition, positive operators,
  and low-rank structure are finite-dimensional prototypes for analytic
  decompositions used later.

### Differential geometry

- **I/03 → VII/04 — Tangent Spaces** (`FOUNDATION`):
  bases and dimension become local linear data on manifolds.
- **I/05 → VII/03 — Smooth Maps and Diffeomorphisms** (`FOUNDATION`):
  linear transformations model differentials of smooth maps.
- **I/08 → VII/10 — Orientation and Integration** (`FOUNDATION`):
  determinant signs encode orientation change and determinant magnitudes enter
  change-of-variables/Jacobian formulas.
- **I/13 → VII/20 — Riemannian Metrics** (`FOUNDATION`):
  a Riemannian metric is a smoothly varying inner product on tangent spaces.
- **I/14 → VII/08 — Principal and Frame Bundles** (`FOUNDATION`):
  orthonormalization and orthogonal bases prepare frame geometry.
- **I/15–I/16 → VII/20–VII/28** (`SEE_ALSO`):
  adjoints, orthogonal/unitary operators, and spectral decomposition supply
  linear models for metric-compatible geometric operators and curvature
  decompositions.

### Algebraic topology

- **I/03 → VIII/16–VIII/18** (`SEE_ALSO`):
  free abelian chain groups and their ranks echo basis/dimension ideas, although
  the coefficient category is no longer merely vector spaces.
- **I/05–I/06 → VIII/16 — Chain Complexes** (`FOUNDATION`):
  chain complexes are sequences of linear or module maps whose kernels and
  images define homology.
- **I/13 → VIII/30–VIII/34** (`SEE_ALSO`):
  bundle geometry, Thom/Euler classes, duality, and intersection forms all use
  finite-dimensional linear algebra locally, even when the global invariants
  are topological.

## Selected external references

For complementary treatments rather than alternate house notation:

- Sheldon Axler, *Linear Algebra Done Right*.
- Paul Halmos, *Finite-Dimensional Vector Spaces*.
- Kenneth Hoffman and Ray Kunze, *Linear Algebra*.
- Roger Horn and Charles Johnson, *Matrix Analysis*.
- Gilbert Strang, *Introduction to Linear Algebra*.

Because these sources may use different inner-product conventions, Volume I's
own `Notation and Conventions` page remains authoritative for conjugation order,
adjoints, and star notation.

## Reading principle

Follow `FOUNDATION` arrows when a later topic genuinely depends on the earlier
linear-algebra language. Follow `CONTINUATION` arrows when the same structure is
generalized. Follow `SEE_ALSO` arrows for conceptual parallels that are useful
but not formal prerequisites.
