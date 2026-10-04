# Companion Part VI — Stage 3 Reader-Facing Build Audit

- Canonical chapters: **49** (`VI/01`–`VI/49`)
- Stabilized inherited formal problems: **49**
- Fresh canonical problems added under the minimum-two policy: **59**
- Final paired problem count: **108**
- Chapters below two problems after augmentation: **0**
- Stable ID range: `CP-VI-0001`–`CP-VI-0108`
- Fresh solution provenance: `FRESH_CANONICAL_AUTHORED_SOLUTION`

## Editorial rule

The reader-facing file follows the exact canonical Volume VI chapter tree. Inherited units are never merged merely to improve presentation. Fresh units are introduced only in chapters whose stabilized inherited count was zero or one.

## Validation scope

`validate_companion_part06_stage3.py` enforces all 49 chapter sections, minimum-two coverage, contiguous/unique Companion IDs, one reader-facing input per problem, paired solutions, and a basic mojibake scan. Full LaTeX build/warning validation still needs to run inside the repository because this upload does not include the Companion preamble/class/macros or the full book tree.
