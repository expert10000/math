#!/usr/bin/env python3
from __future__ import annotations

import argparse
import subprocess
from pathlib import Path

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", required=True)
    args = ap.parse_args()

    repo = Path(args.repo).resolve()

    proc = subprocess.run(
        ["git", "diff", "--name-only", "--", "books"],
        cwd=repo,
        text=True,
        capture_output=True,
        check=True,
    )

    changed = [
        line.strip()
        for line in proc.stdout.splitlines()
        if line.strip().lower().endswith(".tex")
    ]

    normalized = 0

    for rel in changed:
        path = repo / rel
        if not path.is_file():
            continue

        raw = path.read_text(encoding="utf-8")

        # Preserve all content, but remove trailing horizontal whitespace and
        # collapse multiple blank lines at EOF to exactly one final newline.
        lines = raw.splitlines()
        cleaned = "\n".join(line.rstrip(" \t") for line in lines)
        cleaned = cleaned.rstrip("\n") + "\n"

        if cleaned != raw:
            path.write_text(cleaned, encoding="utf-8", newline="\n")
            normalized += 1
            print(f"  NORMALIZE {rel}")

    print(
        f"C01 EOF/whitespace normalization complete: "
        f"{normalized} of {len(changed)} modified TeX files rewritten."
    )
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
