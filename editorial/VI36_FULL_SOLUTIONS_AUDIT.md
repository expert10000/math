# VI/36 Full-Solutions Audit — Projective Space

## Standard

This refinement continues the VI/24–VI/35 detailed-proof standard.

The live VI/36 corpus had:
- 24 exercises;
- 12 problem dossiers;
- 5 challenges.

The refinement brings the chapter to:
- **26 exercises with detailed solutions**;
- **20 problem dossiers with guarded full solutions**;
- **5 complete challenge solutions**.

E25–E26 and P13–P20 are canonical VI/36 extensions only. No new legacy source IDs are claimed.

## Core geometry

The detailed layer develops:

- homogeneous coordinates and scalar equivalence;
- the standard affine atlas `U_i ~= A^n`;
- explicit transition maps and cocycle identities;
- `P^1` as two affine lines glued by inversion;
- `P^2` as three affine planes;
- the hyperplane at infinity;
- projective linear subspaces, spans, dimensions, and codimensions;
- closed non-rational points and residue fields;
- base extension and splitting of closed points;
- local frames and transition functions for `O(d)`;
- nonnegative global sections of `O(d)`;
- homogenization/dehomogenization;
- Veronese and Segre chart computations;
- projective linear transformations and finite-field point counts.

## New canonical dossiers P13–P20

- P13 — the `PGL_{n+1}` action and scalar kernel;
- P14 — `#P^n(F_q)`;
- P15 — span/intersection dimension formulas for projective linear spaces;
- P16 — homogenization/dehomogenization as inverse chart operations;
- P17 — the transition cocycle for `O(d)`;
- P18 — `O(d) tensor O(e) ~= O(d+e)` from transition factors;
- P19 — the rational normal curve on affine charts;
- P20 — the principal affine Segre chart as `A^{m+n}`.

## Challenge strengthening

C1 gives a complete normalized-basis proof of the uniqueness of a projective transformation between two projective
frames.

C2 derives the cross-ratio both in affine coordinates and by a determinant formula, proving PGL_2-invariance.

C3 writes the six quadratic coordinates of the quadratic Veronese map `P^2 -> P^5` and derives the rank-one
symmetric-matrix family of quadratic relations without claiming the later closed-embedding theorem.

C4 proves that every nonzero rank-one matrix is a Segre tensor `xy^T`, unique up to reciprocal scaling.

C5 proves the section-count formula
`dim H^0(P^n,O(d)) = binom(n+d,n)`
by stars and bars.

## Boundary discipline

VI/36 retains the live chapter boundaries:
- VI/37 — projective subschemes, homogeneous coordinate ideals, scheme-theoretic projective closures and intersections;
- VI/38 — projective morphisms and closed embeddings, including the embedding theorems for Veronese and Segre;
- later chapters — general invertible sheaves, Picard groups, divisor theory, and higher cohomology.

The package uses transition functions of the basic twists because they already belong to VI/36, but does not pull
the later general line-bundle or Picard theory forward.
