# Imported problem reconciliation — semantic orphan refinement

This pass follows the duplicate/source-solution reconciliation pass and does not change canonical book content.

It adds a semantic layer for solution/hint blocks:

- normalize and hash exact solution text;
- collapse duplicate solution copies without deleting provenance rows;
- resolve ambiguous candidate IDs when they all denote the same exact statement hash;
- inherit trusted links across exact duplicate solution text;
- apply only fully supported high-confidence numbering shifts;
- recompute problem solution availability;
- produce one human-review row per remaining semantic orphan unit.

Generated artifacts:

- `SOLUTION_SEMANTIC_UNITS.tsv`
- `NUMBERING_SHIFT_APPLICATION.tsv`
- `ORPHAN_SEMANTIC_UNITS.tsv`
- refreshed `REMAINING_ORPHANS.tsv`
- refreshed `remaining_orphans.md`
- `RECONCILIATION_REFINEMENT_SUMMARY.md`

No unresolved block is silently dropped or guessed.
