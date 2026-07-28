# QA Report - Chapter 2 Commits 16-19

## Build

- Build command: `latexmk -pdf main.tex`
- Result: success
- Output: `build/main.pdf`
- Final length: 194 pages
- LaTeX errors: 0
- Undefined references/citations in final log: 0
- Overfull/underfull box warnings in final log: 0

## Computational verification

- Python companion executed successfully.
- Numerical centered-difference Jacobian matched the analytic Jacobian within the configured tolerance.
- Four generated PDF figures were produced.
- Wolfram Language source was syntax-reviewed but not executed because a Wolfram kernel is not available in the build environment.

## Visual verification

The complete PDF was rendered to PNG at 110 dpi. Chapter 2 pages, including the new visual synthesis, rigorous proofs, code listings, and generated plots, were inspected for:

- clipped text;
- overlapping labels;
- broken glyphs;
- misplaced figures;
- excessive whitespace;
- inconsistent headings.

No blocking layout defects were found. New synthesis and computational figures use fixed placement to preserve reading order.

## Repository repair

The `bookfigure` environment now stores labels encountered inside the figure body and emits them after the caption. This fixes the previous `label without proper reference` behavior and makes figure references reliable.
