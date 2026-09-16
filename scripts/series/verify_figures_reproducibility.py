#!/usr/bin/env python3
"""Verify manifest coverage, generated C16 outputs, and frozen output checksums."""
from __future__ import annotations

import argparse
import csv
import hashlib
import importlib.util
import json
import subprocess
import sys
from pathlib import Path


C16_OUTPUTS = (
    "code/volume07/results/heat_distance_convergence.csv",
    "code/volume07/results/heat_distance_convergence.tex",
    "code/volume07/results/curvature_validation.csv",
    "code/volume07/results/curvature_validation.tex",
    "code/volume07/results/ridge_valley_robustness.csv",
    "code/volume07/results/ridge_valley_robustness.tex",
    "code/volume07/figures/ridge_scale_stability.tex",
)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def expected_payload(repo: Path) -> dict[str, object]:
    return {
        "schema_version": 1,
        "generator": "code/volume07/experiments/build_figures.py",
        "artifacts": [{"path": relative, "sha256": sha256(repo / relative)} for relative in C16_OUTPUTS],
    }


def generated_outputs_are_current(repo: Path) -> bool:
    module_path = repo / "code/volume07/experiments/build_figures.py"
    spec = importlib.util.spec_from_file_location("volume07_c16_builder", module_path)
    if spec is None or spec.loader is None:
        return False
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return bool(module.build(check=True))


def active_visuals(repo: Path) -> set[str]:
    return {path.relative_to(repo).as_posix() for path in (repo / "books").rglob("c[0-9][0-9]_*.tex")}


def manifest_visuals(repo: Path) -> tuple[set[str], int, list[str]]:
    manifest = repo / "editorial/FIGURE_SOURCE_MANIFEST.tsv"
    with manifest.open(encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle, delimiter="\t"))
    overlays = {row["overlay_source"] for row in rows}
    labels = [row["label"] for row in rows]
    failures = [] if len(labels) == len(set(labels)) else ["DUPLICATE_MANIFEST_LABEL"]
    return overlays, len(rows), failures


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", required=True, type=Path)
    parser.add_argument("--write-checksums", action="store_true", help="refresh the committed C16 checksum record")
    parser.add_argument("--check", action="store_true", help="require every generated output and checksum to be current")
    args = parser.parse_args()
    repo = args.repo.resolve()
    failures: list[str] = []

    manifest_result = subprocess.run([sys.executable, "scripts/series/check_figure_manifest.py", "--repo", ".", "--check"], cwd=repo, text=True, capture_output=True)
    if manifest_result.returncode:
        failures.append("FIGURE_MANIFEST_AUDIT_FAILED")

    overlays, manifest_row_count, manifest_failures = manifest_visuals(repo)
    failures.extend(manifest_failures)
    unmanifested = sorted(active_visuals(repo) - overlays)
    failures.extend(f"UNMANIFESTED_ACTIVE_VISUAL:{path}" for path in unmanifested)
    missing = [relative for relative in C16_OUTPUTS if not (repo / relative).is_file()]
    failures.extend(f"MISSING_C16_OUTPUT:{relative}" for relative in missing)
    if not generated_outputs_are_current(repo):
        failures.append("STALE_C16_GENERATED_OUTPUT")

    checksum_path = repo / "code/volume07/expected/c16_artifact_checksums.json"
    payload = expected_payload(repo) if not missing else {}
    if args.write_checksums and not failures:
        checksum_path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    if args.check:
        if not checksum_path.exists() or checksum_path.read_text(encoding="utf-8") != json.dumps(payload, indent=2) + "\n":
            failures.append("STALE_C16_CHECKSUMS")

    result = {"schema_version": 1, "status": "PASS" if not failures else "FAIL", "active_visuals": len(active_visuals(repo)), "manifest_rows": manifest_row_count, "c16_outputs": len(C16_OUTPUTS), "failures": failures}
    print(json.dumps(result, indent=2))
    return 0 if not failures else 3


if __name__ == "__main__":
    raise SystemExit(main())
