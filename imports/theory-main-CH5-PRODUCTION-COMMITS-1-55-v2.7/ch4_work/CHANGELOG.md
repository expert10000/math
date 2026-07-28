## v2.1 - Chapter 3 frozen (Commits 32-35)
- Added 100-problem exercise bank.
- Completed glossary, notation, index, and cross-reference integration.
- Passed publication QA and froze Chapter 3.

## PR-BOOK-15.2 Phase V - The Gradient

- Expanded Section 2.5 into a comprehensive graduate-level treatment of the gradient.
- Added motivation, geometric interpretation, steepest-ascent theorem, level-set orthogonality, and tangent-plane connections.
- Added directional-derivative derivation and fully solved examples.
- Added applications to heat flow, conservative forces, electromagnetism, fluid mechanics, optimization, curvilinear coordinates, and quantum mechanics.
- Introduced the del operator, Laplacian, momentum operator, and kinetic-energy operator.
- Added figures, exercises, common mistakes, summary, and a bridge to divergence and curl.
- Synchronized canonical and compatibility source trees.

## PR-BOOK-15.2 Phase IV.1 - Advanced Partial Derivatives

- Expanded Section 2.4 into a rigorous multivariable-calculus treatment.
- Added limit definitions, differentiability criteria, tangent planes, total differentials, and directional derivatives.
- Added Jacobian coordinate transformations, Hessian eigenvalue analysis, and local-extrema classification.
- Added applications in thermodynamics, electromagnetism, fluid mechanics, and quantum mechanics.
- Added figures, worked examples, exercises, common mistakes, and a bridge to the Gradient section.
- Synchronized canonical and compatibility source trees.

## PR-BOOK-15.2 Phase III - Derivatives

- Expanded Section 2.3 from a concise introduction into a complete treatment of derivatives.
- Added first-principles derivations, tangent-line geometry, local linearization, differentials, and differentiability criteria.
- Added proofs and applications of the principal differentiation rules, implicit differentiation, higher derivatives, and notation.
- Connected ordinary derivatives to mechanics, electrodynamics, and quantum-mechanical differential operators.
- Synchronized canonical and compatibility source trees.

## PR-BOOK-15.2 Phase II - Limits

- Expanded Section 2.2 with intuitive and formal definitions of limits.
- Added epsilon-delta rigor, one-sided limits, limit laws, the squeeze principle, continuity, and worked examples.
- Connected limits directly to instantaneous velocity and the derivative.
- Synchronized canonical and compatibility source trees.

# Changelog

## PR-BOOK-15.1 - Chapter 2 Editorial Review

- Reviewed every Chapter 2 section for clarity, grammar, flow, and transitions.
- Standardized derivative, partial-derivative, vector, and nabla notation.
- Consolidated the duplicated Gradient material into one canonical section.
- Applied the PR-13 semantic editorial environment system throughout Chapter 2.
- Added consistent labels and strengthened the chapter-wide pedagogical progression.
- Added `PR-BOOK-15.1.md` and `QA_REPORT_PR-15.1.md`.

# PR-BOOK-14 - Chapter 1 Editorial Completion

- Completed the editorial development of Chapter 1.
- Expanded eight short or skeletal sections into graduate-textbook treatments.
- Added consistent semantic environments, derivations, examples, and physical interpretation.
- Strengthened the bridge from Euclidean vector geometry to abstract vector spaces and quantum mechanics.

# Changelog

## PR-BOOK-13 - Repository Cleanup and Typography

- Introduced canonical publication typography and page furniture.
- Standardized part/chapter/section/subsection hierarchy and TOC presentation.
- Added semantic environment aliases for all new manuscript work.
- Added `cleveref`, PDF bookmarks, document metadata, clickable links, and URL wrapping.
- Added widow/orphan control and resilient line-breaking settings.
- Added `BOOK_STYLE_GUIDE.md` and `PR-BOOK-13.md`.
- Hardened `.gitignore` and formalized the GitHub Release policy.

## PR-BOOK-07.0
- Converted repository to modular book layout.

## PR-BOOK-07.1 — Deduplicated Repository Migration
- Removed the parallel placeholder chapter tree.
- Promoted the historical project contents to the archive root.
- Moved Chapters 1–4 into one canonical `chapters/` hierarchy.
- Initialized only missing Chapters 5–23.
- Archived the old integrated source under `legacy_sources/`.
- Preserved `main.tex` as the current buildable source of truth.

## PR-BOOK-07.2 — Vector Projection and Decomposition
- Added the canonical Section 1.9 source under Chapter 1.
- Reused the existing projection and component-decomposition figures.
- Inserted the section without restructuring or duplicating Chapter 1.

## PR-BOOK-08.0 — Complete Modular Repository
- Split the recovered manuscript into one canonical file per chapter and section.
- Replaced the monolithic master with a concise modular `main.tex`.
- Preserved the previous master under `legacy_sources/monolithic/`.
- Added bibliography, glossary, acronym, notation, theorem, and index infrastructure.
- Added Makefile, latexmk configuration, Git ignore rules, and Overleaf instructions.
- Added generated chapter-state manifests and BOOK_STATE tooling.

## PR-BOOK-08.2 — Vector Fields
- Added a self-contained Vector Fields section before the quantum preview.
- Added uniform, radial, and streamline figures and reused the existing rotational-field figure.
- Existing section prose and ordering were otherwise left unchanged.

## PR-BOOK-08.3 — Divergence
- Appended a canonical divergence section immediately after Vector Fields.
- Added a chapter-local source/sink/neutral-flow figure.
- Existing prose, figures, styles, and section files were otherwise left unchanged.

## PR-BOOK-08.4 — Chapter 1 Epilogue
- Appended a historical and philosophical epilogue after the Chapter 1 summary.
- Added the classical-to-quantum correspondence table and transition to integral methods.
- Existing Chapter 1 sections, figures, styles, and ordering were otherwise unchanged.

## PR-BOOK-09.0 — Vector Integration chapter begins

- Added Chapter 4, *Vector Integration and Integral Theorems*.
- Added Section 4.1, *Introduction—From Local Quantities to Global Physics*.
- Added careful notation for $d\mathbf r$, $ds$, and $d\mathbf A$.
- Shifted the existing Newtonian-mechanics chapter to Chapter 5 in the canonical build order.
- Preserved all existing Newtonian-mechanics section content.

## PR-BOOK-09.1 — Full Dot Product Section

- Replaced the short dot-product placeholder with a complete long-form section titled **The Dot Product (Scalar Product)**.
- Added geometric motivation, projection interpretation, Cartesian component derivation, Kronecker delta notation, special cases, work, a worked example, coordinate invariance, metric-tensor and Hilbert-space previews, historical context, common mistakes, summary, and transition to the cross product.
- Reused the existing dot-product angle TikZ figure with section-local compatibility styles.
- Rebuilt the canonical textbook PDF successfully (84 pages).

## PR-BOOK-09.7 — Full Curl Integration
- Replaced the abbreviated Curl section with the complete structured manuscript.
- Added full derivations, four examples, Maxwell applications, circulation interpretation, Stokes theorem, common mistakes, modern-physics bridge, and two TikZ figures.
- Corrected the local circulation formula to specify the normal component of curl.


## PR-BOOK-12.0 — Editorial hierarchy refactoring

- Numbering now stops at subsection level.
- Existing subsubsections were converted to unnumbered editorial topics.
- Short subsections were demoted using a conservative half-page heuristic.
- Added `\booktopic`, `property`, `bookrule`, and `bookremark`.
- Added `docs/EDITORIAL_HIERARCHY.md`.

## PR-BOOK-15.2 Phase I - Chapter 2 Mathematical Completeness

- Expanded Section 2.1, `Functions`, with formal definitions of domain, codomain, range, and image.
- Clarified scalar-, vector-, single-variable, and multivariable functions.
- Added mechanics and temperature-field examples and a stronger transition to limits.
- Synchronized canonical and compatibility Chapter 2 source files.

## v1.1 — Editorial documentation merge

- Added repository audit and chapter inventory.
- Added editorial, style, figure, notation, example/exercise, and pedagogical guides.
- Added chapter template, figure master plan, content master plan, and production pipeline.
- Preserved the Chapter 1 integrated source and compiled PDF from v1.0 unchanged.

## CH1 Production Sprint - Commit 1
- Polished Section 1.2, *Scalars and Vectors*.
- Removed fragmented prose and excessive vertical spacing.
- Standardized SI-unit typography and bold vector notation.
- Added the transformation-law criterion distinguishing vectors from arbitrary lists of numbers.

## CH1 Production Sprint - Commit 2
- Added four reusable TikZ assets under `figures/ch01/`.
- Integrated position-vector, vector-component, head-to-tail addition, and change-of-basis diagrams into Chapter 1.
- Replaced one embedded figure with a reusable source file.

## CH1 Production Sprint - Commit 3
- Added a dedicated integrated worked-example section.
- Added five complete examples covering magnitude, unit vectors, work, cross products, orthogonal decomposition, and linear dependence.
- Each example now includes calculation and physical or geometric interpretation.

## CH1 Production Sprint - Commit 4
- Added a twelve-problem graded exercise bank spanning foundations, intermediate applications, and advanced reasoning.
- Added `docs/CH1_PRODUCTION_COMMITS_1-4.md` as a concrete sprint record.
- Rebuilt and verified the complete manuscript after all four commits.

## Chapter 1 production commits 5-8
- Completed editorial polish of the remaining Chapter 1 sequence.
- Added eight integrated reusable TikZ figures.
- Expanded integrated worked examples from 5 to 15.
- Expanded the dedicated exercise bank from 12 to 52.
- Rebuilt and visually checked the complete textbook.


## Chapter 1 Production Commits 9-11
- Standardized reusable TikZ figure infrastructure and added twelve integrated figures.
- Added rigorous proofs and geometric interpretation for central vector-space results.
- Added historical notes and explicit connections to mechanics, fields, and quantum theory.

## Chapter 1 - Commits 12-15 (2026-07-27)

- Added the Chapter 1 computational companion with Python and Wolfram Language sources.
- Added generated projection, rotation, linear-transformation, and Gram-Schmidt figures.
- Updated glossary, notation table, bibliography, and Chapter 1/2 cross-references.
- Completed final Chapter 1 QA and froze the chapter as Publication Ready.

## Chapter 2 production commits 16-19

- Completed the Chapter 2 editorial review and strengthened the Chapter 1-to-2 and Chapter 2-to-3 transitions.
- Added eight reusable TikZ figures and four generated computational figures.
- Added a rigorous synthesis of multivariable differentiability, derivative uniqueness, continuity, chain rule, and steepest ascent.
- Added runnable Python and Wolfram Language computational companions.
- Repaired figure-label handling in the shared `bookfigure` environment.
- Rebuilt and visually verified the 194-page manuscript with no final LaTeX errors, undefined references, or box warnings.

## Chapter 2 production commits 20-22
- Added historical and physical-context section.
- Added 25 integrated worked examples.
- Added an 80-problem graded exercise bank with selected guidance.

## Chapter 2 Production Commits 23-25 - v1.8 (2026-07-27)

- Integrated Chapter 2 terminology into the global glossary and notation table.
- Added canonical derivative notation, a repository-wide dependency map, and subject-index anchors.
- Added historical and mathematical bibliography entries and in-text citations.
- Repaired automated glossary and index generation in the out-of-tree `latexmk` build.
- Improved page flow before the worked-example and exercise-bank sections.
- Removed duplicate PDF destination warnings from page anchors.
- Completed a clean 210-page build and visual rendering review.
- Froze Chapter 2 as Publication Ready.

## v1.9 - Chapter 3 production commits 26-28
- Reframed Chapter 3 as *Vector Calculus and Physical Fields*.
- Added local-to-global architecture, field-domain discussion, and orientation foundations.
- Expanded divergence, Laplacian, surface integrals, volume integrals, Green's theorem, Stokes' theorem, and Gauss' theorem.
- Added eight reusable Chapter 3 TikZ figures.
- Rebuilt the complete book successfully at 217 pages.

## v2.0 - Chapter 3 Commits 29-31
- Added 24 integrated vector-calculus worked examples.
- Added executable Python and Wolfram computational companions.
- Added four generated computational figures.
- Added deeper applications to fluids, fields, diffusion, waves, and quantum probability conservation.
- Rebuilt and verified the complete 226-page book.

## v2.2 - Chapter 4 production commits 36-38
- Replaced the Chapter 4 placeholder with *Ordinary Differential Equations and Dynamical Systems*.
- Added foundations of differential equations, initial-value problems, existence/uniqueness context, first-order separable and linear equations, logistic growth, and direction fields.
- Added second-order constant-coefficient equations, free/damped/driven oscillators, energy and resonance.
- Added systems, matrix evolution, eigenmodes, coupled oscillators, phase space, linearization, Lyapunov stability, and a first bifurcation.
- Added eight reusable Chapter 4 TikZ figures.
- Rebuilt and visually verified the complete 245-page manuscript.

## Chapter 4 Commits 39-41
- Added thirty worked examples, computational companions, generated figures, and physics synthesis.

## v2.4 - Chapter 4 Production Commits 42-45
- Added a 100-problem graded Chapter 4 exercise bank with selected guidance.
- Integrated differential-equation terminology, notation, glossary entries, index anchors, and cross-chapter dependencies.
- Completed final publication QA and froze Chapter 4 as Publication Ready.

## v2.5 - Chapter 5 commits 46-48
- Established Complex Analysis foundations, geometry, analyticity, historical context, physical motivation, and reusable figure framework.

## Chapter 5 commits 49-51
Added integrated worked examples, a reproducible computational companion, generated complex-analysis figures, and a physics-applications synthesis.


## v2.7 - Chapter 5 Production Commits 52-55
- Completed Cauchy theory, complex series, singularities, and residues.
- Added a 120-problem graded exercise bank with selected guidance.
- Integrated glossary, notation, index anchors, and chapter dependencies.
- Completed publication QA and froze Chapter 5 as Publication Ready.
