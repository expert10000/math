from __future__ import annotations
import hashlib,json,shutil,subprocess,sys
from pathlib import Path
VOLS=[
("I","vol01_linear_algebra"),("II","vol02_real_analysis"),("III","vol03_fourier_distributions_pde"),("IV","vol04_complex_analysis"),
("V","vol05_commutative_algebra"),("VI","vol06_algebraic_geometry"),("VII","vol07_differential_geometry"),("VIII","vol08_algebraic_topology")]
RC="release/theory_of_mathematics_i_viii_v1.3-rc1"; FINAL="release/theory_of_mathematics_i_viii_v1.3"; RC_COMMIT="1859fca09fbd0492423f374f3b4cf6fd921a40b2"
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def tracked(repo,prefix):
    return [x for x in subprocess.check_output(["git","ls-files",prefix],cwd=repo,text=True).splitlines() if x.strip()]
def main():
    if len(sys.argv)!=4:return 2
    repo=Path(sys.argv[1]).resolve(); repro=sys.argv[2]; docs=sys.argv[3]; rel=repo/"release"; reports=repo/"reports"/"series"
    if json.loads((reports/"V13_RC1_REPRODUCIBILITY.json").read_text()).get("status")!="PASS":raise SystemExit("repro not PASS")
    src=repo/RC; dst=repo/FINAL
    if dst.exists():shutil.rmtree(dst)
    dst.mkdir(parents=True)
    files=tracked(repo,RC)
    for rp in files:
        s=repo/rp; t=dst/Path(rp).relative_to(RC);t.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(s,t)

    roman_to_num={'I':1,'II':2,'III':3,'IV':4,'V':5,'VI':6,'VII':7,'VIII':8}
    for roman,d in VOLS:
        n=f"{roman_to_num[roman]:02d}"
        target=dst/"evidence"/"volume_freeze"/f"volume{n}";target.mkdir(parents=True,exist_ok=True)
        fr=repo/"books"/d/"freeze"
        for name in (f"VOLUME{n}_FREEZE_MANIFEST.sha256",f"VOLUME{n}_FREEZE_REPORT.md",f"RELEASE_VOLUME{n}.md"):
            p=fr/name
            if p.exists():shutil.copy2(p,target/name)

    evdst=dst/"evidence";evdst.mkdir(parents=True,exist_ok=True)
    for name in ("V13_FREEZE_MANIFEST_CANONICALIZATION.json","V13_FREEZE_MANIFEST_CANONICALIZATION.md","V13_RC1_REPRODUCIBILITY.json","V13_RC1_REPRODUCIBILITY.md","V13_RC1_REPRODUCIBILITY.tsv"):
        p=reports/name
        if p.exists():shutil.copy2(p,evdst/name)
    if (rel/"V1.3_RELEASE_NOTES.md").exists():shutil.copy2(rel/"V1.3_RELEASE_NOTES.md",dst/"RELEASE_NOTES.md")

    rj=dst/"RELEASE.json"; data=json.loads(rj.read_text(encoding="utf-8-sig"))
    data.update({"release":"Theory of Mathematics I-VIII v1.3","tag":"theory-of-mathematics-i-viii-v1.3","release_state":"RELEASED","final_release":"v1.3","promoted_from_candidate":"v1.3-rc1","candidate_commit":RC_COMMIT,"reproducibility_commit":repro,"docs_commit":docs,"source_commit_before_release_commit":docs,"freeze_manifest_hash_policy":"canonical Git blob SHA-256"})
    data.pop("candidate",None);rj.write_text(json.dumps(data,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")

    sums=dst/"SHA256SUMS.txt"
    if sums.exists():sums.unlink()
    entries=[f"{sha(p)}  {p.relative_to(dst).as_posix()}" for p in sorted(dst.rglob("*")) if p.is_file() and p!=sums]
    sums.write_text("\n".join(entries)+"\n",encoding="utf-8")

    mp=rel/"CANONICAL_VOLUME_I_VIII_RELEASE_MANIFEST.json"; man=json.loads(mp.read_text(encoding="utf-8-sig"))
    man.update({"status":"PASS","release":"v1.3","release_state":"RELEASED","tag":"theory-of-mathematics-i-viii-v1.3","promoted_from_candidate":"v1.3-rc1","candidate_commit":RC_COMMIT,"reproducibility_commit":repro,"source_commit_before_release_commit":docs,"release_directory":FINAL,"freeze_manifest_hash_policy":"canonical Git blob SHA-256","blocking":[]});man.pop("candidate",None);mp.write_text(json.dumps(man,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    meta=rel/"SERIES_RELEASE_METADATA.json"; m=json.loads(meta.read_text(encoding="utf-8-sig"));m.update({"release":"v1.3","tag":"theory-of-mathematics-i-viii-v1.3","release_state":"RELEASED","promotion_ready":False,"promoted_from_candidate":"v1.3-rc1","candidate_commit":RC_COMMIT,"reproducibility_commit":repro,"docs_commit":docs,"release_directory":FINAL,"freeze_manifest_hash_policy":"canonical Git blob SHA-256","blocking":[]});meta.write_text(json.dumps(m,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    side=rel/"CANONICAL_VOLUME_I_VIII_RELEASE_MANIFEST.sha256";targets=[rel/"CANONICAL_VOLUME_I_VIII_RELEASE_MANIFEST.tsv",mp,meta,reports/"FINAL_RELEASE_CANDIDATE_GATE_I_VIII.json",reports/"SERIES_NAVIGATION_RELEASE_RECONCILIATION.json",reports/"V13_FREEZE_MANIFEST_CANONICALIZATION.json",reports/"V13_RC1_REPRODUCIBILITY.json",rj,sums];side.write_text("\n".join(f"{sha(p)}  {p.relative_to(repo).as_posix()}" for p in targets)+"\n",encoding="utf-8")
    out={"schema":2,"status":"PASS","release":"v1.3","tag":"theory-of-mathematics-i-viii-v1.3","candidate_commit":RC_COMMIT,"reproducibility_commit":repro,"docs_commit":docs,"release_directory":FINAL,"final_release_files_hashed":len(entries),"blocking":[]}
    (reports/"V13_FINAL_RELEASE_PROMOTION.json").write_text(json.dumps(out,indent=2)+"\n",encoding="utf-8")
    (reports/"V13_FINAL_RELEASE_PROMOTION.md").write_text(f"# Theory of Mathematics I-VIII v1.3 Promotion\n\n**Status: PASS**\n\n- Candidate: `v1.3-rc1`\n- Reproducibility commit: `{repro}`\n- Documentation commit: `{docs}`\n- Final tag: `theory-of-mathematics-i-viii-v1.3`\n- Blocking findings: none\n",encoding="utf-8")
    print(json.dumps(out,indent=2));return 0
if __name__=="__main__":raise SystemExit(main())
