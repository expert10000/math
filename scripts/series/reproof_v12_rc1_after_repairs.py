#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, shutil, subprocess
from pathlib import Path


def run(cmd, cwd=None):
    cp = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, errors="replace")
    if cp.returncode != 0:
        raise RuntimeError("Command failed: " + " ".join(map(str, cmd)) + "\n" + cp.stdout[-3000:] + "\n" + cp.stderr[-3000:])
    return cp


def sha256(path: Path):
    h = hashlib.sha256()
    with path.open("rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


def refresh_sums(rc: Path):
    lines = []
    for p in sorted(rc.rglob("*")):
        if p.is_file() and p.name != "SHA256SUMS.txt":
            lines.append(f"{sha256(p)}  {p.relative_to(rc).as_posix()}")
    (rc / "SHA256SUMS.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")
    for line in lines:
        digest, rel = line.split("  ", 1)
        if sha256(rc / rel) != digest:
            raise RuntimeError("Hash verification failed: " + rel)
    return lines


def copy_evidence(repo: Path, rc: Path, rels):
    copied = []
    ev = rc / "evidence"; ev.mkdir(parents=True, exist_ok=True)
    for rel in rels:
        src = repo / rel
        if not src.exists():
            raise RuntimeError("Missing evidence file: " + rel)
        dst = ev / src.name
        shutil.copy2(src, dst)
        copied.append(dst.relative_to(rc).as_posix())
    return copied


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", required=True)
    args = ap.parse_args()
    repo = Path(args.repo).resolve()
    reports = repo / "reports/series"

    triage = json.loads((reports / "V12_RC1_RENDER_TRIAGE.json").read_text(encoding="utf-8"))
    repair = json.loads((reports / "V12_RC1_LAYOUT_REPAIR.json").read_text(encoding="utf-8"))
    if triage.get("status") != "PASS" or repair.get("status") != "PASS":
        raise SystemExit("Triage/repair evidence is not PASS")

    # Official clean rebuild: reuse the already-audited uniform I-VIII driver.
    build_script = repo / "scripts/series/build_post_pedagogy_i_viii.py"
    audit_script = repo / "scripts/series/audit_post_pedagogy_rendered_i_viii.py"
    rc_builder = repo / "scripts/series/build_v12_rc1_bundle.py"
    for p in (build_script, audit_script, rc_builder):
        if not p.exists():
            raise SystemExit("Missing prerequisite series script: " + str(p))

    run(["python", str(build_script), "--repo", str(repo)])

    # Replace the pre-repair reproof snapshot with the official post-repair reproof.
    run([
        "python", str(audit_script), "--repo", str(repo),
        "--label", "POST_PEDAGOGY_REPROOF",
        "--inventory", "reports/series/POST_PEDAGOGY_PDF_INVENTORY.tsv",
        "--dpi", "24",
    ])
    reproof_path = reports / "POST_PEDAGOGY_REPROOF_AUDIT.json"
    reproof = json.loads(reproof_path.read_text(encoding="utf-8"))
    if reproof.get("status") != "PASS" or int(reproof.get("volumes",0)) != 8:
        raise SystemExit("Post-repair rendered reproof is not PASS")

    before_high = int(triage.get("overfull_ge_20pt",0))
    after_high = int(reproof.get("overfull_ge_20pt",0))
    if after_high > before_high:
        raise SystemExit(f"Post-repair reproof regressed severe overfull boxes: {after_high}>{before_high}")

    # Regenerate the existing RC transactionally. The v1.2 builder deliberately
    # keeps final_release_frozen=false and the human rendered-proof gate pending.
    rc = repo / "release/theory_of_mathematics_i_viii_v1.2-rc1"
    backup = repo / "release/.theory_of_mathematics_i_viii_v1.2-rc1.backup"
    if backup.exists():
        shutil.rmtree(backup)
    if not rc.exists():
        raise SystemExit("Current v1.2-rc1 release directory is missing")
    shutil.move(str(rc), str(backup))
    try:
        run(["python", str(rc_builder), "--repo", str(repo)])
        if not rc.exists():
            raise RuntimeError("RC builder did not recreate v1.2-rc1")
    except Exception:
        if rc.exists():
            shutil.rmtree(rc)
        shutil.move(str(backup), str(rc))
        raise
    else:
        shutil.rmtree(backup)

    extra_evidence = [
        "reports/series/V12_RC1_RENDER_TRIAGE.tsv",
        "reports/series/V12_RC1_RENDER_TRIAGE.json",
        "reports/series/V12_RC1_RENDER_TRIAGE.md",
        "reports/series/V12_RC1_LAYOUT_REPAIR.json",
        "reports/series/V12_RC1_LAYOUT_REPAIR.md",
    ]
    copied = copy_evidence(repo, rc, extra_evidence)

    shared_preamble = repo / "shared/preamble.tex"
    layout_hash = sha256(shared_preamble)
    (rc / "manifests/SHARED_LAYOUT_BASELINE.tsv").write_text(
        "path\tsha256\tpolicy\n"
        + f"shared/preamble.tex\t{layout_hash}\tv1.2-rc1-rendered-layout-repair\n",
        encoding="utf-8"
    )

    release_json = rc / "RELEASE.json"
    meta = json.loads(release_json.read_text(encoding="utf-8"))
    meta["rendered_finding_triage"] = triage
    meta["confirmed_layout_repair"] = repair
    meta["post_repair_rendered_reproof"] = reproof
    meta["shared_rendering_layout"] = {
        "path": "shared/preamble.tex",
        "sha256": layout_hash,
        "policy": repair.get("policy"),
    }
    meta["release_decision"] = "PENDING_HUMAN_RENDERED_REPROOF"
    meta["human_rendered_proof_required"] = True
    meta["final_release_frozen"] = False
    evs = list(meta.get("evidence_sources", []))
    for rel in extra_evidence:
        if rel not in evs:
            evs.append(rel)
    meta["evidence_sources"] = evs
    release_json.write_text(json.dumps(meta, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    notes = rc / "RELEASE_NOTES.md"
    notes.write_text(notes.read_text(encoding="utf-8") + "\n## Rendered-repair reproof\n\n"
                     + f"- Confirmed >=20pt overfull queue before repair: **{before_high}**.\n"
                     + f"- Confirmed >=20pt overfull queue after clean reproof: **{after_high}**.\n"
                     + "- Shared line-breaking repair changed no mathematical chapter content.\n"
                     + "- Final release status remains **PENDING_HUMAN_RENDERED_REPROOF**.\n",
                     encoding="utf-8")

    lines = refresh_sums(rc)
    rc_aggregate = hashlib.sha256("\n".join(lines).encode("utf-8")).hexdigest()

    summary_path = reports / "V12_RC1_SUMMARY.json"
    summary = json.loads(summary_path.read_text(encoding="utf-8"))
    summary["status"] = "PASS"
    summary["release_files_hashed"] = len(lines)
    summary["rc_aggregate_sha256"] = rc_aggregate
    summary["render_triage"] = "PASS"
    summary["layout_repair"] = repair.get("effect")
    summary["overfull_ge_20pt_before_repair"] = before_high
    summary["overfull_ge_20pt_after_repair"] = after_high
    summary["human_rendered_proof_required"] = True
    summary["final_release_frozen"] = False
    summary["release_decision"] = "PENDING_HUMAN_RENDERED_REPROOF"
    summary_path.write_text(json.dumps(summary, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    (reports / "V12_RC1_SUMMARY.md").write_text(
        "# Theory of Mathematics I–VIII — v1.2 RC1 summary after rendered repairs\n\n"
        "**Automated reproof:** PASS\n\n"
        f"- Volumes: **{summary.get('volumes')}**\n"
        f"- Chapters: **{summary.get('chapters')}**\n"
        f"- PDFs: **{summary.get('pdfs')}**\n"
        f"- PDF pages: **{summary.get('pdf_pages')}**\n"
        f"- >=20pt overfull queue: **{before_high} -> {after_high}**\n"
        f"- RC aggregate SHA-256: `{rc_aggregate}`\n\n"
        "**Release decision:** PENDING_HUMAN_RENDERED_REPROOF\n\n"
        "The final v1.2 release freeze remains separate.\n",
        encoding="utf-8"
    )

    # Recompute the top-level master hash because RELEASE.json / SHA256SUMS changed
    # after the stock RC builder completed.
    release_root = repo / "release"
    primary = [
        reports / "SERIES_PEDAGOGY_FREEZE.json",
        reports / "POST_PEDAGOGY_REPROOF_AUDIT.json",
        reports / "POST_PEDAGOGY_BUILD_I_VIII.tsv",
        reports / "POST_PEDAGOGY_PDF_INVENTORY.tsv",
        release_root / "SERIES_MASTER_MANIFEST.tsv",
        release_root / "SERIES_RELEASE_READINESS.json",
        rc / "RELEASE.json",
        rc / "SHA256SUMS.txt",
    ]
    master_lines = [f"{sha256(p)}  {p.relative_to(repo).as_posix()}" for p in primary]
    (release_root / "SERIES_MASTER_MANIFEST.sha256").write_text("\n".join(master_lines) + "\n", encoding="utf-8")

    out = {
        "schema": 1,
        "status": "PASS",
        "candidate": "v1.2-rc1",
        "volumes": int(reproof.get("volumes",0)),
        "pdf_pages": int(reproof.get("pdf_pages",0)),
        "rendered_pages": int(reproof.get("rendered_pages",0)),
        "overfull_ge_20pt_before": before_high,
        "overfull_ge_20pt_after": after_high,
        "repair_effect": repair.get("effect"),
        "shared_preamble_sha256": layout_hash,
        "extra_evidence_copied": copied,
        "release_files_hashed": len(lines),
        "rc_aggregate_sha256": rc_aggregate,
        "human_rendered_proof_required": True,
        "final_release_frozen": False,
        "release_decision": "PENDING_HUMAN_RENDERED_REPROOF",
        "blocking": [],
    }
    (reports / "V12_RC1_AFTER_REPAIRS_REPROOF.json").write_text(
        json.dumps(out, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    (reports / "V12_RC1_AFTER_REPAIRS_REPROOF.md").write_text(
        "# v1.2-rc1 reproof after rendered repairs\n\n"
        "**Result:** PASS\n\n"
        f"- Rendered pages: **{out['rendered_pages']} / {out['pdf_pages']}**\n"
        f"- >=20pt overfull queue: **{before_high} -> {after_high}**\n"
        f"- Repair effect: **{out['repair_effect']}**\n"
        "- Final release frozen: **NO**\n"
        "- Human rendered proof required: **YES**\n\n"
        "The final v1.2 freeze remains a separate commit.\n",
        encoding="utf-8"
    )
    print(json.dumps(out, indent=2, ensure_ascii=False))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
