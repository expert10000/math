# GA-10 Batch 45 - Part I problems 0001-0009

Reviewed checkpoint: 3f692bfa9a954ce766817018b3d9ea44e1778ac6. AI independent mathematical review of nine complete statements and solutions, supported by exact SymPy 1.14.0 checks. This does not assert formal or human certification.

## Findings requiring repair

**B45-M01, CP-I-0002, P1: confirmed mathematical error.** The c=-1 factorization is correct, but its geometric interpretation is not: q=x^2+y^2-xy-x-y+1=(x-1)^2+(y-1)^2-(x-1)(y-1). Its quadratic matrix has eigenvalues 1/2 and 3/2, so its real zero locus is the single point (1,1). Consequently the exceptional level is the line x+y+1=0 together with the isolated point (1,1), not a line plus an ellipse. For c=0 the current singularity location is correct; a fuller description of the nodal cubic would satisfy the request to describe the exceptional level more clearly. The tangent cone is xy=0; x=3t/(1+t^3), y=3t^2/(1+t^3), t!=-1 gives its rational parametrization, with the origin included separately.

**B45-C01, CP-I-0005, P2: classification coverage gap.** Spectral reduction and ellipsoid semi-axes are correct. The broad mixed-sign wording fails to distinguish diag(1,-1,0), a hyperbolic cylinder, from nondegenerate hyperboloids. Add inertia cases: (3,0,0) ellipsoid; (2,1,0) one-sheet hyperboloid; (1,2,0) two-sheet hyperboloid; (2,0,1) elliptic cylinder; (1,1,1) hyperbolic cylinder; (1,0,2) two parallel planes; no positive eigenvalue gives empty locus. Triples count positive, negative and zero eigenvalues.

**B45-Q01, CP-I-0006, P2: exceptional-case qualification.** For coincident reflecting planes, n2=+/-n1 and the composition is I; their intersection is a plane, not a unique line. Separate this case. For distinct planes the intersection-axis result holds; rotation direction depends on composition order and orientation. All preceding Householder and half-turn calculations are correct.

## Six solutions correct within scope

- CP-I-0001: homogeneity, submultiplicativity, functional/vector norm identities and Frobenius bounds hold for positive source dimension. Upper equality is rank at most one, including the zero operator; SVD/Riesz are explicit dependencies.
- CP-I-0003: the scalar-operator contradiction, projected trace-zero induction and distinct-real-diagonal commutator construction hold, with zero and one-dimensional cases covered.
- CP-I-0004: the quotient map is well defined and continuous by the quotient universal property. H1 action is A; H2 action is exterior-square A, hence det A, also for singular or negative determinant. The source invokes degree=det as a theorem dependency, not an independently proved step.
- CP-I-0007: eigenvalues 2+/-sqrt(3), det(A-I)=-2 and the two fixed classes are correct and exhaustive.
- CP-I-0008: all four eigenpairs are correct. A4 has column sums 2, so the normalization denominator is positive everywhere on the simplex; the barycenter is fixed. The allowed zero eigenvalue for A3 causes no normalization claim there.
- CP-I-0009: each displayed dual coefficient matrix D satisfies DP=I; the row convention is correct.

## Disposition

Report-only commit; no TeX or asset changes and no rebuild. The three findings remain OPEN until source repairs and PDF verification. Next Batch 46 should repair these three scoped passages, preserve problem identities/provenance, rebuild with pdfLaTeX and inspect changed pages. Do not mark findings closed merely because a patch is prepared.

GA-10 cumulative coverage is 14 distinct Part I problems (five in Batch 44, nine here), leaving 109 not reviewed in these cohorts. The 49 provenance findings and historical proof qualifications remain preserved. Publication approval and release tag remain pending.
