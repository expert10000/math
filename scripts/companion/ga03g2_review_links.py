#!/usr/bin/env python3
"""GA-03g.2: non-destructive editorial review of interproblem links.
Reads chapter + GA03G_HOMOLOGICAL_CONSISTENCY.tsv; writes only
GA03G_CROSS_TOPIC_REVIEW.tsv with --apply. Does not certify provenance.
"""
import argparse,csv,re,sys
from pathlib import Path

CH=Path('books/companion_problems_solutions/chapters/part05_volume_v/chapter.tex')
BASE=Path('reports/companion/global_audit/GA03G_HOMOLOGICAL_CONSISTENCY.tsv')
OUT=Path('reports/companion/global_audit/GA03G_CROSS_TOPIC_REVIEW.tsv')
LINKS={
('0042','0021'):('COMPATIBLE','Minimal free covers are the inductive construction step of minimal free resolutions.'),
('0043','0042'):('COMPATIBLE','Vanishing differentials after tensoring with the residue field identifies Tor with graded free ranks.'),
('0044','0045'):('COMPATIBLE','Maps with entries in the maximal ideal induce zero maps on Ext from the residue field.'),
('0046','0114'):('COMPATIBLE','Connecting morphisms for complexes explain long exact Tor sequences; Ext uses the cohomological counterpart.'),
('0111','0043'):('COMPATIBLE_WITH_DISTINCTION','Schanuel gives stable syzygy equivalence, not uniqueness of arbitrary free resolutions.'),
('0112','0079'):('RELATED_DISTINCT_EXAMPLES','Both involve polynomial syzygies/resolutions, but for different modules; no direct derivation.'),
('0041','0043'):('COMPATIBLE_WITH_DISTINCTION','Periodic nonvanishing Tor forces infinite projective dimension; CP-V-0043 assumes finite projective dimension.'),
('0044','0043'):('COMPATIBLE','The projective dimension detected by minimal resolutions is the term used in Auslander--Buchsbaum.'),
('0048','0047'):('COMPATIBLE','Quotient-ideal Tor calculation specializes to cyclic quotients of Z.'),
('0113','0114'):('COMPATIBLE','A concrete Ext^1 calculation illustrates derived functors; it does not by itself establish the general long exact sequence.'),
}
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--repo',type=Path,default=Path('.'));ap.add_argument('--apply',action='store_true');a=ap.parse_args()
 root=a.repo.resolve();source=(root/CH).read_text(encoding='utf-8');report=root/BASE
 if not report.is_file():sys.exit('ERROR: missing GA-03g.1 ledger')
 with report.open(encoding='utf-8-sig',newline='') as f: prior=list(csv.DictReader(f,delimiter='\t'))
 blocks={}
 for m in re.finditer(r'\\begin\{problem\}\[(CP-V-\d{4})\]([\s\S]*?)\\end\{problem\}\s*\\begin\{solution\}([\s\S]*?)\\end\{solution\}',source):blocks[m.group(1)]=m.group(2)+'\n'+m.group(3)
 listed=set()
 for r in prior:
  if r.get('check_type')!='CROSS_LINK':continue
  mm=re.fullmatch(r'CP-V-(\d{4}) -> CP-V-(\d{4})',r.get('problem_id',''))
  if not mm:sys.exit('ERROR: unexpected cross-link syntax: '+repr(r.get('problem_id')))
  listed.add(mm.groups())
 if listed!=set(LINKS):sys.exit('ERROR: cross-link set differs from audited GA-03g.1 ledger')
 rows=[]
 for (x,y),(finding,reason) in LINKS.items():
  a_id,b_id='CP-V-'+x,'CP-V-'+y
  if a_id not in blocks or b_id not in blocks:sys.exit('ERROR: canonical statement/solution absent: '+a_id+' / '+b_id)
  rows.append(dict(source_problem_id=a_id,target_problem_id=b_id,review_status=finding,editorial_explanation=reason,provenance_status='NOT_ASSERTED',chapter_edit='NONE'))
 anchor='K\\oplus F\''
 anchor_ok=anchor in blocks.get('CP-V-0111','') and "K'\\oplus F" in blocks.get('CP-V-0111','')
 print('GA-03g.2 cross-topic review: 10/10 canonical links checked')
 print('CP-V-0111 Schanuel identity: '+('PRESENT (previous anchor warning is false positive)' if anchor_ok else 'NOT CONFIRMED'))
 if not anchor_ok:sys.exit('ERROR: Schanuel identity needs inspection; no output written')
 from collections import Counter
 print('Statuses:',dict(Counter(r['review_status'] for r in rows)))
 if not a.apply:print('DRY RUN: no files changed');return
 output=root/OUT;output.parent.mkdir(parents=True,exist_ok=True)
 with output.open('w',encoding='utf-8',newline='') as f:
  w=csv.DictWriter(f,fieldnames=rows[0].keys(),delimiter='\t');w.writeheader();w.writerows(rows)
 print('WROTE:',output)
if __name__=='__main__':main()
