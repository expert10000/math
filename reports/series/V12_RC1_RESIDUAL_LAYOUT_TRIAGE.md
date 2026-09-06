# v1.2 RC1 residual layout triage

**Status:** PASS

- Residual overfull boxes >=20pt: **3**.
- Largest residual: **187.04073pt**.
- Low-text review pages: **10**, all classified as intentional structural/frontmatter pages.

## Confirmed residuals

- **Volume VI** — 29.45859pt — `books/vol06_algebraic_geometry/chapters/ch41_divisor_class_groups/figures/figure_07.tex` — tighten TikZ node geometry and constrain explanatory node width.
- **Volume VII** — 49.04295pt — `books/vol07_differential_geometry/chapters/ch10_orientation_and_integration/chapter.tex` — reflow the boxed orientation/integration summary onto two aligned rows.
- **Volume VIII** — 187.04073pt — `books/vol08_algebraic_topology/chapters/ch35_lefschetz_theory/chapter.tex` — reflow the canonical arc into two aligned display rows.

No further shared/global typography change is proposed. The repair scope is exactly the three local source constructs above.
