# VI/25 — Fibers and Geometric Fibers: detailed full-solutions audit

## Scope

This refinement continues the VI/24 proof-depth standard.  It upgrades the existing VI/25 solution layer without changing the chapter's corpus ownership or consuming VI/26 finite-type/Noetherian material.

## Live-source audit

- Canonical chapter path: `books/vol06_algebraic_geometry/chapters/ch25_fibers_geometric_fibers/chapter.tex`.
- 26 exercises are present.
- The previous `exercise_solutions.tex` contained 26 compact answer-key paragraphs, typically one sentence each (about 2.5 KB total).
- 20 problem dossiers are present.
- P1 is the explicit legacy anchor DG4-P12, the family
  `y(y-zx-1)=0`, whose fibers change from intersecting to parallel lines.
- P2–P20 are canonical VI/25 fiber/geometric-fiber developments.
- Five challenge statements are present and had no full challenge-solution layer.
- The reader chapter printed exercise hints and exercise solutions unconditionally before this refinement.

## Refinement performed

1. Replaced all 26 answer-key entries by detailed proof-oriented solutions.  The VI/24 standard is retained: identify the fiber ring or universal property, justify each isomorphism, and explain the geometric meaning.
2. Expanded all 20 problem dossiers.  Each now has a `FullProblemDossiers` guard, guided hints, a developed solution, mathematical summary, extensions, and provenance.
3. Preserved DG4-P12 as VI/25 legacy ownership.
4. Added five full challenge solutions.
5. Normalized VI/25 to the Volume VI reader/full-solutions switches:
   - `IncludeExerciseHints`
   - `IncludeExerciseSolutions`
   - `FullProblemDossiers`
   - `IncludeChallengeSolutions`
6. Kept the boundary with VI/26 explicit: VI/25 studies ordinary/geometric fibers; VI/26 develops finite-type and Noetherian morphisms.

## Mathematical emphasis

The expanded layer now develops, rather than merely states:

- the affine fiber formula `B \otimes_A kappa(p)`;
- the two-step description as quotient by `p` followed by localization;
- empty, reduced, reducible, irreducible, and nonreduced fibers;
- arithmetic generic/special fibers over `Spec Z`;
- ramified/split/inert fibers of `Z[i]`;
- factorization of a monic polynomial modulo `p` as a complete finite-fiber classifier;
- geometric fibers as residue-field extensions of ordinary fibers;
- ordinary irreducibility versus geometric irreducibility;
- separable splitting versus purely inseparable nilpotent thickening;
- fibers after base change and fibers of products;
- fibers of open and closed immersions;
- the distinction among set-theoretic inverse images, ordinary scheme fibers, and geometric fibers.

## Challenge layer

The five complete challenge solutions include:

1. a full reducedness/component/incidence audit of DG4-P12;
2. a worked classifier for `T^3-2` modulo `2,3,5,7,31`, including residue degrees and repeated factors;
3. a separable-splitting versus inseparable-nilpotence comparison;
4. canonical fiber comparisons through a tower of base changes;
5. explicit construction of a family with two reduced nonzero fibers degenerating to a doubled point, and a modified affine family with empty special fiber.

## Verification philosophy

The verifier does not use arbitrary byte-length thresholds.  It checks exact counts and explicit refinement markers for all 26 detailed exercise solutions, all 20 full dossiers, and all five challenge solutions, plus the standard reader/full-solutions guards and the DG4-P12 legacy marker.

## Standalone LaTeX audit

A two-pass standalone compilation of all 26 detailed exercise solutions, all 20 full problem dossiers, and all five challenge solutions produced 34 pages with:

- 0 overfull boxes;
- 0 underfull boxes;
- 0 undefined references;
- 0 undefined control sequences.
