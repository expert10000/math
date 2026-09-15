# Final copy-edit policy

C11 is a mathematical copy-edit, not a rewrite. It must preserve every
mathematical claim, hypothesis, convention, label, citation, and cross-reference
unless a separately reviewed mathematical correction is required.

For each canonical chapter, review the following reader-facing concerns:

- use established theorem names and capitalization consistently;
- introduce notation before first substantive use and distinguish conventions
  from assertions;
- integrate display equations into complete sentences where grammar requires it;
- use definition, example, theorem, and proof transitions to expose dependency
  rather than announce an obvious next step;
- split a dense paragraph only when doing so makes a mathematical dependency or
  change of hypothesis easier to see;
- remove certainty words when the accompanying argument, not the prose, carries
  the justification.

Run the deterministic guard after a copy edit:

```powershell
python scripts/series/style_lint.py --repo .
python scripts/series/style_lint.py --repo . --check
```

The lint deliberately checks only mechanical regressions and a small set of
low-information transition phrases. It is not a substitute for mathematical
review or visual PDF review.
