# GA-09 Batch 33 — consolidated 49-case technical register

Checkpoint: 6ae7093492bc8600c7415a1b3626293b7f6f7ebb. Findings from Batches 30–32, dated 12 November 2026.

The register records AI technical provenance findings for all 49 inherited identities. Each row preserves the source-unit ID, declared source, solution-origin declaration, normalized checkpoint SHA-256, disposition, evidence reference and pending editorial acceptance. Evidence references identify files in the earlier Batch 30–32 evidence packages; they are not all repeated here.

The source hash normalization is UTF-8 without BOM and CRLF converted to LF, with no trimming. This permits Windows line endings while rejecting content drift. A source mismatch stops the whole preflight before any write. All 49 reviewed file bodies must match; this does not require the current branch tip to equal the checkpoint if unrelated later commits exist.

The only TeX change adds four comment lines to CP-VI-0022: supporting L1403–L1526; excluding the independent plane-curve passage L1527–L1752, preserved as CP-VI-0049. The original declared source line is retained. Rendered content is unchanged, so no PDF rebuild is required.

Apply installs this README and GA09_B33_49_CASE_REGISTER.json under reports/companion/global_audit/ga09_b33_part_vi. It does not overwrite different existing reports or change authoritative reviewer worksheets. Repeating the same package is safe. Changed existing files are backed up under reports/companion/ga09_batch33_backup_TIMESTAMP. No staging, commit, push, signature or release tag is performed.

Technical classification is not editorial acceptance or full mathematical certification. Source-derived corrected solutions must retain their correction disclosures, and authored solutions must retain authorship distinctions. The 25 flagged-proof and 15 controlled-correction cohorts still require their own reconciliation; Parts VII/VIII review, final PDF visual acceptance, publication wording and release authorization remain separate gates.

Package validation uses copies of all 49 checkpoint files: complete preflight/apply/repeat, CRLF preservation, and deliberate source-drift rejection. The supplied CP-VI-0022.annotated.tex is a reference output; use the guarded script rather than copying it over a working file.
