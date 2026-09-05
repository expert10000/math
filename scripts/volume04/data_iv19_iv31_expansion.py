from __future__ import annotations

def ex(after, title, body):
    return {"after_section": after, "title": title, "body": body}

def q(title, prompt, hint, solution):
    return {"title": title, "prompt": prompt, "hint": hint, "solution": solution}

def pack(examples, standard, proof, test, application, challenge):
    return {"examples": examples, "exercises": {
        "standard": standard, "proof": proof, "test": test,
        "application": application, "challenge": challenge,
    }}

DATA = {}

DATA["IV/19"] = pack(
examples=[
ex(1,"Gamma at half integers",r"""Starting from
\[
\Gamma\!\left(\frac12\right)=\int_0^\infty t^{-1/2}e^{-t}\,dt=\sqrt{\pi},
\]
the functional equation gives
\[
\Gamma\!\left(\frac32\right)=\frac12\sqrt{\pi},\qquad
\Gamma\!\left(\frac52\right)=\frac34\sqrt{\pi}.
\]
More generally,
\[
\Gamma\!\left(n+\frac12\right)=\frac{(2n)!}{4^n n!}\sqrt{\pi}.
\]
This converts many Gaussian and trigonometric integrals into factorial calculations."""),
ex(4,"A pole and its residue",r"""Use \(\Gamma(s+1)=s\Gamma(s)\). Since \(\Gamma(s+1)\to1\) as \(s\to0\),
\[
\Gamma(s)=\frac{\Gamma(s+1)}{s}=\frac1s+O(1).
\]
Hence \(s=0\) is a simple pole with residue \(1\). Repeating the functional equation yields
\[
\operatorname{Res}_{s=-n}\Gamma(s)=\frac{(-1)^n}{n!}.
\]
The local computation shows exactly how meromorphic continuation records the factorial recursion at negative integers."""),
ex(7,"A Gamma integral with scaling",r"""For \(a>0\) and \(\Re s>0\), substitute \(u=at\) in
\[
I=\int_0^\infty t^{s-1}e^{-at}\,dt.
\]
Then
\[
I=a^{-s}\int_0^\infty u^{s-1}e^{-u}\,du=a^{-s}\Gamma(s).
\]
For example, \(\int_0^\infty t^{3/2}e^{-2t}\,dt=2^{-5/2}\Gamma(5/2)=3\sqrt{\pi}/(2^{9/2})\).""")],
standard=[
q("Factorial value",r"Compute \(\Gamma(7)\).",r"Use \(\Gamma(n+1)=n!\).",r"\(\Gamma(7)=6!=720\)."),
q("Half integer",r"Compute \(\Gamma(7/2)\).",r"Step down repeatedly to \(\Gamma(1/2)\).",r"\(\Gamma(7/2)=(5/2)(3/2)(1/2)\sqrt{\pi}=15\sqrt{\pi}/8\)."),
q("Scaled integral",r"Evaluate \(\int_0^\infty t^2e^{-3t}\,dt\).",r"Use the scaled Gamma integral with \(s=3\).",r"The value is \(3^{-3}\Gamma(3)=2/27\)."),
q("Residue",r"Find \(\operatorname{Res}_{s=-3}\Gamma(s)\).",r"Use the residue formula at negative integers.",r"The residue is \((-1)^3/3!=-1/6\)."),
q("Digamma recurrence",r"From the Gamma functional equation derive a recurrence for \(\psi=\Gamma'/\Gamma\).",r"Take a logarithmic derivative.",r"\(\psi(s+1)=\psi(s)+1/s\).")],
proof=[
q("Functional equation",r"Prove \(\Gamma(s+1)=s\Gamma(s)\) for \(\Re s>0\).",r"Integrate by parts and check both endpoint terms.",r"Take \(u=t^s\) and \(dv=e^{-t}dt\). The boundary terms vanish, leaving \(s\int_0^\infty t^{s-1}e^{-t}dt\)."),
q("Holomorphy",r"Explain why the Euler integral defines a holomorphic function on \(\Re s>0\).",r"Work on a compact vertical strip inside the half plane.",r"On compact subsets, \(t^{s-1}e^{-t}\) and its parameter derivatives are dominated by integrable functions near zero and infinity, so differentiation under the integral sign is valid."),
q("Pole locations",r"Prove that the functional equation gives only simple poles at the nonpositive integers.",r"Shift the argument into the right half plane.",r"For sufficiently large \(N\), write \(\Gamma(s)=\Gamma(s+N)/(s(s+1)\cdots(s+N-1))\). The numerator is holomorphic and nonzero at the relevant points, while each denominator factor occurs once."),
q("Residue recursion",r"Prove \(\operatorname{Res}_{s=-n}\Gamma(s)=(-1)^n/n!\).",r"Compare residues in \(\Gamma(s+1)=s\Gamma(s)\).",r"Starting with residue \(1\) at zero, each step to the left divides by the value of \(s\) at the new pole, producing alternating signs and factorial denominators.")],
test=[
q("Convergence at zero",r"Does the Euler integral converge for \(\Re s=0\)?",r"Inspect the magnitude of \(t^{s-1}\) near zero.",r"In general no. Its magnitude behaves like \(t^{-1}\), whose integral diverges logarithmically near zero."),
q("Entire or meromorphic",r"Is \(\Gamma\) entire after continuation?",r"Recall the values forced by the functional equation at nonpositive integers.",r"No. It is meromorphic with simple poles at \(0,-1,-2,\ldots\)."),
q("Zeros of Gamma",r"Can the functional equation alone permit a zero of \(\Gamma\) in the right half plane?",r"Use the Euler integral only for positive real arguments, then think about the reciprocal Gamma function.",r"The integral is positive on the positive real axis, but excluding complex zeros requires additional theory. One should not infer zero freeness on the whole half plane from positivity on one line.")],
application=[
q("Gaussian moment",r"Evaluate \(\int_0^\infty x^4e^{-x^2}\,dx\).",r"Set \(t=x^2\).",r"The integral becomes \(\frac12\Gamma(5/2)=3\sqrt{\pi}/8\)."),
q("Factorial asymptotics",r"Explain what Stirling asymptotics say about \(\Gamma(n+1)\) for large integers \(n\).",r"Translate the asymptotic formula for Gamma to factorials.",r"It gives \(n!\sim\sqrt{2\pi n}(n/e)^n\), quantifying the factorial growth encoded by Gamma.")],
challenge=[
q("Reflection preparation",r"Why is a product such as \(\Gamma(s)\Gamma(1-s)\) natural when seeking identities symmetric under \(s\mapsto1-s\)?",r"Apply the involution twice and compare pole sets.",r"The product is invariant under replacing \(s\) by \(1-s\). Its poles occur at integers from the two Gamma factors, matching the pole pattern of trigonometric reciprocals such as \(1/\sin(\pi s)\)."),
q("Meromorphic continuation by patches",r"Explain why formulas obtained by shifting by different integers define one continuation rather than conflicting functions.",r"Compare them on a region where both are defined.",r"Repeated use of the functional equation shows the shifted formulas agree on overlaps. The identity theorem then glues them into a unique meromorphic continuation.")])

DATA["IV/20"] = pack(
examples=[
ex(1,"Beta at integer parameters",r"""For positive integers \(m,n\),
\[
B(m,n)=\frac{\Gamma(m)\Gamma(n)}{\Gamma(m+n)}
=\frac{(m-1)!(n-1)!}{(m+n-1)!}.
\]
Thus \(B(3,4)=2!3!/6!=1/60\). Directly, this says
\[
\int_0^1 t^2(1-t)^3\,dt=\frac1{60}.
\]
The Gamma quotient turns a two-endpoint integral into a factorial identity."""),
ex(4,"A sine power integral",r"""Using \(t=\sin^2\theta\),
\[
\int_0^{\pi/2}\sin^{a-1}\theta\cos^{b-1}\theta\,d\theta
=\frac12B\!\left(\frac a2,\frac b2\right).
\]
With \(a=6\) and \(b=2\),
\[
\int_0^{\pi/2}\sin^5\theta\cos\theta\,d\theta
=\frac12 B(3,1)=\frac16.
\]
This agrees with the elementary substitution \(u=\sin\theta\)."""),
ex(7,"Differentiating a parameter",r"""For \(\Re x,\Re y>0\), differentiate the Beta integral with respect to \(x\):
\[
\frac{\partial B}{\partial x}(x,y)
=\int_0^1 t^{x-1}(1-t)^{y-1}\log t\,dt.
\]
From the Gamma quotient,
\[
\frac{\partial B}{\partial x}(x,y)
=B(x,y)\bigl(\psi(x)-\psi(x+y)\bigr).
\]
At \((1,1)\), this gives \(\int_0^1\log t\,dt=-1\).""")],
standard=[
q("Simple Beta value",r"Compute \(B(2,3)\).",r"Use the Gamma quotient.",r"\(B(2,3)=1!2!/4!=1/12\)."),
q("Symmetry",r"Compute \(B(5,2)\) from \(B(2,5)\).",r"Use \(B(x,y)=B(y,x)\).",r"The two values are equal, and both are \(1!4!/6!=1/30\)."),
q("Trigonometric integral",r"Evaluate \(\int_0^{\pi/2}\sin^2\theta\,d\theta\) using Beta.",r"Use \(a=3\) and \(b=1\).",r"The value is \(\frac12B(3/2,1/2)=\pi/4\)."),
q("Recurrence",r"Express \(B(x+1,y)\) in terms of \(B(x,y)\).",r"Use the Gamma functional equation.",r"\(B(x+1,y)=xB(x,y)/(x+y)\)."),
q("Log integral",r"Evaluate \(\int_0^1 t\log t\,dt\).",r"Differentiate \(\int_0^1 t^{x-1}dt=1/x\) at \(x=2\).",r"The value is \(-1/4\).")],
proof=[
q("Symmetry proof",r"Prove \(B(x,y)=B(y,x)\) directly from the integral.",r"Use \(u=1-t\).",r"The substitution exchanges the factors \(t^{x-1}\) and \((1-t)^{y-1}\) and preserves the interval."),
q("Beta Gamma identity",r"Prove the Beta Gamma identity from the product of two Gamma integrals.",r"Use \(u=rt\) and \(v=r(1-t)\).",r"The first quadrant transforms to \(r>0\), \(0<t<1\) with Jacobian \(r\). The product factors as \(\Gamma(x+y)B(x,y)\)."),
q("Trigonometric form",r"Derive the trigonometric Beta formula.",r"Set \(t=\sin^2\theta\).",r"The differential contributes \(2\sin\theta\cos\theta\,d\theta\), and the remaining powers combine to give the stated half Beta integral."),
q("Recurrence proof",r"Prove the recurrence for \(B(x+1,y)\).",r"Apply the Gamma quotient to both sides.",r"Use \(\Gamma(x+1)=x\Gamma(x)\) and \(\Gamma(x+y+1)=(x+y)\Gamma(x+y)\).")],
test=[
q("Endpoint failure",r"What happens to the defining Beta integral if \(\Re x\le0\)?",r"Inspect the endpoint \(t=0\).",r"The factor \(t^{x-1}\) is generally not integrable there, so the defining integral can fail even though meromorphic continuation may still exist."),
q("Symmetry domain",r"Does the symmetry identity disappear after meromorphic continuation?",r"Compare the Gamma quotient under swapping variables.",r"No. The quotient is symmetric wherever both sides are defined, and continuation preserves the identity meromorphically."),
q("Differentiate without control",r"May one always differentiate the Beta integral with respect to a parameter at the boundary of its convergence region?",r"Check for a common integrable majorant.",r"No. Differentiation under the integral requires uniform integrability control. Boundary parameters can introduce nonintegrable logarithmic singularities.")],
application=[
q("Probability normalization",r"Why does \(1/B(a,b)\) normalize the density \(t^{a-1}(1-t)^{b-1}\) on \((0,1)\)?",r"Integrate the density kernel.",r"Its integral is exactly \(B(a,b)\), so division by this value makes the total mass equal to one."),
q("Central binomial coefficient",r"Explain why half-integer Gamma values naturally produce central binomial coefficients.",r"Insert \(\Gamma(n+1/2)\) into a Beta quotient.",r"The half-integer formula contains \((2n)!/(4^n n!)\), the factorial ratio underlying \(\binom{2n}{n}\).")],
challenge=[
q("Duplication route",r"Sketch how Beta identities can lead to the Gamma duplication formula.",r"Use a trigonometric Beta integral and double-angle substitutions.",r"Express the same integral in two ways, one involving \(B(s,s)\) and another involving a half-integer Beta value, then translate both through Gamma quotients and simplify."),
q("Parameter second derivative",r"What integral appears after differentiating \(B(x,y)\) twice with respect to \(x\)?",r"Differentiate the factor \(t^{x-1}\) twice.",r"The integral becomes \(\int_0^1 t^{x-1}(1-t)^{y-1}(\log t)^2dt\), linked on the Gamma side to digamma and trigamma terms.")])

DATA["IV/21"] = pack(
examples=[
ex(1,"Keyhole evaluation of a rational power integral",r"""Fix \(0<a<1\) and use the branch \(0<\arg z<2\pi\) for \(z^{a-1}\). For
\[
f(z)=\frac{z^{a-1}}{1+z},
\]
the upper bank contributes \(I=\int_0^\infty x^{a-1}/(1+x)\,dx\), while the lower bank contributes \(-e^{2\pi i(a-1)}I\). The only enclosed pole is at \(-1\), whose residue is \(e^{i\pi(a-1)}\). Hence
\[
(1-e^{2\pi ia})I=2\pi i e^{i\pi(a-1)},
\]
which simplifies to \(I=\pi/\sin(\pi a)\)."""),
ex(4,"Why both circular arcs vanish",r"""For the same integrand, on the outer circle \(|z|=R\),
\[
|f(z)|=O(R^{a-2}),
\]
so arc length \(O(R)\) gives contribution \(O(R^{a-1})\to0\) because \(a<1\). On the inner circle \(|z|=\varepsilon\),
\[
|f(z)|=O(\varepsilon^{a-1}),
\]
so the contribution is \(O(\varepsilon^a)\to0\) because \(a>0\). These two inequalities explain the exact parameter window \(0<a<1\)."""),
ex(7,"Producing a logarithm by parameter differentiation",r"""Differentiate
\[
I(a)=\int_0^\infty \frac{x^{a-1}}{1+x}\,dx=\frac{\pi}{\sin(\pi a)}
\]
for \(0<a<1\). Then
\[
\int_0^\infty \frac{x^{a-1}\log x}{1+x}\,dx
=-\pi^2\frac{\cos(\pi a)}{\sin^2(\pi a)}.
\]
At \(a=1/2\), the right side vanishes, reflecting the symmetry \(x\mapsto1/x\).""")],
standard=[
q("Jump factor",r"For the branch \(0<\arg z<2\pi\), find the ratio of lower-bank to upper-bank values of \(z^\alpha\) on the positive axis.",r"The arguments are \(2\pi\) and \(0\).",r"The ratio is \(e^{2\pi i\alpha}\)."),
q("Outer arc order",r"If \(f(z)=z^{a-1}/(1+z)\), what is the order of the outer-circle integral?",r"Multiply the magnitude estimate by arc length.",r"It is \(O(R^{a-1})\), so it vanishes when \(a<1\)."),
q("Inner arc order",r"For the same integrand, what is the inner-circle order?",r"Near zero the denominator is bounded away from zero.",r"The contribution is \(O(\varepsilon^a)\), so it vanishes when \(a>0\)."),
q("Pole residue",r"Find the residue of \(z^{a-1}/(1+z)\) at \(z=-1\) for \(0<\arg z<2\pi\).",r"Use \(\arg(-1)=\pi\).",r"The residue is \((-1)^{a-1}=e^{i\pi(a-1)}\) on the chosen branch."),
q("Logarithmic derivative",r"Differentiate \(x^{a-1}\) with respect to \(a\).",r"Write the power as an exponential.",r"The derivative is \(x^{a-1}\log x\).")],
proof=[
q("Keyhole reduction",r"Prove that the two banks combine into a scalar jump factor times one real integral.",r"Track the opposite orientation on the lower bank.",r"The lower bank runs from large radius to small radius and carries the branch phase. Reversing its limits produces a minus sign, so the sum is the upper integral times one minus the phase factor."),
q("Parameter window",r"Prove that \(0<a<1\) is exactly the range making both circular arcs vanish for \(z^{a-1}/(1+z)\).",r"Estimate separately at zero and infinity.",r"The inner contribution behaves like \(\varepsilon^a\), requiring \(a>0\); the outer contribution behaves like \(R^{a-1}\), requiring \(a<1\)."),
q("Orientation sign",r"Explain rigorously why the lower-bank integral has the opposite sign from the upper-bank integral after parametrization.",r"Write the lower bank as \(z=x e^{2\pi i}\) with decreasing \(x\).",r"Its parameter runs from \(R\) down to \(\varepsilon\), so reversing the limits contributes the negative sign."),
q("Differentiate under the integral",r"Give a justification for differentiating the keyhole identity with respect to \(a\) on a compact subinterval of \((0,1)\).",r"Find one integrable bound for the differentiated real integrand.",r"On a compact parameter interval \([\delta,1-\delta]\), the derivative is bounded by a constant times \((x^{\delta-1}+x^{-\delta})|\log x|/(1+x)\), which is integrable at zero and infinity.")],
test=[
q("Wrong branch",r"What is wrong with using a keyhole contour before specifying a branch of \(z^\alpha\)?",r"The boundary values on the two banks are branch dependent.",r"Without a branch, the integrand is not single valued on the contour domain, so neither the jump factor nor the residue values are determined."),
q("Pole on the cut",r"Can the standard residue argument be used unchanged if a pole lies on the branch cut?",r"The contour would pass through a singularity.",r"No. One must indent around the pole, use a principal value prescription, or choose a different cut or contour."),
q("Arc estimate failure",r"What fails when \(a\ge1\) in the standard keyhole example?",r"Inspect the outer-circle bound.",r"The estimate \(O(R^{a-1})\) no longer tends to zero, so the contour does not reduce to just the bank integrals and residues.")],
application=[
q("Mellin transform",r"Explain why keyhole contours naturally evaluate Mellin-type integrals.",r"Mellin kernels are complex powers.",r"A Mellin kernel \(x^{s-1}\) acquires a controlled phase across a branch cut, so the jump converts a contour integral into the desired real Mellin integral."),
q("Branch-cut logarithms",r"How can one create integrals containing \((\log x)^2\)?",r"Differentiate twice with respect to the exponent.",r"Two parameter derivatives of \(x^{a-1}\) produce \(x^{a-1}(\log x)^2\), while the differentiated closed form provides the evaluation.")],
challenge=[
q("Hankel contour",r"Why is a Hankel contour around the negative real axis useful for reciprocal Gamma representations?",r"Think about the jump of a complex power and exponential decay.",r"The power has a simple phase jump across the negative axis while \(e^z\) decays along the two rays, producing a contour representation closely adapted to \(1/\Gamma(s)\)."),
q("Wedge variant",r"How would the jump factor change if the branch cut were bounded by arguments \(\theta_0\) and \(\theta_0+2\pi\)?",r"Evaluate \(z^\alpha\) on the two boundary arguments.",r"Both values gain a common factor \(e^{i\alpha\theta_0}\), while their ratio remains \(e^{2\pi i\alpha}\). The essential jump is therefore unchanged.")])

DATA["IV/22"] = pack(
examples=[
ex(1,"Two local square-root branches",r"""On a disk avoiding the origin, choose a holomorphic logarithm and set
\[
\sqrt z=\exp\!\left(\frac12\operatorname{Log}z\right).
\]
The second branch is its negative. Continuing the first branch once around the origin changes \(\operatorname{Log}z\) by \(2\pi i\), hence multiplies the square root by \(e^{\pi i}=-1\). The endpoint has the same base coordinate but the opposite germ, which is precisely why the surface of germs contains two points over a generic base point."""),
ex(4,"The logarithm surface as infinitely many sheets",r"""A germ of \(\log z\) near \(1\) has values differing by \(2\pi i k\). Continuing once counterclockwise around zero sends the value \(0\) at \(1\) to \(2\pi i\). After \(m\) turns it becomes \(2\pi i m\). Thus the maximal continuation has infinitely many sheets, naturally indexed by the integer winding number."""),
ex(7,"A coordinate near a branch point",r"""For the algebraic relation \(w^2=z\), the projection to the \(z\)-plane is not a local coordinate at \((0,0)\). Instead use \(w\) itself as the surface coordinate. Then the projection is
\[
z=w^2.
\]
The surface is perfectly smooth at the point even though the projection ramifies there. This separates intrinsic smoothness of the Riemann surface from singular behavior of a chosen projection.""")],
standard=[
q("Square-root monodromy",r"What happens to a chosen branch of \(\sqrt z\) after one loop around zero?",r"Track the logarithm change by \(2\pi i\).",r"The square root changes sign."),
q("Logarithm monodromy",r"What happens to \(\log z\) after one positive loop around zero?",r"Use the argument increment.",r"Its value increases by \(2\pi i\)."),
q("Fiber size",r"How many germs of \(\sqrt z\) lie over a generic nonzero point?",r"Solve \(w^2=z\).",r"There are two, corresponding to the two square roots."),
q("Local coordinate",r"For \(w^2=z\) near the branch point, which variable is a good surface coordinate?",r"Choose the variable in which the relation has no branching.",r"The coordinate \(w\) is good; the projection is then \(w\mapsto w^2\)."),
q("Single-valued lift",r"Why is the square root single valued on its two-sheeted surface?",r"A surface point remembers the branch germ.",r"Evaluating the recorded germ gives one unambiguous value at each surface point.")],
proof=[
q("Germ charts",r"Explain how representatives of analytic germs define local charts on the surface of germs.",r"Use one representative on a small disk.",r"Nearby points are assigned the germs of the same holomorphic representative. Projection to the disk is one to one on that neighborhood and gives the chart."),
q("Holomorphic transitions",r"Prove that transition maps between overlapping germ charts are holomorphic.",r"Both charts use the same base coordinate where the representatives agree.",r"On overlap the projection coordinates agree, so the transition is the identity on an open plane set and hence holomorphic."),
q("Maximal continuation connectedness",r"Why is the surface generated from one germ by analytic continuation naturally connected?",r"Every point is reached along a continuation path from the initial germ.",r"The lifted continuation path lies in the germ surface and connects the initial point to the target point, so all generated points lie in one connected component."),
q("Intrinsic holomorphy",r"Show that the definition of a holomorphic function on a Riemann surface is independent of the chosen chart.",r"Insert a holomorphic transition map.",r"If the coordinate expression is holomorphic in one chart, composing with a biholomorphic transition map gives a holomorphic expression in every compatible chart.")],
test=[
q("Plane only",r"Can a globally single-valued square root exist on \(\mathbb C^*\)?",r"Continue around the unit circle.",r"No. One loop changes the sign, contradicting single valuedness."),
q("Branch point as surface singularity",r"Is the point over \(z=0\) on \(w^2=z\) singular as a Riemann-surface point?",r"Use \(w\) as a coordinate.",r"No. The surface is smooth there; only the projection to the \(z\)-plane is ramified."),
q("One sheet for logarithm",r"Can the maximal logarithm surface have finitely many sheets?",r"Count values after repeated loops.",r"No. Each winding adds a distinct multiple of \(2\pi i\), giving infinitely many sheets.")],
application=[
q("Inverse functions",r"Why do Riemann surfaces help with multivalued inverse functions?",r"Each local inverse branch is a germ.",r"The surface separates different inverse germs lying over the same base point, turning the multivalued inverse into an ordinary holomorphic function upstairs."),
q("Algebraic functions",r"How does the surface viewpoint resolve the ambiguity of an algebraic relation such as \(w^3=z(z-1)\)?",r"Treat each compatible local solution as a sheet.",r"Local roots glue into a surface on which \(w\) is single valued; branching is encoded in the projection to the \(z\)-sphere.")],
challenge=[
q("Continuation obstruction",r"What topological feature of the base detects whether a local logarithm can be continued single valued globally?",r"Look at loops around the missing origin.",r"Nontrivial winding around zero creates nonzero logarithmic monodromy. A simply connected domain avoiding zero removes that obstruction."),
q("Surface versus branch cut",r"Compare using a branch cut with using the full Riemann surface for \(\log z\).",r"A branch cut discards paths, while the surface retains them.",r"A cut selects one sheet on a simply connected domain and sacrifices continuity across the cut. The Riemann surface keeps all continuations simultaneously and records their sheet changes geometrically.")])

DATA["IV/23"] = pack(
examples=[
ex(1,"Lifting a loop under the exponential map",r"""Consider \(p(w)=e^w\) and the unit-circle loop \(\gamma(t)=e^{2\pi it}\). Starting at \(w_0=0\), the lift
\[
\widetilde\gamma(t)=2\pi it
\]
satisfies \(e^{\widetilde\gamma(t)}=\gamma(t)\). Its endpoint is \(2\pi i\), not \(0\). Thus a closed base loop can lift to a path joining different points in the same fiber, and the endpoint records monodromy."""),
ex(4,"Cyclic monodromy of a power map",r"""For \(p(w)=w^n\) on \(\mathbb C^*\), the fiber over \(1\) consists of \(e^{2\pi ik/n}\). A positive loop once around zero lifts from the root \(e^{2\pi ik/n}\) to \(e^{2\pi i(k+1)/n}\). Hence the monodromy permutation is the \(n\)-cycle
\[
(0\ 1\ \cdots\ n-1).
\]
After \(n\) turns the lifted path closes."""),
ex(7,"Deck transformations of the exponential covering",r"""Every translation
\[
T_k(w)=w+2\pi i k
\]
satisfies \(e^{T_k(w)}=e^w\), so it is a deck transformation. Conversely, a deck transformation must send \(0\) to another point of the fiber over \(1\), hence to \(2\pi i k\); uniqueness of lifts then forces it to equal \(T_k\) everywhere. The deck group is therefore isomorphic to \(\mathbb Z\).""")],
standard=[
q("Exponential lift",r"Lift \(\gamma(t)=e^{4\pi it}\) under \(e^w\) starting at zero.",r"Take a continuous logarithm along the path.",r"The lift is \(\widetilde\gamma(t)=4\pi it\), ending at \(4\pi i\)."),
q("Power-map fiber",r"List the fiber of \(w\mapsto w^4\) over \(1\).",r"Find the fourth roots of unity.",r"The fiber is \(\{1,i,-1,-i\}\)."),
q("Power monodromy",r"Under \(w\mapsto w^4\), where does the lift of one positive base loop starting at \(1\) end?",r"Advance one fourth-root step.",r"It ends at \(i\)."),
q("Deck translation",r"Which translation sends \(0\) to the point \(-4\pi i\) in the exponential fiber?",r"Deck translations are by integer multiples of \(2\pi i\).",r"It is \(w\mapsto w-4\pi i\)."),
q("Loop closure",r"How many positive turns around zero are needed before a lift under \(w\mapsto w^5\) starting at \(1\) closes?",r"The monodromy is a five cycle.",r"Five turns are required.")],
proof=[
q("Unique path lifting",r"Outline a proof of unique path lifting for coverings.",r"Cover the compact path image by evenly covered neighborhoods.",r"Subdivide the interval so each segment lies in one evenly covered neighborhood. The starting sheet determines a unique local lift, and the pieces concatenate uniquely."),
q("Homotopy invariance",r"Why do homotopic based loops induce the same monodromy permutation?",r"Lift the homotopy and inspect endpoints.",r"Lifted endpoints depend continuously on the homotopy parameter but lie in a discrete fiber, so they remain constant."),
q("Exponential covering",r"Prove that \(e^w:\mathbb C\to\mathbb C^*\) is a covering map.",r"Use local logarithm branches.",r"A small disk avoiding zero admits a logarithm. Its inverse image is a disjoint union of translates of that logarithm branch by \(2\pi i k\), each mapped biholomorphically onto the disk."),
q("Deck group",r"Prove that every deck transformation of the exponential covering is a translation by \(2\pi i k\).",r"Determine the image of one point, then use uniqueness of lifts.",r"The image of zero lies in its fiber, so it is \(2\pi i k\). The deck map and that translation are lifts of the same exponential map with the same starting value, hence coincide.")],
test=[
q("Branch point covering",r"Is \(w\mapsto w^2\) a covering map from all of \(\mathbb C\) to all of \(\mathbb C\)?",r"Inspect a neighborhood of zero.",r"No. The map is not locally a disjoint union of homeomorphic sheets over zero because the two sheets merge there."),
q("Endpoint depends only on loop",r"Does the endpoint of a lifted loop depend only on the base loop and the chosen starting point?",r"Use uniqueness of lifts.",r"Yes for the specified parametrized loop. For homotopy classes, homotopy lifting shows it depends only on the based homotopy class."),
q("Trivial monodromy",r"Must every nontrivial covering have nontrivial monodromy for every loop?",r"Consider a contractible loop.",r"No. Contractible loops act trivially even in a nontrivial covering.")],
application=[
q("Analytic continuation",r"How does path lifting model analytic continuation of inverse branches?",r"A local inverse chooses one point in a fiber.",r"As the base point moves, the chosen inverse value follows the unique lifted path. Loop endpoints encode the permutation of branches."),
q("Root tracking",r"Why is monodromy useful when numerically continuing roots of a polynomial depending on a parameter?",r"Follow roots along parameter loops.",r"Continuation transports each root continuously and the endpoint permutation reveals how branches exchange around discriminant values.")],
challenge=[
q("Monodromy representation",r"Explain why monodromy gives a group homomorphism from the fundamental group into a permutation group.",r"Compare lifting a concatenation with successive lifts.",r"Lifting concatenated loops applies the first endpoint permutation and then the second, so loop multiplication corresponds to composition of permutations."),
q("Regular covering",r"What special feature of the exponential covering makes its deck group act transitively on each fiber?",r"Any two fiber points differ by a period.",r"Fiber points differ by \(2\pi i k\), and the corresponding deck translation sends one to the other. This is the hallmark of a regular covering.")])

DATA["IV/24"] = pack(
examples=[
ex(1,"Local ramification index",r"""Consider \(p(w)=w^3\) near \(w=0\). In the local coordinate \(w\), the map already has the normal form
\[
z=w^3.
\]
The ramification index is \(e=3\). A small nonzero value of \(z\) has three nearby preimages, while the fiber over zero contains one point with multiplicity three. The derivative \(3w^2\) vanishes at the ramification point."""),
ex(4,"Branching of a quadratic polynomial",r"""View \(p(w)=w^2-1\) as a map of Riemann spheres. The finite critical point is \(w=0\), with branch value \(-1\). Infinity is also ramified because in coordinates \(u=1/w\) and \(v=1/z\),
\[
v=\frac{u^2}{1-u^2}=u^2+O(u^4).
\]
Thus the degree-two map has two ramification points, each of index two."""),
ex(7,"Genus from Riemann--Hurwitz",r"""For a degree-two map \(X\to\widehat{\mathbb C}\) with \(r\) simple branch points, Riemann--Hurwitz gives
\[
2-2g(X)=2\cdot2-r.
\]
Hence
\[
g(X)=\frac{r-2}{2}.
\]
A double cover branched at four points has genus one, while branching at six points gives genus two.""")],
standard=[
q("Ramification index",r"Find the ramification index of \(w\mapsto w^5\) at zero.",r"Read the exponent in the local power model.",r"The index is \(5\)."),
q("Derivative criterion",r"Is \(w=0\) ramified for \(p(w)=w^3+w\)?",r"Compute \(p'(0)\).",r"No. Since \(p'(0)=1\), the local index is one."),
q("Critical points",r"Find the finite critical points of \(p(w)=w^3-3w\).",r"Solve \(p'(w)=0\).",r"The critical points are \(w=\pm1\)."),
q("Branch values",r"Find the corresponding finite branch values for \(w^3-3w\).",r"Evaluate the polynomial at the critical points.",r"The branch values are \(-2\) at \(w=1\) and \(2\) at \(w=-1\)."),
q("Double-cover genus",r"Find the genus of a double cover of the sphere with eight simple branch points.",r"Use \(2-2g=4-r\).",r"With \(r=8\), one gets \(g=3\).")],
proof=[
q("Local power model",r"Outline why a nonconstant holomorphic map has local form \(z\mapsto z^e\).",r"Factor the first nonzero Taylor term and absorb the unit.",r"Write the map as \(z^e h(z)\) with \(h(0)\ne0\). A local holomorphic \(e\)-th root of \(h\) produces a new coordinate in which the map is exactly a power."),
q("Derivative criterion",r"Prove that ramification is equivalent to vanishing derivative in local coordinates.",r"Differentiate the power normal form.",r"The derivative of \(z^e\) at zero is nonzero exactly for \(e=1\)."),
q("Generic degree",r"Explain why the number of preimages counted with multiplicity is locally constant away from branch values.",r"Use the argument principle on the equation \(p(x)-y=0\).",r"As \(y\) varies without crossing a critical value, the boundary has no zeros and the argument-principle count cannot jump."),
q("Even number of simple branch points",r"Use Riemann--Hurwitz to show that a double cover of the sphere has an even number of simple branch points.",r"Solve the formula for the branch count.",r"The formula gives \(r=2g+2\), which is even.")],
test=[
q("Critical value confusion",r"Is every point over a branch value necessarily ramified?",r"A branch value can have several preimages.",r"No. At least one preimage is ramified, but other points in the same fiber can be unramified."),
q("Derivative zero means singular surface",r"Does a vanishing derivative of the projection imply the source Riemann surface is singular?",r"Distinguish the map from the surface.",r"No. It means the map is ramified. The source can be a perfectly smooth Riemann surface."),
q("Degree from distinct points only",r"Can degree be computed by counting only distinct points in a branch fiber?",r"Remember multiplicities.",r"No. At branch fibers several sheets merge, so multiplicities must be counted to recover the degree.")],
application=[
q("Hyperelliptic curve",r"For \(y^2=\prod_{j=1}^{2g+2}(x-a_j)\) with distinct roots, explain the natural map to the sphere.",r"Project to the \(x\)-coordinate.",r"The projection is a degree-two branched cover, with simple branching over the roots and genus \(g\) by Riemann--Hurwitz."),
q("Polynomial dynamics",r"Why are critical values central when studying a polynomial as a branched cover?",r"They are exactly where local inverse branches fail to remain separate.",r"Away from critical values the map is a genuine covering, while crossing or looping around critical values changes the organization and monodromy of inverse branches.")],
challenge=[
q("Infinity ramification",r"Determine the ramification index of a degree \(d\) polynomial at infinity as a map of spheres.",r"Use coordinates \(u=1/w\) and \(v=1/p(w)\).",r"The leading term gives \(v\sim c^{-1}u^d\), so infinity has ramification index \(d\)."),
q("Cubic sphere map",r"Check Riemann--Hurwitz for a generic cubic polynomial map of the sphere.",r"There are two finite simple critical points and ramification at infinity.",r"The two finite points contribute one each and infinity contributes two, for total ramification four. Then \(2=3\cdot2-4\), as required for a sphere source.")])

DATA["IV/25"] = pack(
examples=[
ex(1,"Gluing two charts into the sphere",r"""Take two copies \(U_0,U_\infty\cong\mathbb C\) with coordinates \(z\) and \(w\). Identify nonzero points by
\[
w=\frac1z.
\]
The transition map is biholomorphic on \(\mathbb C^*\) and is its own inverse. The quotient is the Riemann sphere: \(U_0\) covers all finite points, while \(w=0\) in the second chart represents infinity."""),
ex(4,"A torus from a parallelogram",r"""Let \(P\) be a parallelogram generated by noncollinear periods \(\omega_1,\omega_2\). Identify opposite sides by translations \(z\mapsto z+\omega_1\) and \(z\mapsto z+\omega_2\). The transition maps are holomorphic translations and the corner identifications are compatible. The quotient is topologically a torus and inherits a complex structure from the planar coordinate."""),
ex(7,"Two slit planes for a square root",r"""Take two copies of the plane slit along the nonnegative real axis. Glue the upper bank of the first copy to the lower bank of the second and vice versa. Moving around the origin switches sheets, while two turns return to the starting sheet. The resulting surface carries a single-valued coordinate \(w\) with projection \(z=w^2\).""")],
standard=[
q("Sphere transition",r"What is the transition map between the finite and infinite charts of the sphere?",r"Use the reciprocal coordinate.",r"It is \(w=1/z\) on \(\mathbb C^*\)."),
q("Inverse transition",r"What is the inverse of \(w=1/z\)?",r"The reciprocal map is an involution.",r"It is \(z=1/w\)."),
q("Torus edge map",r"What holomorphic map identifies opposite vertical edges of a lattice parallelogram?",r"Use translation by one period.",r"It is a translation \(z\mapsto z+\omega_1\) or its inverse, depending on the chosen edge orientation."),
q("Cocycle check",r"If \(g_{12}(z)=z+1\) and \(g_{23}(z)=z+i\), what must \(g_{13}\) be on a triple overlap?",r"Compose the first two transitions.",r"The cocycle condition gives \(g_{13}(z)=z+1+i\)."),
q("Square-root sheet switch",r"How many crossings of the slit are needed to return to the original sheet in the two-sheeted square-root gluing?",r"Each crossing switches sheets.",r"Two crossings return to the original sheet.")],
proof=[
q("Gluing theorem",r"Explain why compatible biholomorphic transition maps define a complex structure on a Hausdorff quotient.",r"Use the images of the original pieces as charts.",r"Each piece descends locally homeomorphically to the quotient, and on overlaps the chart transitions are exactly the prescribed biholomorphisms. Thus the atlas is holomorphically compatible."),
q("Sphere compactness",r"Why is the two-chart sphere gluing compact?",r"Relate it to the one-point compactification of the plane.",r"The second chart provides a neighborhood of the added infinity point, and the resulting quotient is homeomorphic to the compact Riemann sphere."),
q("Cocycle necessity",r"Why is the cocycle condition necessary on triple overlaps?",r"A point can be transferred between charts by two different routes.",r"Without \(g_{ij}\circ g_{jk}=g_{ik}\), the two routes assign different coordinates to the same equivalence class, so the quotient atlas is inconsistent."),
q("Translation transitions",r"Prove that a lattice quotient inherits a Riemann-surface structure.",r"Use disks smaller than the shortest nonzero lattice displacement.",r"Such a disk has disjoint lattice translates. Projection is one to one on it, and any overlap transition between lifted disks is a translation, hence holomorphic.")],
test=[
q("Noninvertible transition",r"Can \(w=z^2\) be used as a chart transition across a neighborhood containing zero?",r"A transition must be biholomorphic.",r"No. Near zero the map is not locally one to one and its derivative vanishes."),
q("Non-Hausdorff quotient",r"Is holomorphic compatibility alone enough if the quotient topology is non-Hausdorff?",r"Recall the manifold separation axiom.",r"No. A Riemann surface must be Hausdorff, so pathological gluing can fail before complex analysis is considered."),
q("Arbitrary boundary identification",r"May opposite polygon edges be glued by any continuous map and still produce a Riemann surface?",r"The transition must respect complex structure.",r"No. The local identifications used as chart transitions must be holomorphic or antiholomorphic only if one is deliberately changing orientation; for a Riemann surface atlas they must be biholomorphic.")],
application=[
q("Polygon models",r"Why are polygon gluings useful for constructing compact surfaces?",r"They encode global topology through finitely many edge identifications.",r"A single polygon with paired edges can represent the whole surface, while affine or translational edge maps often make the induced complex charts explicit."),
q("Algebraic curve normalization",r"How can gluing local branches help construct a smooth surface from an algebraic relation?",r"Use separate local parameters near branch behavior.",r"Smooth local branches are treated as charts and glued where their coordinate descriptions agree, separating sheets that appear multivalued in the plane projection.")],
challenge=[
q("Sphere from disks",r"Construct the sphere by gluing two unit disks along annular collars rather than two full planes.",r"Use reciprocal coordinates on the overlap annuli.",r"Choose annuli where \(w=1/z\) maps one collar biholomorphically to the other. The resulting compact quotient has the same two-chart complex structure as the sphere."),
q("Corner consistency on a torus",r"Why do the four vertices of a fundamental parallelogram become one point without creating a singularity?",r"Use translations around the corner.",r"Neighborhood sectors from the four corners glue by translations into one ordinary disk neighborhood. The total angle and holomorphic coordinate match smoothly, so no cone singularity appears.")])

DATA["IV/26"] = pack(
examples=[
ex(1,"Compactifying the complex plane",r"""Add one point \(\infty\) to \(\mathbb C\). Near infinity use the coordinate
\[
w=\frac1z.
\]
A neighborhood of \(\infty\) corresponds to \(|z|>R\) together with infinity, which maps to \(|w|<1/R\). The reciprocal transition is holomorphic away from zero, giving the one-point compactification its standard Riemann-surface structure."""),
ex(4,"Genus from Euler characteristic",r"""For a compact orientable surface,
\[
\chi=2-2g.
\]
The sphere has \(\chi=2\), hence \(g=0\). A torus has a cell decomposition with one vertex, two edges and one face, so \(\chi=1-2+1=0\), hence \(g=1\). This topological invariant matches the analytic distinction between the sphere and complex tori."""),
ex(7,"Riemann--Hurwitz for a torus double cover",r"""Let \(X\to\widehat{\mathbb C}\) be a double cover branched simply at four points. Then
\[
2-2g(X)=2\cdot2-4=0,
\]
so \(g(X)=1\). Thus any such compact double cover has torus topology. The calculation is the bridge from branch data to global genus.""")],
standard=[
q("Sphere genus",r"Find the genus of a compact surface with Euler characteristic \(2\).",r"Use \(\chi=2-2g\).",r"The genus is zero."),
q("Two-handle Euler characteristic",r"Find the Euler characteristic of a genus-two surface.",r"Use \(\chi=2-2g\).",r"It is \(-2\)."),
q("Torus genus",r"A compact orientable surface has Euler characteristic zero. What is its genus?",r"Solve the genus formula.",r"Its genus is one."),
q("Double-cover branch count",r"How many simple branch points does a degree-two sphere cover of genus two have?",r"Use Riemann--Hurwitz.",r"The equation \(2-4=4-r\) gives \(r=6\)."),
q("Compact holomorphic function",r"What can be said about a holomorphic map from a compact connected Riemann surface to \(\mathbb C\)?",r"Apply the maximum modulus principle.",r"It must be constant.")],
proof=[
q("Compact maximum principle",r"Prove that every holomorphic function on a compact connected Riemann surface is constant.",r"The modulus attains a maximum.",r"Compactness gives a maximum point. In a local chart the maximum modulus principle forces local constancy, and connectedness propagates it globally."),
q("Sphere compactification",r"Show that the reciprocal coordinate produces a compatible chart at infinity.",r"Check the overlap transition.",r"On the overlap with the finite chart, \(w=1/z\) is biholomorphic. Therefore adjoining the point \(w=0\) defines a valid complex chart around infinity."),
q("Torus Euler characteristic",r"Prove from a square cell decomposition that a torus has Euler characteristic zero.",r"Count vertices, edges and faces after identifications.",r"All four vertices identify to one, opposite edge pairs give two edges, and there is one face, so \(\chi=1-2+1=0\)."),
q("Riemann--Hurwitz genus",r"Derive \(g=(r-2)/2\) for a double cover of the sphere with \(r\) simple branch points.",r"Insert degree two and total ramification \(r\).",r"The formula gives \(2-2g=4-r\), hence \(g=(r-2)/2\).")],
test=[
q("Remove compactness",r"Does the theorem that every holomorphic function is constant remain true on a noncompact Riemann surface?",r"Use the complex plane.",r"No. The identity function on \(\mathbb C\) is a nonconstant holomorphic example."),
q("Every puncture fills",r"Can every puncture of a Riemann surface be filled holomorphically?",r"Consider essential singular behavior.",r"No. Filling requires the complex structure and relevant functions or maps to extend appropriately; essential or topological behavior can obstruct a chosen extension."),
q("Genus from local charts",r"Can genus be read from one local coordinate chart?",r"Genus is global topology.",r"No. Every surface is locally disk-like; genus measures global handle structure and requires global information.")],
application=[
q("Projective completion",r"Why does adding points at infinity help when studying affine algebraic curves?",r"Compactness gives global constraints.",r"The projective completion packages behavior at infinity into finitely many surface points and makes tools such as divisors, meromorphic functions and Riemann--Hurwitz global."),
q("Meromorphic maps",r"Why are meromorphic functions on a compact Riemann surface naturally viewed as holomorphic maps to the sphere?",r"Treat poles as values equal to infinity.",r"Near a pole, the reciprocal is holomorphic and vanishes, so adjoining the sphere point at infinity turns the meromorphic function into a holomorphic map.")],
challenge=[
q("Degree and ramification",r"A degree-three map from a genus-two surface to the sphere has total ramification \(R\). Find \(R\).",r"Apply Riemann--Hurwitz.",r"\(2-2\cdot2=3\cdot2-R\), so \(-2=6-R\) and \(R=8\)."),
q("Why genus is invariant",r"Explain why biholomorphic compact Riemann surfaces must have the same genus.",r"A biholomorphism is in particular a homeomorphism.",r"Genus is a topological invariant of compact orientable surfaces, and a biholomorphism preserves the underlying topology.")])

DATA["IV/27"] = pack(
examples=[
ex(1,"Reducing a point to a fundamental parallelogram",r"""For the square lattice \(\Lambda=\mathbb Z+i\mathbb Z\), take \(z=3.4-2.7i\). Subtract the lattice element \(3-3i\):
\[
z-(3-3i)=0.4+0.3i.
\]
Thus \(z\) and \(0.4+0.3i\) represent the same torus point. Reduction modulo the two periods is the concrete quotient operation behind \(\mathbb C/\Lambda\)."""),
ex(4,"Changing lattice basis",r"""Let \(\Lambda=\mathbb Z\omega_1+\mathbb Z\omega_2\) and define
\[
\omega_1'=\omega_1+\omega_2,\qquad \omega_2'=\omega_2.
\]
The change matrix has determinant one, so the new pair generates the same lattice. Conversely,
\[
\omega_1=\omega_1'-\omega_2',\qquad \omega_2=\omega_2'.
\]
The torus depends on the lattice subgroup, not on a particular basis."""),
ex(7,"Normalizing a lattice",r"""Given noncollinear periods \(\omega_1,\omega_2\), scale by \(1/\omega_1\). The lattice becomes
\[
\mathbb Z+\mathbb Z\tau,\qquad \tau=\frac{\omega_2}{\omega_1}.
\]
After reversing a basis vector if necessary, choose \(\Im\tau>0\). This isolates the complex shape parameter while removing the irrelevant overall scale.""")],
standard=[
q("Square lattice reduction",r"Reduce \(2.3+4.8i\) modulo \(\mathbb Z+i\mathbb Z\) to the unit square.",r"Subtract integer real and imaginary parts.",r"One representative is \(0.3+0.8i\)."),
q("Basis determinant",r"Does the pair \(\omega_1'=2\omega_1+\omega_2\), \(\omega_2'=\omega_1+\omega_2\) generate the same lattice?",r"Compute the determinant of the integer matrix.",r"Yes. The determinant is \(2\cdot1-1\cdot1=1\)."),
q("Normalized modulus",r"Normalize the lattice generated by \(2\) and \(1+3i\).",r"Divide both periods by \(2\).",r"It becomes \(\mathbb Z+\mathbb Z((1+3i)/2)\)."),
q("Torus covering",r"What is the deck group of \(\mathbb C\to\mathbb C/\Lambda\)?",r"Deck maps are period translations.",r"It is the translation group \(z\mapsto z+\lambda\) for \(\lambda\in\Lambda\)."),
q("Euler characteristic",r"What is the genus of \(\mathbb C/\Lambda\)?",r"A fundamental parallelogram has torus edge identifications.",r"It has genus one.")],
proof=[
q("Quotient complex structure",r"Prove that \(\mathbb C/\Lambda\) has a Riemann-surface structure.",r"Use sufficiently small disks with disjoint lattice translates.",r"Projection is injective on each small disk and transitions between different lifts are translations, hence holomorphic."),
q("Compactness",r"Prove that the complex torus is compact.",r"Project a closed fundamental parallelogram.",r"The closed parallelogram is compact and its projection is continuous and surjective, so the quotient is compact."),
q("Basis invariance",r"Prove that an integral basis change with determinant \(\pm1\) leaves the lattice unchanged.",r"Use the integer inverse matrix.",r"New generators are integer combinations of old ones, and the inverse matrix with integer entries expresses the old generators as combinations of the new ones."),
q("Descending differential",r"Explain why \(dz\) descends to the torus.",r"Check invariance under deck translations.",r"Translations have differential one, so \(d(z+\lambda)=dz\). Thus the form is invariant and defines a holomorphic one-form downstairs.")],
test=[
q("Collinear generators",r"Do \(1\) and \(2\) generate a complex lattice of rank two?",r"Check real linear independence.",r"No. Their ratio is real, so the subgroup is one-dimensional rather than a discrete rank-two lattice spanning the plane."),
q("Determinant two",r"Does the basis change matrix \(\begin{pmatrix}2&0\\0&1\end{pmatrix}\) preserve the lattice?",r"Its determinant is not \(\pm1\).",r"Not in general. It generates a sublattice of index two."),
q("Noncompact quotient",r"Would quotienting by only one nonzero period give a compact Riemann surface?",r"The remaining transverse direction is unbounded.",r"No. The quotient is a cylinder and remains noncompact.")],
application=[
q("Periodic functions",r"Why does a doubly periodic meromorphic function descend to \(\mathbb C/\Lambda\)?",r"It is constant on lattice equivalence classes.",r"Periodicity makes the function well defined on quotient points, and local quotient charts preserve meromorphicity."),
q("Genus-one moduli",r"What information does the normalized parameter \(\tau\) retain?",r"Overall scaling was removed.",r"It records the complex shape of the lattice, modulo changes of lattice basis by modular transformations.")],
challenge=[
q("Modular basis move",r"Show that swapping a normalized basis sends \(\tau\) to \(-1/\tau\) after rescaling.",r"Use the new basis \((\tau,-1)\) and normalize the first generator.",r"Dividing by \(\tau\) gives generators \(1\) and \(-1/\tau\), so the normalized parameter transforms accordingly."),
q("No holomorphic coordinate globally",r"Why can the torus not admit one global chart into an open subset of \(\mathbb C\)?",r"A chart is a homeomorphism onto an open plane set.",r"The torus is compact, while a nonempty open subset of \(\mathbb C\) is not compact. Hence no single global planar chart exists.")])

DATA["IV/28"] = pack(
examples=[
ex(1,"Residues in one period cell",r"""Let \(f\) be elliptic for \(\Lambda\), with no poles on the boundary of a fundamental parallelogram \(P\). Opposite edge integrals cancel by periodicity, so
\[
\int_{\partial P}f(z)\,dz=0.
\]
The residue theorem gives
\[
\sum_{a\in P}\operatorname{Res}(f,a)=0.
\]
Therefore an elliptic function cannot have exactly one simple pole modulo the lattice with nonzero residue."""),
ex(4,"Zero and pole count from the logarithmic derivative",r"""For a nonzero elliptic function \(f\), the logarithmic derivative \(f'/f\) is also elliptic. Opposite edges cancel, hence
\[
\frac1{2\pi i}\int_{\partial P}\frac{f'}{f}\,dz=0.
\]
By the argument principle, the left side equals the number of zeros minus the number of poles in \(P\), counted with multiplicity. Thus every period cell contains equally many zeros and poles."""),
ex(7,"Why an elliptic function must have a pole",r"""Suppose an elliptic function \(f\) had no poles. It would descend to a holomorphic function on the compact torus \(\mathbb C/\Lambda\). By the compact maximum principle it would be constant. Hence every nonconstant elliptic function has at least one pole in every fundamental cell.""")],
standard=[
q("Residue balance",r"An elliptic function has two simple poles in a cell with residues \(3\) and \(r\). Find \(r\).",r"The residue sum is zero.",r"\(r=-3\)."),
q("Zero count",r"An elliptic function has poles of total multiplicity five in a fundamental cell. How many zeros does it have there, counted with multiplicity?",r"Use zero-pole balance.",r"It has five zeros counted with multiplicity."),
q("Single pole",r"Can an elliptic function have one simple pole modulo the lattice?",r"Use residue balance.",r"No, because its nonzero residue could not be canceled."),
q("Derivative periodicity",r"If \(f\) is elliptic, is \(f'\) elliptic?",r"Differentiate the period identity.",r"Yes. Differentiating \(f(z+\omega)=f(z)\) gives \(f'(z+\omega)=f'(z)\)."),
q("Log derivative",r"Why is \(f'/f\) elliptic where defined?",r"Both numerator and denominator have the same periods.",r"The quotient inherits every period of \(f\), with meromorphic singularities at zeros and poles.")],
proof=[
q("Residue theorem",r"Prove residue balance for an elliptic function.",r"Integrate around a fundamental parallelogram.",r"Each edge integral cancels with the opposite translated edge. The boundary integral is zero, so the residue theorem forces the interior residue sum to vanish."),
q("Zero-pole theorem",r"Prove that zeros and poles balance in a period cell.",r"Apply the argument principle to \(f'/f\).",r"The boundary integral cancels by periodicity and equals \(2\pi i\) times zeros minus poles, so the difference is zero."),
q("Nonconstant implies pole",r"Prove that a nonconstant elliptic function must have a pole.",r"Descend to the compact torus.",r"Without poles it would be holomorphic on the compact torus and therefore constant, contradiction."),
q("Position constraint idea",r"Explain why integrating \(z f'(z)/f(z)\) around a period cell leads to a lattice-valued constraint on sums of zeros and poles.",r"Opposite-edge cancellation now leaves period multiples.",r"Residues give the weighted sum of zero locations minus pole locations. Boundary terms differ by lattice periods, so the resulting difference is determined modulo the lattice.")],
test=[
q("One double pole",r"Can an elliptic function have exactly one double pole modulo the lattice?",r"A double pole can have zero residue.",r"Yes. Residue balance does not forbid it; the Weierstrass \(\wp\)-function is the standard example."),
q("Entire doubly periodic",r"Can a nonconstant entire doubly periodic function exist?",r"Descend to the compact torus.",r"No. It would define a holomorphic function on a compact connected surface and hence be constant."),
q("Boundary pole",r"May one apply the standard period-cell residue count with a pole exactly on the chosen boundary?",r"The contour passes through a singularity.",r"Not directly. Shift the parallelogram slightly or use a boundary convention that avoids poles.")],
application=[
q("Constructing principal parts",r"What compatibility condition must proposed simple-pole residues satisfy before an elliptic function can realize them?",r"Use the residue sum theorem.",r"Their sum over one period cell must be zero."),
q("Compactification viewpoint",r"Why are elliptic-function balance laws stronger than analogous local meromorphic facts in the plane?",r"The quotient torus is compact.",r"Compactness removes boundary escape and forces global residue and divisor-degree constraints within one fundamental cell.")],
challenge=[
q("Order of an elliptic function",r"Why is the total pole multiplicity in a cell often called the order of a nonconstant elliptic function?",r"It equals the total zero multiplicity.",r"The zero-pole theorem shows the same integer counts generic inverse images of values, so it is the degree of the corresponding meromorphic map from the torus to the sphere."),
q("No order one",r"Show that a nonconstant elliptic function cannot have order one.",r"Order one would mean one simple pole.",r"A single simple pole has a nonzero residue, contradicting residue balance. Thus the smallest possible order is two.")])

DATA["IV/29"] = pack(
examples=[
ex(1,"Why the Weierstrass sum converges",r"""For bounded \(z\) and large lattice points \(\omega\),
\[
\frac1{(z-\omega)^2}-\frac1{\omega^2}
=\frac{2z\omega-z^2}{\omega^2(z-\omega)^2}
=O(|\omega|^{-3}).
\]
The lattice sum \(\sum_{\omega\ne0}|\omega|^{-3}\) converges. Therefore the regularized series for \(\wp(z)\) converges normally on compact sets avoiding \(\Lambda\). The subtraction term is exactly what improves the decay from quadratic to cubic order."""),
ex(4,"A half-period critical point",r"""Let \(a\) be a nonzero half-period, so \(2a\in\Lambda\). Periodicity and oddness of \(\wp'\) give
\[
\wp'(a)=\wp'(a-2a)=\wp'(-a)=-\wp'(a).
\]
Hence \(\wp'(a)=0\). The three nonzero half-period classes therefore map to the three finite branch values of the degree-two map \(\wp:\mathbb C/\Lambda\to\widehat{\mathbb C}\)."""),
ex(7,"Recovering the cubic differential equation",r"""Near zero,
\[
\wp(z)=z^{-2}+O(z^2),\qquad \wp'(z)=-2z^{-3}+O(z).
\]
Choose lattice invariants \(g_2,g_3\) so that the principal part of
\[
F=(\wp')^2-4\wp^3+g_2\wp+g_3
\]
cancels. Then \(F\) is elliptic and has no poles, hence is constant on the compact torus. Matching the constant term gives \(F=0\), so
\[
(\wp')^2=4\wp^3-g_2\wp-g_3.
\]""")],
standard=[
q("Principal part",r"What is the principal part of \(\wp\) at a lattice point?",r"Translate the expansion at zero.",r"It is \(1/(z-\omega)^2\)."),
q("Residue",r"What is the residue of \(\wp\) at a lattice point?",r"A pure double pole has no \((z-\omega)^{-1}\) term.",r"The residue is zero."),
q("Parity",r"State the parity of \(\wp\) and \(\wp'\).",r"Differentiate an even function.",r"\(\wp\) is even and \(\wp'\) is odd."),
q("Half-period derivative",r"What is \(\wp'(a)\) at a nonzero half-period class?",r"Use periodicity and oddness.",r"It is zero."),
q("Second derivative",r"Differentiate the cubic equation to find \(\wp''\) away from zeros of \(\wp'\), then extend by analyticity.",r"Differentiate both sides and cancel \(2\wp'\).",r"\(\wp''=6\wp^2-g_2/2\).")],
proof=[
q("Normal convergence",r"Prove normal convergence of the regularized lattice series away from the lattice.",r"Use the \(O(|\omega|^{-3})\) estimate.",r"On a compact set, the estimate is uniform for large \(\omega\), and the lattice sum of inverse cubes converges, so the Weierstrass M-test applies."),
q("Evenness",r"Prove \(\wp(-z)=\wp(z)\).",r"Pair lattice points \(\omega\) and \(-\omega\).",r"Replacing \(z\) by \(-z\) and reindexing the lattice by \(\omega\mapsto-\omega\) leaves the regularized sum unchanged."),
q("Half-period zeros",r"Prove that \(\wp'\) vanishes at all three nonzero half-period classes.",r"Use \(a\equiv-a\pmod\Lambda\).",r"Periodicity gives \(\wp'(a)=\wp'(-a)\), while oddness gives \(\wp'(-a)=-\wp'(a)\), hence the value is zero."),
q("Differential equation",r"Explain why canceling the principal part in the cubic expression forces a global identity.",r"An elliptic function with no poles is constant.",r"After cancellation the difference descends to a holomorphic function on the compact torus, so it is constant. Matching one Laurent coefficient determines that constant as zero.")],
test=[
q("Unregularized sum",r"Why is \(\sum_{\omega\in\Lambda}(z-\omega)^{-2}\) not used naively as the definition of \(\wp\)?",r"Absolute convergence in two lattice dimensions is borderline.",r"The inverse-square lattice sum is not absolutely convergent in the required manner. Regularization removes the problematic leading tail and yields normal convergence."),
q("Simple pole",r"Could \(\wp\) have a simple pole at zero?",r"Use evenness.",r"No. An even Laurent series has no odd-power term such as \(z^{-1}\); the leading pole is double."),
q("Discriminant zero",r"Does the cubic \(y^2=4x^3-g_2x-g_3\) remain a smooth elliptic curve when its discriminant vanishes?",r"A repeated root creates a singular point.",r"No. Vanishing discriminant makes the cubic singular, so the smooth torus uniformization requires nonzero discriminant.")],
application=[
q("Degree-two map",r"Why does \(\wp\) generically identify exactly the pair \(z\) and \(-z\)?",r"Use evenness and the pole order.",r"Evenness gives the pair, and the function has degree two as a meromorphic map on the torus, so a generic value has exactly those two preimages counted with multiplicity."),
q("Cubic uniformization",r"How does the differential equation turn analytic data into an algebraic curve?",r"Set \(x=\wp(z)\) and \(y=\wp'(z)\).",r"The pair satisfies the cubic equation, producing a holomorphic map from the torus into the corresponding projective cubic.")],
challenge=[
q("Branch points of wp",r"Identify the four branch points of the degree-two map \(\wp\) on the torus.",r"They are the fixed points of \(z\mapsto-z\) modulo the lattice.",r"They are the origin class and the three nonzero half-period classes. The origin maps to infinity and the other three map to the finite values \(e_1,e_2,e_3\)."),
q("Invariant weights",r"Predict how \(g_2\) and \(g_3\) scale when the lattice is multiplied by a nonzero complex number \(c\).",r"Inspect their lattice sums of fourth and sixth inverse powers.",r"They scale as \(g_2(c\Lambda)=c^{-4}g_2(\Lambda)\) and \(g_3(c\Lambda)=c^{-6}g_3(\Lambda)\).")])

DATA["IV/30"] = pack(
examples=[
ex(1,"Using the addition formula",r"""For points \(u,v\) with \(\wp(u)\ne\wp(v)\), set
\[
m=\frac{\wp'(u)-\wp'(v)}{\wp(u)-\wp(v)}.
\]
Then
\[
\wp(u+v)=-\wp(u)-\wp(v)+\frac{m^2}{4}.
\]
Thus the sum coordinate is determined by the two points and the chord slope. The same expression is exactly the \(x\)-coordinate computation in the chord law on \(y^2=4x^3-g_2x-g_3\)."""),
ex(4,"Duplication as a tangent limit",r"""Let \(v\to u\). The chord quotient satisfies
\[
\frac{\wp'(u)-\wp'(v)}{\wp(u)-\wp(v)}\longrightarrow
\frac{\wp''(u)}{\wp'(u)}
\]
when \(\wp'(u)\ne0\). Therefore
\[
\wp(2u)=-2\wp(u)+\frac14\left(\frac{\wp''(u)}{\wp'(u)}\right)^2.
\]
The chord has become the tangent, matching the geometric duplication law on the cubic."""),
ex(7,"Adding a half-period",r"""Let \(a\) be a nonzero half-period, so \(\wp'(a)=0\). In the addition formula with \(v=a\), the slope becomes
\[
\frac{\wp'(u)}{\wp(u)-\wp(a)}.
\]
Hence translation by a two-torsion point is represented by a rational expression in \(\wp(u)\) and \(\wp'(u)\). The simplification reflects the fact that half-periods are points of order two on the torus.""")],
standard=[
q("Chord slope",r"Write the slope quantity appearing in the Weierstrass addition formula.",r"Use the difference of derivative values divided by the difference of function values.",r"It is \((\wp'(u)-\wp'(v))/(\wp(u)-\wp(v))\)."),
q("Inverse point",r"What happens to \((\wp(z),\wp'(z))\) when \(z\) is replaced by \(-z\)?",r"Use parity.",r"The first coordinate is unchanged and the second changes sign."),
q("Two-torsion",r"Why is a half-period a point of order two on the torus?",r"Double it modulo the lattice.",r"Because \(2a\in\Lambda\), so \(2[a]=[0]\)."),
q("Duplication slope",r"What replaces the chord slope in the limit \(v\to u\)?",r"Apply l'Hopital to numerator and denominator.",r"It becomes \(\wp''(u)/\wp'(u)\)."),
q("Subtraction",r"How is a formula for \(\wp(u-v)\) obtained from the addition formula?",r"Replace \(v\) by \(-v\).",r"Use \(\wp(-v)=\wp(v)\) and \(\wp'(-v)=-\wp'(v)\) in the same addition identity.")],
proof=[
q("Pole comparison",r"Explain the standard elliptic-function proof strategy for the addition formula.",r"Treat one side minus the other as a function of one variable.",r"Show the difference is elliptic and that all poles and principal parts cancel. It is then holomorphic on the compact torus and hence constant; evaluate a convenient limit to determine the constant."),
q("Duplication formula",r"Derive the duplication formula from the addition formula.",r"Let \(v\to u\) and use l'Hopital.",r"The chord quotient tends to \(\wp''(u)/\wp'(u)\), yielding the tangent formula for \(\wp(2u)\)."),
q("Chord geometry",r"Why does the squared slope determine the third intersection x-coordinate on the Weierstrass cubic?",r"Substitute the line equation into the cubic and use Vieta.",r"The resulting cubic in \(x\) has the two known intersection abscissas and a third one. Comparing the quadratic coefficient expresses the third abscissa in terms of the slope squared and the first two abscissas."),
q("Compatibility with inverse",r"Prove that torus inversion corresponds to reflection across the x-axis on the cubic.",r"Use parity of \(\wp\) and \(\wp'\).",r"Under \(z\mapsto-z\), \(x=\wp(z)\) stays fixed while \(y=\wp'(z)\) changes sign, exactly the cubic group inverse.")],
test=[
q("Equal x-coordinates",r"Can the chord version of the addition formula be used directly when \(\wp(u)=\wp(v)\)?",r"The displayed denominator vanishes.",r"Not directly. One must use a limiting tangent case or recognize that the points may be inverses or otherwise special."),
q("Half-period derivative",r"Does the duplication formula containing \(\wp''/\wp'\) apply directly at a half-period?",r"The denominator vanishes there.",r"No. A separate limiting analysis is required at two-torsion points."),
q("Only wp values",r"Can generic addition be recovered from \(\wp(u)\) and \(\wp(v)\) alone?",r"\(\wp\) forgets the signs of the points.",r"No. Derivative data distinguish \(z\) from \(-z\) and are needed to choose the correct group sum generically.")],
application=[
q("Fast multiplication",r"How can duplication formulas help compute \(nP\) on an elliptic curve?",r"Use repeated doubling and addition.",r"They provide rational recurrences for the coordinates, enabling the same double-and-add strategy used in algebraic elliptic-curve arithmetic."),
q("Torsion detection",r"Why do special addition formulas simplify at torsion points?",r"Some multiples become the identity and derivative values can vanish.",r"Algebraic relations among repeated sums impose polynomial conditions on \(\wp\)-values, leading to division polynomials and torsion equations.")],
challenge=[
q("Third intersection",r"Explain the sign change needed after finding the third intersection of a chord with the cubic.",r"The group sum is the inverse of that third point.",r"Three collinear points sum to the identity, so \(P+Q\) is obtained by reflecting the third intersection across the x-axis."),
q("Multiplication map degree",r"Predict the degree of the multiplication-by-\(n\) map on a complex torus.",r"Count preimages of the origin modulo the lattice.",r"The kernel consists of \(n^2\) classes \((a\omega_1+b\omega_2)/n\), so the map has degree \(n^2\).")])

DATA["IV/31"] = pack(
examples=[
ex(1,"Checking the cubic equation",r"""Set
\[
x=\wp(z),\qquad y=\wp'(z).
\]
The differential equation gives immediately
\[
y^2=4x^3-g_2x-g_3.
\]
Thus every torus point away from the lattice maps to the affine Weierstrass cubic. Near the lattice origin, the pole expansions send the point to the unique point at infinity in projective closure."""),
ex(4,"The invariant differential",r"""On the cubic \(y^2=4x^3-g_2x-g_3\), consider \(dx/y\). Under the Weierstrass parametrization,
\[
dx=\wp'(z)\,dz=y\,dz.
\]
Therefore
\[
\frac{dx}{y}=dz.
\]
The nowhere-vanishing holomorphic differential on the torus is exactly the pullback of the algebraic invariant differential."""),
ex(7,"A nonsingularity check",r"""For
\[
F(x,y)=y^2-4x^3+g_2x+g_3,
\]
a singular affine point would satisfy \(F=F_x=F_y=0\). Thus \(y=0\) and \(12x^2=g_2\), while \(x\) is also a repeated root of \(4x^3-g_2x-g_3\). This occurs exactly when the discriminant \(g_2^3-27g_3^2\) vanishes. Nonzero discriminant therefore gives a smooth cubic.""")],
standard=[
q("Curve point",r"If \(x=\wp(z)\), what is the corresponding y-coordinate in the Weierstrass parametrization?",r"Use the derivative coordinate.",r"It is \(y=\wp'(z)\)."),
q("Identity point",r"Which point of the projective cubic is the group identity?",r"Look at the image of the lattice origin.",r"The unique point at infinity is the identity."),
q("Inverse",r"What is the inverse of \((x,y)\) in the cubic group law?",r"Match torus inversion.",r"It is \((x,-y)\)."),
q("Differential pullback",r"Compute the pullback of \(dx/y\).",r"Use \(x=\wp(z)\) and \(dx=\wp'(z)dz\).",r"The pullback is \(dz\)."),
q("Discriminant condition",r"What condition on \(g_2,g_3\) ensures the cubic is nonsingular?",r"Use the Weierstrass discriminant.",r"One requires \(g_2^3-27g_3^2\ne0\).")],
proof=[
q("Map lies on cubic",r"Prove that the Weierstrass parametrization lands on the cubic.",r"Use the differential equation for \(\wp\).",r"Substituting \(x=\wp(z)\) and \(y=\wp'(z)\) into the cubic equation gives an identity."),
q("Extension at infinity",r"Explain why the parametrization extends over the lattice origin to the projective point at infinity.",r"Use the Laurent orders \(2\) and \(3\) of \(\wp\) and \(\wp'\).",r"The affine coordinates blow up with controlled orders. In projective coordinates, rescaling by an appropriate power of \(z\) yields a finite limit equal to the unique point at infinity."),
q("Biholomorphism",r"Why does an injective nonconstant holomorphic map from the compact torus to a smooth connected cubic become a biholomorphism?",r"Use compactness and the open mapping theorem.",r"The image is compact and therefore closed, and nonconstant holomorphic maps are open. A nonempty subset that is both open and closed in the connected cubic is all of it. A holomorphic bijection between compact Riemann surfaces has holomorphic inverse."),
q("Group-law compatibility",r"Prove conceptually that torus addition matches the chord-and-tangent law.",r"Use the Weierstrass addition formula.",r"The analytic formula gives the coordinates of the image of \(u+v\) and agrees with the coordinate formula obtained from the cubic chord slope. Identity and inversion also match, so the group laws coincide.")],
test=[
q("Zero discriminant",r"What fails when \(g_2^3-27g_3^2=0\)?",r"The cubic has a repeated root.",r"The projective cubic becomes singular, so it is no longer a smooth genus-one Riemann surface."),
q("wp alone injective",r"Is \(z\mapsto\wp(z)\) injective on the torus?",r"Use evenness.",r"No. Generically \(z\) and \(-z\) have the same \(\wp\)-value."),
q("Affine cubic compact",r"Is the affine equation alone a compact Riemann surface?",r"Inspect behavior at infinity.",r"No. One must add the projective point at infinity to obtain the compact elliptic curve.")],
application=[
q("Analytic algebraic dictionary",r"What does the torus-cubic equivalence translate between?",r"Match periods and elliptic functions with algebraic coordinates.",r"It identifies lattice-periodic analytic functions with rational functions on a cubic, torus addition with the algebraic group law, and \(dz\) with the invariant differential \(dx/y\)."),
q("Moduli invariant",r"Why is a scale-invariant quantity such as \(j\) useful for classifying complex elliptic curves?",r"Scaling changes \(g_2\) and \(g_3\) with different weights.",r"A suitable ratio cancels those weights, so it depends on the complex isomorphism class rather than the chosen scaling of the lattice or cubic equation.")],
challenge=[
q("Separation by wp pair",r"Why does the pair \((\wp,\wp')\) separate torus points even though \(\wp\) alone does not?",r"Equal \(\wp\)-values generically give opposite points.",r"If two points have the same \(\wp\)-value, they are generically negatives. Their \(\wp'\)-values then have opposite signs, so equality of both coordinates forces the same torus class, including the branch cases."),
q("Genus-one synthesis",r"State the four equivalent viewpoints assembled in this chapter.",r"Connect topology, quotient geometry, function theory and algebraic geometry.",r"A pointed genus-one compact Riemann surface can be viewed as a complex torus, as a smooth projective cubic, through its elliptic-function field generated by \(\wp\) and \(\wp'\), and as an analytic group uniformized by the complex plane modulo a lattice.")])
