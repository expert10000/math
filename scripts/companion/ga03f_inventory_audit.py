#!/usr/bin/env python3
"""GA-03f conservative Part V inventory/companion audit. No chapter modifications.

Uses committed imported SEMANTIC_PROBLEM_UNITS.tsv for provenance and
Part V companion section structure for current canonical problem IDs.
Does NOT assert semantic-to-companion equivalence without an explicit mapping.
"""
import argparse
import csv
import re
from pathlib import Path

CHAPTER = Path('books/companion_problems_solutions/chapters/part05_volume_v/chapter.tex')
SEMANTIC = Path('imports/problem_inventory/SEMANTIC_PROBLEM_UNITS.tsv')
OUT = Path('reports/companion/global_audit/GA03F_INVENTORY_COVERAGE.tsv')
EXPECTED = {'V/10': 'tensor_products', 'V/11': 'quotients_base_change',
            'V/12': 'hom_finite_presentation', 'V/13': 'projective_modules',
            'V/14': 'flat_modules', 'V/26': 'tor', 'V/27': 'ext',
            'V/28': 'derived_functors'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo', type=Path, default=Path('.'))
    parser.add_argument('--apply', action='store_true', help='Write only coverage ledger (not the chapter)')
    args = parser.parse_args()
    repo = args.repo.resolve()
    cp = repo / CHAPTER
    ip = repo / SEMANTIC
    if not cp.is_file() or not ip.is_file():
        raise SystemExit(f'ERROR: required source absent: chapter={cp.is_file()}, semantic inventory={ip.is_file()}')
    chapter = cp.read_text(encoding='utf-8')
    with ip.open(encoding='utf-8-sig', newline='') as f:
        reader = csv.DictReader(f, delimiter='\t')
        required = {'semantic_problem_id', 'representative_problem_id', 'source_files',
                    'member_problem_ids', 'solution_availability'}
        if not required.issubset(set(reader.fieldnames or [])):
            raise SystemExit('ERROR: inventory schema changed')
        imported = list(reader)
    # Preserve the importer as the authority; no speculative exact source mappings.
    relevant_imports = [r for r in imported if 'commutative-algebra' in r['source_files'].lower()]
    sections = list(re.finditer(r'\\section\*\{(V/\d{2})\s+---\s+([^}]*)\}', chapter))
    blocks = {}
    for n, m in enumerate(sections):
        end = sections[n+1].start() if n+1 < len(sections) else len(chapter)
        blocks[m.group(1)] = (m.group(2), chapter[m.end():end], m.end())
    rows = []
    all_ids = []
    for section, topic in EXPECTED.items():
        if section not in blocks:
            raise SystemExit(f'ERROR: expected chapter section missing: {section}')
        title, block, offset = blocks[section]
        p = list(re.finditer(r'\\begin\{problem\}\[(CP-V-\d{4})\]', block))
        s = list(re.finditer(r'\\begin\{solution\}', block))
        if len(p) != len(s) or not p:
            raise SystemExit(f'ERROR: problem/solution count mismatch in {section}: {len(p)}/{len(s)}')
        for m in p:
            pid = m.group(1)
            all_ids.append(pid)
            rows.append({'section': section, 'topic': topic, 'companion_problem_id': pid,
                'chapter_line': str(chapter.count('\n', 0, offset+m.start())+1),
                'problem_solution_pair': 'PRESENT', 'import_semantic_problem_id': '',
                'import_representative_problem_id': '',
                'mapping_status': 'NOT_ESTABLISHED',
                'quality_status': 'PENDING_MATHEMATICAL_REVIEW',
                'review_note': 'Exact imported semantic correspondence requires evidence; no mapping inferred.'})
    if len(all_ids) != len(set(all_ids)):
        raise SystemExit('ERROR: duplicate companion IDs in GA-03f sections')
    print(f'GA-03f: {len(rows)} companion problems in {len(EXPECTED)} sections')
    print(f'Imported semantic units (entire corpus): {len(imported)}')
    print(f'Imported semantic units with commutative-algebra source filenames: {len(relevant_imports)}')
    for section in EXPECTED:
        print(f'  {section}: {", ".join(r["companion_problem_id"] for r in rows if r["section"]==section)}')
    print('NOTE: source filename is NOT a topic classifier; full import-to-companion links remain unverified.')
    if not args.apply:
        print('DRY RUN; no files changed. Use --apply to write ledger.')
        return
    dest = repo / OUT
    dest.parent.mkdir(parents=True, exist_ok=True)
    with dest.open('w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]), delimiter='\t', lineterminator='\n')
        writer.writeheader(); writer.writerows(rows)
    print(f'WROTE: {dest}')

if __name__ == '__main__':
    main()
