# Volume IV example/exercise expansion policy

Volume IV additions are concrete, theorem-aware, and placed beside the concept they illuminate.
Each enriched chapter receives exactly three new worked examples and sixteen new graded
exercise/hint/solution triads. Existing theorems, proofs, worked examples, solved dossiers,
exercises, hints, solutions, labels, outcomes, chapter summaries, and source provenance are
preserved byte-for-byte after expansion blocks are stripped.

The sixteen added exercises are grouped as:

- 5 standard computations;
- 4 proofs;
- 3 counterexamples or hypothesis tests;
- 2 applications or investigations;
- 2 challenge problems.

Every addition is bracketed by `VOL04-EXPANSION` markers. The Commit-1 audit snapshots the
protected source SHA-256 for all 31 chapters. Later audits strip only those marked blocks and
require every protected hash to match the Commit-1 baseline exactly.

From Commit 2 onward, generated TeX is checked before any canonical chapter is modified.
The preflight rejects unsafe raw TeX special characters in prose, checks balanced generated
structures, and compiles a temporary probe document. After insertion, the same safety scan is
run against the live expansion blocks, followed by the Volume IV structural audit and a real
one-pass Volume IV compile probe.
