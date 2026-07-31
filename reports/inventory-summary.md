# Phase 1 Inventory Summary

Generated: 2026-07-31T16:17:26.753700+00:00

Phase 1 was run as an observational baseline. No source files were moved,
renamed, merged, or rewritten. Build outputs were produced in a temporary build
folder recorded in `build-baseline.json`; only report files were written under
`reports/`.

## Headline counts

| Item | Count |
|---|---:|
| TeX files (`.tex`) | 3735 |
| TeX-like support files (`.sty`, `.cls`, `.bib`) | 2 |
| Primary `chapters/tex/` TeX files | 169 |
| Standalone documents (`\documentclass`) | 740 |
| Chapter/module candidates without `\documentclass` | 2995 |
| Primary standalone documents | 146 |
| Primary module candidates | 23 |
| Assets inventoried | 5253 |
| Referenced assets | 3230 |
| Unreferenced assets | 2023 |
| Files with TikZ/TikZ-CD content | 2494 |
| Duplicate groups total | 1470 |
| Exact duplicate groups | 794 |
| Structural duplicate groups | 676 |
| Orphan TeX modules in dependency graph | 2971 |
| Circular dependencies detected | 0 |

## Build baseline

| Item | Count |
|---|---:|
| Build candidates attempted | 740 |
| Successful builds | 571 |
| Failed builds | 169 |
| Timed out | 18 |
| Success rate | 77.16% |
| Files with undefined-reference messages | 145 |
| Undefined-reference message count | 545 |
| Files with real missing-file messages | 96 |
| Real missing-file message count | 140 |
| Files with package/LaTeX errors | 128 |

Failure grouping, approximate:

| Cause | Count |
|---|---:|
| missing files | 96 |
| LaTeX/package errors | 55 |
| timeout | 18 |

## Asset extensions

| Extension | Count |
|---|---:|
| `.jpeg` | 9 |
| `.jpg` | 30 |
| `.pdf` | 167 |
| `.png` | 4987 |
| `.svg` | 60 |

## Classification tag counts

| Tag | Count |
|---|---:|
| `appendix` | 19 |
| `chapter` | 2548 |
| `diagrams` | 2681 |
| `duplicate` | 3711 |
| `exercises` | 222 |
| `generated` | 733 |
| `obsolete` | 14 |
| `section` | 1373 |
| `solutions` | 125 |
| `standalone` | 740 |
| `unknown` | 1 |


## Deliverables produced

- `reports/tex-inventory.csv`
- `reports/tex-inventory.json`
- `reports/asset-inventory.csv`
- `reports/dependency-graph.json`
- `reports/duplicate-report.csv`
- `reports/entrypoints.json`
- `reports/build-baseline.json`
- `reports/inventory-summary.md`

## Notes for Phase 2

- `chapters/tex/` is confirmed as the primary source tree, but canonical files
  should still be inferred from dependency, duplicate, and build data rather
  than filename history.
- The repository still contains raw imported and archived material; this is why
  the total TeX count and duplicate count are high.
- Build failures are documented, not fixed, in Phase 1.
- The dependency graph contains many orphan modules because many raw import files
  are standalone snippets or duplicate snapshots not referenced by a master file.
