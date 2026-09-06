#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, re, subprocess
from pathlib import Path

VOLS = [
    ("I", "vol01_linear_algebra"),
    ("II", "vol02_real_analysis"),
    ("III", "vol03_fourier_distributions_pde"),
    ("IV", "vol04_complex_analysis"),
    ("V", "vol05_commutative_algebra"),
    ("VI", "vol06_algebraic_geometry"),
    ("VII", "vol07_differential_geometry"),
    ("VIII", "vol08_algebraic_topology"),
]

BEGIN = "% BEGIN V12-RC1-RENDERED-LAYOUT-REPAIR"
END = "% END V12-RC1-RENDERED-LAYOUT-REPAIR"
BLOCK = r'''% BEGIN V12-RC1-RENDERED-LAYOUT-REPAIR
% Rendered-proof triage found repeated wide prose/URL boxes after the pedagogy
% expansion. Give TeX controlled extra line-breaking flexibility without using
% \sloppy, resizing mathematics, or changing any mathematical source content.
\tolerance=2000
\setlength{\emergencystretch}{3em}
\Urlmuskip=0mu plus 2mu\relax
% END V12-RC1-RENDERED-LAYOUT-REPAIR
'''



def sha256(path: Path):
    h = hashlib.sha256()
    with path.open("rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()

def high_log_stats(log: Path):
    if not log.exists():
        return None
    text = log.read_text(encoding="utf-8-sig", errors="replace")
    hard = [
        "LaTeX Warning: There were undefined references",
        "There were undefined citations",
        "multiply defined",
        "Undefined control sequence",
        "Fatal error occurred",
        "Emergency stop",
    ]
    blockers = [x for x in hard if x.casefold() in text.casefold()]
    vals = [float(x) for x in re.findall(r"Overfull \\hbox \(([-+]?[0-9.]+)pt too wide\)", text, flags=re.I)]
    return {
        "total": len(vals),
        "ge20": sum(x >= 20 for x in vals),
        "max": max(vals) if vals else 0.0,
        "blockers": blockers,
    }


def build(repo: Path, dirname: str):
    vol = repo / "books" / dirname
    cp = subprocess.run(
        ["latexmk", "-pdf", "-interaction=nonstopmode", "-halt-on-error", "book.tex"],
        cwd=vol, capture_output=True, text=True, errors="replace"
    )
    if cp.returncode != 0:
        raise RuntimeError(f"Build failed for {dirname}\n{cp.stdout[-2500:]}\n{cp.stderr[-2500:]}")
    if not (vol / "book.pdf").exists() or not (vol / "book.log").exists():
        raise RuntimeError(f"Build artifacts missing for {dirname}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", required=True)
    args = ap.parse_args()
    repo = Path(args.repo).resolve()
    reports = repo / "reports/series"
    triage_path = reports / "V12_RC1_RENDER_TRIAGE.json"
    if not triage_path.exists():
        raise SystemExit("Missing V12_RC1_RENDER_TRIAGE.json")
    triage = json.loads(triage_path.read_text(encoding="utf-8"))
    if triage.get("status") != "PASS" or int(triage.get("confirmed_overfull_candidates",0)) <= 0:
        raise SystemExit("Rendered triage is not ready for repair")

    preamble = repo / "shared/preamble.tex"
    text = preamble.read_text(encoding="utf-8-sig")
    if BEGIN in text or END in text:
        raise SystemExit("v1.2-rc1 layout repair block already exists")
    anchor = "% All volume directories sit two levels below the repository root."
    if anchor not in text:
        raise SystemExit("Shared preamble insertion anchor not found")

    before = {
        "ge20": int(triage.get("overfull_ge_20pt",0)),
        "max": float(triage.get("max_overfull_pt",0)),
        "total": int(triage.get("overfull_boxes_total",0)),
    }
    patched = text.replace(anchor, BLOCK + "\n" + anchor, 1)
    preamble.write_text(patched, encoding="utf-8", newline="\n")

    # Smoke-build all eight volumes before committing the shared policy. The
    # official clean rebuild and full rendered reproof are intentionally Commit 3.
    stats = []
    try:
        for volume, dirname in VOLS:
            build(repo, dirname)
            s = high_log_stats(repo / "books" / dirname / "book.log")
            if s is None:
                raise RuntimeError(f"Missing build log for {volume}")
            if s["blockers"]:
                raise RuntimeError(f"Hard LaTeX finding in {volume}: {s['blockers']}")
            stats.append({"volume": volume, **s})
    except Exception:
        preamble.write_text(text, encoding="utf-8", newline="\n")
        raise

    after = {
        "total": sum(x["total"] for x in stats),
        "ge20": sum(x["ge20"] for x in stats),
        "max": max((x["max"] for x in stats), default=0.0),
    }
    # More flexibility should never worsen the severe warning queue. If it does,
    # restore the preamble and stop before a repair commit is created.
    if after["ge20"] > before["ge20"] or after["max"] > before["max"] + 0.01:
        preamble.write_text(text, encoding="utf-8", newline="\n")
        raise SystemExit(
            f"Layout policy regressed severe warnings: before ge20/max={before['ge20']}/{before['max']}, "
            f"after={after['ge20']}/{after['max']}"
        )

    effect = "IMPROVED" if (after["ge20"] < before["ge20"] or after["max"] < before["max"] - 0.01) else "NONREGRESSING_POLICY"
    summary = {
        "schema": 1,
        "status": "PASS",
        "candidate": "v1.2-rc1",
        "repair_scope": "shared typography line-breaking policy only",
        "changed_source": "shared/preamble.tex",
        "shared_preamble_sha256_after": sha256(preamble),
        "mathematical_chapter_source_changed": False,
        "global_sloppy_enabled": False,
        "math_rescaling_enabled": False,
        "policy": {"tolerance": 2000, "emergencystretch": "3em", "urlmuskip": "0mu plus 2mu"},
        "before": before,
        "smoke_build_after": after,
        "effect": effect,
        "volumes_smoke_built": 8,
        "official_clean_reproof_required": True,
        "human_rendered_proof_required": True,
        "final_release_frozen": False,
        "blocking": [],
    }
    (reports / "V12_RC1_LAYOUT_REPAIR.json").write_text(
        json.dumps(summary, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    md = [
        "# v1.2-rc1 confirmed layout repair",
        "",
        "**Repair smoke test:** PASS",
        "",
        "Only `shared/preamble.tex` is changed. No chapter, problem, solution, example,",
        "or mathematical display is semantically rewritten by this commit.",
        "",
        f"- Severe overfull boxes before: **{before['ge20']}**; smoke-build after: **{after['ge20']}**.",
        f"- Maximum overfull width before: **{before['max']:.5f}pt**; after: **{after['max']:.5f}pt**.",
        f"- Policy effect: **{effect}**.",
        "- `\\sloppy`: **not enabled**.",
        "- Automatic math resizing: **not used**.",
        "",
        "The next commit performs a clean eight-volume rebuild and a full 2999-page rendered reproof.",
        "The final v1.2 release freeze remains separate.",
        "",
    ]
    (reports / "V12_RC1_LAYOUT_REPAIR.md").write_text("\n".join(md), encoding="utf-8")
    print(json.dumps(summary, indent=2, ensure_ascii=False))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
