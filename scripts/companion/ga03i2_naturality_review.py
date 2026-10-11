#!/usr/bin/env python3
"""GA-03i.2: curated naturality and derived-functor review.

Uses GA-03i.1 ledger as source of scoped review entries.  Does not modify
chapters, inventory, or previous ledgers.  --apply writes two new reports.
This is an editorial assessment, not an automated theorem prover.
"""
import argparse
import csv
import re
import sys
from pathlib import Path

REL = Path("reports/companion/global_audit")
INPUT = REL / "GA03I_EXACT_SEQUENCE_AUDIT.tsv"
TSV = REL / "GA03I2_NATURALITY_REVIEW.tsv"
MD = REL / "GA03I2_NATURALITY_REVIEW.md"
CHAPTER = Path("books/companion_problems_solutions/chapters/part05_volume_v/chapter.tex")

CONNECTIONS = [
 ("CP-V-0024", "CP-V-0114", "TENSOR_HOM_EXACTNESS",
  "COMPATIBLE",
  "Tensor is right exact and Hom(M,-) is left exact; Tor and Ext measure their respective failures. The direction of the Ext boundary depends on the chosen variable."),
 ("CP-V-0046", "CP-V-0114", "CONNECTING_TO_DERIVED",
  "COMPATIBLE",
  "The long exact homology sequence applies to degreewise short exact sequences of tensor complexes; for Ext the relevant cochain complexes yield cohomological connecting maps."),
 ("CP-V-0046", "CP-V-0047", "TOR_RESOLUTION",
  "COMPATIBLE",
  "A free resolution of Z/n has differential multiplication by n; tensoring with N makes Tor_1 equal to ker(n:N->N)."),
 ("CP-V-0046", "CP-V-0048", "IDEAL_INTERSECTION_TOR",
  "COMPATIBLE",
  "The boundary and exactness for 0->I->A->A/I->0 after tensoring with A/J identify Tor_1(A/I,A/J) with (I intersect J)/IJ; this identification is natural in maps of compatible ideal pairs."),
 ("CP-V-0022", "CP-V-0096", "BASE_CHANGE_NATURALITY",
  "COMPATIBLE",
  "The natural map (A/I) tensor_A M -> M/IM sends (a+I) tensor m to am+IM. Extension from k to K preserves quotient presentations, with commuting structure maps."),
 ("CP-V-0023", "CP-V-0105", "HOM_FINITE_PRESENTATION",
  "COMPATIBLE_WITH_DISTINCTION",
  "Both results use finite presentation, but one compares Hom with localization while the other compares Hom with filtered colimits. They are distinct natural transformations."),
 ("CP-V-0031", "CP-V-0087", "COMPLETION_VS_LIMIT",
  "COMPATIBLE_WITH_HYPOTHESES",
  "Inverse limits are left exact; surjectivity in the limit depends on the kernel inverse system. Exact completion for finite modules over Noetherian rings additionally uses Artin-Rees/cofinal filtrations."),
 ("CP-V-0110", "CP-V-0046", "HOMOTOPY_VS_NATURALITY",
  "COMPATIBLE_WITH_DISTINCTION",
  "Chain-homotopic chain maps induce the same map on homology; naturality of connecting homomorphisms requires a commuting morphism of short exact sequences of complexes."),
 ("CP-V-0047", "CP-V-0113", "TOR_EXT_DUAL_COMPARISON",
  "COMPATIBLE_WITH_DISTINCTION",
  "Both use the resolution of Z/n. Tor_1(Z/n,N)=ker(n:N->N), whereas Ext^1(Z/n,N)=coker(n:N->N). Similar cyclic outputs do not identify the two functors naturally."),
]
GAPS = [
 ("CONNECTING_NATURALITY", "EDITORIAL_GAP_OPEN",
  "Write and check the naturality square: for a morphism of short exact sequences of chain complexes, H_{n-1}(a) circ boundary = boundary_new circ H_n(c)."),
 ("LONG_EXACT_EXT_VARIANCE", "EDITORIAL_GAP_OPEN",
  "State separately Ext^i(M,-) covariant in the second variable and Ext^i(-,N) contravariant in the first. Explain the connecting maps and arrows in each long exact sequence."),
 ("DERIVED_FUNCTOR_COMPARISON", "EDITORIAL_GAP_OPEN",
  "Distinguish chain-homotopy invariance of homology maps from functorial naturality of boundary operators. Neither theorem should be presented as proving the other."),
 ("INVERSE_LIMIT_CAUTION", "EDITORIAL_GAP_OPEN",
  "Explain inverse-limit left exactness, the role of lim^1, and sufficient Mittag-Leffler/surjective-transition hypotheses for right exactness. Do not assert inverse limits are exact in general."),
]

def load(path):
    with path.open("r", encoding="utf-8-sig", newline="") as stream:
        return list(csv.DictReader(stream, delimiter="\t"))

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=Path("."))
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    repo = args.repo.resolve()
    source = repo / INPUT
    chapter = repo / CHAPTER
    if not source.is_file() or not chapter.is_file():
        sys.exit("ERROR: missing GA-03i.1 ledger or canonical Part V chapter")
    prior = load(source)
    source_headers = set(prior[0]) if prior else set()
    mandatory = {"check_type", "topic", "companion_problem_id", "related_problem_id", "status"}
    if not mandatory.issubset(source_headers):
        sys.exit(f"ERROR: ledger columns missing: {sorted(mandatory - source_headers)}")

    chapter_text = chapter.read_text(encoding="utf-8")
    ids = re.findall(r'\\begin\{problem\}\[(CP-V-\d{4})\]', chapter_text)
    if len(ids) != 114 or len(set(ids)) != 114:
        sys.exit("ERROR: unexpected canonical chapter ID count or duplicates")

    def matching(a, b):
        return [r for r in prior
                if r["check_type"] == "FUNCTORIAL_CONNECTION"
                and r["companion_problem_id"] == a
                and r["related_problem_id"] == b
                and r["status"] == "REVIEW"]

    def gaps_matching(topic):
        return [r for r in prior
                if r["check_type"] == "EDITORIAL_GAP_REVIEW"
                and r["topic"] == topic and r["status"] == "REVIEW"]

    rows = []
    for a, b, topic, status, note in CONNECTIONS:
        found = matching(a, b)
        if len(found) != 1 or a not in ids or b not in ids:
            sys.exit(f"ERROR: missing/nonunique source link or chapter ID: {a} -> {b}")
        rows.append(dict(item_type="CROSS_TOPIC", topic=topic, companion_problem_id=a,
                         related_problem_id=b, review_status=status,
                         mathematical_note=note, source_status=found[0]["status"]))
    for topic, status, note in GAPS:
        found = gaps_matching(topic)
        if len(found) != 1:
            sys.exit(f"ERROR: missing/nonunique editorial gap: {topic}")
        rows.append(dict(item_type="EDITORIAL_GAP", topic=topic, companion_problem_id="",
                         related_problem_id="", review_status=status,
                         mathematical_note=note, source_status=found[0]["status"]))

    print("GA-03i.2 — NATURALITY / DERIVED FUNCTOR REVIEW")
    print(f"  canonical IDs: {len(ids)}; cross-topic assessments: {len(CONNECTIONS)}; open gaps: {len(GAPS)}")
    print("  IMPORTANT: open editorial gaps are not declared resolved.")
    if args.apply:
        out = repo / TSV
        out.parent.mkdir(parents=True, exist_ok=True)
        with out.open("w", encoding="utf-8", newline="") as stream:
            writer = csv.DictWriter(stream, fieldnames=list(rows[0]), delimiter="\t")
            writer.writeheader()
            writer.writerows(rows)
        md = [
            "# GA-03i.2 — Natural transformations and derived-functor compatibility",
            "",
            "Source: GA-03i.1 canonical scope and audit ledger. This is an editorial mathematical review;",
            "the source-import provenance and four editorial gaps remain separately tracked.",
            "",
            "## Reviewed connections", "",
        ]
        for row in rows[:len(CONNECTIONS)]:
            md += [f"### {row['companion_problem_id']} → {row['related_problem_id']}",
                   f"**{row['topic']} — {row['review_status']}**", "",
                   row["mathematical_note"], ""]
        md += ["## Open editorial gaps", ""]
        for row in rows[len(CONNECTIONS):]:
            md += [f"### {row['topic']}", row["mathematical_note"], ""]
        md += [
            "## Connecting-map naturality identity", "",
            "For a commuting morphism of short exact sequences of chain complexes",
            "with vertical maps a, b, c, the homological connecting maps satisfy",
            r"\[ H_{n-1}(a)\circ\partial_n=\widetilde{\partial}_n\circ H_n(c).\]",
            "",
            "## Ext variance", "",
            r"\(\operatorname{Ext}_R^i(M,-)\) is covariant, while",
            r"\(\operatorname{Ext}_R^i(-,N)\) is contravariant.",
            r"For a short exact sequence \(0\to A'\to A\to A''\to0\),",
            "the connecting map for Ext in the second variable goes from",
            r"\(\operatorname{Ext}_R^i(M,A'')\) to \(\operatorname{Ext}_R^{i+1}(M,A')\).",
            "",
            "## Inverse-limit caveat", "",
            "Inverse limits are left exact. For the usual countable index category,",
            "the obstruction to right exactness is related to the derived functor lim^1.",
            "A Mittag–Leffler condition on the kernel system is sufficient for",
            "the needed vanishing. This is distinct from exactness of filtered colimits.",
        ]
        (repo / MD).write_text("\n".join(md)+"\n", encoding="utf-8")
        print("  WROTE:", out)
        print("  WROTE:", repo / MD)
    else:
        print("  DRY RUN; no files changed")

if __name__ == "__main__":
    main()
