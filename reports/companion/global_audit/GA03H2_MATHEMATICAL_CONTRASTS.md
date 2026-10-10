# GA-03h.2 — Mathematical contrasts

The imported inventory remains authoritative for provenance. This report records mathematical comparisons, not imported-source identity.

## CP-V-0077: Z/12 over Z
- **Review:** CANONICAL_EXAMPLE_REVIEWED
- **Result:** pd=1
- **Reason:** 12 is a nonzero nonunit in Z; length-one free resolution
- **Related IDs:** CP-V-0077

## CP-V-0078: k[x]/(x^3) over k[x]
- **Review:** CANONICAL_EXAMPLE_REVIEWED
- **Result:** pd=1
- **Reason:** multiplication by x^3 gives a length-one free resolution
- **Related IDs:** CP-V-0078

## CP-V-0079: k over k[x,y]
- **Review:** CANONICAL_EXAMPLE_REVIEWED
- **Result:** pd=2
- **Reason:** Koszul resolution on the regular sequence x,y
- **Related IDs:** CP-V-0079

## CP-V-0082: k as module over k vs k[x]
- **Review:** CANONICAL_EXAMPLE_REVIEWED
- **Result:** pd=0 versus pd=1
- **Reason:** projective dimension depends on the base ring
- **Related IDs:** CP-V-0082

## CP-V-0041: k over k[x,y]/(xy)
- **Review:** CANONICAL_EXAMPLE_REVIEWED
- **Result:** pd=infinity
- **Reason:** Tor_i(k,k)=k^2 for all i>=1
- **Related IDs:** CP-V-0041

## CP-V-0043: minimal resolutions and Tor
- **Review:** CANONICAL_EXAMPLE_REVIEWED
- **Result:** pd detected by last nonzero Tor
- **Reason:** requires nonzero finitely generated module of finite projective dimension over a Noetherian local ring
- **Related IDs:** CP-V-0043

## CP-V-0024: Z/2 over Z
- **Review:** CANONICAL_EXAMPLE_REVIEWED
- **Result:** not flat
- **Reason:** tensor of multiplication-by-two injection is zero map
- **Related IDs:** CP-V-0024

## CP-V-0048: k[x]/(x) over k[x]
- **Review:** CANONICAL_EXAMPLE_REVIEWED
- **Result:** not flat
- **Reason:** Tor_1^{k[x]}(k,k)=k != 0
- **Related IDs:** CP-V-0048

## CP-V-0019: A[x] over A
- **Review:** CANONICAL_EXAMPLE_REVIEWED
- **Result:** free, projective, faithfully flat
- **Reason:** monomial basis and evaluation retraction
- **Related IDs:** CP-V-0019

## CP-V-0020: A1 x 0 over A1 x A2
- **Review:** CANONICAL_EXAMPLE_REVIEWED
- **Result:** projective not free
- **Reason:** idempotent summand with nonzero annihilator; A1 and A2 nonzero
- **Related IDs:** CP-V-0020

## CP-V-0025: k[x]/(x) over k[x]
- **Review:** CANONICAL_EXAMPLE_REVIEWED
- **Result:** not projective
- **Reason:** quotient sequence does not split
- **Related IDs:** CP-V-0025

## CP-V-0106: torsion-free module over PID
- **Review:** CANONICAL_EXAMPLE_REVIEWED
- **Result:** flat iff torsion-free
- **Reason:** PID hypothesis essential
- **Related IDs:** CP-V-0106

## CP-V-0106: Q over Z
- **Review:** VERIFIED_DERIVED_COMPARISON
- **Result:** flat not projective
- **Reason:** Q torsion-free hence flat; nonzero divisible group cannot be free abelian; projective over PID is free
- **Related IDs:** CP-V-0106

## CP-V-0041: periodic hypersurface vs polynomial-ring Koszul
- **Review:** VERIFIED_DERIVED_COMPARISON
- **Result:** pd infinity versus pd 2
- **Reason:** compare CP-V-0041 to CP-V-0079 with different base rings
- **Related IDs:** CP-V-0041;CP-V-0079
