# Volumes IV–VII asset reconciliation

Baseline: `4c191f6940e0993d6d361b3dfe965820bd15b006`

This commit is an inventory/audit only. It does not add, delete, redraw, or relink mathematical figures.

## Classification policy

- `USED` — reachable from the canonical volume `book.tex` dependency graph.
- `DUPLICATE` — byte-identical extra copy with a recorded canonical target.
- `MISSING_CANONICAL_DESTINATION` — a mathematical render asset exists but no canonical TeX reference was found.
- `OUT_OF_SCOPE` — figure-directory metadata/documentation rather than a render asset.
- `REDRAWN` / `SUPERSEDED` are not inferred automatically; those require a later evidence-based figure commit.

## Volume IV

- assets inventoried: **1**
- USED: **0**
- DUPLICATE: **0**
- MISSING_CANONICAL_DESTINATION: **1**
- OUT_OF_SCOPE: **0**
- unresolved TeX/graphics dependency tokens observed during conservative graph scan: **0**

## Volume V

- assets inventoried: **1**
- USED: **0**
- DUPLICATE: **0**
- MISSING_CANONICAL_DESTINATION: **1**
- OUT_OF_SCOPE: **0**
- unresolved TeX/graphics dependency tokens observed during conservative graph scan: **0**

## Volume VI

- assets inventoried: **417**
- USED: **392**
- DUPLICATE: **8**
- MISSING_CANONICAL_DESTINATION: **4**
- OUT_OF_SCOPE: **13**
- unresolved TeX/graphics dependency tokens observed during conservative graph scan: **2**

## Volume VII

- assets inventoried: **1**
- USED: **0**
- DUPLICATE: **0**
- MISSING_CANONICAL_DESTINATION: **1**
- OUT_OF_SCOPE: **0**
- unresolved TeX/graphics dependency tokens observed during conservative graph scan: **0**

## Release rule

There are zero `UNREVIEWED` rows. Any `MISSING_CANONICAL_DESTINATION` row must be resolved only in a later, figure-specific `feat(vN)` / cleanup commit after mathematical inspection; this audit does not guess whether an unreferenced asset is superseded.
