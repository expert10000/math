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

DATA["IV/01"] = pack(
examples=[
ex(1,"Derivative of a quadratic",r"""Let \(f(z)=z^2\) and fix \(z_0\). Then
\[
\frac{f(z_0+h)-f(z_0)}{h}
=\frac{2z_0h+h^2}{h}=2z_0+h.
\]
The limit is \(2z_0\) independently of the direction in which \(h\to0\). Hence \(f\) is complex differentiable everywhere and \(f'(z_0)=2z_0\). The calculation exhibits the decisive requirement: one complex limit must work for every approach direction."""),
ex(4,"Conjugation fails the direction test",r"""For \(f(z)=\overline z\) at the origin, real increments give
\[
\frac{f(h)-f(0)}{h}=1,
\]
while purely imaginary increments \(h=it\) give
\[
\frac{f(it)-f(0)}{it}=\frac{-it}{it}=-1.
\]
The directional limits disagree, so conjugation is not complex differentiable at \(0\). Translating the same calculation shows that it is nowhere complex differentiable."""),
ex(7,"A function differentiable only at one point",r"""Consider \(f(z)=|z|^2=z\overline z\). At \(0\),
\[
\frac{f(h)-f(0)}{h}=\frac{|h|^2}{h}=\overline h\longrightarrow0,
\]
so \(f'(0)=0\). At a nonzero point \(z_0\), increments along the real and imaginary directions produce different linear terms because of the \(\overline h\) contribution. Thus a function may be complex differentiable at an isolated point without being holomorphic on any neighborhood of that point.""")],
standard=[
q("Polynomial derivative",r"Compute the complex derivative of \(f(z)=3z^4-2z+7\).",r"Use the algebra rules for powers and sums.",r"The power rule gives \(f'(z)=12z^3-2\)."),
q("Reciprocal derivative",r"Differentiate \(f(z)=1/(z-2i)\) on its domain.",r"Apply the reciprocal or quotient rule away from the pole.",r"For \(z\ne2i\), \(f'(z)=-(z-2i)^{-2}\)."),
q("Chain rule",r"Find the derivative of \(f(z)=(z^2+1)^5\).",r"Differentiate the outer fifth power and then the inner quadratic.",r"The chain rule gives \(f'(z)=10z(z^2+1)^4\)."),
q("Directional diagnostic",r"Test complex differentiability of \(f(z)=\operatorname{Re}z\) at \(0\).",r"Compare real and imaginary increments.",r"Along real increments the quotient is \(1\), while along imaginary increments it is \(0\). Therefore the derivative does not exist."),
q("Linearization",r"Write the first order complex linearization of \(e^z\) at \(z_0\).",r"Use the derivative \(e^{z_0}\).",r"The linearization is \(e^{z_0}+e^{z_0}(z-z_0)\), with an error \(o(|z-z_0|)\).")],
proof=[
q("Differentiability implies continuity",r"Prove that complex differentiability at \(z_0\) implies continuity there.",r"Factor \(f(z)-f(z_0)\) by \(z-z_0\).",r"Write \(f(z)-f(z_0)=(z-z_0)Q(z)\), where \(Q(z)\to f'(z_0)\). The factor \(Q\) is bounded near \(z_0\), so the product tends to zero."),
q("Product rule",r"Prove the complex product rule directly from difference quotients.",r"Add and subtract \(f(z)g(z_0)\).",r"Split the increment into \(f(z)(g(z)-g(z_0))+g(z_0)(f(z)-f(z_0))\), divide by \(z-z_0\), and use continuity of \(f\)."),
q("Reciprocal rule",r"If \(f(z_0)\ne0\), prove that \(1/f\) is differentiable at \(z_0\) and find its derivative.",r"Use a difference of reciprocals and continuity of \(f\).",r"The quotient becomes \(-(f(z)-f(z_0))/((z-z_0)f(z)f(z_0))\). Passing to the limit gives \(-(f'(z_0))/f(z_0)^2\)."),
q("Complex linear real derivative",r"Prove that a real linear map \(T:\mathbb C\to\mathbb C\) is complex linear exactly when \(T(i)=iT(1)\).",r"Every complex number is \(x+iy\).",r"If the condition holds, real linearity gives \(T(x+iy)=xT(1)+yT(i)=(x+iy)T(1)\). The converse follows by evaluating a complex linear map at \(i\).")],
test=[
q("Absolute value",r"Is \(f(z)=|z|\) complex differentiable at \(0\)? Justify the answer.",r"Compare positive and negative real increments.",r"For positive real \(h\), the quotient is \(1\); for negative real \(h\), it is \(-1\). Hence no complex derivative exists."),
q("A single derivative is not holomorphicity",r"Does complex differentiability of a function at one point imply holomorphicity near that point?",r"Use \(|z|^2\).",r"No. The function \(|z|^2\) is complex differentiable at \(0\) with derivative zero, but it is not complex differentiable at any nonzero point."),
q("Quotient rule hypothesis",r"What fails if the quotient rule is applied to \(f/g\) at a point where \(g=0\)?",r"First ask whether the quotient is even defined near the point.",r"The quotient need not be defined at the point and its reciprocal factor can be singular. The nonvanishing denominator hypothesis is essential.")],
application=[
q("Error estimate from linearization",r"Suppose \(f'(z_0)=a\). Explain how the derivative predicts \(f(z_0+h)\) for small \(h\).",r"Use the definition of the little o remainder.",r"One has \(f(z_0+h)=f(z_0)+ah+r(h)\) with \(|r(h)|/|h|\to0\). Thus multiplication by \(a\) gives the first order change in both magnitude and direction."),
q("Real linear classifier",r"For \(T(z)=az+b\overline z\), determine when \(T\) is complex linear.",r"Compare \(T(iz)\) with \(iT(z)\).",r"The conjugate term changes sign under multiplication by \(i\). Equality for every \(z\) forces \(b=0\); then \(T(z)=az\) is complex linear.")],
challenge=[
q("Two direction agreement is not enough",r"Explain why agreement of the real and imaginary directional quotients alone does not prove complex differentiability without additional regularity.",r"Directional tests provide necessary conditions, not uniform control over all directions.",r"The derivative requires one limit as \(h\to0\) through arbitrary complex directions. A function can be engineered so the quotients along the coordinate axes agree while quotients along a curved or oblique path do not."),
q("Derivative of inversion as geometry",r"Show that \(f(z)=1/z\) has derivative \(-1/z^2\) and interpret the local map as a rotation-dilation.",r"Compute the difference quotient and then write the nonzero derivative in polar form.",r"The quotient simplifies to \(-1/(z(z+h))\), giving \(-1/z^2\). Any nonzero complex derivative is multiplication by a complex number, hence locally a dilation by its modulus followed by a rotation by its argument.")])

DATA["IV/02"] = pack(
examples=[
ex(1,"Cauchy--Riemann check for a cubic",r"""Write \(z=x+iy\). For \(f(z)=z^3\),
\[
u=x^3-3xy^2,\qquad v=3x^2y-y^3.
\]
Then \(u_x=3x^2-3y^2=v_y\) and \(u_y=-6xy=-v_x\). The partial derivatives are polynomials and therefore continuous, so the sufficiency theorem applies everywhere. Moreover \(f'(z)=u_x+iv_x=3z^2\), agreeing with direct complex differentiation."""),
ex(5,"Recovering a harmonic conjugate",r"""Let \(u(x,y)=x^2-y^2\). A conjugate \(v\) must satisfy
\[
v_y=u_x=2x,\qquad v_x=-u_y=2y.
\]
Integrating the first equation gives \(v=2xy+g(x)\). Differentiating in \(x\) and comparing with the second equation yields \(g'(x)=0\). Hence \(v=2xy+C\), and \(u+iv=z^2+iC\)."""),
ex(8,"Pointwise equations without differentiability",r"""Define \(f(0)=0\) and, for \(z=x+iy\ne0\),
\[
f(z)=\frac{x^3}{x^2+y^2}+i\frac{y^3}{x^2+y^2}.
\]
The coordinate partial derivatives at the origin exist and give \(u_x(0)=v_y(0)=1\) and \(u_y(0)=-v_x(0)=0\), so the Cauchy--Riemann equations hold at that point. Along \(y=x\), however, \(f(x+ix)/(x+ix)=1/2\), whereas along the real axis the quotient is \(1\). Thus the equations at one point, without a suitable differentiability hypothesis, are not sufficient.""")],
standard=[
q("Quadratic CR check",r"Verify the Cauchy--Riemann equations for \(f(z)=z^2\).",r"Expand \((x+iy)^2\).",r"Here \(u=x^2-y^2\) and \(v=2xy\). Thus \(u_x=2x=v_y\) and \(u_y=-2y=-v_x\)."),
q("Derivative from partials",r"For \(f(z)=z^3\), compute \(f'\) from \(u_x+iv_x\).",r"Use the real and imaginary parts of the cubic.",r"The expression is \(3x^2-3y^2+i6xy=3(x+iy)^2=3z^2\)."),
q("Harmonic test",r"Check that \(u(x,y)=e^x\cos y\) is harmonic.",r"Compute the two second partial derivatives.",r"One finds \(u_{xx}=e^x\cos y\) and \(u_{yy}=-e^x\cos y\), so \(\Delta u=0\)."),
q("Find a conjugate",r"Find a harmonic conjugate of \(u=e^x\cos y\).",r"Use \(v_y=u_x\) and then check \(v_x=-u_y\).",r"Integrating \(v_y=e^x\cos y\) gives \(v=e^x\sin y+C\), which satisfies the other equation."),
q("Jacobian determinant",r"If \(f'(z_0)=a+ib\), compute the determinant of the real Jacobian at \(z_0\).",r"The matrix is \(\begin{pmatrix}a&-b\\b&a\end{pmatrix}\).",r"Its determinant is \(a^2+b^2=|f'(z_0)|^2\).")],
proof=[
q("Necessity of CR",r"Derive the Cauchy--Riemann equations from the complex difference quotient.",r"Use real increments and then imaginary increments.",r"The real increment limit is \(u_x+iv_x\). The imaginary increment limit is \(v_y-iu_y\). Equality yields \(u_x=v_y\) and \(u_y=-v_x\)."),
q("Harmonic real part",r"Assuming continuous second partials, prove that the real part of a holomorphic function is harmonic.",r"Differentiate the two CR equations once more.",r"From \(u_x=v_y\) obtain \(u_{xx}=v_{yx}\), and from \(u_y=-v_x\) obtain \(u_{yy}=-v_{xy}\). Equality of mixed partials gives \(u_{xx}+u_{yy}=0\)."),
q("Harmonic imaginary part",r"Prove the analogous harmonicity statement for the imaginary part.",r"Differentiate in the opposite order.",r"The differentiated CR equations give \(v_{xx}=-u_{yx}\) and \(v_{yy}=u_{xy}\), whose sum is zero."),
q("Local angle scaling",r"Show that when \(f'(z_0)\ne0\), the real derivative preserves oriented angles.",r"Write the Jacobian as multiplication by the complex number \(f'(z_0)\).",r"Multiplication by a nonzero complex number is a positive dilation followed by a rotation. It therefore changes every tangent direction by the same angle and preserves oriented angle differences.")],
test=[
q("Conjugation",r"Test the CR equations for \(f(z)=\overline z\).",r"Use \(u=x\) and \(v=-y\).",r"One has \(u_x=1\) and \(v_y=-1\), so the first equation fails everywhere."),
q("Real valued holomorphic function",r"Can a nonconstant real valued function be holomorphic on a connected open set?",r"Set the imaginary part equal to zero in the CR equations.",r"No. The equations force both first partial derivatives of the real part to vanish, so the function is locally constant and hence constant on each connected component."),
q("Pointwise CR",r"Why is satisfying the CR equations at one point not by itself sufficient for complex differentiability?",r"The equations concern only coordinate partial derivatives.",r"Complex differentiability requires a two dimensional linear approximation. Without real differentiability or suitable continuity of partials, coordinate partial information may miss oblique approaches.")],
application=[
q("Potential and stream function",r"If \(u\) is a harmonic potential and \(v\) is its harmonic conjugate, what geometric relation holds between their gradients?",r"Use the CR equations.",r"The equations give \(\nabla v=(-u_y,u_x)\), a quarter turn of \(\nabla u\). Their level curves are therefore orthogonal where the gradients are nonzero."),
q("Local area scaling",r"How does a holomorphic map with derivative \(f'(z_0)\ne0\) scale infinitesimal area?",r"Use the Jacobian determinant.",r"The local area factor is \(|f'(z_0)|^2\), the determinant of the real derivative matrix.")],
challenge=[
q("Polar CR equations",r"Derive the polar Cauchy--Riemann equations for \(f=u+iv\) away from the origin.",r"Express \(u_x,u_y,v_x,v_y\) through radial and angular derivatives.",r"Substituting the polar chain rule into the Cartesian equations yields \(u_r=v_\theta/r\) and \(v_r=-u_\theta/r\)."),
q("Conjugate obstruction",r"Explain why a harmonic function on a punctured plane can fail to have a single valued harmonic conjugate.",r"Consider \(u(z)=\log|z|\).",r"Locally its conjugate is an argument function. Going once around the origin changes the argument by \(2\pi\), so no globally single valued conjugate exists on the punctured plane.")])

DATA["IV/03"] = pack(
examples=[
ex(1,"Radius from coefficient growth",r"""For
\[
\sum_{n=0}^{\infty}\frac{z^n}{3^n},
\]
the ratio of successive absolute terms tends to \(|z|/3\). Thus the series converges for \(|z|<3\) and diverges for \(|z|>3\), so its radius is \(R=3\). Inside the disk it sums to \(1/(1-z/3)\), but the radius is determined before any closed form is used."""),
ex(4,"Taylor expansion about a shifted center",r"""To expand \(1/z\) about \(z_0=2\), write
\[
\frac1z=\frac1{2+(z-2)}=\frac12\frac1{1+(z-2)/2}
=\frac12\sum_{n=0}^{\infty}(-1)^n\left(\frac{z-2}{2}\right)^n.
\]
The nearest singularity to the center is at \(0\), at distance \(2\), so the expansion is valid exactly for \(|z-2|<2\)."""),
ex(7,"Termwise differentiation keeps the radius",r"""Starting from \(e^z=\sum_{n\ge0}z^n/n!\), termwise differentiation gives
\[
\sum_{n\ge1}\frac{nz^{n-1}}{n!}=\sum_{m\ge0}\frac{z^m}{m!}=e^z.
\]
The factorial growth makes the radius infinite both before and after differentiation. This concrete calculation models the general theorem that differentiation preserves the radius of a power series.""")],
standard=[
q("Geometric radius",r"Find the radius of convergence of \(\sum z^n/5^n\).",r"Apply the ratio test.",r"The ratio tends to \(|z|/5\), so \(R=5\)."),
q("Factorial radius",r"Find the radius of convergence of \(\sum z^n/n!\).",r"Use the ratio test.",r"The ratio of successive absolute terms is \(|z|/(n+1)\to0\) for every \(z\), hence \(R=\infty\)."),
q("Differentiate a series",r"Differentiate \(\sum_{n\ge0}z^n\) termwise inside its disk of convergence.",r"The geometric series has radius one.",r"For \(|z|<1\), differentiation gives \(\sum_{n\ge1}nz^{n-1}=1/(1-z)^2\)."),
q("Taylor coefficients",r"Find the first four Taylor coefficients of \(e^z\) at zero.",r"Use \(a_n=f^{(n)}(0)/n!\).",r"They are \(1,1,1/2,1/6\)."),
q("Shifted geometric series",r"Expand \(1/(3-z)\) in powers of \(z-1\) and state the radius.",r"Write \(3-z=2-(z-1)\).",r"One obtains \(\frac12\sum_{n\ge0}((z-1)/2)^n\), valid for \(|z-1|<2\).")],
proof=[
q("Absolute convergence inside the radius",r"Prove that a power series converges absolutely at every point strictly inside its radius.",r"Choose a larger radius where the coefficient terms are bounded.",r"If \(|z-z_0|<r<R\), convergence at radius \(r\) bounds \(|a_n|r^n\). Multiplying by the geometric factor \((|z-z_0|/r)^n\) gives a summable majorant."),
q("Uniform convergence on smaller disks",r"Prove uniform convergence on \(|z-z_0|\le r<R\).",r"Use the same geometric majorant independently of \(z\).",r"Choose \(\rho\) with \(r<\rho<R\). Boundedness of \(|a_n|\rho^n\) yields the uniform majorant \(M(r/\rho)^n\), so the Weierstrass test applies."),
q("Uniqueness of coefficients",r"Show that a power series representation near \(z_0\) has unique coefficients.",r"Differentiate repeatedly and evaluate at the center.",r"Termwise differentiation gives \(f^{(n)}(z_0)=n!a_n\). Hence \(a_n=f^{(n)}(z_0)/n!\), fixing every coefficient."),
q("Derivative radius",r"Explain why the derivative series has the same radius as the original series.",r"Compare \(|na_n|^{1/n}\) with \(|a_n|^{1/n}\).",r"Since \(n^{1/n}\to1\), the limsup controlling the Cauchy--Hadamard radius is unchanged by multiplying coefficients by \(n\).")],
test=[
q("Boundary is separate",r"Does the radius of convergence determine convergence at every boundary point?",r"Compare the geometric series with an alternating harmonic type series.",r"No. The radius separates the open convergence and exterior divergence regions, but individual points on the boundary require separate analysis."),
q("Nearest singularity",r"Why can the Taylor series of \(1/(1-z)\) at zero not have radius larger than one?",r"The represented analytic function has a singularity at \(z=1\).",r"A convergent power series is analytic throughout its disk. A radius larger than one would make the series analytic at \(1\), contradicting the pole there."),
q("Smooth is not analytic",r"Does infinite real differentiability imply a complex power series representation?",r"Complex analyticity is much more rigid than real smoothness.",r"No. Real smoothness alone imposes no Cauchy--Riemann structure. A function of \(x\) and \(y\) can be smooth as a real map but fail complex differentiability everywhere.")],
application=[
q("Summing a weighted geometric series",r"Use power series to evaluate \(\sum_{n\ge1}nr^{n-1}\) for \(|r|<1\).",r"Differentiate the geometric identity.",r"Differentiating \(\sum r^n=1/(1-r)\) gives \(\sum_{n\ge1}nr^{n-1}=1/(1-r)^2\)."),
q("Local analytic model",r"Explain how a Taylor polynomial approximates an analytic function near its center.",r"Separate the first \(N\) terms from the convergent tail.",r"Inside a smaller disk the tail is uniformly controlled, so truncating after degree \(N\) gives a computable local polynomial model whose error tends to zero as \(N\) grows.")],
challenge=[
q("Cauchy--Hadamard",r"State the coefficient formula for the radius of convergence and explain its meaning.",r"Use the root test on \(|a_n(z-z_0)^n|\).",r"The formula is \(1/R=\limsup |a_n|^{1/n}\), with the usual conventions. It measures the exponential growth rate of the coefficients."),
q("Multiple centers",r"The function \(1/(1-z)\) is expanded about \(z_0=-1\). Find the radius without computing coefficients.",r"Measure the distance from the center to the nearest singularity.",r"The only finite singularity is at \(1\), distance \(2\) from \(-1\). Therefore the Taylor radius is \(2\).")])

DATA["IV/04"] = pack(
examples=[
ex(1,"Parametrizing a line segment",r"""Let \(\gamma(t)=t(1+i)\) for \(0\le t\le1\). Then \(\gamma'(t)=1+i\), and
\[
\int_\gamma z\,dz=\int_0^1 t(1+i)(1+i)\,dt
=\frac{(1+i)^2}{2}=i.
\]
The calculation makes the definition operational: substitute the parametrization and multiply by its complex velocity."""),
ex(4,"A circle integral with orientation",r"""For the positively oriented circle \(\gamma(t)=Re^{it}\), \(0\le t\le2\pi\),
\[
\int_\gamma \overline z\,dz
=\int_0^{2\pi}Re^{-it}\,iRe^{it}\,dt
=2\pi iR^2.
\]
Reversing the orientation changes the sign. The example also shows that closed contour integrals need not vanish for nonholomorphic integrands."""),
ex(7,"A primitive makes the path irrelevant",r"""For \(f(z)=3z^2\), a primitive is \(F(z)=z^3\). Therefore every piecewise smooth path from \(z=-1\) to \(z=2+i\) has
\[
\int_\gamma 3z^2\,dz=F(2+i)-F(-1)=(2+i)^3+1.
\]
No parametrization of the chosen path is needed once a primitive is known.""")],
standard=[
q("Straight segment",r"Evaluate \(\int_\gamma z\,dz\) for \(\gamma(t)=t\), \(0\le t\le2\).",r"Substitute the parametrization.",r"The integral is \(\int_0^2 t\,dt=2\)."),
q("Quarter circle",r"Parametrize the counterclockwise quarter circle of radius two from \(2\) to \(2i\).",r"Use an exponential parametrization.",r"A convenient choice is \(\gamma(t)=2e^{it}\) for \(0\le t\le\pi/2\)."),
q("Reverse path",r"If \(\int_\gamma f(z)\,dz=3-i\), find the integral over the reversed path.",r"Reversal changes the sign of the velocity.",r"The value is \(-3+i\)."),
q("Primitive evaluation",r"Evaluate \(\int_\gamma 2z\,dz\) from \(1\) to \(i\) along any path.",r"Use the primitive \(z^2\).",r"The value is \(i^2-1^2=-2\)."),
q("ML bound",r"A contour has length \(5\) and \(|f|\le3\) on it. Bound \(|\int_\gamma f\,dz|\).",r"Use the ML inequality.",r"The integral has modulus at most \(15\).")],
proof=[
q("Reparametrization",r"Prove invariance of a contour integral under an orientation preserving smooth reparametrization.",r"Make a one variable substitution in the parameter integral.",r"If \(t=\phi(s)\) with \(\phi'>0\), then \((\gamma\circ\phi)'=\gamma'(\phi)\phi'\). The ordinary substitution formula gives the same integral."),
q("Concatenation",r"Prove that the integral over a concatenated path is the sum of the two integrals.",r"Split the parameter interval at the joining time.",r"After a standard reparametrization, the parameter integral splits into two ordinary integrals, one for each component path."),
q("ML inequality",r"Prove \(|\int_\gamma f\,dz|\le ML\) when \(|f|\le M\) and the contour length is \(L\).",r"Take absolute values inside the parameter integral.",r"The triangle inequality gives at most \(\int M|\gamma'(t)|dt=M L\)."),
q("Primitive theorem",r"If \(F'=f\), prove \(\int_\gamma f\,dz=F(\gamma(b))-F(\gamma(a))\).",r"Differentiate \(F(\gamma(t))\).",r"The chain rule gives \((F\circ\gamma)'=f(\gamma(t))\gamma'(t)\). The real fundamental theorem of calculus then gives the endpoint difference.")],
test=[
q("Closed does not imply zero",r"Give a continuous integrand whose integral around a closed circle is nonzero.",r"Use conjugation.",r"For \(f(z)=\overline z\) on \(|z|=R\), direct parametrization gives \(2\pi iR^2\ne0\)."),
q("Endpoint data alone",r"Can endpoint data determine \(\int_\gamma f\,dz\) for an arbitrary continuous \(f\)?",r"Path independence requires additional structure such as a primitive.",r"No. Without a primitive or a relevant holomorphic theorem, different paths with the same endpoints may give different integrals."),
q("Orientation forgotten",r"What error results from reversing a contour but keeping the same integral value?",r"Track the sign of the derivative of the reversed parametrization.",r"Reversal multiplies the integral by \(-1\). Forgetting orientation therefore changes the answer by a sign.")],
application=[
q("Arc contribution estimate",r"A semicircular arc has radius \(R\), and \(|f(z)|\le C/R^2\) there. Show its integral tends to zero as \(R\to\infty\).",r"The arc length is \(\pi R\).",r"The ML bound is \(\pi R\cdot C/R^2=\pi C/R\to0\). This estimate will be central in real integral contours."),
q("Path choice",r"Why is a polygonal parametrization often useful for numerical contour integration?",r"Each segment has a constant derivative.",r"The integral becomes a sum of ordinary one dimensional integrals on simple intervals, making both quadrature and error control transparent.")],
challenge=[
q("Unit circle logarithmic integrand",r"Directly parametrize \(\int_{|z|=1} dz/z\).",r"Use \(z=e^{it}\).",r"Then \(dz=ie^{it}dt\), so the integral is \(\int_0^{2\pi}i\,dt=2\pi i\)."),
q("Piecewise primitive",r"Suppose a contour crosses a point where a chosen primitive formula changes branch. Why must the integral be split with care?",r"A primitive must be single valued and differentiable on a neighborhood of each relevant path piece.",r"One may use valid local primitives on separate pieces, but endpoint cancellations only work after branch values are chosen consistently at the joins.")])

DATA["IV/05"] = pack(
examples=[
ex(2,"Triangle cancellation",r"""Suppose \(f\) is holomorphic on a neighborhood of a triangle and its interior. Cauchy's theorem gives
\[
\int_{\partial T}f(z)\,dz=0.
\]
For a polynomial such as \(f(z)=z^3+2z\), this can also be checked from the primitive \(z^4/4+z^2\). The theorem is stronger because it applies even when a primitive has not yet been constructed explicitly."""),
ex(5,"Deforming a contour without crossing singularities",r"""Let \(f(z)=1/(z-3)\), and let \(\gamma_0\) and \(\gamma_1\) be two closed curves lying in the disk \(|z|<2\). Since the pole at \(3\) lies outside the disk and the curves can be deformed into one another there, Cauchy's theorem gives equal integrals. In fact each integral is zero because \(f\) has a primitive on the simply connected disk."""),
ex(8,"The puncture blocks Cauchy's theorem",r"""On \(\mathbb C\setminus\{0\}\), the function \(1/z\) is holomorphic, yet
\[
\int_{|z|=1}\frac{dz}{z}=2\pi i.
\]
There is no contradiction: the unit circle does not bound a region contained in the domain. The missing point is a topological obstruction, and the example explains why domain hypotheses matter as much as pointwise holomorphicity.""")],
standard=[
q("Polynomial loop",r"Evaluate \(\int_\gamma (z^4+z)\,dz\) over any closed contour.",r"The integrand has an entire primitive.",r"The value is zero."),
q("Disk holomorphic",r"Let \(f(z)=1/(z-5)\). Evaluate its integral around \(|z|=2\).",r"The function is holomorphic on the disk bounded by the contour.",r"Cauchy's theorem gives zero."),
q("Rectangle",r"Evaluate the integral of \(e^z\) around the boundary of a rectangle.",r"The exponential is entire.",r"The integral is zero."),
q("Two paths",r"If \(f\) is holomorphic on a simply connected domain, compare integrals along two paths with the same endpoints.",r"Join one path to the reverse of the other.",r"The resulting closed contour has integral zero, so the two path integrals agree."),
q("Primitive consequence",r"What is \(\int_\gamma \cos z\,dz\) from \(0\) to \(\pi\)?",r"Use the primitive \(\sin z\).",r"The value is \(\sin\pi-\sin0=0\).")],
proof=[
q("Path independence from closed loops",r"Prove that vanishing of every closed contour integral implies path independence.",r"Concatenate one path with the reverse of the other.",r"The closed integral is the first path integral minus the second. If it vanishes, the two are equal."),
q("Primitive from path independence",r"On a connected domain with path independent integrals, construct a primitive of \(f\).",r"Fix a base point and integrate to \(z\).",r"Define \(F(z)=\int_{z_*}^{z}f(w)dw\). Path independence makes this well defined. A short final segment and continuity of \(f\) show \(F'(z)=f(z)\)."),
q("Simply connected implication",r"Explain why Cauchy's theorem yields primitives on a simply connected domain.",r"Closed curves can be contracted without leaving the domain.",r"Cauchy's theorem makes every closed contour integral vanish; path independence follows, and the base point integral construction produces a primitive."),
q("Contour deformation",r"Prove that two homologous boundary curves have equal integrals when \(f\) is holomorphic in the region between them.",r"Orient the boundary of the region between the curves.",r"The boundary consists of one curve and the reverse of the other. Cauchy's theorem makes the total integral zero, hence the two original integrals are equal.")],
test=[
q("Punctured disk",r"Why can Cauchy's theorem not be used to conclude \(\int_{|z|=1}dz/z=0\)?",r"Inspect the interior of the contour.",r"The interior contains the missing point \(0\), where the integrand is not holomorphic. The required filled region is not contained in the domain."),
q("Pole on the boundary",r"Can the standard Cauchy theorem be applied when the integrand has a pole on the contour?",r"Holomorphicity is required on a neighborhood of the contour and its interior.",r"No. The contour integral may even be undefined in the ordinary sense, so the hypothesis fails before the theorem is invoked."),
q("Disconnected domain",r"Does simple connectedness make sense without connectedness?",r"Check the definition of a simply connected domain.",r"A domain is connected and open by convention. Statements about simple connectedness presuppose that connected setting.")],
application=[
q("Contour simplification",r"Explain how Cauchy's theorem can simplify a difficult path to an easier one.",r"Deform the path through a region free of singularities.",r"The integral is unchanged under such a deformation. One can therefore replace a complicated contour by a geometrically convenient representative of the same deformation class."),
q("Detecting holes",r"How can a nonzero integral of a holomorphic function around a closed contour reveal domain topology?",r"Compare with the simply connected conclusion.",r"A nonzero closed integral shows that no primitive exists on the whole domain and that the contour cannot be contracted through a region where the integrand remains holomorphic.")],
challenge=[
q("Morera converse",r"State the idea behind the converse principle that vanishing triangle integrals can imply holomorphicity.",r"Use triangle integrals to construct local primitives.",r"If a continuous function has zero integral around every triangle, one constructs a path independent local integral and hence a local primitive. Differentiating that primitive recovers the function, proving holomorphicity."),
q("Annulus comparison",r"Two circles \(|z|=1\) and \(|z|=2\) lie in an annulus where \(f\) is holomorphic. Show their positively oriented integrals are equal.",r"Apply Cauchy's theorem to the region between them with boundary orientation.",r"The boundary integral is the outer circle integral minus the inner circle integral. It vanishes, so the two are equal.")])

DATA["IV/06"] = pack(
examples=[
ex(1,"Cauchy formula in one line",r"""For \(|z|=2\), evaluate
\[
\int_{|z|=2}\frac{e^z}{z-1}\,dz.
\]
The point \(1\) lies inside the circle and \(e^z\) is holomorphic on a neighborhood of the closed disk. Cauchy's integral formula gives the value \(2\pi i e\). No parametrization is required."""),
ex(4,"Derivative extraction",r"""For the positively oriented circle \(|z|=3\),
\[
\int_{|z|=3}\frac{\sin z}{(z-1)^3}\,dz
=\frac{2\pi i}{2!}(\sin z)''\big|_{z=1}
=-\pi i\sin1.
\]
The denominator power determines which derivative is extracted."""),
ex(7,"Cauchy estimate",r"""Suppose \(|f(z)|\le10\) on \(|z-z_0|=2\) and \(f\) is holomorphic on the closed disk. The derivative formula yields
\[
|f^{(3)}(z_0)|\le \frac{3!\,10}{2^3}=\frac{15}{2}.
\]
This turns boundary control into quantitative bounds on every derivative at the center.""")],
standard=[
q("Basic Cauchy value",r"Evaluate \(\int_{|z|=2}(z^2+1)/(z-i)\,dz\).",r"The point \(i\) lies inside the circle.",r"The value is \(2\pi i(i^2+1)=0\)."),
q("Outside point",r"Evaluate \(\int_{|z|=1} e^z/(z-2)\,dz\).",r"The integrand is holomorphic on the closed unit disk.",r"The value is zero by Cauchy's theorem."),
q("First derivative",r"Evaluate \(\int_{|z|=2} e^z/(z-1)^2\,dz\).",r"Use the first derivative form of Cauchy's formula.",r"The result is \(2\pi i e\)."),
q("Second derivative",r"Evaluate \(\int_{|z|=2} z^5/(z-1)^3\,dz\).",r"Extract the second derivative and divide by \(2!\).",r"Since \((z^5)''|_{1}=20\), the integral is \(2\pi i\cdot20/2=20\pi i\)."),
q("Derivative bound",r"If \(|f|\le4\) on \(|z|=3\), bound \(|f''(0)|\).",r"Use the Cauchy estimate \(n!M/R^n\).",r"The bound is \(2!\cdot4/3^2=8/9\).")],
proof=[
q("Higher derivative formula",r"Derive the higher derivative Cauchy formula from the basic formula.",r"Differentiate the kernel with respect to the interior point.",r"Uniform control on a smaller disk justifies differentiation under the contour integral. Repeating gives \(f^{(n)}(a)=n!/(2\pi i)\int f(z)/(z-a)^{n+1}dz\)."),
q("Cauchy estimates",r"Prove the standard Cauchy derivative estimate.",r"Take moduli in the higher derivative formula on a circle of radius \(R\).",r"The kernel contributes \(R^{-(n+1)}\), the contour length contributes \(2\pi R\), and the prefactor gives \(|f^{(n)}(a)|\le n!M/R^n\)."),
q("Liouville theorem",r"Use Cauchy estimates to prove that every bounded entire function is constant.",r"Let the radius tend to infinity in the first derivative estimate.",r"If \(|f|\le M\) globally, then \(|f'(a)|\le M/R\) for every \(R\). Letting \(R\to\infty\) gives \(f'(a)=0\) for every \(a\), so \(f\) is constant."),
q("Mean value identity",r"Derive the mean value formula for a holomorphic function on a circle.",r"Parametrize the Cauchy formula on \(z=a+Re^{it}\).",r"The factors \(Re^{it}\) cancel, leaving \(f(a)=\frac1{2\pi}\int_0^{2\pi}f(a+Re^{it})dt\).")],
test=[
q("Singularity inside",r"Can Cauchy's formula be applied with \(f(z)=1/z\) and center \(a=1\) on a circle enclosing zero?",r"The numerator function in the formula must be holomorphic throughout the interior.",r"Not directly if the chosen circle encloses the pole at zero. One must isolate singularities or use later residue methods."),
q("Point on contour",r"What fails if the evaluation point \(a\) lies on the contour in Cauchy's formula?",r"The kernel has a singularity on the path.",r"The ordinary contour integral is not covered by the formula and may be undefined. The point must lie strictly inside the contour."),
q("Wrong orientation",r"How does clockwise orientation change the Cauchy formula value?",r"Reverse the contour orientation.",r"The integral changes sign, so the usual \(2\pi i f(a)\) becomes \(-2\pi i f(a)\).")],
application=[
q("Coefficient recovery",r"Explain how Cauchy's formula recovers Taylor coefficients from boundary data.",r"Combine the higher derivative formula with \(a_n=f^{(n)}(a)/n!\).",r"One gets \(a_n=(2\pi i)^{-1}\int f(z)/(z-a)^{n+1}dz\). Thus each local coefficient is encoded by the function on any surrounding contour inside the analytic domain."),
q("Maximum growth constraint",r"Why do Cauchy estimates make very slow growth restrictive for entire functions?",r"Choose a large circle and compare growth with the power of its radius in the denominator.",r"If the maximum modulus grows more slowly than \(R^n\), the estimate can force the \(n\)-th derivative to vanish. Repeating such bounds yields polynomial or constant rigidity results.")],
challenge=[
q("Fundamental theorem of algebra",r"Use Liouville's theorem to outline a proof that a nonconstant complex polynomial has a zero.",r"Assume the polynomial has no zeros and examine its reciprocal.",r"If \(p\) has no zeros, \(1/p\) is entire. It tends to zero at infinity and is bounded on a large disk, so it is bounded everywhere. Liouville makes it constant, contradicting nonconstancy of \(p\)."),
q("All derivatives from one contour",r"Explain why knowing a holomorphic function on one circle determines every derivative at its center.",r"Use the family of higher derivative formulas.",r"For every \(n\), the same boundary values enter \(f^{(n)}(a)=n!/(2\pi i)\int f(z)/(z-a)^{n+1}dz\). Thus one contour determines the full Taylor germ at the center.")])

DATA["IV/07"] = pack(
examples=[
ex(2,"Multiplicity by factorization",r"""For \(f(z)=z^3(z-2)^2e^z\), the zero at \(0\) has multiplicity three because \(e^z(z-2)^2\) is holomorphic and nonzero at \(0\). Likewise the zero at \(2\) has multiplicity two. Writing a function as \((z-a)^m g(z)\) with \(g(a)\ne0\) isolates the exact order of vanishing."""),
ex(5,"An accumulation point forces identity",r"""Let \(f\) be holomorphic on the unit disk and suppose \(f(1/n)=0\) for every positive integer \(n\). The zeros accumulate at \(0\), which lies inside the domain. The identity theorem therefore gives \(f\equiv0\) on the entire connected disk. Merely having infinitely many zeros would not suffice if their accumulation occurred only at the boundary."""),
ex(8,"Boundary accumulation is different",r"""The function \(\sin(1/(1-z))\) is holomorphic on the unit disk and has infinitely many zeros accumulating at the boundary point \(z=1\). It is not identically zero. This example isolates the interior accumulation hypothesis in the identity theorem.""")],
standard=[
q("Order of a polynomial zero",r"Find the multiplicity of \(z=1\) for \(f(z)=(z-1)^4(z+2)\).",r"Check whether the remaining factor vanishes at one.",r"The remaining factor equals three, so the multiplicity is four."),
q("Derivative criterion",r"If \(f(a)=f'(a)=0\) and \(f''(a)\ne0\), what is the multiplicity of the zero?",r"Use the Taylor expansion.",r"The first nonzero Taylor term has degree two, so the multiplicity is two."),
q("Zeros of sine",r"List the zeros of \(\sin z\) and their multiplicities.",r"Use the ordinary sine zeros and evaluate the derivative there.",r"The zeros are \(n\pi\), \(n\in\mathbb Z\). Since \(\cos(n\pi)\ne0\), each is simple."),
q("Product multiplicity",r"If \(f\) has order three at \(a\) and \(g\) has order two there, find the order of \(fg\).",r"Factor both functions.",r"The product contains \((z-a)^5\) times a nonvanishing factor, so the order is five."),
q("Quotient order",r"If \(f\) and \(g\) have zero orders five and two at \(a\), what is the zero order of \(f/g\) after cancellation?",r"Subtract the orders.",r"Provided the quotient is interpreted after local cancellation, it has a zero of order three.")],
proof=[
q("Zeros are isolated",r"Prove that a nonzero holomorphic function has isolated zeros.",r"Use the first nonzero Taylor coefficient at a zero.",r"Factor \(f(z)=(z-a)^m g(z)\) with \(g(a)\ne0\). Continuity keeps \(g\) nonzero on a small disk, so \(a\) is the only zero there."),
q("Identity theorem",r"Prove that if zeros of a holomorphic function accumulate at an interior point, the function is identically zero on the connected domain.",r"First show all Taylor coefficients vanish at the accumulation point.",r"If a first nonzero Taylor coefficient existed, the zero would be isolated. Thus the function vanishes on a disk. The set where it locally vanishes is both open and closed in the connected domain, so it is the whole domain."),
q("Agreement on a set",r"Show that two holomorphic functions agreeing on a set with an interior accumulation point agree everywhere on a connected domain.",r"Apply the identity theorem to their difference.",r"The difference is holomorphic and has zeros with the same accumulation point, hence vanishes identically."),
q("Order from derivatives",r"Prove that a zero has multiplicity \(m\) exactly when the first \(m-1\) derivatives vanish and the \(m\)-th does not.",r"Compare with the Taylor expansion.",r"The least index with nonzero Taylor coefficient is exactly the least derivative order with nonzero value, and the coefficient is \(f^{(m)}(a)/m!\).")],
test=[
q("Infinitely many zeros",r"Is an infinite zero set enough to conclude that a holomorphic function is zero?",r"Ask where the zeros accumulate.",r"No. The zeros of \(\sin z\) are infinite but have no finite accumulation point. An interior accumulation point is essential."),
q("Disconnected domain",r"If a holomorphic function vanishes on one component of a disconnected open set, must it vanish on every component?",r"The identity theorem propagates only through connectedness.",r"No. The function can be defined differently on separate components while remaining holomorphic on each."),
q("Boundary accumulation",r"Why do zeros tending to a boundary point not trigger the identity theorem?",r"The accumulation point must belong to the domain.",r"Local Taylor analysis is unavailable at a boundary point not in the domain, so the theorem's key hypothesis fails.")],
application=[
q("Uniqueness of analytic interpolation",r"Two holomorphic models agree at a sequence of sample points converging to an interior point. What follows?",r"Apply the identity theorem to the difference.",r"They agree throughout the connected domain. Thus sufficiently accumulating exact analytic data determine the model uniquely."),
q("Root stability locally",r"Why does factoring a zero help study nearby perturbations?",r"Separate the vanishing factor from the nonzero analytic factor.",r"The factorization identifies multiplicity and isolates a disk where no other zeros occur. Later contour arguments can then track how many perturbed zeros remain in that disk.")],
challenge=[
q("Even order and local square roots",r"Suppose every zero of a holomorphic function in a simply connected neighborhood has even order. Explain locally why a holomorphic square root is plausible.",r"Factor each zero with an even exponent and take a root of the nonvanishing factor.",r"Near a zero, write \(f=(z-a)^{2m}g\) with \(g(a)\ne0\). A local logarithm of \(g\) gives a local square root, so \((z-a)^m\exp(\frac12\log g)\) squares to \(f\)."),
q("Multiplicity under composition",r"If \(f\) has a zero of order \(m\) at \(a\) and \(g\) has a zero of order \(n\) at \(f(a)=0\), determine the order of \(g\circ f\) at \(a\).",r"Factor both functions at the relevant points.",r"Write \(f(z)=(z-a)^m u(z)\) and \(g(w)=w^n v(w)\) with nonvanishing factors. Then \(g(f(z))=(z-a)^{mn}u(z)^n v(f(z))\), so the order is \(mn\).")])

DATA["IV/08"] = pack(
examples=[
ex(1,"One function, two Laurent annuli",r"""For \(f(z)=1/(z(z-1))\), partial fractions give \(-1/z+1/(z-1)\). On \(0<|z|<1\),
\[
\frac1{z-1}=-\frac1{1-z}=-\sum_{n\ge0}z^n,
\]
so \(f(z)=-z^{-1}-\sum_{n\ge0}z^n\). For \(|z|>1\), instead
\[
\frac1{z-1}=\frac1z\frac1{1-1/z}=\sum_{n\ge1}z^{-n},
\]
and cancellation of the first term gives \(f(z)=\sum_{n\ge2}z^{-n}\). The annulus is part of the answer."""),
ex(4,"Essential singularity encoded by infinitely many negative powers",r"""Substituting \(1/z\) into the exponential series gives
\[
e^{1/z}=1+\frac1z+\frac1{2!z^2}+\frac1{3!z^3}+\cdots.
\]
The Laurent series has infinitely many negative powers, so the singularity at zero is essential. The coefficient of \(z^{-1}\) is \(1\), anticipating the residue."""),
ex(7,"Expansion about a shifted point",r"""Expand \(1/(z+1)\) about \(z_0=1\). With \(w=z-1\),
\[
\frac1{z+1}=\frac1{2+w}=\frac12\sum_{n\ge0}(-w/2)^n,
\]
valid for \(|w|<2\). For \(|w|>2\), rewrite instead as \(w^{-1}(1+2/w)^{-1}\), producing a Laurent series in negative powers. The same singularity at \(z=-1\) sets the annular boundary.""")],
standard=[
q("Inner expansion",r"Find the Laurent series of \(1/(z(1-z))\) for \(0<|z|<1\).",r"Use the geometric series for \(1/(1-z)\).",r"The series is \(z^{-1}+1+z+z^2+\cdots\)."),
q("Outer expansion",r"Expand \(1/(z-2)\) for \(|z|>2\).",r"Factor out \(z\).",r"One obtains \(z^{-1}(1-2/z)^{-1}=\sum_{n\ge0}2^n z^{-n-1}\)."),
q("Coefficient extraction",r"What is the coefficient of \(z^{-1}\) in \(e^{1/z}\)?",r"Read it from the exponential series.",r"The coefficient is \(1\)."),
q("Principal part",r"Find the principal part of \(3/z^4-2/z+7+z\) at zero.",r"Keep only negative powers.",r"The principal part is \(3z^{-4}-2z^{-1}\)."),
q("Annulus boundaries",r"For a Laurent expansion about zero of \(1/((z-1)(z-3))\), name the natural radial regions.",r"Use distances from the center to the singularities.",r"The regions are \(|z|<1\), \(1<|z|<3\), and \(|z|>3\), excluding the singular circles themselves.")],
proof=[
q("Laurent coefficient formula",r"Derive the contour formula for a Laurent coefficient \(a_n\) on an annulus.",r"Multiply by \((z-z_0)^{-n-1}\) and integrate around a circle in the annulus.",r"Termwise integration kills every power except the one with exponent \(-1\), yielding \(a_n=(2\pi i)^{-1}\int f(z)/(z-z_0)^{n+1}dz\)."),
q("Uniqueness",r"Prove uniqueness of the Laurent expansion on an annulus.",r"Use the coefficient formula.",r"Every coefficient is determined by the contour integral formula, so two Laurent expansions of the same function must have identical coefficients."),
q("Independence of radius",r"Show that Laurent coefficients do not depend on which circle inside the annulus is used.",r"Apply Cauchy's theorem to the region between two circles.",r"The relevant coefficient integrand is holomorphic throughout the intervening annulus, so its integrals over the two positively oriented circles are equal."),
q("Taylor as a special Laurent series",r"Explain why a Laurent series with no negative powers is a Taylor series.",r"The nonnegative coefficients define an ordinary power series.",r"With all negative coefficients zero, the representation extends analytically across the center and is precisely the Taylor expansion there.")],
test=[
q("Wrong geometric expansion",r"Why is \(1/(1-z)=\sum z^n\) invalid for \(|z|>1\)?",r"Check the geometric ratio.",r"The terms \(z^n\) do not even tend to zero when \(|z|>1\). One must expand in powers of \(1/z\) instead."),
q("Annulus omitted",r"Why is a Laurent formula incomplete without its annulus of validity?",r"Different geometric rewritings can produce different series.",r"The same function can have distinct Laurent expansions in different annuli centered at the same point. The convergence region determines which series represents the function."),
q("Finite principal part",r"Does a finite principal part necessarily indicate an essential singularity?",r"Compare the singularity classification by negative terms.",r"No. A finite nonempty principal part corresponds to a pole; infinitely many negative terms characterize an essential singularity.")],
application=[
q("Residue preview",r"Why is the \((z-z_0)^{-1}\) Laurent coefficient especially important for contour integration?",r"Integrate each Laurent monomial around a circle.",r"Every monomial integrates to zero except exponent \(-1\), whose integral is \(2\pi i\). Thus that coefficient alone controls the local contour contribution."),
q("Local singularity diagnosis",r"How does a computed Laurent series distinguish removable, pole, and essential behavior?",r"Inspect the principal part.",r"No negative powers means removable; finitely many negative powers means a pole; infinitely many negative powers means an essential singularity.")],
challenge=[
q("Three radial regions",r"Find the form of the Laurent expansion of \(1/(z(z-1)(z-2))\) on each of \(0<|z|<1\), \(1<|z|<2\), and \(|z|>2\).",r"Use partial fractions and choose a geometric expansion for each factor appropriate to the region.",r"Partial fractions reduce the problem to terms at \(0,1,2\). In each annulus, expand factors with singularities outside in nonnegative powers of \(z\) and factors inside in negative powers of \(z\); the resulting series are different but unique on their regions."),
q("Center one",r"Describe the natural annuli for the Laurent expansion of \(1/(z(z-2))\) about \(z_0=1\).",r"Measure the two singularity distances from the new center.",r"Both singularities are at distance one from the center. Thus there are only two radial regions: \(|z-1|<1\) and \(|z-1|>1\), with the singular circle separating them.")])

DATA["IV/09"] = pack(
examples=[
ex(1,"Removing a fake singularity",r"""The quotient \(\sin z/z\) is undefined at zero in its displayed form, but
\[
\frac{\sin z}{z}=1-\frac{z^2}{3!}+\frac{z^4}{5!}-\cdots.
\]
The right side is analytic at zero and has value \(1\) there. Defining \(f(0)=1\) removes the singularity."""),
ex(4,"Detecting a pole and its order",r"""For \(f(z)=e^z/z^3\), the numerator is nonzero at zero. Hence \(z^3f(z)=e^z\) extends holomorphically with nonzero value at zero. Therefore zero is a pole of order three. The leading Laurent term is \(z^{-3}\)."""),
ex(7,"An essential singularity",r"""The Laurent series
\[
e^{1/z}=\sum_{n=0}^{\infty}\frac{1}{n!z^n}
\]
contains infinitely many negative powers. Thus zero is essential. No multiplication by a finite power of \(z\) can make the function bounded or holomorphic at the origin.""")],
standard=[
q("Removable quotient",r"Classify the singularity of \((e^z-1)/z\) at zero.",r"Expand the numerator or take a limit.",r"The quotient tends to one and has a Taylor expansion beginning \(1+z/2+\cdots\), so the singularity is removable."),
q("Pole order",r"Classify zero for \((1+z)/z^5\).",r"The numerator is nonzero at zero.",r"Zero is a pole of order five."),
q("Essential exponential",r"Classify zero for \(e^{1/z^2}\).",r"Expand the exponential.",r"The Laurent series has infinitely many negative powers, so zero is essential."),
q("Zero versus pole",r"Classify zero for \(z^3/(e^z-1)^2\).",r"Use \(e^z-1=z+O(z^2)\).",r"The denominator has order two and the numerator order three, leaving a zero of order one after cancellation; the apparent singularity is removable."),
q("Limit criterion",r"If \(\lim_{z\to a}(z-a)^2f(z)=7\ne0\), what singularity does \(f\) have at \(a\)?",r"Use the pole characterization.",r"The point is a pole of order two.")],
proof=[
q("Bounded removable theorem",r"Prove that a bounded holomorphic function on a punctured disk has a removable singularity at the center.",r"Apply Cauchy's formula on circles avoiding the point or examine Laurent coefficients.",r"For negative Laurent coefficients, the coefficient estimate contains a positive power of the circle radius. Boundedness forces each such coefficient to zero as the radius shrinks, leaving a Taylor series."),
q("Pole characterization",r"Prove that \(a\) is a pole of order \(m\) exactly when \((z-a)^m f(z)\) extends holomorphically and nonvanishingly at \(a\).",r"Use the finite principal part factorization.",r"A pole of order \(m\) has Laurent form \((z-a)^{-m}g(z)\) with \(g(a)\ne0\). Multiplying removes exactly that pole; the converse follows by dividing the nonvanishing extension by \((z-a)^m\)."),
q("Removable from finite limit",r"Show that a finite limit of \(f(z)\) as \(z\to a\) makes the isolated singularity removable.",r"A finite limit gives local boundedness.",r"Near \(a\), the function is bounded, so the removable singularity theorem applies. Defining the missing value to be the limit yields continuity and holomorphicity."),
q("Essential criterion",r"Show that an isolated singularity is essential exactly when its Laurent principal part has infinitely many nonzero terms.",r"Use the exhaustive Laurent classification.",r"No negative terms gives a removable point; finitely many gives a pole. The only remaining case is infinitely many negative terms, which therefore characterizes an essential singularity.")],
test=[
q("Unbounded means pole",r"Does unboundedness near an isolated singularity always imply a pole?",r"Recall essential singularities.",r"No. Essential singularities are also unbounded in every punctured neighborhood. One needs finite principal part or equivalent pole behavior."),
q("Vanishing product",r"If \((z-a)f(z)\to0\), must \(f\) have a removable singularity?",r"Apply the removable theorem first to \(g(z)=(z-a)f(z)\).",r"Yes. The function \(g\) extends holomorphically with \(g(a)=0\), so \(g(z)=(z-a)h(z)\) for a holomorphic \(h\). Hence \(f=h\) on the punctured disk and extends holomorphically across \(a\)."),
q("Classification requires isolation",r"Can the removable, pole, essential trichotomy be applied at an accumulation point of singularities?",r"Check the word isolated.",r"No. The Laurent annulus around the point may not exist, so the isolated singularity classification does not apply.")],
application=[
q("Regularizing a formula",r"Why is removing a removable singularity useful in analysis or computation?",r"The extended function is genuinely holomorphic at the point.",r"The extension eliminates artificial division by zero, restores stable local evaluation, and permits direct use of Taylor series and derivative formulas across the point."),
q("Pole order and blowup",r"How does pole order describe the leading local growth?",r"Use the factorization \(f=(z-a)^{-m}g\) with \(g(a)\ne0\).",r"The magnitude behaves like a nonzero constant times \(|z-a|^{-m}\) to leading order, so the integer \(m\) quantifies the algebraic blowup rate.")],
challenge=[
q("Reciprocal classification",r"If \(f\) has a pole of order \(m\) at \(a\), classify \(1/f\) after extension.",r"Invert the local factorization.",r"Writing \(f=(z-a)^{-m}g\) with \(g(a)\ne0\) gives \(1/f=(z-a)^m/g\), which extends holomorphically with a zero of order \(m\)."),
q("Behavior at infinity",r"Explain how to classify the point at infinity for a function by studying \(g(w)=f(1/w)\) at \(w=0\).",r"The map \(w=1/z\) turns large \(z\) into small \(w\).",r"The singularity type of \(g\) at zero defines the type of \(f\) at infinity. For example, a polynomial of degree \(m\) gives a pole of order \(m\) at infinity.")])

DATA["IV/10"] = pack(
examples=[
ex(1,"Residue at a simple pole",r"""For \(f(z)=e^z/(z-1)\),
\[
\operatorname{Res}_{z=1}f=\lim_{z\to1}(z-1)f(z)=e.
\]
Therefore a positively oriented contour enclosing \(1\) and no other singularities has integral \(2\pi i e\)."""),
ex(4,"A second order pole",r"""Consider \(f(z)=1/(z^2(z-1))\) at \(z=0\). Since the pole has order two,
\[
\operatorname{Res}_{z=0}f
=\left.\frac{d}{dz}\frac1{z-1}\right|_{z=0}=-1.
\]
The derivative formula avoids computing the full Laurent series."""),
ex(7,"Summing local contributions",r"""For
\[
f(z)=\frac{1}{(z-1)(z+1)},
\]
the residues at \(1\) and \(-1\) are \(1/2\) and \(-1/2\). A contour enclosing both has zero integral, while a contour enclosing only \(1\) has integral \(\pi i\). The residue theorem converts a global contour integral into a finite sum of local coefficients.""")],
standard=[
q("Simple rational residue",r"Find \(\operatorname{Res}_{z=2}1/(z(z-2))\).",r"Multiply by \(z-2\) and take the limit.",r"The residue is \(1/2\)."),
q("Exponential residue",r"Find the residue of \(e^z/(z-i)\) at \(i\).",r"It is a simple pole.",r"The residue is \(e^i\)."),
q("Second order residue",r"Find \(\operatorname{Res}_{z=0}e^z/z^2\).",r"Read the coefficient of \(z^{-1}\) or differentiate the numerator.",r"Since \(e^z=1+z+\cdots\), the residue is \(1\)."),
q("Contour sum",r"A contour encloses simple poles with residues \(2\) and \(-3i\). Find the integral.",r"Multiply the residue sum by \(2\pi i\).",r"The integral is \(2\pi i(2-3i)=6\pi+4\pi i\)."),
q("Residue from Laurent series",r"What is the residue at zero of \(4z^{-3}-7z^{-1}+2+z\)?",r"Select the coefficient of \(z^{-1}\).",r"The residue is \(-7\).")],
proof=[
q("Residue theorem from Laurent series",r"Prove the residue theorem for finitely many isolated singularities inside a contour.",r"Excise small circles around the singularities and apply Cauchy's theorem to the remaining region.",r"The outer integral equals the sum of the small circle integrals. Each small circle integral is \(2\pi i\) times the local \(z^{-1}\) Laurent coefficient, yielding the residue sum."),
q("Simple pole formula",r"Prove \(\operatorname{Res}_a(g/h)=g(a)/h'(a)\) when \(h(a)=0\), \(h'(a)\ne0\), and \(g(a)\ne0\).",r"Factor the simple zero of \(h\).",r"Write \(h(z)=(z-a)k(z)\) with \(k(a)=h'(a)\). Then \((z-a)g/h=g/k\), whose limit at \(a\) is \(g(a)/h'(a)\)."),
q("Higher pole formula",r"Derive the residue formula for a pole of order \(m\).",r"Multiply by \((z-a)^m\) and take the Taylor coefficient of order \(m-1\).",r"If \(g=(z-a)^m f\) is holomorphic, the \((z-a)^{-1}\) term of \(f\) comes from the \((m-1)\)-st Taylor coefficient of \(g\), giving \(g^{(m-1)}(a)/(m-1)!\)."),
q("Residue of a derivative",r"Show that the residue of \(f'\) at an isolated singularity is zero.",r"Differentiate the Laurent series termwise.",r"A derivative term has exponent \(n-1\) with coefficient \(na_n\). Exponent \(-1\) would require \(n=0\), whose coefficient is zero. Hence there is no \((z-a)^{-1}\) term.")],
test=[
q("Pole on contour",r"Why is the ordinary residue theorem not directly applicable when a pole lies on the contour?",r"The integrand is not defined continuously along the path.",r"The contour integral is not an ordinary integral under the theorem's hypotheses. Indentation or principal value methods require separate arguments."),
q("Orientation",r"What happens to the residue theorem for clockwise orientation?",r"Reverse the contour.",r"The integral becomes \(-2\pi i\) times the enclosed residue sum."),
q("Outside residues",r"Should poles outside a contour be included in the residue sum?",r"Only singularities in the interior contribute.",r"No. Exterior poles do not affect the contour integral as long as the integrand is holomorphic on a neighborhood of the contour itself.")],
application=[
q("Logarithmic derivative",r"If \(f\) has a zero of order \(m\) at \(a\), find the residue of \(f'/f\) there.",r"Factor \(f=(z-a)^m g\).",r"Then \(f'/f=m/(z-a)+g'/g\), and the second term is holomorphic at \(a\). The residue is \(m\)."),
q("Residue at infinity",r"For a rational function decaying as \(1/z^2\) or faster, what relation holds among all finite residues?",r"Integrate on a sufficiently large circle and let its radius grow.",r"The large circle integral tends to zero, so the sum of all finite residues is zero. Equivalently the residue at infinity vanishes.")],
challenge=[
q("Counting zeros and poles",r"Explain why residues of \(f'/f\) naturally count zeros positively and poles negatively.",r"Use local factorizations at zeros and poles.",r"A zero of order \(m\) contributes residue \(m\); a pole of order \(n\) contributes \(-n\). Integrating \(f'/f\) therefore counts the divisor inside the contour."),
q("Residue at infinity formula",r"Show formally that \(\operatorname{Res}_\infty f=-\sum \operatorname{Res}_{a_k}f\) for a meromorphic function on the sphere.",r"Take a large positively oriented circle enclosing all finite poles.",r"The finite residue theorem gives the large circle integral as \(2\pi i\) times the finite sum. Under \(w=1/z\), the same contour is a negatively oriented small circle around infinity, producing the stated negative relation.")])

DATA["IV/11"] = pack(
examples=[
ex(1,"The basic rational integral",r"""For \(a>0\), integrate \(1/(z^2+a^2)\) over the upper semicircle. The only enclosed pole is \(ia\), with residue \(1/(2ia)\). The arc contribution tends to zero because the integrand is \(O(R^{-2})\). Hence
\[
\int_{-\infty}^{\infty}\frac{dx}{x^2+a^2}=2\pi i\frac1{2ia}=\frac{\pi}{a}.
\]"""),
ex(4,"Fourier damping by contour choice",r"""For \(b>0\), consider \(e^{ibz}/(z^2+a^2)\) in the upper half-plane. Since \(|e^{ib(x+iy)}|=e^{-by}\), the exponential damps the large arc. The pole at \(ia\) contributes
\[
\int_{-\infty}^{\infty}\frac{e^{ibx}}{x^2+a^2}\,dx=\frac{\pi}{a}e^{-ab}.
\]
Taking real parts gives the cosine integral."""),
ex(7,"A quartic denominator",r"""For \(1/(z^4+1)\), the upper half-plane poles are \(e^{i\pi/4}\) and \(e^{3i\pi/4}\). Their residues are \(1/(4z_k^3)\). Summing them and multiplying by \(2\pi i\), while the large arc vanishes, gives
\[
\int_{-\infty}^{\infty}\frac{dx}{x^4+1}=\frac{\pi}{\sqrt2}.
\]
Evenness then yields \(\int_0^\infty dx/(x^4+1)=\pi/(2\sqrt2)\).""")],
standard=[
q("Cauchy kernel integral",r"Evaluate \(\int_{-\infty}^{\infty}dx/(x^2+4)\).",r"Use the formula with \(a=2\).",r"The value is \(\pi/2\)."),
q("Cosine transform",r"For \(b>0\), evaluate \(\int_{-\infty}^{\infty}\cos(bx)/(x^2+1)\,dx\).",r"Use the upper half-plane exponential contour.",r"The value is \(\pi e^{-b}\)."),
q("Half line",r"Evaluate \(\int_0^\infty dx/(x^2+1)\).",r"Use evenness.",r"It is half of \(\pi\), so the value is \(\pi/2\)."),
q("Arc decay",r"If a rational integrand is \(O(R^{-3})\) on a semicircle of radius \(R\), what order bound holds for the arc integral?",r"Multiply the supremum by arc length.",r"The arc length is \(O(R)\), so the integral is \(O(R^{-2})\) and tends to zero."),
q("Quartic half line",r"Use the full line value to compute \(\int_0^\infty dx/(x^4+1)\).",r"The integrand is even.",r"The value is \(\pi/(2\sqrt2)\).")],
proof=[
q("Semicircle arc lemma for rational decay",r"Prove that if \(|f(z)|\le C/R^{1+\epsilon}\) on the upper semicircle of radius \(R\), then the arc integral tends to zero.",r"Use the ML inequality and arc length \(\pi R\).",r"The bound is \(\pi R C/R^{1+\epsilon}=\pi C/R^\epsilon\to0\)."),
q("Cosine from exponential integral",r"Justify extracting the cosine integral as the real part of an exponential contour integral.",r"Use absolute convergence or a suitable limiting argument.",r"Since \(e^{ibx}=\cos(bx)+i\sin(bx)\), linearity separates real and imaginary parts. For the rational denominator used here, both limits are controlled by the contour estimates."),
q("Even reduction",r"Prove that an integrable even function satisfies \(\int_{-\infty}^{\infty}f=2\int_0^\infty f\).",r"Substitute \(x=-t\) on the negative half line.",r"The negative half line integral becomes \(\int_0^\infty f(-t)dt=\int_0^\infty f(t)dt\), and adding the positive half gives twice that value."),
q("Choosing the half-plane",r"For \(b<0\), explain why the lower half-plane is the natural choice for \(e^{ibz}\).",r"Inspect \(|e^{ib(x+iy)}|\).",r"The modulus is \(e^{-by}\). When \(b<0\), this decays for \(y<0\), so the lower semicircle provides damping rather than growth.")],
test=[
q("Insufficient decay",r"Why does an \(O(1/R)\) bound on a semicircle not by itself force the arc integral to vanish?",r"Multiply by the arc length.",r"The ML bound is only \(O(1)\), so it need not tend to zero. Stronger decay or oscillatory cancellation is required."),
q("Real pole",r"What obstructs applying the ordinary upper semicircle argument when the integrand has a pole on the real axis?",r"The contour passes through the singularity.",r"The real integral and contour integral are not ordinary integrals under the standard theorem. One needs indentation and often a principal value interpretation."),
q("Wrong exponential half-plane",r"What happens if \(b>0\) but the contour for \(e^{ibz}\) is closed in the lower half-plane?",r"Check the exponential modulus.",r"There \(y<0\), so \(e^{-by}\) grows exponentially. The large arc estimate generally fails.")],
application=[
q("Cauchy density normalization",r"Use the rational integral to verify that \(p(x)=a/(\pi(x^2+a^2))\) integrates to one for \(a>0\).",r"Factor the constant outside the known integral.",r"The integral is \(a/\pi\cdot\pi/a=1\), confirming normalization of the Cauchy density."),
q("Transform pair",r"What qualitative information does \(\int e^{ibx}/(x^2+a^2)dx=(\pi/a)e^{-a|b|}\) reveal?",r"Compare spatial pole distance with transform decay.",r"The imaginary pole distance \(a\) becomes the exponential decay rate in frequency. Singularities away from the real axis control transform decay.")],
challenge=[
q("Squared denominator",r"Outline how to evaluate \(\int_{-\infty}^{\infty}dx/(x^2+a^2)^2\).",r"There is a second order pole at \(ia\); use the higher pole residue formula.",r"The upper half-plane residue calculation yields \(\pi/(2a^3)\). The arc still vanishes because the integrand decays as \(R^{-4}\)."),
q("Indented contour preview",r"Explain the sign of the small upper indentation around a simple real pole when computing a principal value.",r"The small arc is traversed clockwise as the main contour detours above the pole.",r"A clockwise half circle contributes asymptotically \(-i\pi\) times the residue. Moving that term to the other side of the contour identity produces the familiar principal value contribution.")])
