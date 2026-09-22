# Part IV figure migration summary

This audit covers the source-backed visual pass for Companion **Part IV / Volume IV**.

- Part IV atlas rows with visual interest: **46**
- Atlas rows already tagged SOURCE_FIGURE: **12**
- Source-backed rows with staged artifacts: **11**
- Source flag reviewed as non-local / false positive: **1** (CP-IV-0047)
- Raster source figures staged: **24**
- TikZ / TikZ-figure snippets staged: **26**
- Remaining non-source CANDIDATE figure rows: **34** (not changed in this batch)

No figure is inserted into the reader-facing Part IV chapter yet. Integration belongs to the matching
problem migration so that captions, labels, and nearby mathematical text remain coherent.

## Source-backed Companion IDs

CP-IV-0035, CP-IV-0039, CP-IV-0065, CP-IV-0066, CP-IV-0069,
CP-IV-0083, CP-IV-0089, CP-IV-0098, CP-IV-0102, CP-IV-0110,
and CP-IV-0115.

CP-IV-0047 was audited separately: its exact semantic source span contains no figure block.