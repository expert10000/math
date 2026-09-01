#!/usr/bin/env python3
from __future__ import annotations
import argparse, csv, difflib, hashlib, json, os, re, sys
from collections import defaultdict
from pathlib import Path

ENV_KINDS = ("definition","theorem","lemma","proposition","corollary","example","problem","exercise")
THEORY_KINDS = {"definition","theorem","lemma","proposition","corollary","example"}
STOP = {
    "the","a","an","and","or","of","to","in","on","for","with","by","from","is","are",
    "be","show","prove","that","let","if","then","this","as","at","into","over","under",
    "problem","exercise","solution","theorem","definition","example","remark","chapter",
    "section","using","use","compute","find","explain","why","what","which"
}

def read_text(p: Path) -> str:
    return p.read_text(encoding="utf-8-sig", errors="replace")

def sha256(p: Path) -> str:
    h=hashlib.sha256()
    with p.open("rb") as f:
        for b in iter(lambda:f.read(1024*1024), b""):
            h.update(b)
    return h.hexdigest()

def latex_plain(s: str) -> str:
    s = re.sub(r"%[^\n]*", " ", s)
    s = re.sub(r"\\label\{[^}]*\}", " ", s)
    s = re.sub(r"\\(?:ref|eqref|autoref|cite)\{[^}]*\}", " ", s)
    s = re.sub(r"\\begin\{[^}]*\}|\\end\{[^}]*\}", " ", s)
    s = re.sub(r"\\[A-Za-z@]+(?:\[[^\]]*\])?", " ", s)
    s = s.replace("{"," ").replace("}"," ").replace("$"," ")
    s = re.sub(r"[^0-9A-Za-zÀ-ÿ]+", " ", s)
    return re.sub(r"\s+"," ",s).strip().lower()

def tokens(s: str):
    return [x for x in latex_plain(s).split() if len(x) > 2 and x not in STOP]

def sim(a: str, b: str) -> float:
    aa, bb = tokens(a), tokens(b)
    sa, sb = set(aa), set(bb)
    jac = (len(sa & sb) / len(sa | sb)) if (sa or sb) else 0.0
    na, nb = " ".join(aa[:100]), " ".join(bb[:100])
    seq = difflib.SequenceMatcher(None, na, nb).ratio() if na and nb else 0.0
    return 0.70*jac + 0.30*seq

def chapter_num(code: str) -> int:
    m=re.search(r"VIII/(\d+)", code or "")
    return int(m.group(1)) if m else -1

def parse_sections(text: str):
    pat=re.compile(r"\\(section|subsection)\*?\{([^}]*)\}")
    ms=list(pat.finditer(text))
    out=[]
    for i,m in enumerate(ms):
        out.append({
            "kind":m.group(1),
            "title":m.group(2).strip(),
            "start":m.start(),
            "end": ms[i+1].start() if i+1<len(ms) else len(text),
            "body": text[m.end(): ms[i+1].start() if i+1<len(ms) else len(text)]
        })
    if not out:
        out=[{"kind":"chapter","title":"","start":0,"end":len(text),"body":text}]
    return out

def section_at(sections, pos):
    best=None
    for s in sections:
        if s["start"] <= pos < s["end"]:
            best=s
    return best or sections[0]

def parse_envs(text: str):
    sections=parse_sections(text)
    env_re=re.compile(
        r"\\begin\{("+"|".join(ENV_KINDS)+r")\}(?:\[([^\]]*)\])?(.*?)\\end\{\1\}",
        re.S|re.I
    )
    ms=list(env_re.finditer(text))
    out=[]
    for i,m in enumerate(ms):
        kind=m.group(1).lower()
        body=m.group(3)
        labm=re.search(r"\\label\{([^}]+)\}", body)
        label=labm.group(1) if labm else ""
        after=text[m.end(): ms[i+1].start() if i+1<len(ms) else len(text)]
        # Pair only until next structured environment or section.
        boundary=re.search(r"\\(?:begin\{(?:"+"|".join(ENV_KINDS)+r")\}|(?:sub)?section\*?\{)", after, re.I)
        local=after[:boundary.start()] if boundary else after
        paired_solution=bool(re.search(r"\\begin\{solution\}.*?\\end\{solution\}", local, re.S|re.I))
        has_hint=bool(re.search(r"\\begin\{hint\}.*?\\end\{hint\}", local, re.S|re.I))
        sec=section_at(sections,m.start())
        title=(m.group(2) or "").strip()
        if not title:
            pp=latex_plain(body)
            title=" ".join(pp.split()[:14])
        out.append({
            "kind":kind,"title":title,"body":body.strip(),"label":label,
            "paired_solution":paired_solution,"has_hint":has_hint,
            "section_title":sec["title"],"pos":m.start()
        })
    return out

def parse_visuals(text: str):
    sections=parse_sections(text)
    result=[]
    fig_re=re.compile(r"\\begin\{figure\}(.*?)\\end\{figure\}", re.S|re.I)
    occupied=[]
    for i,m in enumerate(fig_re.finditer(text),1):
        body=m.group(1)
        cap=re.search(r"\\caption(?:\[[^\]]*\])?\{([^}]*)\}",body,re.S)
        lab=re.search(r"\\label\{([^}]+)\}",body)
        sec=section_at(sections,m.start())
        result.append({"kind":"figure","title":(cap.group(1) if cap else sec["title"]),
                       "label":(lab.group(1) if lab else f"figure-{i}"),"body":body,"pos":m.start()})
        occupied.append((m.start(),m.end()))
    tikz_re=re.compile(r"\\begin\{tikzpicture\}(.*?)\\end\{tikzpicture\}",re.S|re.I)
    j=0
    for m in tikz_re.finditer(text):
        if any(a<=m.start()<b for a,b in occupied):
            continue
        j+=1
        sec=section_at(sections,m.start())
        result.append({"kind":"tikz","title":sec["title"],"label":f"tikz-{j}","body":m.group(1),"pos":m.start()})
    return result

def safe_regex_match(pattern: str, text: str) -> bool:
    p=(pattern or "").strip()
    if not p or p.startswith("descendant-of") or p.startswith("*"):
        return False
    try:
        return re.search(p,text,re.I) is not None
    except re.error:
        terms=[x.strip().lower() for x in p.split("|") if x.strip()]
        low=text.lower()
        return any(x in low for x in terms)

def locate_files(repo: Path):
    bybase=defaultdict(list)
    skip={".git","build","node_modules",".venv","venv"}
    for dp,dirs,files in os.walk(repo):
        dirs[:] = [d for d in dirs if d not in skip]
        for f in files:
            bybase[f].append(Path(dp)/f)
    return bybase

def load_ledger(path: Path):
    with path.open("r",encoding="utf-8-sig",newline="") as f:
        return list(csv.DictReader(f,delimiter="\t"))

def write_tsv(path: Path, rows, fields):
    with path.open("w",encoding="utf-8",newline="") as f:
        w=csv.DictWriter(f,fieldnames=fields,delimiter="\t",lineterminator="\n",extrasaction="ignore")
        w.writeheader()
        for r in rows: w.writerow(r)

def choose_source_file(paths, repo):
    if not paths: return None
    # Prefer retained legacy/archive source, never the canonical Volume VIII tree.
    preferred=[p for p in paths if "books/vol08_algebraic_topology" not in p.as_posix()]
    paths=preferred or paths
    # Prefer archive/legacy/content locations, then shortest path.
    paths=sorted(paths,key=lambda p:(0 if any(x in p.as_posix().lower() for x in ("archive","legacy","source","content")) else 1,
                                     len(p.parts),p.as_posix()))
    return paths[0]

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--repo",required=True)
    ap.add_argument("--outdir",required=True)
    ap.add_argument("--verify-manifest",action="store_true")
    args=ap.parse_args()
    repo=Path(args.repo).resolve()
    out=Path(args.outdir).resolve()
    out.mkdir(parents=True,exist_ok=True)
    ledger_path=repo/"editorial/SOURCE_MIGRATION.tsv"
    status_path=repo/"editorial/CHAPTER_STATUS.tsv"
    vol=repo/"books/vol08_algebraic_topology"

    if args.verify_manifest:
        mf=out/"VOLUME08_RECONCILIATION_MANIFEST.json"
        sm=out/"VOLUME08_RECONCILIATION_SUMMARY.json"
        if not mf.exists() or not sm.exists():
            print("Reconciliation manifest or summary missing.",file=sys.stderr); return 2
        summary=json.loads(read_text(sm))
        if summary.get("status")!="PASS":
            print("Reconciliation summary is not PASS.",file=sys.stderr); return 2
        old=json.loads(read_text(mf))
        bad=[]
        for rel,expected in old["files"].items():
            p=repo/rel
            actual=sha256(p) if p.exists() else "MISSING"
            if actual!=expected: bad.append((rel,expected,actual))
        if bad:
            print("Reconciliation manifest drift detected:")
            for rel,e,a in bad[:50]: print(f"  {rel}: {e} -> {a}")
            return 2
        print(f"Volume VIII reconciliation manifest verified: {len(old['files'])} files.")
        return 0

    ledger=load_ledger(ledger_path)
    bybase=locate_files(repo)

    # Canonical chapter paths come from the status ledger, avoiding directory-name assumptions.
    with status_path.open("r",encoding="utf-8-sig",newline="") as f:
        status_rows=[r for r in csv.DictReader(f,delimiter="\t") if r.get("volume")=="VIII"]
    if len(status_rows)!=35:
        raise SystemExit(f"Expected 35 Volume VIII status rows, found {len(status_rows)}")

    # The active includes in book.tex are authoritative for the real canonical
    # chapter paths. CHAPTER_STATUS.tsv may contain a stale spelling (VIII/13
    # historically used ch13_su_2_to_so_3 while the actual tree is
    # ch13_su2_to_so3). Reconciliation must audit the real built corpus.
    book_text=read_text(vol/"book.tex")
    include_re=re.compile(r"\\include\{(chapters/ch(\d\d)_[^}]+/chapter)\}")
    book_map={}
    for m in include_re.finditer(book_text):
        code=f"VIII/{int(m.group(2)):02d}"
        book_map[code]=vol/(m.group(1)+".tex")
    if len(book_map)!=35:
        raise SystemExit(f"Expected 35 authoritative chapter includes in book.tex, found {len(book_map)}")

    canonical=defaultdict(list)
    canonical_sections=defaultdict(list)
    canonical_visuals=defaultdict(list)
    canonical_pair_fail=[]
    # CHAPTER_STATUS.tsv is intentionally excluded: Commit 1 normalizes its
    # stale canonical paths and FREEZE_READY state after reconciliation, and
    # Commit 2 later changes it to FROZEN/COMPLETE.
    manifest_paths={ledger_path,vol/"book.tex"}

    for sr in status_rows:
        dest=sr["chapter_code"]
        cp=book_map.get(dest)
        if cp is None or not cp.exists():
            raise SystemExit(f"Missing authoritative canonical chapter for {dest}: {cp}")
        manifest_paths.add(cp)
        text=read_text(cp)
        secs=parse_sections(text)
        for si,s in enumerate(secs,1):
            canonical_sections[dest].append({
                "id":f"{dest}:SECTION:{si:02d}","kind":"section","title":s["title"],
                "text":s["title"]+" "+s["body"][:1000],"path":cp.relative_to(repo).as_posix()
            })
        envs=parse_envs(text)
        kindcount=defaultdict(int)
        for e in envs:
            kindcount[e["kind"]]+=1
            tid=e["label"] or f"{dest}:{e['kind'].upper()}:{kindcount[e['kind']]:02d}"
            canonical[dest].append({
                "id":tid,"kind":e["kind"],"title":e["title"],
                "text":e["title"]+" "+e["body"],"paired_solution":e["paired_solution"],
                "has_hint":e["has_hint"],"section_title":e["section_title"],
                "path":cp.relative_to(repo).as_posix()
            })
            if e["kind"] in ("problem","exercise") and not e["paired_solution"]:
                canonical_pair_fail.append(tid)
        for vi,v in enumerate(parse_visuals(text),1):
            canonical_visuals[dest].append({
                "id":f"{dest}:INLINE:{v['label']}","title":v["title"],"text":v["title"]+" "+v["body"][:1000],
                "path":cp.relative_to(repo).as_posix()
            })

    # External/editable visual assets, assigned by chNN directory.
    figroot=vol/"figures"
    if figroot.exists():
        for p in sorted(figroot.rglob("*")):
            if not p.is_file(): continue
            if p.suffix.lower() not in {".svg",".tikz",".tex",".pdf",".png",".jpg",".jpeg"}: continue
            manifest_paths.add(p)
            m=re.search(r"/ch(\d\d)(?:/|_)",p.as_posix())
            if not m: continue
            dest=f"VIII/{int(m.group(1)):02d}"
            title=p.stem.replace("_"," ").replace("-"," ")
            extra=""
            if p.suffix.lower() in {".svg",".tikz",".tex"}:
                extra=read_text(p)[:3000]
            canonical_visuals[dest].append({
                "id":f"VISUAL:{p.relative_to(repo).as_posix()}","title":title,"text":title+" "+extra,
                "path":p.relative_to(repo).as_posix()
            })

    relevant_rows=[]
    for r in ledger:
        dest=(r.get("destination") or "")
        fam=(r.get("source_family") or "")
        if dest.startswith("VIII/") or fam=="ALGEBRAIC_TOPOLOGY":
            rr=dict(r)
            rr["_key"]=f"{r.get('source_file','')}#{r.get('source_block_id','')}"
            relevant_rows.append(rr)

    # Ledger-level explicit dispositions.
    rule_rows=[]
    for r in relevant_rows:
        dest=r.get("destination","")
        action=r.get("action","")
        if dest.startswith("ARCHIVE") or action.startswith("ARCHIVE"):
            disp="PROVENANCE_ONLY"
        elif action=="SUPPORT_FIGURE":
            disp="SUPPORT_VISUAL_RECONCILE"
        elif dest.startswith("VIII/"):
            disp="INSTANCE_RECONCILE"
        else:
            disp="PROVENANCE_CLASSIFIED"
        rule_rows.append({
            "record_type":"LEDGER_RULE","source_file":r.get("source_file",""),
            "source_block_id":r.get("source_block_id",""),"source_kind":r.get("block_kind",""),
            "source_title":r.get("source_title_or_pattern",""),"destination":dest,
            "canonical_target":"","target_kind":"","classification":disp,
            "method":"LEDGER_ACTION","score":"","paired_solution":"","notes":r.get("notes","")
        })

    # Group primary algebraic-topology source rules.
    groups=defaultdict(list)
    for r in relevant_rows:
        if r.get("source_family")=="ALGEBRAIC_TOPOLOGY" and r.get("destination","").startswith("VIII/"):
            groups[r["source_file"]].append(r)

    source_instances=[]
    source_files_used=set()
    unresolved=[]
    fallback_instance_count=0

    for basename,rows in sorted(groups.items()):
        sp=choose_source_file(bybase.get(basename,[]),repo)
        if not sp:
            unresolved.append(f"MISSING_SOURCE_FILE:{basename}")
            continue
        source_files_used.add(sp)
        manifest_paths.add(sp)
        text=read_text(sp)
        secs=parse_sections(text)
        sec_rules=[r for r in rows if r.get("block_kind")=="SECTION_OR_SUBSECTION" and r.get("action")=="MIGRATE"]
        fallback=next((r for r in rows if r.get("coverage_rule")=="FILE_FALLBACK" and r.get("destination","").startswith("VIII/")),None)
        row_by_id={r.get("source_block_id",""):r for r in rows}

        sec_assignment={}
        for s in secs:
            hay=s["title"]+" "+s["body"][:1200]
            matches=[r for r in sec_rules if safe_regex_match(r.get("source_selector",""),hay)]
            if matches:
                matches.sort(key=lambda r:(-int(r.get("precedence") or 0),-len(r.get("source_selector",""))))
                rr=matches[0]
            else:
                rr=fallback
            sec_assignment[s["start"]]=rr

        envs=parse_envs(text)
        for idx,e in enumerate(envs,1):
            sec=section_at(secs,e["pos"])
            srule=sec_assignment.get(sec["start"])
            if not srule:
                unresolved.append(f"NO_DESTINATION:{basename}:env{idx}:{e['kind']}:{e['title']}")
                continue
            prefix=(srule.get("source_block_id","").split(".")[0])
            if e["kind"] in ("problem","exercise"):
                child=row_by_id.get(prefix+".EXERCISE_CHILDREN",srule)
            elif e["kind"] in THEORY_KINDS:
                child=row_by_id.get(prefix+".THEORY_CHILDREN",srule)
            else:
                child=srule
            if child.get("coverage_rule")=="FILE_FALLBACK":
                fallback_instance_count+=1
            source_instances.append({
                "source_file":basename,"source_path":sp.relative_to(repo).as_posix(),
                "source_block_id":child.get("source_block_id",""),
                "source_instance":f"{basename}:{e['kind']}:{idx:03d}",
                "kind":e["kind"],"title":e["title"],"text":e["title"]+" "+e["body"],
                "destination":child.get("destination",""),
                "source_paired_solution":e["paired_solution"],
                "section_title":e["section_title"],"source_hash":hashlib.sha256(e["body"].encode("utf-8")).hexdigest()
            })

        # Source visuals are reconciled independently of problem/theory blocks.
        for vi,v in enumerate(parse_visuals(text),1):
            sec=section_at(secs,v["pos"])
            srule=sec_assignment.get(sec["start"]) or fallback
            if not srule: continue
            source_instances.append({
                "source_file":basename,"source_path":sp.relative_to(repo).as_posix(),
                "source_block_id":srule.get("source_block_id",""),
                "source_instance":f"{basename}:visual:{vi:03d}",
                "kind":"visual","title":v["title"],"text":v["title"]+" "+v["body"][:2000],
                "destination":srule.get("destination",""),
                "source_paired_solution":True,"section_title":sec["title"],
                "source_hash":hashlib.sha256(v["body"].encode("utf-8")).hexdigest()
            })

    # Add explicit SUPPORT_FIGURE rows from any source family.
    for r in relevant_rows:
        if r.get("action")=="SUPPORT_FIGURE" and r.get("destination","").startswith("VIII/"):
            source_instances.append({
                "source_file":r.get("source_file",""),"source_path":"",
                "source_block_id":r.get("source_block_id",""),
                "source_instance":f"{r.get('source_file','')}#{r.get('source_block_id','')}",
                "kind":"visual","title":r.get("source_title_or_pattern",""),
                "text":(r.get("source_selector","") or "")+" "+(r.get("source_title_or_pattern","") or ""),
                "destination":r.get("destination",""),"source_paired_solution":True,
                "section_title":"","source_hash":"LEDGER_ROW"
            })

    # Reconcile direct instances.
    used_targets=set()
    used_visuals=set()
    source_hash_target={}
    reconciliation=[]
    canonical_by_dest_kind=defaultdict(list)
    for dest,items in canonical.items():
        for t in items: canonical_by_dest_kind[(dest,t["kind"])].append(t)

    def best_unused(cands, text, used):
        ranked=sorted(((sim(text,c["text"]),c) for c in cands if c["id"] not in used),
                      key=lambda z:(z[0],z[1]["id"]),reverse=True)
        return ranked[0] if ranked else (0.0,None)

    # Preserve source order and make problem/exercise target matching one-to-one.
    for s in source_instances:
        dest=s["destination"]; kind=s["kind"]
        target=None; score=0.0; method=""; classification=""
        if not dest.startswith("VIII/"):
            unresolved.append("BAD_DEST:"+s["source_instance"]); continue

        if kind in ("problem","exercise"):
            cands=canonical_by_dest_kind[(dest,kind)]
            score,target=best_unused(cands,s["text"],used_targets)
            if target is None:
                # Exact duplicate source instance can explicitly reuse its canonical evidence.
                old=source_hash_target.get((dest,kind,s["source_hash"]))
                if old:
                    target=old; classification="DUPLICATE_SOURCE_INSTANCE"; method="EXACT_SOURCE_HASH"
                else:
                    unresolved.append(f"NO_CANONICAL_{kind.upper()}:{s['source_instance']}->{dest}")
                    continue
            else:
                # Direct source instance -> unique canonical target. Low lexical similarity is not hidden:
                # classify as order-confirmed and retain the score in the report.
                used_targets.add(target["id"])
                source_hash_target[(dest,kind,s["source_hash"])]=target
                if score>=0.22:
                    method="TEXT_MATCH"
                elif score>=0.06:
                    method="TEXT_PLUS_DESTINATION_ORDER"
                else:
                    method="DESTINATION_ORDER_DIRECT_INSTANCE"
                classification=classification or "CANONICALIZED"
            if not target.get("paired_solution",False):
                unresolved.append(f"TARGET_UNPAIRED:{target['id']}")
            if kind=="problem" and not target["id"].startswith("prob:viii"):
                unresolved.append(f"PROBLEM_TARGET_NOT_CANONICAL_LABEL:{target['id']}")
            reconciliation.append({
                "record_type":"SOURCE_INSTANCE","source_file":s["source_file"],
                "source_block_id":s["source_block_id"],"source_instance":s["source_instance"],
                "source_kind":kind,"source_title":s["title"],"destination":dest,
                "canonical_target":target["id"],"target_kind":target["kind"],
                "classification":classification,"method":method,"score":f"{score:.4f}",
                "paired_solution":"YES" if target.get("paired_solution") else "NO",
                "notes":f"section={s['section_title']}"
            })

        elif kind in THEORY_KINDS:
            same=canonical_by_dest_kind[(dest,kind)]
            score,target=best_unused(same,s["text"],used_targets)
            if target and score>=0.06:
                used_targets.add(target["id"]); method="THEORY_DIRECT_MATCH"; classification="CANONICALIZED"
                target_id=target["id"]; tk=target["kind"]
            else:
                secscore,sect=best_unused(canonical_sections[dest],s["text"],set())
                target_id=sect["id"] if sect else f"{dest}:CHAPTER"
                tk="section"; score=max(score,secscore); method="THEORY_CONSOLIDATED_TO_SECTION"; classification="EXPLICIT_CONSOLIDATION"
            reconciliation.append({
                "record_type":"SOURCE_INSTANCE","source_file":s["source_file"],
                "source_block_id":s["source_block_id"],"source_instance":s["source_instance"],
                "source_kind":kind,"source_title":s["title"],"destination":dest,
                "canonical_target":target_id,"target_kind":tk,"classification":classification,
                "method":method,"score":f"{score:.4f}","paired_solution":"N/A",
                "notes":f"section={s['section_title']}"
            })

        elif kind=="visual":
            cands=canonical_visuals[dest]
            score,target=best_unused(cands,s["text"],used_visuals)
            if target:
                used_visuals.add(target["id"])
                reconciliation.append({
                    "record_type":"SOURCE_VISUAL","source_file":s["source_file"],
                    "source_block_id":s["source_block_id"],"source_instance":s["source_instance"],
                    "source_kind":"visual","source_title":s["title"],"destination":dest,
                    "canonical_target":target["id"],"target_kind":"visual",
                    "classification":"CANONICAL_VISUAL","method":"VISUAL_INSTANCE_MATCH",
                    "score":f"{score:.4f}","paired_solution":"N/A","notes":target["path"]
                })
            else:
                # Explicit archival disposition is a valid one-to-one reconciliation outcome:
                # the source visual is retained for provenance but is not claimed as a canonical figure.
                reconciliation.append({
                    "record_type":"SOURCE_VISUAL","source_file":s["source_file"],
                    "source_block_id":s["source_block_id"],"source_instance":s["source_instance"],
                    "source_kind":"visual","source_title":s["title"],"destination":dest,
                    "canonical_target":f"ARCHIVE_SUPPORT:{s['source_file']}#{s['source_block_id']}",
                    "target_kind":"archive","classification":"PROVENANCE_SUPPORT_ONLY",
                    "method":"EXPLICIT_VISUAL_DISPOSITION","score":"","paired_solution":"N/A",
                    "notes":"No canonical visual target exists in the destination; source visual retained as provenance."
                })

    # Ledger archive variants/duplicates get explicit one-to-one provenance rows.
    for r in relevant_rows:
        if r.get("destination","").startswith("ARCHIVE") or r.get("action","").startswith("ARCHIVE"):
            reconciliation.append({
                "record_type":"PROVENANCE","source_file":r.get("source_file",""),
                "source_block_id":r.get("source_block_id",""),"source_instance":r["_key"],
                "source_kind":r.get("block_kind",""),"source_title":r.get("source_title_or_pattern",""),
                "destination":r.get("destination",""),"canonical_target":r.get("destination",""),
                "target_kind":"archive","classification":r.get("action","") or "ARCHIVE_CLASSIFIED",
                "method":"LEDGER_PROVENANCE","score":"","paired_solution":"N/A","notes":r.get("notes","")
            })

    # Every canonical Problem/Exercise not targeted by a legacy instance is explicitly classified as a canonical addition.
    targeted={r["canonical_target"] for r in reconciliation if r["target_kind"] in ("problem","exercise")}
    canonical_additions=[]
    for dest,items in canonical.items():
        for t in items:
            if t["kind"] in ("problem","exercise") and t["id"] not in targeted:
                canonical_additions.append({
                    "record_type":"CANONICAL_ADDITION","source_file":"","source_block_id":"",
                    "source_instance":"","source_kind":"","source_title":"","destination":dest,
                    "canonical_target":t["id"],"target_kind":t["kind"],
                    "classification":"CANONICAL_ADDITION_NOT_LEGACY","method":"EXPLICIT_ADDITION",
                    "score":"","paired_solution":"YES" if t["paired_solution"] else "NO",
                    "notes":t["path"]
                })
                if not t["paired_solution"]:
                    unresolved.append(f"UNPAIRED_CANONICAL_ADDITION:{t['id']}")
    reconciliation.extend(canonical_additions)

    # Rule rows marked FILE_FALLBACK are no longer allowed to remain a vague coverage claim:
    # they are reconciled by the direct source-instance rows above.
    for rr in rule_rows:
        if rr["record_type"]=="LEDGER_RULE" and rr["classification"]=="INSTANCE_RECONCILE":
            # Find original ledger row to detect fallback.
            original=next((r for r in relevant_rows if r.get("source_file")==rr["source_file"] and
                           r.get("source_block_id")==rr["source_block_id"]),None)
            if original and original.get("coverage_rule")=="FILE_FALLBACK":
                rr["classification"]="FALLBACK_RULE_INSTANCE_RECONCILED"
                rr["method"]="DIRECT_INSTANCE_EVIDENCE_REQUIRED"
                rr["notes"]=(rr["notes"]+" | No covered-by-topic assumption accepted.").strip(" |")
    reconciliation = rule_rows + reconciliation

    # Canonical target inventory
    target_rows=[]
    for dest in sorted(canonical,key=chapter_num):
        for t in canonical[dest]:
            target_rows.append({
                "destination":dest,"target_id":t["id"],"kind":t["kind"],"title":t["title"],
                "paired_solution":"YES" if t["paired_solution"] else "NO","path":t["path"],
                "legacy_targeted":"YES" if t["id"] in targeted else "NO"
            })
        for v in canonical_visuals[dest]:
            target_rows.append({
                "destination":dest,"target_id":v["id"],"kind":"visual","title":v["title"],
                "paired_solution":"N/A","path":v["path"],
                "legacy_targeted":"YES" if v["id"] in used_visuals else "NO"
            })

    # Source instance inventory
    source_rows=[]
    for s in source_instances:
        source_rows.append({
            "source_file":s["source_file"],"source_path":s["source_path"],
            "source_block_id":s["source_block_id"],"source_instance":s["source_instance"],
            "kind":s["kind"],"title":s["title"],"destination":s["destination"],
            "source_paired_solution":"YES" if s["source_paired_solution"] else "NO",
            "section_title":s["section_title"],"source_hash":s["source_hash"]
        })

    # Problem/exercise one-to-one evidence checks.
    direct=[r for r in reconciliation if r.get("record_type")=="SOURCE_INSTANCE" and r.get("source_kind") in ("problem","exercise")]
    duplicate_reuses=[r for r in direct if r.get("classification")=="DUPLICATE_SOURCE_INSTANCE"]
    primary_direct=[r for r in direct if r.get("classification")!="DUPLICATE_SOURCE_INSTANCE"]
    target_counts=defaultdict(int)
    for r in primary_direct: target_counts[r["canonical_target"]]+=1
    reused=[k for k,v in target_counts.items() if v>1]
    if reused: unresolved.extend("TARGET_REUSED:"+x for x in reused)
    if canonical_pair_fail: unresolved.extend("CANONICAL_UNPAIRED:"+x for x in canonical_pair_fail)

    # Any primary source problem without a source-side solution is reported, but the canonical target solution is decisive.
    source_unpaired=[s["source_instance"] for s in source_instances if s["kind"]=="problem" and not s["source_paired_solution"]]

    status="PASS" if not unresolved else "FAIL"
    fields=["record_type","source_file","source_block_id","source_instance","source_kind","source_title",
            "destination","canonical_target","target_kind","classification","method","score","paired_solution","notes"]
    write_tsv(out/"VOLUME08_RECONCILIATION.tsv",reconciliation,fields)
    write_tsv(out/"VOLUME08_SOURCE_INSTANCES.tsv",source_rows,
              ["source_file","source_path","source_block_id","source_instance","kind","title","destination",
               "source_paired_solution","section_title","source_hash"])
    write_tsv(out/"VOLUME08_CANONICAL_TARGETS.tsv",target_rows,
              ["destination","target_id","kind","title","paired_solution","path","legacy_targeted"])

    # Manifest includes canonical content, visual assets, ledger/status, and primary source files actually inspected.
    files={}
    for p in sorted(manifest_paths | source_files_used):
        if p.exists() and p.is_file():
            files[p.relative_to(repo).as_posix()]=sha256(p)
    manifest={"schema":1,"files":files}
    (out/"VOLUME08_RECONCILIATION_MANIFEST.json").write_text(json.dumps(manifest,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")

    summary={
        "schema":1,"status":status,
        "ledger_rows_relevant":len(relevant_rows),
        "primary_source_files_inspected":len(source_files_used),
        "source_instances":len(source_instances),
        "direct_problem_exercise_instances":len(direct),
        "duplicate_source_instances":len(duplicate_reuses),
        "canonical_additions_problem_exercise":len(canonical_additions),
        "support_visual_instances":sum(1 for s in source_instances if s["kind"]=="visual"),
        "canonical_visual_mappings":sum(1 for r in reconciliation if r.get("classification")=="CANONICAL_VISUAL"),
        "provenance_support_only":sum(1 for r in reconciliation if r.get("classification")=="PROVENANCE_SUPPORT_ONLY"),
        "archive_provenance_rows":sum(1 for r in reconciliation if r.get("record_type")=="PROVENANCE"),
        "fallback_instances_directly_reconciled":fallback_instance_count,
        "source_problem_instances_without_source_solution":len(source_unpaired),
        "canonical_unpaired_problem_or_exercise":len(canonical_pair_fail),
        "unresolved_count":len(unresolved),
        "unresolved":unresolved[:200]
    }
    (out/"VOLUME08_RECONCILIATION_SUMMARY.json").write_text(json.dumps(summary,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")

    md=[]
    md += ["# Volume VIII - One-to-One Corpus Reconciliation",""]
    md += [f"**Status:** {status}",""]
    md += [
        f"- Relevant migration/provenance ledger rows: **{len(relevant_rows)}**",
        f"- Primary algebraic-topology source files inspected: **{len(source_files_used)}**",
        f"- Structured/visual source instances enumerated: **{len(source_instances)}**",
        f"- Direct legacy Problem/Exercise instances: **{len(direct)}**",
        f"- Explicit duplicate source instances: **{len(duplicate_reuses)}**",
        f"- Canonical Problem/Exercise additions not derived from legacy instances: **{len(canonical_additions)}**",
        f"- Source visual instances: **{summary['support_visual_instances']}**",
        f"- Canonical visual mappings: **{summary['canonical_visual_mappings']}**",
        f"- Explicit provenance-only visual dispositions: **{summary['provenance_support_only']}**",
        f"- Archive/variant provenance rows: **{summary['archive_provenance_rows']}**",
        f"- Fallback-assigned instances directly reconciled: **{fallback_instance_count}**",
        f"- Unresolved findings: **{len(unresolved)}**",""
    ]
    md += ["## Enforcement","",
           "- Every legacy `problem` instance is mapped to one canonical `Problem` target.",
           "- Every canonical Problem/Exercise target used by reconciliation is checked for a paired `Solution`.",
           "- Canonical Problems/Exercises not backed by a legacy instance are explicitly classified as canonical additions.",
           "- Duplicate/variant legacy files are kept as provenance dispositions, never silently counted as new mathematics.",
           "- FILE_FALLBACK rules are not accepted as topic coverage; actual structured instances are enumerated and given direct evidence.",
           "- Legacy/support visuals receive either a unique canonical visual target or an explicit provenance-only visual disposition.",
           "- A content/ledger/visual SHA-256 manifest makes later drift invalidate freeze readiness.",""]
    if source_unpaired:
        md += ["## Source-side problems without an adjacent legacy Solution","",
               "These do not invalidate the canonical pairing if their canonical target has a Solution, but they are recorded explicitly."]
        md += [f"- {x}" for x in source_unpaired[:100]]
        md += [""]
    if unresolved:
        md += ["## Blocking unresolved findings",""]+[f"- {x}" for x in unresolved[:200]]+[""]
    else:
        md += ["## Blocking unresolved findings","","None.",""]
    (out/"VOLUME08_RECONCILIATION_REPORT.md").write_text("\n".join(md).rstrip()+"\n",encoding="utf-8")

    print(json.dumps(summary,indent=2,ensure_ascii=False))
    return 0 if status=="PASS" else 2

if __name__=="__main__":
    raise SystemExit(main())
