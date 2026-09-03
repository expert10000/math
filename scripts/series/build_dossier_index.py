#!/usr/bin/env python3
from __future__ import annotations
import argparse,csv,json,re
from collections import Counter,defaultdict
from pathlib import Path

VOLUMES=[
("I","vol01_linear_algebra"),
("II","vol02_real_analysis"),
("III","vol03_fourier_distributions_pde"),
("IV","vol04_complex_analysis"),
("V","vol05_commutative_algebra"),
("VI","vol06_algebraic_geometry"),
("VII","vol07_differential_geometry"),
("VIII","vol08_algebraic_topology"),
]

def read_tsv(path):
    path=Path(path)
    if not path.exists(): return []
    with path.open("r",encoding="utf-8-sig",newline="") as f:
        return list(csv.DictReader(f,delimiter="\t"))

def write_tsv(path,rows,fields):
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    with path.open("w",encoding="utf-8",newline="") as f:
        w=csv.DictWriter(f,fieldnames=fields,delimiter="\t",lineterminator="\n",extrasaction="ignore")
        w.writeheader();w.writerows(rows)

def read_text(path):
    return Path(path).read_text(encoding="utf-8-sig",errors="replace")

def strip_comments(text):
    out=[]
    for line in text.splitlines():
        cut=None
        for i,ch in enumerate(line):
            if ch=="%":
                bs=0;j=i-1
                while j>=0 and line[j]=="\\":
                    bs+=1;j-=1
                if bs%2==0:
                    cut=i;break
        out.append(line if cut is None else line[:cut])
    return "\n".join(out)

def resolve_target(current,target,roots):
    raw=Path(target.strip())
    candidates=[]
    if raw.is_absolute():
        candidates.append(raw)
    else:
        candidates.append(current.parent/raw)
        for base in roots:
            candidates.append(Path(base)/raw)
    expanded=[]
    for q in candidates:
        expanded.append(q)
        if q.suffix=="":
            expanded.append(q.with_suffix(".tex"))
    for q in expanded:
        try:q=q.resolve()
        except Exception:pass
        if q.exists() and q.is_file():
            return q
    return None

def tex_graph(root,roots):
    root=Path(root).resolve(); roots=[Path(x).resolve() for x in roots]
    seen=set();stack=[root];ordered=[]
    rx=re.compile(r"\\(?:input|include)\{([^}]+)\}")
    while stack:
        p=stack.pop()
        if p in seen or not p.exists(): continue
        seen.add(p);ordered.append(p)
        text=strip_comments(read_text(p))
        children=[]
        for target in rx.findall(text):
            q=resolve_target(p,target,roots)
            if q is not None and q not in seen:
                children.append(q)
        stack.extend(reversed(children))
    return ordered

def clean_title(raw):
    if not raw:return ""
    s=re.sub(r"\s+"," ",raw).strip()
    return s

def extract_entries(path):
    text=strip_comments(read_text(path))
    begin=re.compile(r"\\begin\{(problem|challenge)\}(?:\[([^\]]*)\])?",re.S)
    rows=[]
    for m in begin.finditer(text):
        kind=m.group(1)
        end=re.search(r"\\end\{"+re.escape(kind)+r"\}",text[m.end():],re.S)
        if not end: continue
        endpos=m.end()+end.end()
        body=text[m.end():m.end()+end.start()]
        lab=re.search(r"\\label\{([^}]+)\}",body)
        if not lab:
            after=text[m.end():min(endpos+120,len(text))]
            lab=re.search(r"\\label\{([^}]+)\}",after)
        title=clean_title(m.group(2))
        line=text.count("\n",0,m.start())+1

        # A same-file solution counts as directly embedded when it starts after
        # this entry and before the next problem/challenge/exercise.
        tail=text[endpos:]
        nxt=re.search(r"\\begin\{(?:problem|challenge|exercise)\}",tail)
        sol=re.search(r"\\begin\{solution\}",tail)
        inline=bool(sol and (not nxt or sol.start()<nxt.start()))
        rows.append({
            "kind":kind,"title":title,"label":lab.group(1) if lab else "",
            "line":line,"inline_solution":inline,
        })
    return rows

def load_provenance(repo):
    by_label={}
    files=[]
    for p in sorted((repo/"books").rglob("*DOSSIER_PROVENANCE.tsv")):
        files.append(p)
        for row in read_tsv(p):
            lab=row.get("dossier_label","")
            if lab:
                item=dict(row)
                item["_ledger"]=p.relative_to(repo).as_posix()
                by_label[lab]=item
    return by_label,files

def main():
    ap=argparse.ArgumentParser();ap.add_argument("--repo",required=True);args=ap.parse_args()
    repo=Path(args.repo).resolve()
    reports=repo/"reports/series";reports.mkdir(parents=True,exist_ok=True)
    status=read_tsv(repo/"editorial/CHAPTER_STATUS.tsv")
    pairing=read_tsv(reports/"GLOBAL_CHAPTER_PAIRING_AUDIT.tsv")
    source_rules=read_tsv(reports/"GLOBAL_SOURCE_RULE_RECONCILIATION.tsv")
    recon=json.loads((reports/"GLOBAL_SERIES_RECONCILIATION.json").read_text(encoding="utf-8"))
    prov,prov_files=load_provenance(repo)

    pair_by_code={r.get("chapter_code",""):r for r in pairing}
    rule_by_code=defaultdict(list)
    for r in source_rules:
        dest=r.get("destination","")
        if re.fullmatch(r"(?:VIII|VII|VI|IV|III|II|V|I)/\d{2}",dest):
            rule_by_code[dest].append(r)

    rows=[]; blockers=[]; problem_count=0;challenge_count=0
    by_volume=Counter();by_origin=Counter();by_solution=Counter()
    for sr in status:
        code=sr.get("chapter_code","")
        v=sr.get("volume","")
        cp=repo/sr.get("canonical_path","")
        if not cp.exists():
            blockers.append(f"MISSING_CHAPTER:{code}")
            continue
        volume_root=cp.parents[2] if cp.parent.name.startswith("ch") else next((repo/"books"/d for vv,d in VOLUMES if vv==v),cp.parent)
        graph=tex_graph(cp,[volume_root,repo])
        ordinals=Counter()
        pair=pair_by_code.get(code,{})
        policy=pair.get("pairing_policy","")
        rules=rule_by_code.get(code,[])
        dispositions=Counter(r.get("global_disposition","") for r in rules)
        disp_text=";".join(f"{k}:{n}" for k,n in sorted(dispositions.items()) if k)
        for gp in graph:
            placement="ROOT_CHAPTER" if gp.resolve()==cp.resolve() else "INCLUDED_ACTIVE_FILE"
            rel=gp.relative_to(repo).as_posix()
            for item in extract_entries(gp):
                kind=item["kind"];ordinals[kind]+=1
                if kind=="problem":problem_count+=1
                else:challenge_count+=1
                by_volume[v]+=1

                lab=item["label"]
                canonical_id=lab or f"{code}:{kind}:{ordinals[kind]:03d}"
                pv=prov.get(lab,{}) if lab else {}
                if pv:
                    origin=pv.get("origin","PROVENANCE_LEDGER")
                    psource=pv.get("source_file","-")
                    pblock=pv.get("source_block_id","-")
                    ledger=pv.get("_ledger","")
                else:
                    origin="NATIVE_FROZEN_OR_UNTRACKED_CANONICAL"
                    psource="-";pblock="-";ledger=""
                by_origin[origin]+=1

                if item["inline_solution"]:
                    solution_mode="INLINE_SAME_FILE"
                    solution_path=rel
                elif v=="VI":
                    solution_mode="VOLUME06_FULL_SOLUTIONS_EDITION"
                    solution_path="books/vol06_algebraic_geometry/book_full_solutions.tex"
                elif policy=="STRICT_INLINE_GRAPH" and pair.get("pairing")=="PASS":
                    solution_mode="CHAPTER_GRAPH_PAIRED"
                    solution_path=sr.get("canonical_path","")
                else:
                    solution_mode="ACTIVE_GRAPH_OR_VOLUME_NATIVE"
                    solution_path=sr.get("canonical_path","")
                by_solution[solution_mode]+=1

                rows.append({
                    "canonical_dossier_id":canonical_id,
                    "volume":v,"chapter_code":code,"chapter_title":sr.get("chapter_title",""),
                    "entry_kind":kind,"ordinal_in_chapter_kind":ordinals[kind],
                    "label":lab or "-","title":item["title"] or "-",
                    "source_path":rel,"source_line":item["line"],"placement":placement,
                    "solution_mode":solution_mode,"solution_path":solution_path,
                    "provenance_origin":origin,"provenance_ledger":ledger or "-",
                    "provenance_source_file":psource,"provenance_source_block_id":pblock,
                    "mapped_source_rules":len(rules),"source_rule_dispositions":disp_text or "-",
                })

    expected=int(recon.get("problems",0) or 0)
    if problem_count!=expected:
        blockers.append(f"PROBLEM_INDEX_COUNT:{problem_count}!={expected}")
    ids=[r["canonical_dossier_id"] for r in rows]
    if len(ids)!=len(set(ids)):
        dup=[x for x,n in Counter(ids).items() if n>1]
        blockers.append("DUPLICATE_DOSSIER_IDS:"+",".join(dup[:20]))
    if any(r["solution_mode"]=="" for r in rows):
        blockers.append("MISSING_SOLUTION_MODE")

    fields=[
        "canonical_dossier_id","volume","chapter_code","chapter_title","entry_kind",
        "ordinal_in_chapter_kind","label","title","source_path","source_line","placement",
        "solution_mode","solution_path","provenance_origin","provenance_ledger",
        "provenance_source_file","provenance_source_block_id","mapped_source_rules",
        "source_rule_dispositions"
    ]
    write_tsv(reports/"DOSSIER_INDEX.tsv",rows,fields)

    # A compact provenance atlas keeps one row per indexed problem/challenge,
    # but focuses on source/provenance fields.
    write_tsv(reports/"DOSSIER_PROVENANCE_ATLAS.tsv",rows,[
        "canonical_dossier_id","volume","chapter_code","entry_kind","label","title",
        "provenance_origin","provenance_ledger","provenance_source_file",
        "provenance_source_block_id","mapped_source_rules","source_rule_dispositions"
    ])

    summary={
        "status":"PASS" if not blockers else "FAIL",
        "canonical_problem_entries":problem_count,
        "canonical_challenge_entries":challenge_count,
        "indexed_problem_like_entries":len(rows),
        "expected_problem_entries_from_global_reconciliation":expected,
        "provenance_ledgers_discovered":len(prov_files),
        "provenance_labels_loaded":len(prov),
        "by_volume":dict(sorted(by_volume.items())),
        "by_provenance_origin":dict(sorted(by_origin.items())),
        "by_solution_mode":dict(sorted(by_solution.items())),
        "blocking":blockers,
    }
    (reports/"DOSSIER_INDEX_SUMMARY.json").write_text(json.dumps(summary,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")

    md=[
        "# Canonical Dossier Index and Provenance Atlas","",
        f"**Result:** {summary['status']}","",
        "This index is generated from the recursive active TeX graph of every FROZEN canonical chapter.",
        "A row therefore represents problem/challenge material physically embedded in the canonical source/build graph.",
        "",
        f"- Canonical `problem` entries: **{problem_count}**",
        f"- Canonical `challenge` entries: **{challenge_count}**",
        f"- Total indexed problem-like entries: **{len(rows)}**",
        f"- Expected `problem` entries from global reconciliation: **{expected}**",
        f"- Dossier provenance ledgers discovered: **{len(prov_files)}**",
        f"- Explicit provenance labels loaded: **{len(prov)}**","",
        "## Interpretation","",
        "- `ROOT_CHAPTER` means the dossier is written directly in the canonical `chapter.tex`.",
        "- `INCLUDED_ACTIVE_FILE` means it is in a TeX file reached by the canonical chapter build graph.",
        "- `VOLUME06_FULL_SOLUTIONS_EDITION` reflects Volume VI's native edition-controlled solution architecture.",
        "- `NATIVE_FROZEN_OR_UNTRACKED_CANONICAL` does not mean unresolved legacy material; it means no newer dossier-level provenance TSV exists for that individual label.",
        "",
        "All source-migration accounting remains governed by `GLOBAL_SOURCE_RULE_RECONCILIATION.tsv`; the dossier index does not claim a one-to-one legacy-row-to-dossier transformation.",
        "",
        "## Volume counts",""
    ]
    for v,n in sorted(by_volume.items()):
        md.append(f"- Volume {v}: **{n}** problem/challenge entries")
    md += ["","## Blocking findings",""]
    md += [f"- {x}" for x in blockers] if blockers else ["None."]
    (reports/"DOSSIER_INDEX.md").write_text("\n".join(md)+"\n",encoding="utf-8")

    print(json.dumps(summary,indent=2,ensure_ascii=False))
    return 0 if not blockers else 4

if __name__=="__main__":
    raise SystemExit(main())
