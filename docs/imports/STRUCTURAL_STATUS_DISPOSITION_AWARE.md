# Disposition-aware structural status audit

The older structural-status audit is intentionally heuristic: it flags long
rows and rows containing multiple explicit problem-like headings even when an
editor has already reviewed and accepted them.

This pass separates:

- raw heuristic risk;
- risk already closed by an explicit structural/editorial disposition;
- genuinely actionable residual structural risk.

It does not modify the ledger.
