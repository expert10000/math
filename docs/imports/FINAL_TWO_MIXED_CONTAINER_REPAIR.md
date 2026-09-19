# Final two mixed-container structural repair

This targeted pass repairs only:

- RSF-004 — `theory-of-algebraic-geometry-5.tex`
- RSF-008 — `theory-of-algebraic-topology-5.tex`

The two sources mix actual problems/examples with long reader-facing theory,
worked explanation, summaries, diagrams, and solution blocks.

The final source-structural rule keeps:

- headings beginning `Problem`, `Exercise`, `Example`, `Question`, `Task`, or
  `Challenge`;
- a section/subsection immediately followed by a `Statement` heading.

It omits explanatory glue such as `Theory for Problem ...`, summaries, tables,
diagrams, and Solution/Proof regions.

Worked examples remain `EXAMPLE` objects but are terminated before the next
same/higher-level heading so they do not absorb later exposition.

Default execution is a dry run.
