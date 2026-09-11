# Volume II provenance notes — editorial only

This ledger is an editorial sidecar for **Volume II — Real Analysis and Topological Foundations**. It keeps source history, rights review, and transformation notes out of reader-facing mathematical prose while preserving a traceable audit path.

Reader-facing chapters should describe mathematical purpose, proof strategy, hypotheses, examples, and exercises directly. Terms such as *corpus mapping*, *legacy migration*, *retained source block*, *reconstruction*, or *canonical completion* belong in editorial records rather than in the book text.

## Per-block record schema

Use the following fields whenever a block needs an explicit provenance record.

| field | meaning |
|---|---|
| `chapter` | canonical Volume II chapter code, e.g. `II/17` |
| `block-id` | stable theorem/example/problem/exercise or editorial block identifier |
| `origin` | actual retained source, source family, or `fresh` when independently authored |
| `license/permission` | recorded permission or license evidence; never infer missing rights data |
| `transformation` | concise description of adaptation, rewrite, synthesis, or fresh construction |
| `reviewer` | person or review process that checked the transformed block |

## Existing detailed records

The detailed migration-era records remain the authoritative evidence for blocks that came through the earlier source-reconciliation process:

- `books/vol02_real_analysis/reconstruction/VOLUME02_I01_I07_DOSSIER_PROVENANCE.tsv`
- `books/vol02_real_analysis/reconstruction/VOLUME02_I08_I12_DOSSIER_PROVENANCE.tsv`
- `books/vol02_real_analysis/reconstruction/VOLUME02_I13_I25_DOSSIER_PROVENANCE.tsv`
- `books/vol02_real_analysis/reconstruction/VOLUME02_SOURCE_INVENTORY.tsv`
- `books/vol02_real_analysis/reconstruction/VOLUME02_SOURCE_RULE_RECONCILIATION.tsv`
- `editorial/SOURCE_MIGRATION.tsv`

Those files are editorial records, not reader-facing content. This sidecar does not duplicate or invent source/license facts; it defines the public/editorial separation and points reviewers to the records where those facts are maintained.

## Reader-facing policy

1. Solved dossiers are presented as mathematical problems, not as migration artifacts.
2. Supplementary exercises are described by mathematical role and level of synthesis, not by whether they were preserved or reconstructed.
3. A source-light chapter may be independently authored, but the public chapter should explain its mathematical role rather than its editorial origin.
4. Proof provenance is a separate issue from source provenance: if a theorem is used with only a sketch or without a full proof, the public text should state that proof status explicitly.
5. Any rights uncertainty stays in the editorial ledgers until resolved; it is not converted into a reader-facing qualification.
