# Final long-child reconciliation

This pass is intended to close the structural review phase.

It performs two conservative operations:

1. clear any currently flagged ledger rows that already have an earlier
   approved safe-closure decision;
2. for `LCR-002` and `LCR-005`, trim the current object immediately before the
   post-solution `Theory for Problems ...` section.

A trim is accepted only if the normalized problem statement hash is exactly the
same before and after trimming.

No problem IDs, stored statement hashes, semantic units, or problem/solution
links are changed.

Successful validation requires zero remaining `LONG_CHILD_REVIEW` rows.
