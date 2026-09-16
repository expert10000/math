# Figures, tables, and reproducibility roadmap

This roadmap turns the current visual/reproducibility recommendations into a
small sequence of reviewable commits. It starts from the completed foundations:

- C07 already added nine chapter-local conceptual visual overlays in Volumes IV,
  V, VI, and VII.
- C08 already supplies a deterministic eight-volume build and document-QA gate.
- C09 already supplies dependency-free, deterministic executable checks for
  Volume VII Chapters 38–42.

The work below must extend those assets rather than replace them with decorative
or duplicate figures.

## Shared contract

Every new visual must explain a specific mathematical relationship, have a
caption that states its intended interpretation and a prose reference near its
first use. Prefer a tracked TikZ, SVG, Asymptote, or source-data file over an
opaque raster asset. Generated outputs must be reproducible by a documented
command and have a source-to-output entry in a figure manifest.

Figures must not silently strengthen a theorem. In particular, diagrams of
`Spec` must be labelled as specialization posets rather than Euclidean pictures;
exponential-map diagrams must not suggest global injectivity; and numerical
figures must state mesh, scale, boundary, sign, and error conventions.

## Commit plan

### C13 — figure inventory and source contract

**Commit**

```text
audit(figures): add canonical vector-source and chapter-anchor manifest
```

**Deliverables**

- Add a machine-readable manifest for every C07 visual and each new planned
  visual: source file, generated artifact (if any), chapter anchor, label,
  caption contract, rebuild command, and review status.
- Audit the existing C07 overlays against the required semantics below before
  redrawing anything.
- Extend document QA to reject an active figure/table input that has no manifest
  row, prose reference, caption, or committed source asset.

**Gate**

- Every active new visual is vector/source-backed and traceable to one chapter.
- The manifest checker reports no missing source, input, caption, or reference.
- No legacy asset is deleted or relinked merely because it is absent from the
  new manifest.

### C14 — series map and analytic/algebraic visual set

**Commit**

```text
figures(iv-vi): add dependency, continuation, and scheme-language diagrams
```

**Targets**

- Add a compact series dependency map to each volume’s front matter. It must
  show chapter clusters, not a 256-node graph: V → VI, IV ↔ VI, VII → VIII, and
  the relevant I/II foundations.
- Review/extend the existing IV/14 and IV/23 C07 visuals into a paired branch
  cut/monodromy and path-lifting figure. Its caption must distinguish the slit
  plane from the covering surface and explain single-valuedness there.
- Review/extend the V/07, VI/07, and VI/13 overlays to cover localization and
  exactness, specialization in `Spec`, and sheaf gluing/stalks.
- Add an affine-contravariance/base-change square near VI/18–VI/24 and a
  base-field hypothesis matrix near VI/01–VI/11.

**Gate**

- All arrow directions and hypotheses are reviewed against the C04 theorem
  audit; the `Spec` and base-field figures make no false geometric implication.
- Each figure/table is referenced in the surrounding exposition and compiles in
  Volumes IV–VI.

### C15 — global and hyperbolic geometry visual set

**Commit**

```text
figures(vii): clarify exponential completeness and hyperbolic models
```

**Targets**

- Extend VII/23’s current visual with tangent-space radial geodesics, a normal
  neighborhood, cut behaviour, and an explicit local/geodesic/metric
  completeness distinction.
- Extend VII/31–VII/36 with an explicit Poincaré disk, upper-half-plane, and
  hyperboloid correspondence diagram, including model maps and geodesic forms.
- Keep the C07 assets where they already meet these contracts; add only the
  missing explanatory panels.

**Gate**

- The exponential-map caption states that `exp_p` need not be globally injective.
- Model transformations, signatures, and geodesic claims agree with Volume VII
  conventions and the C04 audit.

### C16 — computational pipeline and quantitative result tables

**Commit**

```text
repro(vii): add convergence metrics and rebuildable computational figures
```

**Targets**

- Extend `code/volume07/` rather than adding a parallel unversioned `repro/`
  tree. Preserve its fixed Python environment, deterministic seed, tests, and
  expected-output contract.
- Add a rebuildable VII/40 heat-method pipeline figure with the sign convention
  shown below the operator chain.
- Add a Laplacian-convention table for VII/40–41: smooth sign, stiffness-matrix
  sign, generalized eigenproblem, mass matrix, boundary condition, and API
  convention.
- Produce committed, machine-readable result tables for: heat-distance
  convergence; discrete-curvature validation on analytic surfaces; and
  ridge/valley robustness under resolution, scale, and noise sweeps.
- Add the corresponding VII/42 scale-stability figure from generated data.

**Metrics and limitations**

- Report resolution, characteristic edge length, time-step normalization,
  mean/max error, factorization/solve time, and boundary condition for heat
  experiments.
- Report L2/L-infinity curvature error and controlled-noise behaviour on each
  analytic reference surface.
- Report stable/false-positive feature length and displacement from reference
  loci for ridge/valley experiments.
- Name edge-graph paths as graph approximations, never as exact polyhedral
  geodesics.

**Gate**

- All tables and figures are regenerated from the frozen environment and match
  regression expectations.
- Each reported metric records its assumptions and has at least one analytic or
  controlled reference case.
- Volumes VII and the `code/volume07` test suite pass.

### C17 — figure/reproducibility release gate

**Commit**

```text
build(figures): verify visual assets, generated metrics, and archive readiness
```

**Deliverables**

- Add a single documented command sequence that rebuilds canonical PDFs,
  generated computational figures, metrics, indexes, and the archival manifest.
- Add checks for figure manifest completeness, stale generated outputs, missing
  visual assets, duplicate visual labels, and expected computational checksums.
- Add a POSIX shell wrapper only if it invokes the same canonical Python/TeX
  checks as `BUILD_ALL.ps1`; do not create a divergent second build system.
- Record software/version information in the existing archival metadata and
  citation-status record. Do not create `CITATION.cff` until verified
  author/editor metadata exists, consistent with C02 and C12.

**Gate**

- A clean checkout passes the full build and all visual/reproducibility checks.
- The archival manifest includes vector sources, generated data definitions,
  computational code, result tables, and final PDFs.
- No tag, DOI, or external archive deposit is created by this commit; those
  remain release-owner actions defined in `release/ARCHIVAL_WORKFLOW.md`.

### D1 — imported dossier reconciliation and canonical integration

**Commit**

```text
integrate(dossiers): reconcile fused imported sources into canonical books
```

**Purpose**

The `imports/` tree contains combined, fused textbook material: problem
dossiers, worked solutions, theory notes, figures, and several historical or
corrected copies. It is source material for the series, not an archival build
target. File names are not authoritative: some are topic-misnamed, and the
same payload occurs in multiple collections.

**Required workflow**

- Start from `reports/series/IMPORT_INTEGRATION_AUDIT.tsv`, deduplicate by
  content hash, and inspect the mathematical body rather than trusting an
  archive path or file name.
- Reconcile each distinct source block against the active chapter graph and
  `reports/series/DOSSIER_INDEX.tsv` / `DOSSIER_PROVENANCE_ATLAS.tsv`.
  Existing fused canonical material remains in place; it must not be copied a
  second time merely because a legacy source is present under `imports/`.
- Migrate verified missing problems, solutions, worked examples, theory
  explanations, and figures to their mathematical home under `books/`. Keep
  chapter-local source boundaries, labels, references, and pedagogy coherent.
- Where a source spans several topics, split it into chapter-local inputs
  rather than adding a monolithic legacy document or a new parallel book.
- Preserve source provenance in the canonical dossier ledger and record every
  disposition: already integrated, migrated, superseded duplicate, or requires
  mathematical review.

**Gate**

- Every distinct imported source has a recorded disposition and target (or an
  explicit mathematical-review finding); no collection is silently excluded.
- Each migrated dossier compiles in its canonical volume, has stable labels,
  and appears in the relevant book/edition table of contents where appropriate.
- The full canonical build, all available dossier editions, dossier-index
  validation, and document QA pass. The build must use the external G: output
  tree when local staging capacity is insufficient.

## Deliberate exclusions

Volumes IV–VI need source, proof, hypothesis, and citation traceability—not a
synthetic experimental-data repository. Their figures and tables are maintained
as canonical TeX/SVG assets with deterministic builds. Volume VII alone receives
the expanded numerical-result package because it contains computational claims
whose discretization and stability assumptions can be measured.

## Execution order

Run C13 first. C14 and C15 may proceed independently once the manifest contract
exists. C16 follows the C13 contract and feeds C17. C17 is the sole integration
and release-readiness gate.
