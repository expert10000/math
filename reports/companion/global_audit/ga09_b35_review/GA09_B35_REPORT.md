# GA-09 Batch 35 - Provenance, proof qualifications, and whole-book visual review

Review date: 13 November 2026. Reviewed source commit: `8614f3920f7367b8b5e17d82cb6b7092f74aaa8d`.

Reviewed PDF SHA-256: `8dd691c183d21590e176f31347c96e6af1d9701f3d8cfc1d56cbc476c20dc812`. Physical pages: **1,592**.

## Outcome

All **49 provenance findings** and **35 proof-cohort IDs / 40 obligations** are reconciled with explicit limits. Historical evidence is retained, the two Batch 34 fixes are verified, and source identity is kept separate from proof correctness.

The whole-book visual screening is complete, but **corrections are required**: one mathematical statement/solution inconsistency and four presentation issues are recorded below. Publication approval and the release tag remain pending. No rendered TeX was changed by this review.

## Evidence and currentness

The 49 archived main-file fingerprints were recomputed against Batch 33. GitHub comparison of `6ae7093` to `8614f39` confirms exactly three changed mathematical-source files: CP-VI-0010, CP-VI-0022, and CP-VI-0037; the other changes are the four B33/B34 report files. The three current files were fetched at the exact reviewed commit and their normalized hashes verified. CP-VI-0022 changes comments only. CP-VI-0010 and CP-VI-0037 contain the reviewed B34 corrections. The PDF fingerprint matches the uploaded B34 review evidence.

This reconciles the earlier passage comparisons; it does not represent a new independent comparison against all original manuscripts. Archived source excerpts, prior dispositions, commit comparison metadata, page checks, and contact sheets are included as evidence. The archived CP-VI-0047 supplement has one extra terminal newline; the exact current supplement was fetched independently and matches the B34 guard (eec14248cb8ec7e8aa7bf01a75a7b816bddabece7a3a5bcbf2532bff1ba9fef4). This byte-level archive difference is not a mathematical change.

## 49 provenance findings

Normalized identity never means byte identity or proof correctness. Embedded source questions do not transfer source authorship to added canonical solutions. Edited proofs remain explicitly edited. The six presentation-only cases retain their macro/heading qualifications.

| Disposition | Cases |
|---|---:|
| NORMALIZED_FULL_MATCH | 7 |
| SOURCE_DERIVED_CORRECTED | 10 |
| SOURCE_EMBEDDED_IN_CURRENT | 19 |
| AUTHORED_SOLUTION_ADDITION | 2 |
| SOURCE_SPLIT_AND_CORRECTED | 1 |
| PRESENTATION_ONLY | 6 |
| SOURCE_DERIVED_EDITED_TWO_SPANS | 1 |
| NORMALIZED_FULL_MATCH_EXPANDED_RANGE | 1 |
| EXPOSITION_REWRITE | 1 |
| SOURCE_DERIVED_EDITED_WITH_INCLUDED_SUPPLEMENT | 1 |

| Case | Disposition and finding |
|---|---|
| CP-VI-0001 | **NORMALIZED_FULL_MATCH**. Original passage matches the normalized current body; this is not raw byte identity. |
| CP-VI-0002 | **NORMALIZED_FULL_MATCH**. Original passage matches the normalized current body; this is not raw byte identity. |
| CP-VI-0003 | **SOURCE_DERIVED_CORRECTED**. Expanded L712–L1220; later explicit clopen–idempotent proof and typesetting changes disclosed. |
| CP-VI-0004 | **SOURCE_EMBEDDED_IN_CURRENT**. Original passage is embedded in the normalized current body; additions require separate attribution and proof review. |
| CP-VI-0005 | **SOURCE_EMBEDDED_IN_CURRENT**. Original passage is embedded in the normalized current body; additions require separate attribution and proof review. |
| CP-VI-0006 | **SOURCE_EMBEDDED_IN_CURRENT**. Original passage is embedded in the normalized current body; additions require separate attribution and proof review. |
| CP-VI-0007 | **SOURCE_EMBEDDED_IN_CURRENT**. Original passage is embedded in the normalized current body; additions require separate attribution and proof review. |
| CP-VI-0008 | **SOURCE_EMBEDDED_IN_CURRENT**. Original passage is embedded in the normalized current body; additions require separate attribution and proof review. |
| CP-VI-0009 | **SOURCE_EMBEDDED_IN_CURRENT**. Original passage is embedded in the normalized current body; additions require separate attribution and proof review. |
| CP-VI-0010 | **SOURCE_EMBEDDED_IN_CURRENT**. Original passage is embedded in the normalized current body; additions require separate attribution and proof review. Batch 34 corrects the authored conclusion: the dual-number spectrum is nonreduced; Spec k is reduced. Source-question lineage is retained; authored solution is not exact imported text. |
| CP-VI-0011 | **SOURCE_EMBEDDED_IN_CURRENT**. Original passage is embedded in the normalized current body; additions require separate attribution and proof review. |
| CP-VI-0012 | **SOURCE_EMBEDDED_IN_CURRENT**. Original passage is embedded in the normalized current body; additions require separate attribution and proof review. |
| CP-VI-0013 | **SOURCE_EMBEDDED_IN_CURRENT**. Original passage is embedded in the normalized current body; additions require separate attribution and proof review. |
| CP-VI-0014 | **SOURCE_EMBEDDED_IN_CURRENT**. Original passage is embedded in the normalized current body; additions require separate attribution and proof review. |
| CP-VI-0015 | **AUTHORED_SOLUTION_ADDITION**. Original question retained; Chinese remainder theorem solution is authored. The two factors F2 and F3 yield two clopen points. |
| CP-VI-0016 | **SOURCE_EMBEDDED_IN_CURRENT**. Original passage is embedded in the normalized current body; additions require separate attribution and proof review. |
| CP-VI-0017 | **SOURCE_EMBEDDED_IN_CURRENT**. Original passage is embedded in the normalized current body; additions require separate attribution and proof review. |
| CP-VI-0018 | **SOURCE_EMBEDDED_IN_CURRENT**. Original passage is embedded in the normalized current body; additions require separate attribution and proof review. |
| CP-VI-0019 | **NORMALIZED_FULL_MATCH**. Original passage matches the normalized current body; this is not raw byte identity. |
| CP-VI-0020 | **SOURCE_EMBEDDED_IN_CURRENT**. Original passage is embedded in the normalized current body; additions require separate attribution and proof review. |
| CP-VI-0021 | **SOURCE_DERIVED_CORRECTED**. Direct images put all Čech terms on X; insertion homotopy acts on the restricted sheaf complex. This avoids the infinite-product stalk error. Both repeated explanations are repaired. |
| CP-VI-0022 | **SOURCE_SPLIT_AND_CORRECTED**. The original L1403–L1752 contains Problem 4 and independent Problem 5. Current punctured-plane dossier retains the former and adds the affine-acyclic-cover justification. Support L1403–L1526; exclude L1527–L1752, preserved under CP-VI-0049. Do not classify the removed plane-curve block as lost content. Batch 33 adds only source-boundary comments. Supporting source L1403-L1526; L1527-L1752 is the independent CP-VI-0049 problem. Original broad declaration is preserved as historical metadata. |
| CP-VI-0023 | **SOURCE_DERIVED_CORRECTED**. The tensor derivation factorization now proves φ(uv)=μ(u)φ(v)+μ(v)φ(u), hence φ(I²)=0; generators db prove uniqueness. The two-open supplementary example explicitly assumes acyclicity before identifying Čech and sheaf cohomology. |
| CP-VI-0024 | **SOURCE_DERIVED_CORRECTED**. Finiteness is established before finite-module Nakayama. Properness plus quasi-finiteness yields a finite algebra; cotangent surjectivity kills the maximal-ideal quotient over B, then the finite cokernel over A. This is a proof repair, not a presentation normalization. |
| CP-VI-0025 | **PRESENTATION_ONLY**. After the displayed sheaf macro expansions, residual differences expand id to operatorname{id}. Retain normalized source-derived full-body lineage; no new mathematical delta found. |
| CP-VI-0026 | **SOURCE_DERIVED_EDITED_TWO_SPANS**. Supporting spans L352–L556 and L837–L1174; exclude L557–L836, independent CP-VI-0048. Proof rewriting disclosed. |
| CP-VI-0027 | **NORMALIZED_FULL_MATCH**. Original passage matches the normalized current body; this is not raw byte identity. |
| CP-VI-0028 | **PRESENTATION_ONLY**. Full body agrees after explicit Hom, Spec and heading expansions. The earlier conservative comparison had omitted Hom; no mathematical delta found. |
| CP-VI-0029 | **PRESENTATION_ONLY**. Full body agrees after explicit Hom, Spec and heading expansions. The terminal-object proof remains the same. |
| CP-VI-0030 | **SOURCE_EMBEDDED_IN_CURRENT**. Original passage is embedded in the normalized current body; additions require separate attribution and proof review. |
| CP-VI-0031 | **NORMALIZED_FULL_MATCH_EXPANDED_RANGE**. Expanded L184–L1004; normalized whole-section lineage with explicit Spec/Proj expansion. |
| CP-VI-0032 | **SOURCE_DERIVED_CORRECTED**. The local fraction g=h/f^N identifies the same chosen open as D_V(g)=D_U(fh). This replaces an unsupported shrinking step with simultaneous distinguished-open equality. |
| CP-VI-0033 | **SOURCE_DERIVED_CORRECTED**. Nonemptiness is made explicit and the generic-stalk injection replaces the false general nonzero-germ-open-locus argument. The statement is corrected as well as the proof; retain that qualification. |
| CP-VI-0034 | **SOURCE_EMBEDDED_IN_CURRENT**. Original passage is embedded in the normalized current body; additions require separate attribution and proof review. |
| CP-VI-0035 | **NORMALIZED_FULL_MATCH**. Original passage matches the normalized current body; this is not raw byte identity. |
| CP-VI-0036 | **NORMALIZED_FULL_MATCH**. Original passage matches the normalized current body; this is not raw byte identity. |
| CP-VI-0037 | **AUTHORED_SOLUTION_ADDITION**. Imported question retained after OO/Spec expansions. Added proof constructs the unique generic point using nonempty affine opens and identifies its stalk with each fraction field. Keep the authored-solution declaration. Batch 34 qualifies the inherited question with nonempty. The current statement and authored proof therefore must not be represented as an unchanged imported question-and-solution pair. |
| CP-VI-0038 | **NORMALIZED_FULL_MATCH**. Original passage matches the normalized current body; this is not raw byte identity. |
| CP-VI-0039 | **SOURCE_DERIVED_CORRECTED**. Besides exposition compression, the fibre reducedness argument is repaired. For char≠2, F=(U−1)V²+U²(U+1) is primitive and square-free; g=U+a is a non-zero-divisor modulo J=(W,F), so gJ=(g)∩J is radical. For char=2, localization at (W,U+V) makes g and U+1 units and exposes the nonzero nilpotent U+V. These are substantive ideal-level proofs. |
| CP-VI-0040 | **EXPOSITION_REWRITE**. The two Cartesian-square proofs are compressed but retain the same natural test-object bijections: the first condition forces s=x_S=y_S, and the second forces z=y=f∘x. Preserve source-derived edited-prose lineage. |
| CP-VI-0041 | **SOURCE_EMBEDDED_IN_CURRENT**. Original passage is embedded in the normalized current body; additions require separate attribution and proof review. |
| CP-VI-0042 | **SOURCE_DERIVED_CORRECTED**. The dimension/codimension assertions now exclude empty Y. An independent dimension comparison for affine charts, using the common function field, replaces the circular dependency between later parts. Retain both statement qualification and proof addition. |
| CP-VI-0043 | **SOURCE_EMBEDDED_IN_CURRENT**. Original passage is embedded in the normalized current body; additions require separate attribution and proof review. |
| CP-VI-0044 | **PRESENTATION_ONLY**. Residual changes expand A, divisor and standard projective/integer/class-group macros. The displayed class-group computations retain their source text; this does not newly certify the whole proof. |
| CP-VI-0045 | **PRESENTATION_ONLY**. After projective/integer macro expansion, the only residual difference is Pic→operatorname{Pic}. Retain normalized full-body source lineage; this is not a new proof certification. |
| CP-VI-0046 | **SOURCE_DERIVED_CORRECTED**. Coherence of pullback is restricted to locally Noetherian X; quasi-coherence remains unconditional. The infinite square-zero ideal example shows arbitrary coherence preservation fails. Do not describe local Noetherianity as necessary for every individual pullback. |
| CP-VI-0047 | **SOURCE_DERIVED_EDITED_WITH_INCLUDED_SUPPLEMENT**. Main proof is compressed; the included theory/examples are retained with changed headings, layout and substantive clarifications. Supplement adds normal/Noetherian hypotheses, completes divisor-relation calculations using units, specifies geometric base-point freedom and qualifies coherent pullback. Whole-body exact identity is false. Treat as one main problem with included supplementary theory/examples; no extra numbered problem environment was found. Entire 82-kB supplement is not certified by this provenance review. |
| CP-VI-0048 | **PRESENTATION_ONLY**. The remaining delta is the optional short heading and texorpdfstring wrapper for Gamma(U,−). Mathematical text is retained. |
| CP-VI-0049 | **SOURCE_DERIVED_CORRECTED**. Positive degree is explicit; the hypersurface sequence justifies H⁰=k even for singular/nonreduced curves. Overlap survivors are u^r v^(−m), 2≤r≤d−1, 1≤m<r, with cubic survivor u²/v. The original u/v class extends from V and vanishes. Retain the correction disclosure. |

### Boundary and authorship decisions

- CP-VI-0003: expanded support L712-L1220; the explicit idempotent proof is a disclosed later addition.
- CP-VI-0022: supporting range L1403-L1526; exclude L1527-L1752, the independent CP-VI-0049 plane-curve problem. The original broad declaration is historical metadata, not the final support claim.
- CP-VI-0026: support L352-L556 and L837-L1174; exclude L557-L836, independently retained as CP-VI-0048. Proof rewriting remains disclosed.
- CP-VI-0031: expanded support L184-L1004; full-section agreement is after explicit macro and whitespace normalization.
- CP-VI-0037: the inherited statement now has the B34 nonempty qualification; its canonical solution is authored.
- CP-VI-0047: one main problem with an included theory/examples supplement, not an additional numbered problem. The entire supplement is not independently proof-certified by a provenance comparison.

## Proof-review qualifications

The historical cohorts remain 25 flagged rows and 15 corrected IDs with five overlaps: CP-VI-0021, 0023, 0024, 0042, and 0049. Thus 35 distinct IDs carry 40 obligations. The two new B34 sentence fixes remain outside the historical 15-correction cohort.

The 25 flagged paths resolve to **24 main problem files containing solutions** (including the two now-corrected cases) and **one included supplement**, CP-VI-0047. A heading-marker alert is not a missing proof when the mathematical solution is present under another heading. This resolves the content-presence question; it does not prove every argument correct.

The 15 targeted historical repair findings are carried forward with their hypotheses. No new full proof certification is asserted. CP-VI-0047 remains subject to a distinct full-supplement review if such certification is required. Human editorial signatures remain unrecorded; this report is identified as AI technical review.

| Case | Content finding | Controlled correction / qualification |
|---|---|
| CP-VI-0003 | Not in flagged-format cohort. | Explicit clopen-to-idempotent construction removes black-box converse. Content-presence and targeted historical repair findings are reconciled; this does not certify every proof in the file or its supplements. |
| CP-VI-0004 | PID prime classification: generic zero ideal and irreducible-polynomial closed points. | Not in historical controlled-correction cohort. Content-presence and targeted historical repair findings are reconciled; this does not certify every proof in the file or its supplements. |
| CP-VI-0005 | D(x) excludes precisely the primes containing x. | Not in historical controlled-correction cohort. Content-presence and targeted historical repair findings are reconciled; this does not certify every proof in the file or its supplements. |
| CP-VI-0006 | D(x)=Spec k[x,x^-1] via the standard localization theorem. | Not in historical controlled-correction cohort. Content-presence and targeted historical repair findings are reconciled; this does not certify every proof in the file or its supplements. |
| CP-VI-0007 | D(x)∩D(y)=D(xy), with the Laurent coordinate ring. | Not in historical controlled-correction cohort. Content-presence and targeted historical repair findings are reconciled; this does not certify every proof in the file or its supplements. |
| CP-VI-0008 | One prime (epsilon); the local ring contains a nonzero nilpotent. | Not in historical controlled-correction cohort. Content-presence and targeted historical repair findings are reconciled; this does not certify every proof in the file or its supplements. |
| CP-VI-0009 | Every prime contains epsilon, so D(epsilon) is empty. | Not in historical controlled-correction cohort. Content-presence and targeted historical repair findings are reconciled; this does not certify every proof in the file or its supplements. |
| CP-VI-0010 | Solution present; concluding reduced/nonreduced labels are reversed. Guarded correction supplied. B34 correction is now verified in the current source and PDF. | Not in historical controlled-correction cohort. Content-presence and targeted historical repair findings are reconciled; this does not certify every proof in the file or its supplements. |
| CP-VI-0011 | Spectrum of k×k has two clopen points. | Not in historical controlled-correction cohort. Content-presence and targeted historical repair findings are reconciled; this does not certify every proof in the file or its supplements. |
| CP-VI-0012 | Four coordinatewise idempotents in k×k. | Not in historical controlled-correction cohort. Content-presence and targeted historical repair findings are reconciled; this does not certify every proof in the file or its supplements. |
| CP-VI-0013 | Chinese remainder theorem using comaximal (x),(x−1). | Not in historical controlled-correction cohort. Content-presence and targeted historical repair findings are reconciled; this does not certify every proof in the file or its supplements. |
| CP-VI-0014 | Two irreducible components meet, giving a connected reducible spectrum. | Not in historical controlled-correction cohort. Content-presence and targeted historical repair findings are reconciled; this does not certify every proof in the file or its supplements. |
| CP-VI-0015 | Z/6 splits into F2×F3, giving two clopen points. | Not in historical controlled-correction cohort. Content-presence and targeted historical repair findings are reconciled; this does not certify every proof in the file or its supplements. |
| CP-VI-0021 | Long solution present; Čech resolution and flabby argument are identified. | Direct images form sheaves on X; restricted-complex contraction avoids infinite-product stalk interchange. Content-presence and targeted historical repair findings are reconciled; this does not certify every proof in the file or its supplements. |
| CP-VI-0022 | Punctured-plane solution present; acyclic two-open cover and nonzero H1 obstruction. | Not in historical controlled-correction cohort. Content-presence and targeted historical repair findings are reconciled; this does not certify every proof in the file or its supplements. |
| CP-VI-0023 | Relative-differentials solution present, followed by supplementary theory/examples. | Two-open sheaf-cohomology computation states affine/acyclic-cover hypotheses. Content-presence and targeted historical repair findings are reconciled; this does not certify every proof in the file or its supplements. |
| CP-VI-0024 | Closed-immersion solution present; corrected finite-algebra/Nakayama bridge. | Proper quasi-finite gives finiteness before finite-module Nakayama over A. Content-presence and targeted historical repair findings are reconciled; this does not certify every proof in the file or its supplements. |
| CP-VI-0026 | Quotient sheaf solution present; sheafification and stalkwise exactness, followed by supplementary theory. | Not in historical controlled-correction cohort. Content-presence and targeted historical repair findings are reconciled; this does not certify every proof in the file or its supplements. |
| CP-VI-0032 | Not in flagged-format cohort. | Same chosen open equals D_V(g)=D_U(fh). Content-presence and targeted historical repair findings are reconciled; this does not certify every proof in the file or its supplements. |
| CP-VI-0033 | Not in flagged-format cohort. | Nonempty-open domain convention; injection into generic stalk; later irreducibility qualification retained. Content-presence and targeted historical repair findings are reconciled; this does not certify every proof in the file or its supplements. |
| CP-VI-0034 | Authored solution present; simultaneous distinguished-open refinement and finite principal-cover Noetherian criterion. | Not in historical controlled-correction cohort. Content-presence and targeted historical repair findings are reconciled; this does not certify every proof in the file or its supplements. |
| CP-VI-0037 | Authored generic-point/fraction-field solution present. Statement must exclude the empty affine open; guarded correction supplied. B34 correction is now verified in the current source and PDF. | Not in historical controlled-correction cohort. Content-presence and targeted historical repair findings are reconciled; this does not certify every proof in the file or its supplements. |
| CP-VI-0039 | Fibre computations present, with ideal-level reducedness checks. | Not in historical controlled-correction cohort. Content-presence and targeted historical repair findings are reconciled; this does not certify every proof in the file or its supplements. |
| CP-VI-0040 | Both Cartesian-square universal-property proofs are present. | Not in historical controlled-correction cohort. Content-presence and targeted historical repair findings are reconciled; this does not certify every proof in the file or its supplements. |
| CP-VI-0042 | Dimension/codimension solutions present; nonempty-set convention and independent dimension comparison. | Independent affine-open dimension argument avoids circularity; nonempty closed subsets explicit. Content-presence and targeted historical repair findings are reconciled; this does not certify every proof in the file or its supplements. |
| CP-VI-0046 | Not in flagged-format cohort. | Coherent pullback assumes locally Noetherian X; square-zero noncoherent counterexample retained. Content-presence and targeted historical repair findings are reconciled; this does not certify every proof in the file or its supplements. Local Noetherianity is the stated sufficient hypothesis, not a necessary hypothesis for every individual coherent pullback. |
| CP-VI-0047 | Flagged path is the included theory/examples supplement, not a missing stand-alone solution; retain separate editorial classification. | Not in historical controlled-correction cohort. The flagged path is the included theory/examples supplement. Do not add another numbered problem or claim its entire approximately 82-kB body has been independently proof-certified. |
| CP-VI-0048 | Left-exact global-sections proof present; heading wrappers are presentation-only. | Not in historical controlled-correction cohort. Content-presence and targeted historical repair findings are reconciled; this does not certify every proof in the file or its supplements. |
| CP-VI-0049 | Plane-curve Čech solution present; corrected overlap basis and positive-degree qualification. | Correct basis u^r/v^m with 2≤r≤d−1, 1≤m<r; cubic u²/v. Content-presence and targeted historical repair findings are reconciled; this does not certify every proof in the file or its supplements. |
| CP-VI-0054 | Not in flagged-format cohort. | Infinite field stated; monic division proves vanishing ideal; finite-field caution retained. Content-presence and targeted historical repair findings are reconciled; this does not certify every proof in the file or its supplements. |
| CP-VI-0055 | Not in flagged-format cohort. | Finite linearly independent coefficient expansion proves ideal equality, not only equal zero loci. Content-presence and targeted historical repair findings are reconciled; this does not certify every proof in the file or its supplements. |
| CP-VI-0069 | Not in flagged-format cohort. | Common denominator/annihilator exponents and unit-ideal powers prove local-fraction gluing and uniqueness. Content-presence and targeted historical repair findings are reconciled; this does not certify every proof in the file or its supplements. |
| CP-VI-0090 | Not in flagged-format cohort. | Homogenized top term gives a genuine pole on another projective chart, forcing constants. Content-presence and targeted historical repair findings are reconciled; this does not certify every proof in the file or its supplements. |
| CP-VI-0096 | Not in flagged-format cohort. | Regularity is stalkwise; multiplication by f identifies an invertible ideal sheaf. Content-presence and targeted historical repair findings are reconciled; this does not certify every proof in the file or its supplements. |
| CP-VI-0100 | Not in flagged-format cohort. | Geometric singularity test over algebraic closure uses cubic/derivative common roots; infinity is smooth. Content-presence and targeted historical repair findings are reconciled; this does not certify every proof in the file or its supplements. |

## Whole-book visual review

All 1,592 physical pages were rendered and screened across 25 numbered overview sheets; 92 figure-bearing pages received a larger-sheet review, and selected anomalies/corrected passages were inspected individually. Overview screening detects page flow, missing/stranded blocks and conspicuous collisions; it is not a promise that every small glyph on every page was inspected at full resolution. The machine-readable page ledger records that coverage precisely.

Whole-document text checks found no out-of-page spans, no unresolved `??` references, and no Unicode replacement characters. These checks complement visual inspection and cannot certify all clipping, figure labels, or mathematical correctness. The log contains 0 overfull boxes, 6 underfull boxes, and the existing amsmath warning.

Part/chapter transitions, front matter, sparse pages, figure groups, and the final Integration Notes page were screened. The reviewed corrections on physical pages 951 and 1062-1063 and the stereographic label on page 1201 remain legible. The six underfull warnings do not by themselves imply content loss.

### Open findings

#### B35-M01 - P1 - mathematical_statement_inconsistency

Physical pages 563, 564; printed pages 549, 550.

The retained problem box asserts uniform convergence on [r,1) under bounded partial sums and uses necessity-like wording for sum n|a_n|. The solution on the next page already correctly rejects both claims.

Counterexample: a_n=(-1)^n has bounded partial sums, but sup_{x in [r,1)} |a_n x^n|=1 for every n, so the necessary uniform term condition fails.

Recommended correction: In the box assert uniform convergence only on [0,r] (or compact subsets of (-1,1)); state sum n|a_n|<infinity as a sufficient condition for uniform absolute convergence of the derivative on |x|<=1, not a necessary condition. Preserve or explicitly annotate the historical source wording in provenance. The existing solution already supplies the correct qualification.

#### B35-L01 - P2 - pagination

Physical pages 966, 967; printed pages 952, 953.

VI/16 heading occupies a page alone; the body starts on the next page.

Recommended correction: Inspect the first input after the VI/16 heading and keep the heading with initial body text; do not remove mathematical content. Rebuild and inspect both adjacent pages.

#### B35-L02 - P2 - figure_label_overlap

Physical pages 1268; printed pages 1254.

Figure 7.41: the title Mercator chart (u,v) overlaps the vertical-axis label u (Mercator latitude).

Recommended correction: Move the chart title or vertical-axis label to separate positions and inspect the rebuilt figure at normal reading scale.

#### B35-E01 - P2 - caption_without_visible_plot

Physical pages 565, 566; printed pages 551, 552.

A standalone Figure paragraph describes clipped sine functions, but no plot accompanies it on these pages.

Recommended correction: Either include the intended plot or convert the caption into ordinary explanatory prose. Preserve the valid worked argument.

#### B35-E02 - P2 - production_instruction_in_reader_text

Physical pages 575; printed pages 561.

The text says one may use the following code and a footnote instructs loading pgfplots and setting compat=1.18; no following code or corresponding figure appears on that page.

Recommended correction: Replace the dangling production instruction with reader-facing exposition or supply the intended figure; keep build instructions outside the printed problem.

## Repository installation

The included installer adds five report files under `reports/companion/global_audit/ga09_b35_review/`. It verifies 56 Part VI source fingerprints, the current Part VI chapter, the B33/B34 registers, and the reviewed PDF before writing. It rejects changed existing output files, supports repeat execution, and never modifies rendered TeX, existing acceptance worksheets, publication wording, commits, or tags. It must be run locally; no installation in the Windows repository has yet been performed.

No PDF rebuild is needed to install this report. Repairing the five findings will require a separate guarded source patch, a fresh build, and review of the new PDF fingerprint.

## Review state

- Provenance findings: reconciled with attribution and normalization qualifications.
- Proof obligations: targeted findings reconciled; broad independent proof certification is not asserted.
- Whole-book visual screening: complete; corrections required.
- Mathematical content inconsistency B35-M01: open, despite the correct existing solution.
- Publication approval: pending.
- Release tag: pending; none created.
