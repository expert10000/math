# VI/34 Full-Solutions Audit — Graded Rings

## Standard

This refinement continues the VI/24–VI/33 detailed-proof standard.

The live VI/34 corpus had:
- 24 exercises;
- 12 problem dossiers;
- 5 challenges.

The refinement brings the chapter to:
- **26 exercises with detailed solutions**;
- **20 problem dossiers with full-solution guards**;
- **5 complete challenge solutions**.

E25–E26 and P13–P20 are canonical VI/34 extensions only. No numbered legacy problem is invented.

## Core algebra

The detailed layer proves and computes:

- uniqueness of homogeneous decomposition;
- homogeneous ideal component criterion;
- radicals of homogeneous ideals;
- the homogeneous-element primality test;
- graded quotients, kernels, shifts, and hypersurface sequences;
- homogeneous localization and well-defined degrees;
- exactness of localization and exactness of the degree-zero functor;
- standard projective chart rings `S_(x_i)`;
- conic overlap algebra;
- weighted localization;
- Veronese rings;
- cone scaling and the irrelevant ideal;
- `S_(f) = (S_f)_0` and `M_(f) = (M_f)_0`.

## New canonical dossiers P13–P20

- P13 — unequal-degree localization-in-stages formula;
- P14 — module overlap formula;
- P15 — shifted degree-zero localization and local triviality;
- P16 — Veronese chart equality;
- P17 — weighted chart `k[u,v,w]/(uw-v^2)`;
- P18 — saturation preserves all projective localizations;
- P19 — finite graded presentations by shifts;
- P20 — degree zero as the intrinsic `G_m`-invariant subring.

## Challenge strengthening

C1 proves homogeneous saturation and explains why it removes only irrelevant-direction information.

C2 proves chart equality for Veronese regrading and handles an arbitrary homogeneous chart element by passing to a
power lying in the Veronese.

C3 computes a weighted chart that is an affine quadric cone rather than affine space.

C4 constructs finite graded presentations
`F1 -> F0 -> M -> 0`
with finite sums of shifts and records the Noetherian consequence.

C5 reconstructs the VI/35 Proj program while separating definitions from theorems requiring proof.

## Boundary discipline

VI/34 does not define `Proj S`, its topology, its structure sheaf, twisting sheaves as global sheaves, projective
space, or closed projective subschemes. Those belong to VI/35 and subsequent projective chapters.

The source/scope audit remains unchanged: the AG4 graded-algebra thematic block is consumed here, but no separately
numbered legacy problem is claimed.
