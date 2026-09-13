# Theory of Mathematics I-VIII — v1.3

Status: **promotion ready**

Promoted candidate: `v1.3-rc1`  
Original RC commit: `1859fca09fbd0492423f374f3b4cf6fd921a40b2`  
Clean-checkout reproducibility commit: `ff8caba1c887c845176d687a07811e3adeee6859`

## Scope

Version 1.3 freezes the eight-volume series at **8 volumes / 256 numbered canonical chapters**,
all FROZEN / COMPLETE.

## Final release work

- completed professional-review passes across Volumes I-VIII;
- reconciled all chapter-status and source-migration ledgers;
- aligned Volume II topology coverage, retaining 25 numbered chapters plus its unnumbered topology interlude;
- reconciled solved dossiers, exercises, hints and solutions;
- reconciled cross-volume mathematical navigation;
- refreshed publication freeze metadata;
- repaired the final >=20pt layout overflows;
- verified the Volume VI full-solutions edition;
- canonicalized freeze-manifest hashes to immutable Git blob bytes so the freeze contract is platform-independent;
- passed the clean-checkout v1.3 reproducibility gate.

## Reproducibility policy

Freeze-manifest hashes identify immutable Git content rather than platform-specific checkout bytes.
PDF SHA-256 values remain recorded for traceability; regenerated TeX PDFs may differ byte-for-byte
because of embedded build metadata. Page counts, canonical source/freeze integrity, successful
builds, LaTeX diagnostics and global reconciliation are blocking release criteria.

## Versioning

After promotion, v1.3 is frozen. Further mathematical/editorial changes begin v1.4 work.
