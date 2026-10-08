#!/usr/bin/env python3
"""GA-03e v2: guarded CP-V-0027 proof clarification and conservative Part V ledger."""
import argparse,csv,re,sys
from pathlib import Path

CHAPTER='books/companion_problems_solutions/chapters/part05_volume_v/chapter.tex'
OLD=r'''The decomposition is irredundant,
and therefore
\[
\boxed{
I=(x,y)\cap(x,z)\cap(x^2,y,z)
}.
\]'''
NEW=r'''The decomposition is irredundant: the first two components are
needed to retain the two distinct minimal primes, while omitting the
third would replace $I$ by $(x,yz)$ and lose the relation $x^2=0$.
The three radicals are $(x,y)$, $(x,z)$, and $(x,y,z)$, respectively.
By the associated-primes theorem for an irredundant primary
decomposition over the Noetherian ring $R$, these are exactly the
associated primes of $R/I$, confirming the computation above.
Thus
\[
\boxed{
I=(x,y)\cap(x,z)\cap(x^2,y,z)
}.
\]'''
REVIEWED={
 'CP-V-0027':('PROOF_CLARIFICATION','Add explicit associated-primes justification'),
 'CP-V-0030':('REVIEWED_NO_DEFECT_FOUND','I-adic completion examples and kernel'),
 'CP-V-0031':('REVIEWED_NO_DEFECT_FOUND','Artin–Rees and exact completion'),
 'CP-V-0032':('REVIEWED_NO_DEFECT_FOUND','Completion of ideals and Jacobson radical'),
 'CP-V-0053':('REVIEWED_NO_DEFECT_FOUND','Associated graded and Krull intersection'),
 'CP-V-0055':('REVIEWED_NO_DEFECT_FOUND','Analytically reducible domain; char ≠ 2'),
 'CP-V-0056':('REVIEWED_NO_DEFECT_FOUND','Veronese direct sum and Cohen–Macaulayness'),
 'CP-V-0062':('PREVIOUSLY_CORRECTED_PENDING_REVIEW','Characteristic two localization correction'),
 'CP-V-0057':('PREVIOUSLY_CORRECTED_PENDING_REVIEW','Infinite-family prime avoidance'),
 'CP-V-0044':('PREVIOUSLY_CORRECTED_PENDING_REVIEW','Auslander–Buchsbaum proof'),
 'CP-V-0061':('PREVIOUSLY_CORRECTED_PENDING_REVIEW','Characteristic 2/5 correction'),
 'CP-V-0075':('PREVIOUSLY_CORRECTED_PENDING_REVIEW','Cancellation-aware fraction membership'),
 'CP-V-0076':('PREVIOUSLY_CORRECTED_PENDING_REVIEW','Cancellation-aware fraction membership'),
}
def main():
 p=argparse.ArgumentParser();p.add_argument('--repo',default='.');p.add_argument('--apply',action='store_true');a=p.parse_args()
 repo=Path(a.repo).resolve();chapter=repo/CHAPTER
 text=chapter.read_text(encoding='utf-8-sig')
 marker=r'\begin{problem}[CP-V-0027]';start=text.find(marker)
 if start<0:sys.exit('ERROR CP-V-0027 not found')
 stop=text.find(r'\end{solution}',start)
 if stop<0:sys.exit('ERROR CP-V-0027 solution not found')
 sub=text[start:stop]; n=sub.count(OLD)
 if n==1:
  patched=text[:start]+sub.replace(OLD,NEW)+text[stop:];state='PATCH_AVAILABLE'
 elif NEW in sub and OLD not in sub:
  patched=text;state='ALREADY_APPLIED'
 else:sys.exit('ERROR CP-V-0027 original text does not match expected; no changes made')
 print('GA-03e:',state)
 if not a.apply:
  print('DRY RUN: no files changed; --apply to patch and write ledger');return
 matches=list(re.finditer(r'\\begin\{problem\}\[(CP-V-\d{4})\]',patched))
 ids=[m.group(1) for m in matches]
 expected={f'CP-V-{i:04d}' for i in range(1,115)}
 if len(ids)!=114 or set(ids)!=expected:
  sys.exit(f'ERROR chapter IDs unexpected: count={len(ids)}, unique={len(set(ids))}, missing={sorted(expected-set(ids))[:8]}; no changes made')
 if patched!=text:chapter.write_text(patched,encoding='utf-8',newline='')
 out=repo/'reports/companion/global_audit/PART_V_MATHEMATICAL_QUALITY.tsv';out.parent.mkdir(parents=True,exist_ok=True)
 with out.open('w',encoding='utf-8',newline='') as f:
  w=csv.writer(f,delimiter='\t');w.writerow(['problem_id','status','review_note','source_line'])
  for m in matches:
   pid=m.group(1);status,note=REVIEWED.get(pid,('NOT_REVIEWED',''))
   w.writerow([pid,status,note,patched.count('\n',0,m.start())+1])
 print('PATCH AND LEDGER WRITTEN:',out)
 print('Rows: 114; unreviewed:',sum(pid not in REVIEWED for pid in ids))
if __name__=='__main__':main()
