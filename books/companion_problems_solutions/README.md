# Companion Volume — Problems, Solutions, and Worked Examples

**Status:** DEVELOPMENT SCAFFOLD.

This book is a clean intermediate home for the reconciled imported-problem corpus. It is deliberately separate from Volumes I–VIII so that problems can be edited, solved, illustrated, deduplicated, and reviewed before any later integration into the main volumes.

## Architecture

- Part I corresponds to Volume I.
- Part II corresponds to Volume II.
- ...
- Part VIII corresponds to Volume VIII.
- The Companion does **not** duplicate the full chapter tree of the main books.
- Within each Part, problems will be grouped by natural mathematical theme.
- Reader-facing notes give textual links such as `Related material: Volume VI, Chapters VI/18–VI/20`.
- Stable Companion IDs will survive later movement into a main volume.

## Migration rule

Every reconciled semantic problem unit eventually receives exactly one Companion disposition:

- `MIGRATED_TO_COMPANION`
- `ALREADY_EQUIVALENT`
- `NONPROBLEM`
- `REJECTED_WITH_REASON`
- `EDITORIAL_HOLD`

Exact duplicate source statements become one Companion problem with combined provenance.

## Visual enrichment

Figures and plots are added only after the mathematical migration pass. The atlas tracks `figure_requirement`, `figure_type`, and `figure_status` so the visual pass can be audited separately.

## Build

From the repository root:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass `
  -File .\books\companion_problems_solutions\BUILD_WINDOWS.ps1 `
  -Repo $PWD `
  -Clean
```

The canonical development PDF is:

```text
books/companion_problems_solutions/book.pdf
```

## Validation

```powershell
python .\scripts\companion\validate_companion_scaffold.py --repo .
```
