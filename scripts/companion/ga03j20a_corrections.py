#!/usr/bin/env python3
"""GA-03j.20a: four strictly scoped mathematics fixes. Dry run by default.

Requires GA03J19 114-row coverage ledger and canonical prepatch SHA.
Apply writes a backup, diff, manifest, then the canonical chapter.
Does not certify the corrected proofs or modify imported sources.
"""
import argparse, csv, hashlib, difflib, json, re
from pathlib import Path
CH = Path('books/companion_problems_solutions/chapters/part05_volume_v/chapter.tex')
AUD = Path('reports/companion/global_audit')
OLD_SHA = '769a30e7d711ac34dfa24ddbfcc8410605f308d36a6d7ec3f59f1f4c703feb0b'
PAIR = re.compile(r'\\begin\{problem\}\[(CP-V-\d{4})\]([\s\S]*?)\\end\{problem\}\s*\\begin\{solution\}([\s\S]*?)\\end\{solution\}')

def pairs(s):
    matches = list(PAIR.finditer(s))
    expected = {f'CP-V-{i:04d}' for i in range(1,115)}
    if len(matches) != 114 or {m.group(1) for m in matches} != expected:
        raise ValueError('Canonical chapter must contain 114 unique adjacent problem/solution pairs')
    return {m.group(1):m for m in matches}

def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--repo', type=Path, default=Path('.'))
    ap.add_argument('--apply',action='store_true')
    ap.add_argument('--show-diff',action='store_true')
    args = ap.parse_args(); repo = args.repo.resolve()
    raw = (repo/CH).read_bytes(); s = raw.decode('utf-8')
    sha = hashlib.sha256(raw).hexdigest()
    if sha != OLD_SHA: raise ValueError(f'Canonical source SHA drift: {sha}; expected {OLD_SHA}')
    before = pairs(s)
    ledger = repo/AUD/'GA03J19_CONSOLIDATED_114_LEDGER.tsv'
    status = repo/AUD/'GA03J19_COVERAGE_STATUS.json'
    if not ledger.exists() or not status.exists():
        raise ValueError('Complete GA03J19 ledger and status first; do not patch against GA03J18')
    with ledger.open(encoding='utf-8-sig',newline='') as f: rows=list(csv.DictReader(f,delimiter='\t'))
    if len(rows)!=114 or len({r['problem_id'] for r in rows})!=114 or any(r['review_coverage']!='INITIAL_TARGETED_REVIEW' for r in rows):
        raise ValueError('GA03J19 has not confirmed all 114 initially reviewed')
    if json.loads(status.read_text(encoding='utf-8')).get('pending_initial_review') != 0:
        raise ValueError('GA03J19 status still contains pending review')
    for row in rows:
        m=before.get(row['problem_id'])
        if not m or hashlib.sha256(m.group(2).encode()).hexdigest()!=row['problem_sha256'] or hashlib.sha256(m.group(3).encode()).hexdigest()!=row['solution_sha256']:
            raise ValueError('Per-problem fingerprint mismatch: '+row['problem_id'])
    changes=[]
    def change(pid,label,old,new):
        nonlocal s
        m=pairs(s)[pid]; segment=m.group(0)
        if segment.count(old)!=1: raise ValueError(f'{pid} anchor count {segment.count(old)} for {label}')
        updated=segment.replace(old,new,1)
        s=s[:m.start()]+updated+s[m.end():]
        changes.append((pid,label,'PATCHED_NEEDS_INDEPENDENT_MATH_VERIFICATION'))
    change('CP-V-0003','Idempotent lifting through nil ideals',
        'Idempotents lift uniquely across nilpotent ideals, so',
        'Idempotents lift uniquely across nil ideals (not only nilpotent ideals), so')
    change('CP-V-0034','Minimal integral polynomial replaces invalid subtraction',
        r'''Suppose \(b\in B\) is integral over \(A\), and assume for contradiction that
\(b\notin A\). Then \(b\in B\setminus A\). Since the complement is
multiplicatively closed,
\[
b^m\in B\setminus A
\]
for every \(m\ge1\).

On the other hand, integrality gives a monic relation
\[
b^n+a_{n-1}b^{n-1}+\cdots+a_1b+a_0=0,
\qquad a_i\in A.
\]
Hence
\[
b\bigl(b^{n-1}+a_{n-1}b^{n-2}+\cdots+a_1\bigr)=-a_0\in A.
\]
If the second factor were outside \(A\), then by multiplicative closure of
\(B\setminus A\) the product would lie outside \(A\), a contradiction.
Thus
\[
b^{n-1}+a_{n-1}b^{n-2}+\cdots+a_1\in A.
\]
Subtracting the lower terms shows
\[
b^{n-1}\in A.
\]
But this contradicts the fact that every positive power of \(b\) lies in
\(B\setminus A\). Therefore \(b\in A\).''',
        r'''Suppose \(b\in B\) is integral over \(A\), and assume \(b\notin A\).
Choose a monic equation for \(b\) of the least possible degree \(n\):
\[
b^n+a_{n-1}b^{n-1}+\cdots+a_1b+a_0=0,
\qquad a_i\in A.
\]
If \(n=1\), then \(b=-a_0\in A\), a contradiction. Thus \(n\ge2\).
Put
\[
c=b^{n-1}+a_{n-1}b^{n-2}+\cdots+a_1.
\]
Since \(bc=-a_0\in A\), multiplicative closure of \(B\setminus A\)
and \(b\notin A\) imply \(c\in A\). But then \(b\) satisfies
\[
b^{n-1}+a_{n-1}b^{n-2}+\cdots+a_2b+(a_1-c)=0,
\]
a monic equation over \(A\) of degree \(n-1\). This contradicts
minimality of \(n\). Therefore \(b\in A\).''')
    change('CP-V-0037','Krull intersection supplies Archimedean bound',
        r'''Now let \(\delta\in\Gamma\) be positive. By the Archimedean argument forced
by principal generation of powers of \(\mathfrak m\), there is a unique
integer \(n\ge0\) with
\[
n\gamma\le\delta<(n+1)\gamma.
\]
Then
\[
0\le\delta-n\gamma<\gamma.
\]
Minimality of \(\gamma\) implies
\[
\delta-n\gamma=0.
\]
Hence every positive element is an integral multiple of \(\gamma\), and
therefore
\[
\Gamma\cong\mathbb Z.
\]''',
        r'''Now let \(\delta\in\Gamma\) be positive, and choose \(0\ne x\in V\)
with \(v(x)=\delta\). Since \(V\) is a Noetherian local domain,
Krull's intersection theorem gives
\[
\bigcap_{n\ge1}\mathfrak m^n
=\bigcap_{n\ge1}(\pi^n)=0.
\]
Thus \(x\notin(\pi^N)\) for some integer \(N\ge1\), so
\(\delta<N\gamma\). Choose the least such \(N\). Then
\[
0\le\delta-(N-1)\gamma<\gamma.
\]
Since \(\gamma\) is the least positive element of \(\Gamma\), the
difference vanishes. Therefore \(\delta=(N-1)\gamma\).
Every positive value is an integral multiple of \(\gamma\), and hence
\(\Gamma\cong\mathbb Z\) as ordered groups.''')
    change('CP-V-0051','Restrict weak/ordinary associated prime comparison to Noetherian case',
        r'''\textbf{(c)} If the zero ideal has a primary decomposition, prove that
\[
D(A)=\operatorname{Ass}_A(A).
\]''',
        r'''\textbf{(c)} Assume in addition that \(A\) is Noetherian.
Prove that
\[
D(A)=\operatorname{Ass}_A(A).
\]
Explain why the Noetherian hypothesis is relevant.''')
    change('CP-V-0051','Explain Noetherian assumption in solution',
        r'''If
\[
0=Q_1\cap\cdots\cap Q_n
\]
is irredundant primary with radicals \(\mathfrak p_i\), then for each \(i\)''',
        r'''For \textbf{(c)}, over a Noetherian ring, primes minimal over
annihilators coincide with ordinary associated primes. If
\[
0=Q_1\cap\cdots\cap Q_n
\]
is an irredundant primary decomposition with radicals \(\mathfrak p_i\),
then for each \(i\)''')
    change('CP-V-0051','Non-Noetherian counterexample demonstrates need for hypothesis',
        r'''Therefore
\[
D(A)=\operatorname{Ass}_A(A).
\]''',
        r'''Therefore
\[
D(A)=\operatorname{Ass}_A(A).
\]
Without the Noetherian hypothesis, consider
\(A=k[x_1,x_2,\dots]/(x_1^2,x_2^2,\dots)\).
Its unique prime \(\mathfrak m=(x_1,x_2,\dots)\) is nil, so \((0)\)
is \(\mathfrak m\)-primary and \(D(A)=\{\mathfrak m\}\). Yet
\(\operatorname{Ass}_A(A)=\varnothing\): each nonzero element uses
only finitely many variables and is not annihilated by a new variable.
Thus weak and ordinary associated primes need not agree.''')
    expected={'CP-V-0003','CP-V-0034','CP-V-0037','CP-V-0051'}
    after=pairs(s)
    modified={pid for pid in before if before[pid].group(0)!=after[pid].group(0)}
    if modified!=expected:raise ValueError('Unexpected changed IDs: '+repr(modified))
    newsha=hashlib.sha256(s.encode('utf-8')).hexdigest()
    print(json.dumps({'milestone':'GA-03j.20a','mode':'APPLY' if args.apply else 'DRY_RUN',
        'canonical_before_sha256':sha,'canonical_after_sha256':newsha,
        'modified_ids':sorted(modified),'anchor_edits':len(changes),
        'pair_count':114,'mathematical_certification':'NOT_COMPLETE'},indent=2))
    diff=''.join(difflib.unified_diff(raw.decode('utf-8').splitlines(keepends=True),s.splitlines(keepends=True),
                                     fromfile='a/part_v_chapter.tex',tofile='b/part_v_chapter.tex'))
    if args.show_diff:print(diff)
    if not args.apply:return
    outputs=[repo/AUD/'GA03J20A_ORIGINAL_CHAPTER.tex',repo/AUD/'GA03J20A_PATCH.diff',repo/AUD/'GA03J20A_PATCH_MANIFEST.tsv']
    if any(p.exists() for p in outputs):raise ValueError('GA03J20A reports already exist: refusing overwrite')
    outputs[0].write_bytes(raw)
    outputs[1].write_text(diff,encoding='utf-8')
    with outputs[2].open('w',newline='',encoding='utf-8') as f:
        w=csv.writer(f,delimiter='\t');w.writerow(['problem_id','correction','status']);w.writerows(changes)
    (repo/CH).write_bytes(s.encode('utf-8'))
    if hashlib.sha256((repo/CH).read_bytes()).hexdigest()!=newsha:
        raise RuntimeError('Post-write SHA mismatch; restore from GA03J20A_ORIGINAL_CHAPTER.tex')
    print('WROTE canonical corrections, original backup, diff, and manifest')
if __name__=='__main__':main()
