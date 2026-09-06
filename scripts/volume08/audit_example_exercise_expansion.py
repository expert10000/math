#!/usr/bin/env python3
import argparse,json,re,subprocess
from collections import Counter
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
BASE=ROOT/"reports/series/VOLUME08_EXAMPLE_EXERCISE_BASELINE.json"
BOOK=ROOT/"books/vol08_algebraic_topology/book.tex"
LAB=re.compile(r"\\label\{([^}]+)\}")
def git(*args,check=True):
    cp=subprocess.run(["git","-C",str(ROOT),*args],text=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,encoding="utf-8",errors="replace")
    if check and cp.returncode: raise RuntimeError(f"git {' '.join(args)} failed: {cp.stderr}")
    return cp
def cnt(t,e): return len(re.findall(rf"\\begin\{{{e}\}}",t))
def expected(stage,n):
    if stage<=1:return False
    if stage==2:return n<=9
    if stage==3:return n<=18
    if stage==4:return n<=27
    return n<=35
def main():
    ap=argparse.ArgumentParser();ap.add_argument("--stage",type=int,required=True,choices=range(1,8));a=ap.parse_args()
    data=json.loads(BASE.read_text(encoding="utf-8"));fail=[];rows=[];labels=[]
    book=BOOK.read_text(encoding="utf-8-sig")
    for item in data["chapters"]:
        n=int(item["chapter"].split("/")[1]); rel=item["path"]; p=ROOT/rel
        if not p.exists(): fail.append(f"{item['chapter']}: canonical missing");continue
        got=git("rev-parse",f"HEAD:{rel}").stdout.strip()
        if got!=item["protected_git_blob_sha1"]: fail.append(f"{item['chapter']}: protected Git blob drift {got}")
        d=git("diff","--quiet","HEAD","--",rel,check=False)
        if d.returncode==1: fail.append(f"{item['chapter']}: protected working-tree/index drift")
        elif d.returncode not in (0,1): fail.append(f"{item['chapter']}: protected drift check error")
        labels += LAB.findall(p.read_text(encoding="utf-8-sig"))
        ep=p.parent/"pedagogy_expansion.tex"; should=expected(a.stage,n)
        wire=f"VOL08-PEDAGOGY VIII/{n:02d}"
        if should:
            if not ep.exists(): fail.append(f"{item['chapter']}: missing pedagogy expansion");continue
            t=ep.read_text(encoding="utf-8-sig"); labels+=LAB.findall(t)
            c={"examples":cnt(t,"example"),"exercises":cnt(t,"exercise"),"hints":cnt(t,"hint"),"solutions":cnt(t,"solution")}
            if c!={"examples":3,"exercises":16,"hints":16,"solutions":16}: fail.append(f"{item['chapter']}: bad expansion counts {c}")
            code=f"VIII{n:02d}"
            if f"% BEGIN VOL08-EXPANSION {code}" not in t or f"% END VOL08-EXPANSION {code}" not in t: fail.append(f"{item['chapter']}: expansion markers missing")
            if wire not in book: fail.append(f"{item['chapter']}: book wiring missing")
            rows.append({"chapter":item["chapter"],**c})
        else:
            if ep.exists(): fail.append(f"{item['chapter']}: expansion exists before scheduled stage")
            if wire in book: fail.append(f"{item['chapter']}: book wiring exists before scheduled stage")
            rows.append({"chapter":item["chapter"],"examples":0,"exercises":0,"hints":0,"solutions":0})
    for lab,k in Counter(labels).items():
        if k>1: fail.append(f"duplicate composed label:{lab}:{k}")
    status="PASS" if not fail else "FAIL"
    print(json.dumps({"status":status,"stage":a.stage,"chapters":rows,"failures":fail},indent=2))
    return 0 if status=="PASS" else 9
if __name__=="__main__":raise SystemExit(main())
