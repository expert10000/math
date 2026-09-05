#!/usr/bin/env python3
from __future__ import annotations
import argparse, re, shutil, subprocess, tempfile
from pathlib import Path
from expansion_common import load_data, render_all_blocks

MARKER = re.compile(r"(?ms)^% BEGIN VOL04-EXPANSION ([^\n]+)\n.*?^% END VOL04-EXPANSION \1\n?")
MATH = re.compile(r"(?s)\\\(.*?\\\)|\\\[.*?\\\]|\$\$.*?\$\$|(?<!\\)\$.*?(?<!\\)\$")
UNSAFE = set("_^#%&")

def strip_commands_and_math(text: str) -> str:
    text = MATH.sub("", text)
    # Ignore marker comments; generated content must not otherwise rely on comments.
    text = "\n".join(line for line in text.splitlines() if not line.startswith("% BEGIN VOL04-EXPANSION") and not line.startswith("% END VOL04-EXPANSION"))
    # Labels and TeX command syntax are not prose.
    text = re.sub(r"\\label\{[^}]+\}", "", text)
    text = re.sub(r"\\(?:begin|end)\{[^}]+\}(?:\[[^]]*\])?", "", text)
    text = re.sub(r"\\(?:section|subsection)\*?\{[^}]+\}", "", text)
    return text

def safety_findings(text: str, source: str) -> list[str]:
    findings: list[str] = []
    prose = strip_commands_and_math(text)
    for lineno, line in enumerate(prose.splitlines(), 1):
        for ch in UNSAFE:
            # Escaped special characters are allowed, though generated data normally puts notation in math mode.
            for m in re.finditer(re.escape(ch), line):
                if m.start() == 0 or line[m.start()-1] != "\\":
                    findings.append(f"{source}:line{lineno}:raw-{repr(ch)}:{line.strip()}")
                    break
    if text.count("\\begin{example}") != text.count("\\end{example}"):
        findings.append(f"{source}:unbalanced-example-environment")
    if text.count("\\begin{exercise}") != text.count("\\end{exercise}"):
        findings.append(f"{source}:unbalanced-exercise-environment")
    if text.count("\\begin{hint}") != text.count("\\end{hint}"):
        findings.append(f"{source}:unbalanced-hint-environment")
    if text.count("\\begin{solution}") != text.count("\\end{solution}"):
        findings.append(f"{source}:unbalanced-solution-environment")
    return findings

def probe_document(blocks: list[str]) -> str:
    body = "\n".join(blocks)
    return r"""\documentclass{article}
\usepackage{amsmath,amssymb,amsthm}
\newtheorem{example}{Example}
\newtheorem{exercise}{Exercise}
\newenvironment{hint}{\par\noindent\textit{Hint.} }{\par}
\newenvironment{solution}{\par\noindent\textit{Solution.} }{\par}
\begin{document}
""" + body + "\n\\end{document}\n"

def compile_probe(blocks: list[str]) -> None:
    exe = shutil.which("pdflatex")
    if not exe:
        raise RuntimeError("pdflatex not found; pre-write compile probe is mandatory")
    with tempfile.TemporaryDirectory(prefix="vol04_tex_probe_") as td:
        tdir = Path(td)
        tex = tdir / "probe.tex"
        tex.write_text(probe_document(blocks), encoding="utf-8")
        proc = subprocess.run([exe, "-interaction=nonstopmode", "-halt-on-error", tex.name], cwd=tdir, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        if proc.returncode != 0:
            tail = "\n".join(proc.stdout.splitlines()[-80:])
            raise RuntimeError("temporary TeX compile probe failed:\n" + tail)

def generated_blocks(data: dict, start: int, end: int) -> list[tuple[str,str]]:
    out=[]
    for n in range(start,end+1):
        code=f"IV/{n:02d}"
        if code not in data:
            raise RuntimeError(f"missing data for {code}")
        blocks=render_all_blocks(code,data[code])
        out.append((code,"\n".join(blocks)))
    return out

def live_blocks(repo: Path, start: int, end: int) -> list[tuple[str,str]]:
    from expansion_common import path_for
    out=[]
    for n in range(start,end+1):
        code=f"IV/{n:02d}"
        text=path_for(repo,n).read_text(encoding="utf-8-sig")
        blocks="\n".join(m.group(0) for m in MARKER.finditer(text))
        out.append((code,blocks))
    return out

def main() -> int:
    ap=argparse.ArgumentParser()
    ap.add_argument("--data")
    ap.add_argument("--repo")
    ap.add_argument("--start",type=int,required=True)
    ap.add_argument("--end",type=int,required=True)
    ap.add_argument("--compile-probe",action="store_true")
    args=ap.parse_args()
    if bool(args.data)==bool(args.repo):
        raise SystemExit("choose exactly one of --data or --repo")
    if args.data:
        items=generated_blocks(load_data(Path(args.data).resolve()),args.start,args.end)
    else:
        items=live_blocks(Path(args.repo).resolve(),args.start,args.end)
    findings=[]
    for code,text in items:
        findings.extend(safety_findings(text,code))
    if findings:
        print("TeX safety: FAIL")
        for x in findings: print(" -",x)
        return 11
    if args.compile_probe:
        # Probe every chapter: one example plus the complete 16-triad exercise block catches prose errors.
        compact_blocks=[]
        for _,text in items:
            ex=re.search(r"(?s)% BEGIN VOL04-EXPANSION IV\d\d-example-01\n(.*?)% END VOL04-EXPANSION IV\d\d-example-01",text)
            exs=re.search(r"(?s)% BEGIN VOL04-EXPANSION IV\d\d-exercises-01\n(.*?)% END VOL04-EXPANSION IV\d\d-exercises-01",text)
            if not ex or not exs: raise RuntimeError("probe extraction failed")
            compact_blocks += [ex.group(1), exs.group(1)]
        compile_probe(compact_blocks)
    print(f"TeX safety: PASS for IV/{args.start:02d}-IV/{args.end:02d}")
    return 0
if __name__=="__main__":
    raise SystemExit(main())
