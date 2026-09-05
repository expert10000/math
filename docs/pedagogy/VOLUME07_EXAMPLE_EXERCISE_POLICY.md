# Volume VII example/exercise expansion policy

Volume VII uses a **split pedagogy layer**. The canonical chapter files are protected byte-for-byte:
new worked examples and graded exercises live in separate `pedagogy_expansion.tex` files and are
composed into the book immediately after the corresponding protected chapter.

Each enriched chapter receives:
- three substantial worked examples;
- sixteen exercise/hint/solution triads;
- five standard computations or constructions;
- four proofs;
- three counterexamples or hypothesis tests;
- two applications or investigations;
- two challenge problems.

The additions are geometry-first. Coordinate calculations must be tied back to an invariant
statement, and abstract constructions should be anchored by explicit manifolds, bundles, forms,
curves, surfaces, metrics, or discrete models.

The protected chapter blob IDs are recorded in
`reports/series/VOLUME07_EXAMPLE_EXERCISE_BASELINE.json`. The audit script recomputes the Git blob
SHA-1 of every canonical chapter file and rejects any drift. This is stronger than marker stripping:
the expansion commits never rewrite the protected chapter sources at all.

Expansion files use `VOL07-EXPANSION` markers and unique `ex:viiNN-ped-*` /
`exr:viiNN-ped-*` labels. `book.tex` includes a pedagogy file only after that chapter's content
commit has landed.

Planned stages:
1. capture the 42-chapter protected baseline and audit contract;
2. enrich VII/01--VII/11;
3. enrich VII/12--VII/19;
4. enrich VII/20--VII/30;
5. enrich VII/31--VII/42;
6. audit placement and graded-exercise balance;
7. reconcile final pedagogy evidence.
