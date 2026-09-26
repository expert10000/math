# Companion Solution Editorial Standard

This document defines the canonical editorial convention for the Companion
problem/solution volumes. Part III is the reference implementation.

## Canonical six-part structure

Each reader-facing problem should follow this order.

### 1. Problem name

Give every problem a concise descriptive name.

Examples:

- `Hölder Inequality — General Exponents`
- `Fourier Transform of the Sinc Function`
- `Baire Category — Countable Families of Subspaces`

The title should identify the mathematics rather than repeat an internal source
label such as "Problem 9" or "Exercise 4.3".

### 2. Exact problem statement

The mathematical task comes first and remains distinct from exposition.

Preserve the canonical/source hypotheses, notation, subparts, and requested
conclusions. Do not mix a later theory section, the next exercise, or unrelated
examples into the same `problem` environment.

When a source defect is known, do not silently conceal it. Use an explicit
editorial note such as:

- `Source correction.`
- `Source-boundary note.`
- `Source restoration.`

The corrected reader-facing formulation must remain traceable to the source.

### 3. Theory — only when needed

After the exact statement, add only the theory needed to solve that problem.

Useful theory may include:

- a definition actually used in the proof;
- the theorem or estimate that drives the argument;
- the Fourier/sign/normalization convention;
- one short roadmap or key idea.

Do not paste a mini-chapter into a single problem. Background that is not used
in the solution belongs elsewhere.

### 4. Solution

The solution is a worked argument, not just an answer.

Preferred structure:

\[
\boxed{
\text{setup/idea}
\longrightarrow
\text{argument}
\longrightarrow
\text{calculation or proof}
\longrightarrow
\text{conclusion}
}
\]

For multipart problems, solve the parts in the same order and label them
clearly as `(a)`, `(b)`, `(c)`, and so on.

A strong solution normally:

- states the relevant hypotheses;
- shows the important intermediate steps;
- justifies theorem use where it is not completely routine;
- handles endpoint/degenerate cases when they matter;
- keeps constants and transform conventions consistent;
- ends with the requested conclusion.

Avoid empty phrases such as "standard", "immediate", "clearly", or "by the
usual argument" when they replace the main mathematical step.

### 5. Examples — when useful

Examples are optional. Add them when they materially improve understanding.

Useful examples include:

- an explicit numerical case;
- a concrete function;
- a counterexample;
- a geometric interpretation;
- a figure-linked calculation.

Do not add filler examples merely to satisfy a heading.

### 6. Extensions — when useful

Extensions are optional. Useful extensions include:

- higher-dimensional forms;
- endpoint cases;
- weaker hypotheses;
- stronger conclusions;
- relations to nearby theorems;
- a short explanation of what fails without an assumption.

Keep extensions subordinate to the original problem.

## Quality rubric

### `A_STRONG`

The problem boundary is coherent and the solution is mathematically sound,
substantially complete, and publication-ready apart from ordinary copy-editing.

### `B_POLISH`

The mathematics is basically sound but the pair still needs one or more of:

- clearer problem title;
- a missing hypothesis restored;
- fuller intermediate reasoning;
- explicit endpoint treatment;
- better organization;
- a useful example or extension;
- trimming of unnecessary background.

### `C_REWRITE`

Substantial editorial work is required because of:

- weak or incomplete solution;
- poor problem/solution alignment;
- excessive compression;
- substantial overmerge;
- repetitive or mini-chapter-style exposition;
- fragmentary statement requiring reconstruction from an identifiable source
  boundary.

### `D_BLOCKING`

The pair cannot be editorially frozen because of:

- mathematical error;
- wrong sign/constant/normalization;
- invalid proof;
- mismatched problem and solution;
- missing solution;
- unresolved source defect that changes the requested mathematics.

## Provenance rule

`SOURCE_BACKED` is provenance, not a quality grade.

A source-backed solution may still need a rewrite. A canonical-authored
solution may already be strong. Quality and provenance are tracked separately.

## Freeze rule

Coverage is necessary but not sufficient.

A Part is editorially frozen only when:

```text
A_STRONG = every reader-facing problem
B_POLISH = 0
C_REWRITE = 0
D_BLOCKING = 0
P0/P1/P2 queues = empty
structural validator = PASS
full clean Companion build = PASS
```

This is the convention established by the completed Part III editorial pass.
