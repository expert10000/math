# Volume VIII professional review — exercises, hints, solutions and theorem coverage

Pinned review base: `93a9802fd0b9085db57562e15941a42874b6c3d7`

## Scope

This is the third and final professional-review pass for **VIII/01–VIII/35**.

The existing Volume VIII integration audit at the pinned base reports:

- 35 canonical chapter files;
- 35 active chapter includes;
- 35 Volume VIII status rows;
- 1723 unique labels;
- 0 duplicate labels;
- 0 missing Volume-VIII internal references;
- 16 SVG assets;
- 0 SVG metadata warnings.

The final freeze audit is the authoritative semantic pairing gate because it checks every `Problem` and `Exercise` locally for a following `Solution`. The older integration report's raw comparison of **Problem count versus Solution count** is not a proof of imbalance: exercise solutions also use solution environments, so a chapter can legitimately contain more solutions than solved problems.

## Semantic reconciliation rules

For every VIII/01–VIII/35 chapter:

1. each exercise is solvable from material available at that point, unless explicitly marked exploratory;
2. each hint advances the intended method rather than merely restating the question;
3. each solution proves or computes exactly what the exercise/problem asks;
4. all hypotheses used in a solution also appear in the statement or are established earlier;
5. based/unbased distinctions are preserved;
6. reduced/unreduced and absolute/relative groups are not conflated;
7. exact-sequence arrows and connecting-map degrees agree between theorem, hint and solution;
8. coefficient choices are preserved throughout a computation;
9. torsion terms are not discarded in UCT/Künneth exercises;
10. cup/cap product signs agree with the chapter convention;
11. Thom/Euler/duality exercises keep orientation hypotheses;
12. intersection and Lefschetz exercises retain dimension, compactness, orientability and finiteness hypotheses.

## High-risk theorem/exercise pairs

### Coverings

Any exercise using the classification of coverings must state the needed hypotheses on the base. A deck-group computation must distinguish regular coverings from arbitrary coverings.

### Exact sequences

Exercises using a long exact sequence must identify the pair/cofiber/chain cone and the degree of the connecting morphism. Solutions should verify exactness at the specific term actually used.

### UCT and Künneth

Exercises should separately identify free and torsion contributions. A splitting is not to be treated as canonical without justification.

### Cup products

Additive homology/cohomology computations do not by themselves determine the ring. Ring exercises must compute or constrain products and respect graded signs.

### Thom and Euler classes

A nowhere-zero section implies vanishing Euler class. The converse must not be used as an unrestricted theorem.

### Poincaré duality and intersection forms

Integral duality/intersection calculations must preserve orientability and torsion qualifications. Four-manifold forms should be stated on the appropriate free middle-homology group.

### Lefschetz theory

`L(f) != 0` is a sufficient fixed-point criterion under the theorem's hypotheses; it is not a converse. Local index calculations require the local assumptions used by the chapter.

## Canonical QA sequence

Integration audit:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass `
  -File .\books\vol08_algebraic_topology\AUDIT_VOLUME08_INTEGRATION.ps1 `
  -Repo $PWD `
  -WriteReports
```

Freeze-semantic audit:

```powershell
python .\books\vol08_algebraic_topology\freeze\AUDIT_VOLUME08_FREEZE.py `
  --repo $PWD
```

Full clean build:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass `
  -File .\books\vol08_algebraic_topology\BUILD_WINDOWS.ps1 `
  -Repo $PWD `
  -Clean
```

The APPLY script accompanying this review additionally verifies every path/hash already listed in `freeze/VOLUME08_FREEZE_MANIFEST.sha256`. Because this professional review changes only editorial review/navigation sidecars and regenerated integration reports, the frozen chapter/book/figure/reconciliation hashes must remain unchanged.

## Release rule

If a future professional review changes any file already covered by the freeze manifest, that change is a **post-freeze source correction** and the Volume VIII freeze manifest/report/release metadata must be regenerated explicitly. It must never be left silently stale.
