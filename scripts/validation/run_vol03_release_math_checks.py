#!/usr/bin/env python3
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[2]
checks = [
    ROOT / "scripts/validation/validate_vol03_fourier_convention.py",
    ROOT / "scripts/validation/validate_vol03_fourier_pde_constants.py",
]
for check in checks:
    p = subprocess.run([sys.executable, str(check)], cwd=ROOT)
    if p.returncode:
        raise SystemExit(p.returncode)
print("Volume III release math checks: PASS")
