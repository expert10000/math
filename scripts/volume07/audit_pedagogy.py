#!/usr/bin/env python3
from __future__ import annotations
import argparse,csv,json,re
from collections import Counter
from pathlib import Path

MARKER="% PEDAGOGY-ENRICHED-VII"
MEASURABLE={
"analyze","apply","build","calculate","check","classify","compare","compute","construct",
"describe","determine","distinguish","explain","form","identify","interpret","prove",
"recognize","recover","relate","show","state","test","track","translate","use","verify",
"work","prepare","derive","establish","write","give",
}
EXPECTED={
"chapters":42,"problems":714,"exercises":1008,"hints":1008,"solutions":1722,
"raw_pairing_mismatches":0,"pairing_failures":0,
}

def read_tsv(p):
    with Path(p).open("r",encoding="utf-8-sig",newline="") as f:
        return list(csv.DictReader(f,delimiter="\t"))

def strip_comments(text):
    out=[]
    for line in text.splitlines():
        cut=None
        for i,ch in enumerate(line):
            if ch=="%":
                bs=0;j=i-1
                while j>=0 and line[j]=="\\":bs+=1;j-=1
                if bs%2==0:cut=i;break
        out.append(line if cut is None else line[:cut])
    return "\n".join(out)

def resolve_tex_target(current,target,roots):
    raw=Path(target);c=[]
    if raw.is_absolute():c.append(raw)
    else:
        c.append(current.parent/raw)
        for b in roots:c.append(Path(b)/raw)
    expanded=[]
    for q in c:
        expanded.append(q)
        if q.suffix=="":expanded.append(q.with_suffix(".tex"))
    for q in expanded:
        try:qq=q.resolve()
        except Exception:qq=q
        if qq.exists() and qq.is_file():return qq
    return None

def tex_graph(root,roots):
    root=Path(root).resolve();roots=[Path(x).resolve() for x in roots]
    seen=set();stack=[root];rx=re.compile(r"\\(?:input|include)\{([^}]+)\}")
    while stack:
        p=stack.pop()
        if p in seen or not p.exists():continue
        seen.add(p)
        t=strip_comments(p.read_text(encoding="utf-8-sig",errors="replace"))
        for target in rx.findall(t):
            q=resolve_tex_target(p,target,roots)
            if q is not None and q not in seen:stack.append(q)
    return sorted(seen,key=lambda x:x.as_posix())

def extract_goals(text):
    m=re.search(
        r"\\(?:sub)?section\*\{Learning goals\}(.*?)(?=\\(?:sub)?section\*?\{|\\section\{|\\subsection\{|$)",
        text,re.S|re.I
    )
    if not m:return []
    return [re.sub(r"\s+"," ",x).strip().rstrip(";.")
            for x in re.findall(r"\\item\s+(.*?)(?=\\item|\\end\{itemize\})",m.group(1),re.S)]

def first_word(goal):
    g=re.sub(r"\\\([^)]*\\\)","",goal)
    g=re.sub(r"\\[A-Za-z]+(?:\{[^{}]*\})?","",g)
    words=re.findall(r"[A-Za-z]+",g)
    return words[0].lower() if words else ""

def visible_hint(body):
    return re.sub(r"\s+"," ",strip_comments(body)).strip()

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--repo",required=True)
    ap.add_argument("--snapshot",action="store_true")
    ap.add_argument("--require-enriched",type=int,default=0)
    a=ap.parse_args();repo=Path(a.repo).resolve()
    status=[r for r in read_tsv(repo/"editorial/CHAPTER_STATUS.tsv") if r.get("volume")=="VII"]
    blockers=[];goal_warnings=[];rows=[];goal_counts={};hint_texts=[];hint_files=set()
    volroot=repo/"books/vol07_differential_geometry"
    if len(status)!=42:blockers.append(f"STATUS_ROWS:{len(status)}!=42")

    for r in status:
        c=r["chapter_code"];cp=repo/r["canonical_path"]
        if not cp.exists():blockers.append(f"{c}:MISSING_CANONICAL_PATH");continue
        if r.get("status")!="FROZEN" or r.get("next_action")!="COMPLETE":blockers.append(f"{c}:NOT_FROZEN_COMPLETE")
        text=cp.read_text(encoding="utf-8-sig",errors="replace")
        goals=extract_goals(text);meas=sum(first_word(x) in MEASURABLE for x in goals);goal_counts[c]=len(goals)
        if len(goals)<4:goal_warnings.append(f"{c}:LEARNING_GOALS:{len(goals)}<4")
        if goals and meas/len(goals)<0.60:goal_warnings.append(f"{c}:MEASURABLE_RATIO:{meas}/{len(goals)}")
        graph=tex_graph(cp,[volroot,repo])
        hs=[];marked=0
        for p in graph:
            t=p.read_text(encoding="utf-8-sig",errors="replace")
            bodies=re.findall(r"\\begin\{hint\}(.*?)\\end\{hint\}",t,re.S)
            if bodies:hint_files.add(p)
            for b in bodies:
                hs.append(b);hint_texts.append(visible_hint(b))
                if MARKER in b:marked+=1
        rows.append({
            "chapter_code":c,"chapter_title":r.get("chapter_title",""),
            "learning_goals":len(goals),"measurable_goals":meas,
            "hints":len(hs),"enriched_hints":marked,
            "minimum_visible_hint_chars":min([len(visible_hint(x)) for x in hs],default=0),
        })
    total_hints=sum(x["hints"] for x in rows);enriched=sum(x["enriched_hints"] for x in rows)
    if total_hints!=EXPECTED["hints"]:blockers.append(f"TOTAL_HINTS:{total_hints}!={EXPECTED['hints']}")
    if any(x["hints"]!=24 for x in rows):
        bad=[x["chapter_code"] for x in rows if x["hints"]!=24]
        blockers.append("NONUNIFORM_HINT_COUNTS:"+",".join(bad))
    if a.require_enriched and enriched!=a.require_enriched:blockers.append(f"ENRICHED_HINTS:{enriched}!={a.require_enriched}")
    if a.require_enriched:
        for r in rows:
            if r["enriched_hints"] and r["minimum_visible_hint_chars"]<80:
                blockers.append(f"{r['chapter_code']}:ENRICHED_HINT_TOO_SHORT:{r['minimum_visible_hint_chars']}")

    relrows=read_tsv(repo/"reports/series/GLOBAL_VOLUME_RELEASE_AUDIT.tsv")
    vr=next((x for x in relrows if x.get("volume")=="VII"),None);native={}
    if not vr:blockers.append("MISSING_GLOBAL_VOLUME_RELEASE_AUDIT_VII")
    else:
        for k in ("chapters","problems","exercises","hints","solutions","raw_pairing_mismatches","pairing_failures"):
            try:native[k]=int(vr.get(k) or -1)
            except Exception:native[k]=-1
            if native[k]!=EXPECTED[k]:blockers.append(f"NATIVE_{k.upper()}:{native[k]}!={EXPECTED[k]}")
        native["pairing_policy"]=vr.get("pairing_policy","")
        if native["pairing_policy"]!="STRICT_INLINE_GRAPH":blockers.append("BAD_PAIRING_POLICY")

    reports=repo/"reports/series";reports.mkdir(parents=True,exist_ok=True)
    baseline=reports/"VOLUME07_PEDAGOGY_BASELINE.json"
    if a.snapshot:
        baseline.write_text(json.dumps({
            "schema":1,"volume":"VII","chapter_goal_counts":goal_counts,
            "total_learning_outcomes":sum(goal_counts.values()),
            "total_hints":total_hints,
            "target_hint_ranges":{"VII/01-VII/21":504,"VII/22-VII/42":504},
            "native_totals":native,
        },indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    elif baseline.exists():
        b=json.loads(baseline.read_text(encoding="utf-8"))
        if b.get("chapter_goal_counts")!=goal_counts:blockers.append("LEARNING_GOAL_COUNTS_CHANGED_FROM_BASELINE")
        if int(b.get("total_hints",-1))!=total_hints:blockers.append("HINT_COUNT_CHANGED_FROM_BASELINE")
    else:blockers.append("MISSING_PEDAGOGY_BASELINE")

    with (reports/"VOLUME07_PEDAGOGY_AUDIT.tsv").open("w",encoding="utf-8",newline="") as f:
        fields=["chapter_code","chapter_title","learning_goals","measurable_goals","hints","enriched_hints","minimum_visible_hint_chars"]
        w=csv.DictWriter(f,fieldnames=fields,delimiter="\t",lineterminator="\n");w.writeheader();w.writerows(rows)

    dups=sum(1 for n in Counter(hint_texts).values() if n>1)
    s={
        "status":"PASS" if not blockers else "FAIL",
        "chapters":len(status),"learning_outcomes":sum(goal_counts.values()),
        "hints":total_hints,"enriched_hints":enriched,"hint_files":len(hint_files),
        "duplicate_visible_hint_texts":dups,
        "problems":native.get("problems"),"exercises":native.get("exercises"),"solutions":native.get("solutions"),
        "raw_pairing_mismatches":native.get("raw_pairing_mismatches"),"pairing_failures":native.get("pairing_failures"),
        "pairing_policy":native.get("pairing_policy"),"goal_warnings":goal_warnings,"blocking":blockers,
    }
    (reports/"VOLUME07_PEDAGOGY_AUDIT.json").write_text(json.dumps(s,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    md=["# Volume VII Pedagogy Audit","",f"**Result:** {s['status']}","",
        f"- Chapters: **{s['chapters']} / 42**",
        f"- Existing learning outcomes preserved: **{s['learning_outcomes']}**",
        f"- Problems / exercises / hints / solutions: **{s['problems']} / {s['exercises']} / {s['hints']} / {s['solutions']}**",
        f"- Enriched hints: **{s['enriched_hints']}**",
        f"- Pairing policy: **{s['pairing_policy']}**",
        f"- Raw / blocking pairing mismatches: **{s['raw_pairing_mismatches']} / {s['pairing_failures']}**","",
        "## Policy","",
        "Volume VII keeps its existing chapter-specific learning outcomes. The enrichment preserves each original exercise hint as the first clue and appends a chapter-specific geometric method or invariant check.","",
        "## Goal-audit warnings","", *([f"- {x}" for x in goal_warnings] if goal_warnings else ["None."]), "", "## Blocking findings",""]
    md += [f"- {x}" for x in blockers] if blockers else ["None."]
    (reports/"VOLUME07_PEDAGOGY_AUDIT.md").write_text("\n".join(md)+"\n",encoding="utf-8")
    print(json.dumps(s,indent=2,ensure_ascii=False))
    return 0 if not blockers else 9

if __name__=="__main__":raise SystemExit(main())
