# QA Report - Chapter 1 Commits 12-15

**Date:** 2026-07-27  
**Chapter:** Mathematical Language of Physics  
**Status:** PASS - Publication Ready

## Build

- Engine: pdfLaTeX via latexmk
- Full-book output: `build/main.pdf`
- Pages: 182
- File size: 1061638 bytes
- Fatal LaTeX errors: 0
- Undefined references or citations: 0
- Overfull or underfull box warnings: 0
- Other captured LaTeX/package warnings: 0

## Computational companion

- All four Python programs executed successfully.
- Projection, rotation, linear-transformation, and Gram-Schmidt PDF figures regenerated from source.
- Wolfram Language source inspected as plain-text executable input.
- Code listings compile without shell escape or external syntax-highlighting dependencies.

## Repository integration

- Chapter 1 computational section included in the canonical chapter source.
- Glossary expanded with scalar, basis, norm, inner product, linear independence, linear transformation, eigenvector, and orthogonal projection.
- Frontmatter notation table expanded.
- Bibliography entries added for Strang, NumPy, Matplotlib, and Wolfram Language.
- Chapter 2 now has a stable cross-reference label.
- Chapter 1 summary links to Chapter 2 and the computational companion.

## Visual inspection

Rendered PDF pages 57-65 were inspected at 120 dpi. Checks included:

- no clipped listings or captions;
- no overlapping text or figures;
- consistent page headers and numbering;
- acceptable figure scaling;
- clean transition from computational material to worked examples and exercises.

Contact sheet: `ch1_12_15_contact.png` (QA artifact, not required by the manuscript build).

## Freeze decision

Chapter 1 satisfies its editorial, mathematical, visual, computational, integration, and build gates. It is frozen under the maintenance rules in `docs/CHAPTER01_FREEZE.md`.
