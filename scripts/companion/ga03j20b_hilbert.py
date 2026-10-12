#!/usr/bin/env python3
"""GA-03j.20b: scoped CP-V-0084/0085 corrections; dry-run default.
Requires applied GA-03j.20a and 114-row GA-03j.19 initial coverage.
"""
import argparse, csv, difflib, hashlib, json, re
from pathlib import Path

CH=Path('books/companion_problems_solutions/chapters/part05_volume_v/chapter.tex')
AUD=Path('reports/companion/global_audit')
PAIR=re.compile(r'\\begin\{problem\}\[(CP-V-\d{4})\]([\s\S]*?)\\end\{problem\}\s*\\begin\{solution\}([\s\S]*?)\\end\{solution\}')

def pairs(s):
    found=list(PAIR.finditer(s))
    expected={f'CP-V-{i:04d}' for i in range(1,115)}
    if len(found)!=114 or {m.group(1) for m in found}!=expected:
        raise ValueError('Expected exactly 114 canonical problem-solution pairs')
    return {m.group(1):m for m in found}

def scoped_replace(s,pid,old,new):
    m=pairs(s)[pid]
    piece=m.group(0)
    if piece.count(old)!=1:
        raise ValueError(f'Cannot safely patch {pid}: anchor occurs {piece.count(old)} times')
    return s[:m.start()]+piece.replace(old,new,1)+s[m.end():]

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--repo',type=Path,default=Path('.'))
    ap.add_argument('--apply',action='store_true')
    ap.add_argument('--show-diff',action='store_true')
    a=ap.parse_args();repo=a.repo.resolve()
    raw=(repo/CH).read_bytes();src=raw.decode('utf-8')
    before=pairs(src)
    required=[AUD/'GA03J19_CONSOLIDATED_114_LEDGER.tsv',AUD/'GA03J19_COVERAGE_STATUS.json',AUD/'GA03J20A_ORIGINAL_CHAPTER.tex',AUD/'GA03J20A_PATCH_MANIFEST.tsv']
    for p in required:
        if not (repo/p).is_file():raise ValueError('Missing prerequisite: '+str(p))
    with (repo/required[0]).open(encoding='utf-8-sig',newline='') as f:ledger=list(csv.DictReader(f,delimiter='\t'))
    if len(ledger)!=114 or len({r['problem_id'] for r in ledger})!=114 or any(r['review_coverage']!='INITIAL_TARGETED_REVIEW' for r in ledger):
        raise ValueError('GA03J19 initial coverage is incomplete')
    history=json.loads((repo/required[1]).read_text(encoding='utf-8'))
    if history.get('initially_sampled')!=114 or history.get('pending_initial_review')!=0:
        raise ValueError('GA03J19 status does not confirm 114/114')
    previous=(repo/required[2]).read_bytes()
    if hashlib.sha256(previous).hexdigest()!='769a30e7d711ac34dfa24ddbfcc8410605f308d36a6d7ec3f59f1f4c703feb0b':
        raise ValueError('GA03J20A original-backup checksum mismatch')
    original=pairs(previous.decode('utf-8'))
    edits_from_20a={'CP-V-0003','CP-V-0034','CP-V-0037','CP-V-0051'}
    modified={pid for pid in original if original[pid].group(0)!=before[pid].group(0)}
    if modified!=edits_from_20a:
        raise ValueError(f'Expected GA03J20A four-problem patch, actual modified IDs: {sorted(modified)}')
    manifest=(repo/required[3]).read_text(encoding='utf-8-sig')
    if not all(pid in manifest for pid in edits_from_20a):raise ValueError('GA03J20A manifest incomplete')
    s=src
    s=scoped_replace(s,'CP-V-0084',
        r'The leading terms show that the degrees are \(n-1\) and \(n-2\),'+ '\n'+r'respectively.',
        r'''For homogeneous nonunits of positive degrees, the first Hilbert
polynomial has degree \(n-1\) when \(n\ge1\), while the second has
 degree \(n-2\) when \(n\ge2\). At the Artinian boundary the eventual
Hilbert polynomial is zero; the length or graded multiplicity remains
a separate nonzero invariant.'''.replace('\n degree','\ndegree'))
    s=scoped_replace(s,'CP-V-0085',
        r'''Let \(I\subseteq S=k[x_0,\dots,x_n]\) be homogeneous, and define the degree
of \(S/I\) from the leading coefficient of its Hilbert polynomial.''',
        r'''Let \(I\subseteq S=k[x_0,\dots,x_n]\) be homogeneous. For a
nonzero homogeneous quotient of Krull dimension at least one, define
its degree from the leading coefficient of its eventual Hilbert
polynomial, using the usual factorial normalization. For an Artinian
graded quotient, the eventual Hilbert polynomial is zero; its length
or graded multiplicity requires a separate convention.''')
    s=scoped_replace(s,'CP-V-0085',
        r'\textbf{(a)} Show that for a hypersurface of degree \(d\),',
        r'\textbf{(a)} Assume \(n\ge1\) and \(d>0\). Show that for a hypersurface of degree \(d\),')
    s=scoped_replace(s,'CP-V-0085',
        r'\textbf{(b)} If \(f,g\) form a homogeneous regular sequence of degrees',
        r'\textbf{(b)} Assume \(n\ge2\). If \(f,g\) form a homogeneous regular sequence of positive degrees')
    s=scoped_replace(s,'CP-V-0085',
        r'''\textbf{(c)} More generally, if \(h\) is a homogeneous non-zero-divisor on
\(S/I\) of degree \(e\), prove''',
        r'''\textbf{(c)} More generally, assume \(\dim(S/I)\ge2\). If \(h\) is a
homogeneous non-zero-divisor on \(S/I\) of positive degree \(e\), prove''')
    s=scoped_replace(s,'CP-V-0085',
        r'''The first two assertions follow from the leading terms of the Hilbert
polynomials computed in CP-V-0084.''',
        r'''Under the stated dimension and positivity hypotheses, the first
two assertions follow from the Hilbert polynomials in CP-V-0084.
When the quotient is Artinian, its eventual Hilbert polynomial is zero,
so the degree defined above is not applicable.''')
    after=pairs(s)
    changed={pid for pid in before if before[pid].group(0)!=after[pid].group(0)}
    if changed!={'CP-V-0084','CP-V-0085'}:raise ValueError('Unexpected changed problem IDs')
    oldsha=hashlib.sha256(raw).hexdigest();newsha=hashlib.sha256(s.encode('utf-8')).hexdigest()
    summary=dict(milestone='GA-03j.20b',mode='APPLY' if a.apply else 'DRY_RUN',before_sha256=oldsha,after_sha256=newsha,
       modified_problem_ids=sorted(changed),canonical_pairs=114,independent_math_verification='PENDING')
    print(json.dumps(summary,indent=2))
    diff=''.join(difflib.unified_diff(src.splitlines(keepends=True),s.splitlines(keepends=True),
                       fromfile='a/part_v_chapter.tex',tofile='b/part_v_chapter.tex'))
    if a.show_diff:print(diff)
    if not a.apply:return
    files=[repo/AUD/'GA03J20B_ORIGINAL_CHAPTER.tex',repo/AUD/'GA03J20B_PATCH.diff',repo/AUD/'GA03J20B_PATCH_MANIFEST.json']
    if any(p.exists() for p in files):raise ValueError('GA03J20B report already exists; refusing overwrite')
    files[0].write_bytes(raw);files[1].write_text(diff,encoding='utf-8')
    files[2].write_text(json.dumps(summary,indent=2)+'\n',encoding='utf-8')
    (repo/CH).write_bytes(s.encode('utf-8'))
    if hashlib.sha256((repo/CH).read_bytes()).hexdigest()!=newsha:
        raise RuntimeError('Post-write SHA mismatch; restore GA03J20B_ORIGINAL_CHAPTER.tex')
    print('WROTE scoped corrections and backup/diff/manifest')
if __name__=='__main__':main()
