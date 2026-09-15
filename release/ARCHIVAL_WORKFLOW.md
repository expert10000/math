# Archival release workflow

This workflow prepares a reproducible archive without claiming that the current
development line is already a public release. The current metadata describes
`1.4.0-dev.1`; v1.3 remains the last released series archive.

## Archive contents

The generated archival manifest covers canonical TeX source, shared styles and
notation, scripts, executable validation code and deterministic benchmark
definitions, figures/source assets, bibliography, editorial and QA evidence,
build-environment documentation, release metadata, changelog, errata policy,
and the canonical PDF inventory. At release time, place the eight generated PDFs
named in `reports/series/BUILD_I_VIII.tsv` beside this source archive and verify
their hashes against the inventory.

## Prepare and verify

```powershell
.\BUILD_ALL.ps1 -CanonicalOnly -CleanFirst
python scripts/series/style_lint.py --repo . --check
python scripts/series/build_series_indexes.py --repo . --check
python scripts/series/build_archival_manifest.py --repo .
python scripts/series/build_archival_manifest.py --repo . --check
```

The manifest check proves that all listed source artifacts have the expected
SHA-256 values. It does not make PDFs byte-reproducible: TeX metadata can vary
between builds, so PDFs are verified by the fresh build inventory at the tagged
revision.

## Final release-owner actions

1. Supply verified author/editor, affiliation/ORCID if applicable, and a final
   rights/license decision; update the front matter and citation metadata.
2. Set the final version/date in `ARCHIVAL_METADATA.json`, changelog, and
   citation metadata. Mint or reserve a DOI only through the selected archive
   provider, then record it consistently in all three records.
3. Build from a clean checkout, verify the manifest and PDF inventory, and
   archive exactly the manifest-listed source plus the eight PDFs.
4. Create an annotated tag `theory-of-mathematics-i-viii-vX.Y.Z` at that exact
   verified commit; record its immutable commit ID and archive identifier in the
   release metadata. Push the tag only after the archive deposit is complete.
5. Publish a release note linking the tag, DOI/archive record, checksums,
   changelog entry, and errata policy.

No tag or DOI is created by this repository workflow; both are release-owner
decisions with external, durable effects.
