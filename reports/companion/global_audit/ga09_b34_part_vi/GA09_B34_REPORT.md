# GA-09 Batch 34 — Flagged-proof and controlled-correction reconciliation

12 November 2026. AI technical review of checkpoint 7a5abd1967b2e6287c62f9806fe9137b7cb1d499.

## Counts and overlap

25 historical flagged rows plus 15 distinct historically corrected IDs overlap in five cases: CP-VI-0021, CP-VI-0023, CP-VI-0024, CP-VI-0042, CP-VI-0049. Therefore there are 35 distinct canonical IDs and 40 cohort obligations. A case appearing in both groups has both a format/content obligation and a correction obligation; do not count it as two distinct problems.

The flagged list comes from GA06C_SOLUTION_DECISIONS.tsv in the supplied Batch 10 evidence archive. Its two copies are identical. The legacy worksheet is not present at its expected tracked path at this checkpoint (GitHub returned 404); the archived record is used explicitly as the cohort source, not represented as a live authoritative file.

The correction list is reconstructed from the specific patches in GA-06b Batches 01–09 (14 distinct IDs) and GA-06c7 (CP-VI-0021). Repeated changes or EOF cleanup to that file do not create another corrected ID. Later corrections are not silently added to this historical cohort.

## Two new narrow corrections

CP-VI-0010 correctly establishes that the dual-number spectrum and field spectrum are homeomorphic, but its final sentence assigns reducedness to the wrong one. Replace only that sentence: the first has the nonzero nilpotent epsilon; the second is reduced.

CP-VI-0037 states the fraction-field claim for any affine open. The empty affine open has coordinate ring zero, whose fraction field is undefined. Insert nonempty in the statement, consistently with the existing proof. The proof itself is unchanged.

Both are new findings in the flagged cohort, not part of the historical 15 corrections. Before application their format statuses explicitly retain CORRECTION_REQUIRED. The report preserves that pre-application finding even after the guarded installer succeeds; the apply receipt records which source changes were actually made.

## Per-case findings

### CP-VI-0003

Controlled correction (GA-06b Batch 02): Explicit clopen-to-idempotent construction removes black-box converse.

### CP-VI-0004

Format/content: PID prime classification: generic zero ideal and irreducible-polynomial closed points.

### CP-VI-0005

Format/content: D(x) excludes precisely the primes containing x.

### CP-VI-0006

Format/content: D(x)=Spec k[x,x^-1] via the standard localization theorem.

### CP-VI-0007

Format/content: D(x)∩D(y)=D(xy), with the Laurent coordinate ring.

### CP-VI-0008

Format/content: One prime (epsilon); the local ring contains a nonzero nilpotent.

### CP-VI-0009

Format/content: Every prime contains epsilon, so D(epsilon) is empty.

### CP-VI-0010

Format/content: Solution present; concluding reduced/nonreduced labels are reversed. Guarded correction supplied.

### CP-VI-0011

Format/content: Spectrum of k×k has two clopen points.

### CP-VI-0012

Format/content: Four coordinatewise idempotents in k×k.

### CP-VI-0013

Format/content: Chinese remainder theorem using comaximal (x),(x−1).

### CP-VI-0014

Format/content: Two irreducible components meet, giving a connected reducible spectrum.

### CP-VI-0015

Format/content: Z/6 splits into F2×F3, giving two clopen points.

### CP-VI-0021

Format/content: Long solution present; Čech resolution and flabby argument are identified.

Controlled correction (GA-06c7): Direct images form sheaves on X; restricted-complex contraction avoids infinite-product stalk interchange.

### CP-VI-0022

Format/content: Punctured-plane solution present; acyclic two-open cover and nonzero H1 obstruction.

### CP-VI-0023

Format/content: Relative-differentials solution present, followed by supplementary theory/examples.

Controlled correction (GA-06b Batch 06): Two-open sheaf-cohomology computation states affine/acyclic-cover hypotheses.

### CP-VI-0024

Format/content: Closed-immersion solution present; corrected finite-algebra/Nakayama bridge.

Controlled correction (GA-06b Batch 07): Proper quasi-finite gives finiteness before finite-module Nakayama over A.

### CP-VI-0026

Format/content: Quotient sheaf solution present; sheafification and stalkwise exactness, followed by supplementary theory.

### CP-VI-0032

Controlled correction (GA-06b Batch 04): Same chosen open equals D_V(g)=D_U(fh).

### CP-VI-0033

Controlled correction (GA-06b Batch 05): Nonempty-open domain convention; injection into generic stalk; later irreducibility qualification retained.

### CP-VI-0034

Format/content: Authored solution present; simultaneous distinguished-open refinement and finite principal-cover Noetherian criterion.

### CP-VI-0037

Format/content: Authored generic-point/fraction-field solution present. Statement must exclude the empty affine open; guarded correction supplied.

### CP-VI-0039

Format/content: Fibre computations present, with ideal-level reducedness checks.

### CP-VI-0040

Format/content: Both Cartesian-square universal-property proofs are present.

### CP-VI-0042

Format/content: Dimension/codimension solutions present; nonempty-set convention and independent dimension comparison.

Controlled correction (GA-06b Batch 06): Independent affine-open dimension argument avoids circularity; nonempty closed subsets explicit.

### CP-VI-0046

Controlled correction (GA-06b Batch 06): Coherent pullback assumes locally Noetherian X; square-zero noncoherent counterexample retained.

### CP-VI-0047

Format/content: Flagged path is the included theory/examples supplement, not a missing stand-alone solution; retain separate editorial classification.

### CP-VI-0048

Format/content: Left-exact global-sections proof present; heading wrappers are presentation-only.

### CP-VI-0049

Format/content: Plane-curve Čech solution present; corrected overlap basis and positive-degree qualification.

Controlled correction (GA-06b Batch 09): Correct basis u^r/v^m with 2≤r≤d−1, 1≤m<r; cubic u²/v.

### CP-VI-0054

Controlled correction (GA-06b Batch 01): Infinite field stated; monic division proves vanishing ideal; finite-field caution retained.

### CP-VI-0055

Controlled correction (GA-06b Batch 01): Finite linearly independent coefficient expansion proves ideal equality, not only equal zero loci.

### CP-VI-0069

Controlled correction (GA-06b Batch 03): Common denominator/annihilator exponents and unit-ideal powers prove local-fraction gluing and uniqueness.

### CP-VI-0090

Controlled correction (GA-06b Batch 07): Homogenized top term gives a genuine pole on another projective chart, forcing constants.

### CP-VI-0096

Controlled correction (GA-06b Batch 08): Regularity is stalkwise; multiplication by f identifies an invertible ideal sheaf.

### CP-VI-0100

Controlled correction (GA-06b Batch 08): Geometric singularity test over algebraic closure uses cubic/derivative common roots; infinity is smooth.

## Review limits and installation

All 36 required paths (35 cohort paths plus the CP-VI-0047 main file establishing the supplement input) were fetched at the exact checkpoint and verified by recomputing their Git blob hashes. Presence of solution content resolves a missing-marker alert as a content-presence question; it is not full proof certification. CP-VI-0047 remains an included theory/examples classification requiring editorial acceptance. Its full supplement is not independently certified here.

The installer verifies all 36 normalized source SHA-256 hashes, permits exactly the two supplied corrected states on repeat, backs up edited sources, and installs this report plus the JSON register under reports/companion/global_audit/ga09_b34_part_vi. It refuses different preexisting reports. It does not modify authoritative reviewer signatures, edition wording, Git refs or release tags. The historical worksheet is included as evidence only and is not installed over any live worksheet.

A PDF rebuild is required after applying the two rendered-text corrections. The previously accepted figure check does not visually certify the new PDF hash. The report documents targeted correction obligations rather than automatically granting final mathematical, provenance, visual or publication approval.
