# Volume VI visual-spacing audit — pass 1

The reported screenshot was identified as:

`books/vol06_algebraic_geometry/chapters/ch34_graded_rings/figures/figure_06.tex`

The collision was caused by a 14 mm inter-node gap combined with text labels centered on the
arrows.  The first repair raises the gap to 25 mm and adds explicit edge-label clearance.

This pass deliberately avoids global automatic changes such as increasing every `node distance`,
because several diagrams use vertical, diagonal, or compact geometry where a global value would
damage page flow.

Recommended subsequent visual audit:

1. Render all Volume VI TikZ figures at normal book width.
2. Flag node/edge text intersections and figures whose bounding boxes approach the text margins.
3. Repair horizontal pipelines first, especially diagrams using `right=of` plus labelled edges.
4. Then inspect multi-row diagrams, captions, theorem boxes, and long display equations.
5. Rebuild both reader and full-solutions editions and inspect pages around each repaired figure.

The exact VI/34 Figure 6 repair is included in the VI/23 refinement package.
