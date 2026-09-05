#!/usr/bin/env python3
import argparse
from pathlib import Path
from expansion_common import load_data,path_for,expand_chapter,code_for
def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--repo",required=True); ap.add_argument("--data",required=True); ap.add_argument("--start",type=int,required=True); ap.add_argument("--end",type=int,required=True); ap.add_argument("--dry-run",action="store_true"); a=ap.parse_args()
    repo=Path(a.repo).resolve(); data=load_data(Path(a.data).resolve()); expected={code_for(n) for n in range(a.start,a.end+1)}
    if set(data)!=expected: raise RuntimeError(f"data mismatch: {sorted(set(data)^expected)}")
    plans=[]
    for n in range(a.start,a.end+1):
        code=code_for(n); p=path_for(repo,n)
        if not p.exists(): raise RuntimeError(f"missing chapter: {p}")
        old=p.read_text(encoding="utf-8-sig"); new=expand_chapter(old,code,data[code]); plans.append((code,p,old,new))
    changed=[x for x in plans if x[2]!=x[3]]
    if a.dry_run: print(f"Dry run: {len(changed)} chapter(s) would change."); return 0
    for code,p,old,new in changed: p.write_text(new,encoding="utf-8"); print(f"expanded {code}: {p.relative_to(repo)}")
    print(f"Expanded {len(changed)} chapter(s)."); return 0
if __name__=="__main__": raise SystemExit(main())
