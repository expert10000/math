# Phase 2 Summary - Canonical Source Selection and Corpus Reduction

Generated: 2026-07-31T16:36:32.814595+00:00

Phase 2 was classification and selection only. No mathematical content was
rewritten, no files were moved, no files were renamed, and no repository
structure was changed.

## Selection scope

The primary source tree for canonical selection was `chapters/tex/`. The source
map also assigns a repository status to every TeX-like file inventoried in
Phase 1.

| Item | Count |
|---|---:|
| TeX-like files classified repository-wide | 3737 |
| Files reviewed in `chapters/tex/` | 169 |
| Selected canonical/module source files | 134 |
| Canonical standalone entrypoints | 118 |
| Canonical build successes | 87 |
| Canonical build failures | 31 |
| Canonical build success rate | 73.73% |
| Canonical missing input edges | 1 |
| Canonical broken label references | 2 |
| Canonical orphan modules | 16 |
| Duplicate decision groups reviewed | 1470 |
| Assets classified | 5253 |

## Repository-wide source status counts

| Status | Count |
|---|---:|
| `CANONICAL` | 118 |
| `DUPLICATE` | 35 |
| `IMPORT` | 3567 |
| `MODULE` | 16 |
| `UNKNOWN` | 1 |

## `chapters/tex/` source status counts

| Status | Count |
|---|---:|
| `CANONICAL` | 118 |
| `DUPLICATE` | 35 |
| `MODULE` | 16 |

## Canonical entrypoint status counts

| Status | Count |
|---|---:|
| `development` | 32 |
| `production` | 86 |

## Asset status counts

| Status | Count |
|---|---:|
| `CANONICAL` | 652 |
| `DUPLICATE` | 317 |
| `GENERATED` | 125 |
| `IMPORT` | 4157 |
| `UNKNOWN` | 2 |


## Decision rules applied

1. Prefer files in `chapters/tex/` over raw imports, generated outputs, and
   archive/history paths.
2. Prefer standalone files that successfully built in the Phase 1 baseline.
3. Prefer non-generated, non-wrapper, non-template editable sources.
4. Resolve exact and structural duplicates by selecting the highest-scoring
   chapter-tree representative and preserving the rest as duplicate/historical
   material.
5. Mark ambiguous files conservatively, with rationale and confidence columns in
   the CSV reports.

## Deliverables produced

- `reports/canonical-source-map.csv`
- `reports/duplicate-decisions.csv`
- `reports/canonical-entrypoints.json`
- `reports/canonical-build-report.json`
- `reports/canonical-assets.csv`
- `reports/canonical-dependency-graph.json`
- `reports/phase2-summary.md`

## Exit criteria status

- Every TeX-like source file has a repository status in
  `canonical-source-map.csv`.
- Canonical corpus identified: yes, as a conservative `chapters/tex/`-based
  selection.
- Duplicate decisions complete: yes, for all Phase 1 duplicate groups.
- Canonical dependency graph generated: yes.
- Canonical entry points compile: partially. Failures remain documented in
  `canonical-build-report.json`; Phase 2 does not fix source files.
- Asset ownership known: yes, classification is recorded in
  `canonical-assets.csv`.

## Notes for Phase 3

Phase 3 should use `canonical-source-map.csv` and
`canonical-entrypoints.json` as the guardrails before introducing common macros,
shared style files, deterministic build scripts, or master book entrypoints.
