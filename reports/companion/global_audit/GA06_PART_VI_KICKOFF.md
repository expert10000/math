# GA-06 — Companion Part VI Mathematical and Provenance Audit: Kickoff

**Status:** OPEN / READ-ONLY INVENTORY FIRST (not yet certified)

**Scope:** Part VI — *Algebraic Geometry and Sheaf Theory*, main-text chapters VI/01–VI/49.
The canonical Companion Part VI source is
`books/companion_problems_solutions/chapters/part06_volume_vi/chapter.tex`.

## Authoritative inventory inputs

Use the imported inventory as the source of truth, not inferred chapter counts:

- `imports/problem_inventory/PROBLEM_LEDGER.tsv`
- `imports/problem_inventory/SEMANTIC_PROBLEM_UNITS.tsv`
- `imports/problem_inventory/SOURCE_FILES.tsv`

Reconcile those against the Part VI chapter, migration metadata, source candidates,
reader-facing problem identifiers, and one-to-one solution mappings.
Never generate source provenance from a problem title alone.

## Work packages

1. **GA-06a — Inventory and structural baseline.** Determine exact counts directly
   from current chapter + inventory; locate validator(s); check stable Companion IDs,
   problem/solution adjacency, titles, chapter mappings, missing or duplicated units,
   and unresolved canonical source candidates. Record blockers without changing text.
2. **GA-06b — Mathematical quality, batches.** Check hypotheses, proofs,
   counterexamples, notation and dependencies in the topics below. Mark
   VERIFIED, CORRECTED, or REVIEW_REQUIRED with evidence and traceable IDs.
   Do not silently merge independent problems or add invented sources.
3. **GA-06c — Corrections and provenance reconciliation.** Apply only adjudicated,
   backed-up, checksum-guarded corrections; update disposition/migration ledgers
   and re-run validation after each batch.
4. **GA-06d — PDF and freeze.** Check rendered statements, solutions, headings,
   environments and Part V/VI/VII boundaries, then commit/push and record
   the exact post-correction Git revision and source checksum.

## Mathematical coverage

- Affine algebraic sets, coordinate rings, Nullstellensatz (VI/01–VI/05)
- Prime spectra, localization and structure sheaf (VI/06–VI/11)
- Presheaves/sheaves, stalks and gluing (VI/12–VI/17)
- Affine and general schemes (VI/18–VI/22)
- Morphisms, fiber products and families (VI/23–VI/28)
- Krull dimension, chains, local dimension (VI/29–VI/32)
- Quasicoherent modules and projective geometry (VI/33–VI/38)
- Divisors, rational maps, birational geometry (VI/39–VI/45)
- Cohomology of sheaves and exact sequences (VI/46–VI/49)

## Release gates

Exact problem/solution counts and unique labels; complete provenance dispositions;
zero unresolved source candidates or explicitly approved holds; no unverified
mathematical claims; passing Part VI validator and clean PDF boundaries.

**Explicit separation:** GA-05 Part V is frozen in its own recorded Git revision.
GA-06 work must not change Part V without opening a separate documented corrective amendment.
