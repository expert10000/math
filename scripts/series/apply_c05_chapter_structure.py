#!/usr/bin/env python3
from __future__ import annotations

import argparse, csv, re
from pathlib import Path

VOLS=[
"vol01_linear_algebra","vol02_real_analysis","vol03_fourier_distributions_pde",
"vol04_complex_analysis","vol05_commutative_algebra","vol06_algebraic_geometry",
"vol07_differential_geometry","vol08_algebraic_topology"
]

GUIDE = r"""\chapter*{Chapter Structure Guide}
\phantomsection
\addcontentsline{toc}{chapter}{Chapter Structure Guide}

The series uses a common chapter architecture while allowing mathematically
justified exceptions.  A chapter should make the following roles easy to find:

\begin{enumerate}
\item prerequisites or context;
\item learning direction or roadmap;
\item core definitions, propositions, theorems, and proofs;
\item worked examples;
\item exercises and, where appropriate, solved problems or challenges;
\item a chapter-specific summary or synthesis;
\item source/further-reading guidance, maintained at chapter or volume level;
\item a bridge to the next mathematical topic when such a bridge is useful.
\end{enumerate}

This is a structural contract, not a requirement that every chapter use eight
identically named sections.  Short or highly specialized chapters may combine
roles.  The repository structural audit records those differences so they are
intentional rather than accidental.
"""

CONTRACT = """# C05 chapter contract

The series-wide chapter contract is role-based rather than mechanically template-based.

## Core roles

1. Prerequisites/context
2. Learning direction or roadmap
3. Core exposition
4. Worked examples
5. Exercises
6. Solved problems/challenges where pedagogically useful
7. Chapter summary/synthesis
8. Sources/further reading
9. Bridge forward where useful

A chapter may combine roles or omit a role only when the omission is mathematically or pedagogically intentional.

## Canonical heading vocabulary

Preferred headings:
- `Examples`
- `Exercises`
- `Solved problems`
- `Challenges`
- `Chapter summary`
- `Bridge to ...`

Deprecated production-era headings such as `Solved dossiers` or `Solved problem dossiers` are forbidden.

## Source guidance

C03 provides volume-level `Sources and Further Reading` guides mapped by chapter range. A chapter need not duplicate those references unless a local historical/source note materially improves the exposition.

## Audit rule

`reports/series/C05_CHAPTER_STRUCTURE_AUDIT.tsv` is regenerated from the canonical `chapter.tex` files and records which roles are explicit in each chapter.
"""

REPL=[
(r"\section{Extended solved problems}",r"\section{Solved problems}"),
(r"\section{Solved Problems}",r"\section{Solved problems}"),
(r"\section{Solved problem dossiers}",r"\section{Solved problems}"),
(r"\section{Solved dossiers}",r"\section{Solved problems}"),
(r"\section{Chapter synthesis}",r"\section{Chapter summary}"),
(r"\section{Summary}",r"\section{Chapter summary}"),
]

def ensure_guide(book:Path):
    raw=book.read_text(encoding="utf-8-sig")
    marker=r"\input{frontmatter/chapter-structure-guide.tex}"
    if marker in raw: return
    anchor=r"\input{frontmatter/c04-hypotheses-and-conventions.tex}"
    if anchor in raw:
        raw=raw.replace(anchor,anchor+"\n"+marker,1)
    else:
        anchor=r"\input{frontmatter/publication-and-scope.tex}"
        if anchor in raw: raw=raw.replace(anchor,anchor+"\n"+marker,1)
        else: raw=raw.replace(r"\tableofcontents",r"\tableofcontents"+"\n"+marker,1)
    book.write_text(raw,encoding="utf-8",newline="\n")

def roles(text:str):
    low=text.lower()
    return {
      "context": int(any(x in low for x in ["prerequisite","roadmap","chapter overview","motivation"])),
      "examples": int(r"\begin{example}" in text or r"\section{Examples}" in text),
      "exercises": int(r"\begin{exercise}" in text or r"\section{Exercises}" in text),
      "solved": int(r"\begin{problem}" in text or r"\section{Solved problems}" in text),
      "challenges": int("challenge" in low),
      "summary": int(any(x in low for x in [r"\section{chapter summary}",r"\section{chapter synthesis}",r"\section{summary}"])),
      "bridge": int("bridge to" in low or "what comes next" in low),
    }

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--repo",required=True); a=ap.parse_args()
    repo=Path(a.repo).resolve()

    editorial=repo/"editorial"; editorial.mkdir(parents=True,exist_ok=True)
    (editorial/"C05_CHAPTER_CONTRACT.md").write_text(CONTRACT,encoding="utf-8",newline="\n")

    for d in VOLS:
        v=repo/"books"/d
        fm=v/"frontmatter"; fm.mkdir(parents=True,exist_ok=True)
        (fm/"chapter-structure-guide.tex").write_text(GUIDE,encoding="utf-8",newline="\n")
        ensure_guide(v/"book.tex")

    rows=[]
    changed=0
    for d in VOLS:
        base=repo/"books"/d/"chapters"
        for p in sorted(base.glob("*/chapter.tex")):
            raw=p.read_text(encoding="utf-8")
            new=raw
            for old,newh in REPL:
                new=new.replace(old,newh)
            if new!=raw:
                p.write_text(new,encoding="utf-8",newline="\n")
                changed+=1
            r=roles(new)
            chapter_match=re.search(r"\\chapter\{([^}]*)\}",new)
            title=chapter_match.group(1) if chapter_match else p.parent.name
            explicit=sum(r.values())
            status="CONFORMING" if r["exercises"] and r["summary"] else ("PARTIAL" if explicit>=3 else "MINIMAL")
            rows.append((d,p.parent.name,title,r["context"],r["examples"],r["exercises"],r["solved"],r["challenges"],r["summary"],r["bridge"],status))

    out=repo/"reports"/"series"; out.mkdir(parents=True,exist_ok=True)
    with (out/"C05_CHAPTER_STRUCTURE_AUDIT.tsv").open("w",encoding="utf-8",newline="") as f:
        w=csv.writer(f,delimiter="\t",lineterminator="\n")
        w.writerow(["volume_dir","chapter_dir","title","context_or_roadmap","examples","exercises","solved_problems","challenges","summary","bridge","status"])
        w.writerows(rows)

    print(f"C05 normalized headings in {changed} chapter files and audited {len(rows)} canonical chapters.")
    return 0

if __name__=="__main__": raise SystemExit(main())
