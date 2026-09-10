# Volume I mathematical review — I/01–I/18

Pinned review base: `ac26c0fc9bc9d9c35664a089821d0efca850064a`

This is the first pass of the final professional review of **Volume I — Linear Algebra**.
It is intentionally conservative: canonical chapter source is changed only when a concrete
mathematical defect has been demonstrated. Broad stylistic rewriting is not a substitute
for checking hypotheses, fields, dimensions, directions of maps, or proof logic.

The review is performed against the house conventions centralized in
`frontmatter/notation-and-conventions.tex`: finite dimensionality is invoked only when
needed; the scalar field is `\mathbb F` unless a theorem requires `\mathbb R` or
`\mathbb C`; complex inner products are linear in the first argument; and `A^*`/`T^*`
denote conjugate transpose/adjoint.

## Review contract

Every definition, theorem, proof, worked example, solved dossier, exercise, hint, and
solution in I/01–I/18 is checked against these invariants:

1. distinguish vector-space statements valid over an arbitrary field from statements
   requiring `\mathbb R` or `\mathbb C`;
2. state finite-dimensional hypotheses exactly where dimension, determinants, matrices,
   characteristic polynomials, canonical forms, adjoints, or compactness-style arguments
   require them;
3. distinguish an invariant vector/operator from its coordinate column/matrix;
4. preserve the direction of change-of-basis matrices;
5. distinguish similarity from equivalence under independent domain/codomain basis changes;
6. separate algebraic multiplicity, geometric multiplicity, and minimal-polynomial data;
7. state splitting-field/algebraic-closure hypotheses for eigenvalue and canonical-form
   results;
8. distinguish arbitrary, self-adjoint/Hermitian, unitary/orthogonal, and normal operators;
9. preserve the Volume I convention that complex inner products are linear in the first
   argument;
10. use transpose only in the real case when the adjoint/conjugate transpose is intended;
11. state positivity and definiteness hypotheses for inner-product and quadratic-form
   arguments;
12. separate exact algebraic statements from numerical-conditioning claims;
13. distinguish full, reduced, and economy-size QR/SVD factorizations where dimensions
   matter;
14. keep pseudoinverse, least-squares, and minimum-norm conclusions distinct;
15. state norm hypotheses in Eckart–Young–Mirsky claims;
16. never infer diagonalizability merely from the existence of eigenvalues;
17. never infer normality from diagonalizability by a nonorthonormal basis;
18. keep theorem statements, proofs, examples, exercises, hints, and solutions logically
   synchronized.

## I/01–I/06 — vector spaces and linear maps

### I/01 — Scalars, Vectors and Linear Combinations

Audit:

- field axioms versus properties special to `\mathbb R` or `\mathbb C`;
- vector-space axioms and the role of the zero vector;
- linear combinations and span without coordinate dependence;
- uniqueness statements only after linear independence/basis hypotheses are available;
- no use of length, angle, orthogonality, or positivity before an inner product is introduced;
- examples over polynomial/function spaces are checked as genuine vector-space examples.

### I/02 — Subspaces, Span and Linear Independence

Audit:

- nonempty/subspace criteria;
- span as the smallest subspace containing a set;
- linear dependence versus a merely nontrivial representation;
- sums and intersections of subspaces;
- direct sum only when the intersection condition needed for uniqueness is present;
- finite-list arguments distinguished from arbitrary-family statements.

### I/03 — Bases and Dimension

Audit:

- basis means spanning plus linearly independent;
- coordinate uniqueness follows from the basis property;
- basis-extension/reduction arguments use finite-dimensional hypotheses where needed;
- dimension comparisons are justified through injections/surjections or exchange arguments;
- rank-nullity is not imported before kernels/images are established;
- statements about “same dimension implies isomorphic” are restricted to the intended
  finite-dimensional setting.

### I/04 — Coordinates and Change of Basis

Audit:

- coordinate maps are isomorphisms only after an ordered basis is fixed;
- `P_{C\leftarrow B}` converts `B`-coordinates to `C`-coordinates, never the reverse;
- the underlying vector is unchanged by coordinate conversion;
- composition of transition matrices follows arrow direction;
- similarity is reserved for endomorphism matrices under one coordinated basis change;
- coordinate calculations agree with the computational spine added before this review.

### I/05 — Linear Transformations

Audit:

- linearity is checked against both addition and scalar multiplication;
- composition order is correct;
- inverse maps are linear when a linear bijection is inverted;
- injective/surjective/bijective statements are not conflated;
- matrix language is not silently used before bases are chosen;
- dimension-based implications are explicitly finite-dimensional.

### I/06 — Kernels, Images and Isomorphisms

Audit:

- kernel and image are subspaces;
- injectivity iff kernel is zero;
- surjectivity iff image is the codomain;
- rank–nullity uses finite dimension of the domain;
- quotient/isomorphism statements identify the actual induced map;
- “isomorphic” is distinguished from “equal” or “canonically identical.”

## I/07–I/12 — matrices, eigenstructure, and canonical forms

### I/07 — Matrix Representation of Linear Maps

Audit:

- domain and codomain bases are named independently;
- matrix multiplication matches composition order;
- basis-change formula acts on input coordinates on the right and output coordinates on
  the left;
- matrix equivalence for maps between different spaces is distinguished from similarity
  for endomorphisms;
- rank is basis invariant;
- square-matrix assumptions are present only where genuinely needed.

### I/08 — Determinants and Trace

Audit:

- determinant is defined only for square matrices/endormorphisms of equal finite dimension;
- determinant multiplicativity and invertibility criterion are stated correctly;
- trace is similarity invariant but not invariant under arbitrary two-sided equivalence;
- cyclic trace identities are used only for compatible finite matrices;
- determinant/trace are not treated as a complete set of similarity invariants;
- real/complex scalar-field specializations are kept separate when signs or conjugation
  matter.

### I/09 — Eigenvalues and Eigenvectors

Audit:

- eigenvectors are nonzero;
- eigenvalues may fail to lie in the base field;
- characteristic-polynomial roots are interpreted over the stated field/splitting field;
- eigenspaces are kernels of `T-\lambda I`;
- eigenspaces for distinct eigenvalues are linearly independent;
- algebraic and geometric multiplicities are distinguished and bounded correctly;
- spectral claims are not generalized from normal/self-adjoint operators prematurely.

### I/10 — Invariant Subspaces and Triangularization

Audit:

- invariance means `T(W)\subseteq W`;
- restriction and induced quotient maps are defined only when the required invariance holds;
- upper-triangular representation depends on a suitable ordered basis/flag;
- finite-dimensional triangularization requires the characteristic polynomial to split
  over the field (or an explicitly sufficient substitute);
- triangular form is not identified with diagonal form;
- eigenvalue information is read from the diagonal only under the correct square setting.

### I/11 — Diagonalization and Minimal Polynomials

Audit:

- diagonalizability means existence of a basis of eigenvectors;
- the characteristic polynomial splitting condition is separated from sufficiency;
- the minimal polynomial divides every annihilating polynomial and the characteristic
  polynomial in the finite-dimensional setting;
- diagonalizability iff the minimal polynomial splits into distinct linear factors;
- repeated eigenvalues do not by themselves obstruct diagonalizability;
- geometric multiplicities are compared correctly with algebraic multiplicities.

### I/12 — Canonical Forms

Audit:

- Jordan form is used only when the relevant polynomial splits into linear factors;
- rational/Frobenius canonical form is distinguished from Jordan form and works over the
  stated arbitrary field;
- block sizes and elementary/divisor data are invariant up to the stated ordering;
- generalized eigenspaces are not confused with eigenspaces;
- nilpotent Jordan-chain lengths agree with powers of the nilpotent part;
- existence and uniqueness claims identify exactly what is canonical and what depends on
  basis/block ordering.

## I/13–I/18 — inner-product geometry, spectral theory, and SVD

### I/13 — Inner Products and Orthogonality

Audit:

- complex conjugation follows the house convention: linear first argument,
  conjugate-linear second;
- positivity means `\langle x,x\rangle>0` for nonzero `x`;
- Cauchy–Schwarz and triangle inequality are proved from positive definiteness;
- orthogonal complements are subspaces;
- finite-dimensional decomposition statements include the needed hypotheses;
- bilinear symmetric forms are not silently identified with complex inner products.

### I/14 — Gram–Schmidt and Orthogonal Projection

Audit:

- Gram–Schmidt starts from a linearly independent list (or handles discarded zero residuals
  explicitly);
- normalization never divides by zero;
- orthogonal projection formulas use an orthonormal basis or include Gram-matrix corrections;
- `P=QQ^*` is asserted only when the columns of `Q` are orthonormal;
- QR dimensions distinguish square/full and reduced factorizations;
- full-column-rank assumptions are present where triangular `R` is required to be invertible;
- least-squares normal equations are distinguished from the numerically preferable QR solve.

### I/15 — Orthogonal and Unitary Operators

Audit:

- orthogonal/unitary means preservation of the inner product, equivalently `T^*T=I`
  in finite-dimensional coordinates;
- inverse equals adjoint;
- eigenvalues of a unitary operator have modulus one;
- orthogonal real matrices may have nonreal eigenvalues, so real diagonalization is not
  asserted automatically;
- determinant restrictions are stated correctly (`\pm1` over the real orthogonal case);
- normality consequences are not confused with self-adjointness.

### I/16 — The Spectral Theorem

Audit:

- real symmetric operators/matrices are orthogonally diagonalizable;
- complex Hermitian operators/matrices are unitarily diagonalizable with real eigenvalues;
- complex normal operators are unitarily diagonalizable, with no claim that their
  eigenvalues are real;
- converse statements use the correct class of diagonalization;
- orthogonality of eigenspaces is asserted under the correct normal/self-adjoint hypotheses;
- polynomial/functional constructions preserve the stated spectral data.

### I/17 — Quadratic Forms

Audit:

- real quadratic forms are represented by symmetric matrices after symmetrization;
- complex analogues use Hermitian/sesquilinear language when positivity is discussed;
- change of variables for forms is congruence, not similarity;
- Sylvester’s law of inertia is stated over the real field with the proper nonsingular
  congruence interpretation;
- positive definite, semidefinite, indefinite, and degenerate are distinguished;
- principal-axis arguments invoke the appropriate spectral theorem.

### I/18 — Singular Value Decomposition

Audit:

- SVD is restricted to real/complex finite-dimensional inner-product spaces/matrices;
- rectangular dimensions of `U`, `\Sigma`, and `V^*` are compatible;
- singular values are nonnegative square roots of eigenvalues of `A^*A`;
- kernels of `A` and `A^*A` are identified correctly;
- rank, operator norm, Frobenius norm, and condition number are read from singular values
  with their exact hypotheses;
- pseudoinverse reciprocates only positive singular values;
- least-squares and minimum-norm claims distinguish consistent, inconsistent, full-rank,
  and rank-deficient cases;
- Eckart–Young–Mirsky errors use the stated spectral/Frobenius norms;
- the closing synthesis remains consistent with the full volume:
  `bases -> matrices -> eigenstructure -> orthogonality -> spectral theorem -> SVD`.

## Standing proof-quality requirements

Across all 18 chapters:

- every proof proves the statement actually displayed;
- all symbols used in a proof are introduced before use;
- a converse is never smuggled into a one-way theorem;
- existence and uniqueness are proved separately when both are claimed;
- dimension counts do not replace a missing injectivity/surjectivity argument unless the
  finite-dimensional equality-of-dimensions theorem has been invoked correctly;
- coordinate proofs state the chosen bases;
- complex proofs keep conjugation on the correct argument;
- numerical remarks do not modify exact mathematical conclusions;
- examples test hypotheses rather than silently relying on stronger ones.

## Outcome and source-edit rule

This review layer is deliberately non-destructive. It records the mathematical correction
standard for the canonical 18-chapter corpus and prohibits speculative global rewriting.
A chapter-local source correction should be made only when a specific defect is identified,
with the exact theorem/example/exercise and corrected hypothesis or proof recorded in the
commit diff.

The historical Volume I freeze evidence predates the later editorial changes through
`ac26c0f`. Therefore this professional-review sequence does not claim that the old
`freeze/VOLUME01_FREEZE_MANIFEST.sha256` describes the current source tree. Refreshing
release hashes is a separate final freeze/release step after the three review commits.
