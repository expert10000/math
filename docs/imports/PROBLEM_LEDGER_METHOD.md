# Imported dossier/problem ledger — structural discovery pass

This pass inventories problem-like mathematical material under:

```text
imports/ALL_TEX_AND_FIGURES/tex/
```

That is the consolidated copy of the three mathematics import collections:

- `Downloads`
- `MATH-ALLS-2`
- `MATH_ALLS-3`

The pass deliberately does **not** modify any canonical Volume I–VIII chapter.

## Discovery coverage

The scanner recognizes:

- `problem`, `exercise`, `example`, `question`, `task`, and `challenge` environments;
- plain headings such as `Problem 4.` and `Exercise 7.`;
- section/subsection headings that themselves identify a numbered problem;
- `\item` blocks inside sections titled Problems / Exercises / Problem Sets / Dossiers / Challenges;
- theorem/proposition/lemma/corollary blocks inside a problem/exercise section as **LOW-confidence proof-exercise candidates**;
- solution/answer/hint environments and plain `Solution.` / `Hint.` blocks;
- figure references (`\includegraphics`, figure/TikZ inputs, inline TikZ).

## Stable identifiers

Source IDs are deterministic from collection + relative path:

```text
IMP-DL-<path-hash>
IMP-M2-<path-hash>
IMP-M3-<path-hash>
```

Problem IDs append a source-local ordinal:

```text
IMP-DL-1234ABCD90-P001
```

This avoids renumbering unrelated sources when new import files are added.

## Output files

```text
imports/problem_inventory/SOURCE_FILES.tsv
imports/problem_inventory/RAW_PROBLEM_ITEMS.tsv
imports/problem_inventory/REJECTED_STRUCTURAL_ITEMS.tsv
imports/problem_inventory/DETACHED_SOLUTION_ITEMS.tsv
imports/problem_inventory/PROBLEM_LEDGER.tsv
imports/problem_inventory/PROBLEM_SOLUTION_LINKS.tsv
imports/problem_inventory/DUPLICATE_GROUPS.tsv
imports/problem_inventory/INVENTORY_SUMMARY.md
imports/problem_inventory/orphan_solutions.md
imports/problem_inventory/orphan_problems.md
```

`RAW_PROBLEM_ITEMS.tsv` preserves every structural detection with its stable ID. If a detected wrapper/heading normalizes to no mathematical statement, it does not enter the semantic ledger.

A numbered heading such as `\subsection*{Exercise 4.1}` immediately introducing a `solution`/`hint` block is classified as a **detached solution heading** and written to `DETACHED_SOLUTION_ITEMS.tsv`. The actual solution/hint environment is written to `PROBLEM_SOLUTION_LINKS.tsv`, with its source number recovered from that heading when possible. Only genuine empty/non-problem structural markers are placed in `REJECTED_STRUCTURAL_ITEMS.tsv`.

`PROBLEM_LEDGER.tsv` is the master working ledger of statement-bearing problems. The discovery pass leaves semantic and canonical fields explicit rather than blank where possible:

```text
primary_subject       = UNCLASSIFIED
target_volume         = UNCLASSIFIED
target_chapter        = UNCLASSIFIED
canonical_match_type  = UNREVIEWED
mapping_confidence    = UNREVIEWED
migration_status      = UNREVIEWED
review_status         = NEEDS_EDITORIAL_REVIEW
```

This is intentional: discovery and provenance come first; canonical placement and migration come later.

## Exact duplicate handling

The scanner normalizes each statement, removes detected solution/hint material, computes SHA-256, and creates `DUPLICATE_GROUPS.tsv` for exact statement fingerprints that occur more than once. It does **not** delete duplicates or infer which source is primary.

## Validation

Run:

```powershell
py -3 scripts\imports\validate_problem_ledger.py --repo C:\Users\janko\Documents\MATH\math
```

The validator checks unique ledger problem IDs, valid source references, valid line ranges, nonblank statement hashes for every semantic-ledger row, nonblank review/migration statuses, and solution-link referential integrity. Empty structural markers are audited separately and therefore cannot satisfy validation by using a synthetic statement hash.

## Next pass

After this structural ledger exists, the next work is semantic reconciliation:

1. review LOW-confidence candidates;
2. pair detached solutions and companions, including cross-file numbering matches;
3. classify mathematical subject from statement content;
4. assign target Volume/chapter/section;
5. compare against the canonical problem index;
6. classify exact/near duplicates and variants;
7. assign explicit final dispositions before migration.
