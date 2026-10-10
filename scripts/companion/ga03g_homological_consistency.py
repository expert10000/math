#!/usr/bin/env python3
"""GA-03g read-only homological consistency inventory. --apply writes a NEW ledger only."""
import argparse,csv,re,sys
from pathlib import Path
CH='books/companion_problems_solutions/chapters/part05_volume_v/chapter.tex'
OUT='reports/companion/global_audit/GA03G_HOMOLOGICAL_CONSISTENCY.tsv'
SECTIONS={
'V/22':['0046','0110'],
'V/23':['0041','0077','0078','0079','0082'],
'V/24':['0111','0112'],
'V/25':['0042','0043'],
'V/26':['0047','0048'],
'V/27':['0045','0113'],
'V/28':['0044','0114']}
LINKS=[('0042','0021','minimal covers -> minimal resolutions'),('0043','0042','minimal resolutions -> projective dimension'),('0044','0045','minimal differentials -> Ext vanishing'),('0046','0114','connecting homomorphism -> derived long exact sequences'),('0111','0043','Schanuel lemma -> resolution invariance'),('0112','0079','syzygy generators -> polynomial resolution'),('0041','0043','periodic Tor -> infinite projective dimension'),('0044','0043','projective dimension -> Auslander-Buchsbaum'),('0048','0047','ideal-intersection Tor -> cyclic Tor'),('0113','0114','Ext computation -> derived obstruction')]
ANCHORS=[('0041',r'\operatorname{Tor}_i^A(k,k)'),('0041',r'\operatorname{Ext}_A^1(k,A)'),('0042',r'\mathfrak mF_0'),('0043',r'\operatorname{Tor}_{i+1}^A(k,M)=0'),('0111',r'K\oplus F\''),('0112',r'(-y,x,0)'),('0046',r'\partial_n'),('0047',r'N[n]'),('0048',r'\frac{I\cap J}{IJ}'),('0045',r'f_*'),('0044',r'\operatorname{depth}K'),('0113',r'\gcd(n,m)'),('0114',r'\operatorname{Ext}_R^1')]
def run(repo):
 s=(repo/CH).read_text(encoding='utf-8'); heads=list(re.finditer(r'\\section\*\{(V/\d{2})\s+---\s+([^}]+)\}',s)); blocks={}
 for i,m in enumerate(heads):blocks[m.group(1)]=s[m.end():heads[i+1].start() if i+1<len(heads) else len(s)]
 problems={}
 for m in re.finditer(r'\\begin\{problem\}\[(CP-V-\d{4})\]([\s\S]*?)\\end\{problem\}\s*\\begin\{solution\}([\s\S]*?)\\end\{solution\}',s):problems[m.group(1)]=(m.group(2),m.group(3))
 rows=[]
 def add(kind,section,pid,status,detail):rows.append(dict(check_type=kind,section=section,problem_id=pid,status=status,detail=detail))
 for section,nums in SECTIONS.items():
  expected=['CP-V-'+n for n in nums];b=blocks.get(section,'');found=re.findall(r'\\begin\{problem\}\[(CP-V-\d{4})\]',b);sol=len(re.findall(r'\\begin\{solution\}',b));add('SECTION',section,'','PASS' if found==expected and sol==len(expected) else 'FAIL',f'expected {expected}; actual {found}; solutions={sol}')
  for pid in expected:add('PAIR',section,pid,'PASS' if pid in problems else 'FAIL','paired problem and solution present' if pid in problems else 'missing or unpaired')
 for a,b,why in LINKS:add('CROSS_LINK','',f'CP-V-{a} -> CP-V-{b}','REVIEW' if 'CP-V-'+a in problems and 'CP-V-'+b in problems else 'FAIL',why+'; editorial correspondence to verify')
 for n,needle in ANCHORS:
  pair=problems.get('CP-V-'+n,('',''));add('MATH_ANCHOR','','CP-V-'+n,'PASS' if needle in ''.join(pair) else 'REVIEW',f'{needle}; textual anchor only, not proof certification')
 p18=''.join(problems.get('CP-V-0018',('','')));p96=''.join(problems.get('CP-V-0096',('','')))
 add('GA03F_REGRESSION','V/10','CP-V-0018','PASS' if ('f(0)=g(0)' in p18 or 'f(0) = g(0)' in p18) and 'and the two factors generate comaximal ideals' not in p18 else 'FAIL','corrected tensor-product CRT reasoning retained')
 add('GA03F_REGRESSION','V/11','CP-V-0096','PASS' if r'\xrightarrow{\cdot f}' in p96 and r'\operatorname{coker}' in p96 else 'FAIL','corrected base-change proof retained')
 source=repo/'imports/problem_inventory/SEMANTIC_PROBLEM_UNITS.tsv'
 if source.is_file():
  with source.open(encoding='utf-8-sig',newline='') as f: count=sum(1 for _ in csv.DictReader(f,delimiter='\t'))
  add('IMPORT_INVENTORY','','','PASS',f'{count} semantic units; no provenance inference from filename/score')
 else:add('IMPORT_INVENTORY','','','FAIL','authoritative imported semantic units unavailable')
 return rows
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--repo',type=Path,default=Path('.'));p.add_argument('--apply',action='store_true');a=p.parse_args()
 try:rows=run(a.repo.resolve())
 except Exception as e:print('ERROR',e);sys.exit(2)
 from collections import Counter
 counts=Counter(r['status'] for r in rows)
 print('GA-03g:',sum(map(len,SECTIONS.values())),'canonical problems in',len(SECTIONS),'sections;',len(rows),'checks;',dict(counts))
 for r in rows:
  if r['status'] in ('FAIL','REVIEW'):print(r['status'],r['check_type'],r['problem_id'] or r['section'],r['detail'])
 if a.apply:
  out=a.repo.resolve()/OUT;out.parent.mkdir(parents=True,exist_ok=True)
  with out.open('w',encoding='utf-8',newline='') as f:w=csv.DictWriter(f,fieldnames=list(rows[0]),delimiter='\t');w.writeheader();w.writerows(rows)
  print('WROTE',out)
 else:print('DRY RUN; no files changed')
 if counts['FAIL']:sys.exit(1)
