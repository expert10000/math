# Imported problem reconciliation pass — exact duplicates and solutions

This pass operates only on `imports/problem_inventory/` and `scripts/imports/`.
It does **not** modify canonical Volume I–VIII chapter content.

## Goals

1. Collapse/identify exact statement duplicate groups without deleting source rows.
2. Reconcile detached solution headings.
3. Resolve orphan solution/hint blocks conservatively.
4. Detect companion-file numbering mismatches.
5. Recompute `has_solution`, `solution_id`, and hint availability in `PROBLEM_LEDGER.tsv`.
6. Emit an explicit remaining-orphans ledger for every unresolved item.

## Important provenance rule

The first run freezes:

- `PROBLEM_LEDGER_STRUCTURAL_BASELINE.tsv`
- `PROBLEM_SOLUTION_LINKS_STRUCTURAL_BASELINE.tsv`

Subsequent reruns use those structural snapshots, so the reconciliation is idempotent.
Use `--refresh-baseline` only after intentionally rerunning structural discovery against a changed import corpus.

## Duplicate policy

Exact duplicates are **semantically collapsed**, never physically deleted. Each source row remains in
`PROBLEM_LEDGER.tsv`, with:

- `representative_problem_id`
- `duplicate_role`
- `duplicate_group`

`SEMANTIC_PROBLEM_UNITS.tsv` contains one row per unique statement hash and is the preferred input for the later subject/Volume/chapter classification pass.

## Solution policy

Automatic relinking is intentionally strict. Existing same-file structural links are retained. New companion links are applied only when number/file-family/content evidence is unique and strong. If the ambiguity consists only of exact-statement duplicates, a provenance row may be chosen safely because solution availability is propagated across the exact duplicate group.

Numbering-shift patterns are **reported but not auto-applied**. The detector excludes self-pairs and byte-identical source copies, because those belong to duplicate-source reconciliation rather than companion numbering review. Exact-copy paths for the same detected mismatch are collapsed into one semantic mismatch row while all equivalent paths remain recorded for provenance.

## Outputs

- `EXACT_DUPLICATE_COLLAPSE.tsv`
- `SEMANTIC_PROBLEM_UNITS.tsv`
- `SOLUTION_RECONCILIATION.tsv`
- `DETACHED_SOLUTION_RECONCILIATION.tsv`
- `NUMBERING_MISMATCHES.tsv`
- `REMAINING_ORPHANS.tsv`
- `remaining_orphans.md`
- `RECONCILIATION_SUMMARY.md`

The pass also enriches/recomputes:

- `PROBLEM_LEDGER.tsv`
- `PROBLEM_SOLUTION_LINKS.tsv`
- `DUPLICATE_GROUPS.tsv`
