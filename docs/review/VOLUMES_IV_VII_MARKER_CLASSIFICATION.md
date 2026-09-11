# Volumes IV–VII marker classification

Baseline before cleanup: `331aaaa76323d67f06fc94639bccb0cde9bdf543`

Only full-line TeX comments were eligible for removal. No rendered prose, mathematics, theorem statement, label, exercise, hint, or solution line was rewritten.

- marker comments classified: **2425**
- obsolete pure-comment markers removed: **32**
- active marker comments retained: **2393**

## Families

- `Editorial provenance` — keep 0, remove 1
- `Legacy provenance` — keep 1, remove 0
  - active consumers: `scripts/volume02/audit_pedagogy.py`, `scripts/volume03/common_volume03.py`, `scripts/volume04/common_volume04.py`, `scripts/volume05/common_volume05.py`
- `PEDAGOGY-ENRICHED-VI` — keep 429, remove 0
  - active consumers: `scripts/volume06/audit_pedagogy.py`, `scripts/volume06/enrich_hints.py`, `scripts/volume07/audit_pedagogy.py`, `scripts/volume07/enrich_hints.py`
- `PEDAGOGY-ENRICHED-VII` — keep 1008, remove 0
  - active consumers: `scripts/volume07/audit_pedagogy.py`, `scripts/volume07/enrich_hints.py`
- `SOURCE_MIGRATION.tsv` — keep 1, remove 0
  - active consumers: `books/vol01_linear_algebra/freeze/freeze_volume01.py`, `books/vol01_linear_algebra/reconciliation/reconcile_volume01.py`, `books/vol08_algebraic_topology/reconciliation/VOLUME08_RECONCILIATION_MANIFEST.json`, `books/vol08_algebraic_topology/reconciliation/reconcile_volume08.py`, `editorial/provenance/vol3.yaml`, `release/theory_of_mathematics_i_viii_v1.0/RELEASE.json`, `scripts/series/audit_reviewed_freezes_i_viii.py`, `scripts/series/build_i_viii_release_bundle.py`, `scripts/series/generate_release_dashboard.py`, `scripts/series/reconcile_i_viii_release.py`, `scripts/volume01/add_volume01_dossiers.py`, `scripts/volume01/scaffold_volume01.py`, `scripts/volume02/audit_full_volume02.py`, `scripts/volume02/audit_i08_i12.py`, `scripts/volume02/common_volume02.py`, `scripts/volume02/generate_i01_i07.py`, `scripts/volume02/generate_i08_i12.py`, `scripts/volume02/generate_i13_i25.py`, `scripts/volume03/audit_full_volume03.py`, `scripts/volume03/audit_volume03_stage.py`, `scripts/volume03/generate_volume03_batch.py`, `scripts/volume04/audit_full_volume04.py`, `scripts/volume04/audit_volume04_stage.py`, `scripts/volume04/generate_volume04_batch.py`, `scripts/volume05/audit_full_volume05.py`, `scripts/volume05/audit_volume05_stage.py`, `scripts/volume05/generate_volume05_batch.py`
- `Status: DRAFTED` — keep 6, remove 0
  - active consumers: `books/vol01_linear_algebra/freeze/freeze_volume01.py`, `books/vol01_linear_algebra/reconciliation/reconcile_volume01.py`, `books/vol08_algebraic_topology/freeze/AUDIT_VOLUME08_FREEZE.py`, `build/vol03-review/finalize_evidence.py`, `reports/vol03/VOL03_REMAINING_MATH_REPAIRS.json`, `reports/vol03/verify_review.py`, `scripts/series/audit_i_viii.py`, `scripts/series/generate_navigation.py`, `scripts/series/generate_release_dashboard.py`, `scripts/volume01/add_volume01_dossiers.py`, `scripts/volume01/generate_volume01_chapters.py`, `scripts/volume02/audit_full_volume02.py`, `scripts/volume02/audit_i01_i07.py`, `scripts/volume02/audit_i08_i12.py`, `scripts/volume02/common_volume02.py`, `scripts/volume02/generate_i01_i07.py`, `scripts/volume03/audit_full_volume03.py`, `scripts/volume03/audit_volume03_stage.py`, `scripts/volume03/common_volume03.py`, `scripts/volume04/audit_full_volume04.py`, `scripts/volume04/audit_volume04_stage.py`, `scripts/volume04/common_volume04.py`, `scripts/volume05/audit_full_volume05.py`, `scripts/volume05/audit_volume05_stage.py`, `scripts/volume05/common_volume05.py`
- `VOL04-EXPANSION` — keep 248, remove 0
  - active consumers: `scripts/volume04/audit_example_exercise_balance.py`, `scripts/volume04/audit_example_exercise_expansion.py`, `scripts/volume04/expansion_common.py`, `scripts/volume04/reconcile_example_exercise_evidence.py`, `scripts/volume04/tex_safety.py`
- `VOL04-HINT-RECONCILIATION` — keep 0, remove 31
- `VOL05-EXPANSION` — keep 224, remove 0
  - active consumers: `scripts/volume05/audit_example_exercise_balance.py`, `scripts/volume05/audit_example_exercise_expansion.py`, `scripts/volume05/expansion_common.py`
- `VOL06-EXPANSION` — keep 392, remove 0
  - active consumers: `scripts/volume06/audit_example_exercise_balance.py`, `scripts/volume06/audit_example_exercise_expansion.py`, `scripts/volume06/expansion_common.py`
- `VOL07-EXPANSION` — keep 84, remove 0
  - active consumers: `scripts/volume07/audit_example_exercise_expansion.py`, `scripts/volume07/reconcile_example_exercise_evidence.py`

## Policy

A marker family is retained whenever an active code/configuration file references the family token. Otherwise the marker is removed from TeX source only after its original line, location, and family are recorded in the TSV ledger.
