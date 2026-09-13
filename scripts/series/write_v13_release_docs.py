from __future__ import annotations
import csv, hashlib, json, sys
from pathlib import Path

VOLS=[
("I","vol01_linear_algebra","VOLUME01_FREEZE_MANIFEST.sha256"),
("II","vol02_real_analysis","VOLUME02_FREEZE_MANIFEST.sha256"),
("III","vol03_fourier_distributions_pde","VOLUME03_FREEZE_MANIFEST.sha256"),
("IV","vol04_complex_analysis","VOLUME04_FREEZE_MANIFEST.sha256"),
("V","vol05_commutative_algebra","VOLUME05_FREEZE_MANIFEST.sha256"),
("VI","vol06_algebraic_geometry","VOLUME06_FREEZE_MANIFEST.sha256"),
("VII","vol07_differential_geometry","VOLUME07_FREEZE_MANIFEST.sha256"),
("VIII","vol08_algebraic_topology","VOLUME08_FREEZE_MANIFEST.sha256"),
]
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()

def main():
    if len(sys.argv)!=3: return 2
    repo=Path(sys.argv[1]).resolve(); repro_commit=sys.argv[2]; rel=repo/"release"; reports=repo/"reports"/"series"
    repro=json.loads((reports/"V13_RC1_REPRODUCIBILITY.json").read_text(encoding="utf-8-sig"))
    canon=json.loads((reports/"V13_FREEZE_MANIFEST_CANONICALIZATION.json").read_text(encoding="utf-8-sig"))
    if repro.get("status")!="PASS" or canon.get("status")!="PASS": raise SystemExit("Repro/canonicalization evidence not PASS")

    manifest_path=rel/"CANONICAL_VOLUME_I_VIII_RELEASE_MANIFEST.json"
    manifest=json.loads(manifest_path.read_text(encoding="utf-8-sig"))
    fmap={}
    for v,d,mn in VOLS:
        p=repo/"books"/d/"freeze"/mn; fmap[v]=sha(p)
    for row in manifest["volumes_manifest"]:
        row["freeze_manifest_sha256"]=fmap[row["volume"]]
    manifest["reproducibility_commit"]=repro_commit
    manifest["reproducibility_status"]="PASS"
    manifest["freeze_manifest_hash_policy"]="SHA-256 of canonical Git blob targets"
    manifest_path.write_text(json.dumps(manifest,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")

    tsv=rel/"CANONICAL_VOLUME_I_VIII_RELEASE_MANIFEST.tsv"
    with tsv.open("r",encoding="utf-8-sig",newline="") as f: rows=list(csv.DictReader(f,delimiter="\t")); fields=list(rows[0].keys())
    for r in rows: r["freeze_manifest_sha256"]=fmap[r["volume"]]
    with tsv.open("w",encoding="utf-8",newline="") as f:
        w=csv.DictWriter(f,fieldnames=fields,delimiter="\t",lineterminator="\n");w.writeheader();w.writerows(rows)

    notes=f"""# Theory of Mathematics I-VIII — v1.3

Status: **promotion ready**

Promoted candidate: `v1.3-rc1`  
Original RC commit: `1859fca09fbd0492423f374f3b4cf6fd921a40b2`  
Clean-checkout reproducibility commit: `{repro_commit}`

## Scope

Version 1.3 freezes the eight-volume series at **8 volumes / 256 numbered canonical chapters**,
all FROZEN / COMPLETE.

## Final release work

- completed professional-review passes across Volumes I-VIII;
- reconciled all chapter-status and source-migration ledgers;
- aligned Volume II topology coverage, retaining 25 numbered chapters plus its unnumbered topology interlude;
- reconciled solved dossiers, exercises, hints and solutions;
- reconciled cross-volume mathematical navigation;
- refreshed publication freeze metadata;
- repaired the final >=20pt layout overflows;
- verified the Volume VI full-solutions edition;
- canonicalized freeze-manifest hashes to immutable Git blob bytes so the freeze contract is platform-independent;
- passed the clean-checkout v1.3 reproducibility gate.

## Reproducibility policy

Freeze-manifest hashes identify immutable Git content rather than platform-specific checkout bytes.
PDF SHA-256 values remain recorded for traceability; regenerated TeX PDFs may differ byte-for-byte
because of embedded build metadata. Page counts, canonical source/freeze integrity, successful
builds, LaTeX diagnostics and global reconciliation are blocking release criteria.

## Versioning

After promotion, v1.3 is frozen. Further mathematical/editorial changes begin v1.4 work.
"""
    (rel/"V1.3_RELEASE_NOTES.md").write_text(notes,encoding="utf-8")
    (rel/"CITATION.md").write_text("""# Citation

## Theory of Mathematics I-VIII v1.3

Recommended citation:

> *Theory of Mathematics I-VIII*, version 1.3, repository `expert10000/math`,
> tag `theory-of-mathematics-i-viii-v1.3`.

For scholarly use, also identify the cited volume/chapter and final release commit.
""",encoding="utf-8")
    ch=rel/"SERIES_CHANGELOG.md"; old=ch.read_text(encoding="utf-8-sig") if ch.exists() else "# Series Changelog\n"
    section="""## v1.3

- Promoted the professionally reviewed Volume I-VIII series from v1.3-rc1.
- 8 volumes / 256 numbered canonical chapters, all FROZEN / COMPLETE.
- Canonicalized freeze hashes for platform-independent clean-checkout verification.
- Final build, layout, navigation, solution-contract and reconciliation gates PASS.
- v1.3 becomes the frozen baseline; new changes proceed as v1.4.

"""
    if "## v1.3\n" not in old:
        old="# Series Changelog\n\n"+section+(old.split("\n",1)[1].lstrip() if old.startswith("# Series Changelog") and "\n" in old else old)
    ch.write_text(old.rstrip()+"\n",encoding="utf-8")

    meta_path=rel/"SERIES_RELEASE_METADATA.json"; meta=json.loads(meta_path.read_text(encoding="utf-8-sig"))
    meta.update({"candidate":"v1.3-rc1","candidate_commit":"1859fca09fbd0492423f374f3b4cf6fd921a40b2","final_release_target":"v1.3","final_tag_target":"theory-of-mathematics-i-viii-v1.3","release_state":"PROMOTION_READY","promotion_ready":True,"reproducibility_commit":repro_commit,"reproducibility_status":"PASS","freeze_manifest_hash_policy":"canonical Git blob SHA-256","release_notes":"release/V1.3_RELEASE_NOTES.md","citation":"release/CITATION.md","blocking":[]})
    meta_path.write_text(json.dumps(meta,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    readme=rel/"README.md"; txt=readme.read_text(encoding="utf-8-sig")
    if "## v1.3 promotion" not in txt: txt=txt.rstrip()+"\n\n## v1.3 promotion\n\nv1.3-rc1 passed canonical freeze-hash normalization and clean-checkout reproducibility. See `V1.3_RELEASE_NOTES.md` and `CITATION.md`.\n"
    readme.write_text(txt,encoding="utf-8")

    side=rel/"CANONICAL_VOLUME_I_VIII_RELEASE_MANIFEST.sha256"
    targets=[tsv,manifest_path,meta_path,reports/"FINAL_RELEASE_CANDIDATE_GATE_I_VIII.json",reports/"SERIES_NAVIGATION_RELEASE_RECONCILIATION.json",reports/"V13_FREEZE_MANIFEST_CANONICALIZATION.json",reports/"V13_RC1_REPRODUCIBILITY.json"]
    side.write_text("\n".join(f"{sha(p)}  {p.relative_to(repo).as_posix()}" for p in targets)+"\n",encoding="utf-8")
    out={"schema":2,"status":"PASS","candidate":"v1.3-rc1","target":"v1.3","reproducibility_commit":repro_commit,"freeze_manifests_refreshed":8,"blocking":[]}
    (reports/"V13_RELEASE_DOCS.json").write_text(json.dumps(out,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(out,indent=2)); return 0
if __name__=="__main__": raise SystemExit(main())
