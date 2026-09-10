# Volume I professional review — exercises, hints, solutions and theorem coverage

Review sequence base: `ac26c0fc9bc9d9c35664a089821d0efca850064a`

This is the third and final pass of the **I/01–I/18** professional review.

The historical Volume I freeze report records the earlier release baseline as:

- 18 canonical chapters;
- reconciliation PASS / zero unresolved;
- 216 solved dossiers (12 per chapter);
- 144 short exercises / 144 hints / 144 short-exercise solutions;
- a successful canonical PDF build.

Later editorial commits changed current source after that baseline, so the old freeze
manifest is not treated here as a hash invariant. The review instead checks the **current
active source tree** and leaves release-hash regeneration to a separate freeze-refresh
commit.

## Semantic reconciliation rules

For every I/01–I/18 chapter:

1. each exercise is solvable from material available by that point unless explicitly
   identified as exploratory;
2. each hint advances a method, identifies a useful theorem, or reduces the problem rather
   than merely repeating the question;
3. each solution answers exactly the stated exercise/problem;
4. every assumption used in the solution appears in the statement or has already been
   established;
5. scalar-field hypotheses are preserved from statement through solution;
6. finite-dimensional assumptions are not silently introduced or dropped;
7. basis-dependent claims name the relevant basis;
8. matrix dimensions are compatible in every displayed product;
9. eigenvalue exercises distinguish base-field roots, algebraic multiplicity, and geometric
   multiplicity;
10. diagonalization exercises do not confuse splitting with diagonalizability;
11. canonical-form exercises identify whether Jordan or rational/Frobenius structure is
    intended;
12. complex inner-product exercises use the house conjugation convention;
13. projection and QR exercises state orthonormality/rank assumptions when required;
14. spectral-theorem exercises identify self-adjoint/Hermitian, unitary/orthogonal, or normal
    hypotheses correctly;
15. quadratic-form exercises use congruence rather than similarity;
16. SVD exercises keep rectangular dimensions, rank, conditioning, pseudoinverse, and
    least-squares conclusions distinct;
17. every canonical theorem environment contains an accompanying proof;
18. theorem statements and their downstream exercises agree on hypotheses and notation.

## Chapter-by-chapter coverage targets

### I/01 — Scalars, Vectors and Linear Combinations

Exercises should test vector-space axioms, linear combinations, span, and examples over more
than `\mathbb R^n`. Solutions must not import inner-product language.

### I/02 — Subspaces, Span and Linear Independence

Coverage should include subspace tests, span, dependence certificates, sums/intersections,
and direct-sum uniqueness. Hints should distinguish “show closure” from “solve coefficients.”

### I/03 — Bases and Dimension

Coverage should include basis verification, extension/reduction, dimension comparison, and
coordinate uniqueness. Dimension arguments must identify finite-dimensional hypotheses.

### I/04 — Coordinates and Change of Basis

Exercises must test the direction of `P_{C\leftarrow B}` and composition of coordinate
changes. At least one task should force the reader to distinguish a vector from its coordinate
column.

### I/05 — Linear Transformations

Coverage should include linearity tests, composition, inverse maps, injectivity/surjectivity,
and examples not initially given by matrices.

### I/06 — Kernels, Images and Isomorphisms

Exercises should connect kernel with injectivity, image with surjectivity, rank–nullity, and
induced quotient/isomorphism ideas. Solutions should not replace proofs by dimension counts
without the required hypotheses.

### I/07 — Matrix Representation of Linear Maps

Coverage should include domain/codomain bases, composition, rank, and two-sided basis change.
Hints must make matrix dimensions and basis direction explicit.

### I/08 — Determinants and Trace

Exercises should test determinant multiplicativity, invertibility, similarity invariance of
trace/determinant, and the limits of these invariants. Non-square matrices must not be assigned
determinants.

### I/09 — Eigenvalues and Eigenvectors

Coverage should include characteristic-polynomial calculations, eigenspaces, multiplicities,
and examples where eigenvalues leave the base field. Hints should not presuppose
diagonalizability.

### I/10 — Invariant Subspaces and Triangularization

Exercises should distinguish invariant subspaces from eigenspaces and test the polynomial-
splitting hypothesis behind triangularization.

### I/11 — Diagonalization and Minimal Polynomials

Coverage should connect eigenbasis criteria, algebraic/geometric multiplicities, minimal
polynomials, and the square-free split minimal-polynomial criterion.

### I/12 — Canonical Forms

Exercises should distinguish Jordan from rational canonical form, generalized eigenvectors
from eigenvectors, and block-size invariants from arbitrary block ordering.

### I/13 — Inner Products and Orthogonality

Coverage should include Cauchy–Schwarz, norms induced by inner products, orthogonal
complements, and complex conjugation under the house convention.

### I/14 — Gram–Schmidt and Orthogonal Projection

Exercises should cover orthonormalization, projection, QR, and least squares. Rank deficiency
and zero residuals must be handled explicitly rather than hidden by normalization.

### I/15 — Orthogonal and Unitary Operators

Coverage should include `T^{-1}=T^*`, norm/inner-product preservation, eigenvalue modulus,
and real orthogonal examples with complex eigenvalues.

### I/16 — The Spectral Theorem

Exercises should separately test real symmetric, complex Hermitian, unitary, and normal
cases. Solutions must not claim real eigenvalues for arbitrary normal operators.

### I/17 — Quadratic Forms

Coverage should include matrix representation, change by congruence, definiteness, principal
axes, and Sylvester inertia with its real-field hypotheses.

### I/18 — Singular Value Decomposition

Coverage should include construction from `A^*A`, rank/norms, condition number,
pseudoinverse, rank-deficient least squares, and Eckart–Young–Mirsky error formulas. The
exercise layer should reinforce the volume-wide coordinate/projection/SVD computational
spine.

## High-risk theorem/exercise pairs

### Basis change and matrix representation

A hint or solution that multiplies transition matrices must identify source and target
coordinate systems. Reversing one arrow can yield a dimensionally legal but mathematically
wrong computation.

### Triangularization, diagonalization, and canonical forms

Exercises must preserve field/splitting hypotheses. “Characteristic polynomial splits” is
enough for triangularization in the finite-dimensional setting, but not for diagonalization.
Jordan form requires the appropriate splitting hypothesis.

### Complex inner products and adjoints

All formulas must use the Volume I convention that the inner product is linear in the first
argument. Importing a textbook formula written for the opposite convention without
conjugation changes is a blocking error.

### Projection and QR

`QQ^*` is an orthogonal projector only when the columns of `Q` are orthonormal. QR-based
least squares must distinguish full-column-rank solves from rank-deficient cases.

### Spectral theorem

Self-adjoint/Hermitian, unitary/orthogonal, and normal results must not be mixed. In
particular, normal complex operators are unitarily diagonalizable but need not have real
eigenvalues.

### Quadratic forms

Change of variables is congruence, not similarity. Real signatures/inertia statements must
not be exported unchanged to arbitrary complex bilinear forms.

### SVD and pseudoinverse

SVD exists for rectangular real/complex matrices. Pseudoinverse solutions solve least
squares generally and select minimum norm in the appropriate solution set; they are not
ordinary inverses unless the matrix is square and invertible.

## Executable active-source audit

Run:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass `
  -File .\books\vol01_linear_algebra\AUDIT_VOLUME01_ACTIVE_SOURCES.ps1 `
  -Repo $PWD
```

The audit checks:

- exactly 18 active chapter includes, I/01 through I/18;
- all active chapter files exist;
- unique labels across current Volume I TeX sources;
- current Volume I internal references resolve;
- balanced theorem/proof, exercise/hint, and problem/exercise/solution structure;
- at least one proved theorem per chapter;
- at least the established solved-dossier floor per chapter;
- no TODO/FIXME/TBD/PLACEHOLDER markers;
- 18 `FROZEN / COMPLETE` Volume I chapter-status rows;
- no structural source errors before the PDF build.

The master APPLY script then performs a canonical `latexmk` build and rejects undefined
references, undefined citations, or multiply defined labels reported in `book.log`.

## Release rule

These three professional-review commits are editorial QA commits. They do **not** silently
rewrite the historical freeze manifest.

Because current Volume I source has advanced beyond the old freeze baseline, the next
release step after this review should explicitly rebuild Volume I and regenerate the Volume I
freeze manifest/report from the reviewed source tree. That keeps “review complete” and
“release hashes refreshed” as two auditable facts rather than conflating them.
