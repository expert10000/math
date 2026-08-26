# VI/21 — Schemes and Their Points: Full-Solutions Audit

## Scope

This refinement preserves the canonical VI/21 mathematical scope and upgrades the solution layer only.  It does not consume VI/22 open/closed subschemes, VI/23 fiber products, or VI/24 base change.

## Corpus ownership

- **VI.21.P1** is the unique canonical migration of **AG3 Problem 13**: `Spec Z` is final and every scheme has its unique absolute structure morphism.
- P2–P20 are canonical derivatives/applications of VI/19–VI/21 and claim no additional numbered legacy migration.

## Audit findings before refinement

- 26 exercises existed, but their solutions were short answer-key paragraphs.
- 20 problem files existed, with compact inline solutions and no `FullProblemDossiers` reader/full-solution separation.
- P1 was mathematically correct but too compressed for a full-solutions edition: it did not explicitly develop the affine restriction, point formula, residue-characteristic interpretation, and naturality in one proof.
- 5 challenges existed with statements only.
- The chapter unconditionally printed exercise hints and exercise solutions in the ordinary reader build.

## Refinement implemented

- Expanded **26/26 exercise solutions** into explicit proof/calculation blocks.
- Expanded **20/20 problem dossiers**, including a full AG3 Problem 13 proof.
- Added **5/5 challenge solutions**.
- Wrapped problem-dossier solution material in `FullProblemDossiers`.
- Made exercise hints conditional on `IncludeExerciseHints`.
- Made exercise solutions conditional on `IncludeExerciseSolutions`.
- Made challenge solutions conditional on `IncludeChallengeSolutions`.

## Mathematical guardrails

- The absolute structure morphism is obtained from VI/19's universal property for an arbitrary locally ringed source, not merely by asserting the affine case.
- For a point `x`, the formula is `pi_X(x)=ker(Z -> kappa(x))`.
- Pointwise characteristic `p` does **not** by itself imply factorization through `Spec F_p`; `Spec(Z/p^2 Z)` is retained as the counterexample.
- Field-valued points retain the residue-field embedding as part of the data.
- The image of `Spec O_{X,x} -> X` is the set of generalizations of `x`.

## Expected production counts

- Exercises: 26
- Exercise solution environments: 26
- Problem dossiers: 20
- Full problem solution environments: 20
- Challenges: 5
- Challenge solution environments: 5

## Integration

The normal reader edition shows problem statements, exercises, and challenges without the full solution layer.  The existing `book_full_solutions.tex` switch set enables hints, exercise solutions, full problem dossiers, and challenge solutions.
