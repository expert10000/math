# VI/37 Full-Solutions Audit — Projective Schemes and Homogeneous Ideals

## Standard

This refinement continues the VI/24–VI/36 detailed-proof standard.

The live VI/37 corpus had:
- 24 exercises;
- 12 problem dossiers;
- 5 challenges.

The refinement brings the chapter to:
- **26 exercises with detailed solutions**;
- **20 problem dossiers with guarded full solutions**;
- **5 complete challenge solutions**.

E25–E26 and P13–P20 are canonical VI/37 extensions only. No new legacy source IDs are claimed.

## Corpus correction

The original Challenge 5 asked for a Noetherian standard graded ring having:
- one minimal prime containing the irrelevant ideal; and
- another minimal prime not containing it.

For a standard graded `k`-algebra with `A_0=k`, this configuration is impossible. Every proper homogeneous prime
is contained in `A_+`; therefore if `A_+` itself were minimal, no distinct homogeneous minimal prime could lie below it.

The challenge is corrected to the phenomenon actually needed in VI/37:
- a homogeneous minimal prime not containing `A_+`; and
- an embedded associated prime equal to `A_+`.

The model is
`A = k[x,y]/(x^2,xy)`,
where `(x)` is minimal and `(x,y)=A_+` is embedded associated. The embedded vertex contribution disappears on Proj.

## Core scheme-theoretic algebra

The detailed layer proves and computes:

- quotient chart rings `(S/I)_(f)`;
- the closed-subsheme identification `Proj(S/I) -> Proj S`;
- projective conic charts;
- transverse and tangent scheme-theoretic intersections;
- union by intersection of ideals and intersection by sums;
- double hyperplanes and nonreduced projective schemes;
- saturation and equality of projective ideal sheaves;
- the empty-Proj criterion;
- projective closure by homogenization and saturation;
- affine cones and cone vertices;
- reduced/integral descent to Proj;
- projectively invisible nilpotents;
- component detection;
- fat points and local length;
- coordinate-ring dependence through Veronese regrading.

## New canonical dossiers P13–P20

- P13 — exact sequence for union/intersection;
- P14 — recovery of saturated ideals from standard-chart ideals;
- P15 — length-three projective fat point;
- P16 — two homogeneous coordinate rings for `P^1`;
- P17 — projective closure of the cusp;
- P18 — complete empty-Proj equivalence;
- P19 — reduced Proj from a nonreduced coordinate ring;
- P20 — embedded irrelevant associated prime.

## Challenge strengthening

C1 proves equality of the actual projective ideal sheaves for `I` and `I^sat`, not merely equality of supports.

C2 gives an explicit nonempty affine ideal whose chosen generators acquire a spurious nonreduced point at infinity
after naive homogenization:
`J=(x^2-y, x^3-xy-x)=(x,y)`.
Saturation by the homogenizing variable removes that extra structure and recovers `(X,Y)`.

C3 computes a tangent intersection with a smooth conic as
`Spec k[epsilon]/(epsilon^2)`.

C4 proves that the affine quadric cone is singular at its vertex while its projective conic is smooth, including
the characteristic-2 check.

C5 uses the corrected associated-prime formulation and explains chartwise why the embedded irrelevant prime disappears.

## Boundary discipline

VI/37 retains the live chapter boundary:
- VI/38 — projective morphisms, general closed embeddings, and the Veronese/Segre embedding theorems;
- later chapters — general invertible sheaves, Picard groups, divisor theory, and sheaf cohomology.

The package develops scheme-theoretic homogeneous equations fully but does not pull the general closed-embedding
or projective-morphism theory forward.
