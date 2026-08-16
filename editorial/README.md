# Editorial Control Plane

This directory is the canonical control plane for the mathematics-series reconstruction.

## Authority

1. `CONTENT_ATLAS.md` defines the frozen eight-volume architecture and canonical chapter codes.
2. `SOURCE_MIGRATION.tsv` defines where legacy source blocks migrate.
3. `CHAPTER_STATUS.tsv` records reconstruction state for every canonical chapter.
4. `DUPLICATE_MAP.tsv` records source files that must remain provenance-only or be archived after comparison.

Historical filenames in `chapters/tex/` are provenance identifiers only. They do not determine chapter order or subject ownership.

## Reconstruction workflow

For each canonical chapter:

1. Select its chapter code from `CHAPTER_STATUS.tsv`.
2. Query `SOURCE_MIGRATION.tsv` for all rows whose `destination` matches that code.
3. Extract unique definitions, theorems, proofs, examples, figures, problems, and solutions from the listed legacy sources.
4. Compare any `COMPARE_AND_MIGRATE`, `ARCHIVE_VARIANT`, or `ARCHIVE_DUPLICATE` lineages before discarding duplicate prose.
5. Create one canonical chapter source under `books/<volume>/chapters/`.
6. Rewrite and merge in the canonical source. Do **not** create `*_corrected_vN.tex` descendants.
7. Update `CHAPTER_STATUS.tsv` through `PLANNED -> IN_PROGRESS -> DRAFTED -> REVIEWED -> FROZEN`.
8. Only after every mapped block from a legacy source has been accounted for may that source be physically moved to an archive location.

## Migration precedence

Higher-precedence `SOURCE_MIGRATION.tsv` rules override lower-precedence rules. Targeted overrides therefore win over thematic section rules, which win over file fallbacks. See `CONTENT_ATLAS.md` for the normative precedence definitions.

## Non-destructive migration rule

The first architecture commit intentionally leaves `chapters/tex/` untouched. The new `books/` tree is built beside the historical archive. Physical source moves happen only after chapter-level extraction and audit, preserving Git history and making every migration reversible.
