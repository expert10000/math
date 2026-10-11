# GA-03i.1 — Exact Sequences, Derived Functors, Natural Transformations

Evidence-led audit; imported inventory is authoritative. No automatic provenance mapping.

- Canonical problems in scope: 13
- Imported semantic units: 2969
- Status counts: {'PASS': 13, 'REVIEW': 13}

## Canonical example checks

- **CP-V-0022** (NATURAL_TENSOR_QUOTIENT): PASS — (A/I) tensor M = M/IM; line=2403
- **CP-V-0023** (HOM_LOCALIZATION): PASS — Localization commutes with Hom for finitely presented M; line=2509
- **CP-V-0024** (LEFT_RIGHT_EXACTNESS): PASS — Right-exact tensor and left-exact Hom; counterexamples; line=2130
- **CP-V-0031** (COMPLETION_EXACTNESS): PASS — Exact I-adic completion under Noetherian finite-module hypotheses; line=4009
- **CP-V-0087** (INVERSE_LIMIT_EXACTNESS): PASS — Inverse-limit left exactness and surjective transitions; line=4371
- **CP-V-0046** (CONNECTING_HOMOLOGY): PASS — Connecting boundary and long exact homology / Tor; line=5250
- **CP-V-0110** (CHAIN_HOMOTOPY): PASS — Homotopic chain maps induce the same homology maps; line=5358
- **CP-V-0047** (TOR_FROM_RESOLUTION): PASS — Tor from a free resolution over Z; line=5881
- **CP-V-0048** (TOR_IDEAL_FORMULA): PASS — Natural Tor_1 quotient formula; line=5962
- **CP-V-0113** (EXT_FROM_RESOLUTION): PASS — Ext from Hom applied to a free resolution; line=6135
- **CP-V-0114** (DERIVED_EXACT_SEQUENCE): PASS — Tor and Ext as exactness obstructions; line=6250
- **CP-V-0105** (FILTERED_COLIMIT_HOM): PASS — Hom of finitely presented modules commutes with filtered colimits; line=2581
- **CP-V-0096** (BASE_CHANGE_NATURALITY): PASS — Extension of scalars for polynomial quotients; line=2478

## Functorial relationships and open editorial checks

- **CP-V-0024 → CP-V-0114** [REVIEW]: Tensor/Hom failure of exactness vs derived functor obstruction. Confirm naturality and exact hypotheses; do not infer source provenance
- **CP-V-0046 → CP-V-0114** [REVIEW]: Connecting boundary in homology vs long exact Tor/Ext. Confirm naturality and exact hypotheses; do not infer source provenance
- **CP-V-0046 → CP-V-0047** [REVIEW]: Long exact homology as basis for computational Tor. Confirm naturality and exact hypotheses; do not infer source provenance
- **CP-V-0046 → CP-V-0048** [REVIEW]: Naturality of connecting morphisms and Tor ideal quotient. Confirm naturality and exact hypotheses; do not infer source provenance
- **CP-V-0022 → CP-V-0096** [REVIEW]: Naturality under base change and quotient isomorphism. Confirm naturality and exact hypotheses; do not infer source provenance
- **CP-V-0023 → CP-V-0105** [REVIEW]: Finite presentation in Hom/localization vs filtered colimits. Confirm naturality and exact hypotheses; do not infer source provenance
- **CP-V-0031 → CP-V-0087** [REVIEW]: Exact completion vs limitations of inverse limits. Confirm naturality and exact hypotheses; do not infer source provenance
- **CP-V-0110 → CP-V-0046** [REVIEW]: Chain-homotopy invariance vs natural maps on homology. Confirm naturality and exact hypotheses; do not infer source provenance
- **CP-V-0047 → CP-V-0113** [REVIEW]: Left-derived tensor vs right-derived Hom over Z. Confirm naturality and exact hypotheses; do not infer source provenance
- **CONNECTING_NATURALITY** [REVIEW]: Naturality square for boundary homomorphism under a morphism of short exact sequences of complexes. Inspect canonical source material first; do not create a new canonical problem by default
- **LONG_EXACT_EXT_VARIANCE** [REVIEW]: Covariant second and contravariant first variable; articulate correct direction of connecting maps. Inspect canonical source material first; do not create a new canonical problem by default
- **DERIVED_FUNCTOR_COMPARISON** [REVIEW]: Distinguish chain homotopy invariance from naturality of connecting boundary. Inspect canonical source material first; do not create a new canonical problem by default
- **INVERSE_LIMIT_CAUTION** [REVIEW]: Explain why inverse limits need stronger conditions for right exactness. Inspect canonical source material first; do not create a new canonical problem by default
