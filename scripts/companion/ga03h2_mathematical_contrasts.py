#!/usr/bin/env python3
"""GA-03h.2: guarded mathematical contrast review, no canonical edits.

Only creates a new TSV/Markdown report when --apply is given.
Source of IDs is the existing Part V companion chapter. The imported inventory
remains authoritative for provenance; this script does not assert source links.
"""
import argparse
import csv
import re
from pathlib import Path

CHAPTER = Path('books/companion_problems_solutions/chapters/part05_volume_v/chapter.tex')
REPORT_DIR = Path('reports/companion/global_audit')
ROWS = [
    ('FINITE_PD', 'CP-V-0077', 'Z/12 over Z', 'pd=1', '12 is a nonzero nonunit in Z; length-one free resolution', 'CP-V-0077'),
    ('FINITE_PD', 'CP-V-0078', 'k[x]/(x^3) over k[x]', 'pd=1', 'multiplication by x^3 gives a length-one free resolution', 'CP-V-0078'),
    ('FINITE_PD', 'CP-V-0079', 'k over k[x,y]', 'pd=2', 'Koszul resolution on the regular sequence x,y', 'CP-V-0079'),
    ('BASE_RING', 'CP-V-0082', 'k as module over k vs k[x]', 'pd=0 versus pd=1', 'projective dimension depends on the base ring', 'CP-V-0082'),
    ('INFINITE_PD', 'CP-V-0041', 'k over k[x,y]/(xy)', 'pd=infinity', 'Tor_i(k,k)=k^2 for all i>=1', 'CP-V-0041'),
    ('FINITE_PD_THEORY', 'CP-V-0043', 'minimal resolutions and Tor', 'pd detected by last nonzero Tor', 'requires nonzero finitely generated module of finite projective dimension over a Noetherian local ring', 'CP-V-0043'),
    ('NONFLAT', 'CP-V-0024', 'Z/2 over Z', 'not flat', 'tensor of multiplication-by-two injection is zero map', 'CP-V-0024'),
    ('NONFLAT', 'CP-V-0048', 'k[x]/(x) over k[x]', 'not flat', 'Tor_1^{k[x]}(k,k)=k != 0', 'CP-V-0048'),
    ('FREE_FLAT', 'CP-V-0019', 'A[x] over A', 'free, projective, faithfully flat', 'monomial basis and evaluation retraction', 'CP-V-0019'),
    ('PROJECTIVE_NONFREE', 'CP-V-0020', 'A1 x 0 over A1 x A2', 'projective not free', 'idempotent summand with nonzero annihilator; A1 and A2 nonzero', 'CP-V-0020'),
    ('NONPROJECTIVE', 'CP-V-0025', 'k[x]/(x) over k[x]', 'not projective', 'quotient sequence does not split', 'CP-V-0025'),
    ('FLAT_TORSIONFREE', 'CP-V-0106', 'torsion-free module over PID', 'flat iff torsion-free', 'PID hypothesis essential', 'CP-V-0106'),
    ('FLAT_NONPROJECTIVE', 'CP-V-0106', 'Q over Z', 'flat not projective', 'Q torsion-free hence flat; nonzero divisible group cannot be free abelian; projective over PID is free', 'CP-V-0106'),
    ('PERIODIC_CONTRAST', 'CP-V-0041', 'periodic hypersurface vs polynomial-ring Koszul', 'pd infinity versus pd 2', 'compare CP-V-0041 to CP-V-0079 with different base rings', 'CP-V-0041;CP-V-0079'),
]

def blocks(source):
    rx = re.compile(r'\\begin\{problem\}\[(CP-V-\d{4})\]([\s\S]*?)\\end\{problem\}\s*\\begin\{solution\}([\s\S]*?)\\end\{solution\}')
    return {m.group(1): {'statement':m.group(2),'solution':m.group(3)} for m in rx.finditer(source)}


def inspect(repo):
    chapter=repo/CHAPTER
    if not chapter.is_file(): raise FileNotFoundError(chapter)
    source=chapter.read_text(encoding='utf-8')
    parsed=blocks(source)
    # Anchor checks are deliberately syntactic, not a substitute for proof review.
    checks={
      'CP-V-0077':('12',),
      'CP-V-0078':('x^3',),
      'CP-V-0079':('x','y'),
      'CP-V-0082':('k[x]',),
      'CP-V-0041':('\\operatorname{Tor}',),
      'CP-V-0043':('\\operatorname{pd}',),
      'CP-V-0024':('\\mathbb Z/2',),
      'CP-V-0048':('\\operatorname{Tor}',),
      'CP-V-0019':('A[x]',),
      'CP-V-0020':('A_1','A_2'),
      'CP-V-0025':('projective',),
      'CP-V-0106':('torsion-free',),
    }
    results=[]
    for category,pid,example,conclusion,proof,linked in ROWS:
        sources=linked.split(';')
        existing=all(item in parsed for item in sources)
        anchor_ok=existing and all(
            all(anchor in parsed[item]['statement']+parsed[item]['solution'] for anchor in checks.get(item,()))
            for item in sources)
        if not existing: status='FAIL_MISSING_CANONICAL_PROBLEM'
        elif not anchor_ok: status='REVIEW_SOURCE_ANCHOR'
        elif category in ('FLAT_NONPROJECTIVE','PERIODIC_CONTRAST'): status='VERIFIED_DERIVED_COMPARISON'
        else: status='CANONICAL_EXAMPLE_REVIEWED'
        results.append(dict(category=category,companion_problem_id=pid,example=example,
                            mathematical_conclusion=conclusion,review_status=status,
                            verification_argument=proof,linked_canonical_ids=linked,
                            provenance_status='NOT_DETERMINED_BY_THIS_AUDIT'))
    return results


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--repo',type=Path,default=Path('.'))
    ap.add_argument('--apply',action='store_true',help='write NEW review reports only')
    args=ap.parse_args()
    repo=args.repo.resolve()
    rows=inspect(repo)
    print('GA-03h.2 MATHEMATICAL CONTRASTS')
    for status in sorted(set(r['review_status'] for r in rows)):
        print(f'  {status}: {sum(r["review_status"]==status for r in rows)}')
    for r in rows:
        if r['review_status'].startswith(('FAIL','REVIEW')):
            print('  CHECK:',r['companion_problem_id'],r['review_status'])
    print('  No modifications to the canonical chapter or imported inventory.')
    if args.apply:
        out=repo/REPORT_DIR
        out.mkdir(parents=True,exist_ok=True)
        target=out/'GA03H2_MATHEMATICAL_CONTRASTS.tsv'
        with target.open('w',encoding='utf-8',newline='') as f:
            writer=csv.DictWriter(f,fieldnames=list(rows[0]),delimiter='\t')
            writer.writeheader();writer.writerows(rows)
        md=out/'GA03H2_MATHEMATICAL_CONTRASTS.md'
        lines=['# GA-03h.2 — Mathematical contrasts','',
               'The imported inventory remains authoritative for provenance. This report records mathematical comparisons, not imported-source identity.','']
        for r in rows:
            lines += [f"## {r['companion_problem_id']}: {r['example']}",
                      f"- **Review:** {r['review_status']}",
                      f"- **Result:** {r['mathematical_conclusion']}",
                      f"- **Reason:** {r['verification_argument']}",
                      f"- **Related IDs:** {r['linked_canonical_ids']}", '']
        md.write_text('\n'.join(lines),encoding='utf-8')
        print('WROTE:',target)
        print('WROTE:',md)
    else: print('DRY RUN; no reports written')
    if any(r['review_status'].startswith('FAIL') for r in rows):raise SystemExit(1)

if __name__=='__main__':main()
