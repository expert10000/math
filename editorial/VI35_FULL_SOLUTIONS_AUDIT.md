# VI/35 Full-Solutions Audit — Proj

## Standard

This refinement continues the VI/24–VI/34 detailed-proof standard.

The live VI/35 corpus had:
- 24 exercises;
- 12 problem dossiers;
- 5 challenges.

The refinement brings the chapter to:
- **26 exercises with detailed solutions**;
- **20 problem dossiers with guarded full solutions**;
- **5 complete challenge solutions**.

E25–E26 and P13–P20 are canonical VI/35 extensions only. No new legacy source IDs are claimed.

## Core construction

The detailed layer now proves:

- the `V_+` topology and standard-open basis;
- `D_+(f) cap D_+(g) = D_+(fg)`;
- the explicit prime correspondence
  `D_+(f) <-> Spec S_(f)`;
- compatibility of projective standard opens with affine distinguished opens;
- scheme gluing from degree-zero overlap localizations;
- `O_{Proj S,p} ~= S_(p)` with maximal ideal and residue field;
- the graded-module sheaf construction `M -> M~`;
- quasi-coherence and exactness;
- kernels/cokernels after projective sheafification;
- quotient-chart compatibility;
- Veronese invariance of both charts and structure sheaf;
- reducible and nonreduced Proj examples;
- weighted Proj charts;
- irrelevant torsion sheafifying to zero;
- saturation being invisible on projective charts;
- the maximal open domain of a morphism induced by a graded map.

## Added canonical dossiers P13–P20

- P13 — quotient chart ring;
- P14 — kernels and cokernels under projective sheafification;
- P15 — irrelevant torsion sheafifies to zero;
- P16 — Veronese invariance of the structure sheaf;
- P17 — weighted chart rings for weights 1,2,3;
- P18 — saturation is invisible on every standard chart;
- P19 — local dimension of polynomial Proj charts;
- P20 — maximal domain of a graded-map morphism.

## Challenge strengthening

### C1
Saturation is treated both topologically and chartwise. The forward equality
`Proj(S/I) ~= Proj(S/I^sat)` is obtained from equality after homogeneous localization. The converse recovery of a
saturated ideal from its projective ideal sheaf is explicitly assigned the usual finite-generation/Noetherian
setting and left for VI/37's systematic closed-subscheme correspondence.

### C2
The natural map
`S_n -> Gamma(Proj S,O(n))`
is shown not to be an unconditional isomorphism:
- `S=k[x]`, `n=-1` gives failure of surjectivity;
- `S=k[x,y]/(x^2,xy)`, `n=1` gives failure of injectivity through irrelevant torsion.

### C3
For weights 1,2,3:
- the x-chart is affine plane;
- the y-chart is `uw=v^2`;
- the z-chart is `rt=s^3`.

### C4
The largest contraction domain of a degree-preserving map `S -> T` is
`Proj T \ V_+(phi(S_+)T)`, with the chart morphisms and maximality proved.

### C5
The affine atlas, overlap maps, and k-valued points of `Proj k[x_0,...,x_n]` are reconstructed from the general
Proj machine, while global projective-space theory remains reserved for VI/36.

## Boundary discipline

VI/35 keeps the live chapter boundary:
- VI/36 — projective space and homogeneous coordinates;
- VI/37 — closed projective subschemes and homogeneous coordinate ideals;
- VI/38 — projective morphisms and systematic functoriality;
- later chapters — twisting-sheaf invertibility, line bundles, divisor theory, and cohomology.

The general Proj machine is completed here without pulling those later theories forward.
