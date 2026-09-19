#!/usr/bin/env python3
from __future__ import annotations
import argparse,csv
from pathlib import Path

def read(path):
    with path.open('r',encoding='utf-8-sig',newline='') as f: return list(csv.DictReader(f,delimiter='\t'))

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--repo',type=Path,default=Path.cwd()); a=ap.parse_args(); inv=a.repo/'imports'/'problem_inventory'
    links=read(inv/'PROBLEM_SOLUTION_LINKS.tsv'); ledger=read(inv/'PROBLEM_LEDGER.tsv'); rem=read(inv/'REMAINING_ORPHANS.tsv'); units=read(inv/'ORPHAN_SEMANTIC_UNITS.tsv'); solunits=read(inv/'SOLUTION_SEMANTIC_UNITS.tsv'); shifts=read(inv/'NUMBERING_SHIFT_APPLICATION.tsv')
    errs=[]
    pids={r['problem_id'] for r in ledger}
    for s in links:
        pid=s.get('linked_problem_id','')
        if pid and pid not in pids: errs.append(f"dangling linked_problem_id {pid} from {s.get('solution_id')}")
        if not s.get('solution_text_hash'): errs.append(f"blank solution_text_hash {s.get('solution_id')}")
    remids={r['solution_id'] for r in rem}
    unresolved={s['solution_id'] for s in links if not s.get('linked_problem_id')}
    if remids!=unresolved: errs.append(f"REMAINING_ORPHANS mismatch: file={len(remids)} actual={len(unresolved)}")
    for r in rem:
        hashes=[x for x in r.get('candidate_statement_hashes','').split(';') if x]
        # A row with one candidate statement hash should have been resolved by the equivalence rule,
        # except a numbering-mismatch row whose candidates are intentionally generated against unshifted numbers.
        if len(set(hashes))==1 and r.get('status')!='UNRESOLVED_NUMBERING_MISMATCH': errs.append(f"single-hash ambiguity left unresolved {r['solution_id']}")
    for s in shifts:
        if s.get('status')=='APPLIED' and s.get('eligible_for_auto_apply')!='YES': errs.append(f"ineligible numbering shift applied {s.get('mismatch_group')}")
    if errs:
        print('REFINEMENT VALIDATION FAILED');
        for e in errs[:100]: print(' -',e)
        return 1
    print('REFINEMENT VALIDATION PASSED')
    print(f'  links: {len(links)}')
    print(f'  solution semantic units: {len(solunits)}')
    print(f'  remaining source blocks: {len(rem)}')
    print(f'  remaining semantic review units: {len(units)}')
    return 0
if __name__=='__main__': raise SystemExit(main())
