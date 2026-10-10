#!/usr/bin/env python3
"""GA-03f.4: guarded repair to CP-V-0018(b); dry-run by default."""
import argparse, pathlib, sys

CHAPTER = 'books/companion_problems_solutions/chapters/part05_volume_v/chapter.tex'
OLD = r"""If \(\operatorname{char}k\ne2\), then
\[
v^2-w^2=(v-w)(v+w),
\]
and the two factors generate comaximal ideals. Hence the Chinese remainder
theorem gives
\[
k[v,w]/(v^2-w^2)
\cong
k[v,w]/(v-w)\times k[v,w]/(v+w)
\cong
k[v]\times k[v].
\]"""
NEW = r"""If \(\operatorname{char}k\ne2\), then
\[
v^2-w^2=(v-w)(v+w).
\]
The two principal ideals are \emph{not} comaximal: their sum is
\((v-w,v+w)=(v,w)\), not the unit ideal. Therefore the Chinese
remainder theorem does not give a direct product. Instead, the two
lines meet at the origin, and restriction to each line gives
\[
k[v,w]/(v^2-w^2)
\cong
\{(f(t),g(t))\in k[t]\times k[t]:f(0)=g(0)\}.
\]
To justify this, the restriction map to the two lines has kernel
\((v-w)\cap(v+w)=((v-w)(v+w))\), while its image consists
precisely of pairs agreeing at the intersection point. In
particular, the quotient is reduced but is not isomorphic to
\(k[t]\times k[t]\)."""
def main():
 p=argparse.ArgumentParser();p.add_argument('--repo',default='.');p.add_argument('--apply',action='store_true');a=p.parse_args()
 chapter=pathlib.Path(a.repo)/CHAPTER
 if not chapter.is_file():sys.exit('ERROR chapter file missing')
 text=chapter.read_text(encoding='utf-8')
 a0=text.find(r'\begin{problem}[CP-V-0018]')
 b0=text.find(r'\end{solution}',a0)
 if a0<0 or b0<0:sys.exit('ERROR CP-V-0018 solution bounds missing')
 block=text[a0:b0]
 if OLD in block and block.count(OLD)==1:
  print('GA-03f.4 PATCH_AVAILABLE: replace noncomaximal CRT claim')
  patched=text[:a0]+block.replace(OLD,NEW)+text[b0:]
 elif NEW in block and OLD not in block:
  print('GA-03f.4 ALREADY_APPLIED');patched=text
 else:sys.exit('ERROR expected CP-V-0018 source text mismatch; no changes')
 if not a.apply:print('DRY RUN; no files changed');return
 if patched!=text:
  with chapter.open('w',encoding='utf-8',newline='') as f:f.write(patched)
 print('GA-03f.4 APPLIED: '+str(chapter))
if __name__=='__main__':main()
