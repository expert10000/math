#!/usr/bin/env python3
"""GA-03h: read-only canonical example/counterexample inventory.

The authoritative source is the repository Part V chapter and imported semantic inventory.
This script audits existing examples. Proposed derived contrasts are explicitly labelled
and do not create new canonical problems or assert source-provenance matches.
--apply writes new GA03H reports only.
"""
import argparse, csv, re, sys
from pathlib import Path

CHAPTER=Path('books/companion_problems_solutions/chapters/part05_volume_v/chapter.tex')
IMPORT=Path('imports/problem_inventory/SEMANTIC_PROBLEM_UNITS.tsv')
OUT=Path('reports/companion/global_audit')
# Checked against the existing main-branch chapter; exact IDs, not similarity estimates.
CASES=[
 ('FINITE_PD','CP-V-0077','Z/12 over Z','finite free resolution, pd=1','SOURCED'),
 ('FINITE_PD','CP-V-0078','k[x]/(x^3) over k[x]','finite free resolution, pd=1','SOURCED'),
 ('FINITE_PD','CP-V-0079','k over k[x,y]','Koszul resolution, pd=2','SOURCED'),
 ('BASE_RING','CP-V-0082','k over k vs k over k[x]','pd changes from 0 to 1 with base ring','SOURCED'),
 ('INFINITE_PD','CP-V-0041','k over k[x,y]/(xy)','periodic free resolution, pd=infinity, Tor_i=k^2 for i>=1','SOURCED'),
 ('FINITE_PD_THEORY','CP-V-0043','minimal resolutions and Tor','Tor vanishing characterizes finite pd under stated hypotheses','SOURCED'),
 ('NONFLAT','CP-V-0024','Z/2 over Z','tensor fails to preserve an injection','SOURCED'),
 ('NONFLAT','CP-V-0048','k[x]/(x) over k[x]','nonzero Tor_1 with itself','SOURCED'),
 ('FREE_FLAT','CP-V-0019','A[x] over A','free => projective => flat; faithfully flat','SOURCED'),
 ('PROJECTIVE_NONFREE','CP-V-0020','A1 x 0 over A1 x A2','idempotent summand projective but nonfree','SOURCED'),
 ('NONPROJECTIVE','CP-V-0025','k[x]/(x) over k[x]','quotient sequence does not split','SOURCED'),
 ('FLAT_TORSIONFREE','CP-V-0106','torsion-free module over PID','flat iff torsion-free (not necessarily projective)','SOURCED'),
 ('FLAT_NONPROJECTIVE','CP-V-0106','Q as Z-module','derived example: flat but not projective','DERIVED_REQUIRES_EDITORIAL_CONFIRMATION'),
 ('PERIODIC_CONTRAST','CP-V-0041','periodic k over hypersurface vs k over polynomial ring','contrast infinite periodic resolution with finite Koszul resolution CP-V-0079','DERIVED_REQUIRES_EDITORIAL_CONFIRMATION'),
]

def get_blocks(text):
 p=r'\\begin\{problem\}\[(CP-V-\d{4})\]([\s\S]*?)\\end\{problem\}\s*\\begin\{solution\}([\s\S]*?)\\end\{solution\}'
 return {m.group(1):(m.group(2),m.group(3),text.count('\n',0,m.start())+1) for m in re.finditer(p,text)}

def main():
 ap=argparse.ArgumentParser(description=__doc__)
 ap.add_argument('--repo',type=Path,default=Path('.'))
 ap.add_argument('--apply',action='store_true',help='write two new diagnostic reports (does not modify books or imported inventory)')
 a=ap.parse_args(); root=a.repo.resolve()
 if not (root/CHAPTER).exists() or not (root/IMPORT).exists():
  sys.exit('ERROR: Part V chapter or authoritative imported semantic inventory missing')
 chapter=(root/CHAPTER).read_text(encoding='utf-8')
 blocks=get_blocks(chapter)
 ids=re.findall(r'\\begin\{problem\}\[(CP-V-\d{4})\]',chapter)
 if len(ids)!=114 or len(set(ids))!=114:
  sys.exit('ERROR: Part V chapter does not contain 114 unique canonical problems; no files written')
 with (root/IMPORT).open(encoding='utf-8-sig',newline='') as f:
  semantic_count=sum(1 for _ in csv.DictReader(f,delimiter='\t'))
 rows=[]
 for category,pid,example,claim,origin in CASES:
  obj=blocks.get(pid)
  if obj is None: sys.exit(f'ERROR: canonical statement or solution missing for {pid}; no files written')
  statement,solution,line=obj
  rows.append({'category':category,'companion_problem_id':pid,'example':example,'expected_mathematical_contrast':claim,
    'evidence_type':origin,'source_line':line,'status':'REVIEW_REQUIRED' if origin.startswith('DERIVED') else 'CANONICAL_EXAMPLE_PRESENT',
    'editorial_note':'Confirm proof and hypotheses; source equivalence is not implied by this report.'})
 # Automatic checks are syntactic checks only; no theorem prover.
 probes=[
  ('CP-V-0041','periodic-resolution',r'\\operatorname{Tor}_i^A(k,k)'),
  ('CP-V-0079','Koszul',r'\\begin{pmatrix}-y\\x\\end{pmatrix}'),
  ('CP-V-0020','idempotents',r'e_1e_2=0'),
  ('CP-V-0024','non-left-exactness',r'\\xrightarrow{0}'),
  ('CP-V-0106','PID torsion-free',r'filtered colimits'),
 ]
 failures=[]
 for pid,name,needle in probes:
  statement,solution,_=blocks[pid]
  if needle not in statement+solution: failures.append((pid,name))
 print('GA-03h EXAMPLES AND COUNTEREXAMPLES')
 print('Canonical problems:',len(ids),'Imported semantic units:',semantic_count)
 print('Audited rows:',len(rows),'distinct problem IDs:',len(set(x['companion_problem_id'] for x in rows)))
 print('Derived contrasts requiring editorial review:',sum(x['status']=='REVIEW_REQUIRED' for x in rows))
 for pid,name in failures: print('WARNING: textual anchor not detected (not mathematical failure):',pid,name)
 print('NOTE: no source-provenance mapping is inferred from imported-source filenames or similarity.')
 if a.apply:
  out=root/OUT;out.mkdir(parents=True,exist_ok=True)
  tsv=out/'GA03H_EXAMPLE_COUNTEREXAMPLE_AUDIT.tsv'
  with tsv.open('w',encoding='utf-8',newline='') as f:
   w=csv.DictWriter(f,delimiter='\t',fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
  md=out/'GA03H_EXAMPLE_COUNTEREXAMPLE_AUDIT.md'
  md.write_text('# GA-03h — Example and Counterexample Audit\n\n'
   'Read-only review: mathematical contrasts need human verification.\n'
   'Imported semantic inventory is authoritative for provenance; this report does not assign source links.\n\n'
   '| Category | Companion ID | Example | Evidence | Status |\n|---|---|---|---|---|\n'+
   ''.join(f"| {r['category']} | {r['companion_problem_id']} | {r['example']} | {r['evidence_type']} | {r['status']} |\n" for r in rows)+
   '\n## Checks requiring follow-up\n'+(''.join(f'- {pid}: {name} (textual anchor not found)\n' for pid,name in failures) if failures else '- No missing textual anchors in the tested subset.\n'),encoding='utf-8')
  print('WROTE:',tsv);print('WROTE:',md)
 else: print('DRY RUN — no files written')

if __name__=='__main__':main()
