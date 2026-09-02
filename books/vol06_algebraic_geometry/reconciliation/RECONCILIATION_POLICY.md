# Volume VI Reconciliation Policy

The Volume VI freeze is evidence-driven.

1. `book.tex` is authoritative for the 49 active canonical chapter paths.
2. `editorial/SOURCE_MIGRATION.tsv` is authoritative for legacy-source routing.
3. Every mapped Volume VI source rule is represented instance-by-instance in
   `VOLUME06_SOURCE_RULE_RECONCILIATION.tsv`.
4. Every active canonical chapter must exist, contain substantive chapter
   structure, have labels, preserve referenced chapter figure inputs, and be
   free of suspicious encoding signatures.
5. Duplicate labels and unresolved canonical references block freeze.
6. The previously recorded successful canonical build is required for
   `FREEZE_READY`; the freeze commit performs a new clean build.
7. Problem/exercise/hint/solution counts are audited but are not forced into an
   artificial identical count across chapters.
8. On PASS, all 49 Volume VI status rows become `DRAFTED / FREEZE_READY`.
9. The reconciliation manifest protects mathematical source files and
   reconciliation evidence; README/status metadata are intentionally excluded
   because the freeze transition changes them.
