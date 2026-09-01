#!/usr/bin/env python3
from __future__ import annotations
import argparse, csv, json, re, sys
from collections import Counter, defaultdict
from pathlib import Path

VOLUMES = ("I","II","III","IV","V","VI","VII","VIII")
TEXT_SUFFIXES = {".md",".tsv",".tex",".ps1",".py",".json"}
# Sequences strongly associated with UTF-8 bytes decoded/re-encoded incorrectly.
MOJIBAKE = ("Ã","Â","â€","â€“","â€”","Ä‚","Ă","Äą","Ë","Ĺ","Å","Â¬","Â©","Â¶")

def read_text(p: Path) -> str:
    return p.read_text(encoding="utf-8-sig", errors="replace")

def parse_atlas(p: Path):
    text=read_text(p)
    # Example: 14. **I/14 — Gram–Schmidt and Orthogonal Projection**
    rx=re.compile(r"(?m)^\d+\.\s+\*\*((?:VIII|VII|VI|IV|III|II|V|I)/\d{2})\s+—\s+(.+?)\*\*\s*$")
    rows={}
    for m in rx.finditer(text):
        rows[m.group(1)]=m.group(2).strip()
    return rows

def read_tsv(p: Path):
    with p.open("r",encoding="utf-8-sig",newline="") as f:
        return list(csv.DictReader(f,delimiter="\t"))

def write_tsv(p: Path, rows, fields):
    with p.open("w",encoding="utf-8",newline="") as f:
        w=csv.DictWriter(f,fieldnames=fields,delimiter="\t",lineterminator="\n",extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)

def suspicious(text: str):
    hits=[]
    for token in MOJIBAKE:
        n=text.count(token)
        if n: hits.append((token,n))
    replacement=text.count("\ufffd")
    if replacement: hits.append(("U+FFFD",replacement))
    return hits

def canonical_candidates(repo: Path, code: str):
    roman,num=code.split("/")
    volnum=VOLUMES.index(roman)+1
    books=repo/"books"
    dirs=sorted(books.glob(f"vol{volnum:02d}_*"))
    found=[]
    for vd in dirs:
        found += sorted((vd/"chapters").glob(f"ch{int(num):02d}_*/chapter.tex")) if (vd/"chapters").exists() else []
    return found

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--repo",required=True)
    ap.add_argument("--fix",action="store_true")
    args=ap.parse_args()
    repo=Path(args.repo).resolve()
    atlas_p=repo/"editorial/CONTENT_ATLAS.md"
    status_p=repo/"editorial/CHAPTER_STATUS.tsv"
    if not atlas_p.exists() or not status_p.exists():
        raise SystemExit("CONTENT_ATLAS.md or CHAPTER_STATUS.tsv missing.")

    atlas=parse_atlas(atlas_p)
    status=read_tsv(status_p)
    fields=["volume","chapter_code","chapter_title","status","legacy_source_status",
            "mapped_rule_count","canonical_path","next_action"]
    if not status or any(f not in status[0] for f in fields):
        raise SystemExit("Unexpected CHAPTER_STATUS.tsv schema.")

    before_title_mismatch=[]
    path_findings=[]
    duplicate_codes=[]
    codes=[r["chapter_code"] for r in status]
    cc=Counter(codes)
    duplicate_codes=[c for c,n in cc.items() if n>1]

    repaired=0
    path_repaired=0
    for r in status:
        code=r["chapter_code"]
        if code in atlas and r["chapter_title"] != atlas[code]:
            before_title_mismatch.append({
                "chapter_code":code,
                "status_title":r["chapter_title"],
                "atlas_title":atlas[code],
                "action":"REPAIR_FROM_CONTENT_ATLAS" if args.fix else "REPORT"
            })
            if args.fix:
                r["chapter_title"]=atlas[code]
                repaired+=1

        current=repo/r["canonical_path"] if r["canonical_path"] else None
        exists=bool(current and current.exists())
        cands=canonical_candidates(repo,code)
        action="OK" if exists else "MISSING_PLANNED_PATH"
        resolved=""
        if not exists and len(cands)==1:
            resolved=cands[0].relative_to(repo).as_posix()
            action="REPAIR_TO_UNIQUE_EXISTING_PATH"
            if args.fix:
                r["canonical_path"]=resolved
                path_repaired+=1
        elif not exists and len(cands)>1:
            action="AMBIGUOUS_EXISTING_PATHS"
            resolved=";".join(x.relative_to(repo).as_posix() for x in cands)
        elif exists:
            resolved=r["canonical_path"]
        path_findings.append({
            "volume":r["volume"],"chapter_code":code,"declared_path":r["canonical_path"],
            "path_exists":"YES" if (repo/r["canonical_path"]).exists() else "NO",
            "candidate_count":len(cands),"resolved_path":resolved,"classification":action
        })

    if args.fix:
        write_tsv(status_p,status,fields)

    # Re-read the fixed status for post-fix encoding checks.
    status_text=read_text(status_p)
    status_hits=suspicious(status_text)

    # Encoding scan is intentionally restricted to canonical/editorial trees.
    encoding_rows=[]
    scan_roots=[repo/"editorial",repo/"books"]
    for base in scan_roots:
        if not base.exists(): continue
        for p in sorted(base.rglob("*")):
            if not p.is_file() or p.suffix.lower() not in TEXT_SUFFIXES:
                continue
            # Legacy audit snapshots can preserve original broken text; distinguish them.
            rel=p.relative_to(repo).as_posix()
            text=read_text(p)
            hits=suspicious(text)
            if hits:
                canonical = (
                    rel.startswith("editorial/") or
                    "/chapters/" in rel or
                    rel.endswith("/book.tex") or
                    rel.endswith("/README.md") or
                    rel.startswith("books/SERIES")
                )
                encoding_rows.append({
                    "path":rel,
                    "scope":"CANONICAL_OR_EDITORIAL" if canonical else "SUPPORT_OR_PROVENANCE",
                    "hit_count":sum(n for _,n in hits),
                    "tokens":",".join(f"{tok}:{n}" for tok,n in hits),
                    "classification":"REVIEW_ENCODING"
                })

    # Status accounting.
    volume_stats=[]
    for v in VOLUMES:
        rows=[r for r in status if r["volume"]==v]
        st=Counter(r["status"] for r in rows)
        nx=Counter(r["next_action"] for r in rows)
        existing=sum(1 for r in rows if (repo/r["canonical_path"]).exists())
        volume_stats.append({
            "volume":v,"chapters":len(rows),"existing_canonical_paths":existing,
            "planned":st.get("PLANNED",0),"drafted":st.get("DRAFTED",0),
            "frozen":st.get("FROZEN",0),"complete_actions":nx.get("COMPLETE",0),
            "freeze_ready":nx.get("FREEZE_READY",0),
        })

    reports=repo/"reports/series"
    reports.mkdir(parents=True,exist_ok=True)
    write_tsv(reports/"GLOBAL_I_VIII_STATUS_AUDIT.tsv",volume_stats,
              ["volume","chapters","existing_canonical_paths","planned","drafted","frozen","complete_actions","freeze_ready"])
    write_tsv(reports/"GLOBAL_CANONICAL_PATH_AUDIT.tsv",path_findings,
              ["volume","chapter_code","declared_path","path_exists","candidate_count","resolved_path","classification"])
    write_tsv(reports/"GLOBAL_ENCODING_AUDIT.tsv",encoding_rows,
              ["path","scope","hit_count","tokens","classification"])
    write_tsv(reports/"GLOBAL_STATUS_TITLE_REPAIRS.tsv",before_title_mismatch,
              ["chapter_code","status_title","atlas_title","action"])

    atlas_missing=sorted(set(codes)-set(atlas))
    status_missing=sorted(set(atlas)-set(codes))
    ambiguous=[r for r in path_findings if r["classification"]=="AMBIGUOUS_EXISTING_PATHS"]
    canonical_encoding=[r for r in encoding_rows if r["scope"]=="CANONICAL_OR_EDITORIAL"]

    md=[
        "# Global I-VIII Status, Encoding, and Canonical-Path Audit","",
        f"**Mode:** {'repair + audit' if args.fix else 'audit only'}","",
        "## Architecture integrity","",
        f"- CONTENT_ATLAS chapter codes: **{len(atlas)}**",
        f"- CHAPTER_STATUS rows: **{len(status)}**",
        f"- Duplicate status codes: **{len(duplicate_codes)}**",
        f"- Status codes missing from atlas: **{len(atlas_missing)}**",
        f"- Atlas codes missing from status: **{len(status_missing)}**",
        "",
        "## Repairs performed","",
        f"- Chapter titles restored from CONTENT_ATLAS: **{repaired}**",
        f"- Stale canonical paths repaired to unique existing chapter paths: **{path_repaired}**",
        f"- Remaining suspicious encoding tokens in CHAPTER_STATUS.tsv: **{sum(n for _,n in status_hits)}**",
        "",
        "## Canonical-path state","",
    ]
    for r in volume_stats:
        md.append(
            f"- Volume {r['volume']}: {r['chapters']} chapters; "
            f"{r['existing_canonical_paths']} canonical chapter paths currently exist; "
            f"{r['planned']} planned / {r['drafted']} drafted / {r['frozen']} frozen."
        )
    md += [
        "",
        "Missing paths are not automatically blocking: Volumes whose reconstruction has not begun "
        "are expected to have planned canonical destinations without files.",
        "",
        "## Encoding scan","",
        f"- Files with suspicious byte-decoding signatures: **{len(encoding_rows)}**",
        f"- Canonical/editorial files among them: **{len(canonical_encoding)}**",
        "",
        "See `GLOBAL_ENCODING_AUDIT.tsv` for exact files and tokens.",
        "",
        "## Blocking structural findings","",
    ]
    blocking=[]
    if duplicate_codes: blocking.append("Duplicate chapter codes: "+", ".join(duplicate_codes))
    if atlas_missing: blocking.append("Status codes absent from CONTENT_ATLAS: "+", ".join(atlas_missing[:20]))
    if status_missing: blocking.append("CONTENT_ATLAS codes absent from status: "+", ".join(status_missing[:20]))
    if ambiguous: blocking.append(f"Ambiguous existing canonical paths: {len(ambiguous)}")
    if status_hits: blocking.append("CHAPTER_STATUS.tsv still contains suspicious encoding signatures after repair.")
    md += [("- "+x) for x in blocking] if blocking else ["None."]
    (reports/"GLOBAL_I_VIII_AUDIT.md").write_text("\n".join(md).rstrip()+"\n",encoding="utf-8")

    summary={
        "status":"PASS" if not blocking else "FAIL",
        "atlas_chapters":len(atlas),"status_rows":len(status),
        "title_repairs":repaired,"path_repairs":path_repaired,
        "encoding_files":len(encoding_rows),"canonical_encoding_files":len(canonical_encoding),
        "blocking":blocking,
    }
    (reports/"GLOBAL_I_VIII_AUDIT.json").write_text(json.dumps(summary,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    print(json.dumps(summary,indent=2,ensure_ascii=False))
    return 0 if not blocking else 2

if __name__=="__main__":
    raise SystemExit(main())
