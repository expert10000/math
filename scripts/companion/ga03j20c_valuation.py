#!/usr/bin/env python3
"""GA-03j.20c: patch only CP-V-0035 after 20a+20b. Dry-run by default.

Checks immutable baseline/20a/20b backups, all 114 adjacent pairs, and
that the only changes since 20b's backup are CP-V-0084 and CP-V-0085.
Does not certify mathematics or commit changes.
"""
import argparse
import csv
import difflib
import hashlib
import json
import re
from pathlib import Path

CH = Path('books/companion_problems_solutions/chapters/part05_volume_v/chapter.tex')
AUD = Path('reports/companion/global_audit')
ORIGINAL_SHA = '769a30e7d711ac34dfa24ddbfcc8410605f308d36a6d7ec3f59f1f4c703feb0b'
PAIR = re.compile(r'\\begin\{problem\}\[(CP-V-\d{4})\]([\s\S]*?)\\end\{problem\}\s*\\begin\{solution\}([\s\S]*?)\\end\{solution\}')
REPLACEMENT = r'''\begin{solution}
For \textbf{(a)}, let \(\mathcal C\) be an arbitrary chain of local
subrings of \(K\), ordered by domination. Set
\[
A=\bigcup_{R\in\mathcal C}R,
\qquad
\mathfrak m=\bigcup_{R\in\mathcal C}\mathfrak m_R.
\]
The domination condition makes these maximal ideals compatible under
contraction, so \(\mathfrak m\) is an ideal of \(A\). Every element of
\(A\setminus\mathfrak m\) is a unit in a member of the chain, hence
in \(A\). Thus \(A\) is local and dominates every member of
\(\mathcal C\). The chain has an upper bound. Zorn's lemma gives a
maximal element of \(\Sigma\).

For \textbf{(b)}, write \((V,\mathfrak m)\) for a maximal local subring
and fix \(x\in K^\times\) with \(x\notin V\). Suppose that
\(\mathfrak mV[x]\) were a proper ideal of \(V[x]\). Choose a
maximal ideal \(\mathfrak n\) containing it. Since
\(\mathfrak m\subseteq\mathfrak n\cap V\) and \(\mathfrak m\) is
maximal in \(V\), we have \(\mathfrak n\cap V=\mathfrak m\).
The local ring \(V[x]_{\mathfrak n}\subseteq K\) therefore dominates
\(V\) properly, contrary to maximality. Consequently
\[
\mathfrak mV[x]=V[x].
\]
There are \(a_0,\ldots,a_n\in\mathfrak m\) with
\[
1=a_0+a_1x+\cdots+a_nx^n,
\qquad n\ge1.
\]
Since \(1-a_0\) is a unit in \(V\), division by \(1-a_0\)
and multiplication by \(x^{-n}\) give a monic equation
\[
(x^{-1})^n-
\frac{a_1}{1-a_0}(x^{-1})^{n-1}-\cdots-
\frac{a_n}{1-a_0}=0.
\]
Thus \(x^{-1}\) is integral over \(V\). The ring \(V[x^{-1}]\)
is consequently finite and integral over \(V\). By lying over, there
is a prime \(\mathfrak q\subseteq V[x^{-1}]\) contracting to
\(\mathfrak m\). The local ring
\(V[x^{-1}]_{\mathfrak q}\subseteq K\) dominates \(V\).
Maximality forces it to equal \(V\), so \(x^{-1}\in V\).
Therefore, for every \(x\in K^\times\), either \(x\in V\) or
\(x^{-1}\in V\): \(V\) is a valuation ring.

For \textbf{(c)}, let \((V,\mathfrak m_V)\) be a valuation ring,
and suppose a local subring \((B,\mathfrak m_B)\subseteq K\)
dominates it. If \(x\in B\setminus V\), then
\(x^{-1}\in V\), and in fact \(x^{-1}\in\mathfrak m_V\):
otherwise \(x^{-1}\) would be a unit in \(V\), giving \(x\in V\).
But domination implies
\(x^{-1}\in\mathfrak m_B\), whereas its inverse \(x\) belongs
to \(B\). This is impossible in a local ring. Thus \(B=V\),
so \(V\) is maximal under domination.
\end{solution}'''


def parsed(s):
    mm = list(PAIR.finditer(s))
    ids = [m.group(1) for m in mm]
    expected = {f'CP-V-{i:04d}' for i in range(1, 115)}
    if len(mm) != 114 or set(ids) != expected or len(set(ids)) != 114:
        raise ValueError('Canonical 114 problem/solution pair integrity failed')
    return {m.group(1): m for m in mm}


def sha(b):
    return hashlib.sha256(b).hexdigest()


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--repo', type=Path, default=Path('.'))
    ap.add_argument('--apply', action='store_true')
    ap.add_argument('--show-diff', action='store_true')
    args = ap.parse_args()
    root = args.repo.resolve()
    required = [
        AUD/'GA03J19_CONSOLIDATED_114_LEDGER.tsv',
        AUD/'GA03J19_COVERAGE_STATUS.json',
        AUD/'GA03J20A_ORIGINAL_CHAPTER.tex',
        AUD/'GA03J20A_PATCH_MANIFEST.tsv',
        AUD/'GA03J20B_ORIGINAL_CHAPTER.tex',
        AUD/'GA03J20B_PATCH_MANIFEST.json',
    ]
    for path in required:
        if not (root/path).is_file():
            raise ValueError(f'Missing prerequisite {path}; complete GA-03j.20a/20b first')
    pristine = (root/AUD/'GA03J20A_ORIGINAL_CHAPTER.tex').read_bytes()
    if sha(pristine) != ORIGINAL_SHA:
        raise ValueError('GA03J20A backup differs from authoritative initial SHA')
    original = parsed(pristine.decode('utf-8'))
    a_bytes = (root/AUD/'GA03J20B_ORIGINAL_CHAPTER.tex').read_bytes()
    a_pairs = parsed(a_bytes.decode('utf-8'))
    a_modified = {k for k in original if original[k].group(0) != a_pairs[k].group(0)}
    if a_modified != {'CP-V-0003','CP-V-0034','CP-V-0037','CP-V-0051'}:
        raise ValueError('GA03J20A patch not exactly the expected four problems')
    a_manifest = (root/AUD/'GA03J20A_PATCH_MANIFEST.tsv').read_text(encoding='utf-8-sig')
    if not all(i in a_manifest for i in a_modified):
        raise ValueError('GA03J20A manifest incomplete')
    b_manifest = json.loads((root/AUD/'GA03J20B_PATCH_MANIFEST.json').read_text(encoding='utf-8'))
    raw = (root/CH).read_bytes()
    if b_manifest.get('after_sha256') != sha(raw):
        raise ValueError('Current chapter does not match GA03J20B after SHA')
    current = parsed(raw.decode('utf-8'))
    b_modified = {k for k in current if current[k].group(0) != a_pairs[k].group(0)}
    if b_modified != {'CP-V-0084','CP-V-0085'}:
        raise ValueError('Current chapter not the expected GA03J20B two-problem patch')
    with (root/required[0]).open(encoding='utf-8-sig', newline='') as f:
        rows = list(csv.DictReader(f, delimiter='\t'))
    if len(rows) != 114 or any(r.get('review_coverage') != 'INITIAL_TARGETED_REVIEW' for r in rows):
        raise ValueError('GA03J19 must have all 114 initial reviews')
    old = current['CP-V-0035']
    if ('maximality/domination argument' not in old.group(3)
            or 'Zorn' not in old.group(3)
            or 'valuation-ring dichotomy' not in old.group(3)):
        raise ValueError('CP-V-0035 source anchors unexpected; review manually')
    fragment = old.group(0)
    new_fragment = fragment[:fragment.index('\\begin{solution}')] + REPLACEMENT
    src = raw.decode('utf-8')
    result = src[:old.start()] + new_fragment + src[old.end():]
    final = parsed(result)
    changed = {k for k in current if current[k].group(0) != final[k].group(0)}
    if changed != {'CP-V-0035'}:
        raise ValueError('Unexpected modified IDs: '+repr(changed))
    after = result.encode('utf-8')
    summary = {'milestone':'GA-03j.20c','mode':'APPLY' if args.apply else 'DRY_RUN',
        'before_sha256':sha(raw),'after_sha256':sha(after),'changed_problem_ids':['CP-V-0035'],
        'canonical_problem_solution_pairs':114,'independent_math_certification':'PENDING'}
    print(json.dumps(summary, indent=2))
    diff = ''.join(difflib.unified_diff(src.splitlines(keepends=True),result.splitlines(keepends=True),
                       fromfile='a/chapter.tex',tofile='b/chapter.tex'))
    if args.show_diff:print(diff)
    if not args.apply:return
    targets = [root/AUD/'GA03J20C_ORIGINAL_CHAPTER.tex',root/AUD/'GA03J20C_PATCH.diff',root/AUD/'GA03J20C_PATCH_MANIFEST.json']
    if any(p.exists() for p in targets):
        raise ValueError('GA03J20C output already exists; refusing overwrite')
    targets[0].write_bytes(raw)
    targets[1].write_text(diff,encoding='utf-8')
    targets[2].write_text(json.dumps(summary,indent=2)+'\n',encoding='utf-8')
    (root/CH).write_bytes(after)
    if sha((root/CH).read_bytes()) != sha(after):
        raise RuntimeError('Post-write hash mismatch. Restore GA03J20C_ORIGINAL_CHAPTER.tex')
    print('WROTE canonical CP-V-0035 correction plus guarded backup/diff/manifest')


if __name__ == '__main__':
    main()
