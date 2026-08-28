# VI/38 Full-Solutions Audit — Projective Morphisms and Closed Embeddings

## Standard

This refinement continues the VI/24+ detailed-proof standard while preserving the live VI/38 corpus.

The live chapter has:
- **24 canonical exercises**;
- **12 canonical problem dossiers**;
- **5 canonical challenges**.

The refinement keeps exactly those counts. It does **not** add substitute P13+ problems, does not renumber the dossier, and does not claim any new legacy source IDs. Its purpose is to replace terse answer sketches by full scheme-theoretic proofs and to expose challenge solutions only in the full-solutions edition.

## Dossier-first rule

The existing files `problems/problem_01.tex` through `problem_12.tex` are treated as the authoritative VI/38 problem corpus. Their problem titles, labels, and mathematical tasks are preserved; only the solution layer is expanded and placed behind `\ifdefined\FullProblemDossiers`.

The canonical dossier sequence is:

1. **VI.38.P1 — Domain theorem for Proj:** gluing the standard-open maps induced by a degree-preserving graded map.
2. **VI.38.P2 — A map with a base point:** the map `a -> x^2`, `b -> xy`, its maximal Proj domain, and the pointwise formula.
3. **VI.38.P3 — Quotient maps and closed immersion:** a chartwise proof from surjective degree-zero localizations.
4. **VI.38.P4 — Morphism from same-degree forms:** the empty-base-locus criterion and the Veronese regrading mechanism.
5. **VI.38.P5 — Relative projectivity survives base change:** projective embeddings after arbitrary base change.
6. **VI.38.P6 — Quadratic Veronese embedding:** the conic and its principal homogeneous ideal.
7. **VI.38.P7 — General Veronese embedding:** the surjection onto the Veronese subring and the closed immersion.
8. **VI.38.P8 — Proj of a Segre product:** chartwise product identification and gluing.
9. **VI.38.P9 — Segre ideal:** generation of the kernel by the `2 x 2` minors.
10. **VI.38.P10 — Segre quadric:** `P^1 x P^1` as a quadric in `P^3`, with all four product charts.
11. **VI.38.P11 — Composition of projective morphisms:** base change plus relative Segre, with ambient dimension `(m+1)(n+1)-1`.
12. **VI.38.P12 — Very ample twists on projective space:** `nu_d^* O(1) = O(d)` from transition functions.

## Legacy-source provenance

`editorial/CHAPTER_STATUS.tsv` records VI/38 as `LEGACY_SOURCE_IDENTIFIED` with **6** source mappings.

Those six migration selectors are exactly the VI/38 routes in `editorial/SOURCE_MIGRATION.tsv`:

### `theory-of-algebraic-geometry-4.tex`
- `T05.SECTION` — `projective morphism|closed embedding` -> VI/38;
- `T05.EXERCISE_CHILDREN` — problem/exercise/solution descendants of that section -> VI/38;
- `T05.THEORY_CHILDREN` — theorem-like descendants of that section -> VI/38.

### `theory-of-algebraic-geometry-9.tex`
- `T05P.SECTION` — split `projective morphism` overlap -> VI/38;
- `T05P.EXERCISE_CHILDREN` — problem/exercise/solution descendants -> VI/38;
- `T05P.THEORY_CHILDREN` — theorem-like descendants -> VI/38.

The AG9 split is deliberately retained: quasi-coherent/coherent material belongs to VI/33, while the projective-morphism overlap remains in VI/38.

## Proof-depth upgrades

The detailed problem layer now makes explicit:
- the equality of standard-open overlaps and localization-in-stages gluing for Proj maps;
- the irrelevant-ideal obstruction at a base point;
- the kernel `(IS_f)_0` of quotient maps on standard projective charts;
- the same-degree/Veronese regrading behind homogeneous coordinate formulas;
- stability of closed immersions and projective morphisms under arbitrary base change;
- surjectivity onto Veronese subrings and the corresponding closed immersions;
- Segre-product chart rings `A_(x_i) tensor B_(y_j)`;
- the full monomial-swap proof for the determinantal Segre ideal;
- all four affine charts of the Segre quadric;
- the exact relative projective dimension needed in the composition theorem;
- very ampleness of `O(d)` via pullback of `O(1)` under Veronese.

## Exercise layer

All 24 existing exercises are retained. Their former one-line answers are replaced by detailed solutions covering:
- domain/radical criteria;
- regrading;
- quotient and closed-immersion charts;
- projective base change;
- Veronese and Segre coordinate algebra;
- relative Segre;
- composition;
- very ample pullbacks;
- PGL actions;
- rational maps with base loci;
- why injectivity on points is insufficient for closed immersion.

No new exercise IDs are introduced.

## Challenge layer

All five live challenges are retained verbatim and receive complete guarded solutions:

- **C1:** the universal base-locus criterion `S_+ subset sqrt(F_0,...,F_m)`, equivalently a power of the irrelevant ideal lies in the coordinate ideal;
- **C2:** the rational normal curve ideal from `2 x 2` catalecticant minors, with a straightening proof;
- **C3:** the Segre-Veronese embedding and the very ample bundle `O(a,b)`;
- **C4:** projective graph embeddings via separatedness and the diagonal, followed by Segre;
- **C5:** saturated homogeneous ideals and projective ideal sheaves, with an explicit boundary separating the chartwise result available now from later coherent-sheaf/Serre theory.

## Edition discipline

The package changes the VI/38 chapter integration so:
- hints appear only when `\IncludeExerciseHints` is defined;
- exercise solutions appear only when `\IncludeExerciseSolutions` is defined;
- challenge solutions appear only when `\IncludeChallengeSolutions` is defined;
- dossier solutions remain guarded by `\FullProblemDossiers`.

`book_full_solutions.tex` already defines all four switches, so no wrapper change is needed.

## Boundary discipline

VI/38 is allowed to use twists such as `O(d)` only to express the Veronese/very-ampleness interface already present in the live dossier. It does not import the general Picard-group machinery of VI/42 or the later cohomological ampleness theory.

Challenge C5 explicitly marks this boundary: chartwise saturation and equality of projective ideal sheaves belong here; the general coherent-sheaf/graded-module correspondence, Serre vanishing, eventual global generation, and cohomological ampleness criteria remain later.

## Commit intent

Suggested commit message:

`vol06 VI/38: expand dossier-aligned projective morphism solutions`

The commit is a **corpus-preserving proof-depth refinement**, not a corpus expansion.
