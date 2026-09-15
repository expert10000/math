#!/usr/bin/env python3
"""Build and verify the deterministic source-archive manifest for the next release."""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
from pathlib import Path


ROOT_FILES = {
    "README.md", "LICENSE.md", "CHANGELOG.md", "ERRATA.md", "BUILD_ALL.ps1",
    "BUILD_ALL.bat", ".latexmkrc", "CONTRIBUTING.md",
}
SOURCE_ROOTS = ("books", "code", "docs", "editorial", "reports/series", "scripts", "shared")
RELEASE_FILES = {"ARCHIVAL_METADATA.json", "CITATION.md", "CITATION_METADATA.json", "ARCHIVAL_WORKFLOW.md", "README.md"}
SKIP_NAMES = {"ARCHIVAL_MANIFEST.json", "ARCHIVAL_MANIFEST.tsv", "ARCHIVAL_CHECKSUMS.sha256"}
SKIP_SUFFIXES = {".aux", ".bbl", ".blg", ".fls", ".fdb_latexmk", ".log", ".out", ".pdf", ".pyc", ".synctex.gz", ".toc"}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def archive_group(relative: Path) -> str:
    top = relative.parts[0]
    return {
        "books": "canonical_tex_and_figures", "code": "executable_validation", "docs": "documentation",
        "editorial": "editorial_and_provenance", "reports": "qa_and_indexes", "scripts": "build_and_validation",
        "shared": "shared_tex", "release": "release_metadata",
    }.get(top, "root_metadata")


def candidates(repo: Path) -> list[Path]:
    paths = {repo / name for name in ROOT_FILES if (repo / name).is_file()}
    for root_name in SOURCE_ROOTS:
        root = repo / root_name
        if root.exists():
            paths.update(path for path in root.rglob("*") if path.is_file())
    release = repo / "release"
    paths.update(release / name for name in RELEASE_FILES if (release / name).is_file())
    return sorted(
        (path for path in paths if path.name not in SKIP_NAMES and "__pycache__" not in path.parts and not any(str(path).endswith(suffix) for suffix in SKIP_SUFFIXES)),
        key=lambda path: path.relative_to(repo).as_posix(),
    )


def tsv(rows: list[dict[str, str]]) -> str:
    from io import StringIO
    output = StringIO(newline="")
    writer = csv.DictWriter(output, fieldnames=["path", "group", "bytes", "sha256"], delimiter="\t", lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return output.getvalue()


def write_or_check(path: Path, content: str, check: bool, stale: list[str], repo: Path) -> None:
    content = content.rstrip() + "\n"
    if check:
        if not path.exists() or path.read_text(encoding="utf-8") != content:
            stale.append(path.relative_to(repo).as_posix())
        return
    path.write_text(content, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", required=True, type=Path)
    parser.add_argument("--check", action="store_true", help="verify committed manifest outputs")
    args = parser.parse_args()
    repo = args.repo.resolve()
    metadata_path = repo / "release/ARCHIVAL_METADATA.json"
    metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
    required = ("version", "release_date", "status", "volumes", "chapters", "citation_metadata", "changelog", "errata_policy")
    missing = [field for field in required if field not in metadata]
    if missing:
        print("FAIL: missing archival metadata fields: " + ", ".join(missing))
        return 3
    inventory = repo / "reports/series/BUILD_I_VIII.tsv"
    with inventory.open(encoding="utf-8-sig", newline="") as handle:
        build_rows = list(csv.DictReader(handle, delimiter="\t"))
    if len(build_rows) != 8 or any(row.get("status") != "PASS" for row in build_rows):
        print("FAIL: current build inventory is not 8/8 PASS")
        return 3

    rows = [{
        "path": path.relative_to(repo).as_posix(), "group": archive_group(path.relative_to(repo)),
        "bytes": str(path.stat().st_size), "sha256": sha256(path),
    } for path in candidates(repo)]
    aggregate = hashlib.sha256("\n".join(f"{row['sha256']}  {row['path']}" for row in rows).encode("utf-8")).hexdigest()
    manifest = {
        "schema_version": 1, "status": "PASS", "series": metadata["series"],
        "version": metadata["version"], "release_date": metadata["release_date"],
        "release_state": metadata["status"], "volumes": metadata["volumes"], "chapters": metadata["chapters"],
        "source_artifacts": len(rows), "source_aggregate_sha256": aggregate,
        "pdf_inventory": "reports/series/BUILD_I_VIII.tsv",
        "pdfs_verified": len(build_rows), "tag": metadata["release_tag"], "doi": metadata["doi"],
        "tagging_authority": metadata["tagging_authority"], "doi_authority": metadata["doi_authority"],
    }
    release = repo / "release"
    outputs = {
        release / "ARCHIVAL_MANIFEST.tsv": tsv(rows),
        release / "ARCHIVAL_CHECKSUMS.sha256": "\n".join(f"{row['sha256']}  {row['path']}" for row in rows),
        release / "ARCHIVAL_MANIFEST.json": json.dumps(manifest, indent=2, ensure_ascii=False),
    }
    stale: list[str] = []
    for path, content in outputs.items():
        write_or_check(path, content, args.check, stale, repo)
    if stale:
        print("FAIL: out-of-date archival outputs: " + ", ".join(stale))
        return 3
    print(f"PASS: {len(rows)} source artifacts; 8 PDFs recorded; aggregate {aggregate}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
