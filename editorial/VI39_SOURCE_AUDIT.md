# VI/39 Source Audit - Weil Divisors

## Canonical migration evidence

The current `editorial/SOURCE_MIGRATION.tsv` assigns **8 rows** to VI/39.

### Primary AG9 mapping (canonical)

- `theory-of-algebraic-geometry-9.tex`, `T01.SECTION`
  - selector: `Weil divisor|prime divisor`
  - destination: `VI/39 Weil Divisors`
  - action: `MIGRATE`
- `T01.EXERCISE_CHILDREN` -> VI/39
- `T01.THEORY_CHILDREN` -> VI/39
- `FALLBACK.ALL_UNMATCHED` -> VI/39 as a safety-net mapping

The explicit T01 selector and its descendants are the primary provenance for the chapter. The AG9 fallback is not treated as permission to absorb later Cartier/class-group/Picard topics; those have higher-precedence explicit destinations VI/40-VI/42.

### AG10 overlap (compare-and-migrate)

`theory-of-algebraic-geometry-10.tex` has four rows routed to VI/39 with action `COMPARE_AND_MIGRATE`:

- `T01.SECTION`, selector `divisor|Picard|line bundle|coherent`
- inherited exercise children
- inherited theorem-like children
- file fallback

The ledger explicitly says this source strongly overlaps AG9 and should be compared rather than treated as an independent chapter. Because its selector mixes Weil, Picard, line-bundle, and coherent-sheaf material, VI/39 retains only material genuinely belonging to the Weil-divisor layer. Cartier divisors, divisor classes, and line bundles remain reserved for VI/40, VI/41, and VI/42.

## Canonical extension in this reconstruction

The accessible ledger provides topic/block provenance but not the raw legacy prose needed for verbatim reconstruction. The new chapter therefore preserves the mapped scope and adds standard canonical developments needed for a self-contained transition from codimension to Cartier theory:

- prime divisors and codimension-one points;
- Weil divisor group, support, effectivity, positive/negative parts;
- normal Noetherian integral schemes and DVRs in codimension one;
- orders of vanishing and principal divisors;
- finite support and multiplicativity;
- computations on affine space, projective space, and normal curves;
- restriction to open subsets;
- nonnormal warning via the cusp;
- normal singular surface example `xy=z^2`;
- degree of divisors on proper normal curves and degree-zero principal divisors;
- only principal-divisor pullback under dominant maps, with an explicit warning that arbitrary Weil divisors do not pull back canonically;
- preview of the Cartier-to-Weil map, deferring the full theory to VI/40.

## Boundary decisions

The following are deliberately not developed here:

- full Cartier divisor theory -> VI/40;
- linear equivalence and divisor class group -> VI/41;
- invertible sheaves and Picard group -> VI/42;
- plane-cubic divisor calculations -> VI/43;
- birational transforms of divisors -> later birational chapters.
