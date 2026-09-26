# Companion Part II migration — Volume II problem corpus

This pass materializes the Volume II semantic atlas rows as reader-facing Companion problems.
Source provenance, classification confidence, and alternate solution variants remain in the
migration ledger rather than the mathematical prose.

## Coverage

- Part II atlas units: **570**
- Reader-facing problems migrated: **570**
- Reader-facing solutions: **570**
- Reader-facing problems without a solution: **0**
- Editorial holds with no safely recoverable statement: **0**
- Source-backed migrated solutions: **165**
- Canonical authored solutions: **405**
- Migration-ledger rows with source-backed solution provenance: **165**
- Problems with multiple distinct source solution variants retained in provenance: **19**
- Atlas placement-review rows included in Part II: **312**

The migration ledger remains the provenance record for the **165** source-backed solutions.
The later reader-facing completion pass authored **405** canonical solutions for problems
whose migration rows did not contain a reconciled primary source solution. These authored
solutions do not rewrite the original source-provenance fields.

## Reader-facing thematic sections

- Metric and Topological Foundations (II/01--II/07): **132** problems
- Calculus (II/08--II/10): **51** problems
- Sequences of Functions (II/11--II/15): **338** problems
- Fixed Points and Differential Equations (II/16--II/19): **23** problems
- Approximation (II/20--II/25): **26** problems

## Reconciliation gates

The Part II validator now requires:

- exactly **570** canonical `Problem` environments;
- exactly **570** `solution` environments;
- exactly one paired solution after every Part II problem and before the next problem;
- exact migration-ledger / reader-facing ID and label coverage;
- exactly **165** source-backed migrated solutions in provenance;
- exactly **405** canonical authored reader-facing solutions;
- **0** editorial holds;
- the corrected CP-II-0494 unbounded-operator analysis.

## Visual layer

No new plots or diagrams are introduced by the solution-completion reconciliation.
Existing/source visual requirements remain recorded in `COMPANION_PROBLEM_ATLAS.tsv` and
`PART_II_MIGRATION.tsv` for a later visual-enrichment pass.

## Integrity rule

Every Part II atlas unit has exactly one migration-ledger row and therefore one explicit
disposition. Every one of the **570** reader-facing Part II problems has exactly one paired
reader-facing solution. Source provenance remains distinct from canonical authored solution
completion.
