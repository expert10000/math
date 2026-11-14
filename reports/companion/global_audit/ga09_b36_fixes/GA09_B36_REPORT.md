# GA-09 Batch 36 - Five focused corrections

13 November 2026. Predecessor checkpoint: 8614f3920f7367b8b5e17d82cb6b7092f74aaa8d.

## Changes

| Finding | Source correction | Verification needed after rebuild |
|---|---|---|
| B35-M01, CP-II-0556 | Correct the retained problem-box uniform-convergence claim and state weighted absolute convergence as sufficient, not necessary. Existing correct solution remains unchanged. | Box and solution agree; box fits and is legible. |
| B35-L01, VI/16 | Insert a clear page before the section, before the stable-ID helper can force a break after the title. | Heading, ID and opening text occupy the same page; inspect both neighbours. |
| B35-L02, Figure 7.41 | Move Mercator chart title from y=1.9 to y=2.45. | Chart title clears vertical-axis label and nearby text. |
| B35-E01, CP-II-0560 | Remove the empty center block and turn the unused Figure caption into an Interpretation paragraph. | No dangling caption or unexplained empty plot area. |
| B35-E02, CP-II-0098 | Remove the dangling paragraph and footnote about following pgfplots code. | Reader-facing eigenfunction discussion joins cleanly to the Laplacian definition. |

The three edited files are the Part II chapter, Part VI chapter inclusion file, and Part VII chapter. No individual Part VI problem/supplement files are edited. The historical source wording and exact before/after diffs are preserved under evidence/. The CP-II-0556 source correction is explicitly annotated in TeX; it is not described as unchanged imported text.

## Mathematical check

For a_n=(-1)^n, partial sums are bounded, but sup over x in [r,1) of |a_n x^n| is 1 for every n. Thus terms do not converge uniformly to zero there, so the retained box was false under its stated bounded-partial-sum hypothesis. The correction restricts the unconditional uniform conclusion to [0,r]. The existing solution already explains this distinction and remains unchanged.

If sum n|a_n| is finite, the derivative series is uniformly absolutely convergent on |x|<=1 by the Weierstrass bound |n a_n x^(n-1)|<=n|a_n|. This is a sufficient condition, not a necessary condition for uniform convergence on the open interval. The reference to closed endpoints denotes the uniformly convergent series extension.

## Evidence and states

The five Batch 35 reports are installed unchanged as historical evidence if absent; if already installed they must agree after BOM/newline normalization. Their 49 provenance findings and 35 proof IDs / 40 obligations remain tied to the predecessor snapshot. Batch 36 does not overwrite that historical review with a false completed status.

All five findings have status PATCH_PREPARED / PDF_REVIEW_PENDING. A new local full-book build is required. After source edits, the old 1,592-page count and old physical-page coordinates must not be assumed; locate the changed passages by headings and canonical IDs. Publication approval and the release tag remain pending. No commit, push, reviewer signature or tag is created by the installer.

## Guarded installation

The installer checks package integrity, all 56 Part VI problem/supplement hashes, the Part VI inclusion chapter, both changed large chapters, both historical registers, and the predecessor PDF on first application. It accepts only the complete before state or complete after state, rejects mixed states, preserves source BOM/newline style, creates byte-exact backups with hashes, and restores written files on an application error. Differing existing reports are never overwritten.

Backups are retained under reports/companion/global_audit/ga09_b36_backups/. They are evidence, not files to stage in the later checkpoint.

## Validation limits

Source-drift, repeat-run, CRLF/BOM preservation and report-conflict checks are exercised on a reconstructed fixture repository. A small TeX rendering fixture is included for the changed box, figure and page-boundary repair. Local PDF compilation could not run because this environment lacks the pdflatex format file, despite having the executable. Therefore no post-patch PDF visual pass is claimed. The Windows full-book rebuild and resulting review ZIP are required to close the findings.
