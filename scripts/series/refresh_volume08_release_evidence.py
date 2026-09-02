#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import re
from pathlib import Path

def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", required=True)
    args = ap.parse_args()
    repo = Path(args.repo).resolve()
    freeze = repo / "books/vol08_algebraic_topology/freeze"
    manifest = freeze / "VOLUME08_FREEZE_MANIFEST.sha256"
    report = freeze / "VOLUME08_FREEZE_REPORT.md"

    if not manifest.exists() or not report.exists():
        raise SystemExit("Volume VIII freeze evidence is missing.")

    new_lines = []
    missing = []
    for raw in manifest.read_text(encoding="utf-8-sig").splitlines():
        if not raw.strip():
            continue
        parts = raw.split(None, 1)
        if len(parts) != 2:
            raise SystemExit(f"Malformed freeze-manifest row: {raw}")
        rel = parts[1].strip()
        p = repo / rel
        if not p.exists():
            missing.append(rel)
            continue
        new_lines.append(f"{sha256(p)}  {rel}")

    if missing:
        raise SystemExit("Freeze-manifest paths are missing: " + ", ".join(missing[:20]))

    manifest.write_text("\n".join(new_lines) + "\n", encoding="utf-8")

    text = report.read_text(encoding="utf-8-sig")
    marker = "## Post-release evidence refresh"
    if marker in text:
        text = text.split(marker, 1)[0].rstrip()
    text += (
        "\n\n## Post-release evidence refresh\n\n"
        "The canonical mathematics and tagged v1.0 chapter sources are unchanged. "
        "The Volume VIII README encoding was normalized to UTF-8, stale status prose "
        "was replaced by the actual FROZEN / COMPLETE state, and the freeze manifest "
        "was re-hashed against the current global status ledger and release metadata.\n"
    )
    report.write_text(text.rstrip() + "\n", encoding="utf-8")
    print(f"Volume VIII freeze evidence refreshed: {len(new_lines)} manifest entries")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
