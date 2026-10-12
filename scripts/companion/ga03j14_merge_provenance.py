#!/usr/bin/env python3
"""GA-03j.14: safe consolidation of adjudicated imported-source candidates.

Uses authoritative canonical Part V, prior GA03J7 coverage ledger, GA03F ranked
candidates, and GA03J11-13 adjudications. Never invents new provenance mappings.
No input edits. --apply refuses to overwrite existing output files.
"""
from __future__ import annotations
import argparse, csv, hashlib, json, re
from collections import Counter, defaultdict
from pathlib import Path

AUD = Path('reports/companion/global_audit')
CANON = Path('books/companion_problems_solutions/chapters/part05_volume_v/chapter.tex')
EXPECTED_SHA = '769a30e7d711ac34dfa24ddbfcc8410605f308d36a6d7ec3f59f1f4c703feb0b'
EXPECT = {f'CP-V-{i:04d}' for i in range(1, 115)}
OUTPUTS = ('GA03J14_ADJUDICATED_PAIRS.tsv', 'GA03J14_114_PROVENANCE_LEDGER.tsv',
           'GA03J14_ACTIVE_CANDIDATES.tsv', 'GA03J14_SUMMARY.json')

def read_table(path: Path):
    if not path.is_file(): raise ValueError(f'Missing required file: {path}')
    with path.open(encoding='utf-8-sig', newline='') as f:
        return list(csv.DictReader(f, delimiter='\t'))

def write_table(path: Path, rows: list[dict], fields: list[str]):
    with path.open('w', encoding='utf-8', newline='') as f:
        w = csv.DictWriter(f, fieldnames=fields, delimiter='\t', extrasaction='ignore')
        w.writeheader(); w.writerows(rows)

def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--repo', type=Path, default=Path('.'))
    ap.add_argument('--apply', action='store_true')
    args = ap.parse_args(); repo = args.repo.resolve(); a = repo / AUD
    raw = (repo / CANON).read_bytes()
    sha = hashlib.sha256(raw).hexdigest()
    if sha != EXPECTED_SHA:
        raise ValueError(f'Canonical source changed: {sha}. Rebase the audit before proceeding.')
    canonical_ids = re.findall(r'\\begin\{problem\}\[(CP-V-\d{4})\]', raw.decode('utf-8'))
    if len(canonical_ids) != 114 or set(canonical_ids) != EXPECT:
        raise ValueError('Canonical Part V ID integrity failed')
    coverage = read_table(a / 'GA03J7_CONSOLIDATED_114_LEDGER.tsv')
    if len(coverage) != 114 or {r['problem_id'] for r in coverage} != EXPECT:
        raise ValueError('GA03J7 coverage ledger does not contain precisely 114 problems')
    if sum(r['review_coverage'] == 'INITIAL_TARGETED_REVIEW' for r in coverage) != 37:
        raise ValueError('Expected GA03J7 initial review count 37')
    candidates = read_table(a / 'GA03F_SOURCE_CANDIDATES.tsv')
    source_candidates = defaultdict(list)
    for c in candidates:
        if c['companion_problem_id'] not in EXPECT:
            raise ValueError('Unexpected GA03F problem ID')
        source_candidates[c['companion_problem_id']].append(c)
    if len(candidates) != 90 or len(source_candidates) != 18:
        raise ValueError('GA03F ranking baseline changed; do not silently reuse count assumptions')
    data11 = read_table(a / 'GA03J11_ADJUDICATED_PROVENANCE.tsv')
    data12 = read_table(a / 'GA03J12_ADJUDICATED_CANDIDATES.tsv')
    data13 = read_table(a / 'GA03J13_ADJUDICATED_CANDIDATES.tsv')
    if (len(data11),len(data12),len(data13)) != (1,8,5):
        raise ValueError('Expected GA03J11/12/13 review counts 1/8/5')
    reviewed = []
    def append(pid, sid, status, source, evidence, phase):
        if pid not in EXPECT or not sid: raise ValueError('Invalid adjudication identifier')
        matching = [c for c in source_candidates[pid] if c['import_semantic_problem_id'] == sid]
        if len(matching) != 1:
            raise ValueError(f'Adjudicated source is not a unique GA03F candidate: {pid} {sid}')
        candidate = matching[0]
        if Path(candidate['source_file']).name != Path(source).name:
            raise ValueError('Filename differs from GA03F candidate for '+pid)
        reviewed.append({'canonical_problem_id':pid,'import_semantic_problem_id':sid,
          'candidate_rank':candidate['rank'],'source_file':candidate['source_file'],
          'source_line_range':f"{candidate['source_start_line']}-{candidate['source_end_line']}",
          'decision':status,'evidence':evidence,'phase':phase})
    for x in data11:
        append(x['canonical_problem_id'], x['source_semantic_id'], x['mapping_decision'],
               x['source_path'], x.get('mathematical_comparison',''), 'GA03J11')
    for source, data in [('GA03J12',data12), ('GA03J13',data13)]:
        for x in data:
            append(x['canonical_problem_id'],x['import_semantic_problem_id'],x['decision'],
                   x['source_basename'],x['comparison_evidence'],source)
    keys = [(x['canonical_problem_id'],x['import_semantic_problem_id']) for x in reviewed]
    if len(set(keys)) != 14: raise ValueError('Duplicated adjudicated pair')
    decision_by_pair = {(x['canonical_problem_id'],x['import_semantic_problem_id']):x['decision'] for x in reviewed}
    rejected = {'REJECT_TOP_RANKED_CANDIDATE'}
    insufficient = {'INSUFFICIENT_TOP_RANKED_CANDIDATE'}
    positive = {'VERIFIED_STATEMENT_CORRESPONDENCE', 'THEOREM_STATEMENT_CORRESPONDENCE',
                'PARTIAL_EXAMPLE_CORRESPONDENCE','PARTIAL_THEOREM_CORRESPONDENCE',
                'PARTIAL_TO_STRONG_STATEMENT_CORRESPONDENCE'}
    if set(decision_by_pair.values()) - rejected - insufficient - positive:
        raise ValueError('Unknown decision category; update mapping rules explicitly')
    active = []
    for c in candidates:
        pair = (c['companion_problem_id'],c['import_semantic_problem_id'])
        decision = decision_by_pair.get(pair,'NOT_ADJUDICATED')
        if decision in rejected: continue
        c = dict(c)
        c['ga03j14_decision'] = decision
        c['candidate_action'] = ('REVIEW_OTHER_EVIDENCE' if decision in insufficient
                else 'KEEP_REVIEWED_CORRESPONDENCE' if decision in positive
                else 'AWAIT_MATHEMATICAL_COMPARISON')
        active.append(c)
    by_problem=defaultdict(list)
    for x in reviewed: by_problem[x['canonical_problem_id']].append(x)
    led=[]
    for c in sorted(coverage,key=lambda r:r['problem_id']):
        pid=c['problem_id']; decisions=by_problem[pid]
        pos=[x for x in decisions if x['decision'] in positive]
        neg=[x for x in decisions if x['decision'] in rejected]
        inc=[x for x in decisions if x['decision'] in insufficient]
        if pos:
            state='ADJUDICATED_CORRESPONDENCE_WITH_SCOPE_LIMITS'
        elif not source_candidates[pid]:state='NO_GA03F_CANDIDATE'
        elif decisions:state='ADJUDICATED_CANDIDATE_NOT_ESTABLISHED'
        else:state='UNREVIEWED_GA03F_CANDIDATES'
        led.append({'canonical_problem_id':pid,'candidate_count':len(source_candidates[pid]),
          'adjudicated_candidate_count':len(decisions),'positive_correspondence_count':len(pos),
          'rejected_candidate_count':len(neg),'insufficient_candidate_count':len(inc),
          'provenance_status':state,
          'positive_semantic_ids':';'.join(x['import_semantic_problem_id'] for x in pos),
          'review_coverage':c['review_coverage'],
          'mathematical_quality_status':c['quality_status'],
          'mathematical_certification':c['mathematical_certification'],
          'import_inventory_verified':c['import_inventory_verified']})
    counts=Counter(x['decision'] for x in reviewed)
    summary={'milestone':'GA-03j.14','canonical_sha256':sha,'canonical_count':114,
     'ranked_candidate_rows_before':len(candidates), 'ranked_canonical_count':len(source_candidates),
     'adjudicated_candidate_pairs':len(reviewed), 'canonical_ids_with_any_adjudication':len(by_problem),
     'positive_correspondence_pairs':sum(v for k,v in counts.items() if k in positive),
     'rejected_candidate_pairs':sum(v for k,v in counts.items() if k in rejected),
     'insufficient_candidate_pairs':sum(v for k,v in counts.items() if k in insufficient),
     'remaining_active_candidate_rows':len(active),
     'canonical_ids_without_ga03f_candidates':114-len(source_candidates),
     'mathematical_initially_sampled':37,'mathematical_pending_substantive_review':77,
     'quality_findings_not_modified':True,
     'note':'Candidate-level decisions; partial correspondence is not identical problem provenance. No new source matches inferred.'}
    print(json.dumps(summary,indent=2))
    if not args.apply: return
    paths=[a/x for x in OUTPUTS]
    if any(p.exists() for p in paths):
        raise ValueError('GA03J14 output exists; will not overwrite or partially write')
    write_table(paths[0],reviewed,list(reviewed[0]))
    write_table(paths[1],led,list(led[0]))
    write_table(paths[2],active,list(active[0]))
    paths[3].write_text(json.dumps(summary,indent=2)+'\n',encoding='utf-8')
    print('WROTE:',*[str(x) for x in paths],sep='\n')

if __name__=='__main__':
    main()
