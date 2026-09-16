# MATH Series — C01–C12 Improvement Commit Reference

Status date: 2026-09-14  
Repository: `expert10000/math`  
Target branch: `main`

This file is the canonical working reference for the cross-series improvement program after the v1.3 release.

> **Normalization note.** The original review table referred in places to “all four volumes.” The active repository now contains the full **Volume I–VIII** series, so series-wide items below are interpreted across all eight volumes where applicable.

## Status legend

- ✅ **DONE / PUSHED** — completed on `main`
- ⏭ **NEXT** — recommended next commit
- ⬜ **TODO** — planned
- 🔒 **GATE** — must pass before the next priority tier

## Recommended execution order

| Order | ID | Priority | Commit | Status |
|---:|---|---|---|---|
| 1 | C01 | P0 | `fix(editorial): remove internal workflow artifacts from reader-facing text` | ✅ DONE / PUSHED |
| 2 | C02 | P0 | `docs(frontmatter): add authorship, provenance, rights, and scope` | ⏭ NEXT |
| 3 | C03 | P0 | `refs: add primary-source citations and chapter bibliographic notes` | ⬜ TODO |
| 4 | C04 | P0 | `fix(math): audit hypotheses, conventions, and theorem dependencies` | ⬜ TODO |
| 5 | C05 | P1 | `refactor(structure): standardize chapter scaffolding across the series` | ⬜ TODO |
| 6 | C06 | P1 | `refactor(pedagogy): replace template prose and prune repetitive exercises` | ⬜ TODO |
| 7 | C07 | P1 | `figures: add conceptual diagrams and convention tables` | ⬜ TODO |
| 8 | C08 | P1 | `build: add reproducible LaTeX build and document QA checks` | ⬜ TODO |
| 9 | C09 | P1 | `repro(vii): add executable computational-geometry validation package` | ⬜ TODO |
| 10 | C10 | P2 | `docs(index): add notation, theorem, subject, and cross-volume indexes` | ⬜ TODO |
| 11 | C11 | P2 | `style: perform final mathematical copy-edit and clarity pass` | ⬜ TODO |
| 12 | C12 | P3 | `release: add archival metadata, changelog, errata, and versioned DOI workflow` | ⬜ TODO |

---

# P0 — Publication blockers

## C01 — Reader-facing editorial cleanup

**Commit**

```text
fix(editorial): remove internal workflow artifacts from reader-facing text
```

**Status:** ✅ **DONE / PUSHED**

### Purpose

Remove repository-production language from the book while preserving genuine source lineage in formal editorial/provenance records.

### Completed scope

- Removed or renamed reader-visible workflow vocabulary such as:
  - `protected chapter`
  - `provenance ledger`
  - `canonical solved problem`
  - `mapped legacy manuscripts`
  - `Legacy Problem`
  - `Legacy-corpus boundary`
  - `corpus`
  - `dossier`
  - reconstruction/migration bookkeeping where it appeared as reader-facing exposition.
- Replaced production-oriented problem titles with mathematical titles.
- Replaced bookkeeping-only exercises/problems with actual mathematics where necessary.
- Preserved formal audit/source-migration/provenance material outside the reader-facing gate.
- Added an exhaustive reader-facing QA scan.
- Normalized modified TeX whitespace and EOF formatting.
- Passed `git diff --check`.
- Committed and pushed to `main`.

### Permanent rule

Reader-facing text should explain **mathematics, pedagogy, history, or scholarship**.  
Repository workflow belongs in **editorial, migration, provenance, audit, or release records**.

---

## C02 — Front matter, authorship, provenance, rights, and scope

**Commit**

```text
docs(frontmatter): add authorship, provenance, rights, and scope
```

**Priority:** P0  
**Recommended:** ⏭ **NEXT**

### Scope

Add or reconcile front matter for the full Volume I–VIII series:

- author/editor names;
- affiliations and ORCID where appropriate;
- edition/version;
- release date;
- intended audience;
- prerequisites;
- series scope;
- acknowledgments;
- copyright and license;
- recommended citation;
- contributor statement;
- funding/conflict statement where applicable;
- concise provenance statement;
- PDF metadata.

Add a formal **Source and provenance policy** explaining:

- what imported/legacy/source-derived material means;
- how source lineage is tracked;
- how originality and permissions are verified;
- where source ledgers live;
- why provenance workflow language is not repeated inside reader-facing problem statements.

### Important C01/C02 boundary

C01 removes inappropriate **presentation of provenance** from mathematical exposition.

C02 strengthens the **actual provenance apparatus**.

Do **not** undo C01 by reintroducing migration/corpus language into chapter prose.

### Suggested affected areas

```text
books/vol01_*/frontmatter/
books/vol02_*/frontmatter/
...
books/vol08_*/frontmatter/
editorial/
CITATION.cff
README.md
series metadata / PDF metadata configuration
```

### Acceptance gate

- every volume identifies author/editor/edition/date;
- every volume has audience + prerequisite + scope text;
- series-level provenance policy exists;
- citation metadata is internally consistent;
- PDF title/author/subject/keywords metadata is populated;
- no C01-banned workflow terminology returns to reader-facing chapters;
- `git diff --check` passes;
- all affected volumes build.

---

## C03 — Primary-source citations and bibliographic notes

**Commit**

```text
refs: add primary-source citations and chapter bibliographic notes
```

**Priority:** P0

### Scope

Create either:

1. one rigorously maintained bibliography per volume, or
2. one series bibliography with stable volume/chapter citation hooks.

Add short end-of-chapter sections such as:

```text
Sources and further reading
Historical notes
Primary references
```

### High-priority reference targets

- **Volume IV**
  - analytic continuation;
  - Riemann surfaces;
  - elliptic functions;
  - uniformization-related material where present.
- **Volume V**
  - Chs. 22–28 homological algebra;
  - foundational exact-sequence, derived-functor, Ext/Tor sources.
- **Volume VI**
  - FAC;
  - EGA;
  - Grothendieck-era scheme/sheaf/cohomology sources;
  - modern authoritative references for precise hypotheses.
- **Volume VII**
  - Riemannian geometry sources;
  - discrete differential geometry;
  - computational geometry;
  - VII/40: Crane–Weischedel–Wardetzky;
  - VII/41: primary discrete-operator literature.

### Rules

- cite primary literature for named modern algorithms;
- cite historical originals where attribution matters;
- use modern references for exact theorem statements when preferable;
- avoid presenting recent algorithms as folklore;
- keep historical attribution separate from theorem-correctness sourcing.

### Acceptance gate

- no major named modern method remains uncited;
- chapter bibliographic notes exist for all chapters that introduce nontrivial historical/modern results;
- all citations resolve;
- no unused/broken bibliography keys;
- clean build with zero unresolved citation warnings.

---

## C04 — Mathematical hypotheses, conventions, and dependency audit

**Commit**

```text
fix(math): audit hypotheses, conventions, and theorem dependencies
```

**Priority:** P0  
**Role:** 🔒 **P0 correctness gate**

### Deliverable

Create a theorem-audit sheet with columns such as:

| Field | Meaning |
|---|---|
| Volume/chapter | theorem location |
| Statement | short theorem identifier |
| Hypotheses | all assumptions actually needed |
| Convention | sign/grading/base-field/etc. |
| Dependencies | earlier lemmas/theorems |
| Failure mode | counterexample or issue if assumptions are dropped |
| Authoritative reference | source used for verification |
| Status | PASS / FIX / REVIEW |

### Volume-specific audit

#### Volume IV — Complex Analysis

Audit:

- branch choices;
- logarithm/root conventions;
- contour orientation;
- winding-number sign;
- residue conventions;
- compactification/genus hypotheses;
- lattice and elliptic-function normalization.

#### Volume V — Commutative Algebra / Homological Methods

Standardize:

- homological vs cohomological grading;
- differential degree;
- sign conventions;
- connecting morphisms;
- left/right module conventions;
- tensor/Hom variance;
- Ext/Tor conventions.

#### Volume VI — Algebraic Geometry

Audit especially:

- field-dependent claims in early chapters;
- rational points vs closed points;
- maximal ideals over non-algebraically-closed fields;
- finite-field behavior;
- algebraic closure assumptions;
- geometric irreducibility;
- sheaf epimorphism vs sectionwise surjectivity;
- quasi-coherent/coherent hypotheses;
- qcqs assumptions;
- base-change/cohomology statements.

**Negative tests are mandatory:** ask whether each claim survives a change of base field or removal of a stated hypothesis.

#### Volume VII — Differential / Riemannian / Computational Geometry

Add a convention table covering:

- Riemann tensor sign;
- sectional/Gaussian curvature sign;
- shape operator sign;
- mean curvature convention;
- Laplace/Laplace–Beltrami sign;
- Riemannian vs Lorentzian signature where applicable.

Also audit:

- Hopf–Rinow forward references;
- boundary conditions;
- mesh discretization assumptions;
- convergence conditions;
- numerical stability assumptions.

### Acceptance gate

- theorem-audit sheet committed;
- every P0 theorem issue resolved or explicitly tracked;
- all “later” claims corresponding to Hopf–Rinow are resolved;
- convention tables are authoritative and cross-referenced;
- targeted negative tests pass;
- all affected volumes build.

---

# P1 — Structural, pedagogical, visual, and reproducibility quality

## C05 — Standardize chapter scaffolding

**Commit**

```text
refactor(structure): standardize chapter scaffolding across the series
```

**Priority:** P1

### Chapter contract

Use one explicit series-wide contract:

```text
Prerequisites
→ Learning outcomes
→ Core exposition
→ Examples
→ Exercises
→ Solved problems
→ Challenge problems
→ Chapter-specific summary
→ Sources and further reading
→ Bridge forward
```

### Scope

- eliminate accidental differences caused by separate reconstruction/review passes;
- add missing chapter roadmaps where useful;
- add part introductions explaining conceptual dependencies;
- make section naming consistent;
- preserve mathematically justified exceptions rather than enforcing mechanical uniformity.

### Acceptance gate

- chapter-structure audit reports no unexplained structural outliers;
- every exception is intentional;
- chapter navigation is consistent;
- builds pass.

---

## C06 — Replace template prose and prune repetitive exercises

**Commit**

```text
refactor(pedagogy): replace template prose and prune repetitive exercises
```

**Priority:** P1

### Scope

Remove repeated stock prose such as:

- “canonical solved layer”;
- “canonical complex-analysis chain”;
- generic “carry out the chapter's main method” prompts.

Rewrite chapter summaries around **3–5 concrete mathematical takeaways**.

Rewrite solved-problem structure toward:

```text
hypotheses
→ key lemma/mechanism
→ computation/proof
→ failure mode / boundary of applicability
```

Prune exercises that merely duplicate adjacent examples.

### Preserve

- easy/intermediate/hard progression;
- proof practice;
- computational fluency;
- conceptual counterexamples;
- representative challenge problems.

### Acceptance gate

- no repeated template-summary sentence across chapters unless mathematically intentional;
- no obvious duplicated exercise shell;
- every chapter retains balanced exercise difficulty;
- exercise/solution labels remain paired;
- builds pass.

---

## C07 — Conceptual diagrams and convention tables

**Commit**

```text
figures: add conceptual diagrams and convention tables
```

**Priority:** P1

### Candidate figures

- branch cuts and monodromy;
- localization maps and exactness;
- `Spec` specialization;
- sheaf restriction/gluing;
- tangent/exponential-map geometry;
- geodesics;
- hyperbolic models;
- bundle clutching;
- mesh heat flow;
- discrete operators;
- ridge extraction.

### Candidate tables

- notation;
- sign conventions;
- theorem hypotheses;
- equivalent definitions;
- continuous vs discrete operators;
- model comparisons.

### Figure rule

A figure must explain a mathematical relationship.

Avoid decorative figures that merely duplicate an equation.

### Acceptance gate

- figures use consistent style and typography;
- every figure has an explanatory caption;
- every figure is referenced in prose;
- source/vector asset is retained;
- no broken image references;
- builds pass.

---

## C08 — Reproducible LaTeX build and document QA

**Commit**

```text
build: add reproducible LaTeX build and document QA checks
```

**Priority:** P1

### Scope

Add deterministic build instructions and automation:

- `latexmkrc`, Makefile, or canonical series build wrapper;
- TeX engine/version record;
- package/environment record;
- clean-checkout build instructions;
- build logs and failure summaries.

Add QA for:

- unresolved references;
- unresolved citations;
- duplicated labels;
- duplicate problem/exercise numbers;
- undefined notation where detectable;
- missing bibliography entries;
- reader-facing workflow vocabulary;
- stale “later/previously” references;
- missing assets;
- unexpected build outputs;
- deterministic artifact naming.

### Acceptance gate

A clean checkout must be able to build the full Volume I–VIII series with one documented command or one documented command sequence and no manual source edits.

---

## C09 — Executable computational-geometry validation package

**Commit**

```text
repro(vii): add executable computational-geometry validation package
```

**Priority:** P1

### Target

Volume VII computational chapters, especially VII/38–42.

### Scope

Implement and validate the algorithms underlying the exposition.

Include:

- fixed dependency/environment specification;
- generated benchmark meshes;
- analytic reference cases;
- boundary-condition cases;
- scale/noise/resolution sweeps;
- regression outputs;
- figure rebuild scripts;
- deterministic seeds;
- expected error bounds;
- software citations.

### Suggested layout

```text
code/volume07/
  README.md
  environment.*
  meshes/
  analytic_cases/
  experiments/
  figures/
  tests/
  expected/
```

### Acceptance gate

- every computational chapter has at least one executable representative;
- all examples run in the frozen environment;
- expected outputs are regression-tested;
- figures can be regenerated;
- runtime and numerical assumptions are documented.

---

# P2 — Navigation and final editorial polish

## C10 — Notation, theorem, subject, and cross-volume indexes

**Commit**

```text
docs(index): add notation, theorem, subject, and cross-volume indexes
```

**Priority:** P2

### Add

- notation/symbol index;
- theorem-name index;
- subject index;
- cross-volume prerequisite map;
- cross-volume continuation map.

### Important bridges

- IV → VI: complex geometry / analytic-to-algebraic links;
- V → VI: commutative algebra / homological prerequisites;
- VII → VIII: bundles, differential geometry, topology;
- I → later volumes: linear algebra, spectral and chain-complex foundations.

### Programmatic checks

Resolve:

- `later`;
- `previously`;
- `as shown above`;
- `in a later chapter`;
- obsolete chapter/section references.

### Acceptance gate

- all generated indexes build;
- no stale forward/backward references;
- cross-volume maps point to real chapters/sections;
- terminology is index-consistent.

---

## C11 — Final mathematical copy-edit and clarity pass

**Commit**

```text
style: perform final mathematical copy-edit and clarity pass
```

**Priority:** P2  
**Timing:** only after C01–C10

### Scope

Enforce consistency in:

- terminology;
- theorem-name capitalization;
- punctuation;
- mathematical typography;
- notation introduction;
- voice;
- paragraph length;
- display-equation integration;
- definition/proof transitions.

Remove low-information prose such as unnecessary announcements of obvious transitions.

Break dense paragraphs where doing so clarifies mathematical dependency.

### Acceptance gate

- no structural edits remain pending;
- no new mathematical claims are introduced casually during copy-edit;
- style/lint checks pass;
- all volumes build;
- representative visual PDF review passes.

---

# P3 — Archival release engineering

## C12 — Archival metadata, changelog, errata, and versioned DOI workflow

**Commit**

```text
release: add archival metadata, changelog, errata, and versioned DOI workflow
```

**Priority:** P3  
**Timing:** after content stabilization

### Add

- `CHANGELOG.md`;
- release number/date;
- errata policy;
- issue/reporting route;
- citation metadata;
- release manifest;
- source/PDF checksums;
- exact build-environment record;
- archival deposit instructions;
- version-specific identifier/DOI workflow where supported;
- release tag procedure.

### Archive together

For every release archive exactly:

```text
source
scripts
code
data / generated benchmark definitions
bibliography
figures
PDFs
manifest
checksums
environment metadata
```

### Acceptance gate

- release is reproducible from archived source;
- manifest covers every published artifact;
- checksums match;
- version/date/citation metadata agree everywhere;
- release tag points to the exact canonical commit;
- errata process is documented.

---

# Cross-commit rules

## 1. Preserve provenance without exposing production workflow

Formal lineage belongs in:

```text
editorial/
reports/
source-migration ledgers
provenance records
release manifests
bibliographic notes where historically relevant
```

It should not appear as repository bookkeeping inside mathematical exercises, solutions, headings, or summaries.

## 2. Prefer mathematics over mechanical renaming

If a reader-facing exercise exists only to test repository workflow, do not merely rename it.

Replace it with a mathematically appropriate exercise occupying the same conceptual slot.

## 3. Each commit gets its own QA gate

Minimum:

```text
git status --short
git diff --check
targeted audit/validator
affected-volume build
git diff --stat
```

For series-wide structural changes, also run the full series gate before push when practical.

## 4. Do not mix priority layers

- finish **P0** correctness/scholarly-integrity work before major stylistic rewriting;
- finish **P1** structural/reproducibility work before the final copy-edit;
- perform **P3** release engineering only after manuscript stabilization.

## 5. Mathematical-audit negative tests are required

For theorem/hypothesis audits, explicitly ask:

```text
What fails if this hypothesis is removed?
What changes over a non-algebraically-closed field?
What changes in positive characteristic?
What changes at the boundary?
What changes under a different sign/grading convention?
```

A theorem that is only “probably correct” is not considered audited.

---

# Immediate continuation

The natural next commit is:

```text
C02
docs(frontmatter): add authorship, provenance, rights, and scope
```

After C02 passes, continue in order with C03 and C04 to close the P0 publication gate before starting the P1 structural/pedagogical work.

