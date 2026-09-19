# Long-child review dispositions

This pass clears `LONG_CHILD_REVIEW` only when the existing audit indicates a
structurally safe single object:

- nested subexamples/subobjects;
- long problem plus exposition;
- long single problem with solution.

It also clears the three source-reviewed nested-example families:

- PRF-014
- PRF-045
- PRF-036

It does **not** alter problem ranges, statement hashes, semantic units, or
problem/solution links. Unsafe or ambiguous diagnoses remain flagged.
