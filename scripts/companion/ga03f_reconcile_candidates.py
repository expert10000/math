#!/usr/bin/env python3
"""GA-03f v2: read-only source-text recovery and candidate provenance matching.

The imported inventory indexes source line ranges; it DOES NOT store statement text.
Recover it from imports/ALL_TEX_AND_FIGURES/tex using SOURCE_FILES.tsv.
Never mutate imported files, the Companion chapter, or previous audit ledgers.
Only --apply creates GA03F_SOURCE_CANDIDATES.tsv.
"""
import argparse
import csv
import math
import re
from collections import Counter
from pathlib import Path

CHAPTER = Path('books/companion_problems_solutions/chapters/part05_volume_v/chapter.tex')
INV = Path('imports/problem_inventory')
SEM = INV / 'SEMANTIC_PROBLEM_UNITS.tsv'
RAW = INV / 'RAW_PROBLEM_ITEMS.tsv'
SOURCES = INV / 'SOURCE_FILES.tsv'
OUT = Path('reports/companion/global_audit/GA03F_SOURCE_CANDIDATES.tsv')
TARGET = {'V/10', 'V/11', 'V/12', 'V/13', 'V/14', 'V/26', 'V/27', 'V/28'}


def table(path, mandatory):
    with path.open('r', encoding='utf-8-sig', newline='') as f:
        rdr = csv.DictReader(f, delimiter='\t')
        fields = set(rdr.fieldnames or [])
        missing = set(mandatory) - fields
        if missing:
            raise ValueError(f'{path}: missing columns: {sorted(missing)}')
        return list(rdr)


def sections(tex):
    headings = list(re.finditer(r'\\section\*\{(V/\d{2})\s+---[^}]*\}', tex))
    for j, h in enumerate(headings):
        sec = h.group(1)
        if sec not in TARGET:
            continue
        end = headings[j + 1].start() if j + 1 < len(headings) else len(tex)
        fragment = tex[h.end():end]
        found = list(re.finditer(r'\\begin\{problem\}\[(CP-V-\d{4})\]', fragment))
        for m in found:
            body = fragment[m.end():].split(r'\end{problem}', 1)[0]
            yield sec, m.group(1), body


def tokens(s):
    # Retain mathematical names and digits. This ranks candidates, not exact identity.
    s = re.sub(r'(?m)^\s*%[^\n]*', ' ', s)
    s = re.sub(r'\\(?:label|ref|eqref|cite)\{[^}]*\}', ' ', s)
    s = re.sub(r'\\(?:begin|end)\{[^}]*\}', ' ', s)
    s = re.sub(r'\\([A-Za-z]+)', r' \1 ', s)
    words = re.findall(r'[a-z][a-z0-9]*|[0-9]+', s.lower())
    skip = {'the', 'and', 'for', 'with', 'that', 'show', 'prove', 'compute',
            'deduce', 'where', 'then', 'from', 'each', 'given', 'let', 'there',
            'using', 'are', 'its', 'this', 'have', 'over', 'into', 'which',
            'ring', 'rings', 'module', 'modules', 'mathbb', 'mathcal', 'textbf',
            'right', 'left', 'such', 'all', 'any', 'not'}
    return [w for w in words if len(w) > 1 and w not in skip]


def safe_source_path(root, s):
    # SOURCE_FILES.repo_path is the preferred authoritative local relative path.
    p = Path(s.replace('\\', '/'))
    if p.is_absolute() or '..' in p.parts:
        raise ValueError(f'unsafe source path: {s}')
    candidate = (root / p).resolve()
    allowed = (root / 'imports/ALL_TEX_AND_FIGURES/tex').resolve()
    if not candidate.is_relative_to(allowed):
        raise ValueError(f'source outside imported TeX tree: {s}')
    return candidate


def main():
    arg = argparse.ArgumentParser(description=__doc__)
    arg.add_argument('--repo', type=Path, default=Path('.'))
    arg.add_argument('--top', type=int, default=5)
    arg.add_argument('--apply', action='store_true')
    a = arg.parse_args()
    if not 1 <= a.top <= 30:
        arg.error('--top must be from 1 to 30')
    root = a.repo.resolve()
    try:
        comp = list(sections((root / CHAPTER).read_text(encoding='utf-8')))
        if len(comp) != 18 or len({pid for _, pid, _ in comp}) != 18:
            raise ValueError(f'GA-03f expected 18 distinct companion IDs, found {len(comp)}')
        sem = table(root / SEM, ['semantic_problem_id', 'representative_problem_id',
                                'member_problem_ids', 'source_files'])
        raw = table(root / RAW, ['problem_id', 'source_id', 'source_file',
                                'start_line', 'end_line', 'statement_text_hash'])
        sources = table(root / SOURCES, ['source_id', 'source_file', 'repo_path'])
        source_by_id = {r['source_id']: r for r in sources}
        raw_by_id = {r['problem_id']: r for r in raw}
        cache = {}
        failures = Counter()

        def recover(r):
            source = source_by_id.get(r['source_id'])
            if not source:
                failures['source_id_missing'] += 1
                return ''
            # Refuse to silently attach the wrong source in case of corrupt provenance.
            if source['source_file'].replace('\\', '/') != r['source_file'].replace('\\', '/'):
                failures['source_file_mismatch'] += 1
                return ''
            try:
                p = safe_source_path(root, source['repo_path'])
                if p not in cache:
                    cache[p] = p.read_text(encoding='utf-8-sig', errors='replace').splitlines(keepends=True)
                lines = cache[p]
                st, en = int(r['start_line']), int(r['end_line'])
                if st < 1 or en < st or en > len(lines):
                    failures['bad_line_range'] += 1
                    return ''
                return ''.join(lines[st-1:en])
            except (ValueError, OSError) as exc:
                failures[type(exc).__name__] += 1
                return ''

        candidates = []
        matched_semantics = [r for r in sem if 'commutative-algebra' in r['source_files'].lower()]
        for r in matched_semantics:
            ids = list(dict.fromkeys([r['representative_problem_id']] +
                                      [x.strip() for x in r['member_problem_ids'].split(';') if x.strip()]))
            recovered = []
            for id_ in ids:
                raw_row = raw_by_id.get(id_)
                if raw_row:
                    body = recover(raw_row)
                    if len(tokens(body)) >= 6:
                        recovered.append((body, raw_row))
                else:
                    failures['member_not_in_raw'] += 1
            if recovered:
                body, raw_row = max(recovered, key=lambda x: len(tokens(x[0])))
                candidates.append((r, body, raw_row))
        if not candidates:
            raise ValueError('no valid source statements recovered; check source paths and line ranges')

        docs = [Counter(tokens(body)) for _, body, _ in candidates]
        df = Counter(t for doc in docs for t in doc)
        N = len(docs)
        def vec(doc):
            return {t: (1 + math.log(n)) * (1 + math.log((N + 1) / (df[t] + 1)))
                    for t, n in doc.items() if n > 0}
        indexed = []
        for cand, count in zip(candidates, docs):
            v = vec(count)
            indexed.append((cand, v, math.sqrt(sum(x*x for x in v.values()))))

        output = []
        for sec, pid, body in comp:
            v = vec(Counter(tokens(body)))
            mag = math.sqrt(sum(x*x for x in v.values()))
            scored = []
            if mag:
                for cand, w, wm in indexed:
                    if wm:
                        score = sum(q * w.get(k, 0) for k, q in v.items()) / (mag * wm)
                        if score > 0:
                            scored.append((score, cand))
            scored.sort(key=lambda item: (-item[0], item[1][0]['semantic_problem_id']))
            top = scored[:a.top]
            for rank, (score, (r, src_text, raw_row)) in enumerate(top, 1):
                output.append(dict(section=sec, companion_problem_id=pid, rank=rank,
                    cosine_score=f'{score:.4f}', import_semantic_problem_id=r['semantic_problem_id'],
                    representative_problem_id=r['representative_problem_id'],
                    recovered_from_problem_id=raw_row['problem_id'],
                    source_file=raw_row['source_file'],
                    source_start_line=raw_row['start_line'], source_end_line=raw_row['end_line'],
                    member_problem_ids=r['member_problem_ids'],
                    solution_availability=r.get('solution_availability', ''),
                    mapping_status='CANDIDATE_ONLY_REQUIRES_MANUAL_EVIDENCE'))
            print(f'{sec} {pid}: ' + (', '.join(f'{r[0]["semantic_problem_id"]} ({s:.3f})' for s,r in top) or 'NO CANDIDATE'))
        print(f'Imported semantic units: {len(sem)}; source-name-filtered: {len(matched_semantics)}')
        print(f'Recovered source-bearing semantic units: {len(candidates)}; imported .tex files read: {len(cache)}')
        print('Recovery diagnostics:', dict(failures))
        print('WARNING: similarity scores are only review leads, NOT verified source-to-companion links.')
        if not a.apply:
            print('DRY RUN: no files changed')
            return
        if not output:
            raise ValueError('no candidate output; ledger not written')
        dest = root / OUT
        dest.parent.mkdir(parents=True, exist_ok=True)
        with dest.open('w', encoding='utf-8', newline='') as f:
            wr = csv.DictWriter(f, fieldnames=list(output[0]), delimiter='\t', lineterminator='\n')
            wr.writeheader()
            wr.writerows(output)
        print(f'WROTE: {dest} ({len(output)} candidate rows)')
    except (OSError, ValueError, KeyError) as exc:
        arg.exit(1, f'ERROR: {exc}; no new ledger written\n')

if __name__ == '__main__':
    main()
