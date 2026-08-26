# VI/22 Full-Solutions Audit — Open and Closed Subschemes

## Scope

Canonical live path audited:

`books/vol06_algebraic_geometry/chapters/ch22_open_closed_subschemes/chapter.tex`

This is a refinement pass, not a corpus remigration.  The chapter already owns the open/closed
subscheme material.  No numbered legacy problem is claimed by the 20 current dossiers; their
provenance consistently identifies them as canonical VI/22 developments from the AG5 T02 theory
scope.

## Pre-refinement findings

The live chapter had the same reader/full-solutions integration problem previously corrected in
VI/21:

- exercise hints were included unconditionally;
- exercise solutions were included unconditionally;
- all 20 problem files printed their short solution immediately in the reader edition;
- five challenge files contained only short `Solution sketch` paragraphs;
- no separate challenge-solution layer existed.

The exercise solution file contained 26 answers, but most were one sentence.  The 20 problem
solutions were mathematically sound outlines, generally only one short paragraph.  They did not
meet the expanded textbook-solution standard now used in VI/17--VI/21.

## Refinement performed

- expanded all **26/26 exercise solutions** into explicit derivations;
- converted all **20/20 problem files** into conditional full dossiers controlled by
  `\FullProblemDossiers`;
- added guided hints, full proof bodies, interpretation, and extensions to every problem dossier;
- removed the five reader-visible challenge sketches from the challenge statements;
- added **5/5 full challenge solutions** in `challenge_solutions.tex`;
- made exercise hints conditional on `\IncludeExerciseHints`;
- made exercise solutions conditional on `\IncludeExerciseSolutions`;
- made challenge solutions conditional on `\IncludeChallengeSolutions`;
- retained the existing `book_full_solutions.tex` switch architecture.

## Mathematical centers strengthened

The refined solutions explicitly develop:

1. the canonical and unique open-subsheme structure `(U,\mathcal O_X|_U)`;
2. the affine closed immersion
   \[
   \operatorname{Spec}(A/I)\hookrightarrow\operatorname{Spec}A
   \]
   as a homeomorphism onto `V(I)` together with local rings
   \[
   (A/I)_{\mathfrak p/I}\cong A_{\mathfrak p}/IA_{\mathfrak p};
   \]
3. the difference between support and scheme structure, including nilpotent thickenings;
4. compatibility of quotient with localization;
5. gluing of compatible affine closed subschemes;
6. the affine-local surjectivity criterion for closed immersions;
7. the factorization criterion
   \[
   \operatorname{Spec}B\to\operatorname{Spec}A
   \text{ factors through }\operatorname{Spec}(A/I)
   \iff I\subseteq\ker(A\to B);
   \]
8. the reduction `X_red`, its cover-independence, and its universal property;
9. scheme-theoretic intersection via `I+J` and union via `I\cap J`;
10. local algebra of immersions as a quotient of a localization;
11. the strict difference between pointwise vanishing and scheme-theoretic vanishing.

## Editorial correction

The live chapter said that the full theory of quasi-coherent ideal sheaves was deferred to
VI/38.  In the live Volume VI chapter sequence, quasi-coherent `\mathcal O_X`-modules are VI/33;
VI/38 is projective morphisms and closed embeddings.  This refinement corrects that one cross-
reference to VI/33 while retaining the separate VI/38 reference for projective closed embeddings.

## Boundary discipline

This pass does **not** consume:

- VI/23 fiber products;
- VI/24 base change;
- VI/25 fibers and geometric fibers;
- VI/33 general quasi-coherent-module theory beyond the minimal ideal-sheaf language already
  present in VI/22;
- VI/38 projective closed embeddings.

## Verification standard

The verifier checks exact per-solution markers rather than arbitrary total-byte thresholds:

- 26 exercise markers and 26 `solution` environments;
- 20 problem refinement markers, 20 full-dossier guards, and 20 `solution` environments;
- 5 challenge-solution markers and 5 `solution` environments;
- absence of the old `Solution sketch` text from challenge statements;
- reader/full-solutions guards in `chapter.tex`;
- full-solutions wrapper flags;
- presence of this audit.

A standalone LaTeX compilation of the complete refined solution layer is also performed before
release.

## Standalone compile audit

The refined problem/exercise/challenge solution layer compiled in a two-pass `latexmk` audit to **36 pages** with **0 LaTeX/package warnings, 0 overfull boxes, 0 underfull boxes, and 0 undefined references**.
