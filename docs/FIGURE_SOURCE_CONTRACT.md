# Figure and table source contract

`editorial/FIGURE_SOURCE_MANIFEST.tsv` is the canonical inventory for reviewed
conceptual visuals. Each row must name the canonical chapter source, a tracked
source asset, a unique label, a caption contract, a prose anchor, and a rebuild
command. `INLINE_TEX` means that the tracked TikZ/table source is compiled into
the canonical volume PDF rather than emitted as a separate image file.

Validate the contract with:

```powershell
python scripts/series/check_figure_manifest.py --repo .
python scripts/series/check_figure_manifest.py --repo . --check
```

The checker is deliberately scoped to manifest-controlled assets. It does not
reclassify, delete, or relink legacy figure files outside the manifest.
