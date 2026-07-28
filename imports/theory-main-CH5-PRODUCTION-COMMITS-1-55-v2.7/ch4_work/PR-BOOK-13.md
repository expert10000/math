# PR-BOOK-13 - Repository Cleanup and Typography

## Scope

This pull request establishes the publication layer used by all future chapter work.

## Changes

- Added canonical typography in `styles/book_typography.tex`.
- Added canonical semantic aliases in `styles/book_environments.tex`.
- Added PDF metadata, bookmarks, clickable references, `cleveref`, and URL wrapping in `styles/book_references.tex`.
- Standardized part, chapter, section, subsection, running-head, plain-page, and table-of-contents typography.
- Added widow/orphan control and more resilient line breaking.
- Added `BOOK_STYLE_GUIDE.md` as the editorial constitution.
- Hardened `.gitignore` for LaTeX, editors, build folders, and release archives.
- Updated the displayed release identifier to PR-BOOK-13.

## Compatibility

Existing chapter content and legacy environment names remain supported. This PR intentionally avoids substantive manuscript rewriting.
