# Figures and reproducibility release gate

Run this sequence from a clean checkout at the candidate revision. It rebuilds
the tracked C16 data before the canonical PDFs, then checks figures, indexes,
and source-archive contents against their committed contracts.

```powershell
python code/volume07/experiments/build_figures.py
python -m unittest discover -s code/volume07/tests -v
python scripts/series/check_figure_manifest.py --repo . --check
python scripts/series/verify_figures_reproducibility.py --repo . --check
.\BUILD_ALL.ps1 -CanonicalOnly -CleanFirst
python scripts/series/style_lint.py --repo . --check
python scripts/series/build_series_indexes.py --repo . --check
python scripts/series/build_archival_manifest.py --repo . --check
```

The C16 heat table is an explicit local graph-diffusion proxy. Its machine
readable data records mesh scale, time normalization, error, boundary treatment,
and deterministic work units; it deliberately reports sparse-factorization time
as not applicable. It must not be cited as a production timing benchmark.

`verify_figures_reproducibility.py` checks every active `cNN_*.tex` visual is
manifested, runs the manifest audit, verifies generated C16 outputs are fresh,
and compares their SHA-256 values with
`code/volume07/expected/c16_artifact_checksums.json`. To intentionally refresh
that checksum record after reviewing a generator change, run the same command
with `--write-checksums`, then review and commit the changed record.

This is a development and archive-readiness gate only. It does not create a git
tag, mint a DOI, deposit an archive, or create `CITATION.cff`; those remain the
release-owner actions in `release/ARCHIVAL_WORKFLOW.md`.
