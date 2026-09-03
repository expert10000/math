#!/usr/bin/env python3
from __future__ import annotations
import argparse,csv,hashlib,json,re
from pathlib import Path

VOLS=[
("I","vol01_linear_algebra",18),
("II","vol02_real_analysis",25),
("III","vol03_fourier_distributions_pde",28),
("IV","vol04_complex_analysis",31),
("V","vol05_commutative_algebra",28),
("VI","vol06_algebraic_geometry",49),
("VII","vol07_differential_geometry",42),
("VIII","vol08_algebraic_topology",35),
]

def rows(path):
    with Path(path).open("r",encoding="utf-8-sig",newline="") as f:
        return list(csv.DictReader(f,delimiter="\t"))

def sha(path):
    h=hashlib.sha256()
    with Path(path).open("rb") as f:
        for b in iter(lambda:f.read(1024*1024),b""):
            h.update(b)
    return h.hexdigest()

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--repo",required=True)
    args=ap.parse_args()
    repo=Path(args.repo).resolve()
    build=rows(repo/"reports/series/BUILD_I_VIII.tsv")
    pdf=rows(repo/"reports/series/PDF_INVENTORY.tsv")
    status=rows(repo/"editorial/CHAPTER_STATUS.tsv")
    blockers=[]

    canon=[r for r in build if r.get("target")=="book.tex" and r.get("kind")=="canonical"]
    if len(canon)!=8:
        blockers.append(f"canonical_build_rows={len(canon)} expected=8")
    for v,dirname,count in VOLS:
        br=next((r for r in canon if r.get("volume")==v),None)
        if not br:
            blockers.append(f"{v}:missing build row")
            continue
        if br.get("status")!="PASS":
            blockers.append(f"{v}:build={br.get('status')}")
        book=repo/"books"/dirname/"book.tex"
        out=repo/"books"/dirname/"book.pdf"
        if not book.exists():
            blockers.append(f"{v}:book.tex missing")
        if not out.exists():
            blockers.append(f"{v}:book.pdf missing")
        else:
            if br.get("sha256") and br.get("sha256") not in ("N/A","-") and sha(out)!=br["sha256"]:
                blockers.append(f"{v}:BUILD_I_VIII PDF hash mismatch")
            try:
                bbytes=int(br.get("bytes") or 0)
                if bbytes and out.stat().st_size!=bbytes:
                    blockers.append(f"{v}:BUILD_I_VIII PDF byte mismatch")
            except ValueError:
                blockers.append(f"{v}:invalid build byte count")
        text=book.read_text(encoding="utf-8-sig") if book.exists() else ""
        includes=len(re.findall(r"(?m)^[ \t]*\\include\{",text))
        if includes!=count:
            blockers.append(f"{v}:includes={includes} expected={count}")
        sr=[r for r in status if r.get("volume")==v]
        if len(sr)!=count:
            blockers.append(f"{v}:status_rows={len(sr)} expected={count}")

        pr=next((r for r in pdf if r.get("volume")==v),None)
        if not pr or pr.get("exists")!="YES":
            blockers.append(f"{v}:PDF inventory missing")
        elif out.exists() and pr.get("sha256")!=sha(out):
            blockers.append(f"{v}:PDF inventory hash mismatch")

    pass_count=sum(r.get("status")=="PASS" for r in canon)
    fail_count=sum(r.get("status")=="FAIL" for r in canon)
    no_count=sum(r.get("status")=="NO_WRAPPER" for r in canon)
    summary={
        "status":"PASS" if not blockers else "FAIL",
        "canonical_build_rows":len(canon),
        "pass":pass_count,
        "fail":fail_count,
        "no_wrapper":no_count,
        "pdf_inventory_rows":len(pdf),
        "blocking":blockers,
    }
    out=repo/"reports/series/SERIES_BUILD_VERIFICATION.json"
    out.write_text(json.dumps(summary,indent=2)+"\n",encoding="utf-8")
    md=[
        "# I–VIII Canonical Build Verification","",
        f"**Result:** {summary['status']}","",
        f"- Canonical build rows: **{len(canon)} / 8**",
        f"- PASS / FAIL / NO_WRAPPER: **{pass_count} / {fail_count} / {no_count}**",
        f"- PDF inventory rows: **{len(pdf)} / 8**","",
        "## Blockers",""
    ]
    md += [f"- {x}" for x in blockers] if blockers else ["None."]
    (repo/"reports/series/SERIES_BUILD_VERIFICATION.md").write_text("\n".join(md)+"\n",encoding="utf-8")
    print(json.dumps(summary,indent=2))
    return 0 if not blockers else 3

if __name__=="__main__":
    raise SystemExit(main())
