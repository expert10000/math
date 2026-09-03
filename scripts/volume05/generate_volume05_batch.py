#!/usr/bin/env python3
from __future__ import annotations
import argparse,importlib.util,re,sys
from pathlib import Path
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE))
from common_volume05 import *

def load_data(path):
    spec=importlib.util.spec_from_file_location("volume05_data",path)
    mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
    return mod.DATA

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--repo",required=True)
    ap.add_argument("--data",required=True)
    ap.add_argument("--start",type=int,required=True)
    ap.add_argument("--end",type=int,required=True)
    args=ap.parse_args()

    repo=Path(args.repo).resolve()
    vol=repo/"books/vol05_commutative_algebra"
    data=load_data(Path(args.data).resolve())
    expected={f"V/{n:02d}" for n in range(args.start,args.end+1)}
    if set(data)!=expected:
        raise RuntimeError(f"Data codes do not match batch: {sorted(set(data)^expected)}")

    status=read_tsv(repo/"editorial/CHAPTER_STATUS.tsv")
    src=read_tsv(repo/"editorial/SOURCE_MIGRATION.tsv")
    canonical_paths={}
    for row in status:
        code=row.get("chapter_code","")
        if re.fullmatch(r"V/\d{2}",code):
            canonical_paths[code]=row.get("canonical_path","")
    missing=[code for code,_,_ in ALL_CHAPTERS if not canonical_paths.get(code)]
    if missing:
        raise RuntimeError(f"Missing Volume V canonical paths in CHAPTER_STATUS.tsv: {missing}")

    vol.mkdir(parents=True,exist_ok=True)
    (vol/"book.tex").write_text(render_book(canonical_paths),encoding="utf-8")

    prov=[];acc=[]
    for code,title,slug in ALL_CHAPTERS:
        p=repo/canonical_paths[code]
        p.parent.mkdir(parents=True,exist_ok=True)
        if code in data:
            p.write_text(render_chapter(code,title,data[code]),encoding="utf-8")
            pr,ac=provenance(repo,src,code,data[code])
            prov+=pr;acc+=ac
        elif not p.exists():
            p.write_text(render_stub(code,title),encoding="utf-8")
        p.write_text(p.read_text(encoding="utf-8-sig").rstrip()+"\n",encoding="utf-8")

    tag=f"V{args.start:02d}_V{args.end:02d}"
    rec=vol/"reconstruction"
    write_tsv(rec/f"VOLUME05_{tag}_DOSSIER_PROVENANCE.tsv",prov,PROV_FIELDS)
    write_tsv(rec/f"VOLUME05_{tag}_SOURCE_RULE_ACCOUNTING.tsv",acc,ACCOUNT_FIELDS)

    inv=[]
    for code,title,slug in ALL_CHAPTERS:
        p=repo/canonical_paths[code]
        rules=[r for r in src if r.get("destination")==code]
        missing_sources=sum(1 for r in rules if r.get("source_file") and not source_path(repo,r.get("source_file","")))
        inv.append({
            "chapter_code":code,
            "chapter_title":title,
            "mapped_rules":len(rules),
            "missing_sources":missing_sources,
            "canonical_path":p.relative_to(repo).as_posix(),
            "state":"SCAFFOLD" if "Reconstruction scaffold" in p.read_text(encoding="utf-8-sig") else "DEVELOPED"
        })
    write_tsv(rec/"VOLUME05_SOURCE_INVENTORY.tsv",inv,INV_FIELDS)
    write_status(repo,status,src,set(data))

    readme=vol/"README.md"
    text=readme.read_text(encoding="utf-8-sig")
    text=re.sub(
        r"(?m)^\*\*Status:\*\*.*$",
        f"**Status:** Canonical reconstruction underway; V/01–V/{args.end:02d} developed.",
        text,count=1
    )
    readme.write_text(text.rstrip()+"\n",encoding="utf-8")
    print(f"Generated V/{args.start:02d}-V/{args.end:02d}; dossiers={len(prov)}; source rules={len(acc)}")
    return 0

if __name__=="__main__":
    raise SystemExit(main())
