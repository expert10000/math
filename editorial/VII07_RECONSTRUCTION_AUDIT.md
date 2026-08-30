# VII/07 — Vector Bundles: reconstruction audit

## Editorial state

- Canonical chapter: `books/vol07_differential_geometry/chapters/ch07_vector_bundles/chapter.tex`
- Ledger transition: `PLANNED / MAP_AND_REWRITE` -> `DRAFTED / REVIEW_AND_FREEZE`.
- Mapped rule count in `editorial/CHAPTER_STATUS.tsv`: **7**.
- `editorial/SOURCE_MIGRATION.tsv` is **not modified** by this package.

## Legacy-source coverage

Primary mapped material: theory-of-differential-geometry-1.tex (T07 section plus inherited theory/exercise descendants), together with the mapped vector-bundle diagram support files.

The reconstruction preserves the chapter's mapped conceptual territory while rewriting it into the current Volume VII notation and chapter sequence. Material canonically assigned to later chapters is excluded rather than duplicated.

## New chapter architecture

The chapter contains a coherent theory layer, examples, exactly **24 exercises with hints and full solutions**, exactly **12 solved problem dossiers**, and exactly **5 challenge problems with full solutions**. The closing bridge points to VII/08.

## Scope exclusions

Later-chapter topics are mentioned only as forward references where pedagogically useful. No attempt is made to absorb the content already mapped to subsequent canonical chapters.

## QA targets

- 24 `exercise` environments
- 24 `hint` environments
- 12 dossier labels `prob:vii07-NN`
- 5 challenge labels `prob:vii07-chNN`
- 41 `solution` environments
- unique labels
- balanced LaTeX environments
- smoke-compilable with the repository's standard theorem-like environments
