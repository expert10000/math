# VII/09 — Differential Forms: reconstruction audit

## Editorial state

- Canonical chapter: `books/vol07_differential_geometry/chapters/ch09_differential_forms/chapter.tex`
- Ledger transition: `PLANNED / MAP_AND_REWRITE` -> `DRAFTED / REVIEW_AND_FREEZE`.
- Mapped rule count in `editorial/CHAPTER_STATUS.tsv`: **4**.
- `editorial/SOURCE_MIGRATION.tsv` is **not modified** by this package.

## Legacy-source coverage

Primary mapped material: theory-of-differential-geometry-2.tex (T01 differential form/exterior derivative section plus inherited descendants and file-level fallback).

The reconstruction preserves the chapter's mapped conceptual territory while rewriting it into the current Volume VII notation and chapter sequence. Material canonically assigned to later chapters is excluded rather than duplicated.

## New chapter architecture

The chapter contains a coherent theory layer, examples, exactly **24 exercises with hints and full solutions**, exactly **12 solved problem dossiers**, and exactly **5 challenge problems with full solutions**. The closing bridge points to VII/10.

## Scope exclusions

Later-chapter topics are mentioned only as forward references where pedagogically useful. No attempt is made to absorb the content already mapped to subsequent canonical chapters.

## QA targets

- 24 `exercise` environments
- 24 `hint` environments
- 12 dossier labels `prob:vii09-NN`
- 5 challenge labels `prob:vii09-chNN`
- 41 `solution` environments
- unique labels
- balanced LaTeX environments
- smoke-compilable with the repository's standard theorem-like environments
