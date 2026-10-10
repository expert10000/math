#!/usr/bin/env python3
"""GA-03f.5: guarded CP-V-0096 proof clarification plus mathematical-quality ledger.
No source-provenance mappings are approved by this script.
"""
import argparse,csv,re,sys
from pathlib import Path

CHAPTER=Path('books/companion_problems_solutions/chapters/part05_volume_v/chapter.tex')
OUT=Path('reports/companion/global_audit/GA03F_MATHEMATICAL_QUALITY.tsv')
OLD=r'''Tensor the exact presentation
\[
k[x]\xrightarrow{\ \pi\ }k[x]/(f)\to0
\]
with \(K\). Since \(K\) is flat over \(k\),
\[
K\otimes_k(k[x]/(f))
\cong
(K\otimes_k k[x])/(f)
\cong
K[x]/(f).
\]'''
NEW=r'''Start from the exact sequence of \(k\)-vector spaces
\[
0\longrightarrow k[x]\xrightarrow{\cdot f}k[x]
\xrightarrow{\pi}k[x]/(f)\longrightarrow0,
\]
where \(f\ne0\); for \(f=0\), the claim follows immediately from
\(k[x]\otimes_k K\cong K[x]\).
Since every \(k\)-vector space is flat, tensoring with \(K\) preserves
exactness. Under the natural identification
\[
k[x]\otimes_k K\cong K[x],
\]
the map \((\cdot f)\otimes\mathrm{id}_K\) becomes multiplication by the
same polynomial \(f\) in \(K[x]\). Taking cokernels therefore gives
\[
(k[x]/(f))\otimes_k K
\cong\operatorname{coker}(K[x]\xrightarrow{\cdot f}K[x])
\cong K[x]/(f).
\]'''
IDS={
'CP-V-0018':('MATHEMATICAL_DEFECT_PREVIOUS_PATCH','Invalid CRT for intersecting lines in characteristic != 2; verify GA-03f.4 correction applied'),
'CP-V-0019':('REVIEWED_NO_DEFECT_FOUND','Free polynomial modules and faithful flatness'),
'CP-V-0020':('REVIEWED_NO_DEFECT_FOUND','Idempotent summands are projective and nonfree'),
'CP-V-0021':('REVIEWED_NO_DEFECT_FOUND','Minimal free cover using Nakayama'),
'CP-V-0022':('REVIEWED_NO_DEFECT_FOUND','Quotient tensor formula with explicit inverses'),
'CP-V-0023':('REVIEWED_NO_DEFECT_FOUND','Hom commutes with localization for finite presentation'),
'CP-V-0025':('REVIEWED_NO_DEFECT_FOUND','Splitting criterion and k[x]/(x)'),
'CP-V-0044':('REVIEWED_NO_DEFECT_FOUND','Auslander–Buchsbaum via minimal resolutions and depth'),
'CP-V-0045':('REVIEWED_NO_DEFECT_FOUND','Ext map annihilated by residue-field maximal ideal'),
'CP-V-0047':('REVIEWED_NO_DEFECT_FOUND','Tor over Z via free resolution'),
'CP-V-0048':('REVIEWED_NO_DEFECT_FOUND','Tor quotient-ideal formula'),
'CP-V-0058':('REVIEWED_NO_DEFECT_FOUND','Surjective square matrix over commutative ring is invertible'),
'CP-V-0095':('REVIEWED_NO_DEFECT_FOUND','Complex tensor over real uses genuinely comaximal linear factors'),
'CP-V-0096':('PROOF_CLARIFICATION','Restore multiplication-by-f map in finite presentation, justify cokernel'),
'CP-V-0105':('REVIEWED_NO_DEFECT_FOUND','Finitely presented Hom commutes with filtered colimits'),
'CP-V-0106':('REVIEWED_NO_DEFECT_FOUND','Flat iff torsion-free over PID via filtered unions'),
'CP-V-0113':('REVIEWED_NO_DEFECT_FOUND','Ext1 over integers is Z/gcd(n,m)'),
'CP-V-0114':('REVIEWED_NO_DEFECT_FOUND','Tor and Ext as derived exactness obstructions'),
}

def main():
 p=argparse.ArgumentParser();p.add_argument('--repo',default='.');p.add_argument('--apply',action='store_true');a=p.parse_args()
 root=Path(a.repo).resolve(); path=root/CHAPTER
 if not path.is_file():sys.exit('ERROR: chapter missing')
 source=path.read_text(encoding='utf-8')
 spans=list(re.finditer(r'\\begin\{problem\}\[(CP-V-\d{4})\]',source))
 ids=[m.group(1) for m in spans]
 if len(ids)!=114 or len(set(ids))!=114:sys.exit(f'ERROR: expected 114 unique Part V problems; got {len(ids)}, unique {len(set(ids))}')
 if not set(IDS)<=set(ids):sys.exit('ERROR: missing GA03f IDs: '+repr(sorted(set(IDS)-set(ids))))
 begin=source.index(r'\begin{problem}[CP-V-0096]');end=source.find(r'\end{solution}',begin)
 if end<0:sys.exit('ERROR: CP-V-0096 solution missing')
 block=source[begin:end]
 if block.count(OLD)==1 and NEW not in block:state='PATCH_AVAILABLE';patched=source[:begin]+block.replace(OLD,NEW)+source[end:]
 elif OLD not in block and NEW in block:state='ALREADY_APPLIED';patched=source
 else:sys.exit('ERROR: CP-V-0096 solution does not match expected; no files changed')
 a18=patched.index(r'\begin{problem}[CP-V-0018]');b18=patched.find(r'\end{solution}',a18)
 s18=patched[a18:b18]
 fixed18='f(0)=g(0)' in s18 or 'f(0) = g(0)' in s18 or 'fiber product' in s18
 if 'and the two factors generate comaximal ideals' in s18:fixed18=False
 print('GA-03f.5:',state,'; CP-V-0018 CRT correction:', 'DETECTED' if fixed18 else 'NOT_CONFIRMED')
 if not fixed18:print('WARNING: CP-V-0018 correction must be confirmed before milestone closure')
 print('Mathematical-quality records:',len(IDS))
 if not a.apply:
  print('DRY RUN: no files written');return
 if patched!=source:path.write_text(patched,encoding='utf-8',newline='')
 matches=list(re.finditer(r'\\begin\{problem\}\[(CP-V-\d{4})\]',patched))
 out=root/OUT;out.parent.mkdir(parents=True,exist_ok=True)
 with out.open('w',encoding='utf-8',newline='') as f:
  w=csv.writer(f,delimiter='\t');w.writerow(['problem_id','mathematical_status','review_note','source_line','provenance_status'])
  for m in matches:
   pid=m.group(1)
   if pid not in IDS:continue
   status,note=IDS[pid]
   if pid=='CP-V-0018' and fixed18:status='PREVIOUSLY_CORRECTED_REVIEWED'
   w.writerow([pid,status,note,patched.count('\n',0,m.start())+1,'SEPARATE_REVIEW_REQUIRED'])
 print('WROTE:',out)
 print('Note: source correspondences remain independent and unapproved')
if __name__=='__main__':main()
