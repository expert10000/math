# Volumes IV-VII final regression gate

Source HEAD before gate commit: `8119916f7e91354ab79e304424860e46c1796f91`

Overall status: **PASS**

| Volume | Status | Chapters | Overfull | Underfull | Undefined | Duplicate labels | Missing inputs | Missing assets | Pages |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| IV | PASS | 31/31 | 0 | 0 | 0 | 0 | 0 | 0 | 327 |
| V | PASS | 28/28 | 0 | 0 | 0 | 0 | 0 | 0 | 276 |
| VI | PASS | 49/49 | 6 | 20 | 0 | 0 | 0 | 0 | 800 |
| VII | PASS | 42/42 | 0 | 7 | 0 | 0 | 0 | 0 | 496 |

Gate checks:

- clean two-pass PDF build for each volume
- expected chapter include count
- all TeX inputs resolve
- zero duplicate labels
- zero undefined references/citations
- asset references resolve
- balanced problem/exercise/hint/solution environments; main-book hint/solution coverage where that volume uses the convention
- obsolete reconstruction-marker gate
- TOC and PDF artifacts produced
- layout-warning thresholds: IV 0/0, V 0/0, VI 6/20, VII 0/7 (overfull/underfull)

