# Companion Part II reconciliation freeze

Generated: **2026-09-26 18:37:55 +02:00**

## Frozen reader-facing state

- Part II problems: **570**
- Part II solutions: **570**
- Exact problem/solution pairs: **570**
- Reader-facing problems without a solution: **0**
- Source-backed migrated solutions retained in provenance: **165**
- Canonical authored solutions: **405**
- Editorial holds: **0**
- CP-II-0494 operator-domain/unboundedness repair: **PASS**
- Part II exact-coverage verifier: **PASS**
- Part II provenance / exact-pair validator: **PASS**
- Full clean Companion build: **PASS**

## Validator correction in v2

The v1 freeze validator incorrectly treated every line containing only `}` as an
orphan brace.  Such lines are valid closers for multiline TeX arguments.  v2 removes
that stylistic heuristic and retains structural brace-balance checks instead.

## SHA-256 manifest

| Artifact | SHA-256 | Bytes | Repository path |
|---|---|---:|---|
| chapter | `d2a15fc8328a65b0cfd96b21afcbf14fcb54313c7b50bbe459675d744c922cf0` | 1296377 | `books/companion_problems_solutions/chapters/part02_volume_ii/chapter.tex` |
| validator | `6435c9c1be47cebc853ac1a5ef6acc9a1ce7f309387314f1c84845a934539f22` | 15130 | `scripts/companion/validate_companion_part02.py` |
| migration_ledger | `c71ae92f5cbd684960c51c47a5163023f149230625cb60f1b577ff1cd341df29` | 245971 | `books/companion_problems_solutions/metadata/PART_II_MIGRATION.tsv` |
| migration_summary | `18b3b471d8fed24b8a0b7a6bb8810587e1409339e26b7308a8736cdf661f607d` | 2580 | `books/companion_problems_solutions/metadata/PART_II_MIGRATION_SUMMARY.md` |
| companion_pdf | `cd95d7338c053725479db5e11a14ae53066a38b39da0c9a636273fd0f138fd89` | 6907149 | `books/companion_problems_solutions/book.pdf` |

Machine-readable manifest: `metadata/PART_II_RECONCILIATION_FREEZE_SHA256.tsv`.
