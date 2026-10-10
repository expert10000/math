# GA-03h.3 — Module classes and counterexamples

Mathematical judgments require editorial scrutiny; this audit verifies source anchors only.
The imported inventory remains authoritative for provenance. No source mapping is inferred here.

## FREE_IMPLIES_PROJECTIVE_IMPLIES_FLAT — CP-V-0019
- Example: A[x] over A
- Status: MATHEMATICALLY_REVIEWED
- Mathematical argument: A[x] has the monomial A-basis 1,x,x^2,...; free implies projective, and projective implies flat.
- Source relation: CANONICAL_EXAMPLE
- Missing anchors: none

## PROJECTIVE_NOT_FREE — CP-V-0020
- Example: A_1 x 0 over A_1 x A_2 (both nonzero)
- Status: MATHEMATICALLY_REVIEWED
- Mathematical argument: The idempotent summand Ae_1 is projective; its nonzero annihilator excludes any nonzero free A-module.
- Source relation: CANONICAL_EXAMPLE
- Missing anchors: none

## FLAT_NOT_PROJECTIVE — CP-V-0106
- Example: Q over Z
- Status: MATHEMATICALLY_REVIEWED
- Mathematical argument: Q is torsion-free and thus flat over the PID Z. A projective Z-module is free, whereas nonzero free abelian groups are not divisible; Q is divisible.
- Source relation: DERIVED_COMPARISON_FROM_CANONICAL_THEOREM
- Missing anchors: none

## NONFLAT_TORSION — CP-V-0024
- Example: Z/2 over Z
- Status: MATHEMATICALLY_REVIEWED
- Mathematical argument: Tensoring the injection Z --2--> Z with Z/2 makes it the zero map, so Z/2 is not flat.
- Source relation: CANONICAL_EXAMPLE
- Missing anchors: none

## NONPROJECTIVE_NONFLAT — CP-V-0025
- Example: k[x]/(x) over k[x]
- Status: MATHEMATICALLY_REVIEWED
- Mathematical argument: R/(x) is not projective because the quotient sequence over k[x] does not split. It is nonflat since it has x-torsion over the domain k[x].
- Source relation: CANONICAL_EXAMPLE
- Missing anchors: none

## NONFLAT_TOR_WITNESS — CP-V-0048
- Example: Tor_1 of k with itself over k[x]
- Status: MATHEMATICALLY_REVIEWED
- Mathematical argument: Tor_1^{k[x]}(k,k) = (x)/(x^2) is k, not zero. This witnesses that k is not flat over k[x].
- Source relation: CANONICAL_EXAMPLE
- Missing anchors: none

## FINITE_PD_NOT_FLAT — CP-V-0077
- Example: Z/12 over Z
- Status: MATHEMATICALLY_REVIEWED
- Mathematical argument: The length-one free resolution shows projective dimension 1, but Z/12 is not flat because it has torsion over Z.
- Source relation: CANONICAL_EXAMPLE
- Missing anchors: none

## BASE_RING_DEPENDENCE — CP-V-0082
- Example: k over k versus k over k[x]
- Status: MATHEMATICALLY_REVIEWED
- Mathematical argument: The same underlying module is free over k but has projective dimension one over k[x].
- Source relation: CANONICAL_EXAMPLE
- Missing anchors: none
