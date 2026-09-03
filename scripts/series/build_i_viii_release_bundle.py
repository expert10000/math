#!/usr/bin/env python3
from __future__ import annotations
import argparse,csv,hashlib,json,re,shutil
from pathlib import Path

VOLS=[
("I",1,"Linear Algebra","vol01_linear_algebra"),
("II",2,"Real Analysis and Topological Foundations","vol02_real_analysis"),
("III",3,"Measure, Fourier Analysis, Distributions and PDE","vol03_fourier_distributions_pde"),
("IV",4,"Complex Analysis and Riemann Surfaces","vol04_complex_analysis"),
("V",5,"Commutative Algebra and Homological Methods","vol05_commutative_algebra"),
("VI",6,"Algebraic Geometry and Sheaf Theory","vol06_algebraic_geometry"),
("VII",7,"Differential, Riemannian and Hyperbolic Geometry","vol07_differential_geometry"),
("VIII",8,"Algebraic Topology","vol08_algebraic_topology"),
]

def tsv(path):
    with Path(path).open("r",encoding="utf-8-sig",newline="") as f:
        return list(csv.DictReader(f,delimiter="\t"))

def sha(path):
    h=hashlib.sha256()
    with Path(path).open("rb") as f:
        for b in iter(lambda:f.read(1024*1024),b""):
            h.update(b)
    return h.hexdigest()

def pages(path):
    return len(re.findall(rb"/Type\s*/Page(?!s)\b",Path(path).read_bytes()))

def write_tsv(path,rows,fields):
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    with path.open("w",encoding="utf-8",newline="") as f:
        w=csv.DictWriter(f,fieldnames=fields,delimiter="\t",lineterminator="\n",extrasaction="ignore")
        w.writeheader();w.writerows(rows)

def copy_if(src,dst):
    src=Path(src);dst=Path(dst)
    if not src.exists():
        return False
    dst.parent.mkdir(parents=True,exist_ok=True)
    shutil.copy2(src,dst)
    return True

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--repo",required=True)
    ap.add_argument("--release-name",default="theory_of_mathematics_i_viii_v1.0")
    args=ap.parse_args()
    repo=Path(args.repo).resolve()
    release_root=repo/"release"/args.release_name
    if release_root.exists():
        shutil.rmtree(release_root)
    (release_root/"pdfs").mkdir(parents=True)
    (release_root/"evidence").mkdir(parents=True)
    (release_root/"manifests").mkdir(parents=True)

    recon_path=repo/"reports/series/GLOBAL_SERIES_RECONCILIATION.json"
    if not recon_path.exists():
        raise SystemExit("GLOBAL_SERIES_RECONCILIATION.json missing")
    recon=json.loads(recon_path.read_text(encoding="utf-8"))
    if recon.get("status")!="PASS":
        raise SystemExit("Global series reconciliation is not PASS")
    if recon.get("chapters")!=256 or recon.get("frozen")!=256 or recon.get("complete")!=256:
        raise SystemExit("Global series reconciliation is not a 256/256 frozen-complete state")
    if recon.get("volume_builds_pass")!=8:
        raise SystemExit("Global series reconciliation does not show 8/8 PASS builds")

    status=tsv(repo/"editorial/CHAPTER_STATUS.tsv")
    if len(status)!=256:
        raise SystemExit(f"Expected 256 status rows, found {len(status)}")

    pdf_rows=[]
    for v,n,title,dirname in VOLS:
        src=repo/"books"/dirname/"book.pdf"
        if not src.exists():
            raise SystemExit(f"Missing canonical PDF for Volume {v}: {src}")
        dest=release_root/"pdfs"/f"volume{n:02d}_{dirname.removeprefix(f'vol{n:02d}_')}.pdf"
        shutil.copy2(src,dest)
        pdf_rows.append({
            "volume":v,"number":n,"title":title,
            "canonical_pdf":src.relative_to(repo).as_posix(),
            "release_pdf":dest.relative_to(release_root).as_posix(),
            "pages":pages(src),"bytes":src.stat().st_size,"sha256":sha(src),
        })

    chapter_rows=[]
    for r in status:
        cp=repo/r["canonical_path"]
        if not cp.exists():
            raise SystemExit(f"Missing chapter while building release: {r['chapter_code']}")
        chapter_rows.append({
            "volume":r["volume"],"chapter_code":r["chapter_code"],"chapter_title":r["chapter_title"],
            "status":r["status"],"next_action":r["next_action"],
            "canonical_path":r["canonical_path"],"bytes":cp.stat().st_size,"sha256":sha(cp),
        })

    write_tsv(release_root/"manifests/CHAPTERS.tsv",chapter_rows,
              ["volume","chapter_code","chapter_title","status","next_action","canonical_path","bytes","sha256"])
    write_tsv(release_root/"manifests/PDFS.tsv",pdf_rows,
              ["volume","number","title","canonical_pdf","release_pdf","pages","bytes","sha256"])

    evidence=[
        ("editorial/CONTENT_ATLAS.md","CONTENT_ATLAS.md"),
        ("editorial/CHAPTER_STATUS.tsv","CHAPTER_STATUS.tsv"),
        ("editorial/SOURCE_MIGRATION.tsv","SOURCE_MIGRATION.tsv"),
        ("reports/series/GLOBAL_I_VIII_AUDIT.json","GLOBAL_I_VIII_AUDIT.json"),
        ("reports/series/GLOBAL_I_VIII_AUDIT.md","GLOBAL_I_VIII_AUDIT.md"),
        ("reports/series/GLOBAL_SERIES_RECONCILIATION.json","GLOBAL_SERIES_RECONCILIATION.json"),
        ("reports/series/GLOBAL_SERIES_RECONCILIATION.md","GLOBAL_SERIES_RECONCILIATION.md"),
        ("reports/series/GLOBAL_SOURCE_RULE_RECONCILIATION.tsv","GLOBAL_SOURCE_RULE_RECONCILIATION.tsv"),
        ("reports/series/GLOBAL_CHAPTER_PAIRING_AUDIT.tsv","GLOBAL_CHAPTER_PAIRING_AUDIT.tsv"),
        ("reports/series/GLOBAL_VOLUME_RELEASE_AUDIT.tsv","GLOBAL_VOLUME_RELEASE_AUDIT.tsv"),
        ("reports/series/VOLUME06_NATIVE_SOLUTION_CONTRACT.json","VOLUME06_NATIVE_SOLUTION_CONTRACT.json"),
        ("reports/series/VOLUME06_NATIVE_SOLUTION_CONTRACT.md","VOLUME06_NATIVE_SOLUTION_CONTRACT.md"),
        ("reports/series/GLOBAL_DUPLICATE_LABEL_AUDIT.tsv","GLOBAL_DUPLICATE_LABEL_AUDIT.tsv"),
        ("reports/series/GLOBAL_MISSING_REFERENCE_AUDIT.tsv","GLOBAL_MISSING_REFERENCE_AUDIT.tsv"),
        ("reports/series/GLOBAL_CROSS_VOLUME_REFERENCE_RESOLVED.tsv","GLOBAL_CROSS_VOLUME_REFERENCE_RESOLVED.tsv"),
        ("reports/series/GLOBAL_ENCODING_AUDIT.tsv","GLOBAL_ENCODING_AUDIT.tsv"),
        ("reports/series/GLOBAL_CANONICAL_PATH_AUDIT.tsv","GLOBAL_CANONICAL_PATH_AUDIT.tsv"),
        ("reports/series/BUILD_I_VIII.tsv","BUILD_I_VIII.tsv"),
        ("reports/series/BUILD_I_VIII.md","BUILD_I_VIII.md"),
        ("reports/series/PDF_INVENTORY.tsv","PDF_INVENTORY.tsv"),
        ("reports/series/SERIES_BUILD_VERIFICATION.json","SERIES_BUILD_VERIFICATION.json"),
        ("reports/series/SERIES_BUILD_VERIFICATION.md","SERIES_BUILD_VERIFICATION.md"),
        ("books/SERIES_NAVIGATION.md","SERIES_NAVIGATION.md"),
        ("books/CROSS_VOLUME_REFERENCE_AUDIT.tsv","CROSS_VOLUME_REFERENCE_AUDIT.tsv"),
        ("books/VOLUME_METADATA_AUDIT.tsv","VOLUME_METADATA_AUDIT.tsv"),
        ("release/SERIES_MASTER_MANIFEST.tsv","SERIES_MASTER_MANIFEST.tsv"),
        ("release/SERIES_MASTER_MANIFEST.sha256","SERIES_MASTER_MANIFEST.sha256"),
        ("release/SERIES_RELEASE_DASHBOARD.md","SERIES_RELEASE_DASHBOARD.md"),
        ("release/SERIES_RELEASE_READINESS.json","SERIES_RELEASE_READINESS.json"),
    ]
    copied=[]
    for rel,name in evidence:
        if copy_if(repo/rel,release_root/"evidence"/name):
            copied.append(name)

    # Preserve each volume's own freeze evidence without assuming identical filenames.
    freeze_files=[]
    for v,n,title,dirname in VOLS:
        fd=repo/"books"/dirname/"freeze"
        if not fd.exists():
            continue
        destdir=release_root/"evidence"/"volume_freeze"/f"volume{n:02d}"
        for p in sorted(fd.rglob("*")):
            if p.is_file() and p.suffix.lower() in {".md",".json",".tsv",".sha256"}:
                dest=destdir/p.relative_to(fd)
                copy_if(p,dest)
                freeze_files.append(dest.relative_to(release_root).as_posix())

    release_notes=[
        "# Theory of Mathematics I–VIII — Release 1.0","",
        "This directory is the immutable repository release bundle for the fully reconstructed canonical eight-volume series.","",
        "## Release state","",
        "- Canonical volumes: **8 / 8**",
        "- Canonical chapters: **256 / 256**",
        "- Chapter status: **256 FROZEN / 256 COMPLETE**",
        "- Canonical PDF builds: **8 PASS / 0 FAIL / 0 NO_WRAPPER**",
        f"- SOURCE_MIGRATION rows: **{recon.get('source_migration_rows')}**",
        f"- Unresolved source-map rows: **{recon.get('unresolved_source_rows')}**",
        f"- Missing mapped source files: **{recon.get('missing_source_files')}**",
        f"- Duplicate canonical labels: **{recon.get('duplicate_labels')}**",
        f"- Missing canonical references: **{recon.get('missing_references')}**",
        f"- Reconstruction scaffolds remaining: **{recon.get('reconstruction_scaffolds')}**","",
        "## PDFs",""
    ]
    for r in pdf_rows:
        release_notes.append(
            f"- Volume {r['volume']} — {r['title']}: **{r['pages']} pages**, "
            f"SHA-256 `{r['sha256']}`"
        )
    release_notes += [
        "","## Manifests","",
        "- `manifests/CHAPTERS.tsv` — one row per canonical chapter with source hash.",
        "- `manifests/PDFS.tsv` — one row per canonical volume PDF with page count, size, and SHA-256.",
        "- `SHA256SUMS.txt` — hashes for every file in this release bundle except the hash file itself.",
        "","## Evidence","",
        "The `evidence/` directory contains the global audits, source-migration reconciliation, build inventories, navigation, dashboard, and available per-volume freeze evidence.",""
    ]
    (release_root/"RELEASE_NOTES.md").write_text("\n".join(release_notes)+"\n",encoding="utf-8")

    metadata={
        "schema":1,
        "release":"Theory of Mathematics I–VIII v1.0",
        "tag":"theory-of-mathematics-i-viii-v1.0",
        "volumes":8,
        "chapters":256,
        "source_migration_rows":recon.get("source_migration_rows"),
        "pdfs":pdf_rows,
        "chapter_manifest":"manifests/CHAPTERS.tsv",
        "pdf_manifest":"manifests/PDFS.tsv",
        "evidence_files":copied,
        "volume_freeze_evidence_files":freeze_files,
    }
    (release_root/"RELEASE.json").write_text(json.dumps(metadata,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")

    # Final immutable hash manifest.
    lines=[]
    for p in sorted(release_root.rglob("*")):
        if p.is_file() and p.name!="SHA256SUMS.txt":
            lines.append(f"{sha(p)}  {p.relative_to(release_root).as_posix()}")
    (release_root/"SHA256SUMS.txt").write_text("\n".join(lines)+"\n",encoding="utf-8")

    # Self-verification: all listed files exist and hash correctly.
    for line in (release_root/"SHA256SUMS.txt").read_text(encoding="utf-8").splitlines():
        digest,rel=line.split("  ",1)
        p=release_root/rel
        if not p.exists() or sha(p)!=digest:
            raise SystemExit(f"Release hash verification failed: {rel}")

    summary={
        "status":"PASS",
        "release_dir":release_root.relative_to(repo).as_posix(),
        "pdfs":len(pdf_rows),
        "chapters":len(chapter_rows),
        "evidence_files":len(copied),
        "volume_freeze_evidence_files":len(freeze_files),
        "sha256_entries":len(lines),
    }
    print(json.dumps(summary,indent=2))
    return 0

if __name__=="__main__":
    raise SystemExit(main())
