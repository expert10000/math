#!/usr/bin/env python3
from __future__ import annotations
import argparse,csv,json,re,hashlib
from pathlib import Path

def tsv(p):
    with p.open("r",encoding="utf-8-sig",newline="") as f:return list(csv.DictReader(f,delimiter="\t"))

def write_tsv(p,rows,fields):
    p.parent.mkdir(parents=True,exist_ok=True)
    lines=["\t".join(fields)]
    for r in rows:
        vals=[]
        for f in fields:
            v=r.get(f,"-")
            vals.append("-" if v is None or v=="" else str(v))
        lines.append("\t".join(vals))
    p.write_text("\n".join(lines)+"\n",encoding="utf-8")

def source_exists(repo,name):
    if not name:return False
    return (repo/name).exists() or (repo/"chapters/tex"/name).exists()

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

def build_graph(root):
    seen=set();stack=[root]
    rx=re.compile(r"\\(?:input|include)\{([^}]+)\}")
    while stack:
        p=stack.pop().resolve()
        if p in seen or not p.exists():continue
        seen.add(p)
        text=strip_comments(p.read_text(encoding="utf-8-sig"))
        for target in rx.findall(text):
            q=(p.parent/target)
            if q.suffix=="":q=q.with_suffix(".tex")
            stack.append(q)
    return sorted(seen)

def main():
    ap=argparse.ArgumentParser();ap.add_argument("--repo",required=True);args=ap.parse_args()
    repo=Path(args.repo).resolve();vol=repo/"books/vol02_real_analysis";block=[]
    status=tsv(repo/"editorial/CHAPTER_STATUS.tsv")
    rows=[];labels=[];refs=[];total_p=total_e=total_h=total_s=0
    for n in range(1,26):
        code=f"II/{n:02d}";r=next((x for x in status if x.get("chapter_code")==code),None)
        if not r:block.append(f"MISSING_STATUS:{code}");continue
        p=repo/r["canonical_path"]
        if not p.exists():block.append(f"MISSING_CHAPTER:{code}");continue
        text=p.read_text(encoding="utf-8-sig")
        if "Reconstruction scaffold" in text:block.append(f"SCAFFOLD:{code}")
        pr=len(re.findall(r"\\begin\{problem\}",text));ex=len(re.findall(r"\\begin\{exercise\}",text))
        hi=len(re.findall(r"\\begin\{hint\}",text));so=len(re.findall(r"\\begin\{solution\}",text))
        if (pr,ex,hi,so)!=(12,8,8,20):block.append(f"PAIRING:{code}:{pr}/{ex}/{hi}/{so}")
        if r.get("status")!="DRAFTED":block.append(f"STATUS:{code}:{r.get('status')}")
        rows.append({"chapter_code":code,"problems":pr,"exercises":ex,"hints":hi,"solutions":so,
                     "expected_solutions":pr+ex,"pairing":"PASS" if so==pr+ex and hi==ex else "FAIL"})
        total_p+=pr;total_e+=ex;total_h+=hi;total_s+=so
    graph=build_graph(vol/"book.tex")
    for p in graph:
        text=strip_comments(p.read_text(encoding="utf-8-sig"))
        labels += [(m,p) for m in re.findall(r"\\label\{([^}]+)\}",text)]
        refs += [(m,p) for m in re.findall(r"\\(?:ref|eqref|autoref|pageref|cref|Cref)\{([^}]+)\}",text)]
    names=[x for x,_ in labels]
    dups=sorted({x for x in names if names.count(x)>1})
    if dups:block.append("DUPLICATE_LABELS:"+",".join(dups[:20]))
    labelset=set(names);missingrefs=sorted({x for x,_ in refs if x not in labelset})
    if missingrefs:block.append("MISSING_REFS:"+",".join(missingrefs[:20]))

    src=tsv(repo/"editorial/SOURCE_MIGRATION.tsv")
    srules=[r for r in src if re.fullmatch(r"II/\d{2}",r.get("destination",""))]
    rec=[]
    for r in srules:
        ok=source_exists(repo,r.get("source_file",""))
        rec.append({"source_file":r.get("source_file",""),"source_block_id":r.get("source_block_id",""),
                    "destination":r.get("destination",""),"precedence":r.get("precedence",""),
                    "source_exists":"YES" if ok else "NO","canonical_status":"ROUTED"})
        if not ok:block.append(f"MISSING_SOURCE:{r.get('source_file')}:{r.get('source_block_id')}")
    out=vol/"reconstruction"
    write_tsv(out/"VOLUME02_FULL_PAIRING.tsv",rows,
              ["chapter_code","problems","exercises","hints","solutions","expected_solutions","pairing"])
    write_tsv(out/"VOLUME02_SOURCE_RULE_RECONCILIATION.tsv",rec,
              ["source_file","source_block_id","destination","precedence","source_exists","canonical_status"])
    prov=[]
    for name in ["VOLUME02_I01_I07_DOSSIER_PROVENANCE.tsv","VOLUME02_I08_I12_DOSSIER_PROVENANCE.tsv","VOLUME02_I13_I25_DOSSIER_PROVENANCE.tsv"]:
        p=out/name
        if p.exists():prov+=tsv(p)
        else:block.append(f"MISSING_PROVENANCE:{name}")
    if len(prov)!=300:block.append(f"PROVENANCE_TOTAL:{len(prov)}")
    summary={"status":"PASS" if not block else "FAIL","chapters":25,"build_graph_tex_files":len(graph),
             "problems":total_p,"exercises":total_e,"hints":total_h,"solutions":total_s,
             "source_rules":len(srules),"provenance_rows":len(prov),"duplicate_labels":len(dups),
             "missing_refs":len(missingrefs),"unresolved_count":len(block),"unresolved":block}
    (out/"VOLUME02_FULL_RECONCILIATION.json").write_text(json.dumps(summary,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    md=["# Volume II — Full Reconciliation","",f"**Result:** {summary['status']}","",
        f"- Canonical chapters: **25**",f"- Solved dossiers: **{total_p} / 300**",
        f"- Exercises/hints: **{total_e} / {total_h}**",f"- Total solutions: **{total_s} / 500**",
        f"- Source migration rules reconciled: **{len(srules)}**",f"- Provenance rows: **{len(prov)} / 300**",
        f"- Duplicate labels: **{len(dups)}**",f"- Missing references: **{len(missingrefs)}**","",
        "## Blockers",""]
    md += [f"- {b}" for b in block] if block else ["None."]
    (out/"VOLUME02_FULL_RECONCILIATION.md").write_text("\n".join(md)+"\n",encoding="utf-8")
    print(json.dumps(summary,indent=2,ensure_ascii=False))
    return 0 if not block else 3
if __name__=="__main__":raise SystemExit(main())
