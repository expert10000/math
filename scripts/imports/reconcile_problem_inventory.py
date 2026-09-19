#!/usr/bin/env python3
"""Reconcile exact duplicate imported problems and detached/orphan solutions.

This is a provenance/audit pass. It does not edit canonical book content.

Inputs (from the structural discovery pass):
  imports/problem_inventory/PROBLEM_LEDGER.tsv
  imports/problem_inventory/RAW_PROBLEM_ITEMS.tsv
  imports/problem_inventory/PROBLEM_SOLUTION_LINKS.tsv
  imports/problem_inventory/DUPLICATE_GROUPS.tsv
  imports/problem_inventory/DETACHED_SOLUTION_ITEMS.tsv
  imports/problem_inventory/SOURCE_FILES.tsv
  imports/ALL_TEX_AND_FIGURES/tex/**/*.tex

Outputs/updates:
  imports/problem_inventory/PROBLEM_LEDGER.tsv               (recomputed solution fields + audit columns)
  imports/problem_inventory/PROBLEM_SOLUTION_LINKS.tsv       (explicit reconciliation status/method)
  imports/problem_inventory/DUPLICATE_GROUPS.tsv              (representatives + aggregate solutions)
  imports/problem_inventory/EXACT_DUPLICATE_COLLAPSE.tsv
  imports/problem_inventory/DETACHED_SOLUTION_RECONCILIATION.tsv
  imports/problem_inventory/NUMBERING_MISMATCHES.tsv
  imports/problem_inventory/SOLUTION_RECONCILIATION.tsv
  imports/problem_inventory/REMAINING_ORPHANS.tsv
  imports/problem_inventory/remaining_orphans.md
  imports/problem_inventory/RECONCILIATION_SUMMARY.md

Conservative policy:
- Existing same-file links are retained.
- Exact statement duplicates are collapsed only semantically: no source row is deleted.
- Companion-file links are applied only when a unique high-confidence candidate exists.
- Numbering mismatches are detected and reported; ambiguous mappings are never guessed.
- Solution availability may propagate across exact-statement duplicate members, while the
  original solution source ID remains unchanged.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import re
import shutil
from collections import Counter, defaultdict
from dataclasses import dataclass
from difflib import SequenceMatcher
from pathlib import Path
from typing import Iterable

LINE_RANGE_RE = re.compile(r"L?(\d+)\s*-\s*L?(\d+)")
COPY_SUFFIX_RE = re.compile(r"\s*\(\d+\)\s*$")
TOKEN_RE = re.compile(r"[A-Za-z]{3,}|\\[A-Za-z]+|\d+(?:\.\d+)+")
STOPWORDS = {
    "the","and","for","that","with","from","this","show","prove","let","then","such","there","where",
    "which","have","has","into","all","are","was","were","will","can","if","of","to","in","on","is",
    "a","an","be","or","as","by","at","it","we","you","solution","answer","exercise","problem","example",
    "part","section","subsection","exact","statement","hint"
}

TYPE_RANK = {
    "PROBLEM": 8, "PROBLEM_ITEM": 7, "CHALLENGE": 7, "EXERCISE": 6, "EXERCISE_ITEM": 6,
    "QUESTION": 5, "TASK": 5, "WORKED_EXAMPLE": 4, "PROOF_EXERCISE_CANDIDATE": 1,
}
COLLECTION_RANK = {"MATH_ALLS-3": 3, "MATH-ALLS-2": 2, "Downloads": 1}


def read_tsv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    if not path.exists():
        raise SystemExit(f"Required input missing: {path}")
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        r = csv.DictReader(f, delimiter="\t")
        return list(r.fieldnames or []), [dict(x) for x in r]


def write_tsv(path: Path, fields: list[str], rows: Iterable[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, delimiter="\t", lineterminator="\n", extrasaction="ignore")
        w.writeheader()
        for row in rows:
            w.writerow({k: row.get(k, "") for k in fields})


def extend_fields(fields: list[str], extra: Iterable[str]) -> list[str]:
    out = list(fields)
    for x in extra:
        if x not in out:
            out.append(x)
    return out


def parse_range(s: str) -> tuple[int, int] | None:
    m = LINE_RANGE_RE.search(s or "")
    return (int(m.group(1)), int(m.group(2))) if m else None


def safe_read(path: Path) -> list[str]:
    for enc in ("utf-8-sig", "utf-8", "cp1252", "latin-1"):
        try:
            return path.read_text(encoding=enc).splitlines()
        except UnicodeDecodeError:
            continue
    return path.read_text(encoding="utf-8", errors="replace").splitlines()


def extract_range(source_root: Path, rel: str, rng: str) -> str:
    p = source_root / rel
    rr = parse_range(rng)
    if not p.exists() or not rr:
        return ""
    lines = safe_read(p)
    a, b = rr
    a = max(1, a); b = min(len(lines), b)
    return "\n".join(lines[a-1:b]) if a <= b else ""


def strip_tex_for_tokens(text: str) -> set[str]:
    text = re.sub(r"(?<!\\)%.*$", " ", text, flags=re.M)
    text = re.sub(r"\\(?:begin|end)\{[^}]+\}", " ", text)
    text = re.sub(r"[{}\[\]$^_&~]", " ", text)
    toks = {t.lower() for t in TOKEN_RE.findall(text)}
    return {t for t in toks if t not in STOPWORDS and len(t) >= 3}


def token_similarity(a: str, b: str) -> float:
    A, B = strip_tex_for_tokens(a), strip_tex_for_tokens(b)
    if not A or not B:
        return 0.0
    inter = len(A & B)
    return inter / max(1, min(len(A), len(B)))


def norm_number(s: str) -> str:
    return re.sub(r"\s+", "", (s or "").strip().lower())


def numeric_tail(s: str) -> int | None:
    m = re.search(r"(\d+)$", norm_number(s))
    return int(m.group(1)) if m else None


def clean_stem(rel: str) -> str:
    stem = Path(rel).stem.lower().replace("_", " ").replace("-", " ")
    stem = COPY_SUFFIX_RE.sub("", stem)
    stem = re.sub(r"\b(solutions?|answers?|answerkey|answer key|worked solutions?|hints?)\b", " ", stem)
    stem = re.sub(r"\b(full|merged|corrected|append|appendix|final|all|v\d+)\b", " ", stem)
    stem = re.sub(r"\s+", " ", stem).strip()
    return stem


def file_similarity(a: str, b: str) -> float:
    sa, sb = clean_stem(a), clean_stem(b)
    if not sa or not sb:
        return 0.0
    if sa == sb:
        return 1.0
    return SequenceMatcher(None, sa, sb).ratio()


def choose_representative(group: list[dict[str,str]], raw_by_id: dict[str,dict[str,str]]) -> str:
    # Technical representative only; all source rows remain. Prefer actual problem/exercise,
    # richer local metadata, then newer consolidated collection, finally stable problem_id.
    def score(r: dict[str,str]):
        raw = raw_by_id.get(r["problem_id"], {})
        conf = {"HIGH":3,"MEDIUM":2,"LOW":1}.get(raw.get("confidence", ""), 0)
        richness = (1 if r.get("has_solution") == "YES" else 0) + (1 if r.get("has_hint") == "YES" else 0) + (1 if r.get("has_figures") == "YES" else 0)
        return (
            TYPE_RANK.get(r.get("problem_type", ""), 0),
            richness,
            conf,
            COLLECTION_RANK.get(r.get("source_collection", ""), 0),
            # reverse lexical handled below by final min tie-break outside score
        )
    best_score = max(score(r) for r in group)
    ids = sorted(r["problem_id"] for r in group if score(r) == best_score)
    return ids[0]


@dataclass
class CandidateScore:
    problem_id: str
    score: float
    number_match: bool
    family_similarity: float
    token_similarity: float
    same_collection: bool
    duplicate_statement_bonus: bool




def choose_representative_reconciled(group: list[dict[str,str]], raw_by_id: dict[str,dict[str,str]],
                                     solution_links_by_problem: dict[str,list[str]],
                                     hint_links_by_problem: dict[str,list[str]]) -> str:
    def score(r: dict[str,str]):
        raw = raw_by_id.get(r["problem_id"], {})
        conf = {"HIGH":3,"MEDIUM":2,"LOW":1}.get(raw.get("confidence", ""), 0)
        pid = r["problem_id"]
        direct_solution = 1 if solution_links_by_problem.get(pid) else 0
        direct_hint = 1 if hint_links_by_problem.get(pid) else 0
        figures = 1 if r.get("has_figures") == "YES" else 0
        return (
            direct_solution, direct_hint, TYPE_RANK.get(r.get("problem_type", ""), 0),
            figures, conf, COLLECTION_RANK.get(r.get("source_collection", ""), 0)
        )
    best = max(score(r) for r in group)
    return sorted(r["problem_id"] for r in group if score(r) == best)[0]

def build_candidate_scores(sol: dict[str,str], ledger: list[dict[str,str]], source_root: Path,
                           statement_text: dict[str,str], duplicate_solution_hashes: set[str]) -> list[CandidateScore]:
    sfile = sol.get("solution_source_file", "")
    snum = norm_number(sol.get("source_problem_number", ""))
    stext = extract_range(source_root, sfile, sol.get("solution_line_range", ""))
    scol = sol.get("source_id", "").split("-")[1] if sol.get("source_id", "").startswith("IMP-") else ""
    out: list[CandidateScore] = []
    for r in ledger:
        # Never link a solution block back into the exact same physical line range by accident.
        if r.get("source_file") == sfile and not snum:
            continue
        rnum = norm_number(r.get("source_problem_number", ""))
        nmatch = bool(snum and rnum and snum == rnum)
        fsim = file_similarity(sfile, r.get("source_file", ""))
        tsim = token_similarity(stext, statement_text.get(r["problem_id"], ""))
        same_col = r.get("source_collection", "") in {"Downloads","MATH-ALLS-2","MATH_ALLS-3"} and (
            ("-DL-" in sol.get("source_id", "") and r.get("source_collection") == "Downloads") or
            ("-M2-" in sol.get("source_id", "") and r.get("source_collection") == "MATH-ALLS-2") or
            ("-M3-" in sol.get("source_id", "") and r.get("source_collection") == "MATH_ALLS-3")
        )
        dupbonus = r.get("statement_hash", "") in duplicate_solution_hashes
        score = 0.0
        if nmatch: score += 55
        if fsim == 1.0: score += 35
        elif fsim >= .88: score += 26
        elif fsim >= .72: score += 14
        elif fsim >= .55: score += 6
        score += min(25.0, tsim * 25.0)
        if same_col: score += 3
        if dupbonus: score += 4
        # Numbered orphan solutions are only considered against same-number candidates unless
        # this is a very strong companion/text match; mismatches are separately reported.
        if snum and not nmatch and not (fsim >= .88 and tsim >= .40):
            continue
        if score >= 25:
            out.append(CandidateScore(r["problem_id"], score, nmatch, fsim, tsim, same_col, dupbonus))
    return sorted(out, key=lambda x: (-x.score, x.problem_id))


def auto_link_decision(scores: list[CandidateScore], ledger_by_id: dict[str,dict[str,str]]) -> tuple[str,str,str,str]:
    """Return problem_id, method, confidence, candidate_ids."""
    if not scores:
        return "", "NO_CANDIDATE", "NONE", ""
    top = scores[0]
    cand = ";".join(x.problem_id for x in scores[:8])
    margin = top.score - (scores[1].score if len(scores) > 1 else 0)
    # Strict automatic rules: exact number + exact/near companion family, or exact number
    # + strong mathematical token overlap. Require uniqueness/margin.
    # If the only ambiguity is between exact-statement duplicates, linking to the
    # top provenance row is semantically safe because solution availability will
    # propagate to the whole duplicate group.
    near = [x for x in scores if top.score - x.score <= 10]
    near_hashes = {ledger_by_id.get(x.problem_id, {}).get("statement_hash", "") for x in near}
    near_hashes.discard("")
    if top.number_match and top.family_similarity >= .88 and top.score >= 78 and len(near) > 1 and len(near_hashes) == 1:
        return top.problem_id, "COMPANION_EXACT_DUPLICATE_EQUIVALENCE", "HIGH", cand
    if top.number_match and top.family_similarity >= .88 and top.score >= 82 and margin >= 10:
        return top.problem_id, "COMPANION_NUMBER_FAMILY", "HIGH", cand
    if top.number_match and top.token_similarity >= .55 and top.score >= 72 and margin >= 12:
        return top.problem_id, "NUMBER_TEXT_FINGERPRINT", "HIGH", cand
    if top.number_match and top.family_similarity == 1.0 and len(scores) == 1:
        return top.problem_id, "COMPANION_EXACT_FAMILY", "HIGH", cand
    return "", "AMBIGUOUS_CANDIDATES", "REVIEW", cand


def detect_numbering_mismatches(
    orphan_solutions: list[dict[str,str]],
    ledger: list[dict[str,str]],
    source_sha_by_file: dict[str,str],
) -> list[dict[str,object]]:
    """Detect genuine cross-file companion numbering shifts.

    Exact file copies and self-pairs are excluded: those belong to source-duplicate
    reconciliation, not numbering-mismatch review. Exact-copy solution/candidate
    paths are then collapsed into one semantic mismatch row while preserving all
    equivalent paths as provenance.
    """
    sols_by_file: dict[str,list[dict[str,str]]] = defaultdict(list)
    probs_by_file: dict[str,list[dict[str,str]]] = defaultdict(list)
    for s in orphan_solutions:
        if numeric_tail(s.get("source_problem_number", "")) is not None:
            sf = s.get("solution_source_file", "")
            if sf:
                sols_by_file[sf].append(s)
    for r in ledger:
        if numeric_tail(r.get("source_problem_number", "")) is not None:
            pf = r.get("source_file", "")
            if pf:
                probs_by_file[pf].append(r)

    detected: list[dict[str,object]] = []
    for sf, sols in sorted(sols_by_file.items()):
        s_nums = [numeric_tail(s.get("source_problem_number", "")) for s in sols]
        s_nums = [x for x in s_nums if x is not None]
        if len(s_nums) < 2:
            continue
        candidates = []
        ssha = source_sha_by_file.get(sf, "")
        for pf, probs in probs_by_file.items():
            # A file cannot be its own companion; byte-identical copies are source
            # duplicates and must never be reported as numbering mismatches.
            if pf == sf:
                continue
            psha = source_sha_by_file.get(pf, "")
            if ssha and psha and ssha == psha:
                continue
            sim = file_similarity(sf, pf)
            if sim < .60:
                continue
            p_nums = [numeric_tail(r.get("source_problem_number", "")) for r in probs]
            p_nums = [x for x in p_nums if x is not None]
            if len(p_nums) < 2:
                continue
            n = min(len(s_nums), len(p_nums))
            diffs = [s_nums[i] - p_nums[i] for i in range(n)]
            offset, support = Counter(diffs).most_common(1)[0]
            ratio = support / n
            if offset != 0 and support >= 2 and ratio >= .75:
                candidates.append((sim, support, ratio, offset, pf, n))
        if candidates:
            sim, support, ratio, offset, pf, n = max(
                candidates, key=lambda x:(x[0],x[1],x[2],-abs(x[3]),x[4])
            )
            detected.append({
                "solution_source_file": sf,
                "candidate_problem_file": pf,
                "file_similarity": f"{sim:.3f}",
                "sequence_pairs_checked": n,
                "constant_number_offset": offset,
                "support_count": support,
                "support_ratio": f"{ratio:.3f}",
            })

    # Collapse reports that differ only because the same source bytes exist in more
    # than one import collection. Preserve all paths so editorial provenance is not lost.
    grouped: dict[tuple[str,str,int], list[dict[str,object]]] = defaultdict(list)
    for row in detected:
        sf = str(row["solution_source_file"]); pf = str(row["candidate_problem_file"])
        skey = source_sha_by_file.get(sf, "") or f"PATH:{sf}"
        pkey = source_sha_by_file.get(pf, "") or f"PATH:{pf}"
        key = (skey, pkey, int(row["constant_number_offset"]))
        grouped[key].append(row)

    # Expand each semantic group to every exact-copy path known in SOURCE_FILES,
    # even when tie-breaking selected only one of those copies as the best candidate.
    solution_files_by_sha: dict[str,set[str]] = defaultdict(set)
    problem_files_by_sha: dict[str,set[str]] = defaultdict(set)
    for path in sols_by_file:
        key = source_sha_by_file.get(path, "") or f"PATH:{path}"
        solution_files_by_sha[key].add(path)
    for path in probs_by_file:
        key = source_sha_by_file.get(path, "") or f"PATH:{path}"
        problem_files_by_sha[key].add(path)

    rows: list[dict[str,object]] = []
    for idx, (key, members) in enumerate(sorted(grouped.items(), key=lambda kv: (kv[1][0]["solution_source_file"], kv[1][0]["candidate_problem_file"])), 1):
        skey, pkey, _offset = key
        solution_files = sorted(solution_files_by_sha.get(skey, {str(x["solution_source_file"]) for x in members}))
        problem_files = sorted(problem_files_by_sha.get(pkey, {str(x["candidate_problem_file"]) for x in members}))
        best = max(members, key=lambda x:(float(x["file_similarity"]), int(x["support_count"]), float(x["support_ratio"])))
        rows.append({
            "mismatch_group": f"NUMSHIFT-{idx:04d}",
            "solution_source_file": solution_files[0],
            "equivalent_solution_source_files": ";".join(solution_files),
            "candidate_problem_file": problem_files[0],
            "equivalent_candidate_problem_files": ";".join(problem_files),
            "file_similarity": best["file_similarity"],
            "sequence_pairs_checked": best["sequence_pairs_checked"],
            "constant_number_offset": best["constant_number_offset"],
            "support_count": best["support_count"],
            "support_ratio": best["support_ratio"],
            "status": "DETECTED_NOT_AUTO_APPLIED",
            "notes": "Cross-file companion numbering shift; exact file copies/self-pairs excluded. Requires editorial confirmation before relinking.",
        })
    return rows


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--repo", type=Path, default=Path.cwd())
    ap.add_argument("--refresh-baseline", action="store_true", help="Replace stored structural baseline snapshots from current ledger/link files before reconciling")
    args = ap.parse_args()
    repo = args.repo.resolve()
    inv = repo / "imports" / "problem_inventory"
    source_root = repo / "imports" / "ALL_TEX_AND_FIGURES" / "tex"

    # Freeze the structural inputs on first reconciliation so reruns remain idempotent.
    # Use --refresh-baseline only after intentionally rerunning structural discovery on a changed corpus.
    structural_ledger = inv / "PROBLEM_LEDGER_STRUCTURAL_BASELINE.tsv"
    structural_links = inv / "PROBLEM_SOLUTION_LINKS_STRUCTURAL_BASELINE.tsv"
    current_ledger = inv / "PROBLEM_LEDGER.tsv"
    current_links = inv / "PROBLEM_SOLUTION_LINKS.tsv"
    if args.refresh_baseline or not structural_ledger.exists():
        shutil.copy2(current_ledger, structural_ledger)
    if args.refresh_baseline or not structural_links.exists():
        shutil.copy2(current_links, structural_links)

    ledger_fields, ledger = read_tsv(structural_ledger)
    raw_fields, raw = read_tsv(inv / "RAW_PROBLEM_ITEMS.tsv")
    link_fields, links = read_tsv(structural_links)
    dup_fields, old_dups = read_tsv(inv / "DUPLICATE_GROUPS.tsv")
    detached_fields, detached = read_tsv(inv / "DETACHED_SOLUTION_ITEMS.tsv")
    _sf_fields, _sources = read_tsv(inv / "SOURCE_FILES.tsv")
    source_sha_by_file = {r.get("source_file", ""): r.get("sha256", "") for r in _sources if r.get("source_file")}

    if not source_root.exists():
        raise SystemExit(f"Source root missing: {source_root}")

    ledger_by_id = {r["problem_id"]: r for r in ledger}
    raw_by_id = {r["problem_id"]: r for r in raw}

    # Cache statement source text for conservative content similarity.
    statement_text = {
        r["problem_id"]: extract_range(source_root, r.get("source_file", ""), r.get("source_line_range", ""))
        for r in ledger
    }

    # ----- 1. Exact duplicate semantic collapse -----
    groups: dict[str,list[dict[str,str]]] = defaultdict(list)
    for r in ledger:
        h = r.get("statement_hash", "")
        if h: groups[h].append(r)

    hash_to_gid: dict[str,str] = {}
    collapse_rows: list[dict[str,object]] = []
    gid_counter = 0
    representative_by_hash: dict[str,str] = {}
    duplicate_role_by_problem: dict[str,str] = {}
    for h in sorted(groups):
        members = groups[h]
        if len(members) < 2:
            continue
        gid_counter += 1
        gid = f"DUP-{gid_counter:05d}"
        hash_to_gid[h] = gid
        rep = choose_representative(members, raw_by_id)
        representative_by_hash[h] = rep
        for r in members:
            duplicate_role_by_problem[r["problem_id"]] = "REPRESENTATIVE" if r["problem_id"] == rep else "EXACT_DUPLICATE_MEMBER"
            r["duplicate_group"] = gid
        collapse_rows.append({
            "duplicate_group": gid,
            "statement_hash": h,
            "member_count": len(members),
            "representative_problem_id": rep,
            "member_problem_ids": ";".join(sorted(r["problem_id"] for r in members)),
            "source_collections": ";".join(sorted({r.get("source_collection","") for r in members})),
            "source_files": ";".join(sorted({r.get("source_file","") for r in members})),
            "semantic_unit_status": "EXACT_STATEMENT_EQUIVALENCE",
        })

    # Keep singletons explicit as semantic units in ledger, but don't add 3000+ singleton rows to collapse table.

    # Existing trustworthy links first.
    solution_links_by_problem: dict[str,list[str]] = defaultdict(list)
    hint_links_by_problem: dict[str,list[str]] = defaultdict(list)
    for s in links:
        pid = s.get("linked_problem_id", "")
        if pid in ledger_by_id:
            if s.get("solution_kind") == "SOLUTION": solution_links_by_problem[pid].append(s["solution_id"])
            if s.get("solution_kind") == "HINT": hint_links_by_problem[pid].append(s["solution_id"])

    # Statement hashes already known to have a trusted solution somewhere in the group.
    duplicate_solution_hashes: set[str] = set()
    for r in ledger:
        if solution_links_by_problem.get(r["problem_id"]):
            duplicate_solution_hashes.add(r.get("statement_hash", ""))

    # Detect likely numbering-shift companion pairs before auto-linking.  This
    # prevents a shifted solution sequence from being falsely linked merely because
    # one number happens to coincide.
    pre_orphans = [s for s in links if not s.get("linked_problem_id")]
    numbering_rows = detect_numbering_mismatches(pre_orphans, ledger, source_sha_by_file)
    mismatch_files: set[str] = set()
    for r in numbering_rows:
        mismatch_files.add(str(r["solution_source_file"]))
        mismatch_files.update(x for x in str(r.get("equivalent_solution_source_files", "")).split(";") if x)

    # ----- 2/3. Detached + orphan solution reconciliation -----
    solution_recon: list[dict[str,object]] = []
    original_link_by_solution = {s["solution_id"]: s.get("linked_problem_id", "") for s in links}
    auto_linked = 0
    ambiguous = 0
    no_candidate = 0

    for s in links:
        old = s.get("linked_problem_id", "")
        if old in ledger_by_id:
            s["reconciliation_status"] = "RESOLVED_EXISTING_LINK"
            s["reconciliation_method"] = "STRUCTURAL_SAME_FILE"
            s["reconciliation_confidence"] = "HIGH"
            s["candidate_problem_ids"] = old
            solution_recon.append({
                "solution_id": s["solution_id"], "solution_kind": s.get("solution_kind", ""),
                "solution_source_file": s.get("solution_source_file", ""), "source_problem_number": s.get("source_problem_number", ""),
                "old_linked_problem_id": old, "new_linked_problem_id": old,
                "reconciliation_status": s["reconciliation_status"], "reconciliation_method": s["reconciliation_method"],
                "confidence": "HIGH", "candidate_problem_ids": old, "notes": "Existing structural link retained.",
            })
            continue

        if s.get("solution_source_file") in mismatch_files:
            scores = build_candidate_scores(s, ledger, source_root, statement_text, duplicate_solution_hashes)
            cand = ";".join(x.problem_id for x in scores[:8])
            pid, method, conf = "", "NUMBERING_MISMATCH_DETECTED", "REVIEW"
        else:
            scores = build_candidate_scores(s, ledger, source_root, statement_text, duplicate_solution_hashes)
            pid, method, conf, cand = auto_link_decision(scores, ledger_by_id)
        if pid:
            s["linked_problem_id"] = pid
            s["link_status"] = "LINKED_COMPANION_FILE"
            s["reconciliation_status"] = "RESOLVED_AUTO"
            s["reconciliation_method"] = method
            s["reconciliation_confidence"] = conf
            s["candidate_problem_ids"] = cand
            auto_linked += 1
        else:
            s["linked_problem_id"] = ""
            if method == "NUMBERING_MISMATCH_DETECTED":
                s["link_status"] = "UNRESOLVED_NUMBERING_MISMATCH"
            else:
                s["link_status"] = "UNRESOLVED_AMBIGUOUS" if method == "AMBIGUOUS_CANDIDATES" else "UNRESOLVED_NO_CANDIDATE"
            s["reconciliation_status"] = s["link_status"]
            s["reconciliation_method"] = method
            s["reconciliation_confidence"] = conf
            s["candidate_problem_ids"] = cand
            if method == "AMBIGUOUS_CANDIDATES": ambiguous += 1
            elif method != "NUMBERING_MISMATCH_DETECTED": no_candidate += 1
        solution_recon.append({
            "solution_id": s["solution_id"], "solution_kind": s.get("solution_kind", ""),
            "solution_source_file": s.get("solution_source_file", ""), "source_problem_number": s.get("source_problem_number", ""),
            "old_linked_problem_id": old, "new_linked_problem_id": s.get("linked_problem_id", ""),
            "reconciliation_status": s["reconciliation_status"], "reconciliation_method": s["reconciliation_method"],
            "confidence": s["reconciliation_confidence"], "candidate_problem_ids": s["candidate_problem_ids"],
            "notes": "Auto-link applied only under strict unique companion/number/content rules." if pid else "No automatic guess applied.",
        })

    # Rebuild direct link maps after reconciliation.
    solution_links_by_problem.clear(); hint_links_by_problem.clear()
    for s in links:
        pid = s.get("linked_problem_id", "")
        if pid not in ledger_by_id: continue
        if s.get("solution_kind") == "SOLUTION": solution_links_by_problem[pid].append(s["solution_id"])
        elif s.get("solution_kind") == "HINT": hint_links_by_problem[pid].append(s["solution_id"])

    # Re-select technical representatives now that companion links are known.
    # Prefer a member with direct solution provenance, then actual problem/exercise
    # types and richer source metadata. No source row is deleted.
    for h, members in groups.items():
        if len(members) < 2:
            continue
        rep = choose_representative_reconciled(members, raw_by_id, solution_links_by_problem, hint_links_by_problem)
        representative_by_hash[h] = rep
        for r in members:
            duplicate_role_by_problem[r["problem_id"]] = "REPRESENTATIVE" if r["problem_id"] == rep else "EXACT_DUPLICATE_MEMBER"
    for row in collapse_rows:
        h = str(row["statement_hash"])
        row["representative_problem_id"] = representative_by_hash[h]

    # Aggregate exact-duplicate solution/hint provenance and propagate availability.
    sols_by_hash: dict[str,set[str]] = defaultdict(set)
    hints_by_hash: dict[str,set[str]] = defaultdict(set)
    solution_source_members_by_hash: dict[str,set[str]] = defaultdict(set)
    for r in ledger:
        h = r.get("statement_hash", "")
        if not h: continue
        if solution_links_by_problem.get(r["problem_id"]):
            sols_by_hash[h].update(solution_links_by_problem[r["problem_id"]])
            solution_source_members_by_hash[h].add(r["problem_id"])
        if hint_links_by_problem.get(r["problem_id"]):
            hints_by_hash[h].update(hint_links_by_problem[r["problem_id"]])

    # ----- 4. Numbering mismatches were detected before auto-linking -----
    for s in links:
        if not s.get("linked_problem_id") and s.get("solution_source_file") in mismatch_files:
            s["reconciliation_status"] = "UNRESOLVED_NUMBERING_MISMATCH"
            s["link_status"] = "UNRESOLVED_NUMBERING_MISMATCH"
            for rr in solution_recon:
                if rr["solution_id"] == s["solution_id"]:
                    rr["reconciliation_status"] = "UNRESOLVED_NUMBERING_MISMATCH"
                    rr["notes"] = "Likely companion numbering shift detected; not auto-applied. See NUMBERING_MISMATCHES.tsv."
                    break

    # ----- 5. Recompute ledger solution/hint fields -----
    ledger_extra = [
        "representative_problem_id", "duplicate_role", "local_solution_ids", "propagated_solution_ids",
        "solution_link_status", "reconciliation_status"
    ]
    ledger_fields = extend_fields(ledger_fields, ledger_extra)
    for r in ledger:
        pid = r["problem_id"]; h = r.get("statement_hash", "")
        local_sols = sorted(set(solution_links_by_problem.get(pid, [])))
        group_sols = sorted(sols_by_hash.get(h, set())) if h else []
        propagated = [x for x in group_sols if x not in local_sols]
        local_hints = sorted(set(hint_links_by_problem.get(pid, [])))
        group_hints = sorted(hints_by_hash.get(h, set())) if h else []
        all_sols = local_sols + propagated
        r["has_solution"] = "YES" if all_sols else "NO"
        r["solution_id"] = ";".join(all_sols)
        r["has_hint"] = "YES" if (local_hints or group_hints) else "NO"
        r["local_solution_ids"] = ";".join(local_sols)
        r["propagated_solution_ids"] = ";".join(propagated)
        r["representative_problem_id"] = representative_by_hash.get(h, pid)
        r["duplicate_role"] = duplicate_role_by_problem.get(pid, "UNIQUE_STATEMENT")
        if local_sols:
            r["solution_link_status"] = "LOCAL_OR_COMPANION_LINKED"
        elif propagated:
            r["solution_link_status"] = "EXACT_DUPLICATE_PROPAGATED"
        else:
            r["solution_link_status"] = "NO_SOLUTION_LINKED"
        r["reconciliation_status"] = "DUPLICATE_COLLAPSED" if h in representative_by_hash else "UNIQUE_STATEMENT"
        # Keep semantic placement fields untouched for the next pass.
        note = r.get("notes", "")
        stamp = "solution/duplicate reconciliation complete"
        if stamp not in note:
            r["notes"] = (note + "; " + stamp).strip("; ")

    # Enrich duplicate group table deterministically from current hashes.
    dup_fields = extend_fields(dup_fields, ["representative_problem_id", "aggregate_solution_ids", "aggregate_hint_ids", "semantic_unit_status"])
    new_dups: list[dict[str,object]] = []
    for row in collapse_rows:
        h = str(row["statement_hash"])
        new_dups.append({
            "duplicate_group": row["duplicate_group"], "statement_hash": h, "member_count": row["member_count"],
            "problem_ids": row["member_problem_ids"], "source_files": row["source_files"],
            "review_status": "EXACT_DUPLICATE_CONFIRMED", "representative_problem_id": row["representative_problem_id"],
            "aggregate_solution_ids": ";".join(sorted(sols_by_hash.get(h, set()))),
            "aggregate_hint_ids": ";".join(sorted(hints_by_hash.get(h, set()))),
            "semantic_unit_status": "EXACT_STATEMENT_EQUIVALENCE",
        })

    # Detached-heading reconciliation table.
    link_by_id = {s["solution_id"]: s for s in links}
    detached_recon: list[dict[str,object]] = []
    for d in detached:
        sol_ids = [x for x in d.get("linked_solution_ids", "").split(";") if x]
        resolved_pids = sorted({link_by_id[x].get("linked_problem_id", "") for x in sol_ids if x in link_by_id and link_by_id[x].get("linked_problem_id")})
        unresolved_ids = [x for x in sol_ids if x not in link_by_id or not link_by_id[x].get("linked_problem_id")]
        detached_recon.append({
            "heading_problem_id": d.get("problem_id", ""), "source_file": d.get("source_file", ""),
            "source_problem_number": d.get("source_problem_number", ""), "solution_ids": ";".join(sol_ids),
            "resolved_problem_ids": ";".join(resolved_pids), "unresolved_solution_ids": ";".join(unresolved_ids),
            "status": "RESOLVED" if sol_ids and not unresolved_ids else ("PARTIAL" if resolved_pids else "UNRESOLVED"),
            "notes": "Detached solution heading retained as provenance; actual solution block links carry the reconciliation.",
        })

    # ----- 6. Explicit remaining orphan report -----
    remaining: list[dict[str,object]] = []
    for s in links:
        if s.get("linked_problem_id"): continue
        remaining.append({
            "solution_id": s.get("solution_id", ""), "solution_kind": s.get("solution_kind", ""),
            "solution_source_file": s.get("solution_source_file", ""), "solution_line_range": s.get("solution_line_range", ""),
            "source_problem_number": s.get("source_problem_number", ""),
            "status": s.get("reconciliation_status", s.get("link_status", "UNRESOLVED")),
            "candidate_problem_ids": s.get("candidate_problem_ids", ""),
            "editorial_action": "REVIEW_NUMBERING_MISMATCH" if s.get("reconciliation_status") == "UNRESOLVED_NUMBERING_MISMATCH" else (
                "CHOOSE_AMONG_CANDIDATES" if s.get("candidate_problem_ids") else "LOCATE_COMPANION_STATEMENT_OR_MARK_ORPHAN"
            ),
        })

    # One row per unique mathematical statement fingerprint.  This is the preferred
    # input to the next semantic subject/Volume classification pass.
    semantic_units: list[dict[str,object]] = []
    for h in sorted(groups):
        members = groups[h]
        rep = representative_by_hash.get(h) or members[0]["problem_id"]
        semantic_units.append({
            "semantic_unit_id": f"SEM-{hashlib.sha1(h.encode('ascii')).hexdigest()[:12].upper()}",
            "statement_hash": h,
            "duplicate_group": hash_to_gid.get(h, ""),
            "member_count": len(members),
            "representative_problem_id": rep,
            "member_problem_ids": ";".join(sorted(r["problem_id"] for r in members)),
            "problem_types": ";".join(sorted({r.get("problem_type","") for r in members if r.get("problem_type")})),
            "source_collections": ";".join(sorted({r.get("source_collection","") for r in members})),
            "source_files": ";".join(sorted({r.get("source_file","") for r in members})),
            "aggregate_solution_ids": ";".join(sorted(sols_by_hash.get(h, set()))),
            "aggregate_hint_ids": ";".join(sorted(hints_by_hash.get(h, set()))),
            "solution_availability": "YES" if sols_by_hash.get(h) else "NO",
            "semantic_unit_status": "EXACT_DUPLICATE_COLLAPSED" if len(members) > 1 else "UNIQUE_STATEMENT",
            "review_status": "READY_FOR_SEMANTIC_CLASSIFICATION",
        })

    # Write updates and reports.
    link_fields = extend_fields(link_fields, ["reconciliation_status","reconciliation_method","reconciliation_confidence","candidate_problem_ids"])
    write_tsv(inv / "PROBLEM_LEDGER.tsv", ledger_fields, ledger)
    write_tsv(inv / "PROBLEM_SOLUTION_LINKS.tsv", link_fields, links)
    write_tsv(inv / "DUPLICATE_GROUPS.tsv", dup_fields, new_dups)
    write_tsv(inv / "EXACT_DUPLICATE_COLLAPSE.tsv", [
        "duplicate_group","statement_hash","member_count","representative_problem_id","member_problem_ids",
        "source_collections","source_files","semantic_unit_status"
    ], collapse_rows)
    write_tsv(inv / "SEMANTIC_PROBLEM_UNITS.tsv", [
        "semantic_unit_id","statement_hash","duplicate_group","member_count","representative_problem_id","member_problem_ids",
        "problem_types","source_collections","source_files","aggregate_solution_ids","aggregate_hint_ids",
        "solution_availability","semantic_unit_status","review_status"
    ], semantic_units)
    write_tsv(inv / "SOLUTION_RECONCILIATION.tsv", [
        "solution_id","solution_kind","solution_source_file","source_problem_number","old_linked_problem_id",
        "new_linked_problem_id","reconciliation_status","reconciliation_method","confidence","candidate_problem_ids","notes"
    ], solution_recon)
    write_tsv(inv / "DETACHED_SOLUTION_RECONCILIATION.tsv", [
        "heading_problem_id","source_file","source_problem_number","solution_ids","resolved_problem_ids",
        "unresolved_solution_ids","status","notes"
    ], detached_recon)
    write_tsv(inv / "NUMBERING_MISMATCHES.tsv", [
        "mismatch_group","solution_source_file","equivalent_solution_source_files",
        "candidate_problem_file","equivalent_candidate_problem_files","file_similarity",
        "sequence_pairs_checked","constant_number_offset","support_count","support_ratio","status","notes"
    ], numbering_rows)
    write_tsv(inv / "REMAINING_ORPHANS.tsv", [
        "solution_id","solution_kind","solution_source_file","solution_line_range","source_problem_number","status",
        "candidate_problem_ids","editorial_action"
    ], remaining)

    remaining_md = ["# Remaining orphan imported solutions/hints", "",
                    "> Every unresolved block is explicit. No ambiguous link is guessed.", ""]
    if not remaining:
        remaining_md.append("None. All detected solution/hint blocks are linked.")
    else:
        by_status = Counter(str(x["status"]) for x in remaining)
        remaining_md += ["## Counts by status", ""] + [f"- {k}: **{v}**" for k,v in sorted(by_status.items())] + ["", "## Items", ""]
        for x in remaining:
            remaining_md.append(f"- `{x['solution_id']}` — `{x['solution_source_file']}` {x['solution_line_range']} — **{x['status']}** — {x['editorial_action']}")
    (inv / "remaining_orphans.md").write_text("\n".join(remaining_md) + "\n", encoding="utf-8")

    unique_semantic_units = len(groups)
    duplicate_member_rows = sum(len(g) for g in groups.values() if len(g) > 1)
    solved_rows = sum(1 for r in ledger if r.get("has_solution") == "YES")
    local_solved_rows = sum(1 for r in ledger if r.get("local_solution_ids"))
    propagated_rows = sum(1 for r in ledger if r.get("propagated_solution_ids") and not r.get("local_solution_ids"))
    summary = [
        "# Imported problem reconciliation — duplicates and solutions", "",
        "> This pass changes only import/provenance inventory data. Canonical book content and semantic Volume/chapter placement remain untouched.", "",
        "## Exact duplicate collapse", "",
        f"- Statement-bearing source rows: **{len(ledger)}**",
        f"- Unique statement hashes / semantic units: **{unique_semantic_units}**",
        f"- `SEMANTIC_PROBLEM_UNITS.tsv` rows ready for classification: **{len(semantic_units)}**",
        f"- Exact duplicate groups: **{len(collapse_rows)}**",
        f"- Source rows participating in duplicate groups: **{duplicate_member_rows}**",
        "- Source rows deleted: **0** (collapse is semantic/provenance-only)", "",
        "## Solution reconciliation", "",
        f"- Solution/hint blocks: **{len(links)}**",
        f"- Existing structural links retained: **{sum(1 for x in solution_recon if x['reconciliation_status']=='RESOLVED_EXISTING_LINK')}**",
        f"- New conservative companion links applied: **{auto_linked}**",
        f"- Remaining unresolved solution/hint blocks: **{len(remaining)}**",
        f"- Ambiguous candidate sets left for review: **{sum(1 for x in remaining if x['status']=='UNRESOLVED_AMBIGUOUS')}**",
        f"- Numbering-mismatch file pairs detected: **{len(numbering_rows)}**", "",
        "## Recomputed ledger", "",
        f"- Rows with directly linked local/companion solution: **{local_solved_rows}**",
        f"- Rows gaining solution availability only through exact-duplicate propagation: **{propagated_rows}**",
        f"- Rows with any reconciled solution availability: **{solved_rows}**",
        f"- Rows still without reconciled solution availability: **{len(ledger)-solved_rows}**", "",
        "## Detached solution headings", "",
        f"- Heading markers: **{len(detached)}**",
        f"- Resolved: **{sum(1 for x in detached_recon if x['status']=='RESOLVED')}**",
        f"- Partial: **{sum(1 for x in detached_recon if x['status']=='PARTIAL')}**",
        f"- Unresolved: **{sum(1 for x in detached_recon if x['status']=='UNRESOLVED')}**", "",
        "## Next pass", "",
        "1. Review any remaining explicit orphan/numbering cases.",
        "2. Review LOW-confidence `PROOF_EXERCISE_CANDIDATE` rows.",
        "3. Classify mathematical subject from actual statement content.",
        "4. Assign Volume/chapter/section.",
        "5. Compare semantic units against the canonical problem index.",
    ]
    (inv / "RECONCILIATION_SUMMARY.md").write_text("\n".join(summary) + "\n", encoding="utf-8")

    print("Imported problem reconciliation complete")
    print(f"  ledger rows: {len(ledger)}")
    print(f"  semantic units: {unique_semantic_units}")
    print(f"  duplicate groups: {len(collapse_rows)}")
    print(f"  new companion links: {auto_linked}")
    print(f"  numbering mismatch pairs: {len(numbering_rows)}")
    print(f"  remaining orphans: {len(remaining)}")
    print(f"  solved rows after propagation: {solved_rows}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
