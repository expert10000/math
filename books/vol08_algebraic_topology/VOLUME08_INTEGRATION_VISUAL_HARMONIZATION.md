# Volume VIII — Integration and Visual Harmonization

## Scope
This commit is the **integration checkpoint**, not the final corpus freeze.

It performs the following after VIII/35 exists:

1. activates VIII/34 and VIII/35 so all 35 canonical chapters are in `book.tex`;
2. normalizes the Volume VIII README to the complete canonical chapter list;
3. records the editable SVG inventory for the entire volume;
4. installs a repeatable structural/cross-reference audit;
5. checks canonical chapter count, include count, duplicate labels,
   chapter-local Problem/Solution balance, and Volume-VIII internal references;
6. records visual metadata coverage without silently rewriting legacy artwork;
7. leaves the full legacy dossier/problem/solution/provenance reconciliation
   explicitly pending.

## Visual grammar
New and harmonized Volume VIII SVG source assets should use:

- `width="1200" height="720" viewBox="0 0 1200 720"`;
- a meaningful `<title>` and `<desc>`;
- black/white vector geometry that remains readable in print;
- mathematical labels large enough to survive book-scale reduction;
- one conceptual message per panel;
- chapter-local ownership under `figures/chNN/`.

The visual inventory is generated from the repository during application, so
it reflects the actual tracked source graphics rather than a hand-maintained
guess.

## Navigation state
The complete Part VI arc is:

- VIII/28 — Cohomology
- VIII/29 — Cup Products
- VIII/30 — Vector Bundles and Clutching
- VIII/31 — Thom Classes
- VIII/32 — Sphere Bundles and Euler Classes
- VIII/33 — Poincaré Duality
- VIII/34 — Intersection Forms
- VIII/35 — Lefschetz Theory

## What remains before freeze
The next operation is the postponed **one-to-one corpus reconciliation**:

- each mapped legacy dossier/problem instance -> canonical `Problem`;
- each canonicalized problem -> paired `Solution`;
- duplicate/variant/provenance items explicitly classified;
- support figures reconciled one-to-one;
- no item accepted merely because its topic appears somewhere in the chapter.

Only after that reconciliation should Volume VIII run the final clean PDF
build, label/reference audit, chapter-status normalization, visual inventory
freeze, and release commit.
