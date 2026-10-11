#!/usr/bin/env python3
"""GA-03i.5: read-only verification of Part V mathematical integration.

--apply writes only a new audit TSV. Does not modify source, prior ledgers, or PDF.
Checks textual integration, consistency of previous ledgers and 114 ID/solution pairs.
It is not a formal proof or imported-source provenance certification.
"""
import argparse
import csv
import re
import sys
from pathlib import Path
from collections import Counter

CHAPTER = Path('books/companion_problems_solutions/chapters/part05_volume_v/chapter.tex')
AUDIT = Path('reports/companion/global_audit')
NOTES = {
    'CP-V-0046': ('CONNECTING_NATURALITY', 'Naturality of the connecting homomorphism.',
                  r'H_{n-1}(a)\circ\partial_n'),
    'CP-V-0114': ('LONG_EXACT_EXT_VARIANCE', 'Variance of Ext and its connecting maps.',
                  r"\operatorname{Ext}_R^i(A',N)"),
    'CP-V-0110': ('DERIVED_FUNCTOR_COMPARISON', 'Chain homotopy versus boundary naturality.',
                  'CP-V-0046'),
    'CP-V-0087': ('INVERSE_LIMIT_CAUTION', 'The obstruction to right exactness.',
                  r'\varprojlim\nolimits^{1} A_n'),
}

def rows_from(path):
    with path.open(encoding='utf-8-sig', newline='') as stream:
        return list(csv.DictReader(stream, delimiter='\t'))

def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--repo', type=Path, default=Path('.'))
    ap.add_argument('--apply', action='store_true', help='write only GA03I5_INTEGRATION_GATE.tsv')
    args = ap.parse_args()
    repo = args.repo.resolve()
    ch = repo / CHAPTER
    checks = []
    def check(label, success, detail):
        checks.append((label, 'PASS' if success else 'FAIL', detail))
    if not ch.is_file():
        sys.exit(f'ERROR: chapter missing: {ch}')
    text = ch.read_text(encoding='utf-8')
    ids = re.findall(r'\\begin\{problem\}\[(CP-V-\d{4})\]', text)
    expected = {f'CP-V-{n:04d}' for n in range(1,115)}
    check('CANONICAL_IDS', len(ids)==114 and set(ids)==expected and len(set(ids))==114,
          f'{len(ids)} IDs, {len(set(ids))} distinct')
    check('SOLUTION_COUNTS', text.count(r'\begin{solution}') ==114 and text.count(r'\end{solution}')==114,
          f"{text.count(r'\begin{solution}')} beginnings, {text.count(r'\end{solution}')} endings")
    pieces={}
    pattern = re.compile(r'\\begin\{problem\}\[(CP-V-\d{4})\]([\s\S]*?)\\end\{problem\}\s*\\begin\{solution\}([\s\S]*?)\\end\{solution\}')
    for match in pattern.finditer(text):
        pieces[match.group(1)] = (match.group(2), match.group(3))
    check('EXACT_PAIRS', len(pieces)==114, f'{len(pieces)} adjacent pairs')
    for pid, (topic, heading, formula) in NOTES.items():
        sol = pieces.get(pid, ('',''))[1]
        ok = heading in sol and formula in sol
        check('NOTE_'+pid, ok, f'{topic}: heading and mathematical anchor '+('present' if ok else 'missing'))
    original = repo/AUDIT/'GA03I_EXACT_SEQUENCE_AUDIT.tsv'
    curated = repo/AUDIT/'GA03I2_NATURALITY_REVIEW.tsv'
    completion = repo/AUDIT/'GA03I3_MATHEMATICAL_COMPLETION.tsv'
    integrated = repo/AUDIT/'GA03I4_CHAPTER_INTEGRATION.tsv'
    for name, path in [('GA03I1',original),('GA03I2',curated),('GA03I3',completion),('GA03I4',integrated)]:
        if not path.is_file():
            check(name, False, f'missing {path}')
            continue
        rows=rows_from(path)
        if name=='GA03I1': ok=len(rows)==26 and Counter(row.get('status') for row in rows)=={'PASS':13,'REVIEW':13}
        elif name=='GA03I2': ok=len(rows)==13 and sum(row.get('review_status')=='EDITORIAL_GAP_OPEN' for row in rows)==4
        elif name=='GA03I3':
            ok=len(rows)==4 and {r.get('topic') for r in rows}=={v[0] for v in NOTES.values()}
        else:
            ok=len(rows)==4 and {r.get('companion_problem_id') for r in rows}==set(NOTES) and all(r.get('integration_status')=='INTEGRATED' for r in rows)
        check(name,ok,f'rows={len(rows)}; expected structure '+('present' if ok else 'not matched'))
    failures = [r for r in checks if r[1]=='FAIL']
    print('GA-03i.5 INTEGRATION GATE')
    for name, status, detail in checks:
        print(f'  {status} {name}: {detail}')
    print(f'  Result: {len(checks)-len(failures)}/{len(checks)} passed')
    if args.apply:
        path=repo/AUDIT/'GA03I5_INTEGRATION_GATE.tsv'
        path.parent.mkdir(parents=True,exist_ok=True)
        with path.open('w',encoding='utf-8',newline='') as f:
            writer=csv.writer(f,delimiter='\t')
            writer.writerow(('check','status','detail'))
            writer.writerows(checks)
        print('  WROTE:',path)
    print('  NOTE: This validates structure/textual integration, not a formal proof or PDF build.')
    if failures: sys.exit(1)

if __name__=='__main__': main()
