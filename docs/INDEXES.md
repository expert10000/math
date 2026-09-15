# Series indexes

The C10 index set is generated from canonical inputs rather than maintained as
parallel editorial lists:

- `editorial/CHAPTER_STATUS.tsv` supplies the 256 chapter identities and titles.
- Canonical `chapter.tex` files supply named mathematical statements.
- `shared/notation.tex` supplies series-wide notation.
- `reports/series/CROSS_VOLUME_CHAPTER_BRIDGES.tsv` supplies curated reading bridges.

Refresh the bridge ledger first, then rebuild the indexes:

```powershell
python scripts/series/build_cross_volume_navigation.py --repo .
python scripts/series/build_series_indexes.py --repo .
python scripts/series/build_series_indexes.py --repo . --check
```

Generated reader-facing files live in `books/`: `NOTATION_INDEX.md`,
`THEOREM_INDEX.md`, `SUBJECT_INDEX.md`, and `CROSS_VOLUME_INDEX.md`.
Machine-readable theorem and directional-reference audits live in
`reports/series/`.

The directional-reference audit does not treat ordinary local prose such as
“as shown above” as a cross-volume claim. It resolves “previous/next chapter”
against the chapter ledger and flags unresolvable sequence references.
