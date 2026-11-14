# GA-09 Batch 37 - Technical closure of five verified findings

14 November 2026. AI technical review closure.

Source checkpoint: `fbdbd7bc3ab4da9a0f4c246f7c2eb7ba9a89dcae`.

Reviewed PDF SHA-256: `c87077bb8811e8b51cbca5ad7353e2b5505956a00992b9eb5d18eb6e24d1ed2e`. Physical pages: **1,591**.

## Closed technical findings

| Finding | Subject | Physical pages | Verified result |
|---|---|---|---|
| B35-M01 | CP-II-0556 | 563, 564 | Retained box now agrees with the solution on uniform convergence and sufficient versus necessary conditions. |
| B35-L01 | VI/16 section | 965, 966, 967 | Section heading, stable identifier and initial solution content share physical page 966. |
| B35-L02 | Figure 7.41 | 1267 | Mercator title is separated from the vertical-axis label. |
| B35-E01 | CP-II-0560 | 565, 566 | Unused caption became an Interpretation paragraph; no empty plot placeholder remains. |
| B35-E02 | CP-II-0098 | 575 | Dangling build instruction and its pgfplots footnote were removed. |

All three patched source hashes matched the expected Batch 36 states. The uploaded fingerprint text agreed with the reviewed PDF. The build had 0 overfull boxes, 5 underfull boxes and the existing amsmath warning. No out-of-page text spans were found by the prior whole-PDF check. These five findings are technically closed for the exact source/PDF pairing above.

This record consolidates the review already performed in this conversation. It does not claim that the PDF was rebuilt from the pushed commit in a new clean environment, or that this closure re-ran rendering. The source hashes in the review evidence match the source states installed in the checkpoint. A source/PDF pairing is not a reproducible-build attestation.

## Qualifications and pending decisions

- All 49 provenance findings remain qualified as recorded in Batch 35. Normalized matches are not byte identity, proof correctness, or a claim of unchanged authorship for added solutions. Editorial acceptance remains pending.
- The 25 flagged rows and 15 historical controlled corrections overlap in five IDs, giving 35 distinct IDs and 40 obligations. The two later Batch 34 sentence corrections are not silently added to the historical 15.
- Proof-content presence and targeted repair review are not an independent certification of every proof. CP-VI-0047 is one main problem with an included theory/examples supplement; its entire supplement is not independently proof-certified.
- The predecessor PDF received all-page overview screening, with closer figure checks. The current PDF received focused verification of the five fixes and neighbouring pages. Do not label this as a full-resolution visual reading of every current page. Final whole-book visual acceptance remains pending.
- Publication approval remains pending. No publication wording or release tag is authorized by this record.

## Historical records and installation

Batch 35's open-findings report and Batch 36's patch-prepared report remain unchanged as historical snapshots. This separate closure supplies the later verified status; their old pending fields are not evidence that the five fixes were never reviewed.

The installer validates the source/report fingerprints and the exact reviewed PDF, checks the checkpoint is an ancestor of the repository HEAD, and creates only GA09_B37_TECHNICAL_CLOSURE.json and this report under reports/companion/global_audit/ga09_b37_closure/. It refuses conflicting existing outputs and is repeat-safe. It does not edit TeX, rebuild, stage, commit, push, sign approvals or create tags.

The record is prepared for local installation; it has not been installed in the user's Windows repository by this assistant. No rebuild is needed. Technical correction work through Batch 36 is complete; editorial/proof-scope/final visual/publication decisions are not automatically completed.
