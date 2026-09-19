# Final two residual structural audit

This pass targets only the two merged families that remain
`STILL_REVIEW_REQUIRED`:

- RSF-004 — Algebraic Geometry 5
- RSF-008 — Algebraic Topology 5

It ignores all already-valid merged statement segments and inspects only:

- merged segments >=120 lines;
- uncovered parent gaps >=80 lines.

Within those residual regions it detects section/paragraph/bold/item/directive
boundaries and Solution/Answer/Proof terminals, then classifies the remaining
structural defect.

No ledger rows or links are modified.
