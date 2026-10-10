#!/usr/bin/env python3
"""GA-03g.4: guarded non-destructive hypothesis clarifications in Part V.

Edits exactly two canonical problem statements on --apply, plus a new audit TSV.
Does not touch solutions, source imports, prior audit ledgers, or unrelated files.
Dry run by default; applying twice is safe.
"""
import argparse
import csv
import hashlib
import re
import sys
from pathlib import Path

CHAPTER = Path('books/companion_problems_solutions/chapters/part05_volume_v/chapter.tex')
REPORT = Path('reports/companion/global_audit/GA03G4_HYPOTHESIS_CORRECTIONS.tsv')

CHANGES = [
    (
        'CP-V-0043',
        'NONZERO_MODULE_HYPOTHESIS',
        'Let \\( (A,\\mathfrak m) \\) be a Noetherian local ring',  # not used; exact string below
        r'and let \(M\) be a finitely generated \(A\)-module with finite projective'
        '\n' r'dimension.',
        r'and let \(M\ne0\) be a finitely generated \(A\)-module with finite projective'
        '\n' r'dimension.',
        'Exclude M=0 for the finite-length/minimum Tor characterization under the standard nonnegative projective-dimension convention.',
    ),
    (
        'CP-V-0113',
        'POSITIVE_INTEGER_PARAMETERS',
        '',
        'Compute\n' + r'\[' + '\n' + r'\operatorname{Ext}^1_{\mathbb Z}(\mathbb Z/n\mathbb Z,\mathbb Z/m\mathbb Z).',
        'Let \\(n,m\\ge1\\) be integers. Compute\n' + r'\[' + '\n' + r'\operatorname{Ext}^1_{\mathbb Z}(\mathbb Z/n\mathbb Z,\mathbb Z/m\mathbb Z).',
        'Specify n,m>=1, required by the cyclic-module resolution and gcd formula.',
    ),
]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--repo', type=Path, default=Path('.'))
    ap.add_argument('--apply', action='store_true', help='apply precisely guarded edits and write GA03G4 TSV')
    args = ap.parse_args()
    repo = args.repo.resolve()
    chapter = repo / CHAPTER
    if not chapter.is_file():
        sys.exit('ERROR chapter missing: ' + str(chapter))
    original = chapter.read_text(encoding='utf-8')
    newline = '\r\n' if '\r\n' in original else '\n'
    updated = original
    records = []
    for pid, code, _, old, new, reason in CHANGES:
        a = updated.find(r'\begin{problem}[' + pid + ']')
        if a == -1:
            sys.exit('ERROR missing problem: ' + pid)
        b = updated.find(r'\end{problem}', a)
        if b == -1:
            sys.exit('ERROR missing end of problem: ' + pid)
        block = updated[a:b]
        before = old.replace('\n', newline)
        after = new.replace('\n', newline)
        if block.count(after) == 1:
            status = 'ALREADY_APPLIED'
        elif block.count(before) == 1:
            status = 'PATCH_AVAILABLE'
            fixed = block.replace(before, after, 1)
            updated = updated[:a] + fixed + updated[b:]
        else:
            sys.exit('ERROR unexpected statement for ' + pid + '; no changes written')
        records.append(dict(problem_id=pid, check=code, status=status, reason=reason))
    oldids = re.findall(r'\\begin\{problem\}\[(CP-V-\d{4})\]', original)
    newids = re.findall(r'\\begin\{problem\}\[(CP-V-\d{4})\]', updated)
    if oldids != newids or len(oldids) != 114 or len(set(oldids)) != 114:
        sys.exit('ERROR canonical ID inventory mismatch; no changes written')
    if updated.count(r'\begin{solution}') != original.count(r'\begin{solution}'):
        sys.exit('ERROR solution count changed; no changes written')
    print('GA-03g.4 — HYPOTHESIS CLARIFICATIONS')
    for row in records:
        print(row['problem_id'], row['status'], row['check'])
    print('Canonical IDs:',len(newids),'; unchanged:',oldids==newids)
    print('Original SHA256:',hashlib.sha256(original.encode('utf-8')).hexdigest())
    if not args.apply:
        print('DRY RUN; no files changed')
        return
    if updated != original:
        with chapter.open('w', encoding='utf-8', newline='') as f:
            f.write(updated)
        print('PATCHED:',chapter)
    else:
        print('NO CHAPTER CHANGE: already patched')
    report = repo / REPORT
    report.parent.mkdir(parents=True, exist_ok=True)
    with report.open('w', encoding='utf-8', newline='') as f:
        w = csv.DictWriter(f, fieldnames=list(records[0]), delimiter='\t')
        w.writeheader()
        w.writerows(records)
    print('WROTE:',report)

if __name__ == '__main__':
    main()
