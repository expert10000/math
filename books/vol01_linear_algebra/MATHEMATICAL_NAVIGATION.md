# Volume I — Mathematical Navigation

This sidecar records the **internal prerequisite graph**, the standing notation and
conventions, and the principal cross-volume routes for **Volume I — Linear Algebra**.
The chapter text remains authoritative for theorem hypotheses. Navigation arrows explain
dependency and continuation; they never license importing a later theorem into an earlier
proof.

## Internal prerequisite graph

### Part I — Vector Spaces

- **I/01 Scalars, Vectors and Linear Combinations** is the algebraic starting point.
- **I/02 Subspaces, Span and Linear Independence** depends on I/01.
- **I/03 Bases and Dimension** depends on I/01–I/02.
- **I/04 Coordinates and Change of Basis** depends on ordered bases from I/03.
- **I/05 Linear Transformations** depends on I/01–I/03 but is conceptually independent of
  coordinates.
- **I/06 Kernels, Images and Isomorphisms** depends on I/02–I/05 and finite-dimensional
  dimension theory when rank–nullity is invoked.

Key dependency distinction:

```text
invariant objects
I/01 -> I/02 -> I/03 -> I/05 -> I/06
                    \
                     -> I/04 coordinates
```

Coordinates are a representation layer; they do not redefine the underlying vectors or maps.

### Part II — Matrices and Operators

- **I/07 Matrix Representation of Linear Maps** depends on I/04–I/06.
- **I/08 Determinants and Trace** depends on I/07 and finite-dimensional square operators.
- **I/09 Eigenvalues and Eigenvectors** depends on I/05, I/07–I/08.
- **I/10 Invariant Subspaces and Triangularization** depends on I/09 and on the field/splitting
  hypotheses needed for triangularization.
- **I/11 Diagonalization and Minimal Polynomials** depends on I/09–I/10 plus polynomial
  methods for operators.
- **I/12 Canonical Forms** depends on I/10–I/11; Jordan-form statements additionally depend
  on splitting of the relevant polynomial, while rational canonical form supplies an
  arbitrary-field route.

The conceptual progression is:

```text
map -> matrix -> characteristic data -> invariant subspaces
    -> triangular form -> minimal polynomial -> diagonal/canonical form
```

The graph distinguishes three transformations of a matrix:

- **change of coordinates for one linear map:** two-sided basis change;
- **similarity:** one endomorphism represented in two bases;
- **congruence:** change of variables for a bilinear/quadratic form, used later in I/17.

### Part III — Euclidean and Hilbert-Space Geometry

- **I/13 Inner Products and Orthogonality** depends on I/01–I/03 and adds metric structure.
- **I/14 Gram–Schmidt and Orthogonal Projection** depends on I/13 and uses basis ideas from
  I/03–I/04.
- **I/15 Orthogonal and Unitary Operators** depends on I/05, I/07, I/13–I/14.
- **I/16 The Spectral Theorem** depends on eigenstructure from I/09–I/11 and inner-product
  structure from I/13–I/15.
- **I/17 Quadratic Forms** depends on I/07–I/08, I/13 and I/16; its natural matrix relation is
  congruence rather than similarity.
- **I/18 Singular Value Decomposition** depends on I/07, I/13–I/16 and uses the spectral
  theorem for the positive semidefinite operator `A^*A`.

The geometric/computational progression is:

```text
inner product
    -> orthogonality
    -> Gram–Schmidt / projection / QR
    -> adjoints and unitary geometry
    -> spectral theorem
    -> quadratic forms
    -> SVD
```

Together with Parts I–II, the full Volume I spine is:

```text
bases
  -> matrices
  -> eigenstructure
  -> orthogonality
  -> spectral theorem
  -> SVD
```

## High-value dependency routes

### Coordinate route

`I/03 -> I/04 -> I/07 -> I/14 -> I/18`

A basis gives coordinates, coordinates give matrix representatives, orthonormal coordinates
make projection/QR stable and geometric, and SVD chooses orthonormal coordinates
simultaneously in domain and codomain.

### Operator-structure route

`I/05 -> I/06 -> I/09 -> I/10 -> I/11 -> I/12`

This route moves from abstract maps to kernels/images, then to invariant directions,
invariant subspaces, polynomial structure, and canonical forms.

### Inner-product/spectral route

`I/13 -> I/14 -> I/15 -> I/16 -> I/17 -> I/18`

This route adds geometry to algebra and ends with universal orthogonal factorization.

### Exact-computation route

`I/07 -> I/08 -> I/09 -> I/11`

Matrix representation supports determinant/trace calculations, characteristic data, and
diagonalization/minimal-polynomial criteria.

### Numerical linear-algebra route

`I/14 -> I/16 -> I/18`

QR handles orthonormalization and least squares; the spectral theorem handles normal/self-
adjoint structure; SVD handles rank deficiency, conditioning, pseudoinverses, minimum-norm
solutions, and optimal low-rank approximation.

## Standing notation

Unless a chapter explicitly states otherwise:

- `\mathbb F` is the scalar field.
- `V,W,U` denote vector spaces.
- `T,S` denote linear maps/operators.
- `B,C` denote ordered bases.
- `[v]_B` is the coordinate column of `v` in basis `B`.
- `[T]_{C\leftarrow B}` is the matrix of `T` from domain basis `B` to codomain basis `C`.
- `P_{C\leftarrow B}` converts `B`-coordinates to `C`-coordinates.
- `\ker T` and `\operatorname{im}T` are kernel and image.
- `\operatorname{rank}T` denotes the dimension of the image when finite-dimensional.
- `\chi_T` and `m_T` denote characteristic and minimal polynomials when used.
- `E_\lambda` denotes an eigenspace.
- `\langle x,y\rangle` is the inner product, linear in the **first** argument and
  conjugate-linear in the second over `\mathbb C`.
- `\|x\|=\sqrt{\langle x,x\rangle}` is the induced norm.
- `A^*=\overline A^{\,T}` over `\mathbb C`; over `\mathbb R`, `A^*=A^T`.
- `T^*` is the adjoint characterized by
  `\langle Tv,w\rangle=\langle v,T^*w\rangle`.
- `Q` usually denotes an orthogonal/unitary or column-orthonormal matrix.
- `P_W` denotes orthogonal projection onto `W` when an inner product is present.
- `A=QR` denotes a QR factorization with dimensions/shape stated locally.
- `A=U\Sigma V^*` denotes an SVD.
- `A^+` denotes the Moore–Penrose pseudoinverse.
- `\sigma_1\ge\sigma_2\ge\cdots\ge0` denote singular values.

## Global conventions

### Scalar fields and finite dimension

Statements valid over an arbitrary field remain stated over `\mathbb F`. Real/complex
hypotheses are introduced only when order, positivity, conjugation, inner products, spectral
theory, or SVD require them. Finite dimensionality is explicit when determinant, trace,
dimension counting, matrix representation, characteristic polynomial, canonical forms, or
finite orthonormal bases are used.

### Complex inner products

Volume I uses inner products linear in the first argument and conjugate-linear in the
second. Thus on `\mathbb C^n`,

```math
\langle x,y\rangle = y^*x.
```

Any external reference using the opposite convention must be translated before formulas
for adjoints or conjugation are imported.

### Coordinates versus invariant objects

A basis changes a coordinate description, not the vector or operator. Matrix equalities that
depend on a basis are never promoted to basis-free identities without justification.

### Similarity, equivalence, and congruence

- similarity: `A' = P^{-1}AP`;
- two-sided representation change: independent source/target transition matrices;
- congruence for forms: `A' = P^*AP` (or `P^TAP` in the real case).

These relations answer different classification questions and must not be interchanged.

### Spectral classes

Self-adjoint/Hermitian, orthogonal/unitary, and normal operators are distinct classes.
The spectral theorem used in a chapter must match the class and scalar field of the operator.

### Exact versus numerical statements

Algebraic identities are exact. Numerical remarks about conditioning, QR versus normal
equations, or SVD truncation do not change theorem hypotheses and should be identified as
stability/algorithmic guidance.

## Chapter-to-chapter theorem dependencies

- I/03 basis and dimension results support I/04 coordinate isomorphisms.
- I/05–I/06 kernel/image structure supports matrix rank in I/07.
- I/08 determinant criterion supports characteristic-polynomial eigenvalue tests in I/09.
- I/09 eigenspace theory supports invariant flags in I/10.
- I/10 triangularization and polynomial annihilation support I/11.
- I/11 minimal-polynomial structure supports I/12 canonical forms.
- I/13 Cauchy–Schwarz and orthogonal complements support I/14 projection.
- I/14 orthonormal coordinates support I/15 matrix characterizations.
- I/09–I/11 plus I/13–I/15 support I/16 spectral diagonalization.
- I/16 supplies principal-axis diagonalization for I/17.
- I/16 applied to `A^*A` supplies the construction of I/18.

## Cross-volume continuation routes

### Volume II — Real Analysis and Topological Foundations

- **I/13 -> II/05 Metric Spaces and Continuity** (`FOUNDATION`):
  an inner product induces a norm and a norm induces a metric.
- **I/05/I/07 -> II/08 Differentiability in Several Variables** (`FOUNDATION`):
  the derivative is a linear map and the Jacobian is its coordinate matrix.
- **I/14/I/18 -> later numerical/functional analytic viewpoints** (`SEE_ALSO`):
  orthogonal projection, least squares, operator norms, and conditioning supply finite-
  dimensional models for approximation arguments.

### Volume III — Measure, Fourier Analysis, Distributions and PDE

- **I/13–I/16 -> Fourier orthogonality/spectral viewpoints** (`FOUNDATION`):
  orthogonal expansions generalize finite orthonormal coordinates.
- **I/16 -> spectral methods** (`CONTINUATION`):
  diagonalization of finite-dimensional normal/self-adjoint operators is the prototype for
  spectral decomposition of analytic operators.
- **I/18 -> low-rank/compact-operator intuition** (`SEE_ALSO`):
  singular directions and decay motivate later approximation and modal decompositions.

### Volume V — Algebra and Homological Algebra

- **I/01–I/06 -> V/09 Modules and Exact Sequences** (`CONTINUATION`):
  vector spaces and linear maps generalize to modules and module homomorphisms.
- **I/06 -> kernels/images/quotients/exactness** (`FOUNDATION`):
  the first-isomorphism pattern becomes categorical/homological infrastructure.
- **I/11–I/12 -> module-over-a-polynomial-ring viewpoint** (`SEE_ALSO`):
  canonical forms can be reinterpreted using module structure.

### Volume VII — Differential Geometry

- **I/03 -> VII/04 Tangent Spaces** (`FOUNDATION`):
  bases and dimension become local linear data.
- **I/05/I/07 -> VII/03 Smooth Maps and Diffeomorphisms** (`FOUNDATION`):
  differentials are linear maps represented by Jacobian matrices.
- **I/08 -> VII/10 Orientation and Integration** (`FOUNDATION`):
  determinants control orientation change and Jacobian factors.
- **I/13 -> VII/20 Riemannian Metrics** (`FOUNDATION`):
  a Riemannian metric is a smoothly varying inner product on tangent spaces.
- **I/14 -> VII/08 Principal and Frame Bundles** (`FOUNDATION`):
  bases, frames, and orthonormalization become geometric structures.
- **I/16–I/17 -> metric/curvature operator calculations** (`SEE_ALSO`):
  self-adjoint operators and quadratic forms provide the local algebraic model.

### Volume VIII — Algebraic Topology

- **I/05–I/06 -> VIII/16 Chain Complexes** (`FOUNDATION`):
  homology is built from kernels modulo images of consecutive linear/module maps.
- **I/03/I/07 -> VIII/17–VIII/18 homology computations** (`SEE_ALSO`):
  basis/rank/matrix computations become boundary-matrix calculations.
- **I/06 -> exact sequences and induced maps** (`FOUNDATION`):
  kernel/image reasoning underlies exactness.
- **I/08 -> Euler-characteristic matrix/rank bookkeeping** (`SEE_ALSO`):
  finite alternating rank counts inherit linear-algebra discipline.

## References and series navigation

Do not duplicate bibliography entries or long chapter-by-chapter bridge prose here.
For complementary sources and reader-facing series bridges, use
`frontmatter/references-and-series-bridges.tex`.

For the repository-wide map use:

`books/CROSS_VOLUME_MATHEMATICAL_NAVIGATION.md`

For series-level navigation use:

`books/SERIES_NAVIGATION.md`

The back-matter `Volume I Epilogue / What Comes Next` is the reader-facing continuation
summary; this file is the editorial dependency graph.

## Reading principle

Use `FOUNDATION` when the later topic genuinely requires the earlier language.
Use `CONTINUATION` when the same structure is generalized.
Use `SEE_ALSO` for a conceptual parallel that helps orientation but is not a formal
prerequisite.

When two routes meet, the theorem statement in the destination chapter decides the actual
hypotheses. The graph is navigation, not proof.
