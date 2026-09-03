# Canonical Dossier Index and Provenance Atlas

**Result:** PASS

This index is generated from the recursive active TeX graph of every FROZEN canonical chapter.
A row therefore represents problem/challenge material physically embedded in the canonical source/build graph.

- Canonical `problem` entries: **4061**
- Canonical `challenge` entries: **0**
- Total indexed problem-like entries: **4061**
- Expected `problem` entries from global reconciliation: **4061**
- Dossier provenance ledgers discovered: **16**
- Explicit provenance labels loaded: **1560**

## Interpretation

- `ROOT_CHAPTER` means the dossier is written directly in the canonical `chapter.tex`.
- `INCLUDED_ACTIVE_FILE` means it is in a TeX file reached by the canonical chapter build graph.
- `VOLUME06_FULL_SOLUTIONS_EDITION` reflects Volume VI's native edition-controlled solution architecture.
- `NATIVE_FROZEN_OR_UNTRACKED_CANONICAL` does not mean unresolved legacy material; it means no newer dossier-level provenance TSV exists for that individual label.

All source-migration accounting remains governed by `GLOBAL_SOURCE_RULE_RECONCILIATION.tsv`; the dossier index does not claim a one-to-one legacy-row-to-dossier transformation.

## Volume counts

- Volume I: **216** problem/challenge entries
- Volume II: **300** problem/challenge entries
- Volume III: **336** problem/challenge entries
- Volume IV: **372** problem/challenge entries
- Volume V: **336** problem/challenge entries
- Volume VI: **1045** problem/challenge entries
- Volume VII: **714** problem/challenge entries
- Volume VIII: **742** problem/challenge entries

## Blocking findings

None.
