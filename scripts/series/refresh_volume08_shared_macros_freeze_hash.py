#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import re
import subprocess
from pathlib import Path

ROW_RE = re.compile(r"^([0-9a-fA-F]{64})\s{2,}(.+?)\s*$")

def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()

def git_clean_for(repo: Path, rel: str) -> bool:
    cp = subprocess.run(
        ["git", "-C", str(repo), "status", "--porcelain=v1", "--", rel],
        text=True, capture_output=True, encoding="utf-8", errors="replace"
    )
    if cp.returncode != 0:
        raise SystemExit("git status failed while checking " + rel)
    return not cp.stdout.strip()

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", required=True)
    args = ap.parse_args()

    repo = Path(args.repo).resolve()
    rel = "shared/macros.tex"
    macros = repo / rel
    manifest = repo / "books/vol08_algebraic_topology/freeze/VOLUME08_FREEZE_MANIFEST.sha256"

    if not macros.exists() or not manifest.exists():
        raise SystemExit("Volume VIII shared-macros freeze repair prerequisites are missing.")
    if not git_clean_for(repo, rel):
        raise SystemExit("Refusing to refresh Volume VIII freeze hash: shared/macros.tex is not Git-clean.")

    actual = sha256(macros)
    lines = manifest.read_text(encoding="utf-8-sig").splitlines()
    found = 0
    old = None
    out = []
    for raw in lines:
        m = ROW_RE.match(raw.strip())
        if m and m.group(2).replace("\\", "/") == rel:
            found += 1
            old = m.group(1).lower()
            out.append(f"{actual}  {rel}")
        else:
            out.append(raw)
    if found != 1:
        raise SystemExit(f"Expected exactly one {rel} row in Volume VIII freeze manifest; found {found}.")

    manifest.write_text("\n".join(out) + "\n", encoding="utf-8")
    print(f"Volume VIII shared macros freeze hash: {old} -> {actual}")
    if old == actual:
        print("Volume VIII shared macros freeze hash already current.")
    else:
        print("Volume VIII shared macros freeze hash refreshed from the Git-clean pinned source.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
