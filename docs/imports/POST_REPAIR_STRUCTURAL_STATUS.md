# Post-repair structural status audit

This review-only pass should be run after the final-two mixed-container repair
is applied.

It recomputes structural risk from the current authoritative master ledger,
rather than relying on the historical v3 SAFE/REVIEW/INSUFFICIENT tables.

It reports:

- active rows >=120 / >=250 / >=500 lines;
- rows still containing multiple explicit problem/exercise/example headings;
- unique source-equivalent risk families;
- dangling problem/solution links;
- active orphan semantic units.

No master file is modified.
