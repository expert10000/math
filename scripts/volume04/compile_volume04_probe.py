#!/usr/bin/env python3
from __future__ import annotations
import argparse, shutil, subprocess, tempfile
from pathlib import Path

def main() -> int:
    ap=argparse.ArgumentParser(); ap.add_argument("--repo",required=True); args=ap.parse_args()
    repo=Path(args.repo).resolve(); vol=repo/"books/vol04_complex_analysis"; book=vol/"book.tex"
    exe=shutil.which("pdflatex")
    if not exe: raise RuntimeError("pdflatex not found")
    if not book.exists(): raise RuntimeError(f"missing {book}")
    with tempfile.TemporaryDirectory(prefix="vol04_full_probe_") as td:
        out=Path(td)
        proc=subprocess.run([exe,"-interaction=nonstopmode","-halt-on-error",f"-output-directory={out}",book.name],cwd=vol,text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        log=out/"book.log"
        text=log.read_text(encoding="utf-8",errors="replace") if log.exists() else proc.stdout
        fatal=[line for line in text.splitlines() if line.startswith("!") or "Undefined control sequence" in line]
        if proc.returncode!=0 or fatal:
            print("Volume IV compile probe: FAIL")
            print("\n".join(text.splitlines()[-100:]))
            return 13
    print("Volume IV compile probe: PASS")
    return 0
if __name__=="__main__": raise SystemExit(main())
