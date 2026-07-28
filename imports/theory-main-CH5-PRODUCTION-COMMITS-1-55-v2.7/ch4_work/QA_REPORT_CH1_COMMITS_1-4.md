# QA Report - Chapter 1 Production Commits 1-4

## Build

- Engine: `latexmk -pdf`
- Master source: `main.tex`
- Result: successful
- Output: `build/main.pdf`
- Final page count: 166

## Content verification

- Section 1.2 editorial rewrite is present.
- Four new reusable Chapter 1 TikZ sources are integrated.
- Section 1.12 contains five integrated worked examples.
- Section 1.13 contains twelve graded exercises.
- Chapter summary follows as Section 1.14.

## Visual verification

Rendered Chapter 1 pages were inspected for:

- clipped text,
- overlapping boxes,
- broken equations,
- figure overflow,
- malformed glyphs,
- inconsistent page breaks.

No blocking visual defects were found.

## Known non-blocking build messages

The existing glossary/index workflow reports missing intermediate glossary files
on the first pass. The PDF is nevertheless produced successfully, and this
behavior predates these Chapter 1 commits.
