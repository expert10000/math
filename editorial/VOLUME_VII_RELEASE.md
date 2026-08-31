# Volume VII Freeze / Release

**Volume:** VII — Differential, Riemannian and Hyperbolic Geometry

**Status:** COMPLETE / FROZEN

## Acceptance gates

- 42/42 canonical chapter-status rows present.
- 42/42 canonical chapter files present and actively included.
- Corpus audit passed after setting all Volume VII rows to `FROZEN` / `COMPLETE`.
- Clean `latexmk` build passed.
- Post-build log check found no undefined-reference, multiply-defined-label, or undefined-citation regression.
- SHA-256 freeze manifest generated for all 42 chapter sources plus canonical volume QA/navigation files.

## Canonical outputs

- Source wrapper: `books/vol07_differential_geometry/book.tex`
- PDF: `books/vol07_differential_geometry/book.pdf` (build artifact; not required to be tracked)
- Audit: `editorial/VOLUME_VII_CORPUS_AUDIT.md`
- Machine audit: `editorial/VOLUME_VII_CORPUS_AUDIT.json`
- Freeze hashes: `editorial/VOLUME_VII_FREEZE_SHA256.tsv`

## Freeze provenance

The freeze was produced immediately after repository commit `c8f9fc131c38fc292ab9be3fa7670d67b3cb499c` and is finalized by the commit containing this release note.

Volume VIII may now begin without reopening Volume VII except through an explicit post-freeze correction commit.
