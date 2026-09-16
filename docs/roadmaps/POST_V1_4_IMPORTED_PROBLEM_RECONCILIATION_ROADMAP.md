# Post-v1.4 Imported Problem / Dossier Reconciliation Roadmap

**Status:** Draft for review  
**Target repository:** `expert10000/math`  
**Branch:** `main`  
**Purpose:** Establish a complete, auditable, problem-centric inventory of legacy/imported TeX material, reconcile it against the canonical Volumes I–VIII, then migrate only genuinely missing or intentionally retained problem variants.

---

## 0. Release sequencing

The dossier/import program begins **only after the v1.4 release is complete and frozen**.

The intended sequence is:

```text
continue current Volume I–VIII work
        ↓
complete v1.4 release candidate
        ↓
run full series release gates
        ↓
tag / freeze v1.4 canonical baseline
        ↓
begin imported-source / dossier reconciliation
        ↓
freeze semantic PROBLEM_LEDGER
        ↓
migrate missing problems volume by volume
        ↓
reconcile / rebuild / freeze post-import corpus
```

This separation is intentional.

The v1.4 release should represent the clean canonical series **before** the large imported-problem reconciliation.  
The import program can then compare every legacy problem against a fixed and reproducible baseline.

---

# Phase A — complete and freeze the v1.4 baseline

## P01

```text
release(series): complete and freeze v1.4 canonical baseline before import reconciliation
```

### Important sequencing rule

P01 is **not yet ready to close**.

Before this commit/release is finalized, continue the remaining planned work for the current series and bring Volume I–VIII to the intended v1.4 state.

Only after that work is complete:

- run final Volume I–VIII build/release gates;
- verify a clean Git state;
- refresh release manifests and hashes;
- record canonical chapter/problem/solution counts;
- record the exact baseline commit;
- create/tag the v1.4 release;
- preserve the baseline used for every later import comparison.

### Expected outputs

```text
docs/releases/V1.4_BASELINE.md
editorial/release/V1.4_MANIFEST.tsv
editorial/release/V1.4_HASHES.tsv
```

### Baseline invariant

After P01 is closed, every imported problem can be answered against a fixed question:

> Was this mathematical problem already represented in the canonical books at v1.4?

**Dossier/import work begins after this point.**

---

# Phase B — normalize the imported source corpus

## P02

```text
refactor(imports): create canonical imported-source corpus
```

Create a clean working corpus without modifying the historical source directories.

Suggested structure:

```text
imports/PROBLEM_CORPUS/
    sources/
    companions/
    metadata/
    build/
    reports/
```

### Tasks

- collect all relevant `.tex` sources;
- preserve source collection and relative path information;
- preserve companion files;
- do not flatten filenames into a single directory;
- keep the original import directories untouched;
- record checksums so copied/normalized material remains traceable.

No canonical book content changes in this commit.

---

## P03

```text
audit(imports): inventory TeX roots includes and companion assets
```

Create:

```text
imports/PROBLEM_CORPUS/metadata/SOURCE_FILES.tsv
imports/PROBLEM_CORPUS/metadata/DEPENDENCIES.tsv
imports/PROBLEM_CORPUS/metadata/COMPANION_FILES.tsv
```

Recommended source fields:

```text
source_id
source_collection
original_path
corpus_path
sha256
size_bytes
probable_root
included_by
includes
bibliography
figures
styles
other_dependencies
```

This becomes the authoritative **file-level inventory**.

---

## P04

```text
audit(imports): detect duplicate and variant source documents
```

Classify source relations such as:

```text
UNIQUE
EXACT_DUPLICATE
NEAR_DUPLICATE
OLDER_VARIANT
NEWER_VARIANT
DERIVED_COPY
UNKNOWN_RELATION
```

Create:

```text
imports/PROBLEM_CORPUS/metadata/SOURCE_RELATIONS.tsv
imports/PROBLEM_CORPUS/reports/source_duplicate_report.md
```

Do not delete duplicate sources at this stage. Preserve provenance.

---

# Phase C — determine what can actually be built

## P05

```text
build(imports): add isolated legacy TeX build harness
```

Add tooling such as:

```text
scripts/imports/build_problem_corpus.py
scripts/imports/build_one_source.py
```

Requirements:

- identify probable standalone document roots;
- build each candidate independently;
- use isolated build directories;
- never rewrite original imported sources;
- capture command, exit status, stdout/stderr and TeX logs;
- tolerate missing packages and incomplete source trees.

---

## P06

```text
audit(imports): record compile status for imported documents
```

Create:

```text
imports/PROBLEM_CORPUS/metadata/BUILD_STATUS.tsv
imports/PROBLEM_CORPUS/reports/build_summary.md
```

Canonical statuses:

```text
BUILD_OK
BUILD_WARNINGS
BUILD_FAILED
NOT_STANDALONE
INCLUDE_ONLY
MISSING_DEPENDENCY
UNSUPPORTED_LEGACY_SETUP
```

### Rule

Compilation success is useful metadata, **not an admission criterion**.

A broken legacy document may still contain valuable problems and solutions and must still be indexed.

---

# Phase D — discover every problem-like object

## P07

```text
feat(imports): add structural scanner for legacy problem content
```

Detect standard and nonstandard constructs, including:

```latex
\begin{problem}
\begin{exercise}
\begin{example}
\begin{solution}
\section{Problems}
\subsection{Exercises}
Problem 4.
Exercise 7.
Solution.
```

Also inspect:

- problems;
- exercises;
- worked examples;
- proof exercises;
- hints;
- solutions;
- problem sets;
- dossiers;
- theorem/proof blocks that are functioning as exercises;
- hand-written/non-environment problem numbering.

The scanner should locate candidates, not decide canonical placement.

---

## P08

```text
audit(imports): create raw problem discovery inventory
```

Create:

```text
imports/problem_inventory/RAW_PROBLEM_ITEMS.tsv
```

Assign every discovered object a stable permanent ID, for example:

```text
IMP-DL-000012-P001
IMP-M2-000044-P007
IMP-M3-000091-P003
```

Recommended fields:

```text
problem_id
source_id
source_file
start_line
end_line
source_number
source_heading
detected_type
statement_text_hash
has_hint
has_solution
solution_location
figure_references
confidence
```

### Gate

Every problem-like object discovered in the corpus must receive an ID.

---

## P09

```text
audit(imports): recover detached hints solutions and companion material
```

Handle cases where:

- problems and solutions are stored in separate files;
- solutions occur much later in the same document;
- numbering differs between statement and answer sections;
- one solution file serves another source;
- figures are stored elsewhere;
- hints and answers are detached from statements.

Create:

```text
imports/PROBLEM_CORPUS/metadata/PROBLEM_SOLUTION_LINKS.tsv
imports/PROBLEM_CORPUS/metadata/PROBLEM_COMPANIONS.tsv
imports/PROBLEM_CORPUS/reports/orphan_solutions.md
imports/PROBLEM_CORPUS/reports/orphan_problems.md
```

---

# Phase E — semantic indexing

## P10

```text
feat(imports): classify imported problems by mathematical subject
```

Add semantic metadata based on **actual mathematical content**, not filenames.

Suggested fields:

```text
primary_subject
secondary_subject
keywords
mathematical_objects
methods
difficulty
problem_kind
```

Examples:

```text
linear algebra / spectral theorem
real analysis / weak convergence
Fourier analysis / transform methods
PDE / elliptic equations
algebra / modules
algebraic geometry / affine schemes
differential geometry / curvature
algebraic topology / homology
```

### Core rule

A filename is evidence only.  
Volume/chapter placement must be determined from problem content.

---

## P11

```text
audit(imports): assign imported problems to Volume I-VIII
```

Assign every in-scope problem to a target volume.

Allowed exceptional statuses:

```text
OUT_OF_SERIES
MULTI_VOLUME
UNCLASSIFIED
NON_MATHEMATICAL
NOT_A_PROBLEM
```

Create:

```text
imports/problem_inventory/VOLUME_ASSIGNMENT.tsv
imports/PROBLEM_CORPUS/reports/unassigned_problem_items.md
```

### Gate

Before the final inventory freeze:

```text
UNCLASSIFIED = 0
```

Every item must have an explicit disposition.

---

## P12

```text
audit(imports): assign imported problems to canonical chapters and sections
```

Add:

```text
target_volume
target_chapter
target_section
assignment_confidence
assignment_reason
```

Allow explicit exceptional dispositions:

```text
CHAPTER_LEVEL_ONLY
NEEDS_NEW_SECTION
CROSS_CHAPTER
```

No usable problem should remain without a documented canonical destination or documented reason for exclusion.

---

# Phase F — compare against the v1.4 canonical books

## P13

```text
feat(imports): add canonical problem fingerprint index
```

Index all canonical problems in the v1.4 Volume I–VIII baseline.

Create:

```text
editorial/problem_index/CANONICAL_PROBLEMS.tsv
```

Recommended fields:

```text
canonical_problem_id
volume
chapter
section
label
title
statement_hash
solution_hash
keywords
source_provenance
```

This is the canonical side of the reconciliation.

---

## P14

```text
audit(imports): detect exact imported-to-canonical problem matches
```

Classify matches such as:

```text
EXACT_MATCH
NORMALIZED_TEXT_MATCH
SAME_STATEMENT
SAME_STATEMENT_DIFFERENT_SOLUTION
```

Populate:

```text
canonical_problem_id
canonical_location
```

No migration should occur for obvious already-canonical duplicates.

---

## P15

```text
audit(imports): detect near-duplicate and mathematical-variant problems
```

Human-review classifications:

```text
NEAR_DUPLICATE
NOTATION_VARIANT
PARAMETER_VARIANT
STRONGER_VERSION
WEAKER_VERSION
SAME_METHOD_DIFFERENT_DATA
RELATED_BUT_DISTINCT
```

Create:

```text
imports/PROBLEM_CORPUS/reports/near_duplicate_review.md
imports/problem_inventory/DUPLICATE_GROUPS.tsv
```

### Rule

Mathematical variants must not be automatically discarded simply because textual similarity is high.

---

## P16

```text
audit(imports): reconcile imported solutions against canonical solutions
```

Detect cases such as:

```text
problem migrated but solution missing
problem migrated with weaker solution
same problem with a second useful solution
legacy solution more complete than canonical solution
canonical solution exists but provenance is absent
canonical problem combines multiple legacy sources
```

Create:

```text
imports/problem_inventory/SOLUTION_RECONCILIATION.tsv
```

---

# Phase G — establish the master semantic ledger

## P17

```text
docs(imports): create canonical imported-problem ledger
```

Create the authoritative problem-centric ledger:

```text
imports/problem_inventory/PROBLEM_LEDGER.tsv
```

Recommended schema:

```text
problem_id
source_id
source_collection
source_file
source_location
source_problem_number
source_heading

problem_type
primary_subject
secondary_subject
keywords

has_hint
has_solution
solution_id
has_figures
companion_files

source_build_status

duplicate_group
canonical_match_type
canonical_problem_id
canonical_volume
canonical_chapter

target_volume
target_chapter
target_section
mapping_confidence

migration_status
migration_commit
review_status

notes
```

This ledger becomes the central authority for imported problem material.

---

## P18

```text
audit(imports): classify every imported problem disposition
```

Every discovered problem receives one explicit disposition:

```text
ALREADY_CANONICAL
CANONICAL_WITH_VARIANT
MISSING_FROM_CANONICAL
MISSING_SOLUTION
BETTER_LEGACY_SOLUTION
DUPLICATE_SOURCE
OUT_OF_SERIES
NOT_A_PROBLEM
REJECTED
NEEDS_EDITORIAL_REVIEW
```

No blank disposition is allowed.

---

## P19

```text
audit(imports): eliminate unresolved problem and source records
```

Hard reconciliation checks:

```text
unindexed problem-like objects      = 0
unassigned in-scope problems        = 0
unknown source provenance           = 0
orphan solutions unexplained        = 0
missing companion references        = 0
unresolved duplicate groups         = 0
```

Items requiring genuine human judgment may remain:

```text
NEEDS_EDITORIAL_REVIEW
```

but must be explicitly registered.

---

## P20

```text
release(imports): freeze imported-problem inventory v1
```

Create:

```text
imports/problem_inventory/FREEZE_MANIFEST.tsv
imports/problem_inventory/FREEZE_HASHES.tsv
imports/problem_inventory/INVENTORY_SUMMARY.md
```

The summary should report actual counts for:

```text
source TeX files
probable document roots
buildable documents
problem-like objects
problems
worked examples
hints
solutions
canonical matches
near duplicates
new candidate problems
Volume distribution
chapter distribution
unresolved editorial-review items
```

### Milestone

P20 marks:

> **Imported dossier/problem discovery and reconciliation complete.**

Only after this freeze do we begin changing canonical book content.

---

# Phase H — migrate genuinely missing material

## P21

```text
content(v1): migrate remaining indexed Volume I problems
```

For every migrated problem:

- canonical `Problem`;
- canonical `Solution` where available;
- stable label;
- provenance entry;
- `PROBLEM_LEDGER.tsv` update;
- `migration_commit` recorded;
- build/test chapter.

---

## P22

```text
content(v2): migrate remaining indexed Volume II problems
```

Same rules.

Split by chapter ranges if the candidate set is large.

---

## P23

```text
content(v3): migrate remaining indexed Volume III problems
```

---

## P24

```text
content(v4): migrate remaining indexed Volume IV problems
```

---

## P25

```text
content(v5): migrate remaining indexed Volume V problems
```

---

## P26

```text
content(v6): migrate remaining indexed Volume VI problems
```

---

## P27

```text
content(v7): migrate remaining indexed Volume VII problems
```

---

## P28

```text
content(v8): migrate remaining indexed Volume VIII problems
```

### Migration rule

If a volume contains many candidates, replace a single volume-wide commit with chapter-range commits.

The ledger remains the authority for determining which problems have actually been migrated.

---

# Phase I — post-migration reconciliation

## P29

```text
audit(series): reconcile imported-problem ledger after canonical migration
```

Expected terminal dispositions:

```text
ALREADY_CANONICAL
MIGRATED
INTENTIONALLY_RETAINED_VARIANT
OUT_OF_SERIES
REJECTED_WITH_REASON
```

Target:

```text
MISSING_FROM_CANONICAL = 0
```

unless a deliberately deferred set is explicitly documented.

---

## P30

```text
test(series): validate imported-problem provenance and solution pairing
```

Automated checks should verify:

- every migrated problem has provenance;
- every promised solution exists;
- problem/solution labels are unique;
- no duplicate problem IDs;
- no dangling source IDs;
- all target Volume/chapter references are valid;
- no unexplained source references;
- every migrated item records its migration commit;
- every canonical/problem-ledger relationship is internally consistent.

---

## P31

```text
build(series): rebuild Volumes I-VIII after imported-problem migration
```

Run all eight canonical builds.

Record:

```text
build result
page count
problem count
solution count
warnings
cross-reference status
```

No volume should be frozen from a partial build.

---

## P32

```text
audit(series): run cross-volume duplicate and placement review
```

Check for:

- accidental cross-volume duplicates;
- inappropriate chapter placement;
- repeated variants that should instead cross-reference one another;
- advanced problems accidentally inserted into introductory sections;
- inconsistent terminology/notation introduced by migration.

---

## P33

```text
docs(series): publish imported-problem provenance summary
```

Create a maintainers' provenance document, for example:

```text
docs/provenance/IMPORTED_PROBLEM_CORPUS.md
```

Document:

- source collections;
- normalization procedure;
- stable source/problem identifiers;
- duplicate policy;
- canonical mapping procedure;
- relationship between imported IDs and canonical problem IDs;
- rejection/deferment policy.

### Editorial rule

Internal production language should remain in provenance/audit documentation, not leak into reader-facing mathematical prose.

---

## P34

```text
release(series): freeze post-import canonical problem corpus
```

Refresh and freeze:

```text
PROBLEM_LEDGER.tsv
CANONICAL_PROBLEMS.tsv
SOURCE_FILES.tsv
SOURCE_RELATIONS.tsv
FREEZE_MANIFEST.tsv
FREEZE_HASHES.tsv
series release manifest
```

This establishes the next canonical baseline after imported problem migration.

---

# Program gates

The project has four major gates.

## Gate 1 — v1.4 release

Required before any dossier work begins:

```text
v1.4 content complete
all Volume I-VIII release checks pass
all canonical PDFs build
release manifests refreshed
release hashes refreshed
baseline commit fixed
v1.4 tagged/released
```

---

## Gate 2 — source corpus complete

After P09:

```text
all relevant TeX files represented
source provenance known
dependencies/companions indexed
build status recorded
every detected problem-like object has stable ID
```

---

## Gate 3 — semantic inventory freeze

After P20:

```text
every problem classified
every in-scope problem assigned to Volume
every in-scope problem assigned to chapter/section or explicit exception
canonical duplicate comparison complete
solutions reconciled
every problem has explicit disposition
inventory hashes frozen
```

No canonical problem migration should begin before this gate.

---

## Gate 4 — post-import canonical freeze

After P34:

```text
all accepted missing problems migrated
all ledgers reconciled
all provenance links valid
all solution pairings valid
all eight volumes build
cross-volume duplicate audit passes
post-import hashes frozen
```

---

# Commit sequence summary

```text
P01  release(series): complete and freeze v1.4 canonical baseline before import reconciliation

P02  refactor(imports): create canonical imported-source corpus
P03  audit(imports): inventory TeX roots includes and companion assets
P04  audit(imports): detect duplicate and variant source documents

P05  build(imports): add isolated legacy TeX build harness
P06  audit(imports): record compile status for imported documents

P07  feat(imports): add structural scanner for legacy problem content
P08  audit(imports): create raw problem discovery inventory
P09  audit(imports): recover detached hints solutions and companion material

P10  feat(imports): classify imported problems by mathematical subject
P11  audit(imports): assign imported problems to Volume I-VIII
P12  audit(imports): assign imported problems to canonical chapters and sections

P13  feat(imports): add canonical problem fingerprint index
P14  audit(imports): detect exact imported-to-canonical problem matches
P15  audit(imports): detect near-duplicate and mathematical-variant problems
P16  audit(imports): reconcile imported solutions against canonical solutions

P17  docs(imports): create canonical imported-problem ledger
P18  audit(imports): classify every imported problem disposition
P19  audit(imports): eliminate unresolved problem and source records
P20  release(imports): freeze imported-problem inventory v1

P21  content(v1): migrate remaining indexed Volume I problems
P22  content(v2): migrate remaining indexed Volume II problems
P23  content(v3): migrate remaining indexed Volume III problems
P24  content(v4): migrate remaining indexed Volume IV problems
P25  content(v5): migrate remaining indexed Volume V problems
P26  content(v6): migrate remaining indexed Volume VI problems
P27  content(v7): migrate remaining indexed Volume VII problems
P28  content(v8): migrate remaining indexed Volume VIII problems

P29  audit(series): reconcile imported-problem ledger after canonical migration
P30  test(series): validate imported-problem provenance and solution pairing
P31  build(series): rebuild Volumes I-VIII after imported-problem migration
P32  audit(series): run cross-volume duplicate and placement review
P33  docs(series): publish imported-problem provenance summary
P34  release(series): freeze post-import canonical problem corpus
```

---

# Guiding principles

1. **Finish v1.4 first.**
2. **Never infer mathematical content from filenames alone.**
3. **Keep original imports immutable.**
4. **Preserve source provenance through every transformation.**
5. **Index every problem before migrating any problem.**
6. **Treat compilation status as metadata, not a filter.**
7. **Compare against a fixed v1.4 baseline.**
8. **Distinguish exact duplicates from worthwhile mathematical variants.**
9. **Keep discovery, classification, reconciliation and migration as separate stages.**
10. **Every imported item must end with a documented disposition.**
11. **The problem ledger, not filenames or memory, becomes the canonical migration authority.**
12. **Rebuild and freeze the entire series only after reconciliation is complete.**

---

# Final intended lifecycle

```text
CURRENT SERIES WORK
        │
        ▼
      v1.4
        │
        │ fixed canonical baseline
        ▼
SOURCE CORPUS
        │
        ▼
PROBLEM DISCOVERY
        │
        ▼
SOLUTION / COMPANION LINKING
        │
        ▼
SEMANTIC CLASSIFICATION
        │
        ▼
VOLUME + CHAPTER ASSIGNMENT
        │
        ▼
v1.4 CANONICAL COMPARISON
        │
        ▼
PROBLEM_LEDGER v1
        │
        │ inventory freeze
        ▼
V1 → V8 MIGRATION
        │
        ▼
SERIES RECONCILIATION
        │
        ▼
V1–V8 REBUILD
        │
        ▼
POST-IMPORT CANONICAL FREEZE
```

