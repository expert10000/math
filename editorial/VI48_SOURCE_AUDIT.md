# VI/48 — Exact Sequences and Cohomology Source Audit

Canonical destination:

- `books/vol06_algebraic_geometry/chapters/ch48_exact_sequences_and_cohomology/chapter.tex`

## Live ledger

- chapter code: `VI/48`
- title: `Exact Sequences and Cohomology`
- mapped-rule count: **3**
- initial status: `PLANNED`
- initial next action: `MAP_AND_REWRITE`

## Exact migration ownership

All three mapped rules come from `theory-of-algebraic-geometry-11.tex`:

1. `T03.SECTION` — selector `long exact|cohomology exact` — dedicated exact-sequences/cohomology section.
2. `T03.EXERCISE_CHILDREN` — problem/exercise/solution descendants of that section.
3. `T03.THEORY_CHILDREN` — definition/theorem/lemma/proposition/corollary/remark/warning/example descendants of that section.

The neighboring blocks are intentionally not absorbed:

- `T02` Čech material belongs to VI/47.
- `T04` acyclicity/vanishing/flabby-resolution material belongs to VI/49.
- the file fallback belongs to VI/46.

## Reconstruction scope

The chapter develops:

- left exactness of global sections;
- connecting homomorphisms via local lifts;
- the long exact cohomology sequence;
- naturality and split exact sequences;
- the precise relation to Čech boundaries under cover-lifting/Leray hypotheses;
- effective Cartier divisor exact sequences;
- recursive cohomology of `O(n)` on `P^1`;
- dimension shifting with flabby sheaves;
- Euler-characteristic additivity and obstruction language.

## Deferred to VI/49

Systematic affine/quasi-coherent vanishing, general acyclicity criteria, and the main vanishing theorems remain in VI/49.

## Production audit

- 8 TikZ figures
- 24 exercises, each with hint and solution
- 12 solved problem dossiers
- 5 challenges
- 68 unique labels
- 41 solution environments total
