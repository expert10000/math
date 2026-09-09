# Volume V professional review — V/01–V/28

## Review scope

This pass reconciles exercise, hint, theorem, label, and migration coverage after the mathematical-correction and prerequisite/notation passes.

## Static QA expectations

- exactly 28 canonical chapter directories;
- canonical chapter labels `ch:v01` through `ch:v28`;
- no duplicate LaTeX labels in Volume V;
- no statically detectable unresolved Volume-V references;
- exercise/hint counts reviewed by chapter;
- solution counts checked against problems plus exercises;
- all 28 Volume-V rows present in `editorial/CHAPTER_STATUS.tsv`;
- all 28 canonical Volume-V destinations detectable in `editorial/SOURCE_MIGRATION.tsv`.

## Manual review warnings

Generic diagnostic prose is intentionally reported rather than rewritten automatically. It occurs in mathematically distinct contexts and should not be mass-edited.

## Final release gate

Before any push:

1. run the final static QA;
2. build the full Volume V PDF;
3. inspect the build log for LaTeX errors, undefined references, multiply-defined labels, and meaningful overfull boxes;
4. verify final page count from the actual PDF rather than from an estimate;
5. update freeze/page metadata only from the built artifact if such metadata requires refresh.

No push is performed by this review bundle.
