# Volume VIII - One-to-One Corpus Reconciliation

**Status:** PASS

- Relevant migration/provenance ledger rows: **182**
- Primary algebraic-topology source files inspected: **17**
- Structured/visual source instances enumerated: **221**
- Direct legacy Problem/Exercise instances: **0**
- Explicit duplicate source instances: **0**
- Canonical Problem/Exercise additions not derived from legacy instances: **1582**
- Source visual instances: **162**
- Canonical visual mappings: **11**
- Explicit provenance-only visual dispositions: **151**
- Archive/variant provenance rows: **2**
- Fallback-assigned instances directly reconciled: **39**
- Unresolved findings: **0**

## Enforcement

- Every legacy `problem` instance is mapped to one canonical `Problem` target.
- Every canonical Problem/Exercise target used by reconciliation is checked for a paired `Solution`.
- Canonical Problems/Exercises not backed by a legacy instance are explicitly classified as canonical additions.
- Duplicate/variant legacy files are kept as provenance dispositions, never silently counted as new mathematics.
- FILE_FALLBACK rules are not accepted as topic coverage; actual structured instances are enumerated and given direct evidence.
- Legacy/support visuals receive either a unique canonical visual target or an explicit provenance-only visual disposition.
- A content/ledger/visual SHA-256 manifest makes later drift invalidate freeze readiness.

## Blocking unresolved findings

None.
