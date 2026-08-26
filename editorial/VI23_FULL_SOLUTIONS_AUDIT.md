# VI/23 — Fiber Products — Full-Solutions Audit

## Scope

This refinement audits the live Volume VI chapter

`books/vol06_algebraic_geometry/chapters/ch23_fiber_products/chapter.tex`

and its exercise, problem, and challenge solution layers.  It also carries one surgical visual-spacing repair for the exact diagram reported during the audit:

`books/vol06_algebraic_geometry/chapters/ch34_graded_rings/figures/figure_06.tex`.

## Live-state findings

The live VI/23 chapter had the same reader/full-solutions inconsistency previously found in VI/21–VI/22:

- exercise hints were printed unconditionally;
- exercise solutions were printed unconditionally;
- all 20 problem files embedded short `Solution.` paragraphs directly in the reader edition;
- all 5 challenge statements had no full solution layer;
- the full-solutions wrapper already defines `IncludeExerciseHints`, `IncludeExerciseSolutions`,
  `FullProblemDossiers`, and `IncludeChallengeSolutions`, so VI/23 only needed to respect those switches.

The existing exercise solution file contained 26 concise answer-key paragraphs.  They were useful
answers, but not full textbook proofs.

## Mathematical refinement

The refinement now provides:

- 26/26 expanded exercise solutions;
- 20/20 expanded problem dossiers;
- 5/5 complete challenge solutions;
- conditional reader/full-solutions integration.

The central theorem is developed at full universal-property depth:

\[
\operatorname{Spec}B\times_{\operatorname{Spec}A}\operatorname{Spec}C
\cong
\operatorname{Spec}(B\otimes_A C).
\]

The proof is given for arbitrary test schemes, not only affine test schemes, by combining the
VI/19 universal property of affine targets with the tensor-product universal property.

The refined dossiers also give full proofs of:

- uniqueness of fiber products;
- symmetry, associativity, and identity;
- the AG7 diagonal-change Cartesian square;
- the graph-as-pullback-of-diagonal square;
- scheme-theoretic intersections as fiber products;
- principal-open and closed-subscheme pullback computations;
- affine diagonal and graph ring maps;
- equalizers as pullbacks of diagonals;
- existence for arbitrary schemes by affine gluing;
- localization compatibility on overlaps;
- the residue-field explanation of product points;
- the empty-product criterion;
- the functor-of-points formula;
- the formal definition of a fiber over a point without consuming the VI/25 corpus.

## Challenge layer

The five challenge solutions include:

1. a complete local-to-global construction of arbitrary scheme fiber products;
2. classification of product points over a fixed compatible pair via
   \(\operatorname{Spec}(\kappa(x)\otimes_{\kappa(s)}\kappa(y))\);
3. scheme-theoretic equalizers and the affine quotient
   \(B/(\alpha(a)-\beta(a))\);
4. reduced-input examples whose fiber product is reducible, nonreduced, or empty;
5. coordinate-free derivations of the principal formal identities.

## Corpus boundary

VI/23 does not consume the detailed fiber corpus reserved for VI/25 and does not claim the
CA13-E6/E7 base-change exercises reserved for VI/24.

## Reader/full-solutions architecture

The ordinary reader build now prints the exercise statements, problem statements/provenance, and
challenge statements without full solution bodies.

The full-solutions wrapper activates:

- `\IncludeExerciseHints`
- `\IncludeExerciseSolutions`
- `\FullProblemDossiers`
- `\IncludeChallengeSolutions`

and therefore reveals the complete VI/23 solution layer.

## Visual-spacing repair

The reported collision was traced exactly to VI/34 Figure 6.  Its original horizontal pipeline used

`node distance=14mm`

while placing the labels `invert x_i` and `degree zero` above those short arrows.  The labels
therefore intruded into adjacent node boxes.

The repaired figure uses:

- `node distance=25mm`;
- explicit inner node padding;
- `above=2pt` edge-label clearance;
- `\small` edge labels.

A standalone render of the repaired figure was inspected and has clear separation between both
labels and all three boxes.

This is intentionally a surgical fix, not a blind global TikZ-spacing rewrite.  A wider visual
audit should patch additional figures only after inspecting their rendered geometry.
