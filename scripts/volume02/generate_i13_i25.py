#!/usr/bin/env python3
from __future__ import annotations
import argparse,re,sys
from pathlib import Path
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE))
from common_volume02 import read_tsv,write_tsv,provenance_rows,PROV_FIELDS,update_status,render
from data_i13_i25 import CHAPTERS,DATA

def main():
    ap=argparse.ArgumentParser();ap.add_argument("--repo",required=True);args=ap.parse_args()
    repo=Path(args.repo).resolve();vol=repo/"books/vol02_real_analysis"
    src=read_tsv(repo/"editorial/SOURCE_MIGRATION.tsv")
    for code,title,slug in CHAPTERS:
        if code not in DATA:continue
        p=vol/"chapters"/slug/"chapter.tex";p.parent.mkdir(parents=True,exist_ok=True)
        p.write_text(render(code,title,DATA[code]),encoding="utf-8")
    prov=provenance_rows(repo,src,DATA)
    write_tsv(vol/"reconstruction/VOLUME02_I13_I25_DOSSIER_PROVENANCE.tsv",prov,PROV_FIELDS)
    update_status(repo,set(DATA))
    readme=vol/"README.md";txt=readme.read_text(encoding="utf-8-sig")
    txt=re.sub(r"(?m)^\*\*Status:\*\*.*$","**Status:** All 25 canonical chapters reconstructed; full-volume reconciliation and freeze pending.",txt,count=1)
    readme.write_text(txt.rstrip()+"\n",encoding="utf-8")
    print("Reconstructed II/13-II/25.")
    print("New solved dossiers:",sum(len(v["dossiers"]) for v in DATA.values()))
    return 0
if __name__=="__main__":raise SystemExit(main())
