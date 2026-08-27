# VI/33 Full-Solutions Audit — O_X-Modules and Quasi-Coherent Sheaves

## Standard

This refinement continues the VI/24–VI/32 detailed-proof standard.

The live VI/33 corpus had:
- 24 exercises;
- 12 problem dossiers;
- 5 challenges.

To keep the established refinement architecture, this package expands the chapter to:
- **26 exercises with detailed solutions**;
- **20 problem dossiers with full-solution guards**;
- **5 complete challenge solutions**.

The two added exercises and eight added problem dossiers are canonical VI/33 extensions only.  No new legacy
source IDs are claimed.

## Central affine dictionary

The detailed layer develops and repeatedly proves the compatibility formulas

`M~(D(f)) = M_f`

`(M~)_p = M_p`

`Gamma(Spec A, M~) = M`

and the affine equivalence

`A-Mod ~= QCoh(Spec A)`.

## Exactness

VI.33.P2 is expanded into a full proof:

1. localize an exact module sequence at every prime;
2. identify the localized modules with stalks of tilde sheaves;
3. use stalkwise exactness of sheaves.

The package also adds explicit kernel/cokernel consequences:

`~ker(u) ~= ker(~u)`

`~coker(u) ~= coker(~u)`.

This gives a concrete affine proof that quasi-coherent kernels and cokernels are again quasi-coherent.

## New canonical dossiers P13–P20

- P13: restriction to `D(f)` equals sheafification of `M_f`;
- P14: kernels and cokernels under tilde;
- P15: quasi-coherent kernels and cokernels on schemes;
- P16: module isomorphisms detected by localizations/stalks;
- P17: modules annihilated by `I` live on `Spec(A/I)`;
- P18: coherent kernels/images/cokernels on Noetherian affines;
- P19: affine pullback stalk formula;
- P20: support of tensor products of finite modules.

## Challenge strengthening

### C1
Quasi-coherent ideal sheaves are glued affine-locally to closed subschemes, with uniqueness and the converse
construction included.

### C2
Finite locally free sheaves on `Spec A` are identified with finitely generated projective `A`-modules, including
the locally constant rank function and connected-component consequence.

### C3
The finite-generation hypothesis in the support theorem is shown to be essential using

`A = Z`, `M = Q/Z`.

Here `Ann(M)=0`, but the generic point is absent from the support.

### C4
Base change of `Spec(A/I)` is proved to be `Spec(B/IB)`.  The solution explicitly avoids a common error:
pullback is right exact but not left exact in general, so `B tensor_A I -> B` need not be injective.  The pulled
back ideal is the image `IB`.

### C5
The affine tilde construction is transformed into the Proj recipe

`D_+(f) -> (M_f)_0`

with overlap compatibility.

## Boundary discipline

VI/33 keeps the finite locally free/projective and locally Noetherian coherent basics already present in the live
chapter, but does not develop:
- Picard groups or line-bundle classification;
- twisting sheaves in detail;
- graded-module/Proj proofs beyond the bridge;
- derived functors or cohomology;
- pushforward quasi-coherence theorems requiring additional hypotheses.

Those remain later material.
