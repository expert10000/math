#!/usr/bin/env python3
"""GA-03i.1: conservative audit of exactness, naturality and derived functors.

Read-only unless --apply, which writes two NEW reports. No chapter edits,
no provenance claims, and no modifications to earlier GA ledgers.
"""
import argparse
import csv
import re
import sys
from collections import Counter
from pathlib import Path

CHAPTER = Path('books/companion_problems_solutions/chapters/part05_volume_v/chapter.tex')
OUT_DIR = Path('reports/companion/global_audit')
# These are verified existing canonical IDs (not newly proposed problems).
TOPICS = [
    ('CP-V-0022', 'NATURAL_TENSOR_QUOTIENT', '(A/I) tensor M = M/IM', 'V/11'),
    ('CP-V-0023', 'HOM_LOCALIZATION', 'Localization commutes with Hom for finitely presented M', 'V/12'),
    ('CP-V-0024', 'LEFT_RIGHT_EXACTNESS', 'Right-exact tensor and left-exact Hom; counterexamples', 'V/09'),
    ('CP-V-0031', 'COMPLETION_EXACTNESS', 'Exact I-adic completion under Noetherian finite-module hypotheses', 'V/18'),
    ('CP-V-0087', 'INVERSE_LIMIT_EXACTNESS', 'Inverse-limit left exactness and surjective transitions', 'V/18'),
    ('CP-V-0046', 'CONNECTING_HOMOLOGY', 'Connecting boundary and long exact homology / Tor', 'V/22'),
    ('CP-V-0110', 'CHAIN_HOMOTOPY', 'Homotopic chain maps induce the same homology maps', 'V/22'),
    ('CP-V-0047', 'TOR_FROM_RESOLUTION', 'Tor from a free resolution over Z', 'V/26'),
    ('CP-V-0048', 'TOR_IDEAL_FORMULA', 'Natural Tor_1 quotient formula', 'V/26'),
    ('CP-V-0113', 'EXT_FROM_RESOLUTION', 'Ext from Hom applied to a free resolution', 'V/27'),
    ('CP-V-0114', 'DERIVED_EXACT_SEQUENCE', 'Tor and Ext as exactness obstructions', 'V/28'),
    ('CP-V-0105', 'FILTERED_COLIMIT_HOM', 'Hom of finitely presented modules commutes with filtered colimits', 'V/12'),
    ('CP-V-0096', 'BASE_CHANGE_NATURALITY', 'Extension of scalars for polynomial quotients', 'V/11'),
]
# Checks inspect source text, not mathematical truth. A missing token triggers review.
ANCHORS = {
    'CP-V-0022': ('\\overline\\Theta', '\\Psi'),
    'CP-V-0023': ('\\operatorname{Hom}_{S^{-1}A}', '\\frac{f}{s}'),
    'CP-V-0024': ('\\xrightarrow{0}', '\\operatorname{Hom}_{\\mathbb Z}'),
    'CP-V-0031': ('\\widehat M',),
    'CP-V-0087': ('\\varprojlim',),
    'CP-V-0046': ('\\partial_n', 'well defined'),
    'CP-V-0110': ('f-g', 'boundary'),
    'CP-V-0047': ('N[n]', '\\ker'),
    'CP-V-0048': ('\\frac{I\\cap J}{IJ}',),
    'CP-V-0113': ('\\gcd(n,m)',),
    'CP-V-0114': ('\\operatorname{Tor}_1', '\\operatorname{Ext}_R^1'),
    'CP-V-0105': ('\\varinjlim', '\\operatorname{Hom}_A'),
    'CP-V-0096': ('\\xrightarrow{\\cdot f}', '\\operatorname{coker}'),
}
# Cross-topic obligations are editorial review items, not purported source matches.
RELATIONS = [
    ('CP-V-0024', 'CP-V-0114', 'Tensor/Hom failure of exactness vs derived functor obstruction'),
    ('CP-V-0046', 'CP-V-0114', 'Connecting boundary in homology vs long exact Tor/Ext'),
    ('CP-V-0046', 'CP-V-0047', 'Long exact homology as basis for computational Tor'),
    ('CP-V-0046', 'CP-V-0048', 'Naturality of connecting morphisms and Tor ideal quotient'),
    ('CP-V-0022', 'CP-V-0096', 'Naturality under base change and quotient isomorphism'),
    ('CP-V-0023', 'CP-V-0105', 'Finite presentation in Hom/localization vs filtered colimits'),
    ('CP-V-0031', 'CP-V-0087', 'Exact completion vs limitations of inverse limits'),
    ('CP-V-0110', 'CP-V-0046', 'Chain-homotopy invariance vs natural maps on homology'),
    ('CP-V-0047', 'CP-V-0113', 'Left-derived tensor vs right-derived Hom over Z'),
]

def read_rows(path):
    with path.open(encoding='utf-8-sig', newline='') as f:
        return list(csv.DictReader(f, delimiter='\t'))

def run(repo):
    chapter = repo / CHAPTER
    if not chapter.exists():
        raise FileNotFoundError(str(chapter))
    src = chapter.read_text(encoding='utf-8')
    sections = list(re.finditer(r'\\section\*\{(V/\d{2})\s+---\s+[^}]+\}', src))
    section_contents = {}
    for i, match in enumerate(sections):
        stop = sections[i + 1].start() if i + 1 < len(sections) else len(src)
        section_contents[match.group(1)] = src[match.end():stop]
    pairs = {}
    pair_re = re.compile(r'\\begin\{problem\}\[(CP-V-\d{4})\]([\s\S]*?)\\end\{problem\}\s*\\begin\{solution\}([\s\S]*?)\\end\{solution\}')
    for m in pair_re.finditer(src):
        if m.group(1) in pairs:
            raise ValueError('Duplicate paired problem ID: ' + m.group(1))
        pairs[m.group(1)] = (m.group(2), m.group(3), src.count('\n', 0, m.start()) + 1)
    all_ids = re.findall(r'\\begin\{problem\}\[(CP-V-\d{4})\]', src)
    all_solutions = len(re.findall(r'\\begin\{solution\}', src))
    if len(all_ids) != 114 or len(set(all_ids)) != 114 or all_solutions != 114 or len(pairs) != 114:
        raise ValueError(f'Canonical Part V invariant failed: problem IDs={len(all_ids)}, unique={len(set(all_ids))}, solutions={all_solutions}, pairs={len(pairs)}')
    imported = repo / 'imports/problem_inventory/SEMANTIC_PROBLEM_UNITS.tsv'
    if not imported.is_file():
        raise FileNotFoundError('Authoritative imported semantic inventory missing: ' + str(imported))
    with imported.open(encoding='utf-8-sig', newline='') as f:
        count_imported = sum(1 for _ in csv.DictReader(f, delimiter='\t'))
    if count_imported == 0:
        raise ValueError('Imported semantic inventory empty')

    rows = []
    def add(kind, topic, pid, related, status, finding, action):
        rows.append(dict(check_type=kind, topic=topic, companion_problem_id=pid, related_problem_id=related,
                         status=status, finding=finding, review_action=action))
    for pid, topic, description, sec in TOPICS:
        info = pairs.get(pid)
        block = section_contents.get(sec, '')
        assigned = pid in re.findall(r'\\begin\{problem\}\[(CP-V-\d{4})\]', block)
        if info is None or not assigned:
            add('CANONICAL_EXAMPLE', topic, pid, '', 'FAIL', f'pair absent or wrong chapter: {sec}', 'restore canonical structure')
            continue
        joined = info[0] + info[1]
        absent = [a for a in ANCHORS[pid] if a not in joined]
        add('CANONICAL_EXAMPLE', topic, pid, '', 'PASS' if not absent else 'REVIEW',
            description + f'; line={info[2]}' + (f'; missing textual anchors={absent}' if absent else ''),
            '' if not absent else 'Inspect exact LaTeX or mathematical exposition; token absence is not proof of defect')
    for a, b, description in RELATIONS:
        status = 'REVIEW' if a in pairs and b in pairs else 'FAIL'
        add('FUNCTORIAL_CONNECTION', 'CROSS_TOPIC', a, b, status, description,
            'Confirm naturality and exact hypotheses; do not infer source provenance')
    # These are legitimate checks for gaps rather than false declarations of errors.
    for topic, description in [
        ('CONNECTING_NATURALITY', 'Naturality square for boundary homomorphism under a morphism of short exact sequences of complexes'),
        ('LONG_EXACT_EXT_VARIANCE', 'Covariant second and contravariant first variable; articulate correct direction of connecting maps'),
        ('DERIVED_FUNCTOR_COMPARISON', 'Distinguish chain homotopy invariance from naturality of connecting boundary'),
        ('INVERSE_LIMIT_CAUTION', 'Explain why inverse limits need stronger conditions for right exactness'),
    ]:
        add('EDITORIAL_GAP_REVIEW', topic, '', '', 'REVIEW', description,
            'Inspect canonical source material first; do not create a new canonical problem by default')
    return rows, count_imported

def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--repo', type=Path, default=Path('.'))
    ap.add_argument('--apply', action='store_true', help='Write new GA03I audit files only')
    args = ap.parse_args()
    try:
        rows, source_count = run(args.repo.resolve())
    except (OSError, ValueError, KeyError) as ex:
        print('GA-03i ERROR:', ex, file=sys.stderr)
        return 2
    counts = Counter(r['status'] for r in rows)
    print('GA-03i.1 EXACT SEQUENCES / DERIVED FUNCTORS AUDIT')
    print(f'  canonical scope: {len(TOPICS)} problems; imported semantic units: {source_count}')
    print('  check results:', dict(counts))
    print('  IMPORTANT: REVIEW marks explicit mathematical/editorial work, not a failed theorem.')
    for row in rows:
        if row['status'] == 'FAIL':
            print('  FAIL', row['check_type'], row['companion_problem_id'], row['finding'])
    if args.apply:
        dest = args.repo.resolve() / OUT_DIR
        dest.mkdir(parents=True, exist_ok=True)
        tsv = dest / 'GA03I_EXACT_SEQUENCE_AUDIT.tsv'
        with tsv.open('w', encoding='utf-8', newline='') as f:
            w = csv.DictWriter(f, fieldnames=list(rows[0]), delimiter='\t')
            w.writeheader()
            w.writerows(rows)
        md = dest / 'GA03I_EXACT_SEQUENCE_AUDIT.md'
        content = ['# GA-03i.1 — Exact Sequences, Derived Functors, Natural Transformations', '',
                   'Evidence-led audit; imported inventory is authoritative. No automatic provenance mapping.', '',
                   f'- Canonical problems in scope: {len(TOPICS)}', f'- Imported semantic units: {source_count}',
                   f'- Status counts: {dict(counts)}', '',
                   '## Canonical example checks', '']
        for r in rows:
            if r['check_type'] == 'CANONICAL_EXAMPLE':
                content.append(f"- **{r['companion_problem_id']}** ({r['topic']}): {r['status']} — {r['finding']}")
        content.extend(['', '## Functorial relationships and open editorial checks', ''])
        for r in rows:
            if r['check_type'] != 'CANONICAL_EXAMPLE':
                who = f"{r['companion_problem_id']} → {r['related_problem_id']}" if r['related_problem_id'] else r['topic']
                content.append(f"- **{who}** [{r['status']}]: {r['finding']}. {r['review_action']}")
        md.write_text('\n'.join(content) + '\n', encoding='utf-8')
        print('  WROTE:', tsv)
        print('  WROTE:', md)
    else:
        print('  DRY RUN: no files changed')
    return 1 if counts['FAIL'] else 0

if __name__ == '__main__':
    sys.exit(main())
