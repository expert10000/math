# Volume VI professional review — exercise, hint, theorem and release coverage

## Scope

This is the final reconciliation pass for VI/01–VI/49 after mathematical/hypothesis review
and prerequisite/notation review.

## Static release checks

The accompanying QA verifies or reports:

- exactly 49 canonical `book.tex` chapter includes;
- every included canonical chapter has `chapter.tex`;
- duplicate LaTeX labels across Volume VI;
- suspicious internal Volume-VI references;
- stale legacy `DRAFTED` headers;
- presence/count of Volume-VI rows in `editorial/CHAPTER_STATUS.tsv`;
- detectable VI/01–VI/49 destinations in `editorial/SOURCE_MIGRATION.tsv`;
- presence of the Volume VI freeze report and SHA256 manifest;
- generic diagnostic-prose counts for manual review.

## Manual content reconciliation

Review the following by chapter before declaring the release professionally frozen:

1. every migrated legacy dossier maps to exactly one canonical problem unless an explicit
   merge/override is recorded;
2. every exercise that promises a hint has a useful hint;
3. every solved exercise/problem has a matching solution;
4. theorem-proof exercises do not silently strengthen or weaken the theorem hypotheses;
5. later exercises do not depend on results not yet established;
6. classical algebraic-geometry exercises retain field/algebraic-closure assumptions;
7. divisor exercises retain integral/normal/local-Noetherian assumptions where needed;
8. projective/Proj exercises retain grading and finiteness assumptions where needed;
9. Čech/sheaf-cohomology exercises distinguish cover-dependent Čech constructions from
   derived sheaf cohomology unless a comparison theorem is actually available;
10. all freeze/page metadata is refreshed only from the built PDF.

## Build gate

From `books/vol06_algebraic_geometry`:

```powershell
latexmk -C book.tex
latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error book.tex
```

Then inspect:

```powershell
Select-String -Path ".\book.log" `
  -Pattern "Undefined|multiply defined|LaTeX Error|Package .* Error|Overfull|Underfull"

Get-Item ".\book.pdf"
Get-FileHash ".\book.pdf" -Algorithm SHA256
```

Do not push until the build and final git status are clean.
