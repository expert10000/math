# Reconciliation tooling and audit-documentation curation

This record separates durable reconciliation machinery from transient working artifacts.

## Keep

Commit tools that reproduce final transformations, finalization, structural/orphan audits, or source-grounded reconciliation. Commit documentation that records final decisions, final structural closures/repairs, durable status, integrity audits, and reconciliation methodology.

## Remove / ignore

Do not version one-off preview generators, candidate refreshers, packet builders, superseded promotion/resegmentation passes, intermediate review narratives, or residual diagnostic packets after their decisions have been captured in canonical ledgers and final documentation.

## Scope boundary

This commit is limited to `docs/imports`, `scripts/imports`, the curation records themselves, and exact-path `.gitignore` entries. It must not stage `reports/series/*` or modify `imports/problem_inventory/*` from the preceding provenance commit.
