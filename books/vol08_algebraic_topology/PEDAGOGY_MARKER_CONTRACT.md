# Volume VIII pedagogy marker contract

The comment marker

```text
VIII-PEDAGOGY-HINT-v1.1
```

is **active source metadata**, not obsolete editorial scaffolding.

## Why it exists

`scripts/volume08/pedagogy_core.py` uses the marker to make the curated hint
enrichment process idempotent. The patcher writes a marker line adjacent to each
curated hint addition and refuses to enrich a hint that is already marked.

The marker therefore protects against accidental double application of the
curated hint bank.

## Required form

Each active marker has the form

```text
% VIII-PEDAGOGY-HINT-v1.1 <exercise-label> <mode>
```

where `<mode>` is one of:

- `append`
- `replace_template`
- `replace_misdirected_clue`

The exercise label and mode must agree exactly with the corresponding row in:

- `scripts/volume08/hints_01_17.json`
- `scripts/volume08/hints_18_35.json`

## Release invariant

The Volume VIII pedagogy test suite checks that:

- all 840 curated hint-bank entries have exactly one active marker;
- no extra or malformed active markers exist;
- the marker's mode agrees with the curated bank;
- the existing preservation patcher continues to reject reapplication.

A future cleanup may change or remove this marker only together with an explicit
migration of `pedagogy_core.py`, its banks, tests, and any release/audit tooling
that depends on the idempotence contract.
