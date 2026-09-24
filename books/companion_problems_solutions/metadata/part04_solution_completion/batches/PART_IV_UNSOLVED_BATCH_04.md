# Part IV Unsolved Solution Authoring Batch 04

- problems in batch: 20
- IDs: CP-IV-0038, CP-IV-0040, CP-IV-0041, CP-IV-0042, CP-IV-0046, CP-IV-0050, CP-IV-0054, CP-IV-0055, CP-IV-0056, CP-IV-0058, CP-IV-0059, CP-IV-0063, CP-IV-0067, CP-IV-0068, CP-IV-0071, CP-IV-0075, CP-IV-0081, CP-IV-0083, CP-IV-0085, CP-IV-0087

Author canonical worked solutions for these problems. Do not alter the problem statements.

## CP-IV-0038


- chapter line: 7659
- atlas source solution flag: `unknown`
- linked source-solution candidates: `none`
- embedded solution marker in problem body: `NO`

```tex
\par\noindent\textbullet\quad Not necessarily. For example,
	\[
	f(z)=z^{2}+\sin(\pi z)
	\]
	is entire and satisfies $f(n)=n^{2}$ for all $n\in\mathbb Z$, yet $f\not\equiv z^{2}$.

	\medskip
```

## CP-IV-0040


- chapter line: 7670
- atlas source solution flag: `unknown`
- linked source-solution candidates: `none`
- embedded solution marker in problem body: `NO`

```tex
\par\noindent\textbullet\quad $A=\{f\in C([0,1]) : f(1/2)=0\}$;
```

## CP-IV-0041


- chapter line: 7675
- atlas source solution flag: `unknown`
- linked source-solution candidates: `none`
- embedded solution marker in problem body: `NO`

```tex
\par\noindent\textbullet\quad If $X=\mathbb{N}$, show that $(f_n)$ has a pointwise convergent subsequence.
```

## CP-IV-0042


- chapter line: 7680
- atlas source solution flag: `unknown`
- linked source-solution candidates: `none`
- embedded solution marker in problem body: `NO`

```tex
$f_n(x)=\sin(x)/n\to 0$ uniformly on $\mathbb{R}$.

	\par\noindent\textbullet\quad \textbf{Inclusion and restriction.}
	If $Y\subset X$ (subspace topology), the inclusion $i:Y\hookrightarrow X$ is continuous.
	If $f:X\to Z$ is continuous, then $f|_Y$ is continuous.

	\par\noindent\textbullet\quad \textbf{Continuous need not be closed.}
	$f:\mathbb{R}\to\mathbb{R}$, $f(x)=e^x$ is continuous but sends the closed set $\mathbb{R}$ to $(0,\infty)$, which is not closed.
```

## CP-IV-0046


- chapter line: 7721
- atlas source solution flag: `unknown`
- linked source-solution candidates: `none`
- embedded solution marker in problem body: `NO`

```tex
â€” Triangle with vertices \((0,0)\to(2,1)\to(1,3)\to(0,0)\)

Integrate \(\tfrac12(x\,dy-y\,dx)\) edge by edge (CCW orientation).

Parametrize \(x=2t\), \(y=t\), \(t\in[0,1]\). Then \(dx=2\,dt\), \(dy=dt\), and
\[
\frac12(x\,dy-y\,dx)
=
\frac12\,(2t\cdot dt - t\cdot 2\,dt)
=
0
\quad\Rightarrow\quad \text{contribution }=0.
\]

Parametrize \(x=2-s\), \(y=1+2s\), \(s\in[0,1]\). Then \(dx=-ds\), \(dy=2\,ds\), and
\[
\frac12(x\,dy-y\,dx)
=
\frac12\Bigl((2-s)\cdot 2 - (1+2s)\cdot(-1)\Bigr)\,ds
=
\frac{5}{2}\,ds.
\]
Contribution:
\[
\int_{0}^{1}\frac{5}{2}\,ds=\frac{5}{2}=2.5.
\]

Parametrize \(x=1-t\), \(y=3-3t\), \(t\in[0,1]\). Then \(dx=-dt\), \(dy=-3\,dt\), and
\[
\frac12(x\,dy-y\,dx)
=
\frac12\Bigl((1-t)(-3) - (3-3t)(-1)\Bigr)\,dt
=
0
\quad\Rightarrow\quad \text{contribution }=0.
\]

\[
\operatorname{Area}=0+2.5+0=\boxed{2.5}.
\]
(Checks the shoelace formula:
\(\displaystyle \tfrac12\bigl|0\cdot1+2\cdot3+1\cdot0-(2\cdot0+1\cdot1+0\cdot3)\bigr|
=\tfrac12|6-1|=2.5\).)
```

## CP-IV-0050


- chapter line: 7816
- atlas source solution flag: `unknown`
- linked source-solution candidates: `none`
- embedded solution marker in problem body: `NO`

```tex
\par\noindent\textbullet\quad $f_n(x)=x e^{-nx}$ on $X=[0,\infty)$.
```

## CP-IV-0054


- chapter line: 7821
- atlas source solution flag: `unknown`
- linked source-solution candidates: `none`
- embedded solution marker in problem body: `YES`

```tex
\par\noindent\textbullet\quad (\textbf{CR in matrix form})
	Show $T$ is complex-linear iff $a=d$ and $b=-c$.
	\emph{Solution.} From Ex.\ 1, $B=0\iff a=d,\ c=-b$, i.e.\ matrix $\begin{psmallmatrix}a&-t\\ t&a\end{psmallmatrix}$.
```

## CP-IV-0055


- chapter line: 7828
- atlas source solution flag: `unknown`
- linked source-solution candidates: `none`
- embedded solution marker in problem body: `YES`

```tex
\par\noindent\textbullet\quad (\textbf{Recover $A,B$ from a real matrix})
	Let $T$ have real matrix $\begin{psmallmatrix}a&b\\ c&d\end{psmallmatrix}$ via
	$T(x+iy)=(ax+by)+i(cx+dy)$. Derive $A,B$ in $T(z)=Az+B\bar z$.

	\emph{Solution.} Compare coefficients using $z=x+iy,\ \bar z=x-iy$:
	\[
	A=\frac{a+d}{2}+i\,\frac{c-b}{2},\qquad
	B=\frac{a-d}{2}+i\,\frac{c+b}{2}.
	\]
```

## CP-IV-0056


- chapter line: 7841
- atlas source solution flag: `unknown`
- linked source-solution candidates: `none`
- embedded solution marker in problem body: `NO`

```tex
\par\noindent\textbullet\quad $\{(x,y): y/x\in\mathbb{N}\}\ \cup\ \{(x,y): x=0\}$.
```

## CP-IV-0058


- chapter line: 7885
- atlas source solution flag: `unknown`
- linked source-solution candidates: `none`
- embedded solution marker in problem body: `NO`

```tex
\par\noindent\textbullet\quad \textbf{Dropping the top derivative breaks completeness.}

	On $C^k$ with the truncated metric
	\[
	\tilde d(f,g)=\sum_{j=0}^{k-1}\|f^{(j)}-g^{(j)}\|_\infty,
	\]
	choose $(f_n)\subset C^\infty$ so that $f_n^{(j)}$ converge uniformly for $j<k$,
	while $f_n^{(k)}$ oscillate without a uniform limit.
	Then $(f_n)$ is Cauchy for $\tilde d$ but has no limit in $C^k$.

	\medskip
```

## CP-IV-0059


- chapter line: 7900
- atlas source solution flag: `unknown`
- linked source-solution candidates: `none`
- embedded solution marker in problem body: `NO`

```tex
\par\noindent\textbullet\quad \textbf{Cauchy $\Rightarrow$ convergent in $C^k$.}

	On $[0,1]$, let
	\[
	f_n(x)=\sum_{m=0}^{n}\frac{x^{m}}{m!}.
	\]
	Each $f_n\in C^\infty$.
	For every fixed $j\in\{0,\dots,k\}$ we have
	\[
	\sup_{x\in[0,1]}\bigl|\,f_n^{(j)}(x)-e^{(\cdot)\,(j)}(x)\,\bigr|\;\longrightarrow\;0.
	\]
	Hence $(f_n)$ is Cauchy in $d_{C^k}$ and therefore
	\[
	f_n \;\xrightarrow[n\to\infty]{}\; e^x \quad\text{in } C^k([0,1]).
	\]

	\medskip
```

## CP-IV-0063


- chapter line: 7921
- atlas source solution flag: `unknown`
- linked source-solution candidates: `none`
- embedded solution marker in problem body: `NO`

```tex
(restated).

For $\alpha\in(-1,1)$ with $\alpha\neq0$, compute
\[
\int_{0}^{\infty}\frac{x^{\alpha}}{x^{2}+x+1}\,dx .
\]

For $\alpha\in(-1,1)$, $\alpha\neq 0$,
\[
I(\alpha)=\int_{0}^{\infty}\frac{x^{\alpha}}{x^{2}+x+1}\,dx
=\frac{2\pi}{\sqrt3}\,\frac{\sin\!\big((\alpha+1)\pi/3\big)}{\sin(\pi\alpha)}.
\]
\emph{Reason.} Using the Mellinâ€“type formula
$\displaystyle \int_{0}^{\infty}\frac{x^{\mu-1}}{x^{2}+2x\cos\phi+1}\,dx
=\frac{\pi\sin(\mu\phi)}{\sin(\pi\mu)\sin\phi}$ (keyhole contour),
with $\mu=\alpha+1$ and $\phi=\pi/3$.

\medskip
```

## CP-IV-0067


- chapter line: 7982
- atlas source solution flag: `unknown`
- linked source-solution candidates: `none`
- embedded solution marker in problem body: `NO`

```tex
\par\noindent\textbullet\quad Show that $C^k([a,b])$ is a complete metric space.
```

## CP-IV-0068


- chapter line: 7987
- atlas source solution flag: `unknown`
- linked source-solution candidates: `none`
- embedded solution marker in problem body: `NO`

```tex
Let $f(z)=z^{2}$ and $C$ any closed $C^{1}$ loop avoiding singularities (there are none). Then
\[
\oint_{C} z^{2}\,dz \;=\; 0.
\]
```

## CP-IV-0071


- chapter line: 7995
- atlas source solution flag: `unknown`
- linked source-solution candidates: `none`
- embedded solution marker in problem body: `NO`

```tex
\par\noindent\textbullet\quad $f_n(x)=x^{2n}$ on $X=(0,1)$.
```

## CP-IV-0075


- chapter line: 8060
- atlas source solution flag: `unknown`
- linked source-solution candidates: `none`
- embedded solution marker in problem body: `NO`

```tex
\par\noindent\textbullet\quad \textbf{$(C^1,\|\cdot\|_\infty)$ is not complete.}

	Let $f_n(x)=\sqrt{x^2+\tfrac{1}{n}}$.
	Then $f_n\in C^\infty$ and $f_n\to |x|$ uniformly, but $|x|\notin C^1$.
	Thus $(C^1([0,1]),\|\cdot\|_\infty)$ is incomplete.

	\medskip
```

## CP-IV-0081


- chapter line: 8119
- atlas source solution flag: `unknown`
- linked source-solution candidates: `none`
- embedded solution marker in problem body: `YES`

```tex
\par\noindent\textbullet\quad (\textbf{Composition law})
	Let $T(z)=Az+B\bar z$ and $S(z)=Cz+D\bar z$. Show
	\[
	S\circ T(z)=(CA+D\overline{B})\,z\;+\;(CB+D\overline{A})\,\bar z.
	\]
	Deduce that the set of real-linear maps $\mathbb{C}\to\mathbb{C}$ is closed under composition, and $S\circ T$ is complex-linear iff $CB+D\overline{A}=0$.
	\emph{Solution.} Note $\overline{T(z)}=\overline{A}\bar z+\overline{B}z$ and compute
	$S(T(z))=C\,T(z)+D\,\overline{T(z)}$; read off the $z,\bar z$ coefficients.
```

## CP-IV-0083


- chapter line: 8131
- atlas source solution flag: `unknown`
- linked source-solution candidates: `none`
- embedded solution marker in problem body: `NO`

```tex
a circle mapped to the real axis

As a concrete example, let $L$ be the unit circle
	\[
	L = \{ z\in\mathbb C : |z|=1 \},
	\]
	and choose three distinct points on $L$:
	\[
	a = 1,\qquad b=-1,\qquad c=i.
	\]
	Then the associated map
	\[
	\Phi(z) = \frac{(z-a)(c-b)}{(z-b)(c-a)}
	\]
	sends $L$ onto the real axis, with
	\[
	\Phi(a)=0,\qquad \Phi(b)=\infty,\qquad \Phi(c)=1.
	\]
	For $z$ not on $L$, the sign of $\Im \Phi(z)$ indicates on which side of
	the circle $L$ the point $z$ lies. One side of $L$ (for instance, the
	interior) is mapped to the upper half-plane $\Im w>0$, while the other
	side (the exterior) is mapped to the lower half-plane $\Im w<0$.

	Figure~\ref{fig:crossratio-z-plane} illustrates this: we show the circle
	$L$, the points $a,b,c$, and a cloud of sample points in the plane,
	distinguished according to the sign of $\Im\Phi(z)$. In
	Figure~\ref{fig:crossratio-w-plane}, we see their images under $\Phi$,
	which lie strictly above or below the real axis.
```

## CP-IV-0085


- chapter line: 8177
- atlas source solution flag: `unknown`
- linked source-solution candidates: `none`
- embedded solution marker in problem body: `NO`

```tex
\par\noindent\textbullet\quad $\{(x,0): 0< x< 1\}$.
```

## CP-IV-0087


- chapter line: 8182
- atlas source solution flag: `unknown`
- linked source-solution candidates: `none`
- embedded solution marker in problem body: `NO`

```tex
\par\noindent\textbullet\quad $\{(x,y): y>0\}$.
```

