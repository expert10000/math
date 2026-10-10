#!/usr/bin/env python3
"""GA-03f.3: evidence packet for provisional imported-source matches.

Reads canonical import metadata and v2 candidates; never edits imported sources,
Companion chapters, or existing ledgers. --apply writes a separate review TSV
and readable Markdown evidence packet. No fuzzy match is declared verified.
"""
import argparse
import csv
import hashlib
import re
import sys
from collections import Counter
from pathlib import Path

CHAPTER = 'books/companion_problems_solutions/chapters/part05_volume_v/chapter.tex'
INV = 'imports/problem_inventory'
INPUT = 'reports/companion/global_audit/GA03F_SOURCE_CANDIDATES.tsv'
TSV = 'reports/companion/global_audit/GA03F_EVIDENCE_REVIEW.tsv'
MD = 'reports/companion/global_audit/GA03F_EVIDENCE_REVIEW.md'
EXPECTED = {'CP-V-0018','CP-V-0095','CP-V-0022','CP-V-0096',
'CP-V-0023','CP-V-0105','CP-V-0020','CP-V-0021','CP-V-0025','CP-V-0058',
'CP-V-0019','CP-V-0106','CP-V-0047','CP-V-0048','CP-V-0045',
'CP-V-0113','CP-V-0044','CP-V-0114'}


def load_tsv(path, required):
    with path.open(encoding='utf-8-sig', newline='') as f:
        reader = csv.DictReader(f, delimiter='\t')
        missing = set(required) - set(reader.fieldnames or [])
        if missing:
            raise ValueError(f'{path}: missing required columns {sorted(missing)}')
        return list(reader)


def norm(s):
    # Conservative textual identity: remove TeX comments, labels, visual whitespace
    # and style wrappers, but do NOT replace mathematical tokens or numbers.
    s = re.sub(r'(?m)(?<!\\)%[^\n]*', '', s)
    s = re.sub(r'\\label\{[^{}]*\}', '', s)
    s = re.sub(r'\\(?:textbf|emph|mathrm|operatorname)\{([^{}]*)\}', r'\1', s)
    s = re.sub(r'\\(?:begin|end)\{(?:align\*?|equation\*?|gather\*?|displaymath)\}', '', s)
    s = re.sub(r'\\\[|\\\]|\\\(|\\\)|\$+', '', s)
    return re.sub(r'\s+', '', s).lower().strip()


def math_fragments(s):
    # Only literal math spans, not general word overlap. These are EVIDENCE leads.
    pieces = []
    patterns = [r'\\\[([\s\S]*?)\\\]', r'\\\(([\s\S]*?)\\\)',
                r'(?<!\$)\$([^$\n]{4,})\$(?!\$)']
    for pattern in patterns:
        for m in re.finditer(pattern, s):
            value = norm(m.group(1))
            if len(value) >= 12:
                pieces.append(value)
    return set(pieces)


def snippet(text, limit=800):
    text = re.sub(r'\s+', ' ', text).strip()
    return text[:limit] + (' ...' if len(text) > limit else '')


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--repo', type=Path, default=Path('.'))
    ap.add_argument('--apply', action='store_true')
    args = ap.parse_args()
    root = args.repo.resolve()
    try:
        chapter = (root / CHAPTER).read_text(encoding='utf-8')
        companion = {}
        for m in re.finditer(r'\\begin\{problem\}\[(CP-V-\d{4})\]([\s\S]*?)\\end\{problem\}', chapter):
            if m.group(1) in companion:
                raise ValueError('duplicate companion ID: '+m.group(1))
            companion[m.group(1)] = m.group(2)
        if not EXPECTED <= companion.keys():
            raise ValueError('missing expected companion IDs: '+str(sorted(EXPECTED-companion.keys())))
        candidates = load_tsv(root / INPUT,
            ['section','companion_problem_id','rank','cosine_score',
             'import_semantic_problem_id','recovered_from_problem_id'])
        raw = {r['problem_id']:r for r in load_tsv(root / INV / 'RAW_PROBLEM_ITEMS.tsv',
            ['problem_id','source_id','source_file','start_line','end_line'])}
        sources = {r['source_id']:r for r in load_tsv(root / INV / 'SOURCE_FILES.tsv',
            ['source_id','source_file','repo_path'])}
        source_dir = (root / 'imports/ALL_TEX_AND_FIGURES/tex').resolve()
        cache = {}
        report = []
        missing = Counter()
        for c in candidates:
            pid = c['companion_problem_id']
            if pid not in EXPECTED:
                raise ValueError('unexpected companion ID in candidates: '+pid)
            rr = raw.get(c['recovered_from_problem_id'])
            if rr is None:
                missing['missing_raw_id'] += 1
                continue
            sf = sources.get(rr['source_id'])
            if sf is None or sf['source_file'].replace('\\','/') != rr['source_file'].replace('\\','/'):
                missing['missing_or_mismatched_source'] += 1
                continue
            p = (root / sf['repo_path']).resolve()
            if not p.is_relative_to(source_dir) or not p.is_file():
                missing['unsafe_or_absent_source'] += 1
                continue
            if p not in cache:
                cache[p] = p.read_text(encoding='utf-8-sig', errors='replace').splitlines()
            lines = cache[p]
            begin, end = int(rr['start_line']), int(rr['end_line'])
            if begin < 1 or begin > end or end > len(lines):
                missing['bad_line_range'] += 1
                continue
            src = '\n'.join(lines[begin-1:end]); dst = companion[pid]
            src_norm, dst_norm = norm(src), norm(dst)
            exact = len(src_norm) >= 80 and src_norm == dst_norm
            common = math_fragments(src) & math_fragments(dst)
            # Mere common math (e.g., a definition) cannot prove provenance.
            category = 'EXACT_TEXT_MATCH' if exact else 'UNVERIFIED'
            report.append({**c,
                'evidence_status':category,
                'common_literal_math_count':str(len(common)),
                'common_literal_math_preview':' | '.join(sorted(common)[:3])[:350],
                'source_excerpt':snippet(src), 'companion_excerpt':snippet(dst),
                'source_excerpt_sha256':hashlib.sha256(src.encode()).hexdigest(),
                'evidence_note':('Mechanical same-statement fingerprint; still review source boundaries' if exact
                    else 'Cosine and formula overlap are retrieval leads only; inspect full statements')})
        if not report:
            raise ValueError('no reviewable candidate rows')
        by_id = Counter(r['companion_problem_id'] for r in report)
        print('GA-03f.3 evidence rows:',len(report),'companion IDs:',len(by_id))
        print('Exact normalized textual matches:',sum(r['evidence_status']=='EXACT_TEXT_MATCH' for r in report))
        print('Unverified candidate rows:',sum(r['evidence_status']=='UNVERIFIED' for r in report))
        print('Recovery diagnostics:',dict(missing))
        if len(by_id)!=18:
            print('WARNING: fewer than 18 companion problems have evidence rows')
        for pid in sorted(by_id):
            top = sorted((r for r in report if r['companion_problem_id']==pid),key=lambda x:int(x['rank']))[0]
            print(f"  {pid}: top {top['import_semantic_problem_id']} cosine={top['cosine_score']} evidence={top['evidence_status']} math_overlap={top['common_literal_math_count']}")
        if not args.apply:
            print('DRY RUN: no files modified; --apply writes separate evidence files')
            return
        out = root / TSV; out.parent.mkdir(parents=True,exist_ok=True)
        with out.open('w',encoding='utf-8',newline='') as f:
            writer=csv.DictWriter(f,fieldnames=list(report[0].keys()),delimiter='\t',lineterminator='\n')
            writer.writeheader();writer.writerows(report)
        body=['# GA-03f.3 — Imported-source comparison review','',
              'Evidence only. Similarity is not provenance. Inspect actual statements before editing mapping statuses.','',
              f'- Candidate rows: {len(report)}',
              f'- Companion IDs: {len(by_id)}','']
        for pid in sorted(by_id):
            body += [f'## {pid}','']
            for r in sorted((x for x in report if x['companion_problem_id']==pid),key=lambda x:int(x['rank'])):
                body += [f"### Rank {r['rank']} — {r['import_semantic_problem_id']} ({r['cosine_score']})",
                   f"- Evidence: **{r['evidence_status']}**; identical math spans: {r['common_literal_math_count']}",
                   f"- Source: `{r['source_file']}:{r['source_start_line']}-{r['source_end_line']}`",
                   f"- Source excerpt: `{r['source_excerpt'].replace('`', chr(39))}`",
                   f"- Companion excerpt: `{r['companion_excerpt'].replace('`', chr(39))}`",'']
        (root / MD).write_text('\n'.join(body)+'\n',encoding='utf-8')
        print('WROTE:',out)
        print('WROTE:',root / MD)
    except (OSError,ValueError,KeyError) as exc:
        ap.exit(1,'ERROR: '+str(exc)+'; no report written\n')

if __name__=='__main__':
    main()
