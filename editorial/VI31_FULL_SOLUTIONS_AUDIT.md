# VI/31 Full-Solutions Audit — Codimension

## Standard

This refinement continues the VI/24–VI/30 detailed-proof standard.

- 26/26 exercise solutions are expanded into height/chain/additivity arguments.
- 20/20 problem dossiers receive detailed proofs.
- 5/5 challenges receive complete solutions.
- Reader/full-solutions separation is normalized.

## Legacy ownership

VI/31 owns the two codimension-specific numbered AG8 anchors:

1. **AG8-P2b** — codimension via local rings and dimension–codimension additivity.
2. **AG8-P3c** — failure of that additivity on a non-equidimensional scheme.

AG8-P3d remains VI/30-owned; AG8-P3a remains reserved for VI/32.

## Mathematical strengthening

The detailed layer now proves:

- codimension as relative irreducible-closed chain length;
- affine codimension equals prime height;
- codimension equals `dim O_{X,eta_Y}`;
- the infimum formula over points of an irreducible closed subset;
- the component-minimum version for reducible closed subsets;
- `dim Y + codim(Y,X) = dim X` for varieties;
- the AG8-P3c counterexample;
- exact additivity along nested subvarieties;
- the general concatenation inequality;
- coordinate-subspace, closed-point, diagonal, product, and principal-hypersurface computations;
- reduction invariance;
- why equation counting does not define codimension.

## Challenge correction

Challenge VI.31.C4 originally asked for the diagonal of a general `variety`, while the book's current convention
defines a variety as integral finite type over `k` and does not automatically include separatedness.
The package corrects C4 to assume `X` separated over `k`, so the diagonal is a closed subvariety.

## Divisor boundary

VI/31 stops at

`codimension one <=> height one <=> dim O_{X,x}=1`.

It does not prove or use:
- discrete valuation orders;
- principal-divisor sums;
- Weil divisor groups;
- Cartier divisors;
- divisor class groups.

Those remain in the later divisor arc.

## Remaining boundary

VI/32 retains closed-point local dimension, tangent spaces, embedding dimension, regularity, and AG8-P3a.
