#!/usr/bin/env python3
"""GA-03j.24 final Part V audit ledger integration. Never edits canonical TeX.

This is audit integration, not proof certification of all 114 solutions.
"""
import argparse
import csv
import hashlib
import json
import re
from collections import Counter
from pathlib import Path

CHAPTER = 'books/companion_problems_solutions/chapters/part05_volume_v/chapter.tex'
BASELINE = 'reports/companion/global_audit/GA03J20A_ORIGINAL_CHAPTER.tex'
HISTORICAL = 'reports/companion/global_audit/GA03J19_CONSOLIDATED_114_LEDGER.tsv'
REVIEW = 'reports/companion/global_audit/GA03J23_SEVEN_PROOF_CERTIFICATION.tsv'
REPORT = 'reports/companion/global_audit/GA03J24_INTEGRATED_114_LEDGER.tsv'
SUMMARY = 'reports/companion/global_audit/GA03J24_INTEGRATION_STATUS.json'
EXPECTED_SHA = '55b130c64150a90e1a6604a75538659ea4a627ffd86e2f2c6eb5342633c64177'
EXPECTED_CHANGED = {'CP-V-0003', 'CP-V-0034', 'CP-V-0035', 'CP-V-0037', 'CP-V-0051', 'CP-V-0084', 'CP-V-0085'}
PAIR_RE = re.compile(r'\\begin\{problem\}\[(CP-V-\d{4})\]([\s\S]*?)\\end\{problem\}\s*\\begin\{solution\}([\s\S]*?)\\end\{solution\}')


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def load_tsv(path):
    with path.open(encoding='utf-8-sig', newline='') as f:
        reader = csv.DictReader(f, delimiter='\t')
        if not reader.fieldnames:
            raise ValueError(f'Missing TSV headers: {path}')
        return list(reader), reader.fieldnames


def extract(raw, name):
    text = raw.decode('utf-8-sig')
    matches = list(PAIR_RE.finditer(text))
    expected = {f'CP-V-{i:04d}' for i in range(1, 115)}
    ids = [m.group(1) for m in matches]
    if len(ids) != 114 or set(ids) != expected or len(ids) != len(set(ids)):
        raise ValueError(f'{name}: expected 114 unique adjacent canonical problem/solution pairs, got {len(ids)}')
    if text.count('\\begin{solution}') != 114 or text.count('\\end{solution}') != 114:
        raise ValueError(f'{name}: solution environment imbalance')
    return {m.group(1): (m.group(2), m.group(3)) for m in matches}


def run(repo, apply):
    current_raw = (repo / CHAPTER).read_bytes()
    current_sha = sha(current_raw)
    if current_sha != EXPECTED_SHA:
        raise ValueError(f'Canonical chapter SHA mismatch: {current_sha}; expected {EXPECTED_SHA}. No report written.')
    old = extract((repo / BASELINE).read_bytes(), 'GA03J20A original')
    current = extract(current_raw, 'current canonical')
    changed = {pid for pid in current if current[pid] != old[pid]}
    if changed != EXPECTED_CHANGED:
        raise ValueError(f'Correction scope mismatch: actual={sorted(changed)}, expected={sorted(EXPECTED_CHANGED)}')

    hist, hist_cols = load_tsv(repo / HISTORICAL)
    if 'problem_id' not in hist_cols:
        raise ValueError(f'{HISTORICAL} lacks problem_id; inspect the ledger before integration')
    hist_ids = [r['problem_id'] for r in hist]
    if len(hist) != 114 or set(hist_ids) != set(current) or len(set(hist_ids)) != 114:
        raise ValueError('GA03J19 historical review must contain exactly 114 distinct canonical problem IDs')
    for row in hist:
        if 'problem_sha256' in hist_cols:
            if row['problem_sha256'] != sha(old[row['problem_id']][0].encode('utf-8')):
                raise ValueError('Historical problem SHA does not match baseline for ' + row['problem_id'])
        if 'solution_sha256' in hist_cols:
            if row['solution_sha256'] != sha(old[row['problem_id']][1].encode('utf-8')):
                raise ValueError('Historical solution SHA does not match baseline for ' + row['problem_id'])

    reviews, review_cols = load_tsv(repo / REVIEW)
    if not {'problem_id', 'verification_status'}.issubset(review_cols):
        raise ValueError('GA03J23 requires problem_id and verification_status columns')
    review_ids = [r['problem_id'] for r in reviews]
    if len(reviews) != 7 or set(review_ids) != EXPECTED_CHANGED or len(set(review_ids)) != 7:
        raise ValueError('GA03J23 review must contain precisely the seven corrected problem IDs')
    accepted = {'PASS', 'PASS_WITH_REFERENCE_DEPENDENCY', 'PASS_WITH_THEOREM_DEPENDENCY'}
    if any(r['verification_status'] not in accepted for r in reviews):
        raise ValueError('GA03J23 contains nonpassing review disposition; stop for adjudication')
    reviews_by_id = {r['problem_id']: r for r in reviews}
    hist_by_id = {r['problem_id']: r for r in hist}

    result = []
    for pid in sorted(current):
        r = reviews_by_id.get(pid)
        old_problem, old_solution = old[pid]
        new_problem, new_solution = current[pid]
        line = {
            'problem_id': pid,
            'ga03j24_initial_review': 'COVERED_GA03J19',
            'ga03j24_final_canonical_sha256': current_sha,
            'ga03j24_corrected_in_20a_20c': 'YES' if pid in changed else 'NO',
            'ga03j24_final_statement_sha256': sha(new_problem.encode('utf-8')),
            'ga03j24_final_solution_sha256': sha(new_solution.encode('utf-8')),
            'ga03j24_original_statement_sha256': sha(old_problem.encode('utf-8')),
            'ga03j24_original_solution_sha256': sha(old_solution.encode('utf-8')),
            'ga03j24_targeted_proof_review': r['verification_status'] if r else 'NOT_IN_SEVEN_PROOF_REVIEW',
            'ga03j24_review_source': r.get('source', '') if r else '',
            'ga03j24_review_dependency': r.get('dependency', '') if r else '',
            'ga03j24_all_proofs_formally_certified': 'NO',
            'ga03j24_individual_provenance_reconciled': 'NOT_ASSERTED_BY_GA03J24',
        }
        # Explicitly namespace historical fields; they describe the pre-correction ledger.
        for key in hist_cols:
            if key != 'problem_id':
                line['ga03j19_' + key] = hist_by_id[pid][key]
        result.append(line)

    summary = {
        'milestone': 'GA-03j.24',
        'canonical_sha256': current_sha,
        'source_scope_integrity': 'PASS',
        'rows': len(result),
        'historical_initial_reviews': len(hist),
        'targeted_corrected_proofs_reviewed': len(reviews),
        'proof_review_statuses': dict(Counter(r['verification_status'] for r in reviews)),
        'corrected_problem_ids': sorted(changed),
        'individual_import_provenance': 'NOT_REASSESSED_IN_THIS_MILESTONE',
        'full_independent_mathematical_certification_of_all_114': False,
        'formal_proof_verification': False,
        'pdf_review': 'USER_UPLOADED_COMPILED_PDF_REVIEWED_IN_GA03J23',
        'ready_for_commit': False,
        'remaining': ['Review integrated ledger for consistency with GA03J19 findings and GA03J14 provenance adjudications', 'Scope review Git staging before commit'],
    }
    print(json.dumps(summary, indent=2))
    if not apply:
        print('DRY RUN ONLY: no files written. Use --apply after review.')
        return
    paths = [repo / REPORT, repo / SUMMARY]
    if any(p.exists() for p in paths):
        raise FileExistsError('Refusing to overwrite GA03J24 output: ' + ', '.join(str(p) for p in paths if p.exists()))
    paths[0].parent.mkdir(parents=True, exist_ok=True)
    with paths[0].open('w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=list(result[0]), delimiter='\t', lineterminator='\n')
        writer.writeheader()
        writer.writerows(result)
    paths[1].write_text(json.dumps(summary, indent=2) + '\n', encoding='utf-8')
    print('WROTE\n' + '\n'.join(str(p) for p in paths))


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--repo', type=Path, default=Path('.'))
    p.add_argument('--apply', action='store_true')
    args = p.parse_args()
    run(args.repo.resolve(), args.apply)


if __name__ == '__main__':
    main()
