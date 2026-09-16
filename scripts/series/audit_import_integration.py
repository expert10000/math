#!/usr/bin/env python3
"""Inventory imported TeX sources that must be reconciled into the book series.

The ``imports/`` tree is source material, not a build target.  This utility makes
its contents auditable before chapters are migrated into the canonical ``books/``
tree: it identifies duplicate payloads, standalone source documents, and the
volume suggested by an unambiguous filename topic.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
from collections import Counter
from pathlib import Path


TOPIC_VOLUMES = (
    ("linear-algebra", "I"),
    ("real-analysis", "II"),
    ("analysis-functions", "II"),
    ("disitrbutions", "III"),  # Preserves the imported filename spelling.
    ("distributions", "III"),
    ("complex-analysis", "IV"),
    ("commutative-algebra", "V"),
    ("algebraic-topology", "VIII"),
    ("differential-geometry", "VII"),
)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def target_volume(name: str) -> str:
    folded = name.casefold()
    matches = {volume for token, volume in TOPIC_VOLUMES if token in folded}
    return matches.pop() if len(matches) == 1 else "UNMAPPED"


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def collect(imports: Path, repo: Path) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for source in sorted(imports.rglob("*.tex")):
        text = read_text(source)
        rel = source.relative_to(repo).as_posix()
        rows.append(
            {
                "import_root": source.relative_to(imports).parts[0],
                "path": rel,
                "sha256": sha256(source),
                "bytes": str(source.stat().st_size),
                "standalone": "yes" if "\\documentclass" in text else "no",
                "target_volume": target_volume(source.name),
                "active_book_reference": "no",
            }
        )
    duplicate_counts = Counter(row["sha256"] for row in rows)
    for row in rows:
        row["identical_copy_count"] = str(duplicate_counts[row["sha256"]])
        row["integration_status"] = (
            "review-for-book-integration"
            if row["identical_copy_count"] == "1"
            else "deduplicate-before-integration"
        )
    return rows


def write_tsv(rows: list[dict[str, str]], output: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    fields = list(rows[0]) if rows else []
    with output.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, delimiter="\t")
        writer.writeheader()
        writer.writerows(rows)


def write_markdown(rows: list[dict[str, str]], output: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    roots = Counter(row["import_root"] for row in rows)
    volumes = Counter(row["target_volume"] for row in rows)
    standalone = sum(row["standalone"] == "yes" for row in rows)
    unique = len({row["sha256"] for row in rows})
    lines = [
        "# Imported TeX Integration Audit",
        "",
        "The files below are source material to reconcile into `books/`; they are not archival build targets.",
        "",
        f"- TeX files: **{len(rows)}**",
        f"- Distinct byte-identical payloads: **{unique}**",
        f"- Standalone TeX documents: **{standalone}**",
        "",
        "## Import collections",
        "",
        "| Collection | TeX files |",
        "|---|---:|",
    ]
    lines.extend(f"| `{root}` | {count} |" for root, count in sorted(roots.items()))
    lines.extend(
        [
            "",
            "## Inferred target volume",
            "",
            "The inference is intentionally conservative; `UNMAPPED` files require chapter-level editorial review.",
            "",
            "| Volume | Candidate files |",
            "|---|---:|",
        ]
    )
    lines.extend(f"| {volume} | {count} |" for volume, count in sorted(volumes.items()))
    lines.extend(
        [
            "",
            "The machine-readable TSV records every source path, duplicate group, and integration status.",
            "",
        ]
    )
    output.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument("--tsv", type=Path, default=Path("reports/series/IMPORT_INTEGRATION_AUDIT.tsv"))
    parser.add_argument("--markdown", type=Path, default=Path("reports/series/IMPORT_INTEGRATION_AUDIT.md"))
    args = parser.parse_args()
    repo = args.repo.resolve()
    rows = collect(repo / "imports", repo)
    if not rows:
        raise SystemExit("No imported TeX files found.")
    write_tsv(rows, (repo / args.tsv).resolve())
    write_markdown(rows, (repo / args.markdown).resolve())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
