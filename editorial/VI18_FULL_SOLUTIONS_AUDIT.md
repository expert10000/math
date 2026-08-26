# VI/18 — Affine Schemes Full-Solutions Audit

This refinement applies the Volume VI full-solutions standard to VI/18 without changing the chapter's mathematical ownership or legacy provenance.

## Live-source inventory

- 26 exercises.
- 26 exercise answers existed, but most were short answer-key paragraphs.
- 20 problem dossiers.
- VI.18.P1 (legacy AG3 Problem 11) already contains a full topology + sheaf + stalk proof and is preserved.
- VI.18.P2 (legacy AG6 Problem 6.4, affineness subproblem) already contains a complete two-chart proof and is preserved.
- VI.18.P3--P20 are expanded to fuller textbook proofs.
- 5 challenge statements existed with no challenge solution layer.

## Refinement performed

1. Expanded all 26 exercise solutions into explanatory derivations.
2. Preserved P1 and P2 as already full.
3. Expanded P3--P20, emphasizing explicit maps, localization arguments, basis/sheaf comparisons, and global reconstruction.
4. Added five complete challenge solutions.
5. Added a conditional `Challenge solutions` section controlled by `\\IncludeChallengeSolutions`.
6. If `book_full_solutions.tex` exists but does not yet define that flag, the apply script inserts it.

## Guardrails

- No new legacy Problem ownership is claimed.
- AG3 Problem 11 remains exactly VI.18.P1.
- AG6 Problem 6.4's affineness subproblem remains exactly VI.18.P2.
- Morphism anti-equivalence remains reserved for VI/19.
- Scheme gluing remains reserved for VI/20.
- General schemes remain reserved for VI/21.
- Closed subschemes remain reserved for VI/22.

## Verification target

The full-solutions edition should expose:

- 26 expanded exercise solutions,
- 20 problem-dossier solutions,
- 5 challenge solutions.
