#!/usr/bin/env python3
from __future__ import annotations

import argparse, csv, hashlib, re, shutil
from pathlib import Path

ROMAN={1:"I",2:"II",3:"III",4:"IV",5:"V",6:"VI",7:"VII",8:"VIII"}
ID_KEYS=("canonical_problem_id","problem_id","canonical_id","target_problem_id","reader_problem_id")
SRC_KEYS=("source_file","legacy_source_file","source_path","legacy_source","source")
START_KEYS=("source_start_line","source_line_start","start_line","source_start")
END_KEYS=("source_end_line","source_line_end","end_line","source_end")

def first(row, keys):
    low={k.lower():(v or "").strip() for k,v in row.items()}
    for k in keys:
        if low.get(k): return low[k]
    return ""

def num(s):
    m=re.search(r"\d+", s or "")
    return int(m.group()) if m else None

def digest(p):
    h=hashlib.sha256()
    with p.open("rb") as f:
        for b in iter(lambda:f.read(1<<20), b""): h.update(b)
    return h.hexdigest()

def slug(label):
    return re.sub(r"[^A-Za-z0-9._-]+","_",label).strip("_") or "figure"

def resolve_repo_path(repo, raw):
    if not raw: return None
    p=repo/Path(raw.replace("\\","/"))
    return p.resolve() if p.exists() else None

def load_map(repo, tsv):
    out = {}
    if not tsv.exists():
        return out

    with tsv.open("r", encoding="utf-8-sig", newline="") as f:
        for row in csv.DictReader(f, delimiter="\t"):
            pid = first(row, ID_KEYS)
            if not pid:
                m = re.search(r"\bCP-[IVX]+-\d+\b", "\t".join(row.values()))
                pid = m.group(0) if m else ""

            if not pid:
                continue

            # Prefer authoritative resolved provenance.
            resolved = (row.get("resolved_source_file") or "").strip()

            if resolved:
                src = Path(resolved)
                if not src.is_absolute():
                    src = repo / src
                src = src.resolve()

                if src.is_file():
                    start = num(row.get("resolved_start_line"))
                    end = num(row.get("resolved_end_line"))
                    out.setdefault(pid, []).append((src, start, end))
                    continue

            # Compatibility fallback for older ledgers.
            raw = first(row, SRC_KEYS)
            if not raw:
                continue

            # source_files may contain multiple semicolon-separated paths.
            for raw_src in str(raw).split(";"):
                raw_src = raw_src.strip()
                if not raw_src:
                    continue

                src = resolve_repo_path(repo, raw_src)
                if not src:
                    continue

                start = num(first(row, START_KEYS))
                end = num(first(row, END_KEYS))
                out.setdefault(pid, []).append((src, start, end))

    return out

def problem_blocks(text, roman):
    pat=re.compile(rf"\\begin\{{problem\}}\[(CP-{roman}-\d+)\](.*?)\\end\{{problem\}}",re.S)
    return {m.group(1):(m.start(),m.end(),m.group(0)) for m in pat.finditer(text)}

def refs(block):
    return set(re.findall(r"\\(?:ref|autoref|cref|Cref)\{(fig:[^}}]+)\}",block))

def labels(text):
    return set(re.findall(r"\\label\{(fig:[^}}]+)\}",text))

def sliced(src,start,end):
    s=src.read_text(encoding="utf-8",errors="ignore")
    if start and end:
        ls=s.splitlines(keepends=True)
        return "".join(ls[start-1:min(end,len(ls))]), start
    return s,1

def extract_block(s,label):
    idx=s.find(r"\label{"+label+"}")
    if idx<0: return None,None
    for env in ("figure","figure*","center","tikzpicture"):
        b=s.rfind(r"\begin{"+env+"}",0,idx)
        e=s.find(r"\end{"+env+"}",idx)
        if b>=0 and e>=0:
            e+=len(r"\end{"+env+"}")
            return s[b:e], s.count("\n",0,b)+1
    return None,None

def caption(block):
    m=re.search(r"\\caption\{([^{}]*(?:\{[^{}]*\}[^{}]*)*)\}",block,re.S)
    return m.group(1).strip() if m else ""

def graphic(block):
    m=re.search(r"\\includegraphics(?:\[[^\]]*\])?\{([^}]+)\}",block)
    return m.group(1).strip() if m else ""

def resolve_asset(repo,srcfile,raw):
    rp=Path(raw.replace("\\","/"))
    for base in (srcfile.parent/rp, repo/rp):
        for ext in ("",".png",".pdf",".jpg",".jpeg",".eps"):
            p=Path(str(base)+ext)
            if p.is_file(): return p.resolve(),""
    matches=[]
    for root in (repo/"imports",repo/"chapters"):
        if not root.exists(): continue
        for ext in ("",".png",".pdf",".jpg",".jpeg",".eps"):
            matches += [p for p in root.rglob(rp.name+ext) if p.is_file()]
    if not matches: return None,"asset not found"
    byhash={}
    for p in matches: byhash.setdefault(digest(p),[]).append(p)
    if len(byhash)>1: return None,"ambiguous basename with different hashes"
    return matches[0].resolve(),""

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--repo",type=Path,required=True)
    ap.add_argument("--part",type=int,required=True,choices=range(1,9))
    ap.add_argument("--apply",action="store_true")
    a=ap.parse_args()
    repo=a.repo.resolve(); roman=ROMAN[a.part]; nn=f"{a.part:02d}"
    chapter=repo/"books"/"companion_problems_solutions"/"chapters"/f"part{nn}_volume_{roman.lower()}"/"chapter.tex"
    mt=repo/"books"/"companion_problems_solutions"/"metadata"/f"PART_{roman}_MIGRATION.tsv"
    manifest=repo/"books"/"companion_problems_solutions"/"metadata"/f"PART_{roman}_FIGURES.tsv"
    dest=repo/"books"/"companion_problems_solutions"/"figures"/f"part{nn}"
    if not chapter.exists(): raise SystemExit(f"missing chapter: {chapter}")

    text=chapter.read_text(encoding="utf-8")
    pblocks=problem_blocks(text,roman); existing=labels(text); mapping=load_map(repo,mt)
    rows=[]; inserts=[]

    for pid,(start,end,block) in pblocks.items():
        for lab in sorted(refs(block)):
            if lab in existing:
                rows.append([lab,pid,"","","","","","canonical","","ALREADY_CANONICAL",""])
                continue
            found=None
            for src,sline,eline in mapping.get(pid,[]):
                ss,base=sliced(src,sline,eline)
                fb,rel=extract_block(ss,lab)
                if fb:
                    found=(src,base+(rel or 1)-1,fb); break
            if not found:
                rows.append([lab,pid,"","","","","","unknown","","REVIEW_REQUIRED_NO_SOURCE","label not found in mapped source"])
                continue

            src,line,fb=found; cap=caption(fb); raw=graphic(fb)
            if not cap:
                rows.append([lab,pid,str(src),line,"","","","inline" if not raw else "external","","REVIEW_REQUIRED_NO_CAPTION",""])
                continue

            canon_asset=""; source_asset=""; sh=""; status="MIGRATED"; kind="inline"
            if raw:
                kind="external"
                asset,note=resolve_asset(repo,src,raw)
                if not asset:
                    status="REVIEW_REQUIRED_AMBIGUOUS_ASSET" if "ambiguous" in note else "REVIEW_REQUIRED_NO_ASSET"
                    rows.append([lab,pid,str(src),line,"","","","external",cap,status,note]); continue
                source_asset=str(asset); sh=digest(asset); dest.mkdir(parents=True,exist_ok=True)
                reused=None
                for p in dest.iterdir():
                    if p.is_file() and digest(p)==sh: reused=p; break
                target=reused or (dest/f"{slug(lab)}{asset.suffix.lower()}")
                status="REUSED_BY_HASH" if reused else "MIGRATED"
                canon_asset=str(target)
                fb=fb.replace(raw,f"figures/part{nn}/{target.name}")
                if a.apply and not target.exists(): shutil.copy2(asset,target)

            rows.append([lab,pid,str(src),line,source_asset,canon_asset,sh,kind,cap,status,""])
            if status in ("MIGRATED","REUSED_BY_HASH"):
                local_end=block.rfind(r"\end{problem}")
                inserts.append((start+local_end,"\n\n"+fb.rstrip()+"\n"))

    if a.apply:
        for pos,payload in sorted(inserts,reverse=True):
            text=text[:pos]+payload+text[pos:]
        chapter.write_text("\n".join(x.rstrip() for x in text.splitlines())+"\n",encoding="utf-8",newline="\n")

    manifest.parent.mkdir(parents=True,exist_ok=True)
    fields=["figure_label","canonical_problem_id","source_file","source_line","source_asset","canonical_asset","sha256","kind","caption","status","note"]
    with manifest.open("w",encoding="utf-8",newline="") as f:
        w=csv.writer(f,delimiter="\t"); w.writerow(fields); w.writerows(rows)

    review=[r for r in rows if r[9].startswith("REVIEW_REQUIRED")]
    print(f"Part {roman}: problems={len(pblocks)} figure_rows={len(rows)} review_required={len(review)} mode={'APPLY' if a.apply else 'DRY-RUN'}")
    for r in review: print("REVIEW_REQUIRED",r[1],r[0],r[9],r[10],sep="\t")
    print("Manifest:",manifest)
    return 2 if review else 0

if __name__=="__main__":
    raise SystemExit(main())
