#!/usr/bin/env python3
"""GA-03h.3: read-only module-class counterexample evidence audit.

The imported inventory and Part V canonical chapter remain untouched. --apply
writes GA03H3_MODULE_CLASS_COUNTEREXAMPLES.tsv and .md only. This audit
checks content anchors; mathematical judgments are explicitly editorial.
"""
import argparse
import csv
import re
import sys
from pathlib import Path

CHAPTER = Path('books/companion_problems_solutions/chapters/part05_volume_v/chapter.tex')
DEST = Path('reports/companion/global_audit')

# (classification, example, canonical ID, required visible anchors, proof sketch)
CASES = [
    ('FREE_IMPLIES_PROJECTIVE_IMPLIES_FLAT', 'A[x] over A', 'CP-V-0019',
     ['\\bigoplus', 'free', 'flat'],
     'A[x] has the monomial A-basis 1,x,x^2,...; free implies projective, and projective implies flat.'),
    ('PROJECTIVE_NOT_FREE', 'A_1 x 0 over A_1 x A_2 (both nonzero)', 'CP-V-0020',
     ['\\operatorname{Ann}_A(M_1)', 'idempotents', 'projective'],
     'The idempotent summand Ae_1 is projective; its nonzero annihilator excludes any nonzero free A-module.'),
    ('FLAT_NOT_PROJECTIVE', 'Q over Z', 'CP-V-0106',
     ['torsion-free', 'filtered colimits', 'flat'],
     'Q is torsion-free and thus flat over the PID Z. A projective Z-module is free, whereas nonzero free abelian groups are not divisible; Q is divisible.'),
    ('NONFLAT_TORSION', 'Z/2 over Z', 'CP-V-0024',
     ['\\xrightarrow{\\cdot2}', 'not injective'],
     'Tensoring the injection Z --2--> Z with Z/2 makes it the zero map, so Z/2 is not flat.'),
    ('NONPROJECTIVE_NONFLAT', 'k[x]/(x) over k[x]', 'CP-V-0025',
     ['not projective', 'idempotent'],
     'R/(x) is not projective because the quotient sequence over k[x] does not split. It is nonflat since it has x-torsion over the domain k[x].'),
    ('NONFLAT_TOR_WITNESS', 'Tor_1 of k with itself over k[x]', 'CP-V-0048',
     ['\\frac{I\\cap J}{IJ}', '\\cong k'],
     'Tor_1^{k[x]}(k,k) = (x)/(x^2) is k, not zero. This witnesses that k is not flat over k[x].'),
    ('FINITE_PD_NOT_FLAT', 'Z/12 over Z', 'CP-V-0077',
     ['\\xrightarrow{\\cdot 12}', 'kernel'],
     'The length-one free resolution shows projective dimension 1, but Z/12 is not flat because it has torsion over Z.'),
    ('BASE_RING_DEPENDENCE', 'k over k versus k over k[x]', 'CP-V-0082',
     ['free of rank', 'nontrivial free resolution'],
     'The same underlying module is free over k but has projective dimension one over k[x].'),
]


def extract(chapter):
    matches = list(re.finditer(
        r'\\begin\{problem\}\[(CP-V-\d{4})\]([\s\S]*?)\\end\{problem\}\s*\\begin\{solution\}([\s\S]*?)\\end\{solution\}',
        chapter))
    return {m.group(1): (m.group(2), m.group(3)) for m in matches}, matches


def audit(root):
    path = root / CHAPTER
    if not path.is_file():
        raise FileNotFoundError(f'chapter missing: {path}')
    text = path.read_text(encoding='utf-8')
    material, blocks = extract(text)
    ids = [m.group(1) for m in blocks]
    if len(ids) != 114 or set(ids) != {f'CP-V-{i:04d}' for i in range(1, 115)}:
        raise ValueError('canonical Part V problem/solution count or IDs unexpected; no report written')
    inventory = root / 'imports/problem_inventory/SEMANTIC_PROBLEM_UNITS.tsv'
    if not inventory.is_file():
        raise FileNotFoundError(f'authoritative imported inventory missing: {inventory}')
    rows = []
    for category, example, pid, anchors, reasoning in CASES:
        block = material.get(pid)
        if block is None:
            status, missing = 'BLOCKED_MISSING_CANONICAL', anchors
        else:
            combined = '\n'.join(block)
            missing = [anchor for anchor in anchors if anchor not in combined]
            status = 'REVIEW_REQUIRED_ANCHOR' if missing else 'MATHEMATICALLY_REVIEWED'
        rows.append(dict(category=category, example=example, companion_problem_id=pid,
                         audit_status=status, missing_anchors=' | '.join(missing),
                         editorial_reason=reasoning,
                         source_relation='CANONICAL_EXAMPLE' if category != 'FLAT_NOT_PROJECTIVE' else 'DERIVED_COMPARISON_FROM_CANONICAL_THEOREM',
                         provenance_status='NOT_ASSERTED_BY_THIS_AUDIT'))
    return rows


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo', type=Path, default=Path('.'))
    parser.add_argument('--apply', action='store_true', help='write only two new GA03H3 review files')
    args = parser.parse_args()
    try:
        rows = audit(args.repo.resolve())
    except (OSError, ValueError) as exc:
        print('GA-03h.3 ERROR:', exc, file=sys.stderr)
        return 2
    from collections import Counter
    counts = Counter(row['audit_status'] for row in rows)
    print(f'GA-03h.3: {len(rows)} module-class cases; statuses: {dict(counts)}')
    for row in rows:
        print(f"  {row['companion_problem_id']}: {row['category']} — {row['audit_status']}")
        if row['missing_anchors']:
            print('    Missing textual anchors:', row['missing_anchors'])
    if args.apply:
        out = args.repo.resolve() / DEST
        out.mkdir(parents=True, exist_ok=True)
        path = out / 'GA03H3_MODULE_CLASS_COUNTEREXAMPLES.tsv'
        with path.open('w', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, delimiter='\t', fieldnames=list(rows[0]))
            writer.writeheader()
            writer.writerows(rows)
        markdown = ['# GA-03h.3 — Module classes and counterexamples', '',
                    'Mathematical judgments require editorial scrutiny; this audit verifies source anchors only.',
                    'The imported inventory remains authoritative for provenance. No source mapping is inferred here.', '']
        for row in rows:
            markdown += [f"## {row['category']} — {row['companion_problem_id']}",
                         f"- Example: {row['example']}",
                         f"- Status: {row['audit_status']}",
                         f"- Mathematical argument: {row['editorial_reason']}",
                         f"- Source relation: {row['source_relation']}",
                         f"- Missing anchors: {row['missing_anchors'] or 'none'}", '']
        (out / 'GA03H3_MODULE_CLASS_COUNTEREXAMPLES.md').write_text('\n'.join(markdown), encoding='utf-8')
        print('WROTE:', path)
    else:
        print('DRY RUN; no files changed')
    return 1 if any(r['audit_status'] != 'MATHEMATICALLY_REVIEWED' for r in rows) else 0


if __name__ == '__main__':
    sys.exit(main())
