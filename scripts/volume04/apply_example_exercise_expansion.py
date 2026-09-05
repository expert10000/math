#!/usr/bin/env python3
from __future__ import annotations
import argparse
from pathlib import Path
from expansion_common import load_data, path_for, expand_chapter, code_for

def main() -> int:
    ap=argparse.ArgumentParser()
    ap.add_argument("--repo",required=True)
    ap.add_argument("--data",required=True)
    ap.add_argument("--start",type=int,required=True)
    ap.add_argument("--end",type=int,required=True)
    ap.add_argument("--dry-run",action="store_true")
    args=ap.parse_args()
    repo=Path(args.repo).resolve(); data=load_data(Path(args.data).resolve())
    expected={code_for(n) for n in range(args.start,args.end+1)}
    if set(data)!=expected:
        raise RuntimeError(f"data codes do not match requested range: {sorted(set(data)^expected)}")
    plans=[]
    for n in range(args.start,args.end+1):
        code=code_for(n); path=path_for(repo,n)
        if not path.exists(): raise RuntimeError(f"missing chapter: {path}")
        original=path.read_text(encoding="utf-8-sig")
        expanded=expand_chapter(original,code,data[code])
        plans.append((code,path,original,expanded))
    changed=[x for x in plans if x[2]!=x[3]]
    if args.dry_run:
        print(f"Dry run: {len(changed)} chapter(s) would change.")
        return 0
    # All chapters are planned successfully before the first write.
    for code,path,_,expanded in changed:
        path.write_text(expanded,encoding="utf-8")
        print(f"expanded {code}: {path.relative_to(repo)}")
    print(f"Expanded {len(changed)} chapter(s).")
    return 0
if __name__=="__main__":
    raise SystemExit(main())
