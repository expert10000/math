from __future__ import annotations

def ex(after, title, body): return {"after_section":after,"title":title,"body":body}
def q(title,prompt,hint,solution): return {"title":title,"prompt":prompt,"hint":hint,"solution":solution}
def pack(examples, standard, proof, test, application, challenge):
    return {"examples":examples,"exercises":{"standard":standard,"proof":proof,"test":test,"application":application,"challenge":challenge}}
DATA={}

DATA["IV/12"] = pack(
examples=[
ex(1,"Winding number of a translated circle",r"""Let \(\gamma(t)=2+3e^{it}\), \(0\le t\le2\pi\). Around the point \(a=2\),
\[
\operatorname{Ind}(\gamma,2)=\frac{1}{2\pi i}\int_\gamma\frac{dz}{z-2}=1.
\]
Around \(a=6\), the point lies outside the circle and the index is zero. The index records how the curve winds around a chosen point, not merely the shape of the curve itself."""),
ex(4,"Argument principle for a polynomial",r"""Take \(f(z)=z^3-1\) on \(|z|=2\). There are no zeros or poles on the contour, and all three roots lie inside. Therefore
\[
\frac{1}{2\pi i}\int_{|z|=2}\frac{f'(z)}{f(z)}\,dz=3.
\]
Equivalently, the image curve \(f(2e^{it})\) winds three times around the origin."""),
ex(7,"Zeros minus poles",r"""For \(f(z)=(z-1)^2/(z+1)\) on \(|z|=2\), the contour encloses a double zero at \(1\) and a simple pole at \(-1\). The argument principle gives
\[
\frac{1}{2\pi i}\int_{|z|=2}\frac{f'}{f}\,dz=2-1=1.
\]
Multiplicity and pole order enter with opposite signs.""")],
standard=[
q("Unit circle index",r"Compute the winding number of \(e^{it}\), \(0\le t\le2\pi\), about zero.",r"Use the logarithmic integral definition.",r"The index is one."),
q("Double traversal",r"Compute the winding number of \(e^{2it}\) about zero for \(0\le t\le2\pi\).",r"Track the change of argument.",r"The argument increases by \(4\pi\), so the index is two."),
q("Clockwise circle",r"Find the index of \(e^{-it}\) about zero.",r"Orientation matters.",r"The index is minus one."),
q("Zero count",r"Use the argument principle to count zeros of \(z^4+1\) in \(|z|=2\).",r"All four roots have modulus one.",r"There are four zeros, counted with multiplicity, and no poles."),
q("Zero minus pole",r"For \(f(z)=z^3/(z-1)^2\), compute the argument-principle count on \(|z|=2\).",r"Count orders inside.",r"The result is \(3-2=1\).")],
proof=[
q("Index is integer",r"Explain why the winding number of a closed curve about a point not on the curve is an integer.",r"Use a continuous change of argument along the curve.",r"Choose a continuous argument along the parameter interval. Closedness forces the final argument to differ from the initial one by an integer multiple of \(2\pi\), and that integer is the index."),
q("Homotopy invariance",r"Prove that winding number is unchanged under a deformation avoiding the reference point.",r"The index varies continuously with the deformation parameter but takes integer values.",r"The integral defining the index depends continuously on the homotopy. A continuous integer valued function is locally constant, hence constant on the connected parameter interval."),
q("Argument principle",r"Prove the argument principle from residues of \(f'/f\).",r"Find the local residue at a zero or pole.",r"A zero of order \(m\) gives residue \(m\), while a pole of order \(n\) gives residue \(-n\). The residue theorem sums these local integers to give zeros minus poles."),
q("Change of argument form",r"Relate \(\int f'/f\) to the net change of argument of \(f\) along a contour.",r"Parametrize the contour and differentiate a local logarithm.",r"Along intervals where a logarithm is chosen, \(d\log f=f'/f\,dz\). Its real part returns to the initial value on a closed contour, while the imaginary part changes by the total argument increment.")],
test=[
q("Point on curve",r"Can the winding number about \(a\) be defined by the usual integral if \(a\) lies on the curve?",r"The kernel has a pole on the path.",r"No. The integral is singular and the standard index is undefined."),
q("Zero on contour",r"Can the argument principle be applied if \(f\) has a zero on the contour?",r"Then \(f'/f\) is singular on the path.",r"No. Zeros and poles must be absent from the contour."),
q("Ignoring multiplicity",r"What error arises if a double zero is counted only once in the argument principle?",r"The local residue equals the order.",r"The count is off by one because a double zero contributes two, not one.")],
application=[
q("Root counting without solving",r"Why is the argument principle useful for a high degree polynomial?",r"It converts root counting into a contour integral or argument change.",r"One can determine the number of roots in a region without finding their individual values, provided the boundary contains no roots."),
q("Nyquist style interpretation",r"Interpret the argument principle geometrically in terms of the image of the boundary under \(f\).",r"Track how \(f(\gamma)\) winds around zero.",r"The net winding of the image about zero equals the number of enclosed zeros minus poles, counted with multiplicity.")],
challenge=[
q("Meromorphic divisor count",r"Show that a meromorphic function on a bounded region with no boundary zeros or poles has total divisor degree equal to the winding of its boundary values about zero.",r"Apply the argument principle.",r"The divisor degree is the sum of zero orders minus pole orders. The argument principle identifies this integer with \((2\pi i)^{-1}\int f'/f\), which is the winding number of the image curve."),
q("Nested contours",r"Two nested contours contain no zeros or poles in the annulus between them. Compare their argument-principle counts.",r"Apply the residue theorem to \(f'/f\) on the annulus.",r"The two counts are equal because the difference of the contour integrals is the integral over the annular boundary, which vanishes when no zeros or poles lie between them.")])

DATA["IV/13"] = pack(
examples=[
ex(1,"One zero in the unit disk",r"""On \(|z|=1\), compare \(f(z)=z^5+3z+1\) with \(g(z)=3z\). We have \(|f-g|=|z^5+1|\le2<3=|g|\). Rouché's theorem therefore says that \(f\) and \(3z\) have the same number of zeros in the unit disk: exactly one, counted with multiplicity."""),
ex(4,"All five zeros in a larger disk",r"""On \(|z|=2\), compare the same polynomial with \(g(z)=z^5\). Then
\[
|3z+1|\le7<32=|z^5|.
\]
Thus \(z^5+3z+1\) has five zeros in \(|z|<2\). Combined with the unit disk calculation, four zeros lie in the annulus \(1<|z|<2\)."""),
ex(7,"Perturbing a known zero count",r"""Suppose \(p\) has no zeros on a contour \(C\), and \(|h|<|p|\) on \(C\). Then \(p+h\) has exactly the same number of zeros inside. This is not merely qualitative continuity: the strict boundary inequality supplies a verifiable certificate that the zero count is unchanged.""")],
standard=[
q("Dominant monomial",r"How many zeros does \(z^7+2\) have in \(|z|<2\)?",r"Compare with \(z^7\) on \(|z|=2\).",r"Since \(2<2^7\), Rouché gives seven zeros."),
q("Small disk",r"How many zeros does \(z^4+5z+1\) have in \(|z|<1\)?",r"Compare with \(5z\).",r"On the unit circle, \(|z^4+1|\le2<5\), so there is one zero."),
q("Constant dominance",r"Show that \(2+z+z^2\) has no zeros in \(|z|<1/2\).",r"Compare with the constant two.",r"On \(|z|=1/2\), \(|z+z^2|\le3/4<2\). Hence the polynomial has the same zero count as the nonzero constant, namely zero."),
q("Annular subtraction",r"A polynomial has two zeros in \(|z|<1\) and six in \(|z|<3\). How many lie in \(1<|z|<3\)?",r"Subtract the counts.",r"There are four zeros in the annulus."),
q("Multiplicity",r"If Rouché compares a function to \((z-a)^4\), how many zeros are certified inside the contour?",r"Zeros are counted with multiplicity.",r"Exactly four zeros, counted with multiplicity.")],
proof=[
q("Rouché from argument principle",r"Prove Rouché's theorem using the family \(f_t=f+t g\) when \(|g|<|f|\) on the contour.",r"Show no \(f_t\) vanishes on the boundary.",r"The inequality gives \(|f_t|\ge|f|-t|g|>0\). The boundary winding number of \(f_t\) about zero is integer valued and continuous in \(t\), hence constant. The argument principle gives equal zero counts at \(t=0\) and \(t=1\)."),
q("Symmetric version",r"Show that if \(|f-g|<|f|\) on a contour, then \(f\) and \(g\) have the same number of zeros inside.",r"Apply Rouché to \(f\) and perturbation \(g-f\).",r"The hypothesis is precisely \(|g-f|<|f|\), so \(f+(g-f)=g\) has the same zero count as \(f\)."),
q("Local stability",r"Prove that a sufficiently small uniform perturbation preserves the number of zeros in a disk whose boundary contains no zeros.",r"The minimum of \(|f|\) on the compact boundary is positive.",r"Let \(m=\min_C|f|>0\). Any perturbation \(h\) with \(\max_C|h|<m\) satisfies Rouché, so \(f+h\) has the same number of zeros."),
q("FTA by Rouché",r"Use Rouché to prove that a degree \(n\) polynomial has \(n\) zeros counted with multiplicity.",r"On a sufficiently large circle, the leading term dominates all lower terms.",r"For large \(R\), \(|a_n z^n|>\sum_{k<n}|a_k|R^k\) on \(|z|=R\). Thus the polynomial has the same zero count as \(a_n z^n\), namely \(n\).")],
test=[
q("Non-strict inequality",r"Why is \(|g|\le|f|\) not the standard sufficient hypothesis in Rouché's theorem?",r"Equality can allow the homotopy to pass through zero on the boundary.",r"The strict inequality guarantees boundary nonvanishing for the entire deformation. Without it, additional analysis is needed and the conclusion can fail."),
q("Zero on boundary",r"Why must the comparison be arranged so the relevant functions have no boundary zeros?",r"The zero count can jump when a zero crosses the contour.",r"A boundary zero makes the argument-principle winding undefined and destroys the homotopy certificate used in the proof."),
q("Poor comparison",r"If neither term dominates on the chosen circle, does Rouché imply that the zero counts differ?",r"Failure of a sufficient condition is not a negative conclusion.",r"No. It only means that this comparison and contour do not certify the count. A different comparison or contour may work.")],
application=[
q("Root localization",r"How can two Rouché counts localize polynomial roots to an annulus?",r"Count inside an inner and an outer circle.",r"Subtracting the certified counts gives exactly how many roots lie between the circles, without solving the polynomial."),
q("Perturbed characteristic equation",r"A characteristic polynomial \(p\) has a known zero count in a region. How can Rouché certify that modeling error \(h\) does not change it?",r"Bound \(|h|\) by the minimum boundary magnitude of \(p\).",r"If \(\max_C|h|<\min_C|p|\), then \(p+h\) and \(p\) have identical zero counts inside the boundary.")],
challenge=[
q("Two-scale count",r"For \(z^6+4z^2+1\), find useful circles on which different terms dominate and explain how to infer an annular root count.",r"Try a small circle where the constant dominates and a larger circle where \(z^6\) dominates.",r"Choose radii satisfying \(4R^2+R^6<1\) for the inner disk and \(4R^2+1<R^6\) for the outer disk. Rouché then gives zero inner roots and six outer roots, so all six lie in the intervening annulus."),
q("Comparison with a factor",r"Suppose \(f(z)=p(z)+h(z)\) and \(p\) has a multiple zero. Does Rouché preserve the multiplicity count under a small boundary perturbation?",r"Rouché counts zeros with multiplicity rather than tracking individual labels.",r"Yes. It preserves the total number counted with multiplicity inside the contour, even though a multiple zero may split into several nearby simple zeros.")])

DATA["IV/14"] = pack(
examples=[
ex(1,"Principal logarithm",r"""On \(\mathbb C\setminus(-\infty,0]\), define
\[
\operatorname{Log}z=\log|z|+i\operatorname{Arg}z,\qquad -\pi<\operatorname{Arg}z<\pi.
\]
This is holomorphic and satisfies \((\operatorname{Log}z)'=1/z\). The removed ray prevents a loop around zero from forcing the argument to jump by \(2\pi\)."""),
ex(4,"A square-root branch",r"""On the same slit plane, define
\[
\sqrt z=\exp\!\left(\tfrac12\operatorname{Log}z\right).
\]
Then \((\sqrt z)^2=z\), and the chosen branch has positive real value on the positive real axis. The second branch is its negative."""),
ex(7,"Why the punctured plane has no global logarithm",r"""If a holomorphic logarithm \(L\) existed on \(\mathbb C\setminus\{0\}\), then \(L'=1/z\). But
\[
\int_{|z|=1}\frac{dz}{z}=2\pi i\ne0,
\]
whereas the integral of a derivative around a closed curve is zero. Thus no single valued holomorphic logarithm exists on the punctured plane.""")],
standard=[
q("Principal value",r"Compute the principal logarithm of \(-i\).",r"Use principal argument \(-\pi/2\).",r"The value is \(-i\pi/2\)."),
q("Principal square root",r"Compute the principal square root of \(-1\).",r"Use principal logarithm with argument \(\pi\).",r"The principal square root is \(i\)."),
q("Branch interval",r"Give an argument interval defining a logarithm on the plane cut along the positive real axis.",r"Use any interval of length \(2\pi\) that excludes the cut direction.",r"For example, \(0<\arg z<2\pi\)."),
q("Complex power",r"On a chosen logarithm branch, define \(z^\alpha\).",r"Exponentiate \(\alpha\operatorname{Log}z\).",r"Set \(z^\alpha=\exp(\alpha\operatorname{Log}z)\) on the branch domain."),
q("Root branches",r"How many holomorphic branches of the \(n\)-th root differ by constant factors on a connected branch domain?",r"Multiply one branch by the \(n\)-th roots of unity.",r"There are \(n\) choices, obtained from one branch by factors \(e^{2\pi i k/n}\).")],
proof=[
q("Derivative of a logarithm branch",r"Prove that any holomorphic branch \(L\) with \(e^L=z\) satisfies \(L'=1/z\).",r"Differentiate the identity \(e^{L(z)}=z\).",r"The chain rule gives \(e^{L(z)}L'(z)=1\). Since \(e^{L(z)}=z\), one gets \(L'(z)=1/z\)."),
q("Branches differ by constants",r"Show that two logarithm branches on a connected domain differ by an integer multiple of \(2\pi i\).",r"Exponentiate their difference.",r"If \(L_1,L_2\) are branches, \(e^{L_1-L_2}=1\). The difference is continuous and takes values in the discrete set \(2\pi i\mathbb Z\), hence is constant on the connected domain."),
q("Root from logarithm",r"Prove that \(\exp(L/n)\) is an \(n\)-th root branch when \(L\) is a logarithm branch.",r"Raise the expression to the \(n\)-th power.",r"Its \(n\)-th power is \(e^L=z\), and holomorphicity follows by composition."),
q("No logarithm on a winding domain",r"Show that if a domain contains a closed curve with nonzero winding about zero, it cannot admit a holomorphic logarithm of \(z\).",r"A logarithm would have derivative \(1/z\).",r"The integral of its derivative around the curve would be zero, but \(\int dz/z=2\pi i\) times the nonzero winding number, a contradiction.")],
test=[
q("Branch crossing",r"Why is the principal logarithm discontinuous if one tries to include both sides of its cut with the same argument convention?",r"Approach a negative real point from above and below.",r"The principal arguments approach \(\pi\) and \(-\pi\), differing by \(2\pi\), so no continuous single valued extension crosses the cut."),
q("Punctured annulus",r"Does every annulus around zero admit a single valued logarithm?",r"An annulus contains loops winding once around zero.",r"No. The integral of \(1/z\) on such a loop is nonzero, obstructing a logarithm."),
q("Branch independence of powers",r"Is \(z^\alpha\) independent of logarithm branch for arbitrary complex \(\alpha\)?",r"Changing a logarithm by \(2\pi i k\) changes the exponential by a factor.",r"In general no. The factor is \(e^{2\pi i k\alpha}\), which equals one for every integer \(k\) only in special cases such as integer \(\alpha\).")],
application=[
q("Fractional power domain",r"Why is a slit plane a natural domain for \(z^{1/3}\)?",r"It supports a single valued logarithm.",r"Once a logarithm is fixed, \(z^{1/3}=e^{L/3}\) is holomorphic there, avoiding the monodromy caused by circling zero."),
q("Primitive of reciprocal",r"On what kind of region can \(1/z\) have a holomorphic primitive?",r"A primitive is a logarithm branch.",r"Exactly on regions where a logarithm branch exists; in particular, simply connected regions avoiding zero support such a primitive.")],
challenge=[
q("Branch on a sector",r"Construct a logarithm on the sector \(\alpha<\arg z<\beta\) when \(\beta-\alpha<2\pi\).",r"Choose the argument continuously in that interval.",r"Define \(L(z)=\log|z|+i\arg z\) with \(\arg z\in(\alpha,\beta)\). The sector cannot wrap fully around zero, so the argument is single valued."),
q("Monodromy of the square root",r"What happens to a locally chosen square root after analytic continuation once around zero?",r"The logarithm changes by \(2\pi i\).",r"Half the logarithm changes by \(\pi i\), so the exponential is multiplied by \(-1\). A second circuit returns to the original value.")])

DATA["IV/15"] = pack(
examples=[
ex(1,"Continuing the geometric series",r"""The series \(\sum_{n\ge0}z^n\) defines \(1/(1-z)\) only for \(|z|<1\). The rational formula, however, is holomorphic on \(\mathbb C\setminus\{1\}\) and agrees with the series on the disk. It therefore supplies an analytic continuation far beyond the original circle of convergence, except across the genuine singularity at \(1\)."""),
ex(4,"Continuation of a square root changes sheet",r"""Begin with a local square root near \(z=1\). Continue it along a loop encircling zero once. Locally write the root as \(e^{L/2}\). After the loop, the continued logarithm has gained \(2\pi i\), so the root has gained a factor \(e^{\pi i}=-1\). The germ returns to the starting point with the opposite value."""),
ex(7,"Uniqueness on overlaps",r"""Suppose two analytic continuations of the same germ are defined on overlapping connected regions. On a neighborhood where both agree with the original germ, their difference vanishes. The identity theorem then forces them to agree throughout the connected overlap. This is the local uniqueness mechanism behind analytic continuation.""")],
standard=[
q("Rational continuation",r"Give an analytic continuation of \(\sum_{n\ge0}z^n\) beyond \(|z|<1\).",r"Use its closed form.",r"The continuation is \(1/(1-z)\) on \(\mathbb C\setminus\{1\}\)."),
q("Continuation obstruction",r"What point blocks continuation of \(1/(1-z)\) as a holomorphic function?",r"Locate the pole.",r"The point \(z=1\) is a genuine pole and cannot be crossed by a holomorphic continuation of that function."),
q("Overlap rule",r"Two analytic elements agree on a nonempty open subset of a connected overlap. What follows?",r"Use the identity theorem.",r"They agree on the whole connected overlap."),
q("Loop effect",r"After one loop around zero, what happens to a continued square root?",r"Track the logarithm increment.",r"It changes sign."),
q("Two loops",r"What happens to that square root after two loops?",r"Apply the sign change twice.",r"It returns to the original branch value.")],
proof=[
q("Uniqueness of continuation",r"Prove uniqueness of analytic continuation along a fixed chain of overlapping connected neighborhoods.",r"Induct across the overlaps using the identity theorem.",r"Agreement on the initial germ forces agreement on the first overlap, then the next, and so on. Thus every step of the continuation chain is uniquely determined."),
q("Continuation preserves algebraic identities",r"If two analytic functions satisfy \(F^2=g\) on the initial germ and both sides continue, show the identity persists.",r"Continue the difference \(F^2-g\).",r"The difference is analytic and initially zero. Uniqueness and the identity theorem force it to remain zero wherever the continuation is defined."),
q("Path reversal",r"Show that continuation along a path followed by its reverse returns the original germ when all continuations exist uniquely along the path.",r"Use local uniqueness step by step in reverse order.",r"Each overlap transition is uniquely invertible by the same identity theorem argument, so retracing the chain recovers the starting analytic element."),
q("Simply connected monodromy principle",r"Explain why path independent continuation is expected on a simply connected region when continuation is possible along every path.",r"Homotope any two paths with common endpoints while avoiding singularities.",r"Local uniqueness makes the terminal germ stable under small path deformations. A homotopy between the paths then forces their terminal germs to agree.")],
test=[
q("Disconnected overlap",r"Why does agreement on one component of a disconnected overlap not force agreement on another component?",r"The identity theorem propagates through connectedness.",r"The functions may differ on another component because there is no connected analytic path of equality joining the components."),
q("Circle of convergence as barrier",r"Is the boundary of a Taylor disk always a natural barrier to analytic continuation?",r"Use the geometric series as a counterexample.",r"No. Its Taylor series stops at \(|z|=1\), but the function continues through most boundary points. The radius records the nearest singularity relative to the chosen center, not an automatic global barrier."),
q("Path dependence",r"Can analytic continuation around a loop return a different germ?",r"Use the square root around zero.",r"Yes. Multivalued analytic phenomena exhibit monodromy; the terminal germ can differ even at the same base point when the domain has nontrivial loops around branch points.")],
application=[
q("Extending local formulas",r"Why is analytic continuation useful when a power series converges only locally?",r"The locally defined analytic function may have compatible representations on overlapping regions.",r"Continuation transports the same analytic object beyond one convergence disk while preserving identities and derivatives on overlaps."),
q("Detecting branch structure",r"How can continuation around loops reveal a hidden Riemann surface?",r"Record how branch values permute after closed loops.",r"Nontrivial permutations show that one planar domain cannot support a single valued version. The collection of branches and their continuation rules points toward a covering or branched surface.")],
challenge=[
q("Logarithm monodromy",r"Describe the effect of one positive circuit around zero on an analytically continued logarithm.",r"Track the argument change.",r"The logarithm increases by \(2\pi i\). Repeated circuits add integer multiples of \(2\pi i\)."),
q("Algebraic branch permutation",r"For \(w^3=z\), describe the monodromy after one positive loop around zero.",r"A logarithm increment of \(2\pi i\) is divided by three.",r"Each cube root is multiplied by \(e^{2\pi i/3}\), cyclically permuting the three branches. Three loops return each branch to itself.")])

DATA["IV/16"] = pack(
examples=[
ex(1,"Upper half-plane to unit disk",r"""The Möbius map
\[
T(z)=\frac{z-i}{z+i}
\]
sends \(i\) to \(0\). If \(x\in\mathbb R\), then \(|x-i|=|x+i|\), so \(|T(x)|=1\). A point such as \(2i\) maps to \(1/3\), showing that the upper half-plane maps to the unit disk."""),
ex(4,"Three-point normalization",r"""The cross-ratio map
\[
T(z)=\frac{(z-z_1)(z_2-z_3)}{(z-z_3)(z_2-z_1)}
\]
sends \(z_1\mapsto0\), \(z_2\mapsto1\), and \(z_3\mapsto\infty\). Thus any three distinct points on the Riemann sphere can be normalized to \(0,1,\infty\), after which many geometric questions become simpler."""),
ex(7,"A line becomes a circle",r"""For \(T(z)=1/z\), the vertical line \(\operatorname{Re}z=1\) can be written \(z=1+iy\). If \(w=1/z=u+iv\), then solving \(z=1/w\) and imposing real part one gives
\[
\left(u-\tfrac12\right)^2+v^2=\tfrac14.
\]
Thus a line not through the pole maps to a circle through the origin.""")],
standard=[
q("Evaluate a map",r"For \(T(z)=(z-1)/(z+1)\), compute \(T(1)\), \(T(0)\), and \(T(\infty)\).",r"Use the leading coefficient ratio at infinity.",r"The values are \(0\), \(-1\), and \(1\)."),
q("Inverse map",r"Find the inverse of \(w=(z-i)/(z+i)\).",r"Solve algebraically for \(z\).",r"One obtains \(z=i(1+w)/(1-w)\)."),
q("Pole and infinity",r"For \(T(z)=(2z+3)/(z-4)\), where does \(4\) map, and where does infinity map?",r"Use the sphere convention.",r"The point \(4\) maps to infinity, and infinity maps to the leading coefficient ratio \(2\)."),
q("Determinant",r"Is \((2z+2)/(z+1)\) a genuine Möbius transformation?",r"Check \(ad-bc\).",r"No. The determinant is zero and the expression simplifies to the constant two away from the cancelled point."),
q("Fixed points",r"Find the fixed points of \(T(z)=1/z\) on the sphere.",r"Solve \(z=1/z\).",r"The finite fixed points are \(z=1\) and \(z=-1\).")],
proof=[
q("Inverse is Möbius",r"Prove that a Möbius transformation with nonzero determinant has a Möbius inverse.",r"Solve \(w=(az+b)/(cz+d)\) for \(z\).",r"Rearrangement gives \(z=(dw-b)/(-cw+a)\), whose determinant equals the original nonzero determinant up to sign."),
q("Composition closure",r"Show that the composition of two Möbius transformations is Möbius.",r"Represent each transformation by a nonsingular two by two matrix up to scalar.",r"Composition corresponds to matrix multiplication. The product remains nonsingular, so the resulting fractional linear map is Möbius."),
q("Generalized circles",r"Explain why Möbius transformations send circles and lines to circles or lines.",r"It suffices to check translations, nonzero scalings and rotations, and inversion.",r"Affine maps preserve circles and lines. Inversion maps generalized circles to generalized circles, and every Möbius transformation decomposes into these elementary maps."),
q("Three-point uniqueness",r"Prove that a Möbius transformation is uniquely determined by the images of three distinct points.",r"Compose two candidates with the inverse of one and study a map fixing three points.",r"A nonidentity Möbius map has at most two fixed points because its fixed-point equation is quadratic. Hence a map fixing three distinct sphere points is the identity, proving uniqueness.")],
test=[
q("Zero determinant",r"What fails when \(ad-bc=0\)?",r"The numerator and denominator become proportional.",r"The fractional expression is constant where defined and has no Möbius inverse, so it is not an automorphism of the sphere."),
q("Forgetting infinity",r"Why must infinity be included when discussing global Möbius maps?",r"Denominator zeros map naturally to infinity.",r"Adding infinity turns every nonsingular fractional linear expression into a bijective holomorphic map of the Riemann sphere."),
q("Interior versus boundary",r"If a Möbius map sends the real axis to the unit circle, is checking boundary images alone enough to know which half-plane maps inside?",r"Test one interior point.",r"No. The two complementary regions could be interchanged. Evaluating one point in the chosen half-plane determines the side.")],
application=[
q("Normalize a domain",r"Why map a half-plane to a disk before solving a boundary problem?",r"Standard theorems and kernels often have canonical disk forms.",r"A Möbius normalization transfers the geometry to a standard domain where symmetry and known formulas simplify analysis, then the result can be pulled back."),
q("Cross-ratio invariant",r"What geometric data can the cross-ratio preserve under Möbius transformations?",r"Apply the same normalization before and after the map.",r"The cross-ratio of four ordered sphere points is invariant, providing a coordinate-free quantity for comparing configurations.")],
challenge=[
q("Disk automorphism",r"Show that \(T_a(z)=(z-a)/(1-\overline a z)\) maps the unit disk to itself when \(|a|<1\).",r"Compute \(1-|T_a(z)|^2\).",r"One obtains \((1-|a|^2)(1-|z|^2)/|1-\overline a z|^2>0\) for \(|z|<1\), so the image lies in the disk; the inverse has the same form."),
q("Map three points",r"Construct a Möbius transformation sending \(-1,0,1\) to \(0,1,\infty\).",r"Use the cross-ratio formula or solve three equations.",r"The map \(T(z)=(z+1)/(1-z)\) sends \(-1\) to zero, \(0\) to one, and \(1\) to infinity.")])

DATA["IV/17"] = pack(
examples=[
ex(1,"A sector straightened by a power map",r"""On the sector \(0<\arg z<\pi/2\), the map \(w=z^2\) doubles arguments. Hence
\[
0<\arg w<\pi,
\]
so the sector maps conformally onto the upper half-plane. The derivative \(2z\) is nonzero on the sector, so local angles are preserved."""),
ex(4,"A strip mapped to the upper half-plane",r"""For the horizontal strip \(0<\operatorname{Im}z<\pi\), the exponential map satisfies
\[
\arg(e^z)=\operatorname{Im}z\in(0,\pi).
\]
Thus \(e^z\) maps the strip onto the upper half-plane. Restricting the imaginary width to \(2\pi\) or less is essential for injectivity."""),
ex(7,"Disk automorphism as a conformal normalizer",r"""For \(|a|<1\),
\[
\phi_a(z)=\frac{z-a}{1-\overline a z}
\]
is a conformal automorphism of the unit disk and sends \(a\) to \(0\). Its derivative never vanishes in the disk. This normalization lets one move an arbitrary interior point to the symmetric center before applying disk estimates.""")],
standard=[
q("Quadrant to half-plane",r"Find a simple conformal map from the first quadrant to the upper half-plane.",r"Double the argument.",r"The map \(w=z^2\) works."),
q("Strip to half-plane",r"Map \(0<\operatorname{Im}z<\pi\) to the upper half-plane.",r"Use the exponential.",r"The map \(w=e^z\) works."),
q("Half-plane to disk",r"Give a conformal map from the upper half-plane to the unit disk sending \(i\) to zero.",r"Use a Cayley transform.",r"The map \((z-i)/(z+i)\) works."),
q("Angle scaling",r"What angle does \(z^3\) assign to a sector of opening \(\pi/6\)?",r"Multiply arguments by three.",r"The image sector has opening \(\pi/2\)."),
q("Derivative test",r"At which point does \(z^2\) fail to be conformal as a local map?",r"Find where the derivative vanishes.",r"At \(z=0\), since the derivative is \(2z\).")],
proof=[
q("Nonzero derivative preserves angles",r"Prove local conformality of a holomorphic function where its derivative is nonzero.",r"Use the first order expansion.",r"Near \(z_0\), \(f(z_0+h)-f(z_0)=f'(z_0)h+o(|h|)\). The leading multiplication by a nonzero complex number is a rotation-dilation, so tangent angles are preserved in the limit."),
q("Inverse conformality",r"If a holomorphic injective map has nonzero derivative, show its local inverse is holomorphic and conformal.",r"Use the complex inverse function theorem.",r"The inverse derivative is \(1/f'(z)\), which is nonzero. Hence the inverse is holomorphic and angle preserving locally."),
q("Composition",r"Show that a composition of conformal maps is conformal where both are defined.",r"Use the chain rule.",r"The derivative of the composition is the product of two nonzero complex derivatives, hence is nonzero and represents the composition of two rotation-dilations."),
q("Harmonic pullback",r"Explain why composing a harmonic function with a conformal coordinate change preserves harmonicity in two dimensions.",r"Use the Laplacian transformation under a holomorphic map.",r"The Laplacian picks up the positive factor \(|f'|^2\). Thus if the original Laplacian is zero, the pulled back one is also zero.")],
test=[
q("Derivative zero",r"Is \(z^2\) conformal at zero?",r"Local angle preservation requires a nonzero derivative.",r"No. The derivative vanishes and small angles are doubled rather than preserved."),
q("Holomorphic but not injective globally",r"Does nonzero derivative everywhere guarantee global injectivity?",r"Consider the exponential.",r"No. The exponential has nonzero derivative everywhere but is periodic, so it is not globally injective on the whole plane."),
q("Boundary correspondence",r"Does a conformal map automatically extend continuously to every boundary point of arbitrary domains?",r"Boundary regularity requires extra hypotheses.",r"No. Interior conformality alone does not guarantee a well behaved boundary extension.")],
application=[
q("Dirichlet transfer",r"How can a conformal map help solve a planar Dirichlet problem?",r"Move the domain to one with a known Poisson kernel.",r"Solve the harmonic boundary problem in the standard domain and compose with the conformal inverse. Harmonicity is preserved by the coordinate change."),
q("Slit normalization",r"Why are power and square-root maps useful for slit domains?",r"They change argument range and can unfold a cut.",r"A suitable branch of a fractional power converts the slit geometry into a half-plane or sector where canonical conformal tools apply.")],
challenge=[
q("Strip to disk",r"Construct a conformal map from \(0<\operatorname{Im}z<\pi\) to the unit disk.",r"First exponentiate to the upper half-plane, then apply a Cayley transform.",r"One choice is \(w=(e^z-i)/(e^z+i)\)."),
q("Sector to disk",r"Map the sector \(0<\arg z<\alpha\) conformally to the unit disk for \(0<\alpha<2\pi\).",r"First use a power to reach the upper half-plane.",r"The power \(z^{\pi/\alpha}\) maps the sector to the upper half-plane on a chosen branch; composing with a Cayley transform maps it to the disk.")])

DATA["IV/18"] = pack(
examples=[
ex(1,"Interior angle determines the exponent",r"""Near a prevertex \(x_k\), a Schwarz--Christoffel derivative has local form
\[
f'(z)\sim C(z-x_k)^{\alpha_k/\pi-1},
\]
where \(\alpha_k\) is the polygon interior angle. Integrating gives \(f(z)-f(x_k)\sim C'(z-x_k)^{\alpha_k/\pi}\), so a half-plane angle \(\pi\) is transformed into the polygon angle \(\alpha_k\)."""),
ex(4,"Right angles give square-root factors",r"""For a rectangle, every finite vertex has interior angle \(\pi/2\), hence exponent
\[
\frac{\alpha}{\pi}-1=-\frac12.
\]
After normalizing three prevertices, the derivative therefore contains inverse square-root factors. Integrating leads to an elliptic integral, explaining why rectangle maps naturally connect Schwarz--Christoffel theory with elliptic functions."""),
ex(7,"Triangle exponents",r"""For a triangle with angles \(\alpha_1,\alpha_2,\alpha_3\), the derivative has factors \((z-x_k)^{\alpha_k/\pi-1}\). Since \(\alpha_1+\alpha_2+\alpha_3=\pi\), the three exponents sum to \(-2\). This global balance matches the behavior required at infinity for a half-plane-to-polygon map.""")],
standard=[
q("Right angle exponent",r"Find the Schwarz--Christoffel exponent for an interior angle \(\pi/2\).",r"Compute \(\alpha/\pi-1\).",r"The exponent is \(-1/2\)."),
q("Equilateral triangle",r"Find the exponent at each vertex of an equilateral triangle.",r"Each interior angle is \(\pi/3\).",r"Each exponent is \(-2/3\)."),
q("Reflex vertex",r"Find the exponent for interior angle \(3\pi/2\).",r"Use the same formula.",r"The exponent is \(1/2\), reflecting a reflex corner."),
q("Straight angle",r"What exponent corresponds to interior angle \(\pi\)?",r"Substitute directly.",r"The exponent is zero, so no singular power factor is needed for a straight continuation."),
q("Triangle sum",r"What is the sum of the three derivative exponents for a triangle?",r"Use the angle sum \(\pi\).",r"The sum is \((\pi/\pi)-3=-2\).")],
proof=[
q("Local corner law",r"Derive the local angle law from \(f'(z)\sim C(z-x_k)^{\beta_k-1}\).",r"Integrate the leading power.",r"Integration gives \(f(z)-f(x_k)\sim (C/\beta_k)(z-x_k)^{\beta_k}\). Arguments are multiplied by \(\beta_k\), so the half-plane angle \(\pi\) becomes \(\beta_k\pi=\alpha_k\)."),
q("Polygon exponent sum",r"For an \(n\)-gon, show that the finite-vertex exponents \(\alpha_k/\pi-1\) sum to \(-2\).",r"Use the polygon interior angle sum.",r"Since \(\sum\alpha_k=(n-2)\pi\), the exponent sum is \((n-2)-n=-2\)."),
q("Affine freedom",r"Explain why multiplying a Schwarz--Christoffel map by a nonzero constant and adding a constant preserves the polygon shape up to similarity and translation.",r"Differentiate the transformed map.",r"The derivative is multiplied by one nonzero complex constant, which rotates and scales all edges uniformly; the additive constant translates the image."),
q("Prevertex order",r"Why must the real prevertices occur in the same cyclic order as the polygon vertices for a standard upper-half-plane map?",r"Follow the boundary image of the oriented real axis.",r"The real boundary is traversed monotonically through the prevertices. Continuity maps successive real intervals to successive polygon edges, fixing the cyclic vertex order.")],
test=[
q("Wrong exponent",r"What geometric defect results if a right-angle vertex is assigned exponent \(-1/3\) instead of \(-1/2\)?",r"Convert the exponent back to an angle.",r"The corresponding angle factor is \(2/3\), giving an interior angle \(2\pi/3\) rather than \(\pi/2\)."),
q("Repeated prevertices",r"Can two distinct finite polygon vertices be assigned the same ordinary prevertex in a nondegenerate Schwarz--Christoffel map?",r"A single boundary point has only one local turning exponent.",r"Not in the standard nondegenerate setup. Coincident prevertices signal a limiting or degenerate polygon configuration."),
q("Ignoring normalization",r"Why are prevertex positions not all independent parameters?",r"The upper half-plane has a three-real-parameter Möbius automorphism group.",r"Three real degrees of freedom can be normalized, commonly by fixing three prevertices. Failing to account for this produces redundant parameters.")],
application=[
q("Numerical parameter problem",r"What must be solved numerically when mapping the half-plane to a specified polygon with more than three vertices?",r"Angles determine exponents, but side lengths determine prevertex spacing.",r"One solves nonlinear equations for the remaining prevertices and scale so that integrals between consecutive prevertices reproduce the prescribed side lengths."),
q("Flow around polygons",r"Why are Schwarz--Christoffel maps useful in two dimensional potential flow?",r"Conformal maps preserve harmonic structure and angles.",r"A difficult polygonal boundary can be mapped to a half-plane where analytic potentials are simple, then transported back to the physical polygonal domain.")],
challenge=[
q("Rectangle and elliptic integrals",r"Explain why the rectangle map leads to an integral with four square-root branch points.",r"Each right angle contributes exponent \(-1/2\).",r"With four finite prevertices in a symmetric normalization, the derivative is proportional to the reciprocal square root of a quartic polynomial. Integrating this differential is an elliptic integral."),
q("Vertex at infinity",r"How can placing one polygon vertex at infinity simplify a Schwarz--Christoffel formula?",r"Use Möbius freedom to send a convenient prevertex to infinity.",r"Its factor is absorbed into the behavior at infinity, reducing the number of explicit finite factors and often simplifying both the integral and the parameter equations.")])
