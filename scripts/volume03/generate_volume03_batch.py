#!/usr/bin/env python3
from __future__ import annotations
import argparse,importlib.util,re,sys
from pathlib import Path
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE))
from common_volume03 import (
    ALL_CHAPTERS,read_tsv,write_tsv,source_path,render_chapter,render_stub,render_book,
    write_status,provenance_rows,label
)

PROV_FIELDS=["chapter_code","dossier_index","dossier_label","dossier_title","origin","source_file","source_block_id","source_selector","source_topic","note"]
ACCOUNT_FIELDS=["source_file","source_family","source_block_id","block_kind","source_selector","source_topic","destination","precedence","source_exists","disposition","canonical_dossier_label"]
INV_FIELDS=["chapter_code","chapter_title","mapped_rules","missing_sources","canonical_path","state"]

def load_data(path):
    spec=importlib.util.spec_from_file_location("volume03_batch_data",path)
    mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
    return mod.DATA

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--repo",required=True)
    ap.add_argument("--data",required=True)
    ap.add_argument("--start",type=int,required=True)
    ap.add_argument("--end",type=int,required=True)
    args=ap.parse_args()
    repo=Path(args.repo).resolve();vol=repo/"books/vol03_fourier_distributions_pde"
    data=load_data(Path(args.data).resolve())
    expected={f"III/{n:02d}" for n in range(args.start,args.end+1)}
    if set(data)!=expected:
        raise RuntimeError(f"Data codes do not match requested batch: {sorted(set(data)^expected)}")
    status=read_tsv(repo/"editorial/CHAPTER_STATUS.tsv")
    src=read_tsv(repo/"editorial/SOURCE_MIGRATION.tsv")
    vol.mkdir(parents=True,exist_ok=True)
    (vol/"book.tex").write_text(render_book(),encoding="utf-8")

    provenance=[];accounting=[]
    for code,title,slug in ALL_CHAPTERS:
        p=vol/"chapters"/slug/"chapter.tex";p.parent.mkdir(parents=True,exist_ok=True)
        if code in data:
            p.write_text(render_chapter(code,title,data[code]),encoding="utf-8")
            pr,acc=provenance_rows(repo,src,code,data[code])
            provenance+=pr;accounting+=acc
        elif not p.exists():
            p.write_text(render_stub(code,title),encoding="utf-8")
        # Normalize every chapter to one final newline.
        p.write_text(p.read_text(encoding="utf-8-sig").rstrip()+"\n",encoding="utf-8")

    tag=f"III{args.start:02d}_III{args.end:02d}"
    rec=vol/"reconstruction"
    write_tsv(rec/f"VOLUME03_{tag}_DOSSIER_PROVENANCE.tsv",provenance,PROV_FIELDS)
    write_tsv(rec/f"VOLUME03_{tag}_SOURCE_RULE_ACCOUNTING.tsv",accounting,ACCOUNT_FIELDS)

    # Refresh whole-volume inventory from live source map and current files.
    inv=[]
    for code,title,slug in ALL_CHAPTERS:
        p=vol/"chapters"/slug/"chapter.tex"
        rules=[r for r in src if r.get("destination")==code]
        missing=sum(1 for r in rules if r.get("source_file") and not source_path(repo,r.get("source_file","")))
        text=p.read_text(encoding="utf-8-sig")
        inv.append({
            "chapter_code":code,"chapter_title":title,"mapped_rules":len(rules),"missing_sources":missing,
            "canonical_path":p.relative_to(repo).as_posix(),
            "state":"SCAFFOLD" if "Reconstruction scaffold" in text else "DEVELOPED"
        })
    write_tsv(rec/"VOLUME03_SOURCE_INVENTORY.tsv",inv,INV_FIELDS)
    write_status(repo,status,src,set(data))

    readme=vol/"README.md";txt=readme.read_text(encoding="utf-8-sig")
    txt=re.sub(r"(?m)^\*\*Status:\*\*.*$",
               f"**Status:** Canonical reconstruction underway; III/01–III/{args.end:02d} developed.",
               txt,count=1)
    readme.write_text(txt.rstrip()+"\n",encoding="utf-8")
    print(f"Generated Volume III batch III/{args.start:02d}-III/{args.end:02d}.")
    print(f"Canonical solved dossiers added: {len(provenance)}.")
    print(f"Source rules accounted in batch: {len(accounting)}.")
    return 0

if __name__=="__main__":
    raise SystemExit(main())
