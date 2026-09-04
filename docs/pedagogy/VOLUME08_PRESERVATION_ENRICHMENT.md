# Volume VIII — preservation and enrichment contract

## Scope

Apply three local commits to the inspected `expert10000/math` baseline
`9e8346d067f47d6d49b1d3da228ad07386de6e93`. No source outside Volume VIII
is edited. Existing shared TeX is read for the input/reference audit, never
modified. Existing theorem statements, proofs, problem/exercise statements,
solutions, labels, chapter-specific goals, notation, chapter order and artwork
remain unchanged. Only the bodies of the 840 existing exercise hints change.

The patcher preserves the UTF-8 BOM and a consistent LF or CRLF worktree
newline convention. Cross-platform Git comparisons normalize LF/CRLF only;
actual chapter patching does not rewrite the file's other bytes.

## Three commits

1. `vol08: audit measurable outcomes and hint architecture`
   installs the checker, preservation plan, open findings, tests, supplemental
   outcome review map, and a freshly computed baseline source report.
2. `vol08: enrich mathematical hints in VIII/01-VIII/17`
   applies 408 label-specific additions and records the intermediate source audit.
3. `vol08: complete hint enrichment in VIII/18-VIII/35 and audit pedagogy`
   applies 432 further entries and records the final source audit with readiness
   still **HOLD**. “Complete hint enrichment” does not mean complete pedagogy.

## Preservation choices

623 original clues remain verbatim, followed by a mathematically actionable
addition. 216 repeated template clues in VIII/22–VIII/30 are replaced by
individual mathematical hints. One misdirected clue, `exr:viii32-02`, is replaced
by the appropriate normalization argument. Original text is recoverable from
the pinned Git parent; no statement or solution is silently “fixed” in a hint pass.

Each entry is keyed by its existing exercise label. Each late placeholder
chapter is explicitly marked `existing_solution_missing_exercise_statement`.
There is no claim that those 216 entries are aligned to real questions: the
questions do not yet exist in the inspected source.

Hints name concrete objects and operations: a cycle representative, a lift,
a boundary/coboundary, a kernel or cokernel, a sign calculation, an orientation
class, an attaching-map degree, a connecting homomorphism, or a nondegeneracy
condition. They also distinguish reduced/ordinary conventions, support choices,
coefficient rings, dimension restrictions, and primary/higher obstructions.
A marker, word count, or TeX compilation alone is not proof of actionability.

## What the source audit establishes

The checker follows statically resolvable `input` and `include` commands from
the canonical entry point. It compares the entire active source graph with
the pinned baseline plus exactly the authorized hint replacements. This is
stronger than comparing selected theorem labels: every non-hint character in
active protected source must still agree, subject only to LF/CRLF normalization.

Counts and statement–hint–solution associations are recomputed from source
order. Problems without hints are allowed; exercises without hints, missing
solutions, orphan solutions, duplicate statement labels, duplicate active labels
and unresolved static references are reported. Commented-out and common
verbatim content are excluded. Dynamic TeX and conditional branches remain
explicit verification limits and require a real build.

The outcome audit inventories recognized learning-goal/outcome headings,
item counts, content hashes and action-verb candidates. It does not rewrite
outcomes or interpret every possible presentation of an outcome. No recognized
heading means “review this chapter,” not “this chapter has no goals.” The
35-row review worksheet is supplemental, with proposed observable tasks.

## Why readiness remains HOLD

The source still contains 216 placeholder exercise statements and the open
mathematical findings in `VOLUME08_PROTECTED_FINDINGS.md`. Their correction is
outside this package's preservation contract. The actual canonical Volume VIII
PDF, I–VIII builds and the independent series checks have not been run by this
kit. Therefore `structural_source_status=PASS` is compatible with and must not
be substituted for `pedagogy_readiness=HOLD`.

The strict auditor returns exit code 2 for this HOLD after successful source
checks. It returns 1 for a structural failure. The non-strict source checker
returns 0 when only the structural checks pass, while printing HOLD explicitly.

## Artifacts and exclusions

New reports are placed only under `reports/volume08/pedagogy-enrichment/`.
Source hashes there are preservation evidence, not PDF or release hashes.
The kit does not touch existing freeze ledgers, chapter-status ledgers, migration
ledgers, release evidence, PDF inventories, canonical PDFs, tags or remotes.
There is no push, freeze or build option in the runner.
