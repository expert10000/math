# VI/33 source audit — architecture sync resolved

## Status

Resolved by the Volume VI architecture sync.

The former projective arc placed **Graded Rings** at VI/33 and **Coherent and Quasi-Coherent Sheaves** at VI/38. The revised order inserts the sheaf-module bridge before projective geometry:

- VI/33 — $\mathcal O_X$-Modules and Quasi-Coherent Sheaves
- VI/34 — Graded Rings
- VI/35 — Proj
- VI/36 — Projective Space
- VI/37 — Projective Schemes
- VI/38 — Projective Morphisms and Closed Embeddings

The divisor and cohomology arcs remain VI/39–VI/49.

## Migration-ledger split

The legacy `theory-of-algebraic-geometry-9.tex` selector previously mixed
`coherent|quasi-coherent|projective morphism` under one destination. It is now split into two explicit families:

- `T05Q.*` — coherent/quasi-coherent material → VI/33;
- `T05P.*` — projective-morphism overlap → VI/38.

The independent `theory-of-algebraic-geometry-4.tex` projective selectors are shifted by one chapter:

- graded rings VI/33 → VI/34;
- Proj VI/34 → VI/35;
- projective space VI/35 → VI/36;
- projective schemes VI/36 → VI/37;
- projective morphisms VI/37 → VI/38.

This removes the mixed-selector ambiguity while preserving the original source provenance. The projective-morphism overlap from AG9 remains attached to VI/38 rather than being absorbed into the quasi-coherent chapter.

## Reconstruction consequence

VI/34 can now be reconstructed as **Graded Rings** with a clean prerequisite chain:

`structure sheaf → O_X-modules → quasi-coherent sheaves → graded rings → Proj`.
