# VI/26 Full-Solutions Audit — Finite-Type and Noetherian Morphisms

## Scope

This refinement applies the VI/24–VI/25 detailed-proof standard to VI/26.

Inventory:
- 26 exercises: all receive expanded derivations/proofs.
- 20 problem dossiers: all receive expanded proof bodies.
- 5 challenges: all receive complete solutions.
- Reader/full-solutions separation is normalized with the existing global switches.

## Legacy ownership preserved

The following recovered corpus anchors remain in VI/26 with statements/provenance preserved:

1. **AG5-P4** — every affine open of a locally Noetherian scheme is Noetherian.
2. **AG6-P5**, with duplicate/variant **AG5-P5 merged** — locally finite type may be checked over every affine open of the target.
3. **AG6-P6e** — the three standard finiteness counterexamples.

No additional legacy problem ownership is claimed.

## Mathematical strengthening

The refinement makes explicit:

- finite type = locally finite type + quasi-compact;
- transitivity and base-change stability;
- localization and quotient arguments;
- Hilbert basis theorem consequences;
- the finite distinguished-cover local-to-global Noetherian proof, including the annihilation step for \(I/J\);
- a rigorous finite-type/not-finitely-presented example over a non-Noetherian base;
- the distinction between finite type and finite morphisms;
- fibers of finite-type morphisms;
- the exact hypotheses needed for Noetherian conclusions.

## Boundary discipline

VI/26 does not consume:
- VI/27 integral schemes and function fields;
- VI/28 normalization;
- later projective/proper finiteness theory.

Finite presentation is used only to distinguish it from finite type; no later presentation machinery is migrated into this chapter.

## Build audit

The package contains a solution-layer LaTeX audit.  The repository verifier uses structural markers and exact counts rather than arbitrary byte-size thresholds.
