#!/usr/bin/env python3
"""GA-03d: guarded correction of CP-V-0061, CP-V-0075 and CP-V-0076.
Dry-run by default. Use --apply to write. Does not touch any other problem.
"""
import argparse
from pathlib import Path
import re

ROOT = Path('books/companion_problems_solutions/chapters/part05_volume_v/chapter.tex')
REPLACEMENTS = {
'CP-V-0061': r'''\begin{problem}[CP-V-0061]
\label{prob:cp-v-0061}
Determine whether
\[
\frac{x^2+1}{x-2}
\]
belongs to
\[
k[x]_{(x)}
\qquad\text{and}\qquad
k[x]_{(x-2)}.
\]
State any dependence on the characteristic of the field $k$.
\end{problem}

\begin{solution}
Work in $k(x)$ and cancel common factors before testing membership.
For the localization at $(x)$, the denominator $x-2$ is a unit precisely
when $-2\ne0$ in $k$. When $\operatorname{char}(k)=2$, the fraction is
$(x^2+1)/x$, whose numerator has nonzero value $1$ at $0$; it does not
belong to $k[x]_{(x)}$. Hence
\[
\boxed{\frac{x^2+1}{x-2}\in k[x]_{(x)}
\iff \operatorname{char}(k)\ne2.}
\]
At $(x-2)$, the simple factor $x-2$ must cancel with the numerator.
The factor theorem gives
\[
(x-2)\mid(x^2+1)\iff 2^2+1=5=0\text{ in }k.
\]
In characteristic $5$, $x^2+1=(x-2)(x+2)$, so the fraction equals
$x+2$ in $k(x)$; otherwise its denominator retains a factor $x-2$.
Therefore
\[
\boxed{\frac{x^2+1}{x-2}\in k[x]_{(x-2)}
\iff\operatorname{char}(k)=5.}
\]
\end{solution}''',
'CP-V-0075': r'''\begin{problem}[CP-V-0075]
\label{prob:cp-v-0075}
Let $A=k[x]$, $\mathfrak p=(x-a)$, and let $f,g\in k[x]$ with $g\ne0$.
\textbf{(a)} Show that $g(a)\ne0$ is sufficient for the displayed
fraction $f/g$ to belong to $A_{\mathfrak p}$.
\textbf{(b)} Prove that $f/g\in A_{\mathfrak p}$ if and only if,
after cancellation to coprime numerator and denominator, the
reduced denominator does not vanish at $a$.
\textbf{(c)} Give an example showing why $g(a)\ne0$ is not necessary
for an arbitrary presentation $f/g$.
\end{problem}

\begin{solution}
Set $S=k[x]\setminus(x-a)$. If $g(a)\ne0$, then $g\in S$, so
$f/g$ is represented by an element of $S^{-1}k[x]$.
Write $f/g=u/v$ with $\gcd(u,v)=1$ in the PID $k[x]$.
If $v(a)\ne0$, then $v\in S$ and $u/v$ is in the localization.
Conversely, if $u/v=h/s$ with $s(a)\ne0$, then $su=vh$.
Coprimality gives $v\mid s$, hence $v(a)\ne0$.
Thus
\[
\boxed{f/g\in k[x]_{(x-a)}\iff v(a)\ne0
\quad\text{for a coprime presentation }f/g=u/v.}
\]
For instance $f=g=x-a$ gives $f/g=1$ in the fraction field,
although $g(a)=0$. This shows why the test on the original
unreduced denominator is only sufficient.
\end{solution}''',
'CP-V-0076': r'''\begin{problem}[CP-V-0076]
\label{prob:cp-v-0076}
Let $A=k[x,y]$, $\mathfrak m=(x-a,y-b)$, and let $f,g\in A$ with $g\ne0$.
\textbf{(a)} Show that $g(a,b)\ne0$ is sufficient for $f/g\in A_{\mathfrak m}$.
\textbf{(b)} Prove that $f/g\in A_{\mathfrak m}$ precisely when it
admits a presentation $h/s$ with $s(a,b)\ne0$.
\textbf{(c)} Explain why the displayed denominator $g$ may vanish
at $(a,b)$ even if the rational function belongs to the local ring.
\end{problem}

\begin{solution}
The localization is $S^{-1}A$ for
$S=A\setminus\mathfrak m=\{s\in A:s(a,b)\ne0\}$.
Thus if $g(a,b)\ne0$, the displayed fraction is a valid localization
representative. More generally, a rational function $f/g\in k(x,y)$
belongs to $S^{-1}A$ exactly when there exist $h\in A$ and $s\in S$
with $f/g=h/s$ in $k(x,y)$, equivalently $sf=hg$ in $A$.
The latter criterion makes no assumption that $g\in S$.
For example,
\[
\frac{x-a}{x-a}=1\in A_{\mathfrak m},
\]
while the displayed denominator vanishes at $(a,b)$.
In particular, an arbitrary unreduced denominator cannot provide a
necessary membership test.
\end{solution}'''
}
GUARDS = {
'CP-V-0061': ('(x-2)(0)=-2\\neq 0', 'x-2\\in (x-2)'),
'CP-V-0075': ('g(a)\\neq 0', 'By the factor theorem'),
'CP-V-0076': ('g(a,b)\\neq 0', 'consists exactly of those polynomials'),
}

def patch(data):
    updated=data
    for pid, replacement in REPLACEMENTS.items():
        pat=re.compile(r'\\begin\{problem\}\[' + re.escape(pid) + r'\][\s\S]*?\\end\{problem\}\s*\\begin\{solution\}[\s\S]*?\\end\{solution\}')
        matches=list(pat.finditer(updated))
        if len(matches)!=1:
            raise ValueError(f'{pid}: expected exactly one problem/solution pair, found {len(matches)}')
        old=matches[0].group()
        if old==replacement:
            print(f'{pid}: ALREADY_CORRECTED')
            continue
        if not all(marker in old for marker in GUARDS[pid]):
            raise ValueError(f'{pid}: source guards failed; refusing to overwrite')
        updated=updated[:matches[0].start()]+replacement+updated[matches[0].end():]
        print(f'{pid}: PATCH_AVAILABLE')
    return updated

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--repo',type=Path,default=Path('.'))
    ap.add_argument('--apply',action='store_true')
    args=ap.parse_args()
    target=args.repo/ROOT
    original=target.read_text(encoding='utf-8-sig')
    result=patch(original)
    if result==original:
        print('NO CHANGES')
    elif args.apply:
        with target.open('w',encoding='utf-8',newline='') as f: f.write(result)
        print('APPLIED:',target)
    else:
        print('DRY RUN: no changes; add --apply')
if __name__=='__main__': main()
