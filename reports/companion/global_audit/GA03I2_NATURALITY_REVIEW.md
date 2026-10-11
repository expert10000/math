# GA-03i.2 — Natural transformations and derived-functor compatibility

Source: GA-03i.1 canonical scope and audit ledger. This is an editorial mathematical review;
the source-import provenance and four editorial gaps remain separately tracked.

## Reviewed connections

### CP-V-0024 → CP-V-0114
**TENSOR_HOM_EXACTNESS — COMPATIBLE**

Tensor is right exact and Hom(M,-) is left exact; Tor and Ext measure their respective failures. The direction of the Ext boundary depends on the chosen variable.

### CP-V-0046 → CP-V-0114
**CONNECTING_TO_DERIVED — COMPATIBLE**

The long exact homology sequence applies to degreewise short exact sequences of tensor complexes; for Ext the relevant cochain complexes yield cohomological connecting maps.

### CP-V-0046 → CP-V-0047
**TOR_RESOLUTION — COMPATIBLE**

A free resolution of Z/n has differential multiplication by n; tensoring with N makes Tor_1 equal to ker(n:N->N).

### CP-V-0046 → CP-V-0048
**IDEAL_INTERSECTION_TOR — COMPATIBLE**

The boundary and exactness for 0->I->A->A/I->0 after tensoring with A/J identify Tor_1(A/I,A/J) with (I intersect J)/IJ; this identification is natural in maps of compatible ideal pairs.

### CP-V-0022 → CP-V-0096
**BASE_CHANGE_NATURALITY — COMPATIBLE**

The natural map (A/I) tensor_A M -> M/IM sends (a+I) tensor m to am+IM. Extension from k to K preserves quotient presentations, with commuting structure maps.

### CP-V-0023 → CP-V-0105
**HOM_FINITE_PRESENTATION — COMPATIBLE_WITH_DISTINCTION**

Both results use finite presentation, but one compares Hom with localization while the other compares Hom with filtered colimits. They are distinct natural transformations.

### CP-V-0031 → CP-V-0087
**COMPLETION_VS_LIMIT — COMPATIBLE_WITH_HYPOTHESES**

Inverse limits are left exact; surjectivity in the limit depends on the kernel inverse system. Exact completion for finite modules over Noetherian rings additionally uses Artin-Rees/cofinal filtrations.

### CP-V-0110 → CP-V-0046
**HOMOTOPY_VS_NATURALITY — COMPATIBLE_WITH_DISTINCTION**

Chain-homotopic chain maps induce the same map on homology; naturality of connecting homomorphisms requires a commuting morphism of short exact sequences of complexes.

### CP-V-0047 → CP-V-0113
**TOR_EXT_DUAL_COMPARISON — COMPATIBLE_WITH_DISTINCTION**

Both use the resolution of Z/n. Tor_1(Z/n,N)=ker(n:N->N), whereas Ext^1(Z/n,N)=coker(n:N->N). Similar cyclic outputs do not identify the two functors naturally.

## Open editorial gaps

### CONNECTING_NATURALITY
Write and check the naturality square: for a morphism of short exact sequences of chain complexes, H_{n-1}(a) circ boundary = boundary_new circ H_n(c).

### LONG_EXACT_EXT_VARIANCE
State separately Ext^i(M,-) covariant in the second variable and Ext^i(-,N) contravariant in the first. Explain the connecting maps and arrows in each long exact sequence.

### DERIVED_FUNCTOR_COMPARISON
Distinguish chain-homotopy invariance of homology maps from functorial naturality of boundary operators. Neither theorem should be presented as proving the other.

### INVERSE_LIMIT_CAUTION
Explain inverse-limit left exactness, the role of lim^1, and sufficient Mittag-Leffler/surjective-transition hypotheses for right exactness. Do not assert inverse limits are exact in general.

## Connecting-map naturality identity

For a commuting morphism of short exact sequences of chain complexes
with vertical maps a, b, c, the homological connecting maps satisfy
\[ H_{n-1}(a)\circ\partial_n=\widetilde{\partial}_n\circ H_n(c).\]

## Ext variance

\(\operatorname{Ext}_R^i(M,-)\) is covariant, while
\(\operatorname{Ext}_R^i(-,N)\) is contravariant.
For a short exact sequence \(0\to A'\to A\to A''\to0\),
the connecting map for Ext in the second variable goes from
\(\operatorname{Ext}_R^i(M,A'')\) to \(\operatorname{Ext}_R^{i+1}(M,A')\).

## Inverse-limit caveat

Inverse limits are left exact. For the usual countable index category,
the obstruction to right exactness is related to the derived functor lim^1.
A Mittag–Leffler condition on the kernel system is sufficient for
the needed vanishing. This is distinct from exactness of filtered colimits.
