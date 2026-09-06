# v1.2-rc1 confirmed layout repair

**Repair smoke test:** PASS

Only `shared/preamble.tex` is changed. No chapter, problem, solution, example,
or mathematical display is semantically rewritten by this commit.

- Severe overfull boxes before: **18**; smoke-build after: **3**.
- Maximum overfull width before: **187.04073pt**; after: **187.04073pt**.
- Policy effect: **IMPROVED**.
- `\sloppy`: **not enabled**.
- Automatic math resizing: **not used**.

The next commit performs a clean eight-volume rebuild and a full 2999-page rendered reproof.
The final v1.2 release freeze remains separate.
