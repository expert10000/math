# QA Report - Chapter 1 Commits 9-11

## Build
- Full book compiled successfully with `latexmk -pdf`.
- Output: `build/main.pdf`.
- Final length: 177 pages.
- No fatal LaTeX errors.
- No undefined control sequences.
- No unresolved citations or references after the final pass.

## Commit 9 verification
- Reusable style library loaded from `figures/common/chapter_figure_styles.tex`.
- Twelve new TikZ figures are present and integrated into the active canonical Chapter 1.
- Figures use the common visual palette, arrow conventions, line widths, and LaTeX fonts.
- Modified chapter pages were rendered and visually inspected.

## Commit 10 verification
- Cauchy-Schwarz proof checked algebraically.
- Triangle inequality proof derives correctly from Cauchy-Schwarz.
- Orthogonal decomposition includes existence, orthogonality, and uniqueness.
- Misconception and physical-interpretation boxes compile and render correctly.

## Commit 11 verification
- Historical notes on Euclid, Descartes, Newton, Gibbs, and Hilbert are integrated.
- Each note is paired with a later-physics connection.
- The vector-space-to-Hilbert-space bridge is explicit and visually supported.

## Remaining non-blocking build behavior
- The repository's existing glossary/index workflow reports missing generated glossary files during compilation; this predates these commits and does not prevent PDF generation.
- One pre-existing overfull box warning remains outside the newly added Chapter 1 material.
