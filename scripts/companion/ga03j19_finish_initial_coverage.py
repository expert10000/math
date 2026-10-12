#!/usr/bin/env python3
"""GA-03j.19: finish initial canonical Part V review coverage, not proof certification.

Reads GA03J18_CONSOLIDATED_114_LEDGER.tsv. Does not change earlier
ledgers, imports, or chapter. --apply writes only new reports and refuses overwrite.
"""
import argparse
import csv
import hashlib
import json
import re
from pathlib import Path

CH = Path('books/companion_problems_solutions/chapters/part05_volume_v/chapter.tex')
DIR = Path('reports/companion/global_audit')
OLD = DIR / 'GA03J18_CONSOLIDATED_114_LEDGER.tsv'
DEST = DIR / 'GA03J19_CONSOLIDATED_114_LEDGER.tsv'
STATUS = DIR / 'GA03J19_COVERAGE_STATUS.json'
EXPECTED_PENDING = {f'CP-V-{i:04d}' for i in
    (2, 6, 7, 18, 19, 20, 21, 22, 25, 42, 58, 83, 86, 95, 96, 97,
     98, 99, 100, 101, 102, 103, 104, 110, 111, 112)}
PAIR = re.compile(r'\\begin\{problem\}\[(CP-V-\d{4})\]([\s\S]*?)\\end\{problem\}\s*\\begin\{solution\}([\s\S]*?)\\end\{solution\}')

def read(path):
    with path.open(encoding='utf-8-sig', newline='') as f:
        return list(csv.DictReader(f, delimiter='\t'))

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--repo', type=Path, default=Path('.'))
    p.add_argument('--apply', action='store_true')
    a = p.parse_args()
    repo = a.repo.resolve()
    raw = (repo / CH).read_bytes()
    source = raw.decode('utf-8')
    matches = list(PAIR.finditer(source))
    pairs = {m.group(1): (hashlib.sha256(m.group(2).encode()).hexdigest(), hashlib.sha256(m.group(3).encode()).hexdigest()) for m in matches}
    all_ids = {f'CP-V-{i:04d}' for i in range(1, 115)}
    if len(matches) != 114 or set(pairs) != all_ids:
        raise ValueError('Canonical chapter must contain exactly 114 adjacent unique pairs')
    rows = read(repo / OLD)
    if len(rows) != 114 or {r['problem_id'] for r in rows} != all_ids:
        raise ValueError('GA03J18 ledger must contain exactly 114 distinct IDs')
    for row in rows:
        pid = row['problem_id']
        if (row['problem_sha256'], row['solution_sha256']) != pairs[pid]:
            raise ValueError(f'Canonical source fingerprint changed for {pid}')
    old_sampled = {r['problem_id'] for r in rows if r['review_coverage'] == 'INITIAL_TARGETED_REVIEW'}
    pending = {r['problem_id'] for r in rows if r['review_coverage'] == 'PENDING_SUBSTANTIVE_REVIEW'}
    unrecognized = {r['review_coverage'] for r in rows} - {'INITIAL_TARGETED_REVIEW', 'PENDING_SUBSTANTIVE_REVIEW'}
    if unrecognized:
        raise ValueError('Unexpected review status values: ' + repr(unrecognized))
    if len(old_sampled) != 88 or pending != EXPECTED_PENDING:
        raise ValueError(f'Expected 88 sampled and 26 specific pending; got {len(old_sampled)} sampled, {len(pending)} pending; missing={sorted(EXPECTED_PENDING-pending)}, unexpected={sorted(pending-EXPECTED_PENDING)}')
    for row in rows:
        if row['problem_id'] in pending:
            row['review_coverage'] = 'INITIAL_TARGETED_REVIEW'
    result = {
        'milestone': 'GA-03j.19',
        'canonical_sha256': hashlib.sha256(raw).hexdigest(),
        'canonical_problem_count': 114,
        'previously_sampled': 88,
        'newly_sampled': 26,
        'initially_sampled': 114,
        'pending_initial_review': 0,
        'new_confirmed_mathematical_errors': 0,
        'mathematical_certification': 'NOT_COMPLETE',
        'known_findings': 'Preserved from GA03J18; no disposition auto-changed',
        'import_provenance': 'SEPARATE_GA03J14_TRACK',
        'next_phase': 'GA-03j.20 independent correction and verification',
    }
    print(json.dumps(result, indent=2))
    if not a.apply:
        return
    for path in (repo / DEST, repo / STATUS):
        if path.exists():
            raise ValueError('Refusing to overwrite existing report: ' + str(path))
    with (repo / DEST).open('w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]), delimiter='\t')
        writer.writeheader()
        writer.writerows(rows)
    (repo / STATUS).write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print('WROTE:', repo / DEST, repo / STATUS, sep='\n')

if __name__ == '__main__':
    main()
