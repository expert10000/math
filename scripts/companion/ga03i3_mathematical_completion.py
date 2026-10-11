#!/usr/bin/env python3
"""GA-03i.3: verify and document four mathematical editorial gaps.

--apply creates a new TSV and Markdown report; never modifies the chapter,
prior ledgers, or imported inventory. It does not claim chapter gaps closed.
"""
import argparse
import csv
import re
from pathlib import Path

BASE = Path('reports/companion/global_audit')
SOURCE = BASE / 'GA03I2_NATURALITY_REVIEW.tsv'
CHAPTER = Path('books/companion_problems_solutions/chapters/part05_volume_v/chapter.tex')
OUT_TSV = BASE / 'GA03I3_MATHEMATICAL_COMPLETION.tsv'
OUT_MD = BASE / 'GA03I3_MATHEMATICAL_COMPLETION.md'

GAPS = [
    ('CONNECTING_NATURALITY', ('CP-V-0046',),
     'MATHEMATICALLY_VERIFIED_CHAPTER_EXPOSITION_PENDING',
     'For a morphism of short exact sequences of chain complexes, H_{n-1}(a) composed with boundary equals new_boundary composed with H_n(c).',
     r'''### Connecting-map naturality
Consider a commutative morphism from a short exact sequence
\(0\to C'\xrightarrow{\alpha}C\xrightarrow{\beta}C''\to0\)
to \(0\to D'\xrightarrow{\alpha'}D\xrightarrow{\beta'}D''\to0\),
with chain maps \(a,b,c\) in the three columns. For a homology class
\([z'']\in H_n(C'')\), choose \(z\in C_n\) with \(\beta(z)=z''\).
The top connecting class is represented by \(z'\) such that
\(\alpha(z')=d_Cz\). Commutativity yields
\[
\alpha'(a(z'))=b(\alpha(z'))=b(d_Cz)=d_D(b(z)),
\qquad \beta'(b(z))=c(z'').
\]
Thus the bottom connecting map applied to \([c(z'')]\) is represented
by \(a(z')\), proving
\[
\boxed{H_{n-1}(a)\circ\partial_n
=\widetilde{\partial}_n\circ H_n(c).}
\]
The statement is independent of choices because both connecting
homomorphisms are well defined.'''),
    ('LONG_EXACT_EXT_VARIANCE', ('CP-V-0114','CP-V-0113'),
     'MATHEMATICALLY_VERIFIED_CHAPTER_EXPOSITION_PENDING',
     'Ext^i_R(M,-) is covariant and Ext^i_R(-,N) is contravariant. Both have long exact sequences; the first-variable sequence reverses the original short exact arrows.',
     r'''### Ext variance and connecting maps
For fixed \(M\), the covariant cohomological functor
\(\operatorname{Ext}_R^i(M,-)\) sends
\(0\to A'\to A\to A''\to0\) to a long exact sequence with
\[
\operatorname{Ext}_R^i(M,A)\to
\operatorname{Ext}_R^i(M,A'')\xrightarrow{\delta^i}
\operatorname{Ext}_R^{i+1}(M,A')\to
\operatorname{Ext}_R^{i+1}(M,A).
\]
For fixed \(N\), the contravariant functor
\(\operatorname{Ext}_R^i(-,N)\) yields, for the same short exact
sequence of modules,
\[
\operatorname{Ext}_R^i(A,N)\to
\operatorname{Ext}_R^i(A',N)\xrightarrow{\delta^i}
\operatorname{Ext}_R^{i+1}(A'',N)\to
\operatorname{Ext}_R^{i+1}(A,N).
\]
Both long exact sequences are natural in morphisms of short exact
sequences. For commutative rings these constructions are valid in the
usual module category (and with appropriate left/right module
conventions more generally).'''),
    ('DERIVED_FUNCTOR_COMPARISON', ('CP-V-0110','CP-V-0046'),
     'MATHEMATICALLY_VERIFIED_CHAPTER_EXPOSITION_PENDING',
     'Chain-homotopy invariance identifies maps induced by homotopic chain maps; connecting-map naturality compares maps arising from morphisms of short exact sequences. Neither property implies the other by itself.',
     r'''### Chain homotopy versus naturality
A chain homotopy \(f-g=d_Dh+hd_C\) implies that for every cycle
\(z\), \((f-g)(z)=d_Dh(z)\), so \(H_n(f)=H_n(g)\).
This fact does not, by itself, prove the commuting identity for
connecting homomorphisms. Connecting-map naturality requires a
commutative diagram of *short exact sequences of complexes* and the
lift-and-boundary argument above. The two facts serve different
functorial purposes.'''),
    ('INVERSE_LIMIT_CAUTION', ('CP-V-0087','CP-V-0031'),
     'MATHEMATICALLY_VERIFIED_CHAPTER_EXPOSITION_PENDING',
     'Inverse limits are left exact, but not generally right exact. In standard countable towers a Mittag-Leffler kernel system makes lim^1 vanish; completion exactness also uses Noetherian/Artin-Rees hypotheses.',
     r'''### Inverse limits and completion
For a short exact sequence of inverse systems
\(0\to A_n\to B_n\to C_n\to0\), taking inverse limits gives
\[
0\to\varprojlim A_n\to\varprojlim B_n\to\varprojlim C_n,
\]
but the final map need not be surjective. For ordinary countable
towers the derived-limit exact sequence continues
\[
\varprojlim B_n\to\varprojlim C_n\to
\varprojlim{}^1 A_n\to\varprojlim{}^1 B_n\to\cdots.
\]
A Mittag--Leffler condition on \((A_n)\), such as surjective
transition maps, ensures \(\varprojlim{}^1 A_n=0\) and hence
surjectivity of \(\varprojlim B_n\to\varprojlim C_n\).
For completion of finitely generated modules over a Noetherian ring,
Artin--Rees gives the cofinality needed to compare induced and
intrinsic filtrations; this is distinct from asserting that inverse
limits are always exact.'''),
]

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--repo', type=Path, default=Path('.'))
    ap.add_argument('--apply', action='store_true')
    args=ap.parse_args()
    repo=args.repo.resolve()
    source=repo/SOURCE
    chapter=repo/CHAPTER
    if not source.is_file() or not chapter.is_file():
        ap.error('GA-03i.2 TSV or canonical chapter missing')
    with source.open(encoding='utf-8-sig',newline='') as fh:
        rows=list(csv.DictReader(fh,delimiter='\t'))
    expected=[x for x in rows if x.get('item_type')=='EDITORIAL_GAP']
    got={x.get('topic'): x for x in expected}
    if len(expected)!=4 or len(got)!=4:
        ap.error('GA-03i.2 editorial gap count is not exactly four')
    text=chapter.read_text(encoding='utf-8')
    ids=re.findall(r'\\begin\{problem\}\[(CP-V-\d{4})\]', text)
    if len(ids)!=114 or len(set(ids))!=114:
        ap.error('Canonical chapter count or uniqueness changed')
    results=[]
    for topic,linked,status,math_note,_ in GAPS:
        prior=got.get(topic)
        if prior is None or prior.get('review_status')!='EDITORIAL_GAP_OPEN':
            ap.error(f'Unexpected prior classification: {topic}')
        if any(pid not in ids for pid in linked):
            ap.error(f'Canonical problem missing for {topic}')
        results.append(dict(topic=topic,linked_problem_ids=';'.join(linked),
                            prior_status=prior['review_status'],
                            mathematical_review_status=status,
                            chapter_integration_status='NOT_APPLIED',
                            mathematical_finding=math_note))
    print('GA-03i.3 MATHEMATICAL COMPLETION')
    print(f'  canonical problems: {len(ids)}; gaps reviewed: {len(results)}')
    print('  mathematical treatment prepared; chapter integration remains pending')
    if args.apply:
        out=repo/OUT_TSV
        out.parent.mkdir(parents=True,exist_ok=True)
        with out.open('w',encoding='utf-8',newline='') as fh:
            writer=csv.DictWriter(fh,fieldnames=list(results[0]),delimiter='\t')
            writer.writeheader(); writer.writerows(results)
        md=['# GA-03i.3 — Mathematical completion of four editorial gaps','',
            'The arguments below are mathematical audit notes, not yet modifications to canonical problems.',
            'All four issues require a separate editorial decision before insertion into Part V.','']
        for _,_,_,_,proof in GAPS:
            md.extend([proof,''])
        (repo/OUT_MD).write_text('\n'.join(md)+'\n',encoding='utf-8')
        print('  WROTE:',out)
        print('  WROTE:',repo/OUT_MD)
    else:
        print('  DRY RUN; no files changed')

if __name__=='__main__':
    main()
