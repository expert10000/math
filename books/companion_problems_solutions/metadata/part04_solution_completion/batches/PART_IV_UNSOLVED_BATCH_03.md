# Part IV Unsolved Solution Authoring Batch 03

- problems in batch: 20
- IDs: CP-IV-0043, CP-IV-0052, CP-IV-0086, CP-IV-0107, CP-IV-0124, CP-IV-0135, CP-IV-0138, CP-IV-0001, CP-IV-0002, CP-IV-0003, CP-IV-0006, CP-IV-0010, CP-IV-0011, CP-IV-0013, CP-IV-0021, CP-IV-0022, CP-IV-0026, CP-IV-0030, CP-IV-0032, CP-IV-0033

Author canonical worked solutions for these problems. Do not alter the problem statements.

## CP-IV-0043


- chapter line: 5840
- atlas source solution flag: `unknown`
- linked source-solution candidates: `none`
- embedded solution marker in problem body: `NO`

```tex
\par\noindent\textbullet\quad \textbf{(a)}\;
	Show that, if \(\zeta^{2}=z^{2}+1\) and
	\[
	z = i + r_{1}e^{i\theta_{1}} = -\,i + r_{2}e^{i\theta_{2}},
	\qquad r_{1},r_{2}>0,\ \theta_{1},\theta_{2}\in\mathbb{R},
	\]
	then
	\[
	\zeta \;=\; \pm\,(r_{1}r_{2})^{1/2}\,e^{\,i(\theta_{1}+\theta_{2})/2}.
	\]
	Explain briefly why \(z=\pm i\) are the branch points of the multifunction \((z^{2}+1)^{1/2}\).

	\medskip
```

## CP-IV-0052


- chapter line: 5857
- atlas source solution flag: `unknown`
- linked source-solution candidates: `none`
- embedded solution marker in problem body: `NO`

```tex
(restated).

Let $p(z)=z^{5}+z$.

	\par\noindent\textbullet\quad Find all $z$ with $|z|=1$ such that $\Im p(z)=0$.
	\par\noindent\textbullet\quad Compute $\Re p(z)$ at the points from (a).
	\par\noindent\textbullet\quad Sketch the curve $p\circ\gamma$ where $\gamma(t)=e^{2\pi i t}$.
	\par\noindent\textbullet\quad Using your sketch, determine for each real $x$ the number of solutions $z$ (counted with multiplicity) to $p(z)=x$ with $|z|<1$.

\paragraph{6. The map $p(z)=z^{5}+z$ on the unit circle.}
Let $z=e^{i\theta}$.
\[
p(e^{i\theta})=e^{5i\theta}+e^{i\theta}
=2\cos(2\theta)\,e^{i3\theta}.
\]

\emph{(a) Real axis crossings.} $\Im p=0 \iff \sin(5\theta)+\sin\theta=2\sin(3\theta)\cos(2\theta)=0$,
so $\theta=\frac{m\pi}{3}$ ($m=0,\dots,5$) or $\theta=\frac{\pi}{4}+\frac{k\pi}{2}$ ($k=0,1,2,3$).

\emph{(b) Real parts at these points.} $\Re p=\cos(5\theta)+\cos\theta=2\cos(3\theta)\cos(2\theta)$.
For $\cos(2\theta)=0$, $\Re p=0$; for $\theta=\frac{m\pi}{3}$ the values are $2,1,-1,-2,-1,1$.

\emph{(c) Sketch.} The curve $p(\gamma)$ ($\gamma(t)=e^{2\pi it}$) is a three-petal curve of maximal radius $2$, meeting the real axis at $-2,-1,0,1,2$.

\emph{(d) Number of solutions to $z^{5}+z=x$ with $|z|<1$, $x\in\mathbb R$.}
By the argument principle, the number equals the winding number of $p(\gamma)$ about $x$. From the sketch,
\[
N(x)=
\begin{cases}
	0, & |x|>2,\\[2pt]
	1, & 1<|x|<2,\\[2pt]
	2, & 0<|x|<1,\\[2pt]
	1, & x=0\ \text{(one interior root; the other four sit on/near the boundary)}.
\end{cases}
\]


\emph{Mellin/keyhole integrals.}
For $0<\Re\mu<2$ and $0<\phi<\pi$,
\[
\int_{0}^{\infty}\frac{x^{\mu-1}}{x^{2}+2x\cos\phi+1}\,dx
=\frac{\pi\,\sin(\mu\phi)}{\sin(\pi\mu)\,\sin\phi}.
\]
Derivation uses a keyhole contour with the branch of $\Log$ on $\mathbb C\setminus(-\infty,0]$.

\smallskip
\emph{Definitions.}
Mellin transform: $\mathcal M[f](s)=\int_{0}^{\infty}x^{s-1}f(x)\,dx$.
Keyhole contour: a contour encircling the positive real axis to capture the $2\pi i$ jump of the logarithm.

\medskip
\emph{Cauchyâ€™s root bound (polynomials).}
For $p(z)=z^{n}+a_{n-1}z^{n-1}+\cdots+a_0$, every root satisfies
\[
|z|<1+\max_{0\le k\le n-1}|a_k|=:A+1.
\]
Idea: on $|z|=R>A$, $|z|^{n}>\sum_{k\le n-1}|a_k||z|^{k}$, hence $|p(z)|>0$.

\smallskip
\emph{RouchĂ©â€™s theorem (context).}
If $f,g$ are holomorphic and $|f|>|g|$ on a simple closed curve, then $f$ and $f+g$ have the same number of zeros inside.

\medskip
\emph{Argument principle.}
If $f$ is meromorphic with no zeros/poles on a positively oriented simple closed curve $\gamma$,
\[
N-P=\frac{1}{2\pi i}\int_{\gamma}\frac{f'(z)}{f(z)}\,dz=\frac{1}{2\pi}\Delta_{\gamma}\arg f.
\]
For $f(z)=p(z)-x$ (polynomial minus real parameter), $P=0$, and the integral counts the zeros of $p(z)=x$ inside.

\smallskip
\emph{Unit circle parametrization for $p(z)=z^5+z$.}
For $z=e^{i\theta}$,
\[
p(e^{i\theta})=e^{i5\theta}+e^{i\theta}
=2\cos(2\theta)\,e^{i3\theta}.
\]
Thus $p(\partial\mathbb D)$ is a three-petal curve (max radius $2$) with real-axis crossings at $-2,-1,0,1,2$.

\medskip

\emph{(4) Mellin use.}
With $x^{2}+x+1=x^{2}+2x\cos(\pi/3)+1$, set $\mu=\alpha+1$, $\phi=\pi/3$:
\[
\int_{0}^{\infty}\frac{x^{\alpha}}{x^{2}+x+1}\,dx
=\frac{2\pi}{\sqrt3}\,\frac{\sin\!\big((\alpha+1)\pi/3\big)}{\sin(\pi\alpha)}
\quad(-1<\alpha<1,\ \alpha\neq 0).
\]

\smallskip
\emph{(5) Root bound.}
If $p(z)=z^{4}-7z^{2}+10$, then $A=\max\{7,10\}=10$, so every root has $|z|<11$.

\smallskip
\emph{(6) Winding numbers for $z^5+z=x$.}
From $p(e^{i\theta})=2\cos(2\theta)e^{i3\theta}$, the number of zeros of $z^5+z=x$ in $|z|<1$ (counting multiplicity) is
\[
N(x)=
\begin{cases}
	0, & |x|>2,\\
	1, & 1<|x|<2,\\
	2, & 0<|x|<1,\\
	1, & x=0.
\end{cases}
\]


\emph{Setup.}
For integrals of the form
\[
\int_{0}^{\infty} x^{\mu-1} F(x)\,dx,
\]
choose the branch $z^{\mu-1}=e^{(\mu-1)\Log z}$ with $\Log z=\log|z|+i\Arg z$ and a branch cut along a ray (typically the positive or negative real axis). The \emph{keyhole contour} $\Gamma_{R,\varepsilon}$ wraps once around this cut:

	\par\noindent\textbullet\quad upper bank: $x\in[\varepsilon,R]$ along the ray, angle $0$,
	\par\noindent\textbullet\quad large circle $C_R$: $|z|=R$, counterclockwise,
	\par\noindent\textbullet\quad lower bank: $x\in[R,\varepsilon]$ just below the ray, angle $2\pi$,
	\par\noindent\textbullet\quad small circle $c_\varepsilon$: $|z|=\varepsilon$, counterclockwise.

Along the lower bank, $z^{\mu-1}$ picks up the factor $e^{2\pi i(\mu-1)}$.

\medskip
\emph{Vanishing of circular arcs.}
If $f(z)=z^{\mu-1}/Q(z)$ and $Q$ is a polynomial, then
\[
\int_{C_R} f(z)\,dz \to 0 \quad (R\to\infty) \ \text{if}\ \Re\mu<\deg Q,
\qquad
\int_{c_\varepsilon} f(z)\,dz \to 0 \quad (\varepsilon\to0) \ \text{if}\ \Re\mu>0.
\]
Hence one typically assumes $0<\Re\mu<\deg Q$.

\medskip
\emph{Bank contributions and jump factor.}
Let $I=\displaystyle\int_{0}^{\infty}\frac{x^{\mu-1}}{Q(x)}\,dx$.
Upper bank contributes $I$. Lower bank contributes $-e^{2\pi i(\mu-1)} I$ (reversed orientation).
Thus
\[
\int_{\Gamma_{R,\varepsilon}} \frac{z^{\mu-1}}{Q(z)}\,dz
\;\xrightarrow[R\to\infty]{\varepsilon\to0}\;
\bigl(1-e^{2\pi i(\mu-1)}\bigr)\,I
=2i\,e^{i\pi(\mu-1)}\sin(\pi\mu)\,I.
\]

\medskip
\emph{Residue theorem.}
If $Q$ has zeros $a_k$ not on the cut, then
\[
\int_{\Gamma_{R,\varepsilon}} \frac{z^{\mu-1}}{Q(z)}\,dz
\to 2\pi i \sum_k \operatorname{Res}\!\left(\frac{z^{\mu-1}}{Q(z)}; a_k\right).
\]
Equate with the bank expression to solve for $I$.

\medskip
\emph{Example 1 (Eulerâ€™s Beta integral).}
For $Q(z)=1+z$ and $0<\Re\mu<1$,
\[
\int_{0}^{\infty}\frac{x^{\mu-1}}{1+x}\,dx
=\frac{\pi}{\sin(\pi\mu)}.
\]

\medskip
\emph{Example 2 (quadratic denominator).}
For $Q(z)=z^{2}+2z\cos\phi+1=(z-e^{i\phi})(z-e^{-i\phi})$ with $0<\phi<\pi$ and $0<\Re\mu<2$,
\[
\int_{0}^{\infty}\frac{x^{\mu-1}}{x^{2}+2x\cos\phi+1}\,dx
=\frac{\pi\,\sin(\mu\phi)}{\sin(\pi\mu)\,\sin\phi}.
\]
\emph{Sketch.} The poles are at $e^{\pm i\phi}$; compute
\[
\operatorname{Res}\left(\frac{z^{\mu-1}}{(z-e^{i\phi})(z-e^{-i\phi})};e^{i\phi}\right)
=\frac{e^{i\phi(\mu-1)}}{2i\sin\phi},\quad
\operatorname{Res}(\cdots;e^{-i\phi})=\frac{e^{-i\phi(\mu-1)}}{-2i\sin\phi}.
\]
Sum and equate with the bank expression.

\medskip
\emph{Pitfalls.}
(1) Be consistent with the branch cut; (2) ensure the circular arcs vanish (conditions on $\Re\mu$);
(3) avoid poles on the cut (move the cut, or indent and take principal values if needed).
```

## CP-IV-0086


- chapter line: 6042
- atlas source solution flag: `unknown`
- linked source-solution candidates: `none`
- embedded solution marker in problem body: `NO`

```tex
\par\noindent\textbullet\quad \textbf{Essential:} neither removable nor pole. The Laurent expansion at $a$ then has infinitely many negative powers.

\medskip
\emph{Casorati--Weierstrass \& Picard (context for Problem 9).}
If $a$ is an essential singularity of $f$, then the image of any punctured neighborhood of $a$ is dense in $\mathbb C$
(Casorati--Weierstrass). A stronger statement (Great Picard) says that near an essential singularity $f$ attains every complex value, with at most one exception, infinitely often.

\medskip
\emph{Identity theorem \& isolated zeros.}
If $f,g$ are holomorphic on a domain $U$ and $f=g$ on a set with a limit point in $U$, then $f\equiv g$ on $U$.
Consequently, a nonzero holomorphic function on $U$ has zeros that do not accumulate in $U$.

\medskip
\emph{Path independence and primitives (for Problem 10).}
If $\omega(z)\,dz$ is holomorphic on a simply connected domain $D$, then
\[
F(z):=\int_{z_0}^{z}\omega(\zeta)\,d\zeta
\]
is well defined (independent of path), holomorphic on $D$, and satisfies $F'=\omega$.
In particular, if $0\notin D$, the $1$-form $d\zeta/\zeta$ has the primitive
$F(z)=\int_{z_0}^z \frac{d\zeta}{\zeta}$ on $D$, so $e^{F}$ gives a single-valued branch of the logarithm.

\smallskip
\emph{Winding number criterion for a logarithm.}
A holomorphic, nowhereâ€“vanishing function $g$ on a domain $D$ admits a holomorphic branch of $\Log g$ on $D$
iff $\displaystyle \int_{\gamma} \frac{g'}{g}\,dz=0$ for every closed curve $\gamma\subset D$;
equivalently, $g(\gamma)$ has winding number $0$ about $0$ for all such $\gamma$.
When $D$ is simply connected and $g$ never vanishes, a branch of $\Log g$ always exists.

\medskip
\emph{Power series, radius of convergence, and natural boundaries (for Problem 11).}
A power series $\sum_{n\ge0} a_n z^n$ has a radius of convergence $R\in[0,\infty]$ determined by the Cauchy--Hadamard formula.
It defines an analytic function on $|z|<R$ and cannot be analytically continued across points where the function has a singularity.
A Jordan curve $\Gamma$ is a \emph{natural boundary} for $f$ if no analytic continuation of $f$ exists across \emph{any} point of $\Gamma$.

\smallskip
\emph{Hadamard gap theorem (lacunary series).}
If $f(z)=\sum_{k\ge1} a_k z^{n_k}$ with strictly increasing exponents $(n_k)$ satisfying
$\displaystyle \liminf_{k\to\infty} \frac{n_{k+1}}{n_k}>1$ (``Hadamard gaps''),
then the circle of convergence $|z|=R$ is a \emph{natural boundary} for $f$ (unless $f$ is a polynomial).
In particular, for $n_k=2^k$ (ratio $=2$) the unit circle is a natural boundary when $R=1$.

\medskip
\emph{Dense boundary singularities via functional identities (alternate route for Problem 11).}
If a function $f$ on $|z|<1$ satisfies identities of the form
\[
(1-z^{N})\,f(z)=P_N(z)\qquad (N\in\mathbb N),
\]
with $P_N$ polynomial and $N\to\infty$, then every $N$-th root of unity
is a singularity (unless canceled), and the union of these roots for $N\to\infty$ is dense on $|z|=1$.
Hence $|z|=1$ is a natural boundary (no analytic continuation across any boundary point).
```

## CP-IV-0107


- chapter line: 6099
- atlas source solution flag: `unknown`
- linked source-solution candidates: `none`
- embedded solution marker in problem body: `NO`

```tex
(Conformal equivalences and a harmonic function).

Find conformal equivalences between the following pairs of domains:

	\par\noindent\textbullet\quad The sector
	\[
	S_1=\{\,z\in\mathbb{C} : -\tfrac{\pi}{4}<\Arg z<\tfrac{\pi}{4}\,\}
	\]
	and the open unit disc
	\[
	\mathbb{D}=D(0,1)=\{\,w\in\mathbb{C}:|w|<1\,\}.
	\]

	\par\noindent\textbullet\quad The lens
	\[
	L=\{\,z\in\mathbb{C} : |z-1|<\sqrt{2}\ \text{and}\ |z+1|<\sqrt{2}\,\}
	\]
	and $\mathbb{D}$.

	\par\noindent\textbullet\quad The strip
	\[
	S=\{\,z\in\mathbb{C} : 0<\Im z<1\,\}
	\]
	and the quadrant
	\[
	Q=\{\,w\in\mathbb{C} : \Re w>0,\ \Im w>0\,\}.
	\]

\noindent
By considering a suitable bounded solution of Laplace's equation $u_{xx}+u_{yy}=0$ on $S$,
find a non-constant harmonic function on $Q$ which is constant on its boundary axes.
```

## CP-IV-0124


- chapter line: 6215
- atlas source solution flag: `unknown`
- linked source-solution candidates: `none`
- embedded solution marker in problem body: `NO`

```tex
Temperature in a right halfâ€“plane with a removed disk

The domain $D$ consists of the right-hand half plane $x>0$ with the circle $|z-a|=b$, $0<b<a$, and its interior removed.
	Find the temperature $u(x,y)$ in steady heat flow if $u=0$ on the $y$ axis, $u=1$ on $|z-a|=b$, and $u\to0$ at infinity.

	\medskip
	\noindent\textit{Hint:} Show that the mapping $\displaystyle \zeta=\frac{z-\alpha}{z+\alpha}$, with $\alpha$ real and positive,
	takes $D$ onto an annular region with the imaginary axis mapping to $|\zeta|=1$ and show that, if $\alpha^{2}=a^{2}-b^{2}$, then the image of $D$ is a concentric circular annulus.

	\bigskip\hrule\bigskip

	Consider the real-parameter MĂ¶bius map
	\[
	\zeta=\zeta(z)=\frac{z-\alpha}{z+\alpha}, \qquad \alpha>0.
	\]

	For $z=iy$ we have
	\[
	\left|\frac{iy-\alpha}{iy+\alpha}\right|=1 \quad\text{(numerator and denominator are conjugates),}
	\]
	so the $y$â€“axis maps to the unit circle $|\zeta|=1$.

	\paragraph{Image of the circle $\boldsymbol{|z-a|=b}$.}
	Write $z=a+be^{i\theta}$ and compute
	\[
	|\zeta|^{2}
	=\frac{|a-\alpha+be^{i\theta}|^{2}}{|a+\alpha+be^{i\theta}|^{2}}
	=\frac{A+B\cos\theta}{C+D\cos\theta},
	\]
	where
	\[
	A=(a-\alpha)^{2}+b^{2}, \qquad B=2b(a-\alpha), \qquad
	C=(a+\alpha)^{2}+b^{2}, \qquad D=2b(a+\alpha).
	\]
	For $|\zeta|$ to be constant on the circle (i.e. the image is a circle \emph{centered at the origin}),
	the $\cos\theta$â€“dependence must drop out:
	\[
	\frac{A+B\cos\theta}{\,C+D\cos\theta\,}\equiv\frac{A}{C}
	\quad\Longleftrightarrow\quad AD=BC.
	\]
	We now verify that
	\[
	AD-BC
	=2b\Big[(a+\alpha)((a-\alpha)^{2}+b^{2})-(a-\alpha)((a+\alpha)^{2}+b^{2})\Big]
	=4b\alpha\,(\alpha^{2}+b^{2}-a^{2}).
	\]
	Thus $AD=BC$ is equivalent to
	\[
	\boxed{\ \alpha^{2}=a^{2}-b^{2}\ }.
	\]
	With this choice (note $a>b>0\Rightarrow \alpha>0$), the ratio becomes \emph{constant}:
	\[
	|\zeta|^{2}=\frac{A}{C}
	=\frac{(a-\alpha)^{2}+b^{2}}{(a+\alpha)^{2}+b^{2}}
	=\frac{2a(a-\alpha)}{2a(a+\alpha)}
	=\frac{a-\alpha}{a+\alpha}.
	\]
	Hence the circle $|z-a|=b$ maps to the circle $|\zeta|=\rho$ with
	\[
	\boxed{\ \rho=\sqrt{\frac{a-\alpha}{a+\alpha}}\in(0,1). \ }
	\]

	Therefore, for $\alpha=\sqrt{a^{2}-b^{2}}$, the map $z\mapsto\zeta$ sends the domain $D$
	(right halfâ€“plane with the closed disk $\{|z-a|\le b\}$ removed) onto the concentric circular \emph{annulus}
	\[
	\mathcal A=\{\ \rho<|\zeta|<1\ \}.
	\]
	The boundary pieces correspond as follows:
	\[
	\{x=0\}\ \longmapsto\ |\zeta|=1,
	\qquad
	\{|z-a|=b\}\ \longmapsto\ |\zeta|=\rho.
	\]

	\bigskip\hrule\bigskip

	Let $U(\zeta)$ denote the temperature in the $\zeta$â€“plane. Harmonicity is preserved by conformal maps, so
	$U$ is harmonic on $\mathcal A$ and the boundary data become
	\[
	U=0 \ \ \text{on}\ \ |\zeta|=1,
	\qquad
	U=1 \ \ \text{on}\ \ |\zeta|=\rho.
	\]
	By rotational symmetry, $U$ depends only on $r=|\zeta|$. The general radial harmonic function on an annulus is
	$A\log r + B$. Imposing the boundary values gives
	\[
	U(r)=\frac{\log(1/r)}{\log(1/\rho)}
	=\frac{-\log r}{-\log \rho}
	=\frac{\log r}{\log \rho}
	\quad\text{for}\quad \rho<r<1.
	\]
	(Any of the three displayed forms is correct; we will use the first one momentarily.)

	\bigskip\hrule\bigskip

	The physical temperature is $u(z)=U(\zeta(z))$ with $r=|\zeta(z)|=\left|\frac{z-\alpha}{z+\alpha}\right|$.
	Hence
	\[
	u(z)
	=U\!\left(\left|\frac{z-\alpha}{z+\alpha}\right|\right)
	=\frac{\displaystyle \log\!\left(\frac{1}{\left|\frac{z-\alpha}{z+\alpha}\right|}\right)}
	{\displaystyle \log\!\left(\frac{1}{\rho}\right)}
	=\frac{\displaystyle \log\left|\frac{z+\alpha}{z-\alpha}\right|}
	{\displaystyle \log\!\left(\frac{1}{\rho}\right)}.
	\]
	Since $\displaystyle \rho=\sqrt{\frac{a-\alpha}{a+\alpha}}$ we have
	\[
	\log\!\left(\frac{1}{\rho}\right)
	=\frac{1}{2}\,\log\!\left(\frac{a+\alpha}{a-\alpha}\right).
	\]
	Therefore a convenient explicit form is
	\[
	\boxed{\quad
		u(z)
		=\frac{2\,\log\!\left|\dfrac{z+\alpha}{z-\alpha}\right|}
		{\log\!\left(\dfrac{a+\alpha}{a-\alpha}\right)},
		\qquad
		\alpha=\sqrt{a^{2}-b^{2}}.
		\quad}
	\]

	\bigskip

		\par\noindent\textbullet\quad \textbf{On the $y$--axis $x=0$:} for $z=iy$ we have $\left|\dfrac{z-\alpha}{z+\alpha}\right|=1$,
		so the numerator $\log\left|\dfrac{z+\alpha}{z-\alpha}\right|=0$ and hence $u=0$.
		\par\noindent\textbullet\quad \textbf{On the circle $|z-a|=b$:} by construction $|\zeta|=\rho$, i.e.
		$\left|\dfrac{z-\alpha}{z+\alpha}\right|=\rho$, so
		$\log\left|\dfrac{z+\alpha}{z-\alpha}\right|=\log\!\left(\dfrac{1}{\rho}\right)$
		and the fraction evaluates to $u=1$.
		\par\noindent\textbullet\quad \textbf{At infinity:} as $|z|\to\infty$, $\left|\dfrac{z+\alpha}{z-\alpha}\right|\to 1$,
		so the numerator $\to 0$ and $u(z)\to 0$.

	\bigskip\hrule\bigskip

	With $\alpha=\sqrt{a^{2}-b^{2}}$ and $\displaystyle \rho=\sqrt{\frac{a-\alpha}{a+\alpha}}$,
	the MĂ¶bius map $\displaystyle \zeta=\frac{z-\alpha}{z+\alpha}$ carries
	$D$ onto the annulus $\{\rho<|\zeta|<1\}$.
	The unique harmonic function with $U=1$ on $|\zeta|=\rho$ and $U=0$ on $|\zeta|=1$
	is $U(r)=\log(1/r)/\log(1/\rho)$, and hence
	\[
	u(z)=\frac{2\,\log\!\left|\dfrac{z+\alpha}{z-\alpha}\right|}
	{\log\!\left(\dfrac{a+\alpha}{a-\alpha}\right)}.
	\]
	This $u$ satisfies all the prescribed boundary conditions and $u(z)\to 0$ as $|z|\to\infty$.

\textbf{Background:} entire, odd; period $2\pi i$. \quad
\textbf{Zeros:} $z=i\pi k$; \textbf{poles:} none.\\
\textbf{Decomposition: } $w=u+iv=\sinh x\cos y + i\,\cosh x\sin y$.\\
\textbf{Vertical lines } $x=\text{const}$: $\left(\frac{u}{\sinh x}\right)^2+\left(\frac{v}{\cosh x}\right)^2=1$ (ellipses, foci $\pm i$).\\
\textbf{Horizontal lines } $y=\text{const}$: $\left(\frac{u}{\cos y}\right)^2-\left(\frac{v}{\sin y}\right)^2=-1$ (hyperbolas, foci $\pm i$).\\
\textbf{Strip mapping:}
\[
\boxed{\,\sinh:\ \{|\Im z|<\tfrac{\pi}{2}\}\ \xrightarrow{\ 1\text{--}1\ }\ \mathbb C\setminus i\big((-\infty,-1]\cup[1,\infty)\big)\,}
\]
Boundaries $y=\pm\frac{\pi}{2}$ map to imaginary rays $\pm i[1,\infty)$.

\bigskip\hrule\bigskip

\textbf{Background:} entire, even; period $2\pi i$. \quad
\textbf{Zeros:} $z=i\pi(k+\frac12)$; \textbf{poles:} none.\\
\textbf{Decomposition: } $w=u+iv=\cosh x\cos y + i\,\sinh x\sin y$.\\
\textbf{Vertical lines } $x=\text{const}$: $\left(\frac{u}{\cosh x}\right)^2+\left(\frac{v}{\sinh x}\right)^2=1$ (ellipses, foci $\pm1$).\\
\textbf{Horizontal lines } $y=\text{const}$: $\left(\frac{u}{\cos y}\right)^2-\left(\frac{v}{\sin y}\right)^2=1$ (hyperbolas, foci $\pm1$).\\
\textbf{Strip mapping:}
\[
\boxed{\,\cosh:\ \{|\Im z|<\pi\}\ \xrightarrow{\ 2\text{--}1\ }\ \mathbb C\setminus\big((-\infty,-1]\cup[1,\infty)\big)\,}
\]
On the half-strip $0<|\Im z|<\pi$, the map is 1--1 onto the slit plane.

\bigskip\hrule\bigskip

\textbf{Background:} meromorphic, odd; period $i\pi$. \quad
\textbf{Zeros:} $z=i\pi k$; \textbf{poles:} $z=i\pi(k+\tfrac12)$.\\
\textbf{Strip $\to$ disk:}
\[
\boxed{\,\tanh:\ \{|\Im z|<\tfrac{\pi}{2}\}\ \xrightarrow{\ 1\text{--}1\ }\ \mathbb D\,}
\]
Real line maps to $(-1,1)$; as $|\Im z|\to\pi/2$, $|\tanh z|\to1$.

\bigskip\hrule\bigskip

\textbf{Background:} meromorphic, odd; period $i\pi$. \quad
\textbf{Zeros:} $z=i\pi(k+\tfrac12)$; \textbf{poles:} $z=i\pi k$.\\
\textbf{Strip $\to$ exterior disk:}
\[
\boxed{\,\coth:\ \{|\Im z|<\tfrac{\pi}{2}\}\setminus\{0\}\ \xrightarrow{\ 1\text{--}1\ }\ \{\,|w|>1\,\}\,}
\]
Real line maps to $(-\infty,-1)\cup(1,\infty)$; $|\Im z|\to\pi/2$ gives $|w|\to1^+$.

Throughout, write $z=x+iy$, $x,y\in\mathbb R$, and $w=u+iv$ for the image.
Recall the basic identities
\[
\cosh z=\frac{e^{z}+e^{-z}}{2},\qquad
\sinh z=\frac{e^{z}-e^{-z}}{2},\qquad
\tanh z=\frac{\sinh z}{\cosh z},\qquad
\coth z=\frac{\cosh z}{\sinh z}.
\]
We use the principal branch of the logarithm $\log$ on $\mathbb C\setminus(-\infty,0]$, and principal square roots $\sqrt{\cdot}$ with branch cut on $(-\infty,0]$ unless stated otherwise.

\bigskip\hrule\bigskip

 \mbox{}\\[2pt]
$\sinh$ is an \emph{entire}, \emph{odd} function, with imaginary-periodicity:
\[
\sinh(-z)=-\sinh z,\qquad \sinh(z+2\pi i)=\sinh z.
\]
Zeros occur at $z_k=i\pi k$ for $k\in\mathbb Z$ (all simple). No poles.

\medskip

 \mbox{}\\[2pt]
With $z=x+iy$,
\[
\sinh z=\sinh x\cos y\ +\ i\,\cosh x\sin y \quad\Rightarrow\quad
u=\sinh x\cos y,\ \ v=\cosh x\sin y.
\]
From this, one obtains orthogonal families of confocal conics:
\begin{align*}
	x=\text{const}&:\quad \left(\frac{u}{\sinh x}\right)^{2}+\left(\frac{v}{\cosh x}\right)^{2}=1
	&&\text{(ellipses, foci at $\pm i$)},\\[2pt]
	y=\text{const}&:\quad \left(\frac{u}{\cos y}\right)^{2}-\left(\frac{v}{\sin y}\right)^{2}=-1
	&&\text{(hyperbolas, foci at $\pm i$)}.
\end{align*}
Real and imaginary axes map as:
\[
y=0:\ w=\sinh x\in\mathbb R\ \text{(onto $\mathbb R$)},\qquad
x=0:\ w=i\sin y\ \text{(onto the segment $i[-1,1]$)}.
\]

\medskip

 \mbox{}\\[2pt]
$\sinh'(z)=\cosh z$, and $\cosh z\neq 0$ on the strip $|\Im z|<\tfrac{\pi}{2}$; hence $\sinh$ is conformal there.

\medskip

 \mbox{}\\[2pt]
\[
\boxed{\
	\sinh:\ \{\,|\Im z|<\tfrac{\pi}{2}\,\}\ \xrightarrow[\ \text{biholomorphism}\ ]{}\
	\mathbb C\setminus i\big((-\infty,-1]\cup[1,\infty)\big)\ .
}\]
\emph{Explanation.} The boundary lines $y=\pm\frac{\pi}{2}$ map to the imaginary rays $\pm i[1,\infty)$
(via $v=\cosh x\,\sin y$ with $\sin(\pm\pi/2)=\pm1$ and $u=\sinh x\cos(\pm\pi/2)=0$), while the interior maps injectively since $\cosh z\neq0$ and periodicity in the imaginary direction has period $2\pi$, not $\pi$.

\medskip

 \mbox{}\\[2pt]
A principal inverse on the slit domain is
\[
\operatorname{arsinh} w=\log\!\big(w+\sqrt{w^{2}+1}\big),
\]
with branch cuts along $i(-\infty,-1]\cup i[1,\infty)$ so that $\Im(\operatorname{arsinh} w)\in(-\tfrac{\pi}{2},\tfrac{\pi}{2})$.

\medskip

 \mbox{}\\[2pt]
\[
\cosh^{2}z-\sinh^{2}z=1,\qquad
\sinh(z+\zeta)=\sinh z\,\cosh\zeta+\cosh z\,\sinh\zeta.
\]

\bigskip\hrule\bigskip

 \mbox{}\\[2pt]
$\cosh$ is \emph{entire}, \emph{even}, and $2\pi i$-periodic:
\[
\cosh(-z)=\cosh z,\qquad \cosh(z+2\pi i)=\cosh z.
\]
Zeros at $z=i\pi\big(k+\tfrac12\big)$, all simple. No poles.

\medskip

 \mbox{}\\[2pt]
With $z=x+iy$,
\[
\cosh z=\cosh x\cos y\ +\ i\,\sinh x\sin y \quad\Rightarrow\quad
u=\cosh x\cos y,\ \ v=\sinh x\sin y.
\]
Again one gets confocal conics:
\begin{align*}
	x=\text{const}&:\quad \left(\frac{u}{\cosh x}\right)^{2}+\left(\frac{v}{\sinh x}\right)^{2}=1
	&&\text{(ellipses, foci at $\pm1$)},\\[2pt]
	y=\text{const}&:\quad \left(\frac{u}{\cos y}\right)^{2}-\left(\frac{v}{\sin y}\right)^{2}=1
	&&\text{(hyperbolas, foci at $\pm1$)}.
\end{align*}
On the axes,
\[
y=0:\ w=\cosh x\in[1,\infty),\qquad
x=0:\ w=\cos y\in[-1,1].
\]

\medskip

 \mbox{}\\[2pt]
$\cosh'(z)=\sinh z$, which vanishes at $z=i\pi k$. Thus $\cosh$ fails to be injective across lines $y=k\pi$, but is injective on any strip avoiding these lines (e.g.\ $0<\Im z<\pi$).

\medskip

 \mbox{}\\[2pt]
\[
\boxed{\
	\cosh:\ \{\,0<\Im z<\pi\,\}\ \xrightarrow[\ \text{biholomorphism}\ ]{}\
	\mathbb C\setminus\big((-\infty,-1]\cup[1,\infty)\big)\ .
}\]
\emph{Explanation.} The midline $y=0$ maps to $[1,\infty)$; the top boundary $y=\pi$ maps to $(-\infty,-1]$; injectivity holds on $0<\Im z<\pi$ since there $\sinh z\neq0$.

\medskip

 \mbox{}\\[2pt]
\[
\operatorname{arcosh} w=\log\!\Big(w+\sqrt{w-1}\,\sqrt{w+1}\Big),
\]
with branch cuts along $(-\infty,-1]\cup[1,\infty)$ so that $\Re(\operatorname{arcosh} w)\ge0$ and $0<\Im(\operatorname{arcosh} w)<\pi$ on the principal sheet.

\medskip

 \mbox{}\\[2pt]
\[
\cosh(z+\zeta)=\cosh z\,\cosh\zeta+\sinh z\,\sinh\zeta,\qquad
\cosh z=1+2\sinh^{2}\!\frac{z}{2}.
\]

\bigskip\hrule\bigskip

 \mbox{}\\[2pt]
$\tanh$ is \emph{meromorphic}, \emph{odd}, and $i\pi$-periodic:
\[
\tanh(-z)=-\tanh z,\qquad \tanh(z+i\pi)=\tanh z.
\]
Zeros at $z=i\pi k$; poles (simple) at $z=i\pi\big(k+\tfrac12\big)$.

\medskip

 \mbox{}\\[2pt]
\[
\boxed{\
	\tanh:\ \{\,|\Im z|<\tfrac{\pi}{2}\,\}\ \xrightarrow[\ \text{biholomorphism}\ ]{}\ \mathbb D\ .
}\]
\emph{Boundary correspondence.} The real axis $y=0$ maps bijectively onto $(-1,1)$ (strictly increasing).
As $y\to\pm\frac{\pi}{2}$, $|\tanh(x+iy)|\to1$ uniformly in $x$; hence the horizontal boundaries map to $\partial\mathbb D$.

\medskip

 \mbox{}\\[2pt]
\[
\operatorname{artanh} w=\frac{1}{2}\log\!\left(\frac{1+w}{1-w}\right),
\qquad |w|<1,
\]
which maps $\mathbb D$ conformally onto $\{|\Im z|<\tfrac{\pi}{2}\}$.

\medskip

 \mbox{}\\[2pt]
\[
(\tanh z)'=\operatorname{sech}^{2}\!z,\qquad
\left|\tanh'(z)\right|=\frac{1}{|\cosh z|^{2}}
\]
and conjugating by a disk automorphism shows $\tanh$ is extremal for the disk-strip version of Schwarz--Pick.

\medskip

 \mbox{}\\[2pt]
Lines $x=\text{const}$ and $y=\text{const}$ in the strip map to orthogonal circle arcs inside $\mathbb D$ meeting $\partial\mathbb D$ orthogonally (images of preimages under the conformal equivalence with the half-plane followed by a Cayley map).

\bigskip\hrule\bigskip

 \mbox{}\\[2pt]
$\coth$ is \emph{meromorphic}, \emph{odd}, and $i\pi$-periodic:
\[
\coth(-z)=-\coth z,\qquad \coth(z+i\pi)=\coth z.
\]
Poles (simple) at $z=i\pi k$; zeros (simple) at $z=i\pi\big(k+\tfrac12\big)$.

\medskip

 \mbox{}\\[2pt]
\[
\boxed{\
	\coth:\ \{\,|\Im z|<\tfrac{\pi}{2}\,\}\setminus\{0\}\ \xrightarrow[\ \text{biholomorphism}\ ]{}\ \{\,|w|>1\,\}\ .
}\]
\emph{Boundary correspondence.} The real axis (excluding $0$) maps to the rays $(-\infty,-1)\cup(1,\infty)$.
As $y\to\pm\frac{\pi}{2}$, $|\coth(x+iy)|\to1^{+}$; thus horizontal boundaries map to the unit circle from the \emph{exterior} side.

\medskip

 \mbox{}\\[2pt]
\[
\operatorname{arcoth} w=\frac{1}{2}\log\!\left(\frac{w+1}{w-1}\right),\qquad |w|>1,
\]
with the standard logarithm branch so that $\Im(\operatorname{arcoth} w)\in(-\tfrac{\pi}{2},\tfrac{\pi}{2})$.

\medskip

 \mbox{}\\[2pt]
\[
\coth z=\tanh\!\left(z+\tfrac{i\pi}{2}\right),
\]
so the exterior-disk picture is just the disk picture shifted vertically by $i\pi/2$ and inverted via $w\mapsto 1/w$.

\bigskip\hrule\bigskip

 \mbox{}\\[2pt]
\[
\operatorname{arsinh} w=\log\!\big(w+\sqrt{w^{2}+1}\big),\qquad
\operatorname{arcosh} w=\log\!\big(w+\sqrt{w-1}\,\sqrt{w+1}\big),
\]
\[
\operatorname{artanh} w=\frac12\log\!\left(\frac{1+w}{1-w}\right),\qquad
\operatorname{arcoth} w=\frac12\log\!\left(\frac{w+1}{w-1}\right).
\]
Branch cuts are chosen to match the canonical target domains described above.

\medskip

 \mbox{}\\[2pt]
Using the Cayley map $C(\zeta)=\frac{1+\zeta}{1-\zeta}$ and its inverse $C^{-1}(w)=\frac{w-1}{w+1}$,
\[
\tanh z=\ C^{-1}\!\left(e^{2z}\right),\qquad
\coth z=\ C^{-1}\!\left(e^{2z}\right)^{-1},\qquad
\sinh z=\frac{e^{z}-e^{-z}}{2},\quad \cosh z=\frac{e^{z}+e^{-z}}{2}.
\]
Thus strip $\leftrightarrow$ disk/exterior-disk mappings for $\tanh$ and $\coth$ are just the exponentialâ€™s strip-to-sector equivalences composed with a Cayley map.

\medskip

 \mbox{}\\[2pt]
As $x\to\pm\infty$ with $y$ fixed, $\sinh z\sim \frac12 e^{x}e^{iy}$ and $\cosh z\sim \frac12 e^{x}e^{iy}$; hence horizontal lines map to asymptotically radial curves. For $\tanh$ and $\coth$, $|\tanh(x+iy)|\to 1$ and $|\coth(x+iy)|\to 1$ exponentially in $|x|$ (uniform in $y$ within the strip height).

\medskip

 \mbox{}\\[2pt]
$\sinh'(z)=\cosh z$ vanishes along $y=\frac{\pi}{2}+\pi\mathbb Z$; $\cosh'(z)=\sinh z$ vanishes along $y=\pi\mathbb Z$.
Therefore, the natural injectivity strips are $|\Im z|<\tfrac{\pi}{2}$ for $\sinh$ and $0<\Im z<\pi$ for $\cosh$.
For $\tanh$ and $\coth$, poles on the horizontal boundaries determine the natural strip height $\pi$.

\bigskip\hrule\bigskip

\[
\boxed{\
	\sinh:\ \{\,|\Im z|<\tfrac{\pi}{2}\,\}\ \longrightarrow\
	\mathbb C\setminus i\big((-\infty,-1]\cup[1,\infty)\big)\ \ \text{(biholomorphism)}\ .
}\]
\[
\boxed{\
	\cosh:\ \{\,0<\Im z<\pi\,\}\ \longrightarrow\
	\mathbb C\setminus\big((-\infty,-1]\cup[1,\infty)\big)\ \ \text{(biholomorphism)}\ .
}\]
\[
\boxed{\
	\tanh:\ \{\,|\Im z|<\tfrac{\pi}{2}\,\}\ \longrightarrow\ \mathbb D\ \ \text{(biholomorphism)}\ .
}\]
\[
\boxed{\
	\coth:\ \{\,|\Im z|<\tfrac{\pi}{2}\,\}\setminus\{0\}\ \longrightarrow\ \{\,|w|>1\,\}\ \ \text{(biholomorphism)}\ .
}\]

\medskip

If $\sinh z_{1}=\sinh z_{2}$ then $e^{z_{1}}-e^{-z_{1}}=e^{z_{2}}-e^{-z_{2}}$.
Rearranging gives $\{e^{z_{1}},e^{-z_{1}}\}=\{e^{z_{2}},e^{-z_{2}}\}$.
Taking logs in the horizontal strip $|\Im z|<\pi/2$ (where the exponential is injective modulo $2\pi i$) forces $z_{1}=z_{2}$.

Set $z=x\pm i\pi/2$. Then $\sinh z=\sinh x\cdot 0 \ \pm i\,\cosh x$, so the boundaries map to $\pm i[1,\infty)$; the interior cannot reach those rays by the open mapping theorem and the maximum modulus principle applied to $1/(\sinh z\mp i)$.

  apply to $\cosh$ (use $\sinh$ zeros to avoid critical lines) and to $\tanh,\coth$ using the representation via exponentials and the Cayley transform.

	\par\noindent\textbullet\quad \textbf{Cayley (disk $\leftrightarrow$ right half-plane).}\\[2pt]
	\[
	\boxed{\,w=\frac{1+z}{1-z}\,}\qquad\text{inverse:}\quad z=\frac{w-1}{w+1}.
	\]

	\par\noindent\textbullet\quad \textbf{Half-plane $\to$ half-plane (three-point normalization).}\\[2pt]
	\[
	\boxed{\,w=\frac{(z-a)(c-b)}{(z-b)(c-a)}\,}.
	\]

	\par\noindent\textbullet\quad \textbf{Disk automorphisms.}\\[2pt]
	\[
	\boxed{\,\phi_{a,\theta}(z)=e^{i\theta}\frac{z-a}{1-\bar a z}\,},\qquad |a|<1.
	\]

	\par\noindent\textbullet\quad \textbf{Strip $|\Im z|<h/2$ $\to$ right half-plane.}\\[2pt]
	\[
	\boxed{\,w=\exp\!\left(\frac{\pi z}{h}\right)\,}.
	\]

	\par\noindent\textbullet\quad \textbf{Strip $|\Im z|<h/2$ $\to$ unit disk.}\\[2pt]
	\[
	\boxed{\,\zeta=\frac{e^{\pi z/h}-1}{\,e^{\pi z/h}+1\,}\,}.
	\]

	\par\noindent\textbullet\quad \textbf{Strip $\to$ strip (height scaling).}\\[2pt]
	\[
	\boxed{\,z\mapsto \frac{h_2}{h_1}\,z\,}.
	\]

	\par\noindent\textbullet\quad \textbf{Band $a<\Im z<b$ $\to$ centered strip.}\\[2pt]
	\[
	\boxed{\,z\mapsto \frac{\pi}{b-a}\!\left(z-i\frac{a+b}{2}\right)\,}.
	\]

	\par\noindent\textbullet\quad \textbf{Sector $\{0<\arg z<\alpha\}$ $\to$ upper half-plane.}\\[2pt]
	\[
	\boxed{\,w=z^{\pi/\alpha}\,}\ \ \text{(principal branch)}.
	\]

	\par\noindent\textbullet\quad \textbf{Wedge $\to$ disk.}\\[2pt]
	Compose item (8) with Cayley (item 1).

	\par\noindent\textbullet\quad \textbf{Upper half-plane $\to$ disk (prescribed triple).}\\[2pt]
	\[
	\boxed{\,\Phi(z)=\frac{(z-a)}{(z-\bar a)}\cdot \frac{(b-\bar a)}{(b-a)}\,}.
	\]

	\par\noindent\textbullet\quad \textbf{Annulus $r<|z|<1$ $\leftrightarrow$ strip.}\\[2pt]
	\[
	\boxed{\,w=\log z\,}\quad\text{maps to }\ \log r<\Re w<0.
	\]

	\par\noindent\textbullet\quad \textbf{Annulus $\to$ disk.}\\[2pt]
	Use $w=\log z$ then item (5).

	\par\noindent\textbullet\quad \textbf{Half-plane minus disk $\to$ annulus.}\\[2pt]
	\[
	\boxed{\,\zeta=\frac{z-\alpha}{z+\alpha}\,},\qquad \alpha^{2}=a^{2}-b^{2}.
	\]

	\par\noindent\textbullet\quad \textbf{Disk with off-center hole $\to$ annulus.}\\[2pt]
	Center via $\phi_a$ (item 3), then items (11)â€“(12).

	\par\noindent\textbullet\quad \textbf{Punctured plane $\leftrightarrow$ cylinder.}\\[2pt]
	\[
	\boxed{\,w=\log z\,}\quad(\text{period }2\pi i).
	\]

	\par\noindent\textbullet\quad \textbf{Strip $\to$ punctured plane.}\\[2pt]
	\[
	\boxed{\,z\mapsto e^{z}\,}.
	\]

	\par\noindent\textbullet\quad \textbf{Ray-slit plane $\mathbb C\setminus[0,\infty)$ $\to$ half-plane.}\\[2pt]
	\[
	\boxed{\,w=\sqrt{z}\,}\ \ \text{(choose branch)}.
	\]

	\par\noindent\textbullet\quad \textbf{Segment-slit plane $\mathbb C\setminus[a,b]$ $\to$ half-plane.}\\[2pt]
	\[
	\boxed{\,w=\sqrt{\frac{z-a}{\,z-b\,}}\,}.
	\]

	\par\noindent\textbullet\quad \textbf{Exterior of $[-1,1]$ $\leftrightarrow$ exterior unit circle (Joukowski).}\\[2pt]
	\[
	\boxed{\,w=z+\frac{1}{z}\,},\qquad
	z=\frac{w\pm\sqrt{w^{2}-4}}{2}.
	\]

	\par\noindent\textbullet\quad \textbf{Exterior of ellipse $\leftrightarrow$ exterior unit circle.}\\[2pt]
	\[
	\boxed{\,w=\tfrac12\!\left(c z+\frac{1}{c z}\right)\,}\quad(\text{$c$ from axes}).
	\]

	\par\noindent\textbullet\quad \textbf{Right half-plane $\to$ vertical strip.}\\[2pt]
	\[
	\boxed{\,z\mapsto \frac{1}{\pi}\log\frac{z-1}{\,z+1\,}\,}.
	\]

	\par\noindent\textbullet\quad \textbf{Upper half-plane $\to$ rectangle (SC/elliptic).}\\[2pt]
	\[
	\boxed{\,\zeta=\int^z \frac{dt}{\sqrt{(t-a)(t-b)(t-c)(t-d)}}\,}.
	\]

	\par\noindent\textbullet\quad \textbf{Rectangle $\to$ disk (Jacobi sn).}\\[2pt]
	\[
	\boxed{\,\zeta=\operatorname{sn}\!\left(\frac{K(k)}{L}\,z;\,k\right)\,}.
	\]

	\par\noindent\textbullet\quad \textbf{Half-disk $\leftrightarrow$ half-plane.}\\[2pt]
	Restriction of Cayley (item 1) and inverse.

	\par\noindent\textbullet\quad \textbf{Lens (intersection of two disks) $\to$ disk.}\\[2pt]
	MĂ¶bius normalizes the circles; then a power map; then Cayley.

	\par\noindent\textbullet\quad \textbf{Half-strip $\{x>0,\ 0<\Im z<h\}$ $\to$ half-disk.}\\[2pt]
	\[
	\boxed{\,\exp(\pi z/h)\,}\ \ \text{then power, then Cayley}.
	\]

	\par\noindent\textbullet\quad \textbf{Polygon $\to$ half-plane (Schwarz--Christoffel).}\\[2pt]
	\[
	\boxed{\,\Phi'(z)=C\prod_k (z-z_k)^{\alpha_k-1}\,},\qquad \sum\alpha_k=2.
	\]

	\par\noindent\textbullet\quad \textbf{Upper half-plane $\to$ slit half-plane.}\\[2pt]
	\[
	\boxed{\,w=z+\frac{1}{z}\,}\ \ \text{then a real MĂ¶bius adjustment}.
	\]

	\par\noindent\textbullet\quad \textbf{Disk $\to$ disk with boundary arc removed.}\\[2pt]
	Automorphism to put endpoints at $\pm1$, then boundary power $z^\lambda$.

	\par\noindent\textbullet\quad \textbf{Finite Blaschke product (disk $\to$ disk, degree $n$).}\\[2pt]
	\[
	\boxed{\,B(z)=e^{i\theta}\prod_{k=1}^n \frac{z-a_k}{\,1-\bar a_k z\,}\,}.
	\]

 \mbox{}\\[2pt]
\[
w=\frac{1+z}{\,1-z\,}
\quad\text{maps}\quad
\mathbb D=\{|z|<1\}\ \text{onto}\ \{\,\Re w>0\,\},
\qquad
z=\frac{w-1}{\,w+1\,}
\]
is the inverse.

\medskip

 \mbox{}\\[2pt]
Compute
\[
\Re\!\left(\frac{1+z}{\,1-z\,}\right)
=\frac{\,1-|z|^{2}\,}{\,|1-z|^{2}\,}.
\]
Thus $\Re w>0$ for $|z|<1$, and $\Re w=0$ for $|z|=1$ (except $z=1$, which maps to $w=\infty$).
Therefore
\[
|z|<1\ \Longleftrightarrow\ \Re w>0,
\qquad
|z|=1\ \Longleftrightarrow\ \Re w=0 .
\]

\medskip

 \mbox{}\\[2pt]
$z=0\mapsto w=1$,
\quad
$z\to1^{-}\mapsto w\to+\infty$,
\quad
and $\partial\mathbb D\setminus\{1\}$ maps to the line $\Re w=0$.\\[2pt]
Circles/lines orthogonal to $\partial\mathbb D$ map to \emph{vertical} lines in the $w$â€“plane.

\bigskip\hrule\bigskip

 \mbox{}\\[2pt]
Let $L$ be a line or circle, and choose three distinct points $a,b,c\in L$. Define
\[
\Phi(z)=\frac{(z-a)(c-b)}{(z-b)(c-a)}.
\]
Then $\Phi(L)\subset\mathbb R\cup\{\infty\}$, with
\[
\Phi(a)=0,\qquad \Phi(b)=\infty,\qquad \Phi(c)=1,
\]
and the two sides of $L$ map to the half-planes $\Im\Phi(z)\gtrless 0$.

\medskip

 \mbox{}\\[2pt]
Given half-planes $H_1,H_2$ with boundary arcs $L_1,L_2$,
pick ordered boundary triples $a,b,c\in L_1$ and $A,B,C\in L_2$ (same cyclic order).
Then
\[
T(z)=\frac{(z-a)(c-b)}{(z-b)(c-a)}\cdot\frac{(C-A)}{(C-B)}
\]
is a MĂ¶bius map sending $L_1\!\to L_2$ with
\[
a\mapsto A,\qquad b\mapsto B,\qquad c\mapsto C,
\]
and taking the chosen side of $H_1$ onto the chosen side of $H_2$.

\medskip

 \mbox{}\\[2pt]
To send $L$ to $\mathbb R$, use $\Phi$ above; then pre/postcompose with an \emph{affine real} map
\[
\xi\longmapsto \alpha\,\xi+\beta,\qquad \alpha>0,
\]
to obtain any target half-plane, e.g.\ $\Re w>0$ or $\Im w>0$.
```

## CP-IV-0135


- chapter line: 6899
- atlas source solution flag: `unknown`
- linked source-solution candidates: `none`
- embedded solution marker in problem body: `NO`

```tex
Temperature in a right halfâ€“plane with a removed disk

The domain $D$ consists of the right-hand half plane $x>0$ with the circle $|z-a|=b$, $0<b<a$, and its interior removed.
	Find the temperature $u(x,y)$ in steady heat flow if $u=0$ on the $y$ axis, $u=1$ on $|z-a|=b$, and $u\to0$ at infinity.

	\medskip
	\noindent\textit{Hint:} Show that the mapping $\displaystyle \zeta=\frac{z-\alpha}{z+\alpha}$, with $\alpha$ real and positive,
	takes $D$ onto an annular region with the imaginary axis mapping to $|\zeta|=1$ and show that, if $\alpha^{2}=a^{2}-b^{2}$, then the image of $D$ is a concentric circular annulus.

	\bigskip\hrule\bigskip

	Consider the real-parameter MĂ¶bius map
	\[
	\zeta=\zeta(z)=\frac{z-\alpha}{z+\alpha}, \qquad \alpha>0.
	\]

	For $z=iy$ we have
	\[
	\left|\frac{iy-\alpha}{iy+\alpha}\right|=1 \quad\text{(numerator and denominator are conjugates),}
	\]
	so the $y$â€“axis maps to the unit circle $|\zeta|=1$.

	\paragraph{Image of the circle $\boldsymbol{|z-a|=b}$.}
	Write $z=a+be^{i\theta}$ and compute
	\[
	|\zeta|^{2}
	=\frac{|a-\alpha+be^{i\theta}|^{2}}{|a+\alpha+be^{i\theta}|^{2}}
	=\frac{A+B\cos\theta}{C+D\cos\theta},
	\]
	where
	\[
	A=(a-\alpha)^{2}+b^{2}, \qquad B=2b(a-\alpha), \qquad
	C=(a+\alpha)^{2}+b^{2}, \qquad D=2b(a+\alpha).
	\]
	For $|\zeta|$ to be constant on the circle (i.e. the image is a circle \emph{centered at the origin}),
	the $\cos\theta$â€“dependence must drop out:
	\[
	\frac{A+B\cos\theta}{\,C+D\cos\theta\,}\equiv\frac{A}{C}
	\quad\Longleftrightarrow\quad AD=BC.
	\]
	We now verify that
	\[
	AD-BC
	=2b\Big[(a+\alpha)((a-\alpha)^{2}+b^{2})-(a-\alpha)((a+\alpha)^{2}+b^{2})\Big]
	=4b\alpha\,(\alpha^{2}+b^{2}-a^{2}).
	\]
	Thus $AD=BC$ is equivalent to
	\[
	\boxed{\ \alpha^{2}=a^{2}-b^{2}\ }.
	\]
	With this choice (note $a>b>0\Rightarrow \alpha>0$), the ratio becomes \emph{constant}:
	\[
	|\zeta|^{2}=\frac{A}{C}
	=\frac{(a-\alpha)^{2}+b^{2}}{(a+\alpha)^{2}+b^{2}}
	=\frac{2a(a-\alpha)}{2a(a+\alpha)}
	=\frac{a-\alpha}{a+\alpha}.
	\]
	Hence the circle $|z-a|=b$ maps to the circle $|\zeta|=\rho$ with
	\[
	\boxed{\ \rho=\sqrt{\frac{a-\alpha}{a+\alpha}}\in(0,1). \ }
	\]

	Therefore, for $\alpha=\sqrt{a^{2}-b^{2}}$, the map $z\mapsto\zeta$ sends the domain $D$
	(right halfâ€“plane with the closed disk $\{|z-a|\le b\}$ removed) onto the concentric circular \emph{annulus}
	\[
	\mathcal A=\{\ \rho<|\zeta|<1\ \}.
	\]
	The boundary pieces correspond as follows:
	\[
	\{x=0\}\ \longmapsto\ |\zeta|=1,
	\qquad
	\{|z-a|=b\}\ \longmapsto\ |\zeta|=\rho.
	\]

	\bigskip\hrule\bigskip

	Let $U(\zeta)$ denote the temperature in the $\zeta$â€“plane. Harmonicity is preserved by conformal maps, so
	$U$ is harmonic on $\mathcal A$ and the boundary data become
	\[
	U=0 \ \ \text{on}\ \ |\zeta|=1,
	\qquad
	U=1 \ \ \text{on}\ \ |\zeta|=\rho.
	\]
	By rotational symmetry, $U$ depends only on $r=|\zeta|$. The general radial harmonic function on an annulus is
	$A\log r + B$. Imposing the boundary values gives
	\[
	U(r)=\frac{\log(1/r)}{\log(1/\rho)}
	=\frac{-\log r}{-\log \rho}
	=\frac{\log r}{\log \rho}
	\quad\text{for}\quad \rho<r<1.
	\]
	(Any of the three displayed forms is correct; we will use the first one momentarily.)

	\bigskip\hrule\bigskip

	The physical temperature is $u(z)=U(\zeta(z))$ with $r=|\zeta(z)|=\left|\frac{z-\alpha}{z+\alpha}\right|$.
	Hence
	\[
	u(z)
	=U\!\left(\left|\frac{z-\alpha}{z+\alpha}\right|\right)
	=\frac{\displaystyle \log\!\left(\frac{1}{\left|\frac{z-\alpha}{z+\alpha}\right|}\right)}
	{\displaystyle \log\!\left(\frac{1}{\rho}\right)}
	=\frac{\displaystyle \log\left|\frac{z+\alpha}{z-\alpha}\right|}
	{\displaystyle \log\!\left(\frac{1}{\rho}\right)}.
	\]
	Since $\displaystyle \rho=\sqrt{\frac{a-\alpha}{a+\alpha}}$ we have
	\[
	\log\!\left(\frac{1}{\rho}\right)
	=\frac{1}{2}\,\log\!\left(\frac{a+\alpha}{a-\alpha}\right).
	\]
	Therefore a convenient explicit form is
	\[
	\boxed{\quad
		u(z)
		=\frac{2\,\log\!\left|\dfrac{z+\alpha}{z-\alpha}\right|}
		{\log\!\left(\dfrac{a+\alpha}{a-\alpha}\right)},
		\qquad
		\alpha=\sqrt{a^{2}-b^{2}}.
		\quad}
	\]

	\bigskip

		\par\noindent\textbullet\quad \textbf{On the $y$--axis $x=0$:} for $z=iy$ we have $\left|\dfrac{z-\alpha}{z+\alpha}\right|=1$,
		so the numerator $\log\left|\dfrac{z+\alpha}{z-\alpha}\right|=0$ and hence $u=0$.
		\par\noindent\textbullet\quad \textbf{On the circle $|z-a|=b$:} by construction $|\zeta|=\rho$, i.e.
		$\left|\dfrac{z-\alpha}{z+\alpha}\right|=\rho$, so
		$\log\left|\dfrac{z+\alpha}{z-\alpha}\right|=\log\!\left(\dfrac{1}{\rho}\right)$
		and the fraction evaluates to $u=1$.
		\par\noindent\textbullet\quad \textbf{At infinity:} as $|z|\to\infty$, $\left|\dfrac{z+\alpha}{z-\alpha}\right|\to 1$,
		so the numerator $\to 0$ and $u(z)\to 0$.

	\bigskip\hrule\bigskip

	With $\alpha=\sqrt{a^{2}-b^{2}}$ and $\displaystyle \rho=\sqrt{\frac{a-\alpha}{a+\alpha}}$,
	the MĂ¶bius map $\displaystyle \zeta=\frac{z-\alpha}{z+\alpha}$ carries
	$D$ onto the annulus $\{\rho<|\zeta|<1\}$.
	The unique harmonic function with $U=1$ on $|\zeta|=\rho$ and $U=0$ on $|\zeta|=1$
	is $U(r)=\log(1/r)/\log(1/\rho)$, and hence
	\[
	u(z)=\frac{2\,\log\!\left|\dfrac{z+\alpha}{z-\alpha}\right|}
	{\log\!\left(\dfrac{a+\alpha}{a-\alpha}\right)}.
	\]
	This $u$ satisfies all the prescribed boundary conditions and $u(z)\to 0$ as $|z|\to\infty$.

\textbf{Background:} entire, odd; period $2\pi i$. \quad
\textbf{Zeros:} $z=i\pi k$; \textbf{poles:} none.\\
\textbf{Decomposition: } $w=u+iv=\sinh x\cos y + i\,\cosh x\sin y$.\\
\textbf{Vertical lines } $x=\text{const}$: $\left(\frac{u}{\sinh x}\right)^2+\left(\frac{v}{\cosh x}\right)^2=1$ (ellipses, foci $\pm i$).\\
\textbf{Horizontal lines } $y=\text{const}$: $\left(\frac{u}{\cos y}\right)^2-\left(\frac{v}{\sin y}\right)^2=-1$ (hyperbolas, foci $\pm i$).\\
\textbf{Strip mapping:}
\[
\boxed{\,\sinh:\ \{|\Im z|<\tfrac{\pi}{2}\}\ \xrightarrow{\ 1\text{--}1\ }\ \mathbb C\setminus i\big((-\infty,-1]\cup[1,\infty)\big)\,}
\]
Boundaries $y=\pm\frac{\pi}{2}$ map to imaginary rays $\pm i[1,\infty)$.

\bigskip\hrule\bigskip

\textbf{Background:} entire, even; period $2\pi i$. \quad
\textbf{Zeros:} $z=i\pi(k+\frac12)$; \textbf{poles:} none.\\
\textbf{Decomposition: } $w=u+iv=\cosh x\cos y + i\,\sinh x\sin y$.\\
\textbf{Vertical lines } $x=\text{const}$: $\left(\frac{u}{\cosh x}\right)^2+\left(\frac{v}{\sinh x}\right)^2=1$ (ellipses, foci $\pm1$).\\
\textbf{Horizontal lines } $y=\text{const}$: $\left(\frac{u}{\cos y}\right)^2-\left(\frac{v}{\sin y}\right)^2=1$ (hyperbolas, foci $\pm1$).\\
\textbf{Strip mapping:}
\[
\boxed{\,\cosh:\ \{|\Im z|<\pi\}\ \xrightarrow{\ 2\text{--}1\ }\ \mathbb C\setminus\big((-\infty,-1]\cup[1,\infty)\big)\,}
\]
On the half-strip $0<|\Im z|<\pi$, the map is 1--1 onto the slit plane.

\bigskip\hrule\bigskip

\textbf{Background:} meromorphic, odd; period $i\pi$. \quad
\textbf{Zeros:} $z=i\pi k$; \textbf{poles:} $z=i\pi(k+\tfrac12)$.\\
\textbf{Strip $\to$ disk:}
\[
\boxed{\,\tanh:\ \{|\Im z|<\tfrac{\pi}{2}\}\ \xrightarrow{\ 1\text{--}1\ }\ \mathbb D\,}
\]
Real line maps to $(-1,1)$; as $|\Im z|\to\pi/2$, $|\tanh z|\to1$.

\bigskip\hrule\bigskip

\textbf{Background:} meromorphic, odd; period $i\pi$. \quad
\textbf{Zeros:} $z=i\pi(k+\tfrac12)$; \textbf{poles:} $z=i\pi k$.\\
\textbf{Strip $\to$ exterior disk:}
\[
\boxed{\,\coth:\ \{|\Im z|<\tfrac{\pi}{2}\}\setminus\{0\}\ \xrightarrow{\ 1\text{--}1\ }\ \{\,|w|>1\,\}\,}
\]
Real line maps to $(-\infty,-1)\cup(1,\infty)$; $|\Im z|\to\pi/2$ gives $|w|\to1^+$.

	\par\noindent\textbullet\quad \textbf{Cayley (disk $\leftrightarrow$ right half-plane).}\\[2pt]
	\[
	\boxed{\,w=\frac{1+z}{1-z}\,}\qquad\text{inverse:}\quad z=\frac{w-1}{w+1}.
	\]

	\par\noindent\textbullet\quad \textbf{Half-plane $\to$ half-plane (three-point normalization).}\\[2pt]
	\[
	\boxed{\,w=\frac{(z-a)(c-b)}{(z-b)(c-a)}\,}.
	\]

	\par\noindent\textbullet\quad \textbf{Disk automorphisms.}\\[2pt]
	\[
	\boxed{\,\phi_{a,\theta}(z)=e^{i\theta}\frac{z-a}{1-\bar a z}\,},\qquad |a|<1.
	\]

	\par\noindent\textbullet\quad \textbf{Strip $|\Im z|<h/2$ $\to$ right half-plane.}\\[2pt]
	\[
	\boxed{\,w=\exp\!\left(\frac{\pi z}{h}\right)\,}.
	\]

	\par\noindent\textbullet\quad \textbf{Strip $|\Im z|<h/2$ $\to$ unit disk.}\\[2pt]
	\[
	\boxed{\,\zeta=\frac{e^{\pi z/h}-1}{\,e^{\pi z/h}+1\,}\,}.
	\]

	\par\noindent\textbullet\quad \textbf{Strip $\to$ strip (height scaling).}\\[2pt]
	\[
	\boxed{\,z\mapsto \frac{h_2}{h_1}\,z\,}.
	\]

	\par\noindent\textbullet\quad \textbf{Band $a<\Im z<b$ $\to$ centered strip.}\\[2pt]
	\[
	\boxed{\,z\mapsto \frac{\pi}{b-a}\!\left(z-i\frac{a+b}{2}\right)\,}.
	\]

	\par\noindent\textbullet\quad \textbf{Sector $\{0<\arg z<\alpha\}$ $\to$ upper half-plane.}\\[2pt]
	\[
	\boxed{\,w=z^{\pi/\alpha}\,}\ \ \text{(principal branch)}.
	\]

	\par\noindent\textbullet\quad \textbf{Wedge $\to$ disk.}\\[2pt]
	Compose item (8) with Cayley (item 1).

	\par\noindent\textbullet\quad \textbf{Upper half-plane $\to$ disk (prescribed triple).}\\[2pt]
	\[
	\boxed{\,\Phi(z)=\frac{(z-a)}{(z-\bar a)}\cdot \frac{(b-\bar a)}{(b-a)}\,}.
	\]

	\par\noindent\textbullet\quad \textbf{Annulus $r<|z|<1$ $\leftrightarrow$ strip.}\\[2pt]
	\[
	\boxed{\,w=\log z\,}\quad\text{maps to }\ \log r<\Re w<0.
	\]

	\par\noindent\textbullet\quad \textbf{Annulus $\to$ disk.}\\[2pt]
	Use $w=\log z$ then item (5).

	\par\noindent\textbullet\quad \textbf{Half-plane minus disk $\to$ annulus.}\\[2pt]
	\[
	\boxed{\,\zeta=\frac{z-\alpha}{z+\alpha}\,},\qquad \alpha^{2}=a^{2}-b^{2}.
	\]

	\par\noindent\textbullet\quad \textbf{Disk with off-center hole $\to$ annulus.}\\[2pt]
	Center via $\phi_a$ (item 3), then items (11)â€“(12).

	\par\noindent\textbullet\quad \textbf{Punctured plane $\leftrightarrow$ cylinder.}\\[2pt]
	\[
	\boxed{\,w=\log z\,}\quad(\text{period }2\pi i).
	\]

	\par\noindent\textbullet\quad \textbf{Strip $\to$ punctured plane.}\\[2pt]
	\[
	\boxed{\,z\mapsto e^{z}\,}.
	\]

	\par\noindent\textbullet\quad \textbf{Ray-slit plane $\mathbb C\setminus[0,\infty)$ $\to$ half-plane.}\\[2pt]
	\[
	\boxed{\,w=\sqrt{z}\,}\ \ \text{(choose branch)}.
	\]

	\par\noindent\textbullet\quad \textbf{Segment-slit plane $\mathbb C\setminus[a,b]$ $\to$ half-plane.}\\[2pt]
	\[
	\boxed{\,w=\sqrt{\frac{z-a}{\,z-b\,}}\,}.
	\]

	\par\noindent\textbullet\quad \textbf{Exterior of $[-1,1]$ $\leftrightarrow$ exterior unit circle (Joukowski).}\\[2pt]
	\[
	\boxed{\,w=z+\frac{1}{z}\,},\qquad
	z=\frac{w\pm\sqrt{w^{2}-4}}{2}.
	\]

	\par\noindent\textbullet\quad \textbf{Exterior of ellipse $\leftrightarrow$ exterior unit circle.}\\[2pt]
	\[
	\boxed{\,w=\tfrac12\!\left(c z+\frac{1}{c z}\right)\,}\quad(\text{$c$ from axes}).
	\]

	\par\noindent\textbullet\quad \textbf{Right half-plane $\to$ vertical strip.}\\[2pt]
	\[
	\boxed{\,z\mapsto \frac{1}{\pi}\log\frac{z-1}{\,z+1\,}\,}.
	\]

	\par\noindent\textbullet\quad \textbf{Upper half-plane $\to$ rectangle (SC/elliptic).}\\[2pt]
	\[
	\boxed{\,\zeta=\int^z \frac{dt}{\sqrt{(t-a)(t-b)(t-c)(t-d)}}\,}.
	\]

	\par\noindent\textbullet\quad \textbf{Rectangle $\to$ disk (Jacobi sn).}\\[2pt]
	\[
	\boxed{\,\zeta=\operatorname{sn}\!\left(\frac{K(k)}{L}\,z;\,k\right)\,}.
	\]

	\par\noindent\textbullet\quad \textbf{Half-disk $\leftrightarrow$ half-plane.}\\[2pt]
	Restriction of Cayley (item 1) and inverse.

	\par\noindent\textbullet\quad \textbf{Lens (intersection of two disks) $\to$ disk.}\\[2pt]
	MĂ¶bius normalizes the circles; then a power map; then Cayley.

	\par\noindent\textbullet\quad \textbf{Half-strip $\{x>0,\ 0<\Im z<h\}$ $\to$ half-disk.}\\[2pt]
	\[
	\boxed{\,\exp(\pi z/h)\,}\ \ \text{then power, then Cayley}.
	\]

	\par\noindent\textbullet\quad \textbf{Polygon $\to$ half-plane (Schwarz--Christoffel).}\\[2pt]
	\[
	\boxed{\,\Phi'(z)=C\prod_k (z-z_k)^{\alpha_k-1}\,},\qquad \sum\alpha_k=2.
	\]

	\par\noindent\textbullet\quad \textbf{Upper half-plane $\to$ slit half-plane.}\\[2pt]
	\[
	\boxed{\,w=z+\frac{1}{z}\,}\ \ \text{then a real MĂ¶bius adjustment}.
	\]

	\par\noindent\textbullet\quad \textbf{Disk $\to$ disk with boundary arc removed.}\\[2pt]
	Automorphism to put endpoints at $\pm1$, then boundary power $z^\lambda$.

	\par\noindent\textbullet\quad \textbf{Finite Blaschke product (disk $\to$ disk, degree $n$).}\\[2pt]
	\[
	\boxed{\,B(z)=e^{i\theta}\prod_{k=1}^n \frac{z-a_k}{\,1-\bar a_k z\,}\,}.
	\]

 \mbox{}\\[2pt]
\[
w=\frac{1+z}{\,1-z\,}
\quad\text{maps}\quad
\mathbb D=\{|z|<1\}\ \text{onto}\ \{\,\Re w>0\,\},
\qquad
z=\frac{w-1}{\,w+1\,}
\]
is the inverse.

\medskip

 \mbox{}\\[2pt]
Compute
\[
\Re\!\left(\frac{1+z}{\,1-z\,}\right)
=\frac{\,1-|z|^{2}\,}{\,|1-z|^{2}\,}.
\]
Thus $\Re w>0$ for $|z|<1$, and $\Re w=0$ for $|z|=1$ (except $z=1$, which maps to $w=\infty$).
Therefore
\[
|z|<1\ \Longleftrightarrow\ \Re w>0,
\qquad
|z|=1\ \Longleftrightarrow\ \Re w=0 .
\]

\medskip

 \mbox{}\\[2pt]
$z=0\mapsto w=1$,
\quad
$z\to1^{-}\mapsto w\to+\infty$,
\quad
and $\partial\mathbb D\setminus\{1\}$ maps to the line $\Re w=0$.\\[2pt]
Circles/lines orthogonal to $\partial\mathbb D$ map to \emph{vertical} lines in the $w$â€“plane.

\bigskip\hrule\bigskip

 \mbox{}\\[2pt]
Let $L$ be a line or circle, and choose three distinct points $a,b,c\in L$. Define
\[
\Phi(z)=\frac{(z-a)(c-b)}{(z-b)(c-a)}.
\]
Then $\Phi(L)\subset\mathbb R\cup\{\infty\}$, with
\[
\Phi(a)=0,\qquad \Phi(b)=\infty,\qquad \Phi(c)=1,
\]
and the two sides of $L$ map to the half-planes $\Im\Phi(z)\gtrless 0$.

\medskip

 \mbox{}\\[2pt]
Given half-planes $H_1,H_2$ with boundary arcs $L_1,L_2$,
pick ordered boundary triples $a,b,c\in L_1$ and $A,B,C\in L_2$ (same cyclic order).
Then
\[
T(z)=\frac{(z-a)(c-b)}{(z-b)(c-a)}\cdot\frac{(C-A)}{(C-B)}
\]
is a MĂ¶bius map sending $L_1\!\to L_2$ with
\[
a\mapsto A,\qquad b\mapsto B,\qquad c\mapsto C,
\]
and taking the chosen side of $H_1$ onto the chosen side of $H_2$.

\medskip

 \mbox{}\\[2pt]
To send $L$ to $\mathbb R$, use $\Phi$ above; then pre/postcompose with an \emph{affine real} map
\[
\xi\longmapsto \alpha\,\xi+\beta,\qquad \alpha>0,
\]
to obtain any target half-plane, e.g.\ $\Re w>0$ or $\Im w>0$.
```

## CP-IV-0138


- chapter line: 7305
- atlas source solution flag: `unknown`
- linked source-solution candidates: `none`
- embedded solution marker in problem body: `NO`

```tex
Let $U=\mathbb{C}$ and $f(z)=e^{z}$.

\emph{Existence of $\log f$ on $U$.}
Since $f$ is entire and never zero, $f'/f\equiv 1$ is entire.
Because $U$ is simply connected, $G(z):=z$ is a primitive of $f'/f$.
Define $F(z):=G(z)=z$. Then $e^{F(z)}=e^{z}=f(z)$, so $F$ is a holomorphic branch of $\log f$ on $U$.
Uniqueness holds up to $2\pi i\mathbb{Z}$: if $F_1,F_2$ satisfy $e^{F_j}=f$, then $e^{F_1-F_2}\equiv 1$, hence $F_1-F_2\in 2\pi i\mathbb{Z}$ is a constant.

\medskip

\emph{Failure of a branch of $\log$ on $f(U)$.}
We have $f(U)=\mathbb{C}^\times$.
If there were a holomorphic branch $L$ of the scalar logarithm on $\mathbb{C}^\times$, then $L'(w)=1/w$ and, for every closed loop $\Gamma\subset\mathbb{C}^\times$,
\[
\oint_{\Gamma}\frac{dw}{w}=\oint_{\Gamma}L'(w)\,dw=0.
\]
Taking $\Gamma=\{\,|w|=1\,\}$ yields $\displaystyle\oint_{|w|=1}\frac{dw}{w}=2\pi i\neq 0$, a contradiction.
Therefore, no holomorphic branch of the scalar $\log$ exists on $\mathbb{C}^\times$.

\medskip

\emph{Monodromy/winding viewpoint.}
For any closed loop $\Gamma$ in a domain that avoids $0$,
\[
\oint_{\Gamma}\frac{dw}{w}=2\pi i\cdot \mathrm{Wind}(\Gamma,0).
\]
Thus a global holomorphic branch of $\log$ on a domain $V\subset\mathbb{C}^\times$ exists iff every loop in $V$ has winding number $0$ about $0$ (equivalently, $V$ is simply connected).
Here $V=\mathbb{C}^\times$ has nontrivial loops around $0$, so monodromy obstructs single-valuedness.

\medskip

\emph{Analytic continuation around a circle (explicit jump).}
Start with a local branch of $\log$ near $w=1$ and analytically continue once along the unit circle $w=e^{it}$, $t\in[0,2\pi]$.
The continuation returns to the starting point but accumulates the increment
\[
\int_{0}^{2\pi}\frac{d}{dt}\big(\log(e^{it})\big)\,dt
\;=\;\int_{0}^{2\pi} i\,dt
\;=\;2\pi i,
\]
so the value jumps by $2\pi i$. This nontrivial monodromy forbids a single-valued holomorphic logarithm on $\mathbb{C}^\times$.

\medskip

\emph{Bounded variant (annulus image).}
Let $U=\{z:|z|<2\}$ and $f(z)=e^{z}$. Then $F(z)=z$ gives a branch of $\log f$ on $U$, but
\[
f(U)=\{e^{x+iy}\,:\,|x|<2,\ |y|<2\}
=\{w\in\mathbb{C}^\times: e^{-2}<|w|<e^{2}\},
\]
an annulus encircling $0$. Any circle $\{|w|=r\}$ with $e^{-2}<r<e^{2}$ satisfies $\displaystyle\oint\frac{dw}{w}=2\pi i\neq 0$, so no holomorphic branch of the scalar $\log$ exists on $f(U)$.

\medskip

\emph{Local vs.\ global behavior.}
On any simply connected subdomain $V\subset\mathbb{C}^\times$ that does not wrap around $0$ (e.g.\ a slit plane or a sector of angle $<2\pi$), one \emph{can} choose a holomorphic branch of the scalar $\log$.
The obstruction is purely topological: encircling $0$ forces a $2\pi i$ jump.

\medskip

\emph{Connection with $\arg$ and $f'/f$.}
For $w\neq 0$, $\log w=\log|w|+i\,\arg w$; the impossibility of a global continuous $\arg$ on $\mathbb{C}^\times$ is the same obstruction.
Equivalently, if $L$ existed on $V$, then $(\log\circ f)'=(f'/f)$ would be the derivative of a \emph{global} holomorphic function on $V$.
On simply connected $U$ this always holds for $f'/f$ (hence $\log f$ exists on $U$); on $f(U)$ it fails exactly when some loop winds around $0$.

\medskip

\emph{Takeaway.}
A holomorphic nonvanishing $f$ on a simply connected $U$ always has a holomorphic logarithm $F$ with $e^{F}=f$ (unique up to $2\pi i\mathbb{Z}$).
But a holomorphic scalar logarithm on $f(U)$ may not exist if $f(U)$ winds around $0$ (as with $f=\exp$ giving $\mathbb{C}^\times$ or an annulus).

\par\noindent\textbullet\quad $f$ is entire and never zero, so $f'/f \equiv 1$ is entire.
\par\noindent\textbullet\quad On the simply connected set $U=\mathbb{C}$, a primitive of $f'/f$ is $G(z)=z$.
\par\noindent\textbullet\quad Set $F(z):=G(z)=z$. Then $e^{F(z)}=e^{z}=f(z)$.
Thus $F$ is a (holomorphic) branch of $\log f$ on $U$.

\bigskip

\subsection*{2) Why a holomorphic $\log$ cannot exist on $f(U)=\mathbb{C}^{\times}$}

\par\noindent\textbullet\quad $f(U)=\mathbb{C}\setminus\{0\}$ is not simply connected (its fundamental group is $\mathbb{Z}$);
any loop going once around $0$ has nonzero winding number.
\par\noindent\textbullet\quad If a holomorphic branch of the scalar logarithm $\Log$ existed on $\mathbb{C}^{\times}$, then
$(\Log)'(w)=1/w$ and hence, for every closed loop $\Gamma\subset\mathbb{C}^{\times}$,
\[
\oint_{\Gamma}\frac{dw}{w}
\;=\;
\oint_{\Gamma}(\Log)'(w)\,dw
\;=\;0.
\]
But for the unit circle $\{|w|=1\}$,
\[
\oint_{|w|=1}\frac{dw}{w} \;=\; 2\pi i \;\neq\; 0.
\]
Contradiction. Therefore no holomorphic branch of $\log$ exists on $\mathbb{C}^{\times}$.

\bigskip
```

## CP-IV-0001


- chapter line: 7409
- atlas source solution flag: `unknown`
- linked source-solution candidates: `none`
- embedded solution marker in problem body: `NO`

```tex
$f_n(x)=x^n$ on $[0,1]$ converges pointwise to $f=\mathbf{1}_{\{1\}}$ but not uniformly on $(0,1)$.
	\par\noindent\textbullet\quad Pointwise limit of uniformly continuous functions need not be uniformly continuous.
```

## CP-IV-0002


- chapter line: 7415
- atlas source solution flag: `unknown`
- linked source-solution candidates: `none`
- embedded solution marker in problem body: `NO`

```tex
â€” Disk of radius \(R\)

Parametrize the boundary circle \(C\):
\[
x=R\cos t,\qquad y=R\sin t,\qquad t\in[0,2\pi],
\]
so that
\[
dx=-R\sin t\,dt,\qquad dy=R\cos t\,dt.
\]
Then
\[
\frac12\bigl(x\,dy-y\,dx\bigr)
=
\frac12\Bigl(R\cos t\cdot R\cos t - R\sin t\cdot(-R\sin t)\Bigr)\,dt
=
\frac{R^{2}}{2}\,dt.
\]
Integrate:
\[
\operatorname{Area}
=
\int_{0}^{2\pi} \frac{R^{2}}{2}\,dt
=
\pi R^{2}.
\]
```

## CP-IV-0003


- chapter line: 7445
- atlas source solution flag: `unknown`
- linked source-solution candidates: `none`
- embedded solution marker in problem body: `NO`

```tex
(ellipse).

For the ellipse
\[
C:\quad \frac{x^{2}}{a^{2}} + \frac{y^{2}}{b^{2}} = 1,
\]
we have
\[
\oint_{C} \tfrac{1}{2}\,\bigl(x\,dy - y\,dx\bigr) \;=\; \pi a b.
\]
(You can parametrize $x=a\cos t$, $y=b\sin t$ and compute directly, or just invoke Green's theorem.)
```

## CP-IV-0006


- chapter line: 7460
- atlas source solution flag: `unknown`
- linked source-solution candidates: `none`
- embedded solution marker in problem body: `NO`

```tex
\par\noindent (ii)\quad Let $g$ be an entire function such that $|f(z)|\le |g(z)|$ for all $z\in\mathbb C$.
	Show that there exists $c\in\mathbb C$ such that $f(z)=c\,g(z)$ for all $z\in\mathbb C$.

\bigskip\hrule\bigskip
```

## CP-IV-0010


- chapter line: 7468
- atlas source solution flag: `unknown`
- linked source-solution candidates: `none`
- embedded solution marker in problem body: `NO`

```tex
Evaluate the following integrals.

\medskip
\emph{(a)} $\displaystyle \int_{0}^{\pi}\frac{d\theta}{4+\sin^{2}\theta}$.

Using $\displaystyle \int_{0}^{\pi}\frac{d\theta}{a+b\sin^{2}\theta}
=\frac{\pi}{\sqrt{a(a+b)}}$ for $a>0$, with $a=4$, $b=1$,
\[
\int_{0}^{\pi}\frac{d\theta}{4+\sin^{2}\theta}
=\frac{\pi}{\sqrt{4\cdot 5}}=\boxed{\frac{\pi}{2\sqrt5}}.
\]

\medskip
\emph{(b)} $\displaystyle \int_{0}^{\infty}\sin(x^{2})\,dx$.

By the Fresnel/Gaussian argument,
\[
\int_{0}^{\infty}\sin(x^{2})\,dx
=\int_{0}^{\infty}\cos(x^{2})\,dx
=\boxed{\frac{\sqrt{2\pi}}{4}=\frac{\sqrt{\pi}}{2\sqrt2}}.
\]

\medskip
\emph{(c)} $\displaystyle \int_{0}^{\infty}\frac{x^{2}}{(x^{2}+4)^{2}(x^{2}+9)}\,dx$.

Let $f(z)=\dfrac{z^{2}}{(z^{2}+4)^{2}(z^{2}+9)}$. The integrand is even; hence
\[
\int_{0}^{\infty}f(x)\,dx=\frac12\int_{-\infty}^{\infty}f(x)\,dx.
\]
Poles in the upper half-plane: $2i$ (double), $3i$ (simple).
\[
\operatorname{Res}(f;2i)=-\frac{13i}{200},\qquad \operatorname{Res}(f;3i)=\frac{3i}{50},\qquad
\operatorname{Res}(f;2i)+\operatorname{Res}(f;3i)=-\frac{i}{200}.
\]
Thus
\[
\int_{-\infty}^{\infty} f(x)\,dx
=2\pi i\!\left(-\frac{i}{200}\right)=\frac{\pi}{100},
\qquad
\int_{0}^{\infty} f(x)\,dx=\boxed{\frac{\pi}{200}}.
\]

\medskip
\emph{(d)} $\displaystyle \int_{0}^{\infty}\frac{\ln(x^{2}+1)}{x^{2}+1}\,dx$.

With $x=\tan t$ ($t\in[0,\pi/2)$), $x^{2}+1=\sec^{2}t$, $dx=\sec^{2}t\,dt$,
\[
\int_{0}^{\infty}\frac{\ln(x^{2}+1)}{x^{2}+1}\,dx
=\int_{0}^{\pi/2}\ln(\sec^{2}t)\,dt
=2\int_{0}^{\pi/2}\ln(\sec t)\,dt
=-2\int_{0}^{\pi/2}\ln(\cos t)\,dt
=\boxed{\pi\ln 2}.
\]
```

## CP-IV-0011


- chapter line: 7526
- atlas source solution flag: `unknown`
- linked source-solution candidates: `none`
- embedded solution marker in problem body: `NO`

```tex
\par\noindent\textbullet\quad If $f_n \Rightarrow f$ uniformly on $\mathbb{R}$, prove that $f$ is uniformly continuous.
```

## CP-IV-0013


- chapter line: 7531
- atlas source solution flag: `unknown`
- linked source-solution candidates: `none`
- embedded solution marker in problem body: `YES`

```tex
\par\noindent\textbullet\quad (\textbf{Jacobian, determinant, and orientation})
	Show the Jacobian determinant of $T$ equals
	\[
	\det DT=|A|^2-|B|^2.
	\]
	Conclude that $T$ is orientation-preserving iff $|A|>|B|$, reversing iff $|A|<|B|$, and singular iff $|A|=|B|$.

	\emph{Solution.} Using Ex.\ 3â€™s matrix and a short computation:
	$\det=\!(\alpha+\gamma)(\alpha-\gamma)-(-\beta+\delta)(\beta+\delta)
	=(\alpha^2+\beta^2)-(\gamma^2+\delta^2)=|A|^2-|B|^2$.
```

## CP-IV-0021


- chapter line: 7579
- atlas source solution flag: `unknown`
- linked source-solution candidates: `none`
- embedded solution marker in problem body: `NO`

```tex
\par\noindent (i)\quad Prove that $f$ is a polynomial of degree at most $k$ if and only if there exist real constants $M,R>0$ and an integer $k$ such that
	\[
	|f(z)|\le M\,|z|^{k}\qquad\text{for }|z|>R.
	\]
```

## CP-IV-0022


- chapter line: 7587
- atlas source solution flag: `unknown`
- linked source-solution candidates: `none`
- embedded solution marker in problem body: `NO`

```tex
(unit circle).

For $\Gamma=\{|\zeta|=1\}$ and $f(\zeta)=\zeta^{m}$ ($m\ge0$):
	\[
	F(z)=\begin{cases} z^{m}, & |z|<1,\\ 0, & |z|>1,\end{cases}
	\quad\Rightarrow\quad
	F^{+}(e^{it})-F^{-}(e^{it})=e^{im t}=f(e^{it}),
	\]
	and
	\(
	\operatorname{P.V.}\,\frac{1}{2\pi i}\int_{|\zeta|=1}\frac{\zeta^{m}}{\zeta-e^{it}}\,d\zeta
	=\tfrac12 e^{imt}.
	\)

	The Plemelj formulas remain valid for \emph{Lipschitz} curves (e.g.\ piecewise $C^{1}$ with finite length) when boundary limits are taken \emph{nontangentially}.
	This is classical in singularâ€“integral theory (Calder\'onâ€“Zygmund): the Cauchy singular integral operator is bounded on $L^{p}(\Gamma)$ for $1<p<\infty$, and the nontangential boundary limits exist almost everywhere.

	\medskip

		\par\noindent\textbullet\quad For classical \emph{pointwise} limits at every boundary point, it suffices to assume $f\in C^{0,\alpha}(\Gamma)$ (H\"older) for some $\alpha\in(0,1]$.
		\par\noindent\textbullet\quad For \emph{almost-everywhere} (a.e.) limits and $L^{p}$ jump relations, it is enough to assume $f\in L^{p}(\Gamma)$ with $1<p<\infty$.
		\par\noindent\textbullet\quad The original hypothesis $f\in C^{1}(\Gamma)$ is more than enough; it guarantees the principal value is well defined and that the interior/exterior limits exist \emph{at every} $\zeta_{0}\in\Gamma$ (no exceptional set).
```

## CP-IV-0026


- chapter line: 7615
- atlas source solution flag: `unknown`
- linked source-solution candidates: `none`
- embedded solution marker in problem body: `NO`

```tex
\par\noindent\textbullet\quad $\{(x,y): y\ne 0\}$.
```

## CP-IV-0030


- chapter line: 7643
- atlas source solution flag: `unknown`
- linked source-solution candidates: `none`
- embedded solution marker in problem body: `NO`

```tex
\par\noindent\textbullet\quad $\{(x,0): 0\le x\le 1\}$.
```

## CP-IV-0032


- chapter line: 7648
- atlas source solution flag: `unknown`
- linked source-solution candidates: `none`
- embedded solution marker in problem body: `NO`

```tex
$f(x)=x^2$ on $\mathbb{R}$ is not uniformly continuous.
	\par\noindent\textbullet\quad Pointwise convergence $\nRightarrow$ uniform convergence.
```

## CP-IV-0033


- chapter line: 7654
- atlas source solution flag: `unknown`
- linked source-solution candidates: `none`
- embedded solution marker in problem body: `NO`

```tex
\par\noindent\textbullet\quad Show that the map $f \mapsto \displaystyle\Big(x\mapsto \int_a^x f(y)\,dy\Big)$ is a continuous map from $C^k([a,b])$ to $C^{k+1}([a,b])$.
```

