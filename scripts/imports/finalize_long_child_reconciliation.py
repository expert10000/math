#!/usr/bin/env python3
from __future__ import annotations
import argparse, csv, hashlib, re, shutil
from pathlib import Path

LINE_RANGE_RE=re.compile(r"L?(\d+)\s*-\s*L?(\d+)")
COMMENT_RE=re.compile(r"(?<!\\)%.*$")
THEORY_RE=re.compile(r"^\s*\\section\*?\{\s*Theory\s+for\s+Problems?\b",re.I)
SOLUTION_RE=re.compile(
    r"^\s*(?:\\noindent\s*)?(?:\\textbf\{\s*)?(?:Solution|Answer|Proof)\s*[.:]?",
    re.I
)

FINAL_TRIM_FAMILIES={"LCR-002","LCR-005"}

def read_tsv(path):
    with path.open("r",encoding="utf-8-sig",newline="") as f:
        r=csv.DictReader(f,delimiter="\t")
        return list(r.fieldnames or []),[dict(x) for x in r]

def write_tsv(path,fields,rows):
    path.parent.mkdir(parents=True,exist_ok=True)
    with path.open("w",encoding="utf-8",newline="") as f:
        w=csv.DictWriter(f,fieldnames=fields,delimiter="\t",lineterminator="\n",extrasaction="ignore")
        w.writeheader()
        for r in rows:
            w.writerow({k:r.get(k,"") for k in fields})

def extend(fields,extras):
    out=list(fields)
    for x in extras:
        if x not in out:out.append(x)
    return out

def parse_range(s):
    m=LINE_RANGE_RE.search(s or "")
    return (int(m.group(1)),int(m.group(2))) if m else None

def split_ids(s):
    return [x for x in (s or "").split(";") if x]

def safe_lines(path):
    for enc in ("utf-8-sig","utf-8","cp1252","latin-1"):
        try:return path.read_text(encoding=enc).splitlines()
        except UnicodeDecodeError:pass
    return path.read_text(encoding="utf-8",errors="replace").splitlines()

def strip_comment(s):return COMMENT_RE.sub("",s)

def normalize_statement(text):
    text=re.sub(r"\\begin\{(?:solution|answer|proofsolution|hint|hints)\}.*?\\end\{(?:solution|answer|proofsolution|hint|hints)\}"," ",text,flags=re.I|re.S)
    text=re.split(r"(?im)^\s*(?:\\noindent\s*)?(?:\\textbf\{)?(?:Solution|Answer|Hint)\}?\s*[:.]",text,maxsplit=1)[0]
    text="\n".join(strip_comment(x) for x in text.splitlines())
    text=re.sub(r"\\label\{[^}]+\}"," ",text)
    text=re.sub(r"\\begin\{(?:problem|exercise|example|question|task|challenge)\*?\}(?:\[[^\]]*\])?"," ",text,flags=re.I)
    text=re.sub(r"\\end\{(?:problem|exercise|example|question|task|challenge)\*?\}"," ",text,flags=re.I)
    text=re.sub(r"\\(?:section|subsection|subsubsection|paragraph)\*?\{\s*(?:Problem|Exercise|Example|Question|Task|Challenge)[^}]*\}"," ",text,flags=re.I)
    text=re.sub(r"^\s*\\item(?:\[[^\]]+\])?\s*","",text,flags=re.I)
    text=re.sub(r"^\s*(?:\\textbf\{)?(?:Problem|Exercise|Example|Question|Task|Challenge)(?:\s+[A-Za-z0-9][A-Za-z0-9.()_\-/]*)?\}?\s*[:.]\s*","",text,flags=re.I)
    return re.sub(r"\s+"," ",text).strip()

def shash(text):
    n=normalize_statement(text)
    return hashlib.sha256(n.encode()).hexdigest() if n else ""

def add_approved_ids(inv):
    ids=set()
    # Earlier source-reviewed safe dispositions.
    p=inv/"LONG_CHILD_REVIEW_DISPOSITIONS.tsv"
    if p.exists():
        _,rows=read_tsv(p)
        for r in rows:
            if r.get("clear_review_flag")=="YES":
                ids.add(r["problem_id"])

    # Earlier high-confidence closure family members.
    p=inv/"LONG_CHILD_HIGH_CONF_CLOSURES.tsv"
    if p.exists():
        _,rows=read_tsv(p)
        for r in rows:
            ids.update(split_ids(r.get("member_problem_ids","")))

    # Final targeted closure family members.
    p=inv/"FINAL_STRUCTURAL_CLOSURES.tsv"
    if p.exists():
        _,rows=read_tsv(p)
        for r in rows:
            ids.update(split_ids(r.get("member_problem_ids","")))
    return ids

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--repo",type=Path,required=True)
    ap.add_argument("--apply",action="store_true")
    args=ap.parse_args()

    repo=args.repo.resolve()
    inv=repo/"imports"/"problem_inventory"
    srcroot=repo/"imports"/"ALL_TEX_AND_FIGURES"/"tex"

    lfields,ledger=read_tsv(inv/"PROBLEM_LEDGER.tsv")
    _,families=read_tsv(inv/"LONG_CHILD_UNRESOLVED_FAMILIES.tsv")
    fam_by={r["long_review_family_id"]:r for r in families}

    current_flags=[r for r in ledger if r.get("structural_review_flag")=="LONG_CHILD_REVIEW"]
    current_ids={r["problem_id"] for r in current_flags}
    approved_ids=add_approved_ids(inv)

    trim_ids=set()
    for fid in FINAL_TRIM_FAMILIES:
        fam=fam_by.get(fid)
        if not fam:
            raise SystemExit(f"Missing family metadata for {fid}")
        trim_ids.update(split_ids(fam.get("member_problem_ids","")) or [fam["representative_problem_id"]])

    stale_close_ids=(current_ids & approved_ids) - trim_ids

    new_fields=extend(lfields,[
        "structural_review_flag",
        "structural_review_disposition",
        "structural_review_rationale",
        "structural_original_line_range",
    ])

    errors=[]
    changes=[]
    shadow=[]

    for r0 in ledger:
        r=dict(r0)
        pid=r.get("problem_id","")

        if pid in stale_close_ids:
            r["structural_review_flag"]=""
            r["structural_review_disposition"]="RECONCILED_PREVIOUSLY_APPROVED_CLOSURE"
            r["structural_review_rationale"]="Current flag reconciled against an earlier approved safe-closure decision."
            changes.append({
                "problem_id":pid,
                "change_type":"CLEAR_STALE_APPROVED_FLAG",
                "source_file":r.get("source_file",""),
                "old_line_range":r.get("source_line_range",""),
                "new_line_range":r.get("source_line_range",""),
                "old_statement_hash":r.get("statement_hash",""),
                "new_statement_hash":r.get("statement_hash",""),
                "status":"OK",
            })

        elif pid in trim_ids and r.get("structural_review_flag")=="LONG_CHILD_REVIEW":
            rr=parse_range(r.get("source_line_range",""))
            src=r.get("source_file","")
            p=srcroot/src
            if not rr or not p.exists():
                errors.append(f"{pid}: missing range/source")
                shadow.append(r); continue
            a,b=rr
            lines=safe_lines(p)

            solution_seen=False
            theory_line=None
            for lineno in range(a,b+1):
                x=strip_comment(lines[lineno-1]).strip()
                if SOLUTION_RE.search(x):
                    solution_seen=True
                if solution_seen and THEORY_RE.search(x):
                    theory_line=lineno
                    break

            if theory_line is None:
                errors.append(f"{pid}: no post-solution Theory for Problems heading found")
                shadow.append(r); continue
            new_b=theory_line-1
            if new_b < a:
                errors.append(f"{pid}: invalid trim end {new_b}")
                shadow.append(r); continue

            old_text="\n".join(lines[a-1:b])
            new_text="\n".join(lines[a-1:new_b])
            old_norm_hash=shash(old_text)
            new_norm_hash=shash(new_text)
            ledger_hash=r.get("statement_hash","")

            if old_norm_hash != new_norm_hash:
                errors.append(f"{pid}: normalized statement changed after trim")
                shadow.append(r); continue
            if ledger_hash and old_norm_hash != ledger_hash:
                # Do not fail if historical scanner hash normalization differs; require equality
                # old-vs-new, which proves the trim preserves the current statement semantics.
                hash_note="LEDGER_HASH_NORMALIZER_DIFFERS"
            else:
                hash_note="LEDGER_HASH_MATCH"

            old_range=r["source_line_range"]
            r["structural_original_line_range"]=old_range
            r["source_line_range"]=f"L{a}-L{new_b}"
            if "source_location" in r:
                r["source_location"]=r["source_line_range"]
            r["structural_review_flag"]=""
            r["structural_review_disposition"]="TRIMMED_POST_SOLUTION_EXPOSITION"
            r["structural_review_rationale"]="Trimmed before post-solution `Theory for Problems ...` exposition; normalized statement hash is unchanged."

            changes.append({
                "problem_id":pid,
                "change_type":"TRIM_POST_SOLUTION_EXPOSITION",
                "source_file":src,
                "old_line_range":old_range,
                "new_line_range":r["source_line_range"],
                "old_statement_hash":ledger_hash,
                "new_statement_hash":ledger_hash,
                "status":hash_note,
            })

        shadow.append(r)

    remaining=[r for r in shadow if r.get("structural_review_flag")=="LONG_CHILD_REVIEW"]

    change_fields=["problem_id","change_type","source_file","old_line_range","new_line_range","old_statement_hash","new_statement_hash","status"]
    write_tsv(inv/"FINAL_LONG_CHILD_RECONCILIATION_CHANGES.tsv",change_fields,changes)
    write_tsv(inv/"PROBLEM_LEDGER_FINAL_LONG_CHILD_SHADOW.tsv",new_fields,shadow)
    write_tsv(
        inv/"FINAL_LONG_CHILD_REMAINING_FLAGS.tsv",
        new_fields,
        remaining,
    )

    trim_changes=[x for x in changes if x["change_type"]=="TRIM_POST_SOLUTION_EXPOSITION"]
    stale_changes=[x for x in changes if x["change_type"]=="CLEAR_STALE_APPROVED_FLAG"]

    summary=[
        "# Final long-child reconciliation","",
        f"- Mode: **{'APPLY' if args.apply else 'DRY RUN'}**",
        f"- LONG_CHILD_REVIEW rows at start: **{len(current_flags)}**",
        f"- Previously approved stale flags cleared: **{len(stale_changes)}**",
        f"- Post-solution exposition rows trimmed: **{len(trim_changes)}**",
        f"- LONG_CHILD_REVIEW rows remaining: **{len(remaining)}**",
        f"- Validation errors: **{len(errors)}**","",
        "The two trim operations are accepted only when the normalized problem statement hash is identical before and after trimming.",
        "No problem IDs, statement hashes, semantic units, or solution links are changed."
    ]
    if errors:
        summary += ["","## Validation errors",""]+[f"- {e}" for e in errors]
    (inv/"FINAL_LONG_CHILD_RECONCILIATION_SUMMARY.md").write_text("\n".join(summary)+"\n",encoding="utf-8")

    if errors:
        print("FINAL LONG-CHILD RECONCILIATION VALIDATION FAILED")
        for e in errors: print(" -",e)
        return 1
    if remaining:
        print("FINAL LONG-CHILD RECONCILIATION INCOMPLETE")
        for r in remaining:
            print(" -",r.get("problem_id"),r.get("source_file"),r.get("source_line_range"))
        return 1

    print(
        f"FINAL LONG-CHILD RECONCILIATION DRY RUN PASSED: start={len(current_flags)} "
        f"stale_closed={len(stale_changes)} trimmed={len(trim_changes)} remaining=0"
    )
    if not args.apply:
        print("No master files changed.")
        return 0

    src=inv/"PROBLEM_LEDGER.tsv"
    snap=inv/"PROBLEM_LEDGER_PRE_FINAL_LONG_CHILD_RECONCILIATION.tsv"
    if not snap.exists():
        shutil.copy2(src,snap)
    write_tsv(inv/"PROBLEM_LEDGER.tsv",new_fields,shadow)

    print(
        f"FINAL LONG-CHILD RECONCILIATION APPLIED: "
        f"stale_closed={len(stale_changes)} trimmed={len(trim_changes)} remaining=0"
    )
    return 0

if __name__=="__main__":
    raise SystemExit(main())
