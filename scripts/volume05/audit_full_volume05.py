#!/usr/bin/env python3
from __future__ import annotations
import argparse,csv,json,re
from pathlib import Path

def tsv(path):
    with Path(path).open("r",encoding="utf-8-sig",newline="") as f:
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
                if bs%2==0:
                    cut=i;break
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
            if q.suffix=="":
                q=q.with_suffix(".tex")
            stack.append(q)
    return sorted(seen)

def source_exists(repo,name):
    if not name:return False
    return (repo/name).exists() or (repo/"chapters/tex"/name).exists()

def source_key(r):
    return (r.get("source_file",""),r.get("source_block_id",""),r.get("destination",""),r.get("source_selector",""))

def main():
    ap=argparse.ArgumentParser();ap.add_argument("--repo",required=True);args=ap.parse_args()
    repo=Path(args.repo).resolve()
    vol=repo/"books/vol05_commutative_algebra"
    rec=vol/"reconstruction"
    status=tsv(repo/"editorial/CHAPTER_STATUS.tsv")
    src=tsv(repo/"editorial/SOURCE_MIGRATION.tsv")
    blockers=[]
    problems=exercises=hints=solutions=0

    for n in range(1,29):
        code=f"V/{n:02d}"
        row=next((r for r in status if r.get("chapter_code")==code),None)
        if not row:
            blockers.append(f"MISSING_STATUS:{code}");continue
        p=repo/row.get("canonical_path","")
        if not p.exists():
            blockers.append(f"MISSING_CHAPTER:{code}");continue
        text=p.read_text(encoding="utf-8-sig")
        if "Reconstruction scaffold" in text:
            blockers.append(f"SCAFFOLD:{code}")
        pr=len(re.findall(r"\\begin\{problem\}",text))
        ex=len(re.findall(r"\\begin\{exercise\}",text))
        hi=len(re.findall(r"\\begin\{hint\}",text))
        so=len(re.findall(r"\\begin\{solution\}",text))
        if (pr,ex,hi,so)!=(12,8,8,20):
            blockers.append(f"PAIRING:{code}:{pr}/{ex}/{hi}/{so}")
        if row.get("status")!="DRAFTED":
            blockers.append(f"STATUS:{code}:{row.get('status')}")
        live=sum(1 for r in src if r.get("destination")==code)
        try:ledger=int(row.get("mapped_rule_count") or 0)
        except:ledger=-1
        if live!=ledger:
            blockers.append(f"MAPPED_RULE_COUNT:{code}:{ledger}!={live}")
        problems+=pr;exercises+=ex;hints+=hi;solutions+=so

    book=vol/"book.tex"
    includes=len(re.findall(r"\\include\{chapters/",book.read_text(encoding="utf-8-sig")))
    if includes!=28:blockers.append(f"BOOK_INCLUDES:{includes}")

    build=graph(book);labels=[];refs=[]
    for p in build:
        text=strip_comments(p.read_text(encoding="utf-8-sig"))
        labels+=re.findall(r"\\label\{([^}]+)\}",text)
        refs+=re.findall(r"\\(?:ref|eqref|autoref|pageref|cref|Cref)\{([^}]+)\}",text)
    dups=sorted({x for x in labels if labels.count(x)>1})
    missingrefs=sorted({x for x in refs if x not in set(labels)})
    if dups:blockers.append("DUPLICATE_LABELS:"+",".join(dups[:30]))
    if missingrefs:blockers.append("MISSING_REFS:"+",".join(missingrefs[:30]))

    batches=["V01_V08","V09_V18","V19_V28"]
    accounting=[];provenance=[]
    for tag in batches:
        apath=rec/f"VOLUME05_{tag}_SOURCE_RULE_ACCOUNTING.tsv"
        ppath=rec/f"VOLUME05_{tag}_DOSSIER_PROVENANCE.tsv"
        if not apath.exists():blockers.append(f"MISSING_ACCOUNTING:{tag}")
        else:accounting+=tsv(apath)
        if not ppath.exists():blockers.append(f"MISSING_PROVENANCE:{tag}")
        else:provenance+=tsv(ppath)

    live_rules=[r for r in src if re.fullmatch(r"V/\d{2}",r.get("destination",""))]
    if len(accounting)!=len(live_rules):
        blockers.append(f"ACCOUNTING_COUNT:{len(accounting)}!={len(live_rules)}")
    if len(provenance)!=336:
        blockers.append(f"PROVENANCE_COUNT:{len(provenance)}!=336")
    unresolved=[r for r in accounting if r.get("disposition","").startswith("UNRESOLVED")]
    if unresolved:blockers.append(f"UNRESOLVED_SOURCE_RULES:{len(unresolved)}")
    missing_sources=[r for r in live_rules if not source_exists(repo,r.get("source_file",""))]
    if missing_sources:blockers.append(f"MISSING_SOURCE_FILES:{len(missing_sources)}")
    if sorted(map(source_key,accounting))!=sorted(map(source_key,live_rules)):
        blockers.append("SOURCE_ACCOUNTING_KEY_MISMATCH")
    dossier_labels=[r.get("dossier_label","") for r in provenance]
    if len(dossier_labels)!=len(set(dossier_labels)):
        blockers.append("DUPLICATE_PROVENANCE_DOSSIER_LABELS")
    if (repo/"scripts/volume05/__pycache__").exists():
        blockers.append("PYTHON_CACHE_PRESENT")

    summary={
        "status":"PASS" if not blockers else "FAIL",
        "chapters":28,
        "book_includes":includes,
        "build_graph_tex_files":len(build),
        "solved_dossiers":problems,
        "exercises":exercises,
        "hints":hints,
        "solutions":solutions,
        "source_rules":len(live_rules),
        "source_accounting_rows":len(accounting),
        "provenance_rows":len(provenance),
        "corpus_guided_dossiers":sum(r.get("origin")=="CORPUS_GUIDED" for r in provenance),
        "fresh_canonical_dossiers":sum(r.get("origin")=="FRESH_CANONICAL" for r in provenance),
        "duplicate_labels":len(dups),
        "missing_refs":len(missingrefs),
        "unresolved_count":len(blockers),
        "unresolved":blockers
    }
    (rec/"VOLUME05_FULL_RECONCILIATION.json").write_text(json.dumps(summary,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    md=[
        "# Volume V — Full Reconciliation","",f"**Result:** {summary['status']}","",
        "- Canonical chapters: **28**",
        f"- Embedded solved dossiers: **{problems} / 336**",
        f"- Exercises / hints / total solutions: **{exercises} / {hints} / {solutions}**",
        f"- Live source rules accounted: **{len(accounting)} / {len(live_rules)}**",
        f"- Dossier provenance rows: **{len(provenance)} / 336**",
        f"- Corpus-guided / fresh canonical dossiers: **{summary['corpus_guided_dossiers']} / {summary['fresh_canonical_dossiers']}**",
        f"- Duplicate labels: **{len(dups)}**",
        f"- Missing references: **{len(missingrefs)}**","",
        "## Blockers",""
    ]
    md += [f"- {b}" for b in blockers] if blockers else ["None."]
    (rec/"VOLUME05_FULL_RECONCILIATION.md").write_text("\n".join(md)+"\n",encoding="utf-8")
    print(json.dumps(summary,indent=2,ensure_ascii=False))
    return 0 if not blockers else 3

if __name__=="__main__":
    raise SystemExit(main())
