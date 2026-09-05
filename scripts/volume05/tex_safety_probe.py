#!/usr/bin/env python3
import argparse,re
from pathlib import Path
from expansion_common import load_data,render_all_blocks
SPECIAL=re.compile(r"[_^#%&]")
MATH=[re.compile(r"\$.*?\$",re.S),re.compile(r"\\\(.*?\\\)",re.S),re.compile(r"\\\[.*?\\\]",re.S)]
def prose(s):
    for p in MATH: s=p.sub("",s)
    return s
def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--data",required=True); a=ap.parse_args(); data=load_data(Path(a.data).resolve()); bad=[]
    for code,d in data.items():
        strings=[]
        for e in d["examples"]: strings += [e["title"],e["body"]]
        for g in d["exercises"].values():
            for x in g: strings += [x["title"],x["prompt"],x["hint"],x["solution"]]
        for i,s in enumerate(strings,1):
            found=SPECIAL.findall(prose(s))
            if found: bad.append(f"{code}:STRING{i}:RAW_SPECIAL:{''.join(sorted(set(found)))}")
        render_all_blocks(code,d)
    if bad: print("\n".join(bad)); return 7
    print(f"PASS: TeX prose safety for {len(data)} chapter(s)."); return 0
if __name__=="__main__": raise SystemExit(main())
