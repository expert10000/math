#!/usr/bin/env python3
from __future__ import annotations
import argparse, csv, hashlib, json, shutil, subprocess
from pathlib import Path

TARGETS = [
    "books/vol06_algebraic_geometry/chapters/ch41_divisor_class_groups/chapter.tex",
    "books/vol07_differential_geometry/chapters/ch10_orientation_and_integration/chapter.tex",
    "books/vol08_algebraic_topology/chapters/ch35_lefschetz_theory/chapter.tex",
]

def run(cmd, cwd=None):
    cp=subprocess.run(cmd,cwd=cwd,capture_output=True,text=True,errors="replace")
    if cp.returncode!=0:
        raise RuntimeError("Command failed: "+" ".join(map(str,cmd))+"\n"+cp.stdout[-4000:]+"\n"+cp.stderr[-4000:])
    return cp

def sha256(path: Path):
    h=hashlib.sha256()
    with path.open("rb") as f:
        for b in iter(lambda:f.read(1<<20),b""):
            h.update(b)
    return h.hexdigest()

def refresh_sums(rc: Path):
    lines=[]
    for p in sorted(rc.rglob("*")):
        if p.is_file() and p.name!="SHA256SUMS.txt":
            lines.append(f"{sha256(p)}  {p.relative_to(rc).as_posix()}")
    (rc/"SHA256SUMS.txt").write_text("\n".join(lines)+"\n",encoding="utf-8")
    for line in lines:
        digest,rel=line.split("  ",1)
        if sha256(rc/rel)!=digest:
            raise RuntimeError("Hash verification failed: "+rel)
    return lines

def copy_to_evidence(repo: Path, rc: Path, rels):
    out=[]
    ev=rc/"evidence";ev.mkdir(parents=True,exist_ok=True)
    for rel in rels:
        src=repo/rel
        if not src.exists():
            raise RuntimeError("Missing residual evidence: "+rel)
        dst=ev/src.name
        shutil.copy2(src,dst)
        out.append(dst.relative_to(rc).as_posix())
    return out

def write_tsv(path: Path, rows, fields):
    path.parent.mkdir(parents=True,exist_ok=True)
    with path.open("w",encoding="utf-8",newline="") as f:
        w=csv.DictWriter(f,fieldnames=fields,delimiter="\t",lineterminator="\n",extrasaction="ignore")
        w.writeheader();w.writerows(rows)

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--repo",required=True)
    args=ap.parse_args()
    repo=Path(args.repo).resolve()
    reports=repo/"reports/series"
    rc=repo/"release/theory_of_mathematics_i_viii_v1.2-rc1"

    triage=json.loads((reports/"V12_RC1_RESIDUAL_LAYOUT_TRIAGE.json").read_text(encoding="utf-8"))
    repair=json.loads((reports/"V12_RC1_RESIDUAL_LAYOUT_REPAIR.json").read_text(encoding="utf-8"))
    if triage.get("status")!="PASS" or repair.get("status")!="PASS":
        raise SystemExit("Residual triage/repair prerequisite is not PASS.")
    if int(repair.get("after_affected_volume_overfull_ge_20pt",99))!=0:
        raise SystemExit("Affected-volume smoke build still has >=20pt overfull findings.")

    old_reproof=repo/"scripts/series/reproof_v12_rc1_after_repairs.py"
    if not old_reproof.exists():
        raise SystemExit("Missing prerequisite reproof_v12_rc1_after_repairs.py")
    run(["python",str(old_reproof),"--repo",str(repo)])

    reproof=json.loads((reports/"POST_PEDAGOGY_REPROOF_AUDIT.json").read_text(encoding="utf-8"))
    if reproof.get("status")!="PASS" or int(reproof.get("volumes",0))!=8:
        raise SystemExit("Full rendered reproof is not PASS for eight volumes.")
    if int(reproof.get("overfull_ge_20pt",99))!=0:
        raise SystemExit(f"Residual >=20pt queue is not zero: {reproof.get('overfull_ge_20pt')}")
    if int(reproof.get("rendered_pages",0))!=int(reproof.get("pdf_pages",0)):
        raise SystemExit("Not every final PDF page rendered.")

    dashboard=repo/"scripts/series/generate_release_dashboard.py"
    if dashboard.exists():
        run(["python",str(dashboard),"--repo",str(repo)])

    residual_evidence=[
        "reports/series/V12_RC1_RESIDUAL_LAYOUT_TRIAGE.tsv",
        "reports/series/V12_RC1_RESIDUAL_LAYOUT_TRIAGE.json",
        "reports/series/V12_RC1_RESIDUAL_LAYOUT_TRIAGE.md",
        "reports/series/V12_RC1_RESIDUAL_LAYOUT_REPAIR.json",
        "reports/series/V12_RC1_RESIDUAL_LAYOUT_REPAIR.md",
    ]
    copied=copy_to_evidence(repo,rc,residual_evidence)

    source_rows=[]
    for rel in TARGETS:
        p=repo/rel
        source_rows.append({"path":rel,"sha256":sha256(p),"role":"v1.2-residual-layout-fix"})
    write_tsv(rc/"manifests/RESIDUAL_LAYOUT_SOURCE_BASELINE.tsv",source_rows,["path","sha256","role"])

    meta_path=rc/"RELEASE.json"
    meta=json.loads(meta_path.read_text(encoding="utf-8"))
    meta["residual_layout_cleanup"]={
        "status":"PASS",
        "before_overfull_ge_20pt":3,
        "after_overfull_ge_20pt":0,
        "low_text_pages_classified_intentional":int(triage.get("low_text_pages_classified_intentional",0)),
        "source_baseline":source_rows,
    }
    meta["release_decision"]="PENDING_HUMAN_RENDERED_REPROOF"
    meta["human_rendered_proof_required"]=True
    meta["final_release_frozen"]=False
    evs=list(meta.get("evidence_sources",[]))
    for rel in residual_evidence:
        if rel not in evs: evs.append(rel)
    meta["evidence_sources"]=evs
    meta_path.write_text(json.dumps(meta,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")

    notes=rc/"RELEASE_NOTES.md"
    ntext=notes.read_text(encoding="utf-8")
    marker="## Residual display-layout cleanup"
    if marker not in ntext:
        ntext += (
            "\n"+marker+"\n\n"
            "- Three local residual display overflows were repaired in VI/41, VII/10, and VIII/35.\n"
            "- Final automated rendered reproof: **PASS**.\n"
            "- Final >=20pt overfull queue: **0**.\n"
            "- Low-text candidates remain classified as intentional structural/frontmatter pages.\n"
            "- Final release remains **PENDING_HUMAN_RENDERED_REPROOF** until the separate freeze commit.\n"
        )
    notes.write_text(ntext,encoding="utf-8")

    out={
        "schema":1,
        "status":"PASS",
        "candidate":"v1.2-rc1",
        "volumes":8,
        "pdf_pages":int(reproof.get("pdf_pages",0)),
        "rendered_pages":int(reproof.get("rendered_pages",0)),
        "overfull_ge_20pt_before_residual_fixes":3,
        "overfull_ge_20pt_after_residual_fixes":0,
        "low_text_pages_classified_intentional":int(triage.get("low_text_pages_classified_intentional",0)),
        "residual_sources":source_rows,
        "human_rendered_proof_required":True,
        "final_release_frozen":False,
        "release_decision":"PENDING_HUMAN_RENDERED_REPROOF",
        "blocking":[],
    }
    rjson=reports/"V12_RC1_RESIDUAL_REPROOF.json"
    rmd=reports/"V12_RC1_RESIDUAL_REPROOF.md"
    rjson.write_text(json.dumps(out,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    rmd.write_text(
        "# v1.2 RC1 residual-layout reproof\n\n"
        "**Status:** PASS\n\n"
        f"- Volumes: **8**.\n"
        f"- PDF/rendered pages: **{out['pdf_pages']} / {out['rendered_pages']}**.\n"
        "- >=20pt overfull queue: **3 -> 0**.\n"
        f"- Low-text structural/frontmatter pages classified intentional: **{out['low_text_pages_classified_intentional']}**.\n"
        "- Final release frozen: **No**.\n"
        "- Release decision: **PENDING_HUMAN_RENDERED_REPROOF**.\n",
        encoding="utf-8",
    )
    copied += copy_to_evidence(repo,rc,[
        "reports/series/V12_RC1_RESIDUAL_REPROOF.json",
        "reports/series/V12_RC1_RESIDUAL_REPROOF.md",
    ])
    meta=json.loads(meta_path.read_text(encoding="utf-8"))
    evs=list(meta.get("evidence_sources",[]))
    for rel in [
        "reports/series/V12_RC1_RESIDUAL_REPROOF.json",
        "reports/series/V12_RC1_RESIDUAL_REPROOF.md",
    ]:
        if rel not in evs: evs.append(rel)
    meta["evidence_sources"]=evs
    meta_path.write_text(json.dumps(meta,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")

    lines=refresh_sums(rc)
    aggregate=hashlib.sha256("\n".join(lines).encode("utf-8")).hexdigest()
    out["release_files_hashed"]=len(lines)
    out["rc_aggregate_sha256"]=aggregate
    out["extra_evidence_copied"]=copied
    rjson.write_text(json.dumps(out,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    shutil.copy2(rjson,rc/"evidence"/rjson.name)
    lines=refresh_sums(rc)
    aggregate=hashlib.sha256("\n".join(lines).encode("utf-8")).hexdigest()
    out["release_files_hashed"]=len(lines)
    out["rc_aggregate_sha256"]=aggregate
    rjson.write_text(json.dumps(out,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    shutil.copy2(rjson,rc/"evidence"/rjson.name)
    refresh_sums(rc)

    release_root=repo/"release"
    primary=[
        reports/"SERIES_PEDAGOGY_FREEZE.json",
        reports/"POST_PEDAGOGY_REPROOF_AUDIT.json",
        reports/"POST_PEDAGOGY_BUILD_I_VIII.tsv",
        reports/"POST_PEDAGOGY_PDF_INVENTORY.tsv",
        reports/"V12_RC1_RESIDUAL_REPROOF.json",
        release_root/"SERIES_MASTER_MANIFEST.tsv",
        release_root/"SERIES_RELEASE_READINESS.json",
        rc/"RELEASE.json",
        rc/"SHA256SUMS.txt",
    ]
    (release_root/"SERIES_MASTER_MANIFEST.sha256").write_text(
        "\n".join(f"{sha256(p)}  {p.relative_to(repo).as_posix()}" for p in primary)+"\n",
        encoding="utf-8",
    )
    print(json.dumps(out,indent=2))
    return 0

if __name__=="__main__":
    raise SystemExit(main())
