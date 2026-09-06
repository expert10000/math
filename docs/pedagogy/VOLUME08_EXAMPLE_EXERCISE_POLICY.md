# Volume VIII example/exercise expansion policy

Volume VIII uses a split pedagogy layer so the reconstructed canonical chapter sources remain protected.
Each enriched chapter receives a sibling `pedagogy_expansion.tex` file containing three substantial
worked examples and sixteen graded exercise/hint/solution triads.  `book.tex` composes the protected
chapter with its pedagogy layer.

The sixteen added exercises are grouped as five standard computations or constructions, four proofs,
three counterexamples or hypothesis tests, two applications or investigations, and two challenges.

Canonical `chapter.tex` files are protected by Git blob SHA-1 recorded at the audit commit.  Validation
queries Git objects with `git rev-parse HEAD:<path>` so Windows CRLF checkout conversion cannot create
false drift.  The working tree is checked separately for staged or unstaged canonical edits.

All expansion files are bracketed by `VOL08-EXPANSION` markers and use globally unique `viiiNN-ped`
labels.  Before a content commit is accepted, the expansion blocks are checked structurally and probed
with `pdflatex`; the full Volume VIII build is run after the third commit.
