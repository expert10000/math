# GA-06b Batch 03 — Sheaves and exact sequences (VI/12–VI/17)

- Baseline: `410a7ff3edf4d46d74eee85634c286d59319389a`; observed local HEAD: `410a7ff3edf4d46d74eee85634c286d59319389a`
- Part VI chapter SHA-256: `8603a3f43609448bfaabdc2eb8f6d7ce8e6ba2413c92840b01cc7de2af7d03dd`
- Part V frozen SHA-256: `09bf70c6290e478e00689af1e6f83f9281e13cffacdfd19837dc35b19f1d57ce`
- Source blobs reviewed: **12**; no blocking mathematical first-pass findings in 11; one **P1 proof-exposition gap** in CP-VI-0069.
- CP-VI-0069: **TARGETED CORRECTION APPLIED, NOT COMMITTED**; old source preserved in `CP-VI-0069_before_batch03.tex`.
- CP-VI-0026: **EDITORIAL STRUCTURE REVIEW OPEN**, since a full `\section{Theory}` occurs inside a problem input following the proof, with extensive definitions/theorems. This is not automatically a mathematical error; do not auto-delete inherited material.
- No master import ledger, Part V source, unrelated sources, or Git refs changed.

## P1 — CP-VI-0069: affine structure-sheaf sections

The original solution invokes a 'standard gluing argument' while the exercise specifically asks for a proof of `Γ(D(f), O_X) ≅ A_f`. The replacement supplies a finite basic-open cover and verifies the localization equalizer using common denominators and a unit-ideal partition. The resulting proof also gives `Γ(X, O_X) ≅ A` for `f=1`.

## Open gates

1. Confirm Batch 01 and 02 Git commits separately; the script accepts unchanged baseline blobs for this batch and does not stage changes.
2. Independently resolve 25 solution-style cases and the CP-VI-0047 supplementary filename issue; this mathematical audit is not their adjudication.
3. Check how the nested `\section{Theory}` in CP-VI-0026 affects the PDF hierarchy, and preserve provenance before any relocation.
4. Inspect import-to-canonical source mapping and run Part VI validators and a PDF build/visual review before a freeze.
