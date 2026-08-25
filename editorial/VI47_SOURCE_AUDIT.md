# VI/47 — Čech Cohomology Source Audit

Canonical destination:

- `books/vol06_algebraic_geometry/chapters/ch47_ech_cohomology/chapter.tex`

Live ledger status before application:

- `PLANNED`
- `LEGACY_SOURCE_IDENTIFIED`
- mapped-rule count: **3**
- next action: `MAP_AND_REWRITE`

## Exact source ownership

All three VI/47 rules come from `theory-of-algebraic-geometry-11.tex`, topic `T02`:

1. `T02.SECTION` — selector `Čech|Cech`, destination VI/47;
2. `T02.EXERCISE_CHILDREN` — all problem/exercise/solution descendants of the matched Čech section;
3. `T02.THEORY_CHILDREN` — all theorem-like descendants of the matched Čech section.

The neighboring `T01` flabby material belongs to VI/46, `T03` long-exact/cohomology-exact material belongs to VI/48, and `T04` vanishing material belongs to VI/49. The file fallback is owned by VI/46, not VI/47.

## Reconstructed mathematical scope

The chapter develops:

- ordered covers and finite intersections;
- Čech cochains and the alternating differential;
- the proof that `δ²=0`;
- cocycles, coboundaries, and `\check H^p`;
- two-open and three-open calculations;
- refinements and global Čech cohomology;
- flabby vanishing and the Leray comparison criterion;
- the standard two-affine cover of `\mathbb P^1`;
- explicit Laurent-polynomial calculations of `\mathcal O(n)`;
- the Picard-group interpretation of `\check H^1(\mathcal O_X^\times)`;
- the Čech form of the obstruction that becomes the connecting morphism in VI/48.

## Deliberate boundaries

- The full long exact sequence in sheaf cohomology is deferred to VI/48.
- Affine vanishing for quasi-coherent sheaves is used only as a preview and is proved in VI/49.
- The chapter distinguishes fixed-cover Čech cohomology from derived-functor sheaf cohomology unless a comparison hypothesis is present.

## Production audit

- 8 TikZ figures
- 24 exercises with 24 hints and 24 solutions
- 12 solved problem dossiers
- 5 challenges with solutions
- 68 labels, all unique
