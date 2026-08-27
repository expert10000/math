# VI/32 Full-Solutions Audit — Tangent Spaces and Local Geometry

## Standard

This refinement continues the VI/24–VI/31 detailed-proof standard.

- 26/26 exercise solutions are expanded into local-ring, cotangent-space, Jacobian, and regularity arguments.
- 20/20 problem dossiers receive detailed proofs.
- 5/5 challenge problems receive complete solutions.
- Reader/full-solutions separation is normalized.

## Legacy ownership

VI/32 owns:
1. the AG8 Problem 2 closed-point local-dimension slice;
2. **AG8-P3a**, the remaining local-dimension counterexample;
3. **DG4 Problem 13**, distinguishing two unions of three lines using tangent-space dimension.

This completes the AG8 Problem 3 routing:
- part (d) -> VI/30,
- part (c) -> VI/31,
- part (a) -> VI/32.

## Mathematical strengthening

The detailed layer proves:
- `dim O_{X,x} = ht(p)` on affine schemes;
- the closed-point theorem `dim O_{X,x}=dim X` for varieties;
- the AG8-P3a failure on a non-equidimensional scheme;
- cotangent and tangent spaces from `m/m^2`;
- Nakayama's minimal-generator interpretation of embedding dimension;
- `dim O_{X,x} <= edim_x X`;
- regular-local numerical equality;
- Jacobian tangent equations from dual-number substitutions;
- parabola regularity;
- cusp, node, and crossing singularity calculations;
- nilpotent-thickening singularity;
- non-rational residue-field tangent calculations;
- the cusp normalization comparison;
- intrinsic invariance of regularity;
- product tangent-space splitting;
- DG4 Problem 13 via tangent dimensions 3 versus 2.

## Challenge boundary refinements

### Regularity under localization
Regularity localizes, so the regular locus is stable under generalization.  The package explicitly avoids falsely
claiming that the regular locus of every Noetherian scheme is open.  Openness needs stronger hypotheses such as
finite type over a field / excellence-type conditions.

### Normal versus regular
The quadric cone `xy-z^2=0` is treated as a normal two-dimensional affine semigroup variety but is singular at
its vertex, giving the standard `normal != regular` warning.

### Smoothness boundary
The final challenge distinguishes regular, Jacobian-nonsingular, smooth, geometrically regular, and normal.
It records the finite-type/perfect-field hypotheses under which familiar equivalences hold and keeps systematic
smoothness/differential theory outside VI/32.

## Boundary discipline

VI/32 does not develop:
- Kähler differentials systematically;
- smooth or étale morphisms;
- completions;
- tangent cones in full generality;
- Serre's conditions;
- divisor theory.

The chapter closes the dimension/local-geometry arc rather than absorbing later structural chapters.
