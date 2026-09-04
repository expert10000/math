#!/usr/bin/env python3
from __future__ import annotations
import argparse,csv,json,re
from collections import Counter
from pathlib import Path

MEASURABLE={'analyze','apply','choose','compare','compute','connect','construct','derive','detect','determine','distinguish','explain','extend','identify','interpret','localize','prove','recognize','relate','show','solve','test','track','translate','truncate','use','verify'}
BANNED_GOALS=(
"the reader should be able to state the definitions precisely, prove the core structural results",
"move between global and localized formulations",
"explain and use",
)
BANNED_HINTS=(
"begin from the exact definition or theorem hypothesis in the corresponding section",
"identify the definition or structural theorem",
)

def rows(repo):
    with (repo/"editorial/CHAPTER_STATUS.tsv").open("r",encoding="utf-8-sig",newline="") as f:
        return list(csv.DictReader(f,delimiter="\t"))

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--repo",required=True)
    ap.add_argument("--require-goals",action="store_true")
    ap.add_argument("--require-hints-through",type=int,default=0)
    ap.add_argument("--require-full",action="store_true")
    a=ap.parse_args()
    repo=Path(a.repo).resolve()
    rs=[r for r in rows(repo) if r.get("volume")=="V"]
    blockers=[]; report=[]; allh=[]; generic=0
    totals={"goals":0,"problems":0,"exercises":0,"hints":0,"solutions":0}
    if len(rs)!=28:blockers.append(f"STATUS_ROWS:{len(rs)}!=28")
    for r in rs:
        c=r["chapter_code"]; n=int(c.split("/")[1]); p=repo/r["canonical_path"]
        if not p.exists(): blockers.append(f"MISSING:{c}"); continue
        text=p.read_text(encoding="utf-8-sig")
        gm=re.search(r"\\section\*\{Learning goals\}(.*?)(?=\\section\*\{Conceptual roadmap\})",text,re.S)
        gs=[]
        if gm: gs=[re.sub(r"\s+"," ",x).strip().rstrip(";") for x in re.findall(r"\\item\s+(.*?);",gm.group(1),re.S)]
        mcount=0
        for g in gs:
            first=re.sub(r"\\\([^)]*\\\)","",g).strip().split()
            if first and first[0].lower() in MEASURABLE:mcount+=1
        probs=re.findall(r"\\begin\{problem\}",text)
        exs=re.findall(r"\\begin\{exercise\}",text)
        hs=[re.sub(r"\s+"," ",x).strip() for x in re.findall(r"\\begin\{hint\}(.*?)\\end\{hint\}",text,re.S)]
        sols=re.findall(r"\\begin\{solution\}",text)
        totals["goals"]+=len(gs);totals["problems"]+=len(probs);totals["exercises"]+=len(exs);totals["hints"]+=len(hs);totals["solutions"]+=len(sols);allh.extend(hs)
        loc=sum(1 for h in hs if any(x in h.lower() for x in BANNED_HINTS));generic+=loc
        if a.require_goals or a.require_full:
            if len(gs)!=6:blockers.append(f"{c}:GOALS:{len(gs)}!=6")
            if mcount!=len(gs):blockers.append(f"{c}:NONMEASURABLE_GOALS:{len(gs)-mcount}")
            low=gm.group(1).lower() if gm else ""
            for frag in BANNED_GOALS:
                if frag in low:blockers.append(f"{c}:GENERIC_GOAL:{frag}")
        if n<=a.require_hints_through or a.require_full:
            if len(hs)!=8:blockers.append(f"{c}:HINTS:{len(hs)}!=8")
            if loc:blockers.append(f"{c}:GENERIC_HINTS:{loc}")
            for i,h in enumerate(hs,1):
                if len(h)<55:blockers.append(f"{c}:HINT_{i:02d}_TOO_SHORT:{len(h)}")
                if len(h)>780:blockers.append(f"{c}:HINT_{i:02d}_TOO_LONG:{len(h)}")
        if a.require_full:
            if len(probs)!=12:blockers.append(f"{c}:PROBLEMS:{len(probs)}!=12")
            if len(exs)!=8:blockers.append(f"{c}:EXERCISES:{len(exs)}!=8")
            if len(sols)!=20:blockers.append(f"{c}:SOLUTIONS:{len(sols)}!=20")
        report.append({"chapter_code":c,"chapter_title":r["chapter_title"],"goals":len(gs),"measurable_goals":mcount,"problems":len(probs),"exercises":len(exs),"hints":len(hs),"solutions":len(sols),"generic_hint_hits":loc})
    dup={h:n for h,n in Counter(allh).items() if n>1}
    if a.require_full:
        exp={"goals":168,"problems":336,"exercises":224,"hints":224,"solutions":560}
        for k,v in exp.items():
            if totals[k]!=v:blockers.append(f"TOTAL_{k.upper()}:{totals[k]}!={v}")
        if generic:blockers.append(f"TOTAL_GENERIC_HINT_HITS:{generic}")
        if dup:blockers.append(f"DUPLICATE_HINT_TEXTS:{len(dup)}")
    out=repo/"reports/series";out.mkdir(parents=True,exist_ok=True)
    fields=["chapter_code","chapter_title","goals","measurable_goals","problems","exercises","hints","solutions","generic_hint_hits"]
    with (out/"VOLUME05_PEDAGOGY_AUDIT.tsv").open("w",encoding="utf-8",newline="") as f:
        w=csv.DictWriter(f,fieldnames=fields,delimiter="\t",lineterminator="\n");w.writeheader();w.writerows(report)
    s={"status":"PASS" if not blockers else "FAIL","chapters":len(rs),"learning_outcomes":totals["goals"],"problems":totals["problems"],"exercises":totals["exercises"],"hints":totals["hints"],"solutions":totals["solutions"],"generic_hint_hits":generic,"duplicate_hint_texts":len(dup),"homological_arc":"V/22-V/28","required_hints_through":28 if a.require_full else a.require_hints_through,"blocking":blockers}
    (out/"VOLUME05_PEDAGOGY_AUDIT.json").write_text(json.dumps(s,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    md=["# Volume V Pedagogy Audit","",f"**Result:** {s['status']}","",f"- Chapters: **{len(rs)} / 28**",f"- Measurable learning outcomes: **{totals['goals']}**",f"- Solved dossiers/problems: **{totals['problems']}**",f"- Exercises / hints / solutions: **{totals['exercises']} / {totals['hints']} / {totals['solutions']}**",f"- Generic hint hits: **{generic}**",f"- Duplicate hint texts: **{len(dup)}**","","## Special arc","","V/22–V/28: chain complexes, resolutions, syzygies, minimal resolutions, Tor, Ext, and the derived-functor viewpoint.","","## Blocking findings",""]
    md += [f"- {b}" for b in blockers] if blockers else ["None."]
    (out/"VOLUME05_PEDAGOGY_AUDIT.md").write_text("\n".join(md)+"\n",encoding="utf-8")
    print(json.dumps(s,indent=2,ensure_ascii=False))
    return 0 if not blockers else 7
if __name__=="__main__":raise SystemExit(main())
