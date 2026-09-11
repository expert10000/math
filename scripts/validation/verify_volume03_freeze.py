#!/usr/bin/env python3
from pathlib import Path
import hashlib
import sys

ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "books/vol03_fourier_distributions_pde/freeze/VOLUME03_FREEZE_MANIFEST.sha256"

errors = []
for raw in MANIFEST.read_text(encoding="utf-8").splitlines():
    raw = raw.strip()
    if not raw or raw.startswith("#"):
        continue
    digest, rel = raw.split("  ", 1)
    path = ROOT / rel
    if not path.exists():
        errors.append(f"missing: {rel}")
        continue
    actual = hashlib.sha256(path.read_bytes()).hexdigest()
    if actual != digest:
        errors.append(f"hash mismatch: {rel}")

if errors:
    print("\n".join("ERROR: " + e for e in errors))
    sys.exit(1)

print("Volume III freeze manifest: PASS")
