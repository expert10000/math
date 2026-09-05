#!/usr/bin/env python3
import argparse,subprocess,tempfile,shutil
from pathlib import Path
from expansion_common import load_data,render_all_blocks
def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--data",required=True); a=ap.parse_args()
    if not shutil.which("pdflatex"): print("pdflatex not found"); return 8
    data=load_data(Path(a.data).resolve()); body=[]
    for code,d in data.items(): body += [f"\\section*{{{code}}}"]+render_all_blocks(code,d)
    tex=r"""\documentclass{article}
\usepackage[T1]{fontenc}
\usepackage{lmodern}
\usepackage{amsmath,amssymb,amsthm}
\newtheorem{example}{Example}
\newtheorem{exercise}{Exercise}
\newenvironment{hint}{\par\noindent\textbf{Hint.}}{\par}
\newenvironment{solution}{\par\noindent\textbf{Solution.}}{\par}
\begin{document}
"""+"\n".join(body)+"\n\\end{document}\n"
    with tempfile.TemporaryDirectory(prefix="vol06_probe_") as td:
        p=Path(td); (p/"probe.tex").write_text(tex,encoding="utf-8")
        cp=subprocess.run(["pdflatex","-interaction=nonstopmode","-halt-on-error","probe.tex"],cwd=p,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True,encoding="utf-8",errors="replace")
        if cp.returncode: print(cp.stdout[-8000:]); return cp.returncode or 9
    print(f"PASS: generated-content pdflatex probe for {len(data)} chapter(s)."); return 0
if __name__=="__main__": raise SystemExit(main())
