from __future__ import annotations
import csv, hashlib, json, re, subprocess, sys
from pathlib import Path

VOLUMES=[
("I","vol01_linear_algebra","VOLUME01_FREEZE_MANIFEST.sha256"),
("II","vol02_real_analysis","VOLUME02_FREEZE_MANIFEST.sha256"),
("III","vol03_fourier_distributions_pde","VOLUME03_FREEZE_MANIFEST.sha256"),
("IV","vol04_complex_analysis","VOLUME04_FREEZE_MANIFEST.sha256"),
("V","vol05_commutative_algebra","VOLUME05_FREEZE_MANIFEST.sha256"),
("VI","vol06_algebraic_geometry","VOLUME06_FREEZE_MANIFEST.sha256"),
("VII","vol07_differential_geometry","VOLUME07_FREEZE_MANIFEST.sha256"),
("VIII","vol08_algebraic_topology","VOLUME08_FREEZE_MANIFEST.sha256"),
]
ROW=re.compile(r"^([0-9a-fA-F]{64})\s{2,}(.+?)\s*$")
OVER=re.compile(r"Overfull [\\]?[hv]box \(([-+]?\d+(?:\.\d+)?)pt too (?:wide|high)\)",re.I)
BLOCK_PHRASES=("latex warning: there were undefined references","there were undefined citations","multiply defined","! latex error","! emergency stop")
SOURCE_EXTS={".tex",".sty",".cls",".bib",".svg",".png",".jpg",".jpeg",".eps"}

def run(cmd,cwd,label,commands):
    print(f"\n=== {label} ===",flush=True)
    p=subprocess.run(cmd,cwd=cwd)
    commands.append({"label":label,"command":cmd,"returncode":p.returncode})
    if p.returncode: raise SystemExit(f"{label} failed with exit code {p.returncode}")

def tracked(repo,rel):
    return subprocess.run(["git","cat-file","-e",f"HEAD:{rel}"],cwd=repo,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL).returncode==0

def resolve(repo,d,entry):
    entry=entry.replace("\\","/").lstrip("./")
    for rel in (entry,f"books/{d}/{entry}"):
        if tracked(repo,rel): return rel
    raise RuntimeError(f"Unresolvable manifest entry: {d}: {entry}")

def git_blob(repo,rel):
    p=subprocess.run(["git","show",f"HEAD:{rel}"],cwd=repo,capture_output=True)
    if p.returncode: raise RuntimeError(f"Cannot read HEAD:{rel}")
    return p.stdout

def canonical_manifest_verify(repo):
    findings=[]; count=0
    for v,d,mn in VOLUMES:
        mp=repo/"books"/d/"freeze"/mn
        for line in mp.read_text(encoding="utf-8-sig").splitlines():
            m=ROW.match(line)
            if not m: continue
            count+=1
            rel=resolve(repo,d,m.group(2))
            got=hashlib.sha256(git_blob(repo,rel)).hexdigest()
            if got.lower()!=m.group(1).lower():
                findings.append({"volume":v,"entry":m.group(2),"resolved_path":rel,"expected":m.group(1).lower(),"git_blob_sha256":got})
    return count,findings

def adapt_manifests_to_checkout(repo):
    changed=0
    for v,d,mn in VOLUMES:
        mp=repo/"books"/d/"freeze"/mn
        lines=[]
        for line in mp.read_text(encoding="utf-8-sig").splitlines():
            m=ROW.match(line)
            if not m:
                lines.append(line); continue
            rel=resolve(repo,d,m.group(2))
            raw=(repo/rel).read_bytes()
            h=hashlib.sha256(raw).hexdigest()
            if h.lower()!=m.group(1).lower(): changed+=1
            lines.append(f"{h}  {m.group(2)}")
        mp.write_text("\n".join(lines)+"\n",encoding="utf-8")
    return changed

def loadj(p):
    return json.loads(p.read_text(encoding="utf-8-sig"))

def readtsv(p):
    with p.open("r",encoding="utf-8-sig",newline="") as f: return list(csv.DictReader(f,delimiter="\t"))

def local_only(repo):
    tracked_files=set(subprocess.check_output(["git","ls-files"],cwd=repo,text=True).splitlines())
    bad=set()
    for _,d,_ in VOLUMES:
        fls=repo/"books"/d/"book.fls"
        if not fls.exists(): continue
        for line in fls.read_text(encoding="utf-8",errors="replace").splitlines():
            if not line.startswith("INPUT "): continue
            val=line[6:].strip().strip('"')
            p=Path(val)
            try:
                p=(p if p.is_absolute() else fls.parent/p).resolve()
                rel=p.relative_to(repo).as_posix()
            except Exception: continue
            if p.suffix.lower() in SOURCE_EXTS and rel not in tracked_files: bad.add(rel)
    return sorted(bad)

def main():
    if len(sys.argv)<2:
        print("usage: verify_v13_rc1_reproducibility.py REPO [EXPECTED_PARENT]",file=sys.stderr); return 2
    repo=Path(sys.argv[1]).resolve()
    expected_parent=sys.argv[2] if len(sys.argv)>2 else None
    reports=repo/"reports"/"series"; reports.mkdir(parents=True,exist_ok=True)
    head=subprocess.check_output(["git","rev-parse","HEAD"],cwd=repo,text=True).strip()
    tree=subprocess.check_output(["git","rev-parse","HEAD^{tree}"],cwd=repo,text=True).strip()
    if expected_parent:
        parent=subprocess.check_output(["git","rev-parse","HEAD^"],cwd=repo,text=True).strip()
        if parent!=expected_parent: raise SystemExit(f"candidate parent {parent} != expected {expected_parent}")

    canonical_rows,canonical_drift=canonical_manifest_verify(repo)
    if canonical_drift:
        print(json.dumps(canonical_drift[:20],indent=2))
        raise SystemExit(f"canonical freeze-manifest verification failed: {len(canonical_drift)} row(s)")

    adapted=adapt_manifests_to_checkout(repo)

    commands=[]; py=sys.executable
    run([py,"scripts/series/audit_reviewed_freezes_i_viii.py","--repo",str(repo),"--repair-shared-metadata"],repo,"Reviewed freeze verification + clean canonical builds",commands)
    vi=repo/"books"/"vol06_algebraic_geometry"
    run(["latexmk","-C","book_full_solutions.tex"],vi,"Volume VI full-solutions clean",commands)
    run(["latexmk","-pdf","-interaction=nonstopmode","-halt-on-error","-file-line-error","book_full_solutions.tex"],vi,"Volume VI full-solutions build",commands)
    run([py,"scripts/series/refresh_current_pdf_inventory.py","--repo",str(repo)],repo,"Refresh PDF inventory",commands)
    run([py,"scripts/series/verify_series_build.py","--repo",str(repo)],repo,"Verify canonical builds",commands)
    run([py,"scripts/series/audit_pedagogy_i_viii.py","--repo",str(repo)],repo,"Pedagogy audit",commands)
    run([py,"scripts/series/reconcile_i_viii_release.py","--repo",str(repo)],repo,"Full I-VIII release reconciliation",commands)

    ev={
      "reviewed_freeze":loadj(reports/"REVIEWED_FREEZE_BUILD_AUDIT_I_VIII.json"),
      "build_verification":loadj(reports/"SERIES_BUILD_VERIFICATION.json"),
      "reconciliation":loadj(reports/"GLOBAL_SERIES_RECONCILIATION.json"),
    }
    inv={r["volume"]:r for r in readtsv(reports/"PDF_INVENTORY.tsv")}
    rc=loadj(repo/"release"/"CANONICAL_VOLUME_I_VIII_RELEASE_MANIFEST.json")
    exp={x["volume"]:x for x in rc["volumes_manifest"]}
    rows=[]; blockers=[]; drift=[]
    for v,d,_ in VOLUMES:
        got=inv.get(v); ex=exp.get(v)
        if not got or not ex:
            blockers.append(f"{v}: missing PDF inventory/RC row"); continue
        pm=str(got.get("pages"))==str(ex.get("pdf_pages"))
        hm=str(got.get("sha256","")).lower()==str(ex.get("pdf_sha256","")).lower()
        if not pm: blockers.append(f"{v}: page count {got.get('pages')} != RC {ex.get('pdf_pages')}")
        if not hm: drift.append(v)
        log=repo/"books"/d/"book.log"
        txt=log.read_text(encoding="utf-8",errors="replace") if log.exists() else ""
        low=txt.lower(); hits=[p for p in BLOCK_PHRASES if p in low]; overs=[float(x) for x in OVER.findall(txt)]; ge20=[x for x in overs if x>=20]
        if hits: blockers.append(f"{v}: blocking LaTeX diagnostics")
        if ge20: blockers.append(f"{v}: {len(ge20)} overfull box(es) >=20pt")
        rows.append({"volume":v,"pages_rc":ex.get("pdf_pages"),"pages_rebuilt":got.get("pages"),"page_match":"YES" if pm else "NO","sha256_rc":ex.get("pdf_sha256"),"sha256_rebuilt":got.get("sha256"),"byte_hash_match":"YES" if hm else "NO","overfull_ge_20pt":len(ge20),"blocking_log_phrases":len(hits)})
    loc=local_only(repo)
    if loc: blockers.append(f"local-only tracked-source dependencies={len(loc)}")
    for k,x in ev.items():
        if x.get("status")!="PASS": blockers.append(f"{k} status={x.get('status')}")
    status="PASS" if not blockers else "FAIL"
    summary={
      "schema":2,"status":status,"gate":"V13_RC1_CLEAN_CHECKOUT_REPRODUCIBILITY",
      "candidate_commit":head,"candidate_tree":tree,"parent_commit":expected_parent,
      "canonical_freeze_manifest_rows_verified":canonical_rows,
      "canonical_freeze_manifest_drift":0,
      "legacy_worktree_hash_rows_adapted_in_disposable_checkout":adapted,
      "volumes":8,"chapters":256,
      "page_counts_match":sum(r["page_match"]=="YES" for r in rows),
      "pdf_byte_hashes_match":sum(r["byte_hash_match"]=="YES" for r in rows),
      "pdf_byte_hash_drift_volumes":drift,
      "pdf_byte_hash_policy":"informational; TeX build metadata may alter bytes",
      "overfull_ge_20pt_total":sum(r["overfull_ge_20pt"] for r in rows),
      "local_only_dependencies":loc,
      "evidence_status":{k:x.get("status") for k,x in ev.items()},
      "commands":commands,"blocking":blockers,
    }
    with (reports/"V13_RC1_REPRODUCIBILITY.tsv").open("w",encoding="utf-8",newline="") as f:
        fields=list(rows[0].keys()); w=csv.DictWriter(f,fieldnames=fields,delimiter="\t",lineterminator="\n");w.writeheader();w.writerows(rows)
    (reports/"V13_RC1_REPRODUCIBILITY.json").write_text(json.dumps(summary,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    md=["# v1.3-rc1 Clean-Checkout Reproducibility","",f"**Status: {status}**","",f"- Candidate commit: `{head}`",f"- Candidate tree: `{tree}`",f"- Canonical freeze-manifest rows verified: {canonical_rows}",f"- Page-count matches: {summary['page_counts_match']}/8",f"- Byte-identical PDF hashes: {summary['pdf_byte_hashes_match']}/8",f"- Overfull boxes >=20pt: {summary['overfull_ge_20pt_total']}","", "Freeze hashes are verified against immutable Git blob bytes before the disposable checkout is adapted for the legacy raw-worktree audit.","","## Blockers",""]+(["None."] if not blockers else ["- "+x for x in blockers])
    (reports/"V13_RC1_REPRODUCIBILITY.md").write_text("\n".join(md)+"\n",encoding="utf-8")
    print(json.dumps(summary,indent=2))
    return 0 if status=="PASS" else 4

if __name__=="__main__":
    raise SystemExit(main())
