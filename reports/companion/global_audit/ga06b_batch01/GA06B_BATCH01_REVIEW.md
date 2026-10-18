# GA-06b Batch 01 — Mathematical first-pass audit (VI/01–VI/06)

- Reviewed against Git commit: `410a7ff3edf4d46d74eee85634c286d59319389a`
- Executed against local HEAD: `410a7ff3edf4d46d74eee85634c286d59319389a`
- Part VI chapter SHA-256: `8603a3f43609448bfaabdc2eb8f6d7ce8e6ba2413c92840b01cc7de2af7d03dd`
- Part V frozen chapter SHA-256: `09bf70c6290e478e00689af1e6f83f9281e13cffacdfd19837dc35b19f1d57ce`
- Status: **TWO TARGETED CORRECTIONS APPLIED; NOT COMMITTED**
- 12 first-pass reviews; 10 without material first-pass findings; 2 P1 mathematical issues.
- No mathematical proof is formally certified. Provenance and PDF certification are separate gates.

| Canonical ID | Chapter | Finding |
|---|---|---|
| CP-VI-0050 | VI/01 | FIRST_PASS_NO_BLOCKING_FINDING |
| CP-VI-0051 | VI/01 | FIRST_PASS_NO_BLOCKING_FINDING |
| CP-VI-0052 | VI/02 | FIRST_PASS_NO_BLOCKING_FINDING |
| CP-VI-0053 | VI/02 | FIRST_PASS_NO_BLOCKING_FINDING |
| CP-VI-0054 | VI/03 | FIELD_HYPOTHESIS |
| CP-VI-0055 | VI/03 | PROOF_GAP_IDEAL_EQUALITY |
| CP-VI-0056 | VI/04 | FIRST_PASS_NO_BLOCKING_FINDING |
| CP-VI-0057 | VI/04 | FIRST_PASS_NO_BLOCKING_FINDING |
| CP-VI-0014 | VI/05 | FIRST_PASS_NO_BLOCKING_FINDING |
| CP-VI-0058 | VI/05 | FIRST_PASS_NO_BLOCKING_FINDING |
| CP-VI-0059 | VI/06 | FIRST_PASS_NO_BLOCKING_FINDING |
| CP-VI-0060 | VI/06 | FIRST_PASS_NO_BLOCKING_FINDING |

## CP-VI-0054 — field hypothesis (P1)
Under the definition $k[X]=k[x,y]/I(X)$ for $k$-rational points, the equation $y=x^3$ has an additional vanishing polynomial $x^q-x$ over a finite field $k=\mathbb F_q$. The existing proof silently uses an infinite field. Add the infinite-field hypothesis and prove $I(X)=(y-x^3)$ by polynomial division and the infinitely-many-roots argument.

## CP-VI-0055 — ideal equality (P1)
The fact that $I(X)+I(Y)$ has zero locus $X\times Y$ is insufficient by itself to establish equality with $I(X\times Y)$. The proposed proof works over any field by writing $H$ modulo $I(Y)$ with linearly independent coefficient functions and evaluating at points of $X$.

## Structural/provenance gates kept open
- `CP-VI-0047` original/supplementary identity needs an explicit content decision (outside Batch 01).
- 25 GA-06a3 solution-format cases remain under review (outside Batch 01).
- Explicit source-to-canonical IMP links remain unreconciled; do not infer links.

## Subsequent work
Run the existing Part VI validation and a full PDF build/visual review independently after applying; review VI/07 onward in Batch 02. Do not freeze GA-06 from this report.
