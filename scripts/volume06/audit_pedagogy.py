#!/usr/bin/env python3
from __future__ import annotations
import argparse,csv,json,re
from collections import Counter
from pathlib import Path

MARKER="% PEDAGOGY-ENRICHED-VI"
MEASURABLE={
"analyze","apply","build","calculate","check","classify","compare","compute","construct",
"describe","determine","distinguish","explain","form","identify","interpret","prove",
"recognize","recover","relate","show","state","test","track","translate","use","verify",
"work","prepare","reinterpret","pass","locate","derive","establish","write","give",
}
EXPECTED={
"chapters":49,"problems":1045,"exercises":1120,"hints":429,"solutions":1527,
"raw_pairing_mismatches":29,"pairing_failures":0,
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
        text=strip_comments(p.read_text(encoding="utf-8-sig",errors="replace"))
        for target in rx.findall(text):
            q=resolve_tex_target(p,target,roots)
            if q is not None and q not in seen:stack.append(q)
    return sorted(seen,key=lambda x:x.as_posix())

def extract_goals(text):
    # Volume VI uses both section* and subsection* in different generations.
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
    body=strip_comments(body)
    body=re.sub(r"\s+"," ",body).strip()
    return body

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--repo",required=True)
    ap.add_argument("--snapshot",action="store_true")
    ap.add_argument("--require-enriched",type=int,default=0)
    args=ap.parse_args()
    repo=Path(args.repo).resolve()
    status=[r for r in read_tsv(repo/"editorial/CHAPTER_STATUS.tsv") if r.get("volume")=="VI"]
    blockers=[]; goal_warnings=[]; rows=[]; goal_counts={}; hint_texts=[]; all_hint_files=set()
    volroot=repo/"books/vol06_algebraic_geometry"

    if len(status)!=49:blockers.append(f"STATUS_ROWS:{len(status)}!=49")

    for r in status:
        code=r["chapter_code"];cp=repo/r["canonical_path"]
        if not cp.exists():
            blockers.append(f"{code}:MISSING_CANONICAL_PATH");continue
        if r.get("status")!="FROZEN" or r.get("next_action")!="COMPLETE":
            blockers.append(f"{code}:NOT_FROZEN_COMPLETE")
        text=cp.read_text(encoding="utf-8-sig",errors="replace")
        goals=extract_goals(text)
        measurable=sum(first_word(g) in MEASURABLE for g in goals)
        goal_counts[code]=len(goals)
        if len(goals)<4:goal_warnings.append(f"{code}:LEARNING_GOALS:{len(goals)}<4")
        if goals and measurable/len(goals)<0.60:
            goal_warnings.append(f"{code}:MEASURABLE_RATIO:{measurable}/{len(goals)}")

        graph=tex_graph(cp,[volroot,repo])
        local_hints=[];local_marked=0
        for p in graph:
            t=p.read_text(encoding="utf-8-sig",errors="replace")
            bodies=re.findall(r"\\begin\{hint\}(.*?)\\end\{hint\}",t,re.S)
            if bodies:
                all_hint_files.add(p)
            for b in bodies:
                local_hints.append(b)
                if MARKER in b:local_marked+=1
                hint_texts.append(visible_hint(b))
        rows.append({
            "chapter_code":code,
            "chapter_title":r.get("chapter_title",""),
            "learning_goals":len(goals),
            "measurable_goals":measurable,
            "hints":len(local_hints),
            "enriched_hints":local_marked,
            "minimum_visible_hint_chars":min([len(visible_hint(x)) for x in local_hints],default=0),
        })

    total_hints=sum(r["hints"] for r in rows)
    enriched=sum(r["enriched_hints"] for r in rows)
    if total_hints!=EXPECTED["hints"]:
        blockers.append(f"TOTAL_HINTS:{total_hints}!={EXPECTED['hints']}")
    if args.require_enriched and enriched!=args.require_enriched:
        blockers.append(f"ENRICHED_HINTS:{enriched}!={args.require_enriched}")
    if args.require_enriched:
        short=sum(1 for h in hint_texts if h and MARKER not in h and False)
        # Every marked hint should now expose a substantive visible route.
        for r in rows:
            if r["enriched_hints"] and r["minimum_visible_hint_chars"]<70:
                blockers.append(f"{r['chapter_code']}:ENRICHED_HINT_TOO_SHORT:{r['minimum_visible_hint_chars']}")

    release_rows=read_tsv(repo/"reports/series/GLOBAL_VOLUME_RELEASE_AUDIT.tsv")
    vr=next((x for x in release_rows if x.get("volume")=="VI"),None)
    native={}
    if not vr:
        blockers.append("MISSING_GLOBAL_VOLUME_RELEASE_AUDIT_VI")
    else:
        for k in ("chapters","problems","exercises","hints","solutions","raw_pairing_mismatches","pairing_failures"):
            try:native[k]=int(vr.get(k) or -1)
            except Exception:native[k]=-1
            if native[k]!=EXPECTED[k]:
                blockers.append(f"NATIVE_{k.upper()}:{native[k]}!={EXPECTED[k]}")
        native["pairing_policy"]=vr.get("pairing_policy","")
        native["native_solution_contract"]=vr.get("native_solution_contract","")
        if native["pairing_policy"]!="NATIVE_FREEZE_PLUS_FULL_SOLUTIONS_BUILD":
            blockers.append("BAD_NATIVE_PAIRING_POLICY")
        if native["native_solution_contract"]!="PASS":
            blockers.append("NATIVE_SOLUTION_CONTRACT_NOT_PASS")

    reports=repo/"reports/series";reports.mkdir(parents=True,exist_ok=True)
    baseline_path=reports/"VOLUME06_PEDAGOGY_BASELINE.json"
    if args.snapshot:
        baseline={
            "schema":1,
            "volume":"VI",
            "chapter_goal_counts":goal_counts,
            "total_learning_outcomes":sum(goal_counts.values()),
            "total_hints":total_hints,
            "target_hint_ranges":{"VI/07-VI/25":189,"VI/39-VI/49":240},
            "native_totals":native,
        }
        baseline_path.write_text(json.dumps(baseline,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    elif baseline_path.exists():
        b=json.loads(baseline_path.read_text(encoding="utf-8"))
        if b.get("chapter_goal_counts")!=goal_counts:
            blockers.append("LEARNING_GOAL_COUNTS_CHANGED_FROM_BASELINE")
        if int(b.get("total_hints",-1))!=total_hints:
            blockers.append("HINT_COUNT_CHANGED_FROM_BASELINE")
    else:
        blockers.append("MISSING_PEDAGOGY_BASELINE")

    with (reports/"VOLUME06_PEDAGOGY_AUDIT.tsv").open("w",encoding="utf-8",newline="") as f:
        fields=["chapter_code","chapter_title","learning_goals","measurable_goals","hints","enriched_hints","minimum_visible_hint_chars"]
        w=csv.DictWriter(f,fieldnames=fields,delimiter="\t",lineterminator="\n");w.writeheader();w.writerows(rows)

    duplicate_visible=sum(1 for n in Counter(hint_texts).values() if n>1)
    summary={
        "status":"PASS" if not blockers else "FAIL",
        "chapters":len(status),
        "learning_outcomes":sum(goal_counts.values()),
        "hints":total_hints,
        "enriched_hints":enriched,
        "hint_files":len(all_hint_files),
        "duplicate_visible_hint_texts":duplicate_visible,
        "native_problems":native.get("problems"),
        "native_exercises":native.get("exercises"),
        "native_solutions":native.get("solutions"),
        "raw_pairing_mismatches":native.get("raw_pairing_mismatches"),
        "pairing_failures":native.get("pairing_failures"),
        "pairing_policy":native.get("pairing_policy"),
        "native_solution_contract":native.get("native_solution_contract"),
        "goal_warnings":goal_warnings,"blocking":blockers,
    }
    (reports/"VOLUME06_PEDAGOGY_AUDIT.json").write_text(json.dumps(summary,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    md=[
        "# Volume VI Pedagogy and Native Architecture Audit","",
        f"**Result:** {summary['status']}","",
        f"- Chapters: **{summary['chapters']} / 49**",
        f"- Existing learning outcomes preserved: **{summary['learning_outcomes']}**",
        f"- Existing hints: **{summary['hints']} / 429**",
        f"- Enriched hints: **{summary['enriched_hints']}**",
        f"- Native problems / exercises / solutions: **{summary['native_problems']} / {summary['native_exercises']} / {summary['native_solutions']}**",
        f"- Raw pairing mismatches (diagnostic): **{summary['raw_pairing_mismatches']}**",
        f"- Blocking pairing failures: **{summary['pairing_failures']}**",
        f"- Pairing policy: **{summary['pairing_policy']}**",
        f"- Native solution contract: **{summary['native_solution_contract']}**","",
        "## Policy","",
        "Volume VI keeps its heterogeneous native exercise/solution architecture. This audit preserves chapter-specific learning goals and enriches only the existing hint layer; it does not manufacture hints for chapters whose frozen edition has none.","",
        "## Goal-audit warnings","", *([f"- {x}" for x in goal_warnings] if goal_warnings else ["None."]), "", "## Blocking findings",""
    ]
    md += [f"- {x}" for x in blockers] if blockers else ["None."]
    (reports/"VOLUME06_PEDAGOGY_AUDIT.md").write_text("\n".join(md)+"\n",encoding="utf-8")
    print(json.dumps(summary,indent=2,ensure_ascii=False))
    return 0 if not blockers else 8

if __name__=="__main__":raise SystemExit(main())
