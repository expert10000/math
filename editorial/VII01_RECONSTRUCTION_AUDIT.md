# VII/01 — Topological Manifolds — Reconstruction audit

## Target state
The canonical target chapter did not exist on `main` at audit time.  This package is therefore **create-only**, not a refinement of a live `chapter.tex`.

## Migration authority
`editorial/SOURCE_MIGRATION.tsv` maps VII/01 material from:
- `chapters/tex/theory-of-differential-geometry-1.tex` — explicit `topological manifold|Hausdorff|second countable` selector and inherited descendants;
- `chapters/tex/theory-of-geometry.tex` — topological surface/manifold and quotient/identification blocks, including legacy Problems 1 and 2;
- `chapters/tex/theory-of-geometry-II.tex` — overlapping foundation material to compare and merge, not preserve as a separate chapter.

The reconstruction deliberately excludes smooth-atlas/maximal-atlas material routed to VII/02.

## Preserved legacy problem material
The six substantive subproblems of the two mapped legacy problem groups are carried into the solved dossiers:
1. double cone is not a surface;
2. plane with two origins;
3. uncountable discrete family of surfaces;
4. two-sheeted torus self-cover;
5. two-sheeted torus-to-Klein-bottle cover;
6. three pairwise nonconjugate involution subgroups of the torus.

The remaining dossiers/exercises are editorial reconstruction material designed to make VII/01 a self-contained modern chapter; they are not presented as verbatim legacy problems.

## Ledger action
The APPLY script changes only the exact VII/01 status row from
`PLANNED / MAP_AND_REWRITE`
to
`DRAFTED / REVIEW_AND_FREEZE`.
