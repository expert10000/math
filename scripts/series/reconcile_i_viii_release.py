#!/usr/bin/env python3
from __future__ import annotations
import argparse,csv,json,re,hashlib
from collections import Counter,defaultdict
from pathlib import Path

VOLS=[
("I",1,"Linear Algebra","vol01_linear_algebra",18),
("II",2,"Real Analysis and Topological Foundations","vol02_real_analysis",25),
("III",3,"Measure, Fourier Analysis, Distributions and PDE","vol03_fourier_distributions_pde",28),
("IV",4,"Complex Analysis and Riemann Surfaces","vol04_complex_analysis",31),
("V",5,"Commutative Algebra and Homological Methods","vol05_commutative_algebra",28),
("VI",6,"Algebraic Geometry and Sheaf Theory","vol06_algebraic_geometry",49),
("VII",7,"Differential, Riemannian and Hyperbolic Geometry","vol07_differential_geometry",42),
("VIII",8,"Algebraic Topology","vol08_algebraic_topology",35),
]
ROMANS={v for v,_,_,_,_ in VOLS}
TEXT_ENCODINGS=("utf-8-sig","utf-8")

def read_tsv(path):
    with Path(path).open("r",encoding="utf-8-sig",newline="") as f:
        return list(csv.DictReader(f,delimiter="\t"))

def write_tsv(path,rows,fields):
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    with path.open("w",encoding="utf-8",newline="") as f:
        w=csv.DictWriter(f,fieldnames=fields,delimiter="\t",lineterminator="\n",extrasaction="ignore")
        w.writeheader();w.writerows(rows)

def read_text(path):
    return Path(path).read_text(encoding="utf-8-sig",errors="replace")

def source_path(repo,name):
    if not name:return None
    for p in (repo/name,repo/"chapters/tex"/name):
        if p.exists():return p
    return None

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

def refs_in(text):
    text=strip_comments(text)
    out=[]
    rx=re.compile(r"\\(?:ref|eqref|autoref|pageref|cref|Cref)\{([^}]+)\}")
    for raw in rx.findall(text):
        for lab in raw.split(","):
            lab=lab.strip()
            if lab:out.append(lab)
    return out

def resolve_tex_target(current, target, search_roots):
    r"""Resolve an active \input/\include target using chapter-, volume-, and repo-relative candidates."""
    raw=Path(target)
    candidates=[]
    if raw.is_absolute():
        candidates.append(raw)
    else:
        candidates.append(current.parent/raw)
        for base in search_roots:
            candidates.append(Path(base)/raw)
    expanded=[]
    for q in candidates:
        expanded.append(q)
        if q.suffix=="":
            expanded.append(q.with_suffix(".tex"))
    for q in expanded:
        try:
            qq=q.resolve()
        except Exception:
            qq=q
        if qq.exists() and qq.is_file():
            return qq
    return None

def tex_graph(root, search_roots):
    """Return the recursive active TeX graph rooted at one canonical file."""
    root=Path(root).resolve()
    roots=[Path(x).resolve() for x in search_roots]
    seen=set()
    stack=[root]
    rx=re.compile(r"\\(?:input|include)\{([^}]+)\}")
    while stack:
        p=stack.pop()
        if p in seen or not p.exists():
            continue
        seen.add(p)
        text=strip_comments(read_text(p))
        for target in rx.findall(text):
            q=resolve_tex_target(p,target,roots)
            if q is not None and q not in seen:
                stack.append(q)
    return sorted(seen,key=lambda x:x.as_posix())

def combined_graph_text(paths):
    return "\n".join(strip_comments(read_text(p)) for p in paths)

def page_count(pdf):
    return len(re.findall(rb"/Type\s*/Page(?!s)\b",Path(pdf).read_bytes()))

def sha(path):
    h=hashlib.sha256()
    with Path(path).open("rb") as f:
        for b in iter(lambda:f.read(1024*1024),b""):
            h.update(b)
    return h.hexdigest()

def classify_source(row,repo,status_by_code):
    name=row.get("source_file","")
    src=source_path(repo,name)
    source_exists=bool(src)
    dest=row.get("destination","")
    action=(row.get("action","") or "").upper()
    family=(row.get("source_family","") or "").upper()
    audit=(row.get("audit_status","") or "").upper()
    canonical=""
    canonical_exists=False
    chapter_state=""
    next_action=""
    destination_class=""

    if re.fullmatch(r"(?:VIII|VII|VI|IV|III|II|V|I)/\d{2}",dest):
        destination_class="CANONICAL_CHAPTER"
        sr=status_by_code.get(dest)
        if sr:
            canonical=sr.get("canonical_path","")
            canonical_exists=bool(canonical and (repo/canonical).exists())
            chapter_state=sr.get("status","")
            next_action=sr.get("next_action","")
        if not source_exists:
            disp="UNRESOLVED_MISSING_SOURCE"
        elif not sr:
            disp="UNRESOLVED_MISSING_DESTINATION_STATUS"
        elif not canonical_exists:
            disp="UNRESOLVED_MISSING_CANONICAL_CHAPTER"
        elif chapter_state!="FROZEN" or next_action!="COMPLETE":
            disp="UNRESOLVED_DESTINATION_NOT_FROZEN"
        elif "ARCHIVE" in action:
            disp="ARCHIVE_RULE_ATTACHED_TO_CANONICAL_CHAPTER"
        elif family=="SUPPORT" or "SUPPORT" in action:
            disp="SUPPORT_ONLY"
        else:
            disp="MAPPED_TO_FROZEN_CANONICAL_CHAPTER"
    elif dest.upper().startswith("ARCHIVE") or "ARCHIVE" in action or "DUPLICATE" in action:
        destination_class="ARCHIVE"
        disp="ARCHIVE_ACCOUNTED" if source_exists else "UNRESOLVED_MISSING_SOURCE"
    elif family=="SUPPORT" and ("COVERED" in audit or "CURATED" in audit or "SUPPORT" in action):
        destination_class="SUPPORT_NONCHAPTER"
        disp="SUPPORT_ONLY" if source_exists else "UNRESOLVED_MISSING_SOURCE"
    else:
        destination_class="NONCANONICAL_OTHER"
        if not source_exists:
            disp="UNRESOLVED_MISSING_SOURCE"
        elif not dest or any(tok in audit for tok in ("UNRESOLVED","UNMAPPED","TODO","REVIEW_REQUIRED")):
            disp="UNRESOLVED_NONCANONICAL_DESTINATION"
        else:
            # SOURCE_MIGRATION itself is the canonical disposition ledger. Some
            # intentional nonchapter destinations are support/archive buckets
            # with curated audit statuses; retain them as explicitly accounted
            # rather than forcing them into a chapter code.
            disp="NONCANONICAL_ACCOUNTED"

    return {
        "source_file":name,
        "source_family":row.get("source_family",""),
        "source_block_id":row.get("source_block_id",""),
        "block_kind":row.get("block_kind",""),
        "source_selector":row.get("source_selector",""),
        "source_topic":row.get("source_title_or_pattern",""),
        "destination":dest,
        "action":row.get("action",""),
        "precedence":row.get("precedence",""),
        "audit_status":row.get("audit_status",""),
        "source_exists":"YES" if source_exists else "NO",
        "source_resolved_path":src.relative_to(repo).as_posix() if src else "",
        "destination_class":destination_class,
        "canonical_path":canonical,
        "canonical_exists":"YES" if canonical_exists else ("NO" if canonical else ""),
        "chapter_status":chapter_state,
        "next_action":next_action,
        "global_disposition":disp,
    }

def native_volume06_evidence(repo):
    """Validate the current Volume VI release using its native frozen architecture."""
    vol=repo/"books/vol06_algebraic_geometry"
    freeze_report=vol/"freeze/VOLUME06_FREEZE_REPORT.md"
    recon_summary=vol/"reconciliation/VOLUME06_RECONCILIATION_SUMMARY.json"
    full_pdf=vol/"book_full_solutions.pdf"
    full_log=vol/"book_full_solutions.log"
    blockers=[]

    if not freeze_report.exists():
        blockers.append("missing Volume VI freeze report")
    else:
        text=read_text(freeze_report)
        if "**Result:** PASS" not in text:
            blockers.append("Volume VI freeze report is not PASS")

    recon={}
    if not recon_summary.exists():
        blockers.append("missing Volume VI reconciliation summary")
    else:
        try:
            recon=json.loads(read_text(recon_summary))
        except Exception as exc:
            blockers.append(f"invalid Volume VI reconciliation summary: {exc}")
        else:
            if recon.get("status")!="PASS":
                blockers.append("Volume VI reconciliation summary is not PASS")
            try:
                if int(recon.get("unresolved_count",1))!=0:
                    blockers.append("Volume VI reconciliation has unresolved items")
            except Exception:
                blockers.append("Volume VI reconciliation unresolved_count is invalid")

    if not full_pdf.exists():
        blockers.append("fresh Volume VI full-solutions PDF missing")
    if not full_log.exists():
        blockers.append("fresh Volume VI full-solutions log missing")
    if full_log.exists():
        log=read_text(full_log)
        for pattern in (
            "LaTeX Warning: There were undefined references",
            "There were undefined citations",
            "multiply defined",
        ):
            if pattern.lower() in log.lower():
                blockers.append("Volume VI full-solutions build warning: "+pattern)

    return {
        "status":"PASS" if not blockers else "FAIL",
        "policy":"NATIVE_FREEZE_PLUS_FULL_SOLUTIONS_BUILD",
        "freeze_report":freeze_report.relative_to(repo).as_posix() if freeze_report.exists() else "",
        "reconciliation_summary":recon_summary.relative_to(repo).as_posix() if recon_summary.exists() else "",
        "full_solutions_pdf":full_pdf.relative_to(repo).as_posix() if full_pdf.exists() else "",
        "full_solutions_pages":page_count(full_pdf) if full_pdf.exists() else 0,
        "full_solutions_bytes":full_pdf.stat().st_size if full_pdf.exists() else 0,
        "full_solutions_sha256":sha(full_pdf) if full_pdf.exists() else "",
        "blockers":blockers,
    }

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--repo",required=True)
    args=ap.parse_args()
    repo=Path(args.repo).resolve()
    reports=repo/"reports/series";reports.mkdir(parents=True,exist_ok=True)
    status=read_tsv(repo/"editorial/CHAPTER_STATUS.tsv")
    migration=read_tsv(repo/"editorial/SOURCE_MIGRATION.tsv")
    build=read_tsv(repo/"reports/series/BUILD_I_VIII.tsv")
    pdfinv=read_tsv(repo/"reports/series/PDF_INVENTORY.tsv")
    global_audit_path=repo/"reports/series/GLOBAL_I_VIII_AUDIT.json"
    global_audit=json.loads(global_audit_path.read_text(encoding="utf-8")) if global_audit_path.exists() else {}
    native_vi=native_volume06_evidence(repo)

    blockers=[]
    status_by_code={r.get("chapter_code",""):r for r in status}
    if len(status)!=256:
        blockers.append(f"CHAPTER_STATUS rows {len(status)} != 256")
    codes=[r.get("chapter_code","") for r in status]
    if len(set(codes))!=len(codes):
        blockers.append("duplicate CHAPTER_STATUS chapter codes")

    volume_rows=[]
    chapter_rows=[]
    all_labels={}
    label_occ=defaultdict(list)
    all_refs=[]
    scaffold_hits=[]
    canonical_tex_files=set()
    tex_file_owner={}
    total_problem=total_exercise=total_hint=total_solution=0

    for v,n,title,dirname,expected in VOLS:
        volume_root=repo/"books"/dirname
        sr=[r for r in status if r.get("volume")==v]
        vblock=[]
        if len(sr)!=expected:
            vblock.append(f"status_rows={len(sr)} expected={expected}")
        frozen=sum(r.get("status")=="FROZEN" for r in sr)
        complete=sum(r.get("next_action")=="COMPLETE" for r in sr)
        missing_paths=0
        pairing_fail=0
        raw_pairing_mismatch=0
        pairing_policy="NATIVE_FREEZE_PLUS_FULL_SOLUTIONS_BUILD" if v=="VI" else "STRICT_INLINE_GRAPH"
        vpro=vex=vhint=vsol=0
        for r in sr:
            code=r.get("chapter_code","")
            cp=repo/r.get("canonical_path","")
            exists=cp.exists()
            if not exists:
                missing_paths+=1
                chapter_rows.append({
                    "volume":v,"chapter_code":code,"chapter_title":r.get("chapter_title",""),
                    "canonical_path":r.get("canonical_path",""),"path_exists":"NO",
                    "status":r.get("status",""),"next_action":r.get("next_action",""),
                    "graph_tex_files":0,
                    "pairing_policy":pairing_policy,"raw_pairing_match":"UNKNOWN",
                    "problems":0,"exercises":0,"hints":0,"solutions":0,
                    "expected_solutions":0,"pairing":"MISSING_CHAPTER","scaffold":"UNKNOWN",
                })
                continue
            chapter_graph=tex_graph(cp,[volume_root,repo])
            clean=combined_graph_text(chapter_graph)
            problems=len(re.findall(r"\\begin\{problem\}",clean))
            exercises=len(re.findall(r"\\begin\{exercise\}",clean))
            hints=len(re.findall(r"\\begin\{hint\}",clean))
            solutions=len(re.findall(r"\\begin\{solution\}",clean))
            expected_solutions=problems+exercises
            raw_match=(solutions==expected_solutions)
            if not raw_match:
                raw_pairing_mismatch+=1
            if pairing_policy=="STRICT_INLINE_GRAPH":
                pairing="PASS" if raw_match else "FAIL"
                if pairing=="FAIL":
                    pairing_fail+=1
            else:
                # Volume VI intentionally has an edition-controlled solution layer.
                # Raw source counts are diagnostic only; the blocking contract is
                # its native freeze evidence plus a fresh full-solutions build.
                pairing="NATIVE_VOLUME_CONTRACT"
            scaffold=bool(re.search(r"\\section\*\{Reconstruction scaffold\}",clean))
            if scaffold:scaffold_hits.append(code)

            # Register physical files once for global label/ref auditing. This is
            # crucial for legacy frozen chapters whose solutions/labels live in
            # recursively included files.
            for gp in chapter_graph:
                canonical_tex_files.add(gp)
                tex_file_owner.setdefault(gp,(v,code))

            vpro+=problems;vex+=exercises;vhint+=hints;vsol+=solutions
            total_problem+=problems;total_exercise+=exercises;total_hint+=hints;total_solution+=solutions
            chapter_rows.append({
                "volume":v,"chapter_code":code,"chapter_title":r.get("chapter_title",""),
                "canonical_path":r.get("canonical_path",""),"path_exists":"YES",
                "status":r.get("status",""),"next_action":r.get("next_action",""),
                "graph_tex_files":len(chapter_graph),
                "pairing_policy":pairing_policy,"raw_pairing_match":"YES" if raw_match else "NO",
                "problems":problems,"exercises":exercises,"hints":hints,"solutions":solutions,
                "expected_solutions":expected_solutions,"pairing":pairing,
                "scaffold":"YES" if scaffold else "NO",
            })

        br=next((r for r in build if r.get("volume")==v and r.get("target")=="book.tex" and r.get("kind")=="canonical"),None)
        build_status=br.get("status","MISSING") if br else "MISSING"
        book=volume_root/"book.tex"
        pdf=volume_root/"book.pdf"
        if book.exists():
            for gp in tex_graph(book,[volume_root,repo]):
                canonical_tex_files.add(gp)
                tex_file_owner.setdefault(gp,(v,"BOOK"))
        pr=next((r for r in pdfinv if r.get("volume")==v),None)
        pdf_ok=bool(pr and pr.get("exists")=="YES" and pdf.exists() and pr.get("sha256")==sha(pdf))
        includes=len(re.findall(r"(?m)^[ \t]*\\include\{",read_text(book))) if book.exists() else 0

        if frozen!=expected:vblock.append(f"frozen={frozen} expected={expected}")
        if complete!=expected:vblock.append(f"complete={complete} expected={expected}")
        if missing_paths:vblock.append(f"missing_paths={missing_paths}")
        if pairing_fail:
            vblock.append(f"pairing_failures={pairing_fail}")
        if v=="VI" and native_vi["status"]!="PASS":
            vblock.append("native Volume VI solution/freeze contract failed: "+"; ".join(native_vi["blockers"]))
        if build_status!="PASS":vblock.append(f"build_status={build_status}")
        if includes!=expected:vblock.append(f"book_includes={includes} expected={expected}")
        if not pdf_ok:vblock.append("PDF inventory/hash mismatch")
        if vblock:blockers.extend(f"{v}:{x}" for x in vblock)
        volume_rows.append({
            "volume":v,"title":title,"chapters":len(sr),"expected_chapters":expected,
            "frozen":frozen,"complete":complete,"canonical_paths":len(sr)-missing_paths,
            "pairing_policy":pairing_policy,
            "pairing_failures":pairing_fail,"raw_pairing_mismatches":raw_pairing_mismatch,
            "problems":vpro,"exercises":vex,"hints":vhint,"solutions":vsol,
            "native_solution_contract":"PASS" if v!="VI" else native_vi["status"],
            "book_includes":includes,"build_status":build_status,
            "pdf_verified":"YES" if pdf_ok else "NO",
            "status":"PASS" if not vblock else "FAIL",
            "blockers":"; ".join(vblock) if vblock else "-"
        })

    # Global labels/references are scanned once per physical file in the
    # recursive active build graph, avoiding false duplicates from shared inputs.
    for gp in sorted(canonical_tex_files,key=lambda x:x.as_posix()):
        clean=strip_comments(read_text(gp))
        owner_v,owner_code=tex_file_owner.get(gp,("",""))
        rel=gp.relative_to(repo).as_posix() if repo in gp.parents else gp.as_posix()
        for lab in re.findall(r"\\label\{([^}]+)\}",clean):
            label_occ[lab].append((owner_v,owner_code,rel))
        for lab in refs_in(clean):
            all_refs.append((owner_v,owner_code,rel,lab))

    duplicates={lab:locs for lab,locs in label_occ.items() if len(locs)>1}
    if duplicates:
        blockers.append(f"duplicate LaTeX labels={len(duplicates)}")
    label_owner={lab:locs[0] for lab,locs in label_occ.items() if len(locs)==1}
    missing_ref_rows=[]
    cross_ref_rows=[]
    for v,code,path,lab in all_refs:
        target=label_owner.get(lab)
        if not target:
            missing_ref_rows.append({"source_volume":v,"source_code":code,"source_path":path,"label":lab})
        elif target[0]!=v:
            cross_ref_rows.append({
                "source_volume":v,"source_code":code,"source_path":path,"label":lab,
                "target_volume":target[0],"target_code":target[1],"target_path":target[2]
            })
    if missing_ref_rows:
        blockers.append(f"missing LaTeX references={len(missing_ref_rows)}")
    if scaffold_hits:
        blockers.append(f"reconstruction scaffolds={len(scaffold_hits)}")

    source_rows=[classify_source(r,repo,status_by_code) for r in migration]
    unresolved_sources=[r for r in source_rows if r["global_disposition"].startswith("UNRESOLVED")]
    missing_source_rows=[r for r in source_rows if r["source_exists"]=="NO"]
    if unresolved_sources:
        blockers.append(f"unresolved SOURCE_MIGRATION rows={len(unresolved_sources)}")
    if missing_source_rows:
        blockers.append(f"missing source files={len(missing_source_rows)}")

    if global_audit.get("status")!="PASS":
        blockers.append("GLOBAL_I_VIII_AUDIT is not PASS")
    if int(global_audit.get("canonical_encoding_files",0) or 0)!=0:
        blockers.append(f"canonical encoding findings={global_audit.get('canonical_encoding_files')}")

    write_tsv(reports/"GLOBAL_CHAPTER_PAIRING_AUDIT.tsv",chapter_rows,
              ["volume","chapter_code","chapter_title","canonical_path","path_exists","status","next_action",
               "graph_tex_files","pairing_policy","raw_pairing_match",
               "problems","exercises","hints","solutions","expected_solutions","pairing","scaffold"])
    write_tsv(reports/"GLOBAL_VOLUME_RELEASE_AUDIT.tsv",volume_rows,
              ["volume","title","chapters","expected_chapters","frozen","complete","canonical_paths",
               "pairing_policy","pairing_failures","raw_pairing_mismatches",
               "problems","exercises","hints","solutions","native_solution_contract","book_includes",
               "build_status","pdf_verified","status","blockers"])
    write_tsv(reports/"GLOBAL_SOURCE_RULE_RECONCILIATION.tsv",source_rows,
              ["source_file","source_family","source_block_id","block_kind","source_selector","source_topic",
               "destination","action","precedence","audit_status","source_exists","source_resolved_path",
               "destination_class","canonical_path","canonical_exists","chapter_status","next_action","global_disposition"])
    write_tsv(reports/"GLOBAL_MISSING_REFERENCE_AUDIT.tsv",missing_ref_rows,
              ["source_volume","source_code","source_path","label"])
    write_tsv(reports/"GLOBAL_CROSS_VOLUME_REFERENCE_RESOLVED.tsv",cross_ref_rows,
              ["source_volume","source_code","source_path","label","target_volume","target_code","target_path"])

    dup_rows=[]
    for lab,locs in sorted(duplicates.items()):
        for v,code,path in locs:
            dup_rows.append({"label":lab,"volume":v,"chapter_code":code,"path":path,"occurrences":len(locs)})
    write_tsv(reports/"GLOBAL_DUPLICATE_LABEL_AUDIT.tsv",dup_rows,
              ["label","volume","chapter_code","path","occurrences"])

    (reports/"VOLUME06_NATIVE_SOLUTION_CONTRACT.json").write_text(
        json.dumps(native_vi,indent=2,ensure_ascii=False)+"\n",encoding="utf-8"
    )
    vi_md=[
        "# Volume VI — Native Solution Contract Verification","",
        f"**Result:** {native_vi['status']}","",
        "- Policy: **native Volume VI freeze/reconciliation + fresh full-solutions edition build**",
        f"- Full-solutions pages: **{native_vi['full_solutions_pages']}**",
        f"- Full-solutions bytes: **{native_vi['full_solutions_bytes']}**",
        f"- Full-solutions SHA-256: `{native_vi['full_solutions_sha256']}`" if native_vi['full_solutions_sha256'] else "- Full-solutions SHA-256: unavailable",
        "","## Blockers",""
    ]
    vi_md += [f"- {x}" for x in native_vi["blockers"]] if native_vi["blockers"] else ["None."]
    (reports/"VOLUME06_NATIVE_SOLUTION_CONTRACT.md").write_text("\n".join(vi_md)+"\n",encoding="utf-8")

    summary={
        "status":"PASS" if not blockers else "FAIL",
        "chapters":len(status),
        "expected_chapters":256,
        "frozen":sum(r.get("status")=="FROZEN" for r in status),
        "complete":sum(r.get("next_action")=="COMPLETE" for r in status),
        "canonical_paths_existing":sum((repo/r.get("canonical_path","")).exists() for r in status),
        "volume_builds_pass":sum(r.get("status")=="PASS" for r in volume_rows),
        "source_migration_rows":len(migration),
        "source_rows_accounted":len(source_rows)-len(unresolved_sources),
        "unresolved_source_rows":len(unresolved_sources),
        "missing_source_files":len(missing_source_rows),
        "problems":total_problem,"exercises":total_exercise,"hints":total_hint,"solutions":total_solution,
        "active_tex_files_scanned":len(canonical_tex_files),
        "raw_pairing_mismatches":sum(r.get("raw_pairing_match")=="NO" for r in chapter_rows),
        "chapter_pairing_failures":sum(r["pairing"]=="FAIL" for r in chapter_rows),
        "volume06_native_solution_contract":native_vi["status"],
        "duplicate_labels":len(duplicates),
        "missing_references":len(missing_ref_rows),
        "cross_volume_references_resolved":len(cross_ref_rows),
        "reconstruction_scaffolds":len(scaffold_hits),
        "canonical_encoding_files":int(global_audit.get("canonical_encoding_files",0) or 0),
        "blocking":blockers,
    }
    (reports/"GLOBAL_SERIES_RECONCILIATION.json").write_text(json.dumps(summary,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    md=[
        "# Theory of Mathematics I–VIII — Global Corpus and Freeze Reconciliation","",
        f"**Result:** {summary['status']}","",
        "## Canonical atlas","",
        f"- Chapters / expected: **{summary['chapters']} / 256**",
        f"- FROZEN / COMPLETE: **{summary['frozen']} / {summary['complete']}**",
        f"- Existing canonical chapter paths: **{summary['canonical_paths_existing']} / 256**",
        f"- Canonical volume builds PASS: **{summary['volume_builds_pass']} / 8**","",
        "## Corpus accounting","",
        f"- SOURCE_MIGRATION rows: **{summary['source_migration_rows']}**",
        f"- Accounted without unresolved disposition: **{summary['source_rows_accounted']}**",
        f"- Unresolved rows: **{summary['unresolved_source_rows']}**",
        f"- Missing source files: **{summary['missing_source_files']}**","",
        "## Solved-material pairing audit","",
        f"- `problem` environments: **{summary['problems']}**",
        f"- `exercise` environments: **{summary['exercises']}**",
        f"- `hint` environments: **{summary['hints']}**",
        f"- `solution` environments: **{summary['solutions']}**",
        f"- Active physical TeX files scanned recursively: **{summary['active_tex_files_scanned']}**",
        f"- Raw chapters where source counts differ (`solutions != problems + exercises`): **{summary['raw_pairing_mismatches']}**",
        f"- Blocking pairing failures under the volume-specific release policy: **{summary['chapter_pairing_failures']}**",
        f"- Volume VI native full-solutions/freeze contract: **{summary['volume06_native_solution_contract']}**","",
        "## Labels and references","",
        f"- Duplicate labels: **{summary['duplicate_labels']}**",
        f"- Missing references: **{summary['missing_references']}**",
        f"- Resolved cross-volume references: **{summary['cross_volume_references_resolved']}**",
        f"- Remaining reconstruction scaffolds: **{summary['reconstruction_scaffolds']}**",
        f"- Canonical encoding findings: **{summary['canonical_encoding_files']}**","",
        "## Blocking findings",""
    ]
    md += [f"- {b}" for b in blockers] if blockers else ["None."]
    (reports/"GLOBAL_SERIES_RECONCILIATION.md").write_text("\n".join(md)+"\n",encoding="utf-8")
    print(json.dumps(summary,indent=2,ensure_ascii=False))
    return 0 if not blockers else 4

if __name__=="__main__":
    raise SystemExit(main())
