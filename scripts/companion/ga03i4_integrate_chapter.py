#!/usr/bin/env python3
"""GA-03i.4: guarded, idempotent integration of four solution notes.
Dry-run default; --apply writes only the canonical Part V chapter and a new ledger.
"""
import argparse, csv, re, sys
from pathlib import Path
CHAPTER=Path('books/companion_problems_solutions/chapters/part05_volume_v/chapter.tex')
LEDGER=Path('reports/companion/global_audit/GA03I4_CHAPTER_INTEGRATION.tsv')
NOTES={
'CP-V-0046':('CONNECTING_NATURALITY',r'''
\medskip
\noindent\textbf{Naturality of the connecting homomorphism.}
Suppose the short exact sequence of complexes above maps to another such
sequence by commuting vertical chain maps $a,b,c$ on the first, middle,
and third complexes, respectively. If $z''$ is a cycle and $z$ is a
lift satisfying $\alpha(z')=dz$, then
\[
\widetilde\alpha(a(z'))=b(\alpha(z'))=d\,b(z),
\qquad \widetilde\beta(b(z))=c(z'').
\]
Thus $b(z)$ lifts $c(z'')$ and its boundary represents $a(z')$.
Consequently the naturality square commutes:
\[
H_{n-1}(a)\circ\partial_n
=\widetilde\partial_n\circ H_n(c).
\]
This requires a morphism of short exact sequences, not merely two
chain-homotopic maps.
'''),
'CP-V-0114':('LONG_EXACT_EXT_VARIANCE',r'''
\medskip
\noindent\textbf{Variance of Ext and its connecting maps.}
For fixed $M$, the functor $\operatorname{Hom}_R(M,-)$ is covariant
and left exact. The associated long exact sequence contains
\[
\operatorname{Ext}_R^i(M,A)
\longrightarrow\operatorname{Ext}_R^i(M,A'')
\xrightarrow{\delta^i}\operatorname{Ext}_R^{i+1}(M,A').
\]
For fixed $N$, the functor $\operatorname{Hom}_R(-,N)$ is
contravariant and left exact. The corresponding long exact sequence
instead contains the connecting map
\[
\operatorname{Ext}_R^i(A',N)
\xrightarrow{\delta_i}\operatorname{Ext}_R^{i+1}(A'',N).
\]
These connecting maps are natural under morphisms of short exact
sequences; their directions reflect the functor's variance.
'''),
'CP-V-0110':('DERIVED_FUNCTOR_COMPARISON',r'''
\medskip
\noindent\textbf{Chain homotopy versus boundary naturality.}
The present argument shows that chain-homotopic maps induce equal
homology maps. By contrast, the naturality assertion for the connecting
map in CP-V-0046 concerns a commuting morphism between two short exact
sequences of chain complexes. It compares two connecting homomorphisms
by transporting a lifted cycle through the vertical chain maps.
These are distinct compatibility statements, neither of which alone
proves the other.
'''),
'CP-V-0087':('INVERSE_LIMIT_CAUTION',r'''
\medskip
\noindent\textbf{The obstruction to right exactness.}
Inverse limits are left exact but not right exact in general.
For inverse systems indexed by the positive integers, the associated
derived-limit sequence contains
\[
\varprojlim B_n\longrightarrow\varprojlim C_n
\longrightarrow\varprojlim\nolimits^{1} A_n.
\]
Thus $\varprojlim^{1} A_n=0$ is sufficient for surjectivity.
The surjective transition maps in part \textbf{(b)} imply this
vanishing; more generally, the Mittag--Leffler condition on the
kernel system suffices in the countable setting. This limitation
contrasts with the exactness of filtered direct limits.
'''),
}
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--repo',type=Path,default=Path('.'));ap.add_argument('--apply',action='store_true');a=ap.parse_args()
    repo=a.repo.resolve();path=repo/CHAPTER
    source=path.read_text(encoding='utf-8');patched=source;rows=[]
    for pid,(topic,note) in NOTES.items():
        needle=r'\begin{problem}['+pid+']'
        start=patched.find(needle)
        if start<0:sys.exit('ERROR missing '+pid)
        stop=patched.find(r'\end{solution}',start)
        nextp=patched.find(r'\begin{problem}',start+len(needle))
        if stop<0 or (nextp>=0 and nextp<stop):sys.exit('ERROR unpaired '+pid)
        block=patched[start:stop]; insertion=note.strip()+'\n\n'
        marker=next(line for line in insertion.splitlines() if line.startswith(r'\noindent\textbf'))
        if insertion in block:state='ALREADY_APPLIED'
        elif marker in block:sys.exit('ERROR conflicting prior note for '+pid)
        else:
            patched=patched[:stop]+insertion+patched[stop:]
            state='PATCH_AVAILABLE'
        rows.append((pid,topic,state))
    ids=re.findall(r'\\begin\{problem\}\[(CP-V-\d{4})\]',patched)
    expected={f'CP-V-{i:04d}' for i in range(1,115)}
    if len(ids)!=114 or set(ids)!=expected or patched.count(r'\begin{solution}')!=114:
        sys.exit('ERROR canonical IDs/solutions changed')
    print('GA-03i.4 GUARDED CHAPTER INTEGRATION')
    for pid,topic,state in rows:print(' ',pid,topic,state)
    print('  114 problems; 114 solutions')
    if not a.apply:
        print('DRY RUN; no files changed');return
    if patched!=source:path.write_text(patched,encoding='utf-8',newline='')
    target=repo/LEDGER;target.parent.mkdir(parents=True,exist_ok=True)
    with target.open('w',encoding='utf-8',newline='') as f:
        w=csv.writer(f,delimiter='\t');w.writerow(['companion_problem_id','topic','integration_status'])
        w.writerows((pid,topic,'INTEGRATED') for pid,topic,_ in rows)
    print('WROTE:',target)
if __name__=='__main__':main()
