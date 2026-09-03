#!/usr/bin/env python3
from __future__ import annotations
import argparse,csv,json,re
from pathlib import Path

def tsv(p):
    with Path(p).open("r",encoding="utf-8-sig",newline="") as f:
        return list(csv.DictReader(f,delimiter="\t"))

def strip_comments(text):
    out=[]
    for line in text.splitlines():
        cut=None
        for i,ch in enumerate(line):
            if ch=="%":
                bs=0;j=i-1
                while j>=0 and line[j]=="\\":
                    bs+=1;j-=1
                if bs%2==0:cut=i;break
        out.append(line if cut is None else line[:cut])
    return "\n".join(out)

def graph(root):
    seen=set();stack=[root]
    rx=re.compile(r"\\(?:input|include)\{([^}]+)\}")
    while stack:
        p=stack.pop().resolve()
        if p in seen or not p.exists():continue
        seen.add(p)
        text=strip_comments(p.read_text(encoding="utf-8-sig"))
        for target in rx.findall(text):
            q=p.parent/target
            if q.suffix=="":q=q.with_suffix(".tex")
            stack.append(q)
    return sorted(seen)

def source_exists(repo,name):
    return bool(name) and ((repo/name).exists() or (repo/"chapters/tex"/name).exists())

def main():
    ap=argparse.ArgumentParser();ap.add_argument("--repo",required=True);args=ap.parse_args()
    repo=Path(args.repo).resolve();vol=repo/"books/vol03_fourier_distributions_pde";block=[]
    status=tsv(repo/"editorial/CHAPTER_STATUS.tsv");src=tsv(repo/"editorial/SOURCE_MIGRATION.tsv")
    probs=exs=hints=sols=0
    for n in range(1,29):
        code=f"III/{n:02d}";sr=next((r for r in status if r.get("chapter_code")==code),None)
        if not sr:block.append(f"MISSING_STATUS:{code}");continue
        p=repo/sr["canonical_path"]
        if not p.exists():block.append(f"MISSING_CHAPTER:{code}");continue
        text=p.read_text(encoding="utf-8-sig")
        if "Reconstruction scaffold" in text:block.append(f"SCAFFOLD:{code}")
        pr=len(re.findall(r"\\begin\{problem\}",text));ex=len(re.findall(r"\\begin\{exercise\}",text))
        hi=len(re.findall(r"\\begin\{hint\}",text));so=len(re.findall(r"\\begin\{solution\}",text))
        if (pr,ex,hi,so)!=(12,8,8,20):block.append(f"PAIRING:{code}:{pr}/{ex}/{hi}/{so}")
        if sr.get("status")!="DRAFTED":block.append(f"STATUS:{code}:{sr.get('status')}")
        expected=sum(1 for r in src if r.get("destination")==code)
        try:actual=int(sr.get("mapped_rule_count") or 0)
        except:actual=-1
        if actual!=expected:block.append(f"MAPPED_RULE_COUNT:{code}:{actual}!={expected}")
        probs+=pr;exs+=ex;hints+=hi;sols+=so

    build=graph(vol/"book.tex");labels=[];refs=[]
    for p in build:
        text=strip_comments(p.read_text(encoding="utf-8-sig"))
        labels+=re.findall(r"\\label\{([^}]+)\}",text)
        refs+=re.findall(r"\\(?:ref|eqref|autoref|pageref|cref|Cref)\{([^}]+)\}",text)
    dups=sorted({x for x in labels if labels.count(x)>1})
    if dups:block.append("DUPLICATE_LABELS:"+",".join(dups[:20]))
    missingrefs=sorted({x for x in refs if x not in set(labels)})
    if missingrefs:block.append("MISSING_REFS:"+",".join(missingrefs[:20]))

    rec=vol/"reconstruction"
    batches=["III01_III08","III09_III15","III16_III22","III23_III28"]
    accounting=[];provenance=[]
    for tag in batches:
        apath=rec/f"VOLUME03_{tag}_SOURCE_RULE_ACCOUNTING.tsv"
        ppath=rec/f"VOLUME03_{tag}_DOSSIER_PROVENANCE.tsv"
        if not apath.exists():block.append(f"MISSING_ACCOUNTING:{tag}")
        else:accounting+=tsv(apath)
        if not ppath.exists():block.append(f"MISSING_PROVENANCE:{tag}")
        else:provenance+=tsv(ppath)
    live_rules=[r for r in src if re.fullmatch(r"III/\d{2}",r.get("destination",""))]
    if len(accounting)!=len(live_rules):block.append(f"ACCOUNTING_COUNT:{len(accounting)}!={len(live_rules)}")
    if len(provenance)!=336:block.append(f"PROVENANCE_COUNT:{len(provenance)}!=336")
    unresolved=[r for r in accounting if r.get("disposition","").startswith("UNRESOLVED")]
    if unresolved:block.append(f"UNRESOLVED_SOURCE_RULES:{len(unresolved)}")
    missing_sources=[r for r in live_rules if not source_exists(repo,r.get("source_file",""))]
    if missing_sources:block.append(f"MISSING_SOURCE_FILES:{len(missing_sources)}")
    keys=lambda r:(r.get("source_file",""),r.get("source_block_id",""),r.get("destination",""),r.get("source_selector",""))
    if sorted(map(keys,accounting))!=sorted(map(keys,live_rules)):
        block.append("SOURCE_ACCOUNTING_KEY_MISMATCH")
    if (repo/"scripts/volume03/__pycache__").exists():block.append("PYTHON_CACHE_PRESENT")

    summary={"status":"PASS" if not block else "FAIL","chapters":28,"build_graph_tex_files":len(build),
             "solved_dossiers":probs,"exercises":exs,"hints":hints,"solutions":sols,
             "source_rules":len(live_rules),"source_accounting_rows":len(accounting),
             "provenance_rows":len(provenance),"duplicate_labels":len(dups),"missing_refs":len(missingrefs),
             "unresolved_count":len(block),"unresolved":block}
    (rec/"VOLUME03_FULL_RECONCILIATION.json").write_text(json.dumps(summary,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    md=["# Volume III — Full Reconciliation","",f"**Result:** {summary['status']}","",
        f"- Canonical chapters: **28**",f"- Embedded solved dossiers: **{probs} / 336**",
        f"- Exercises / hints / total solutions: **{exs} / {hints} / {sols}**",
        f"- Live source rules accounted: **{len(accounting)} / {len(live_rules)}**",
        f"- Dossier provenance rows: **{len(provenance)} / 336**",
        f"- Duplicate labels: **{len(dups)}**",f"- Missing references: **{len(missingrefs)}**","",
        "## Blockers",""]
    md += [f"- {b}" for b in block] if block else ["None."]
    (rec/"VOLUME03_FULL_RECONCILIATION.md").write_text("\n".join(md)+"\n",encoding="utf-8")
    print(json.dumps(summary,indent=2,ensure_ascii=False))
    return 0 if not block else 3
if __name__=="__main__":raise SystemExit(main())
