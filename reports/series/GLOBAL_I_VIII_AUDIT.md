# Global I-VIII Status, Encoding, and Canonical-Path Audit

**Mode:** repair + audit

## Architecture integrity

- CONTENT_ATLAS chapter codes: **256**
- CHAPTER_STATUS rows: **256**
- Duplicate status codes: **0**
- Status codes missing from atlas: **0**
- Atlas codes missing from status: **0**

## Repairs performed

- Chapter titles restored from CONTENT_ATLAS: **0**
- Stale canonical paths repaired to unique existing chapter paths: **0**
- Remaining suspicious encoding tokens in CHAPTER_STATUS.tsv: **0**

## Canonical-path state

- Volume I: 18 chapters; 18 canonical chapter paths currently exist; 0 planned / 0 drafted / 18 frozen.
- Volume II: 25 chapters; 25 canonical chapter paths currently exist; 0 planned / 0 drafted / 25 frozen.
- Volume III: 28 chapters; 0 canonical chapter paths currently exist; 28 planned / 0 drafted / 0 frozen.
- Volume IV: 31 chapters; 0 canonical chapter paths currently exist; 31 planned / 0 drafted / 0 frozen.
- Volume V: 28 chapters; 0 canonical chapter paths currently exist; 28 planned / 0 drafted / 0 frozen.
- Volume VI: 49 chapters; 49 canonical chapter paths currently exist; 0 planned / 0 drafted / 49 frozen.
- Volume VII: 42 chapters; 42 canonical chapter paths currently exist; 0 planned / 0 drafted / 42 frozen.
- Volume VIII: 35 chapters; 35 canonical chapter paths currently exist; 0 planned / 0 drafted / 35 frozen.

Missing paths are not automatically blocking: Volumes whose reconstruction has not begun are expected to have planned canonical destinations without files.

## Encoding scan

- Files with suspicious byte-decoding signatures: **3**
- Canonical/editorial files among them: **0**

See `GLOBAL_ENCODING_AUDIT.tsv` for exact files and tokens.

## Blocking structural findings

None.
