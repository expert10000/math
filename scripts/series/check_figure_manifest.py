#!/usr/bin/env python3
"""Validate the source, caption, label, and prose-anchor contract for curated visuals."""
from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path


FIELDS = ("asset_id", "volume", "chapter_code", "chapter_source", "overlay_source", "asset_kind", "label", "generated_artifact", "rebuild_command", "caption_contract", "prose_anchor", "review_status")


def read_rows(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def write_or_check(path: Path, content: str, check: bool, stale: list[str], repo: Path) -> None:
    content = content.rstrip() + "\n"
    if check:
        if not path.exists() or path.read_text(encoding="utf-8") != content:
            stale.append(path.relative_to(repo).as_posix())
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", required=True, type=Path)
    parser.add_argument("--check", action="store_true", help="verify the committed audit report")
    args = parser.parse_args()
    repo = args.repo.resolve()
    rows = read_rows(repo / "editorial/FIGURE_SOURCE_MANIFEST.tsv")
    failures: list[str] = []
    seen_assets, seen_labels, manifest_overlays = set(), set(), set()
    kinds = {"figure", "table"}
    for row in rows:
        identity = row.get("asset_id", "")
        label = row.get("label", "")
        missing_fields = [field for field in FIELDS if not row.get(field, "").strip()]
        if missing_fields:
            failures.append(f"MISSING_FIELDS:{identity}:{','.join(missing_fields)}")
            continue
        if identity in seen_assets:
            failures.append(f"DUPLICATE_ASSET_ID:{identity}")
        if label in seen_labels:
            failures.append(f"DUPLICATE_LABEL:{label}")
        seen_assets.add(identity); seen_labels.add(label)
        if row["asset_kind"] not in kinds:
            failures.append(f"UNKNOWN_ASSET_KIND:{identity}:{row['asset_kind']}")
        chapter = repo / row["chapter_source"]
        overlay = repo / row["overlay_source"]
        manifest_overlays.add(overlay.resolve())
        if not chapter.is_file():
            failures.append(f"MISSING_CHAPTER_SOURCE:{identity}")
            continue
        if not overlay.is_file():
            failures.append(f"MISSING_OVERLAY_SOURCE:{identity}")
            continue
        chapter_text = chapter.read_text(encoding="utf-8-sig", errors="replace")
        overlay_text = overlay.read_text(encoding="utf-8-sig", errors="replace")
        if overlay.stem not in chapter_text:
            failures.append(f"OVERLAY_NOT_INPUT:{identity}")
        if f"\\label{{{label}}}" not in overlay_text:
            failures.append(f"MISSING_LABEL_IN_SOURCE:{identity}")
        label_position = overlay_text.find(f"\\label{{{label}}}")
        if label_position >= 0 and "\\caption" not in overlay_text[max(0, label_position - 800):label_position]:
            failures.append(f"MISSING_CAPTION_NEAR_LABEL:{identity}")
        if row["prose_anchor"] not in chapter_text:
            failures.append(f"MISSING_PROSE_ANCHOR:{identity}")

    c07_overlays = {path.resolve() for path in (repo / "books").rglob("c07_visuals.tex")}
    unmanifested = sorted(path.relative_to(repo).as_posix() for path in c07_overlays - manifest_overlays)
    if unmanifested:
        failures.extend(f"UNMANIFESTED_C07_OVERLAY:{path}" for path in unmanifested)
    result = {
        "schema_version": 1,
        "status": "PASS" if not failures else "FAIL",
        "manifest_rows": len(rows),
        "unique_labels": len(seen_labels),
        "c07_overlays": len(c07_overlays),
        "failures": failures,
    }
    report = repo / "reports/series/FIGURE_MANIFEST_AUDIT.json"
    stale: list[str] = []
    write_or_check(report, json.dumps(result, indent=2) + "\n", args.check, stale, repo)
    if stale:
        failures.extend(f"OUT_OF_DATE:{path}" for path in stale)
        result["status"] = "FAIL"
    print(json.dumps(result, indent=2))
    return 0 if not failures else 3


if __name__ == "__main__":
    raise SystemExit(main())
