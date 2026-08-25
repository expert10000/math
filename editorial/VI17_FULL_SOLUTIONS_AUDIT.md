# Volume VI — VI/17 Full-Solutions and Integration Refinement

## Purpose

This refinement addresses two production issues found in the rendered Volume VI PDF:

1. the standard `book` TOC number box is too narrow for section numbers such as `17.10` and `33.10`, causing the title to touch the number;
2. VI/17 had complete exercise-answer coverage but not a true full-solutions edition: exercise answers were compressed, problem-dossier solutions were hidden in the reader build, and the five challenges had no solutions.

## Changes

- widen the shared section/subsection TOC number boxes;
- normalize Volume VI to exactly one Part IX block and canonical chapter paths;
- add `book_full_solutions.tex` as an explicit full-solutions build mode;
- add `BUILD_FULL_SOLUTIONS_WINDOWS.ps1`;
- expand all 26 VI/17 exercise solutions;
- replace the solution body in each of the 21 VI/17 problem dossiers with a fuller proof while preserving statements, hints, interpretation, extensions, and provenance;
- add full solutions to all 5 VI/17 challenges;
- make challenge solutions conditional on `\IncludeChallengeSolutions` so the reader edition remains concise.

## Edition behavior

`book.tex` remains the reader edition.

`book_full_solutions.tex` defines:

- `\IncludeExerciseHints`
- `\IncludeExerciseSolutions`
- `\FullProblemDossiers`
- `\IncludeChallengeSolutions`

before loading `book.tex`.

## Mathematical quality standard

The expanded solutions explicitly expose nontrivial steps such as localization equality/zero criteria, basis reconstruction, finite gluing, stalk colimits, UFD intersection arguments, nilpotent thickening kernels, and the idempotent/clopen correspondence.  Simple computations remain proportionate rather than artificially verbose.
