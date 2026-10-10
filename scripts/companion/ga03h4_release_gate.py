#!/usr/bin/env python3
"""GA-03h.4 conservative release gate (no chapter/import modifications).

Default: read-only. --apply writes only GA03H4_RELEASE_GATE.tsv.
Check scope: canonical pairs, 3 GA-03h review ledgers, authoritative import,
regression of two GA-03f and two GA-03g corrections.
This does NOT prove mathematical statements or source-provenance equivalence.
"""
import argparse
import csv
import re
import sys
from collections import Counter
from pathlib import Path

CHAPTER = Path('books/companion_problems_solutions/chapters/part05_volume_v/chapter.tex')
INVENTORY = Path('imports/problem_inventory/SEMANTIC_PROBLEM_UNITS.tsv')
REPORTS = Path('reports/companion/global_audit')


def rows_of(path):
    with path.open('r', encoding='utf-8-sig', newline='') as stream:
        return list(csv.DictReader(stream, delimiter='\t'))


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--repo', type=Path, default=Path('.'))
    ap.add_argument('--apply', action='store_true', help='write a new diagnostic release-gate TSV only')
    args = ap.parse_args()
    root = args.repo.resolve()
    checks = []

    def record(name, passed, detail):
        checks.append(dict(check=name, status='PASS' if passed else 'FAIL', detail=str(detail)))

    cp = root / CHAPTER
    if not cp.is_file():
        print('ERROR: missing chapter', cp)
        return 2
    text = cp.read_text(encoding='utf-8')
    pattern = re.compile(r'\\begin\{problem\}\[(CP-V-\d{4})\]([\s\S]*?)\\end\{problem\}\s*\\begin\{solution\}([\s\S]*?)\\end\{solution\}')
    blocks = list(pattern.finditer(text))
    mapped = {match.group(1): match.group(2) + '\n' + match.group(3) for match in blocks}
    all_ids = re.findall(r'\\begin\{problem\}\[(CP-V-\d{4})\]', text)
    expected = {f'CP-V-{i:04d}' for i in range(1, 115)}
    record('CANONICAL_114', len(all_ids) == len(blocks) == 114 and len(mapped) == 114 and set(mapped) == expected,
           f'problem headings={len(all_ids)}; paired solutions={len(blocks)}; unique IDs={len(mapped)}')
    labels = re.findall(r'\\label\{prob:(cp-v-\d{4})\}', text)
    record('UNIQUE_LABELS', len(labels) == 114 and len(set(labels)) == 114 and set(labels) == {i.lower() for i in expected},
           f'canonical labels={len(labels)}')

    inv = root / INVENTORY
    if inv.is_file():
        unitrows = rows_of(inv)
        record('AUTHORITATIVE_IMPORT', bool(unitrows) and 'semantic_problem_id' in unitrows[0],
               f'semantic units={len(unitrows)}; no source mappings inferred')
    else:
        record('AUTHORITATIVE_IMPORT', False, f'missing {inv}')

    ledger_specs = [
        ('GA03H_EXAMPLE_COUNTEREXAMPLE_AUDIT.tsv', 14, 'status', {'CANONICAL_EXAMPLE_PRESENT': 12, 'REVIEW_REQUIRED': 2}),
        ('GA03H2_MATHEMATICAL_CONTRASTS.tsv', 14, 'review_status', {'CANONICAL_EXAMPLE_REVIEWED': 12, 'VERIFIED_DERIVED_COMPARISON': 2}),
        ('GA03H3_MODULE_CLASS_COUNTEREXAMPLES.tsv', 8, 'audit_status', {'MATHEMATICALLY_REVIEWED': 8}),
    ]
    for filename, count, status_col, wanted in ledger_specs:
        path = root / REPORTS / filename
        if not path.is_file():
            record('LEDGER_' + filename, False, 'missing file')
            continue
        data = rows_of(path)
        counts = Counter(row.get(status_col, '') for row in data)
        ids_ok = all(row.get('companion_problem_id') in expected for row in data)
        provenance_ok = all(row.get('provenance_status', 'NOT_ASSERTED_BY_THIS_AUDIT')
                            not in ('VERIFIED', 'EXACT_SOURCE_MATCH') for row in data)
        record('LEDGER_' + filename, len(data) == count and counts == wanted and ids_ok and provenance_ok,
               f'rows={len(data)}; statuses={dict(counts)}; canonical IDs={ids_ok}; no asserted provenance={provenance_ok}')

    p18 = mapped.get('CP-V-0018', '')
    record('GA03F_CP0018_CRT', ('f(0)=g(0)' in p18 or 'f(0) = g(0)' in p18)
           and 'and the two factors generate comaximal ideals' not in p18,
           'correct fiber product and no invalid CRT claim')
    p96 = mapped.get('CP-V-0096', '')
    record('GA03F_CP0096_BASE_CHANGE', r'\xrightarrow{\cdot f}' in p96
           and r'\operatorname{coker}' in p96,
           'full exact-presentation/cokernel correction')
    p43 = mapped.get('CP-V-0043', '')
    record('GA03G_CP0043_NONZERO', r'M\ne0' in p43.split(r'\end{problem}')[0],
           'nonzero module hypothesis')
    p113 = mapped.get('CP-V-0113', '')
    record('GA03G_CP0113_POSITIVE', bool(re.search(r'n\s*,\s*m\s*\\ge\s*1', p113)) or
           'n,m\\ge1' in p113 or 'n,m\\ge 1' in p113,
           'positive integer parameters')

    print('GA-03h.4 RELEASE GATE')
    for row in checks:
        print('  {status:<4} {check}: {detail}'.format(**row))
    failures = sum(x['status'] == 'FAIL' for x in checks)
    print(f'GA-03h.4: {len(checks)-failures}/{len(checks)} checks passed')
    print('NOTE: PDF build, complete Part V validator, and provenance verification are independent steps.')
    if args.apply:
        out = root / REPORTS / 'GA03H4_RELEASE_GATE.tsv'
        out.parent.mkdir(parents=True, exist_ok=True)
        with out.open('w', encoding='utf-8', newline='') as stream:
            writer = csv.DictWriter(stream, fieldnames=['check', 'status', 'detail'], delimiter='\t')
            writer.writeheader()
            writer.writerows(checks)
        print('WROTE:', out)
    return 1 if failures else 0


if __name__ == '__main__':
    sys.exit(main())
