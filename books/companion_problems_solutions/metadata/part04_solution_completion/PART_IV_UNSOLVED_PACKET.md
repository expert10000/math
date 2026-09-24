# Part IV Unsolved Problem Packet

- total Part IV problems: 139
- solution environments present: 39
- unsolved problems: 100
- unsolved with linked source-solution candidates: 0

This packet is generated from the current local Part IV chapter. It is the basis for source-recovery first, then canonical solution authoring.

## Unclassified

### CP-IV-0009

- chapter line: 56
- atlas source solution flag: `unknown`
- linked source-solution candidates: `none`
- embedded solution marker in problem body: `NO`

```tex
\par\noindent\textbullet\quad \textbf{Removable:} $f$ is bounded near $a$ $\Rightarrow$ $f$ extends holomorphically to $a$ (Riemann).
```

### CP-IV-0012

- chapter line: 61
- atlas source solution flag: `unknown`
- linked source-solution candidates: `none`
- embedded solution marker in problem body: `NO`

```tex
the exponential sequence

On a complex manifold $X$, there is an exact sequence of sheaves

	\[
	0
	\longrightarrow
	\mathbb Z
	\longrightarrow
	\mathcal O_X
	\xrightarrow{\exp(2\pi i\,\cdot)}
	\mathcal O_X^\times
	\longrightarrow
	0.
	\]

	Here $\mathbb Z$ denotes the constant sheaf of locally constant integer-valued
	functions.

	The map

	\[
	\mathbb Z\to \mathcal O_X
	\]

	is the inclusion of locally constant integer-valued functions into holomorphic
	functions.

	The map

	\[
	\mathcal O_X\to \mathcal O_X^\times
	\]

	is

	\[
	f\mapsto e^{2\pi i f}.
	\]

	We check exactness.

	First, the kernel of the exponential map consists of holomorphic functions
	$f$ satisfying

	\[
	e^{2\pi i f}=1.
	\]

	Locally, this means

	\[
	f\in \mathbb Z.
	\]

	Thus

	\[
	\ker(\exp)=\mathbb Z.
	\]

	Second, the exponential map is locally surjective. Indeed, every nowhere-zero
	holomorphic function has a local holomorphic logarithm.

	Therefore

	\[
	\im(\exp)=\mathcal O_X^\times
	\]

	as sheaves.

	Hence the sequence

	\[
	0
	\longrightarrow
	\mathbb Z
	\longrightarrow
	\mathcal O_X
	\xrightarrow{\exp(2\pi i\,\cdot)}
	\mathcal O_X^\times
	\longrightarrow
	0
	\]

	is exact as a sequence of sheaves.

	However, it need not be exact on global sections.

	For example, if

	\[
	X=\mathbb C^\times,
	\]

	then

	\[
	z\mapsto z
	\]

	is a global section of $\mathcal O_X^\times$, but it has no global holomorphic
	logarithm.

	Therefore the map

	\[
	\mathcal O_X(X)\to \mathcal O_X^\times(X)
	\]

	is not surjective.

	This example shows:

	\[
	\boxed{
		\text{Exactness of sheaves is local exactness.}}
\]

	It also shows:

	\[
	\boxed{
		\text{A surjective morphism of sheaves need not be surjective on global sections.}
	}\]
```

### CP-IV-0014

- chapter line: 191
- atlas source solution flag: `unknown`
- linked source-solution candidates: `none`
- embedded solution marker in problem body: `NO`

```tex
\par\noindent\textbullet\quad \textbf{Holomorphic (MĂ¶bius) â€śinversionâ€ť} about $a$ with radius $r$:
	\[
	J_{a,r}(z)\;=\;a+\frac{r^{2}}{z-a}
	\qquad (z\neq a).
	\]
	This is a MĂ¶bius transformation (holomorphic on $\mathbb C\setminus\{a\}$).

\paragraph{\textbf{Polar form: what happens to modulus and argument.}}
Write
\[
z-a=\rho e^{i\theta}\qquad(\rho>0).
\]
Then
```

### CP-IV-0017

- chapter line: 329
- atlas source solution flag: `unknown`
- linked source-solution candidates: `none`
- embedded solution marker in problem body: `YES`

```tex
\par\noindent\textbullet\quad (\textbf{Quick diagnostics})
	For each matrix, compute $(A,B)$ and decide if $T$ is complex-linear.
	\[
	\text{(a) }\begin{psmallmatrix}2&1\\ -1&2\end{psmallmatrix}\quad
	\text{(b) }\begin{psmallmatrix}1&1\\ 1&1\end{psmallmatrix}\quad
	\text{(c) }\begin{psmallmatrix}0&1\\ 1&0\end{psmallmatrix}.
	\]
	\emph{Solution.}
	(a) $A=2+i(-1-1)/2=2-i,\ B=\tfrac{2-2}{2}+i\tfrac{-1+1}{2}=0$ $\Rightarrow$ holomorphic.
	(b) $A=1+i\,0=1,\ B=0+i\,1=i$ $\Rightarrow$ not holomorphic.
	(c) $A=\tfrac{0+0}{2}+i\,\tfrac{1-1}{2}=0,\ B=\tfrac{0-0}{2}+i\,\tfrac{1+1}{2}=i$ $\Rightarrow$ not holomorphic.
```

### CP-IV-0034

- chapter line: 407
- atlas source solution flag: `unknown`
- linked source-solution candidates: `none`
- embedded solution marker in problem body: `NO`

```tex
an image sheaf larger than the objectwise image

Let

	\[
	X=\mathbb C^\times
	=
	\mathbb C\setminus\{0\}.
	\]

	Let $\mathcal O_X$ be the sheaf of holomorphic functions on $X$, and let
	$\mathcal O_X^\times$ be the sheaf of nowhere-zero holomorphic functions.

	There is a morphism of sheaves

	\[
	\exp:\mathcal O_X\to \mathcal O_X^\times
	\]

	given by

	\[
	f\longmapsto e^{2\pi i f}.
	\]

	Locally, every nowhere-zero holomorphic function has a holomorphic logarithm.
	Therefore, locally, every section of $\mathcal O_X^\times$ lies in the image of
	$\exp$.

	Hence the sheaf image is

	\[
	\im(\exp)=\mathcal O_X^\times.
	\]

	However, globally, the function

	\[
	g(z)=z
	\]

	on $\mathbb C^\times$ has no global holomorphic logarithm.

	Indeed, if there were a holomorphic function

	\[
	h:\mathbb C^\times\to\mathbb C
	\]

	such that

	\[
	e^{2\pi i h(z)}=z,
	\]

	then $h$ would define a global branch of the logarithm on $\mathbb C^\times$.
	But such a branch does not exist.

	Therefore

	\[
	z\notin
	\im\left(
	\mathcal O_X(X)\to \mathcal O_X^\times(X)
	\right).
	\]

	Thus

	\[
	\boxed{
		\im_{\text{sheaf}}(\exp)=\mathcal O_X^\times,
	}\]

	but

	\[
	\boxed{
		\im\left(
		\mathcal O_X(X)\to \mathcal O_X^\times(X)
		\right)
		\neq
		\mathcal O_X^\times(X).
	}\]

	This is one of the most important examples of the difference between global
	image and sheaf image.

	\[
	\boxed{
		\text{Sheaf image means locally image, not globally image.}
	}\]
```

### CP-IV-0035

- chapter line: 503
- atlas source solution flag: `unknown`
- linked source-solution candidates: `none`
- embedded solution marker in problem body: `NO`

```tex
a line mapped to the real axis

Now let $L$ be a straight line instead of a circle. Take, for instance,
	the imaginary axis
	\[
	L = \{ z = i y : y\in\mathbb R\},
	\]
	and choose three distinct points on $L$:
	\[
	a = i,\qquad b=-i,\qquad c=0.
	\]
	The corresponding cross-ratio map
	\[
	\Phi(z)
	= \frac{(z-a)(c-b)}{(z-b)(c-a)}
	\]
	again satisfies
	\[
	\Phi(a)=0,\qquad \Phi(b)=\infty,\qquad \Phi(c)=1,
	\]
	and sends the whole line $L$ onto the real axis
	$\mathbb R\cup\{\infty\}$. As before, the two sides of $L$ are mapped
	onto the upper and lower half-planes:
	\[
	\text{one side of } L \;\longmapsto\; \{ w : \Im w > 0\},\qquad
	\text{the other side} \;\longmapsto\; \{ w : \Im w < 0\}.
	\]

	Figure~\ref{fig:crossratio-line-z-plane} shows the line $L$ and some
	sample points on each side, distinguished by the sign of $\Im \Phi(z)$.
	Figure~\ref{fig:crossratio-line-w-plane} illustrates their images under
	$\Phi$: the line becomes the real axis, with $\Phi(a)=0$ and
	$\Phi(c)=1$, and the two sides become the upper and lower half-planes.
\begin{figure}[ht]
  \centering
  \includegraphics[width=0.78\textwidth]{figures/part04/cp_iv_0035_crossratio_line_w_plane.png}
  \caption{Source-backed Part IV figure: crossratio line w plane.}
  \label{fig:crossratio-line-w-plane}
\end{figure}

\begin{figure}[ht]
  \centering
  \includegraphics[width=0.78\textwidth]{figures/part04/cp_iv_0035_crossratio_line_z_plane.png}
  \caption{Source-backed Part IV figure: crossratio line z plane.}
  \label{fig:crossratio-line-z-plane}
\end{figure}


	\medskip

	\clearpage

Let $H_1,H_2$ be half-planes with boundary arcs $L_1,L_2$.
Choose boundary triples
\[
a,b,c \in L_1, \qquad A,B,C \in L_2
\]
in the same cyclic order as seen from the chosen sides of $H_1,H_2$.

First send $L_1$ to the real axis by the cross-ratio map
\[
\Phi(z) := \frac{(z-a)(c-b)}{(z-b)(c-a)}.
\]
Then $\Phi(a)=0$, $\Phi(b)=\infty$, $\Phi(c)=1$, and the two sides of
$L_1$ correspond to the half-planes $\Im\Phi(z)\gtrless 0$.

Next send $L_2$ to the real axis by
\[
\Psi(w) := \frac{(w-A)(C-B)}{(w-B)(C-A)},
\]
so that $\Psi(A)=0$, $\Psi(B)=\infty$, $\Psi(C)=1$.

The desired map $T : H_1 \to H_2$ is given by
\[
\Psi\bigl(T(z)\bigr) = \Phi(z),
\qquad\text{i.e.}\qquad
T(z) = \Psi^{-1}(\Phi(z)).
\]
Solving for $\Psi^{-1}$ yields the explicit formula
\[
T(z)
= \frac{A(C-B) - \Phi(z)\, B(C-A)}{(C-B) - \Phi(z)\,(C-A)},
\qquad
\Phi(z) = \frac{(z-a)(c-b)}{(z-b)(c-a)}.
\]
Then
\[
T(a)=A,\qquad T(b)=B,\qquad T(c)=C,
\]
and $T$ maps the chosen side of $H_1$ biholomorphically onto the chosen
side of $H_2$. If the orientation of the half-plane is reversed, one may
replace $\Phi$ by $-\Phi$ or interchange two of the boundary points to
flip the side.
```

### CP-IV-0037

- chapter line: 600
- atlas source solution flag: `unknown`
- linked source-solution candidates: `none`
- embedded solution marker in problem body: `NO`

```tex
Let $U\subset\mathbb C$ be a domain and let $(f_n)$ be a sequence of univalent
(holomorphic injective) functions $f_n:U\to\mathbb C$ such that
$f_n\to f$ uniformly on every compact $K\Subset U$.
Show that the limit $f$ is either univalent or constant.

\bigskip

  We collect the tools we use and the exact way they are applied.

\medskip

\textbf{Rouch\'e's Theorem.}
Let $g,h$ be holomorphic on and inside a simple closed curve $\gamma$.
If $|h(z)|<|g(z)|$ for all $z\in\gamma$, then $g$ and $g+h$ have the same number
of zeros (counted with multiplicity) in the interior of $\gamma$.

\emph{Application here.}
Fix $w\in\mathbb C$. If $f(z_0)=w$ and $z_0$ is the only zero of $f-w$ in a small disc $D$
(with $|f(z)-w|>0$ on $\partial D$), then the uniform convergence on $\partial D$ gives
$|f_n-f|<|f-w|$ there for all large $n$.
Hence $f_n-w$ and $f-w$ have the same zero count in $D$; in particular, $f_n(z)=w$
has at least one solution in $D$ for all large $n$.

\medskip

\textbf{Hurwitz's Theorem.}
If $g_n\to g$ uniformly on compacta in a domain and each $g_n$ is holomorphic
and \emph{non-vanishing}, then either $g\equiv 0$ or $g$ is non-vanishing.
Equivalently, zeros of $g$ are locally the limits of zeros of $g_n$, counted with multiplicity.

\emph{Application here (derivative version).}
For univalent $f_n$, the inverse function theorem ensures $f_n'(z)\neq 0$ on $U$.
If $f$ were non-constant \emph{and} had a critical point $f'(z_0)=0$, then by Hurwitz
applied to $g_n=f_n'$ we would get a contradiction, since $g_n$ never vanish.
Thus a non-constant limit $f$ must satisfy $f'(z)\neq 0$ everywhere (hence be locally injective).

\medskip

\textbf{Two consequences for univalent maps.}
(i) If $f$ is holomorphic and injective on $U$, then $f'(z)\neq 0$ for all $z\in U$.
(ii) If $f(z_1)=f(z_2)=w$ with $z_1\neq z_2$, then by Rouch\'e the value $w$ must be
assumed by $f_n$ in disjoint neighborhoods of $z_1$ and $z_2$ for all large $n$,
contradicting injectivity of $f_n$.

\bigskip

Assume $f$ is not constant.
Suppose, towards a contradiction, that $f$ is not injective: pick
$z_1\neq z_2$ in $U$ with $f(z_1)=f(z_2)=:w$.

Choose disjoint closed discs $\overline{D_1},\overline{D_2}\Subset U$ centered at
$z_1,z_2$, respectively, so small that
\[
f(\partial D_j)\cap\{w\}=\varnothing
\quad\text{and}\quad
\text{$f-w$ has no zeros in $\overline{D_j}$ except at $z_j$}
\]
for $j=1,2$.
Uniform convergence on $\partial D_j$ yields $|f_n-f|<|f-w|$ there for all $n\ge N$,
hence, by Rouch\'e, $f_n-w$ and $f-w$ have the same number of zeros in $D_j$.
Therefore, for all $n\ge N$, the equation $f_n(z)=w$ has at least one solution in each $D_j$.
Because $D_1\cap D_2=\varnothing$, this gives \emph{two} distinct solutions,
contradicting injectivity of $f_n$.

Thus a non-constant limit $f$ cannot fail to be injective.
Hence $f$ is either univalent or constant.
\hfill$\square$

\bigskip

Assume $f$ is not constant and $f_n\to f$ locally uniformly.
Since each $f_n$ is univalent, $f_n'(z)\neq 0$ for all $z$.
By Hurwitz applied to $(f_n')$, either $f'\equiv 0$ (which would force $f$ to be constant,
contrary to assumption) or $f'(z)\neq 0$ everywhere.
Thus $f$ is a local biholomorphism on $U$; a standard covering-space/plane-domain argument
then promotes local injectivity to global injectivity on $U$, so $f$ is univalent.

\bigskip

	\par\noindent\textbullet\quad \emph{Univalent limit:} $f_n(z)=z+\tfrac1n$ on any domain $U$.
	Then $f_n\to f(z)=z$ (univalent).
	\par\noindent\textbullet\quad \emph{Constant limit:} $f_n(z)=\tfrac1n\,z$ on any domain $U$.
	Then $f_n\to f\equiv 0$ (constant).
	\par\noindent\textbullet\quad \emph{Disk automorphisms:} On $\mathbb D$, $f_n(z)=\dfrac{z}{1-\frac{z}{n}}$ are univalent
	and $f_n\to f(z)=z$ uniformly on compacta.
```

### CP-IV-0039

- chapter line: 691
- atlas source solution flag: `unknown`
- linked source-solution candidates: `none`
- embedded solution marker in problem body: `NO`

```tex
(General mixed map).

Take $A=1+\tfrac12 i$, $B=0.6-0.2i$. Then
\[
\det DT=|A|^2-|B|^2=(1^2+\tfrac{1}{4})-(0.6^2+0.2^2)=1.25-0.40=0.85>0,
\]
so $T$ is invertible and orientation-preserving, but not holomorphic ($B\neq0$).
Singular values are $\sigma_{\max}=|A|+|B|\approx \sqrt{1.25}+ \sqrt{0.40}$ and
$\sigma_{\min}=||A|-|B||$, giving principal stretches of the ellipse.

For any $T(z)=Az+B\bar z$, the image of the unit circle is an ellipse whenever $|A|\neq|B|$; it degenerates to a segment/point when $|A|=|B|$.
Holomorphicity is equivalent to $B=0$; antiholomorphicity (composition with conjugation) corresponds to $A=0$.
```

### CP-IV-0047

- chapter line: 874
- atlas source solution flag: `unknown`
- linked source-solution candidates: `none`
- embedded solution marker in problem body: `NO`

```tex
Complex Geometry

Let \(X\) be a complex manifold, and let
\[
\OO_X
\]
be the sheaf of holomorphic functions on \(X\).

Fix a point
\[
p\in X.
\]

Define
\[
\mathfrak m_p(U)
=
\{f\in \OO_X(U): f(p)=0 \text{ if }p\in U\}.
\]

Then
\[
\mathfrak m_p\subseteq \OO_X.
\]

There is an evaluation morphism
\[
\OO_X\to \CC_p.
\]

The kernel consists of holomorphic functions vanishing at \(p\). Therefore
\[
\ker(\OO_X\to \CC_p)=\mathfrak m_p.
\]

Hence
\[
\OO_X/\mathfrak m_p\cong \CC_p.
\]

So we have the short exact sequence
\[
0\to \mathfrak m_p
\to \OO_X
\to \CC_p
\to 0.
\]

At the level of stalks at \(p\), this gives
\[
0\to \mathfrak m_p
\to \OO_{X,p}
\to \CC
\to 0.
\]

Therefore
\[
\OO_{X,p}/\mathfrak m_p\cong \CC.
\]

The stalk
\[
\OO_{X,p}
\]
is the local ring of holomorphic function germs at \(p\).

The ideal
\[
\mathfrak m_p
\]
is the maximal ideal of germs vanishing at \(p\).

The quotient
\[
\OO_{X,p}/\mathfrak m_p
\]
is the residue field at \(p\), which is
\[
\CC.
\]

Thus quotient sheaves connect directly to local rings and residue fields.

\[
\boxed{
	\OO_{X,p}/\mathfrak m_p\cong \CC.
}\]
```

### CP-IV-0051

- chapter line: 966
- atlas source solution flag: `unknown`
- linked source-solution candidates: `none`
- embedded solution marker in problem body: `NO`

```tex
Let $\gamma:[0,1]\to\mathbb C$ be a $C^1$ curve with $\gamma(0)=i$, $\gamma(1)=-i$,
	such that $\gamma$ does not intersect $(-\infty,0]$. Compute
	\[
	\int_{\gamma}\Log^2(z)\,dz,
	\]
	where $\Log$ denotes the principal branch.

	We use $\Log z=\ln|z|+i\Arg z$ with branch cut $(-\infty,0]$ and $\Arg z\in(-\pi,\pi)$.
	On any simply connected set avoiding the cut, $\Log^2 z$ is holomorphic, hence the integral
	is path independent. Seek an antiderivative of the form $F(z)=z\,G(\Log z)$. Then
	\[
	F'(z)=G(\Log z)+G'(\Log z)=\Log^2 z
	\iff
	G'(w)+G(w)=w^2.
	\]
	A polynomial solution is $G(w)=w^2-2w+2$, since $(2w-2)+(w^2-2w+2)=w^2$.
	Thus
	\[
	F(z)=z\big(\Log^2 z-2\Log z+2\big),\qquad F'(z)=\Log^2 z.
	\]

	Using $\Log(i)=i\frac{\pi}{2}$, $\Log(-i)=-i\frac{\pi}{2}$,
	\[
	\begin{aligned}
		F(i)&=i\!\left(\left(i\frac{\pi}{2}\right)^{2}-2\left(i\frac{\pi}{2}\right)+2\right)
		=-\frac{i\pi^{2}}{4}+\pi+2i,\\[2mm]
		F(-i)&=-i\!\left(\left(-i\frac{\pi}{2}\right)^{2}-2\left(-i\frac{\pi}{2}\right)+2\right)
		=\frac{i\pi^{2}}{4}+\pi-2i.
	\end{aligned}
	\]
	Therefore
	\[
	\boxed{\ \displaystyle \int_{\gamma}\Log^{2}z\,dz
		=F(-i)-F(i)= i\!\left(\frac{\pi^{2}}{2}-4\right). \ }
	\]

	More generally, for $n\in\mathbb N$ one may integrate $\Log^{n}z$ by solving
	$G'+G=w^{n}$ and taking $F(z)=z\,G(\Log z)$.

\section*{Integral of $e^{e^{it}}$ over one period}
```

### CP-IV-0065

- chapter line: 1057
- atlas source solution flag: `unknown`
- linked source-solution candidates: `none`
- embedded solution marker in problem body: `NO`

```tex
upper half-plane to right half-plane

A particularly simple instance is obtained by taking
\[
T(z) = -i z.
\]
Then
\[
\Re T(z) = \Re(-iz) = \Im z,
\]
so
\[
\Im z > 0 \quad\Longleftrightarrow\quad \Re T(z) > 0.
\]
Thus $T$ maps the upper half-plane
\[
H_1 = \{ z : \Im z > 0 \}
\]
bijectively onto the right half-plane
\[
H_2 = \{ w : \Re w > 0 \},
\]
sending the boundary line $L_1 = \mathbb R$ to the boundary line
$L_2 = i\mathbb R$.

Figures~\ref{fig:hp-to-hp-z-plane-fixed} and
\ref{fig:hp-to-hp-w-plane-fixed} illustrate this example.
\begin{figure}[ht]
  \centering
  \includegraphics[width=0.78\textwidth]{figures/part04/cp_iv_0065_hp_to_hp_w_plane.png}
  \caption{Source-backed Part IV figure: hp to hp w plane fixed.}
  \label{fig:hp-to-hp-w-plane-fixed}
\end{figure}

\begin{figure}[ht]
  \centering
  \includegraphics[width=0.78\textwidth]{figures/part04/cp_iv_0065_hp_to_hp_z_plane.png}
  \caption{Source-backed Part IV figure: hp to hp z plane fixed.}
  \label{fig:hp-to-hp-z-plane-fixed}
\end{figure}


\medskip
\noindent
The above example is the simplest possible case of a half-plane to
half-plane mapping, since $T(z)=-iz$ is just a rotation by $-\pi/2$.
However, every biholomorphic map between half-planes can be obtained from
the general threeâ€“boundaryâ€“points construction described earlier.  In
particular, if $a,b,c$ are three distinct points on the boundary line
$L_1=\mathbb R$, and $A,B,C$ are three distinct points on the boundary
line $L_2=i\mathbb R$ in the same cyclic order, then the unique M\"obius
map satisfying
\[
T(a)=A,\qquad T(b)=B,\qquad T(c)=C
\]
is given explicitly by
\[
T(z)
= \frac{A(C-B) - \Phi(z)\, B(C-A)}{(C-B) - \Phi(z)\,(C-A)},
\qquad
\Phi(z) = \frac{(z-a)(c-b)}{(z-b)(c-a)}.
\]
This expression reduces to $T(z)=-iz$ precisely when the triples
$(a,b,c)$ and $(A,B,C)$ are chosen so that the cross-ratios coincide and
the real axis is mapped to the imaginary axis by a pure rotation.
Thus the simple rotation $T(z)=-iz$ is not an isolated coincidence, but
a special case of the general boundary-normalization principle.

We now give a non-trivial instance of the general construction.
Take three distinct boundary points on the real axis
\[
a=-2,\qquad b=1,\qquad c=4,
\]
and three distinct boundary points on the imaginary axis
\[
A=-i,\qquad B=0,\qquad C=2i,
\]
listed in the same cyclic order (bottom $\to$ top).

The cross-ratio map sending $a,b,c$ to $0,\infty,1$ is
\[
\Phi(z)
= \frac{(z-a)(c-b)}{(z-b)(c-a)}
= \frac{(z+2)(3)}{(z-1)(6)}.
\]

The inverse map sending $0,\infty,1$ back to $A,B,C$ is
\[
\Psi^{-1}(\xi)
= \frac{A(C-B) - \xi\,B(C-A)}{(C-B) - \xi\,(C-A)}.
\]

Hence the desired half-plane map is
\[
T(z) = \Psi^{-1}(\Phi(z)),
\]
which explicitly is
\[
T(z)
= \frac{-i(2i-0) - \Phi(z)\,0(2i - (-i))}
{(2i-0) - \Phi(z)(2i - (-i))}
= \frac{-2i^2}{2i - 3i\,\Phi(z)}
= \frac{2}{\,2i - 3i\,\Phi(z)\,}.
\]

With these boundary triples one verifies
\[
T(a)=A,\qquad T(b)=B,\qquad T(c)=C,
\]
and $T$ maps the chosen side $\Im z>0$ biholomorphically onto the
chosen side $\Re w>0$.

Figures~\ref{fig:nontrivial-hp-z} and \ref{fig:nontrivial-hp-w}
illustrate this map.
\begin{figure}[ht]
  \centering
  \includegraphics[width=0.78\textwidth]{figures/part04/cp_iv_0065_nontrivial_hp_w_plane.png}
  \caption{Source-backed Part IV figure: nontrivial hp w.}
  \label{fig:nontrivial-hp-w}
\end{figure}

\begin{figure}[ht]
  \centering
  \includegraphics[width=0.78\textwidth]{figures/part04/cp_iv_0065_nontrivial_hp_z_plane.png}
  \caption{Source-backed Part IV figure: nontrivial hp z.}
  \label{fig:nontrivial-hp-z}
\end{figure}


\clearpage
```

### CP-IV-0066

- chapter line: 1191
- atlas source solution flag: `unknown`
- linked source-solution candidates: `none`
- embedded solution marker in problem body: `NO`

```tex
\par\noindent\textbullet\quad Always: $a,z,z^{*}$ are collinear and $|z-a|\cdot|z^{*}-a|=r^2$.

\paragraph{\textbf{TikZ diagram (schematic).}}
\begin{center}

\end{center}

\subsection*{\textbf{Geometric inversion vs holomorphic inversion (modulus inverted; angle preserved vs negated)}}

\paragraph{\textbf{Two maps that are both called â€śinversionâ€ť.}}
Fix a circle $C=\{|z-a|=r\}$.
```

### CP-IV-0069

- chapter line: 1206
- atlas source solution flag: `unknown`
- linked source-solution candidates: `none`
- embedded solution marker in problem body: `NO`

```tex
\par\noindent\textbullet\quad For \textbf{holomorphic inversion}:
	\[
	J_{a,r}(z)-a=\frac{r^{2}}{\rho e^{i\theta}}
	=\frac{r^{2}}{\rho}\,e^{-i\theta}.
	\]
	Hence
	\[
	|J_{a,r}(z)-a|=\frac{r^{2}}{|z-a|},\qquad
	\arg\bigl(J_{a,r}(z)-a\bigr)=-\arg(z-a)=-\theta.
	\]
	So the \textbf{modulus is inverted} and the \textbf{argument is negated}.

\paragraph{\textbf{Relation between them: â€śreflection + geometric inversionâ€ť.}}
Define reflection across the line through $a$ parallel to the real axis:
\[
R_a(z)=a+\overline{z-a}.
\]
Then
\[
J_{a,r}=R_a\circ I_{a,r}.
\]
Indeed, for $z\neq a$,
\[
(R_a\circ I_{a,r})(z)
=a+\overline{\,I_{a,r}(z)-a\,}
=a+\overline{\frac{r^{2}}{\overline{z-a}}}
=a+\frac{r^{2}}{z-a}
=J_{a,r}(z).
\]

\subsection*{\textbf{Chart: angle preserved vs negated (picture for $a=0$, $r=1$)}}

\paragraph{\textbf{Setup.}}
For the diagram we take $a=0$, $r=1$. (The general case is obtained by translating by $a$ and scaling by $r$.)

\paragraph{\textbf{Interpretation.}}
If $z=\rho e^{i\theta}$:
\[
I_{0,1}(z)=\frac{1}{\overline{z}}=\frac{1}{\rho}e^{i\theta}
\quad\text{(same ray, angle $\theta$),}\qquad
J_{0,1}(z)=\frac{1}{z}=\frac{1}{\rho}e^{-i\theta}
\quad\text{(reflected ray, angle $-\theta$).}
\]

\begin{center}

\end{center}

\subsection*{\textbf{Three common â€śinversionsâ€ť in complex analysis and geometry}}

\paragraph{\textbf{(A) The basic MĂ¶bius inversion (unit-circle inversion).}}
\[
J(z)=\frac{1}{z}\qquad (z\neq 0).
\]
If $z=\rho e^{i\theta}$, then
\[
J(z)=\frac{1}{\rho}e^{-i\theta},
\qquad
|J(z)|=\frac{1}{|z|},\qquad \arg J(z)=-\arg z.
\]
It fixes the unit circle: if $|z|=1$ then $|J(z)|=1$.

\paragraph{\textbf{(B) Geometric inversion in the circle $|z-a|=r$ (anti-holomorphic).}}
\[
I_{a,r}(z)=a+\frac{r^{2}}{\overline{z-a}}\qquad (z\neq a).
\]
Write $z-a=\rho e^{i\theta}$, then
\[
I_{a,r}(z)-a=\frac{r^{2}}{\rho}e^{i\theta},
\qquad
|I_{a,r}(z)-a|=\frac{r^{2}}{|z-a|},\qquad
\arg\bigl(I_{a,r}(z)-a\bigr)=\arg(z-a).
\]
Thus it inverts the radius but \emph{preserves} the argument (same ray from $a$). It fixes the circle $|z-a|=r$ pointwise.

\paragraph{\textbf{(C) Holomorphic â€ścircle inversionâ€ť (a MĂ¶bius map).}}
\[
H_{a,r}(z)=a+\frac{r^{2}}{z-a}\qquad (z\neq a).
\]
Write $z-a=\rho e^{i\theta}$, then
\[
H_{a,r}(z)-a=\frac{r^{2}}{\rho}e^{-i\theta},
\qquad
|H_{a,r}(z)-a|=\frac{r^{2}}{|z-a|},\qquad
\arg\bigl(H_{a,r}(z)-a\bigr)=-\arg(z-a).
\]
Thus it inverts the radius and \emph{negates} the argument (reflection of the ray). It preserves the circle $|z-a|=r$ as a set (not pointwise).

\paragraph{\textbf{Relationship between (B) and (C).}}
Let
\[
R_a(z)=a+\overline{z-a}
\]
be reflection across the horizontal line through $a$. Then
\[
H_{a,r}=R_a\circ I_{a,r}.
\]

\subsection*{\textbf{Summary table}}

\begin{center}
	\renewcommand{\arraystretch}{1.25}
	\begin{tabular}{|l|l|l|l|}
		\hline
		\textbf{Name} & \textbf{Formula} & \textbf{Modulus rule} & \textbf{Angle rule} \\
		\hline
		Unit MĂ¶bius inversion & $J(z)=\dfrac1z$ &
		$\left|J(z)\right|=\dfrac{1}{|z|}$ &
		$\arg J(z)= -\arg z$ \\
		\hline
		Geometric circle inversion & $I_{a,r}(z)=a+\dfrac{r^2}{\overline{z-a}}$ &
		$\left|I_{a,r}(z)-a\right|=\dfrac{r^2}{|z-a|}$ &
		$\arg(I_{a,r}(z)-a)=\arg(z-a)$ \\
		\hline
		Holomorphic circle inversion & $H_{a,r}(z)=a+\dfrac{r^2}{z-a}$ &
		$\left|H_{a,r}(z)-a\right|=\dfrac{r^2}{|z-a|}$ &
		$\arg(H_{a,r}(z)-a)= -\arg(z-a)$ \\
		\hline
	\end{tabular}
\end{center}

	\subsection*{\textbf{Inversion as a MĂ¶bius transformation (and its geometric cousin)}}

	\paragraph{\textbf{MĂ¶bius transformations.}}
	A MĂ¶bius map is
	\[
	f(z)=\frac{Az+B}{Cz+D},\qquad AD-BC\neq 0,
	\]
	and it is represented (projectively) by the matrix
	\[
	\begin{pmatrix}A & B\\ C & D\end{pmatrix}
	\quad\text{in } PSL(2,\mathbb C).
	\]

	\subsection*{\textbf{1) Where is the simple inversion $1/z$ in MĂ¶bius form?}}
	Take
	\[
	f(z)=\frac{0\cdot z+1}{1\cdot z+0}=\frac{1}{z}.
	\]
	So $1/z$ corresponds to the matrix
	\[
	\begin{pmatrix}0 & 1\\ 1 & 0\end{pmatrix}
	\quad\text{(in } PSL(2,\mathbb C)\text{).}
	\]

	\subsection*{\textbf{2) Where is the â€śradius-$r$â€ť holomorphic inversion $r^{2}/z$?}}
	Just scale:
	\[
	f(z)=\frac{0\cdot z+r^{2}}{1\cdot z+0}=\frac{r^{2}}{z},
	\qquad
	\begin{pmatrix}0 & r^{2}\\ 1 & 0\end{pmatrix}.
	\]

	\subsection*{\textbf{3) Where is the shifted version $a+\dfrac{r^{2}}{z-a}$?}}

	\paragraph{\textbf{Conjugation by translations.}}
	Let $T_a(z)=z+a$. Starting from $r^{2}/z$ we obtain
	\[
	H_{a,r}(z)=a+\frac{r^{2}}{z-a}
	= T_a\circ\left(\frac{r^{2}}{z}\right)\circ T_{-a}(z).
	\]

	\paragraph{\textbf{As an explicit fraction $(Az+B)/(Cz+D)$.}}
	Compute:
	\[
	H_{a,r}(z)=a+\frac{r^{2}}{z-a}
	=\frac{a(z-a)+r^{2}}{z-a}
	=\frac{az+(r^{2}-a^{2})}{z-a}.
	\]
	Therefore, matching with $\dfrac{Az+B}{Cz+D}$, we read off
	\[
	A=a,\qquad B=r^{2}-a^{2},\qquad C=1,\qquad D=-a,
	\]
	and hence
	\[
	H_{a,r}(z)\ \longleftrightarrow\
	\begin{pmatrix}
		a & r^{2}-a^{2}\\[2pt]
		1 & -a
	\end{pmatrix},
	\qquad
	\det=
	a(-a)-(r^{2}-a^{2})\cdot 1=-r^{2}\neq 0.
	\]

	\subsection*{\textbf{4) What about geometric circle inversion $a+\dfrac{r^{2}}{\overline{z-a}}$?}}

	\paragraph{\textbf{Not MĂ¶bius (anti-holomorphic).}}
	The geometric circle inversion is
	\[
	I_{a,r}(z)=a+\frac{r^{2}}{\overline{z-a}},
	\]
	and it is \emph{not} MĂ¶bius because it depends on $\overline{z}$ (it is anti-holomorphic).

	\paragraph{\textbf{But it becomes MĂ¶bius after composing with a reflection.}}
	Let
	\[
	R_a(z)=a+\overline{z-a}
	\]
	(reflection across the horizontal line through $a$). Then
	\[
	H_{a,r}=R_a\circ I_{a,r}.
	\]

	\subsection*{\textbf{Opposite direction: starting from $(A,B,C,D)$}}

	\paragraph{\textbf{(I) Universal factorization when $C\neq 0$.}}
	Assume $C\neq 0$. Define
	\[
	\alpha=\frac{A}{C},\qquad
	\delta=\frac{D}{C},\qquad
	\beta=\frac{BC-AD}{C^{2}}.
	\]
	Then the identity
	\[
	\frac{Az+B}{Cz+D}=\alpha+\frac{\beta}{z+\delta}
	\]
	holds. Consequently,
	\[
	f=T_{\alpha}\circ S_{\beta}\circ J\circ T_{\delta},
	\qquad
	T_t(z)=z+t,\quad S_\lambda(z)=\lambda z,\quad J(z)=\frac{1}{z}.
	\]

	\paragraph{\textbf{(II) The affine case $C=0$.}}
	If $C=0$, then
	\[
	f(z)=\frac{Az+B}{D}=\left(\frac{A}{D}\right)z+\left(\frac{B}{D}\right),
	\]
	so $f$ is just a similarity plus a translation.

	\paragraph{\textbf{(III) When is $f$ of the special form $H_{a,r}(z)=a+\dfrac{r^{2}}{z-a}$?}}
	Assume $C\neq 0$. The map $f(z)=\dfrac{Az+B}{Cz+D}$ is of the form
	\[
	H_{a,r}(z)=a+\frac{r^{2}}{z-a}
	\]
	(up to an overall nonzero scalar in the coefficients) exactly when
	\[
	A=-D.
	\]
	In that case one can set
	\[
	a=\frac{A}{C}=-\frac{D}{C},
	\qquad
	r^{2}=\frac{BC-AD}{C^{2}},
	\]
	and then indeed
	\[
	\frac{Az+B}{Cz+D}=a+\frac{r^{2}}{z-a}.
	\]

	\subsection*{\textbf{How this relates to the exercise: why (i) $\Rightarrow$ (ii)}}

	\paragraph{\textbf{Goal of (ii).}}
	We want to prove: every MĂ¶bius map
	\[
	f(z)=\frac{Az+B}{Cz+D}\qquad(AD-BC\neq 0)
	\]
	is a composition of inversions (in circles/lines).

	\paragraph{\textbf{Step 1: (i) provides the explicit inversion map.}}
	From (i), inversion in the circle $|z-a|=r$ is the map
	\[
	I_{a,r}(z)=a+\frac{r^{2}}{\overline{z-a}}.
	\]
	This is a genuine Euclidean circle inversion: it sends $z$ to the unique point $z^{*}$ on the ray from $a$ through $z$
	such that $|z-a|\cdot|z^{*}-a|=r^{2}$.

	\paragraph{\textbf{Step 2: reduce an arbitrary MĂ¶bius map to generators.}}
	If $C\neq 0$, define
	\[
	\alpha=\frac{A}{C},\qquad
	\delta=\frac{D}{C},\qquad
	\beta=\frac{BC-AD}{C^{2}}.
	\]
	Then one checks the identity
	\[
	\frac{Az+B}{Cz+D}=\alpha+\frac{\beta}{z+\delta}.
	\]
	Hence, writing
	\[
	T_t(z)=z+t,\qquad S_\lambda(z)=\lambda z,\qquad J(z)=\frac{1}{z},
	\]
	we obtain the factorization
	\[
	f \;=\; T_{\alpha}\circ S_{\beta}\circ J\circ T_{\delta}.
	\]
	If $C=0$, then $f(z)=\left(\frac{A}{D}\right)z+\left(\frac{B}{D}\right)$ is already a similarity plus translation.

	\paragraph{\textbf{Step 3: realize each generator as a composition of inversions.}}
	We allow inversions in circles and also in lines (lines are circles through $\infty$, i.e.\ reflections).
```

### CP-IV-0084

- chapter line: 1723
- atlas source solution flag: `unknown`
- linked source-solution candidates: `none`
- embedded solution marker in problem body: `NO`

```tex
\par\noindent\textbullet\quad \textbf{Enneper associated family.}
	Take $g(z)=z$ and $f(z)=1$ (on a simply connected domain). Then $f_\theta=e^{-i\theta}$ produces the associated Enneper
	family, all locally isometric for the same reason.

\medskip

Let $D\subset\mathbb C$ be simply connected and let $(f,g)$ be holomorphic data (with $g$ meromorphic in general).
Define the $\mathbb C^3$-valued holomorphic $1$-form
\[
\Phi_{(f,g)}(z)\,dz
=
\Bigl(\tfrac12 f(1-g^2),\ \tfrac{i}{2}f(1+g^2),\ fg\Bigr)\,dz.
\]
The associated minimal immersion is given by
\[
\phi_{(f,g)}(z)=\Re\int^z \Phi_{(f,g)}(\zeta)\,d\zeta.
\]
The choice of $\Phi_{(f,g)}$ ensures $\Phi_{(f,g)}\cdot\Phi_{(f,g)}=0$ (complex bilinear dot product), so the parametrization is
conformal, and holomorphicity implies the coordinate functions are harmonic; hence $\phi_{(f,g)}$ is minimal.

\smallskip
The induced metric (first fundamental form) of $\phi_{(f,g)}$ is conformal:
\[
ds^2
=
2\langle \phi_z,\phi_{\bar z}\rangle\,|dz|^2
=
\frac{|f|^2(1+|g|^2)^2}{4}\,|dz|^2.
\]
In particular, the metric depends only on $|f|$ and $|g|$. Thus multiplying $f$ by a unimodular constant
$e^{-i\theta}$ leaves $ds^2$ unchanged.

\smallskip
Non-uniqueness arises from holomorphic reparametrization.
If $\alpha:W\to D$ is biholomorphic and we reparametrize by $z=\alpha(w)$, then $dz=\alpha'(w)\,dw$ and
$\phi_{(f,g)}\circ\alpha$ is again a Weierstrass immersion with new data
\[
\tilde g(w)=g(\alpha(w)),
\qquad
\tilde f(w)=f(\alpha(w))\,\alpha'(w).
\]
At points where $g'(z_0)\neq 0$, the holomorphic inverse function theorem gives a local inverse $g^{-1}$.
Choosing $\alpha=g^{-1}$ yields $\tilde g=\mathrm{id}$ and $\tilde f=:F$ holomorphic, so locally one may normalize the data to
$(F,\mathrm{id})$ and write the immersion as $\phi_F$.
The family $\phi_{e^{-i\theta}F}$ ($\theta\in\mathbb R$) is called the associated family; since $|e^{-i\theta}F|=|F|$, all
members have the same induced metric and are therefore locally isometric.

\medskip

The Weierstrass data $(f,g)$ encode two geometric ingredients.

\smallskip
\emph{(1) The Gauss map.}
For a conformal minimal immersion $X=\phi_{(f,g)}$, let $N$ be the unit normal field.
The Gauss map is $N:D\to\mathbb S^2$. Composing with stereographic projection
$\sigma:\mathbb S^2\setminus\{(0,0,1)\}\to\mathbb C$ gives a (locally) meromorphic function
\[
g=\sigma\circ N.
\]
Thus $g(z)$ is the normal direction written in a complex coordinate. In particular, constant $g$ means constant normal,
hence $X$ is a plane; nonconstant $g$ corresponds to bending of the surface.

\smallskip
\emph{(2) The holomorphic $1$-form $f\,dz$.}
The differential $f(z)\,dz$ controls the conformal scale of the parametrization. The induced metric is
\[
ds^2=\frac{|f|^2(1+|g|^2)^2}{4}\,|dz|^2,
\]
so $|f|$ (together with $|g|$) determines local lengths on the surface, while the argument of $f$ represents a constant
``phase'' in the complex differential.

\smallskip
\emph{(3) Conformality and minimality.}
The $\mathbb C^3$-valued $1$-form
\[
\Phi_{(f,g)}\,dz
=
\Bigl(\tfrac12 f(1-g^2),\ \tfrac{i}{2}f(1+g^2),\ fg\Bigr)\,dz
\]
is arranged so that the complex derivative satisfies $X_z\cdot X_z=0$, which is the isotropy condition ensuring the
parametrization is conformal. Moreover each coordinate function of $X=\Re\int \Phi$ is harmonic (real part of a holomorphic
function), hence $X$ is minimal.

\smallskip
\emph{(4) Associated family.}
Multiplying $f$ by a unimodular constant $e^{-i\theta}$ rotates the holomorphic differential by a constant phase.
This generally changes the immersion in $\mathbb R^3$, but does not change the metric since $|e^{-i\theta}f|=|f|$.
Therefore $\phi_{e^{-i\theta}F}$ all share the same first fundamental form and are locally isometric.

\medskip

\smallskip
\textbf{Complex coordinate and derivatives.}
Let $z=x+iy$ on a domain $D\subset\mathbb C$. Then $|dz|^2:=dx^2+dy^2$.
We use $\partial_z=\tfrac12(\partial_x-i\partial_y)$ and $\partial_{\bar z}=\tfrac12(\partial_x+i\partial_y)$.

\smallskip
\textbf{Weierstrass $1$-form and immersion.}
Given holomorphic data $(f,g)$ (with $g$ meromorphic in general), define the $\mathbb C^3$-valued holomorphic $1$-form
\[
\Phi_{(f,g)}(z)\,dz
=
\Bigl(\tfrac12 f(1-g^2),\ \tfrac{i}{2}f(1+g^2),\ fg\Bigr)\,dz.
\]
On simply connected $D$, set $\Psi(z):=\int^z \Phi_{(f,g)}(\zeta)\,d\zeta\in\mathbb C^3$ and define the immersion
\[
\phi_{(f,g)}(z)=\Re \Psi(z)\in\mathbb R^3.
\]
We distinguish the \emph{complex bilinear} dot product $a\cdot b=\sum_{j=1}^3 a_j b_j$ from the Hermitian product
$\langle a,b\rangle=\sum_{j=1}^3 a_j\overline{b_j}$.

\smallskip
\textbf{Isotropy $\Phi\cdot\Phi=0$ (conformality).}
Write
\[
\Phi_1=\tfrac12 f(1-g^2),\qquad
\Phi_2=\tfrac{i}{2}f(1+g^2),\qquad
\Phi_3=fg.
\]
Then, using the complex bilinear dot product,
\[
\Phi\cdot\Phi=\Phi_1^2+\Phi_2^2+\Phi_3^2
=
\frac{f^2}{4}(1-g^2)^2-\frac{f^2}{4}(1+g^2)^2+f^2g^2.
\]
Since $(1-g^2)^2-(1+g^2)^2=-4g^2$, it follows that $\Phi\cdot\Phi=0$.
Moreover, $\Psi$ is holomorphic with $\Psi'(z)=\Phi(z)$, hence
\[
\phi_z=\partial_z\Re\Psi=\frac12\Psi'(z)=\frac12\Phi(z),\qquad
\phi_{\bar z}=\frac12\overline{\Phi(z)}.
\]
Therefore $\phi_z\cdot\phi_z=\tfrac14(\Phi\cdot\Phi)=0$, which is the conformality condition.

\smallskip
\textbf{Induced metric.}
In complex notation, the first fundamental form of a conformal immersion is
\[
ds^2 = 2\langle \phi_z,\phi_{\bar z}\rangle\,|dz|^2.
\]
Using $\phi_z=\tfrac12\Phi$ we get
\[
\langle \phi_z,\phi_{\bar z}\rangle
=
\left\langle \tfrac12\Phi,\tfrac12\overline{\Phi}\right\rangle
=
\frac14 \langle \Phi,\overline{\Phi}\rangle
=
\frac14|\Phi|^2,
\]
hence $ds^2=\frac{|\Phi|^2}{2}|dz|^2$, where $|\Phi|^2:=|\Phi_1|^2+|\Phi_2|^2+|\Phi_3|^2$.
Now
\[
|\Phi_1|^2=\frac{|f|^2}{4}|1-g^2|^2,\quad
|\Phi_2|^2=\frac{|f|^2}{4}|1+g^2|^2,\quad
|\Phi_3|^2=|f|^2|g|^2,
\]
so
\[
|\Phi|^2
=
\frac{|f|^2}{4}\Bigl(|1-g^2|^2+|1+g^2|^2+4|g|^2\Bigr).
\]
Expanding gives
\[
|1-g^2|^2+|1+g^2|^2 = 2(1+|g|^4),
\]
hence the bracket equals
\[
2(1+|g|^4)+4|g|^2=2(1+2|g|^2+|g|^4)=2(1+|g|^2)^2.
\]
Therefore
\[
|\Phi|^2=\frac{|f|^2}{2}(1+|g|^2)^2,
\qquad
ds^2=\frac{|\Phi|^2}{2}|dz|^2
=\frac{|f|^2(1+|g|^2)^2}{4}\,|dz|^2.
\]

\smallskip
\textbf{Why minimal.}
Each component $\Psi_k$ is holomorphic and $\phi_k=\Re\Psi_k$ is harmonic, so $\Delta\phi=0$.
For a conformal immersion, $\Delta\phi=2\lambda^2 H$ where $H$ is the mean curvature vector.
Thus $\Delta\phi=0$ implies $H=0$, i.e.\ $\phi$ is minimal.

\medskip

Let $\phi=\phi(x,y)$ be a smooth map into $\mathbb R^3$ and set
\[
E=\langle \phi_x,\phi_x\rangle,\qquad
F=\langle \phi_x,\phi_y\rangle,\qquad
G=\langle \phi_y,\phi_y\rangle,
\]
so that the first fundamental form is
\[
ds^2=E\,dx^2+2F\,dx\,dy+G\,dy^2.
\]
Define complex derivatives
\[
\phi_z=\tfrac12(\phi_x-i\phi_y),\qquad
\phi_{\bar z}=\tfrac12(\phi_x+i\phi_y).
\]
Then
\[
\langle \phi_z,\phi_{\bar z}\rangle
=
\left\langle \tfrac12(\phi_x-i\phi_y),\tfrac12(\phi_x+i\phi_y)\right\rangle
=
\frac14\bigl(\langle \phi_x,\phi_x\rangle+\langle \phi_y,\phi_y\rangle\bigr)
=
\frac{E+G}{4}.
\]
In particular, if $\phi$ is conformal, then $F=0$ and $E=G=\lambda^2$, hence
\[
\langle \phi_z,\phi_{\bar z}\rangle=\frac{\lambda^2}{2},
\qquad\text{and therefore}\qquad
ds^2=\lambda^2(dx^2+dy^2)=\lambda^2|dz|^2
=
2\langle \phi_z,\phi_{\bar z}\rangle\,|dz|^2.
\]

\medskip

With $\phi_z=\tfrac12(\phi_x-i\phi_y)$ we compute
\[
\langle \phi_z,\phi_z\rangle
=
\left\langle \tfrac12(\phi_x-i\phi_y),\tfrac12(\phi_x-i\phi_y)\right\rangle
=
\frac14\Bigl(\langle \phi_x,\phi_x\rangle-\langle \phi_y,\phi_y\rangle-2i\langle \phi_x,\phi_y\rangle\Bigr)
=
\frac{E-G-2iF}{4}.
\]
Hence $\langle \phi_z,\phi_z\rangle=0$ if and only if $E=G$ and $F=0$, i.e.\ if and only if the parametrization is conformal.

\medskip

We want a systematic way to write all conformal minimal immersions
$\phi : D \subset \mathbb{C} \to \mathbb{R}^3$ using holomorphic data.
The Weierstrass representation gives exactly that: two complex functions $(f,g)$ generate the surface.

\medskip
\textbf{1) Start from a minimal immersion and use complex coordinates.}

Let $z = x + iy$ be a complex parameter on $D$. For a smooth map $\phi(x,y) \in \mathbb{R}^3$, define
\[
\phi_z = \frac{1}{2}(\phi_x - i\phi_y),
\qquad
\phi_{\bar z} = \frac{1}{2}(\phi_x + i\phi_y).
\]

A parametrization is \textbf{conformal} if and only if
\[
\langle \phi_x,\phi_x\rangle = \langle \phi_y,\phi_y\rangle,
\qquad
\langle \phi_x,\phi_y\rangle = 0.
\]
Equivalently, in complex form,
\[
\phi_z \cdot \phi_z = 0
\qquad
\text{(complex bilinear dot product).}
\]

A surface is \textbf{minimal} if its coordinate functions are harmonic in conformal parameters, i.e.
\[
\Delta \phi = 0.
\]
In complex notation, $\Delta = 4\,\partial_z \partial_{\bar z}$, so $\Delta \phi = 0$ means
\[
\partial_{\bar z}\phi_z = 0,
\]
i.e.\ $\phi_z$ is holomorphic as a $\mathbb{C}^3$-valued function.

\medskip
So:
\[
\boxed{\text{Minimal + conformal} \ \Longrightarrow\  \phi_z \text{ is a holomorphic } \mathbb{C}^3\text{-valued function satisfying } \phi_z\cdot\phi_z = 0.}
\]

\smallskip
\textbf{2) The holomorphic $1$-form.}
Set
\[
\Phi(z):=2\phi_z(z)\in\mathbb C^3.
\]
Then $\Phi$ is holomorphic and satisfies $\Phi\cdot\Phi=0$.
Since $D$ is simply connected, the integral
\[
\Psi(z)=\int^z \Phi(\zeta)\,d\zeta\in\mathbb C^3
\]
is well-defined (up to an additive constant), and the immersion is recovered by
\[
\phi(z)=\Re\Psi(z)=\Re\int^z \Phi(\zeta)\,d\zeta.
\]

\smallskip
\textbf{3) Introducing $(f,g)$ from $\Phi\cdot\Phi=0$.}
Write $\Phi=(\Phi_1,\Phi_2,\Phi_3)$ with $\Phi_1^2+\Phi_2^2+\Phi_3^2=0$.
On the set where $\Phi_1-i\Phi_2\neq 0$, define
\[
f:=\Phi_1-i\Phi_2,\qquad g:=\frac{\Phi_3}{\Phi_1-i\Phi_2}=\frac{\Phi_3}{f}.
\]
Then $\Phi_3=fg$ and
\[
(\Phi_1-i\Phi_2)(\Phi_1+i\Phi_2)+\Phi_3^2=0
\quad\Longrightarrow\quad
f(\Phi_1+i\Phi_2)+(fg)^2=0
\quad\Longrightarrow\quad
\Phi_1+i\Phi_2=-fg^2.
\]
Hence
\[
\Phi_1=\tfrac12\bigl((\Phi_1-i\Phi_2)+(\Phi_1+i\Phi_2)\bigr)=\tfrac12 f(1-g^2),
\]
\[
\Phi_2=\tfrac{1}{2i}\bigl((\Phi_1+i\Phi_2)-(\Phi_1-i\Phi_2)\bigr)=\tfrac{i}{2} f(1+g^2),
\]
\[
\Phi_3=fg.
\]
Therefore
\[
\Phi_{(f,g)}(z)\,dz
=
\Bigl(\tfrac12 f(1-g^2),\ \tfrac{i}{2}f(1+g^2),\ fg\Bigr)\,dz,
\qquad
\phi_{(f,g)}(z)=\Re\int^z \Phi_{(f,g)}(\zeta)\,d\zeta.
\]
Geometrically, $g$ is the stereographic coordinate of the Gauss map (normal direction), and $f\,dz$
is the holomorphic differential controlling the conformal scale.

\smallskip
\textbf{4) Metric and associated family.}
The induced metric is conformal and equals
\[
ds^2=\frac{|f|^2(1+|g|^2)^2}{4}\,|dz|^2.
\]
In particular $ds^2$ depends only on $|f|$ and $|g|$, so replacing $f$ by $e^{-i\theta}f$ leaves $ds^2$ unchanged.

\smallskip
\textbf{5) Reparametrization.}
If $\alpha:W\to D$ is biholomorphic and $z=\alpha(w)$, then $dz=\alpha'(w)\,dw$ and the pullback gives
new Weierstrass data
\[
\tilde g(w)=g(\alpha(w)),\qquad \tilde f(w)=f(\alpha(w))\,\alpha'(w).
\]

\medskip

\smallskip
\textbf{Complex derivative of a conformal minimal immersion.}
Start with a (conformal) minimal immersion
\[
\phi : D \subset \mathbb{C} \longrightarrow \mathbb{R}^3.
\]
Write $z=x+iy$ and define the complex derivatives
\[
\phi_z=\frac12(\phi_x-i\phi_y)\in\mathbb C^3,
\qquad
\phi_{\bar z}=\frac12(\phi_x+i\phi_y)\in\mathbb C^3.
\]
For a conformal minimal immersion, $\phi_z$ has two key properties:
```

### CP-IV-0089

- chapter line: 2091
- atlas source solution flag: `unknown`
- linked source-solution candidates: `none`
- embedded solution marker in problem body: `NO`

```tex
\par\noindent\textbullet\quad The data $(f,g)$ are two complex functions, hence define a map $(f,g):D\to\mathbb C^2$,
	but $(f,g)$ is \emph{not} the surface. It is the holomorphic data used to build $\Phi$ and then $\phi$.

\medskip
\textbf{One-sentence summary.}
The surface is $\phi:D\subset\mathbb C\to\mathbb R^3$; the complex derivative produces $\Phi=2\phi_z\in\mathbb C^3$ with
$\Phi\cdot\Phi=0$; and the functions $f=\Phi_1-i\Phi_2$ and $g=\Phi_3/f$ encode $\Phi$, with $g$ representing the Gauss map
(stereographic coordinate) and $f\,dz$ controlling the conformal scale.

\medskip

A parametrized surface patch is a smooth map
\[
\phi : D \subset \mathbb R^2 \to \mathbb R^3,\qquad (x,y)\mapsto \phi(x,y).
\]
Hence it has the usual partial derivatives with respect to the two real parameters:
\[
\phi_x(x,y)=\frac{\partial \phi}{\partial x}(x,y),\qquad
\phi_y(x,y)=\frac{\partial \phi}{\partial y}(x,y).
\]
Writing $\phi=(\phi^1,\phi^2,\phi^3)$, these are
\[
\phi_x=\big(\partial_x\phi^1,\partial_x\phi^2,\partial_x\phi^3\big)\in\mathbb R^3,
\qquad
\phi_y=\big(\partial_y\phi^1,\partial_y\phi^2,\partial_y\phi^3\big)\in\mathbb R^3.
\]
If we identify $(x,y)$ with the complex coordinate $z=x+iy$, we often write $\phi(z)$ instead of $\phi(x,y)$; this is only
a change of notation.
The complex derivatives are defined by the linear combinations
\[
\phi_z=\tfrac12(\phi_x-i\phi_y),\qquad
\phi_{\bar z}=\tfrac12(\phi_x+i\phi_y),
\]
which package the two real tangent vectors $\phi_x,\phi_y$ into complex form.

\medskip

A surface is \emph{minimal} if and only if its mean curvature satisfies $H\equiv 0$.
For an immersion $\phi:D\subset\mathbb R^2\to\mathbb R^3$ there is the fundamental identity
\[
\Delta_g \phi = 2H\,N,
\]
where $\Delta_g$ is the Laplace--Beltrami operator of the induced metric $g$ and $N$ is the unit normal.
Thus $H=0$ is equivalent to $\Delta_g\phi=0$.

If $(x,y)$ are \emph{conformal} (isothermal) coordinates, then
\[
g=\lambda^2(dx^2+dy^2)\qquad (E=G=\lambda^2,\;F=0),
\]
and the Laplace--Beltrami operator simplifies to
\[
\Delta_g = \frac{1}{\lambda^2}\Delta,
\qquad
\Delta=\partial_x^2+\partial_y^2.
\]
Substituting into $\Delta_g\phi=2H N$ yields
\[
\frac{1}{\lambda^2}\Delta\phi = 2H N
\quad\Longrightarrow\quad
\Delta\phi = 2\lambda^2 H N.
\]
Hence, for a minimal surface ($H=0$), we obtain $\Delta\phi=0$.

Finally, since $\Delta = 4\,\partial_z\partial_{\bar z}$, the equation $\Delta\phi=0$ implies
\[
\partial_{\bar z}\phi_z=\partial_{\bar z}(\partial_z\phi)=0,
\]
so $\phi_z$ is holomorphic as a $\mathbb C^3$-valued function.

\medskip

Write the immersion as
\[
\phi(x,y)=(\phi^1(x,y),\phi^2(x,y),\phi^3(x,y))\in\mathbb R^3.
\]
Then
\[
\phi_x=(\partial_x\phi^1,\partial_x\phi^2,\partial_x\phi^3)\in\mathbb R^3,
\qquad
\phi_y=(\partial_y\phi^1,\partial_y\phi^2,\partial_y\phi^3)\in\mathbb R^3.
\]
By definition,
\[
\phi_z=\tfrac12(\phi_x-i\phi_y),
\]
so each component is a complex number:
\[
\phi_z=
\left(
\tfrac12(\partial_x\phi^1-i\partial_y\phi^1),\
\tfrac12(\partial_x\phi^2-i\partial_y\phi^2),\
\tfrac12(\partial_x\phi^3-i\partial_y\phi^3)
\right)\in\mathbb C^3.
\]
Thus $\phi$ takes values in $\mathbb R^3$, but its complex derivative $\phi_z$ is a complex linear combination of real
tangent vectors and naturally lives in the complexified space $\mathbb C^3$.

Moreover, saying that $\phi_z$ is \emph{holomorphic as a $\mathbb C^3$-valued function} means
\[
\partial_{\bar z}\phi_z=0,
\]
equivalently $\partial_{\bar z}(\phi_z^k)=0$ for each component $k=1,2,3$.

\medskip

Although $\phi:D\to\mathbb R^3$ is real-valued, its complex derivative
\[
\phi_z=\tfrac12(\phi_x-i\phi_y)
\]
is $\mathbb C^3$-valued. Set
\[
\Phi:=2\phi_z \in \mathbb C^3.
\]
Since $\Phi$ is holomorphic, we can integrate componentwise to obtain a holomorphic map
\[
\Psi(z)=\int^z \Phi(\zeta)\,d\zeta \in \mathbb C^3
\]
(well-defined on simply connected domains, up to an additive constant). The original immersion is then recovered by taking
the real part componentwise:
\[
\phi(z)=\Re \Psi(z)=\Re\int^z \Phi(\zeta)\,d\zeta \in \mathbb R^3.
\]
Thus we \emph{temporarily} work in the complexified space $\mathbb C^3$ to exploit holomorphicity, and then take $\Re$ to
return to a surface in $\mathbb R^3$.

	\medskip
	\textbf{Why $g$ is the Gauss map, but $f$ is not.}

	Let $X=\phi_{(f,g)}:D\subset\mathbb C\to\mathbb R^3$ be a conformal minimal immersion given by the Weierstrass data $(f,g)$:
	\[
	X(z)=\Re\int^z \Phi_{(f,g)}(\zeta)\,d\zeta,
	\qquad
	\Phi_{(f,g)}(z)
	=
	\Bigl(\tfrac12 f(1-g^2),\ \tfrac{i}{2}f(1+g^2),\ fg\Bigr).
	\]
	The induced metric is
	\[
	ds^2=\frac{|f|^2(1+|g|^2)^2}{4}\,|dz|^2.
	\]

	\smallskip
	\textbf{1) The Gauss map and the role of $g$.}
	The \emph{Gauss map} of $X$ is the unit normal field
	\[
	N:D\to \mathbb S^2.
	\]
	Let $\sigma:\mathbb S^2\setminus\{(0,0,1)\}\to\mathbb C$ be stereographic projection. A fundamental fact of the Weierstrass
	representation is that
	\[
	g=\sigma\circ N,
	\]
	so $g$ is (locally) the complex coordinate of the normal direction. Equivalently, $N$ can be recovered from $g$ by inverse
	stereographic projection:
	\[
	N
	=
	\frac{1}{1+|g|^2}\,\bigl(2\Re g,\ 2\Im g,\ |g|^2-1\bigr).
	\]
	Thus \emph{$g$ encodes the direction of the unit normal}, i.e.\ the Gauss map.

	\smallskip
	\textbf{2) The role of $f$ (conformal scale, not normals).}
	The function $f$ is \emph{not} a Gauss map. It controls the conformal scale of the parametrization via the metric:
	\[
	ds^2=\frac{|f|^2(1+|g|^2)^2}{4}\,|dz|^2.
	\]
	In particular, $|f|$ determines local lengths in the parameter domain (together with $|g|$), while the argument of $f$ is a
	constant ``phase'' in the holomorphic differential. There is no formula expressing $N$ purely in terms of $f$.

	\smallskip
	\textbf{3) Why it may look like ``both are Gauss maps'' after a reparametrization.}
	Non-uniqueness comes from biholomorphic reparametrization. If $\alpha:W\to D$ is biholomorphic, then
	$X\circ\alpha$ is again a Weierstrass immersion with new data
	\[
	\tilde g(w)=g(\alpha(w)),
	\qquad
	\tilde f(w)=f(\alpha(w))\,\alpha'(w).
	\]
	If $g'(z_0)\neq 0$, then $g$ has a local holomorphic inverse $g^{-1}$ near $z_0$. Choosing $\alpha=g^{-1}$ gives
	\[
	\tilde g(w)=g(g^{-1}(w))=w=\mathrm{id}(w),
	\qquad
	\tilde f(w)=f(g^{-1}(w))\,(g^{-1})'(w)=:F(w).
	\]
	So locally we may normalize the data to $(F,\mathrm{id})$. This does \emph{not} mean that $F$ is a Gauss map; it only means we
	chose coordinates so that the Gauss-map coordinate becomes the parameter $w$ itself.

	\smallskip
	\textbf{Summary.}
	\[
	\boxed{\text{$g$ is (stereographic) Gauss map data, while $f\,dz$ controls the conformal scale of the immersion.}}
	\]

	\medskip
	\noindent
	\textbf{Idea (one picture).}
	The Weierstrass pair $(f,g)$ is not unique because we may reparametrize the domain by any biholomorphic map
	$\alpha:W\to D$ (change of complex coordinate). Under $z=\alpha(w)$, the same minimal immersion can be written again in
	Weierstrass form with new data
	\[
	\tilde g(w)=g(\alpha(w)),\qquad \tilde f(w)=f(\alpha(w))\,\alpha'(w).
	\]
	At a regular point $z_0$ of $g$ (where $g'(z_0)\neq 0$), the holomorphic inverse function theorem allows us to choose
	$\alpha=g^{-1}$ locally, which normalizes the Gauss-map coordinate to $\tilde g=\mathrm{id}$ and leaves only one holomorphic
	function $F:=\tilde f$. In this normalized form $(F,\mathrm{id})$, multiplying $F$ by a unimodular constant
	$e^{-i\theta}$ rotates the complex differential by a constant phase but does not change its modulus; hence the induced metric
	\[
	ds^2=\frac{|F|^2(1+|z|^2)^2}{4}\,|dz|^2
	\]
	is unchanged. Therefore the associated family $\{\phi_{e^{-i\theta}F}\}_{\theta\in\mathbb R}$ consists of locally isometric
	minimal surfaces.
	\medskip

	\medskip
	\noindent
	\textbf{Geometric meaning of $g$ (Gauss map in complex coordinates).}
	For a conformal minimal immersion $\phi:D\to\mathbb R^3$, let $N:D\to\mathbb S^2$ be the unit normal (Gauss map).
	Stereographic projection $\sigma:\mathbb S^2\setminus\{N_0\}\to\mathbb C$ (from the north pole $N_0=(0,0,1)$) identifies
	$\mathbb S^2$ (minus one point) with the complex plane. The Weierstrass function $g$ is precisely this normal direction
	written as a complex number:
	\[
	g=\sigma\circ N.
	\]
	Thus $g$ encodes how the surface bends (how the normal changes), while $f\,dz$ controls the conformal scale; the induced
	metric is
	\[
	ds^2=\frac{|f|^2(1+|g|^2)^2}{4}\,|dz|^2,
	\]
	so the modulus $|f|$ matters for lengths, whereas a constant phase factor $e^{-i\theta}$ does not change $ds^2$.
	\medskip

	\medskip
	\noindent
	\textbf{Bidirectional view: $g$ encodes the unit normal.}
	Stereographic projection $\sigma:\mathbb S^2\setminus\{N_0\}\to\mathbb C$ identifies (almost all of) the unit sphere with
	the complex plane. For a conformal immersion $\phi$, the Gauss map $N:D\to\mathbb S^2$ gives the unit normal, and
	\[
	g=\sigma\circ N
	\]
	is exactly that normal direction written as a complex number. Conversely, $g$ determines the unit normal by inverse
	stereographic projection:
	\[
	N=\sigma^{-1}(g)=\frac{1}{1+|g|^2}\bigl(2\Re g,\ 2\Im g,\ |g|^2-1\bigr)\in\mathbb S^2.
	\]
	\medskip

	\clearpage
```

### CP-IV-0096

- chapter line: 2427
- atlas source solution flag: `unknown`
- linked source-solution candidates: `none`
- embedded solution marker in problem body: `NO`

```tex
\par\noindent\textbullet\quad Suppose $f(1/n)=1/(n+1)$ for all $n$. Then
	\[
	h(z):=f(z)-\frac{z}{z+1}
	\]
	is holomorphic on $D(0,2)\setminus\{-1\}$, vanishes at $z=1/n$ for all $n$, and the set $\{1/n\}$ accumulates at $0$ in that domain.
	By the identity theorem, $h\equiv 0$ there, i.e.\ $f(z)=\dfrac{z}{z+1}$ on $D(0,2)\setminus\{-1\}$.
	But $\dfrac{z}{z+1}$ has a pole at $z=-1$, whereas $f$ is holomorphic there â€” a contradiction.
	Hence some $n$ satisfies $f(1/n)\ne 1/(n+1)$.

\bigskip
```

### CP-IV-0097

- chapter line: 2441
- atlas source solution flag: `unknown`
- linked source-solution candidates: `none`
- embedded solution marker in problem body: `NO`

```tex
(Real shear).

Let $T$ have real matrix $\begin{psmallmatrix}1&1\\ 0&1\end{psmallmatrix}$.
By the formulas,
\[
A=\frac{1+1}{2}+i\,\frac{0-1}{2}=1-\tfrac{i}{2},\qquad
B=\frac{1-1}{2}+i\,\frac{0+1}{2}=\tfrac{i}{2}.
\]
The image of the unit circle is an ellipse tilted by the shear. Since $B\neq0$, $T$ is not holomorphic.
The Jacobian is $|A|^2-|B|^2=(1^2+(\tfrac12)^2)-(\tfrac12)^2=1>0$, so orientation is preserved.
```

### CP-IV-0102

- chapter line: 2455
- atlas source solution flag: `unknown`
- linked source-solution candidates: `none`
- embedded solution marker in problem body: `NO`

```tex
automorphism of the upper half-plane

Consider the M\"obius transformation
	\[
	T(z) = \frac{z-1}{z+1}.
	\]
	We work on the upper half-plane
	\[
	H = \{ z : \Im z > 0 \}
	\]
	with boundary the extended real line
	\[
	L = \mathbb R \cup \{\infty\}.
	\]

	Writing $z=x+iy$ with $y>0$, a direct computation yields
	\[
	\Im T(z)
	= \Im\!\left(\frac{z-1}{z+1}\right)
	= \frac{\Im z}{|z+1|^2}
	= \frac{y}{|z+1|^2} > 0.
	\]
	Hence
	\[
	\Im z > 0 \quad\Longleftrightarrow\quad \Im T(z) > 0,
	\]
	so $T$ is a non-affine automorphism of the upper half-plane and maps
	$L$ to itself.

	Along the boundary $L$ we have:
	\[
	T(1) = \frac{1-1}{1+1} = 0, \qquad
	T(-1) = \frac{-1-1}{-1+1} = \infty, \qquad
	T(\infty) = \lim_{z\to\infty}\frac{z-1}{z+1} = 1.
	\]
	Thus, in the three-point normalization language we may choose
	\[
	a = 1, \quad b = -1, \quad c = \infty
	\quad\text{on } L_1 = L,
	\]
	and
	\[
	A = 0, \quad B = \infty, \quad C = 1
	\quad\text{on } L_2 = L.
	\]
	Then $T$ is exactly the M\"obius map sending
	\[
	a \mapsto A,\qquad b \mapsto B,\qquad c \mapsto C,
	\]
	i.e.
	\[
	1 \mapsto 0,\qquad -1 \mapsto \infty,\qquad \infty \mapsto 1.
	\]

	When one of the boundary points is $\infty$, the cross-ratio formula
	simplifies: for $(a,b,c)=(1,-1,\infty)$ we have
	\[
	\Phi(z) = \frac{(z-a)(c-b)}{(z-b)(c-a)}
	= \frac{(z-1)}{(z+1)},
	\]
	so in this case $T(z) = \Phi(z)$ is precisely the three-point
	normalization carrying $(1,-1,\infty)$ to $(0,\infty,1)$ on the same
	boundary line.

	Figures~\ref{fig:hp-auto-z} and \ref{fig:hp-auto-w} illustrate the
	action of $T$ on the upper half-plane.
\begin{figure}[ht]
  \centering
  \includegraphics[width=0.78\textwidth]{figures/part04/cp_iv_0102_hp_auto_z_plane.png}
  \caption{Half-plane automorphism: source \(z\)-plane.}
  \label{fig:hp-auto-z}
\end{figure}

\begin{figure}[ht]
  \centering
  \includegraphics[width=0.78\textwidth]{figures/part04/cp_iv_0102_hp_auto_w_plane.png}
  \caption{Half-plane automorphism: image \(w\)-plane.}
  \label{fig:hp-auto-w}
\end{figure}


	Let
	\[
	H_1 = \{ z : \Im z > 0 \}, \qquad L_1 = \mathbb R,
	\]
	and
	\[
	H_2 = \{ w : \Re w > 1 \}, \qquad
	L_2 = \{ w : \Re w = 1 \}.
	\]

	Choose boundary triples
	\[
	a = -1,\quad b = 0,\quad c = 2 \in L_1,
	\]
	\[
	A = 1-i,\quad B = 1,\quad C = 1+i \in L_2,
	\]
	listed in the same cyclic order (bottom to top).

	The cross-ratio map sending $L_1$ to the real axis is
	\[
	\Phi(z)
	= \frac{(z-a)(c-b)}{(z-b)(c-a)}
	= \frac{2(z+1)}{3z},
	\]
	so that $\Phi(a)=0$, $\Phi(b)=\infty$, $\Phi(c)=1$.
	Similarly, the map sending $L_2$ to the real axis is
	\[
	\Psi(w)
	= \frac{(w-A)(C-B)}{(w-B)(C-A)}
	= \frac{w-1+i}{2(w-1)},
	\]
	for which $\Psi(A)=0$, $\Psi(B)=\infty$, $\Psi(C)=1$.

	The desired map $T : H_1 \to H_2$ is defined by
	\[
	\Psi(T(z)) = \Phi(z),
	\]
	i.e.\ $T(z) = \Psi^{-1}(\Phi(z))$. Solving $\Psi(w)=\xi$ for $w$ gives
	\[
	\Psi^{-1}(\xi) = \frac{2\xi - 1 + i}{2\xi - 1},
	\]
	and hence
	\[
	T(z)
	= \frac{2\Phi(z) - 1 + i}{2\Phi(z) - 1},
	\qquad
	\Phi(z) = \frac{2(z+1)}{3z}.
	\]
	Then
	\[
	T(-1) = 1-i,\qquad T(0) = 1,\qquad T(2) = 1+i,
	\]
	and $T$ maps the upper half-plane $\Im z>0$ biholomorphically onto the
	half-plane $\Re w>1$.

	Figures~\ref{fig:hp-h1h2-z} and \ref{fig:hp-h1h2-w}
	illustrate this non-automorphism half-plane map.
```

### CP-IV-0106

- chapter line: 2612
- atlas source solution flag: `unknown`
- linked source-solution candidates: `none`
- embedded solution marker in problem body: `NO`

```tex
(restated)

Let $\Gamma$ be a simple smooth positively oriented closed curve in the plane, and let $f$ be continuously differentiable on $\Gamma$.
Define, for $z\in\mathbb{C}\setminus\Gamma$,
\[
F(z):=\frac{1}{2\pi i}\int_{\Gamma}\frac{f(\zeta)}{\zeta-z}\,d\zeta .
\]
This integral diverges when $z$ approaches a point $\zeta_0\in\Gamma$ with $f(\zeta_0)\neq 0$.
Define the principal value at $\zeta_0$ by
\[
\operatorname{P.V.}\,\frac{1}{2\pi i}\int_{\Gamma}\frac{f(\zeta)}{\zeta-\zeta_0}\,d\zeta
\;:=\;
\lim_{\varepsilon\to 0^+}\frac{1}{2\pi i}
\int_{\Gamma_\varepsilon}\frac{f(\zeta)}{\zeta-\zeta_0}\,d\zeta,
\]
where $\Gamma_\varepsilon$ is $\Gamma$ with a small open arc of radius $\varepsilon$ around $\zeta_0$ removed (the remaining part is traversed with the original orientation).

\bigskip\hrule\bigskip

For $z\notin\Gamma$ the integrand is continuous on $\Gamma$ and the function $F$ is well defined and holomorphic in each of the two components of $\mathbb{C}\setminus\Gamma$ (the interior and the exterior).
Differentiation under the integral sign gives
\[
F'(z)=\frac{1}{2\pi i}\int_{\Gamma}\frac{f(\zeta)}{(\zeta-z)^2}\,d\zeta,
\qquad z\in\mathbb{C}\setminus\Gamma.
\]

If $f$ extends to a function holomorphic in the interior of $\Gamma$ and continuous on $\overline{\mathrm{int}(\Gamma)}$, then the Cauchy integral formula yields
\[
F(z)=f(z)\quad\text{for }z\text{ in the interior of }\Gamma,
\qquad
F(z)=0\quad\text{for }z\text{ in the exterior and }|z|\ \text{large}.
\]

At $z=\zeta_0\in\Gamma$ the kernel $(\zeta-\zeta_0)^{-1}$ has a simple pole on the contour.
The principal value extracts the finite, symmetric part of the singular integral by removing a small arc around the pole and letting its size shrink to $0$.

\bigskip\hrule\bigskip

Let $F^\pm(\zeta_0)$ denote the limits of $F(z)$ as $z\to\zeta_0\in\Gamma$
from the interior $(+)$ and from the exterior $(-)$ along nontangential approaches.
If $f\in C^1(\Gamma)$, then these limits exist and
\[
\boxed{
\begin{aligned}
F^{+}(\zeta_0) &= \frac{1}{2}\,f(\zeta_0)
\;+\;\operatorname{P.V.}\,\frac{1}{2\pi i}\int_{\Gamma}\frac{f(\zeta)}{\zeta-\zeta_0}\,d\zeta,\\[6pt]
F^{-}(\zeta_0) &= -\frac{1}{2}\,f(\zeta_0)
\;+\;\operatorname{P.V.}\,\frac{1}{2\pi i}\int_{\Gamma}\frac{f(\zeta)}{\zeta-\zeta_0}\,d\zeta.
\end{aligned}}
\]
Consequently,
\[
\boxed{\,F^{+}(\zeta_0)-F^{-}(\zeta_0)=f(\zeta_0)\,}
\qquad\text{and}\qquad
\boxed{\,\frac{F^{+}(\zeta_0)+F^{-}(\zeta_0)}{2}
=\operatorname{P.V.}\,\frac{1}{2\pi i}\int_{\Gamma}\frac{f(\zeta)}{\zeta-\zeta_0}\,d\zeta.}
\]

\bigskip

Fix $\zeta_0\in\Gamma$ and replace a small arc of $\Gamma$ near $\zeta_0$ by a circle of radius $\varepsilon$ centered at $\zeta_0$, lying inside (for $F^+$) or outside (for $F^-$) the domain. Then
\[
F(z)=\frac{1}{2\pi i}\!\!\int_{\Gamma_\varepsilon}\!\!\frac{f(\zeta)}{\zeta-z}\,d\zeta
\;+\;\frac{1}{2\pi i}\!\!\int_{C_\varepsilon}\!\!\frac{f(\zeta)}{\zeta-z}\,d\zeta,
\]
where $C_\varepsilon$ is the small circular arc. Let $z\to\zeta_0$ from the chosen side.
The first integral tends to the principal value term.
On $C_\varepsilon$, write $f(\zeta)=f(\zeta_0)+o(1)$ and compute
\[
\frac{1}{2\pi i}\int_{C_\varepsilon}\frac{f(\zeta_0)}{\zeta-\zeta_0}\,d\zeta
=\pm\frac{1}{2}f(\zeta_0),
\]
with the sign $+$ for the inner indentation and $-$ for the outer one (by orientation).
Adding the contributions yields the two Plemelj formulas above.

\bigskip\hrule\bigskip

\par\noindent\textbullet\quad The regularity assumption $f\in C^1(\Gamma)$ can be weakened (e.g.\ H\"older continuity suffices for the nontangential limits).
\par\noindent\textbullet\quad If $\Gamma$ is a line, these formulas reduce to the classical Hilbert transform jump relations.
\par\noindent\textbullet\quad Orientation matters: reversing the orientation of $\Gamma$ switches the signs in the $\pm\tfrac12 f(\zeta_0)$ terms.

Let $\Gamma=\{\zeta:|\zeta|=1\}$ (counterclockwise) and $f(\zeta)=\zeta^{m}$ with $m\in\mathbb{Z}_{\ge0}$.
Define
\[
F(z)=\frac{1}{2\pi i}\int_{|\zeta|=1}\frac{\zeta^{m}}{\zeta-z}\,d\zeta,\qquad z\in\mathbb{C}\setminus\Gamma.
\]

\emph{Inside/outside values.}
By Cauchyâ€™s integral formula, if $|z|<1$ then $F(z)=z^{m}$, while if $|z|>1$ then $F(z)=0$.
Thus $F$ is analytic on each side of $\Gamma$, equals $z^{m}$ in the interior, and vanishes in the exterior.

\medskip

\emph{Boundary limits and principal value.}
For $\zeta_{0}\in\Gamma$, the Sokhotski--Plemelj formulas yield
\[
F^{+}(\zeta_{0})
=\frac{1}{2}\zeta_{0}^{m}
+\operatorname{P.V.}\,\frac{1}{2\pi i}\!\int_{|\zeta|=1}\frac{\zeta^{m}}{\zeta-\zeta_{0}}\,d\zeta,
\qquad
F^{-}(\zeta_{0})
=-\frac{1}{2}\zeta_{0}^{m}
+\operatorname{P.V.}\,\frac{1}{2\pi i}\!\int_{|\zeta|=1}\frac{\zeta^{m}}{\zeta-\zeta_{0}}\,d\zeta.
\]
Since $F^{+}(\zeta_{0})=\zeta_{0}^{m}$ and $F^{-}(\zeta_{0})=0$, it follows that
\[
\boxed{\ \operatorname{P.V.}\,\frac{1}{2\pi i}\!\int_{|\zeta|=1}\frac{\zeta^{m}}{\zeta-\zeta_{0}}\,d\zeta
=\frac{1}{2}\,\zeta_{0}^{m}\ },
\qquad
\boxed{\ F^{+}(\zeta_{0})-F^{-}(\zeta_{0})=\zeta_{0}^{m}=f(\zeta_{0})\ }.
\]

\medskip

\emph{Special case $m=0$.}
For $f(\zeta)\equiv 1$ we have $F(z)=1$ for $|z|<1$ and $F(z)=0$ for $|z|>1$, and on $\Gamma$,
\[
F^{+}(\zeta_{0})=1,\qquad F^{-}(\zeta_{0})=0,\qquad
\operatorname{P.V.}\,\frac{1}{2\pi i}\!\int_{|\zeta|=1}\frac{1}{\zeta-\zeta_{0}}\,d\zeta=\frac{1}{2}.
\]

\paragraph{Inside/outside values (unit circle \(\Gamma=\{|\zeta|=1\}\)).}
Consider
\[
F(z)=\frac{1}{2\pi i}\int_{|\zeta|=1}\frac{\zeta^{m}}{\zeta-z}\,d\zeta,
\qquad m\in\mathbb{Z}_{\ge 0}.
\]

\emph{Case \(|z|<1\) (pole inside).}
As a function of \(\zeta\), the integrand has a simple pole at \(\zeta=z\) lying inside \(\Gamma\).
By Cauchyâ€™s integral formula,
\[
\frac{1}{2\pi i}\int_{|\zeta|=1}\frac{\zeta^{m}}{\zeta-z}\,d\zeta
=\zeta^{m}\big|_{\zeta=z}
=z^{m}.
\]
Equivalently, \(\operatorname{Res}_{\zeta=z}\frac{\zeta^{m}}{\zeta-z}=z^{m}\), so the integral is \(2\pi i\,z^{m}\), and dividing by \(2\pi i\) yields \(F(z)=z^{m}\).

\medskip

\emph{Case \(|z|>1\) (no pole inside).}
Now the pole \(\zeta=z\) lies outside \(\Gamma\), hence the integrand is holomorphic on and inside the contour.
By Cauchyâ€™s theorem,
\[
\frac{1}{2\pi i}\int_{|\zeta|=1}\frac{\zeta^{m}}{\zeta-z}\,d\zeta=0,
\quad\text{i.e. }\; F(z)=0.
\]

\medskip

\emph{Series check for \(|z|>1\) (optional).}
For \(|z|>1\),
\[
\frac{\zeta^{m}}{\zeta-z}
=-\frac{1}{z}\,\frac{\zeta^{m}}{1-\zeta/z}
=-\frac{1}{z}\sum_{k=0}^{\infty}\frac{\zeta^{m+k}}{z^{k}}
\quad\big(|\zeta/z|<1\big).
\]
Integrating termwise over \(|\zeta|=1\) gives \(\displaystyle \oint \zeta^{n}\,d\zeta=0\) for all \(n\neq -1\),
so the whole integral is \(0\), confirming \(F(z)=0\) outside.
```

### CP-IV-0116

- chapter line: 2778
- atlas source solution flag: `unknown`
- linked source-solution candidates: `none`
- embedded solution marker in problem body: `NO`

```tex
(Rotationâ€“scaling; holomorphic).

Let $T(z)=\lambda z$ with $\lambda=1.3 e^{i\pi/6}$. Then $A=\lambda$, $B=0$.
The image of the unit circle is a circle of radius $1.3$ rotated by $\pi/6$, and $T$ preserves angles and orientation.
```

### CP-IV-0129

- chapter line: 2904
- atlas source solution flag: `unknown`
- linked source-solution candidates: `none`
- embedded solution marker in problem body: `NO`

```tex
\par\noindent\textbullet\quad \textbf{Pole:} $|f(z)|\to\infty$ as $z\to a$; equivalently, $(z-a)^m f(z)$ extends holomorphically with nonzero value at $a$ for some $m\in\mathbb N$.
```

### CP-IV-0134

- chapter line: 2931
- atlas source solution flag: `unknown`
- linked source-solution candidates: `none`
- embedded solution marker in problem body: `NO`

```tex
\par\noindent\textbullet\quad \textbf{Isotropic:} conformality is equivalent to
	\[
	\phi_z\cdot \phi_z = 0
	\qquad\text{(complex bilinear dot product).}
	\]

\smallskip
\textbf{The holomorphic $\mathbb C^3$-valued $1$-form.}
Now set
\[
\Phi := 2\phi_z \in \mathbb C^3.
\]
Then $\Phi$ is a holomorphic map into $\mathbb C^3$ satisfying $\Phi\cdot \Phi=0$.
The $1$-form $\Phi\,dz$ is the holomorphic $\mathbb C^3$-valued form that one integrates to recover $\phi$:
\[
\Psi(z)=\int^z \Phi(\zeta)\,d\zeta \in \mathbb C^3,
\qquad
\phi(z)=\Re \Psi(z)\in \mathbb R^3.
\]

\smallskip
\textbf{Geometric meaning.}
The function $g$ is (up to stereographic projection) the Gauss map: it encodes the unit normal direction
$N\in\mathbb S^2$. Concretely,
\[
N
=
\frac{1}{1+|g|^2}\,\bigl(2\Re g,\ 2\Im g,\ |g|^2-1\bigr),
\]
which is inverse stereographic projection from $g\in\mathbb C$ to $N\in\mathbb S^2$.
The holomorphic $1$-form $f\,dz$ controls the conformal scale; the induced metric is
\[
ds^2
=
\frac{|f|^2(1+|g|^2)^2}{4}\,|dz|^2.
\]
Thus $|f|$ (together with $|g|$) determines local lengths; multiplying $f$ by $e^{-i\theta}$ rotates the differential but
does not change the metric.

\smallskip
\textbf{Clarifying the target spaces ($\mathbb C^3$ vs.\ $\mathbb R^3$ vs.\ $\mathbb C^2$).}
```

### CP-IV-0024

- chapter line: 2980
- atlas source solution flag: `unknown`
- linked source-solution candidates: `none`
- embedded solution marker in problem body: `NO`

```tex
Consider the meromorphic function
	\[
	F(z) = \frac{1}{1+z^2} \frac{\cos[(\pi-\theta)z]}{2\sin(\pi z)}.
	\]

	The poles occur at $z=\pm i$ and $z=n$, $n\in\mathbb{Z}$.
	At $z=\pm i$:
	\[
	\operatorname{Res}[F,\pm i] = -\frac{\cosh(\pi-\theta)}{4\sinh \pi}.
	\]
	At $z=n\in\mathbb{Z}$:
	\[
	\operatorname{Res}[F,n] = \frac{\cos(n\theta)}{2\pi(1+n^2)}.
	\]

	\subsection*{b) The contour $\Gamma^{(N)}$}
	Define
	\[
	\Gamma^{(N)}_1(t) = \Big(N+\tfrac{1}{2}\Big)(1+it), \quad -1\leq t\leq 1,
	\]
	\[
	\Gamma^{(N)}_2(t) = \Big(N+\tfrac{1}{2}\Big)(-t+i), \quad -1\leq t\leq 1,
	\]
	\[
	\Gamma^{(N)}_3(t) = \Big(N+\tfrac{1}{2}\Big)(-1-it), \quad -1\leq t\leq 1,
	\]
	\[
	\Gamma^{(N)}_4(t) = \Big(N+\tfrac{1}{2}\Big)(t-i), \quad -1\leq t\leq 1.
	\]
	Then $\Gamma^{(N)}$ is the closed square contour with vertices
	$\pm(N+\tfrac{1}{2}) \pm i(N+\tfrac{1}{2})$.
	It encloses the poles at $\pm i$ and all integers $n$ with $|n|\leq N$.

	On $\Gamma^{(N)}$, $|z|\sim N$, so $|F(z)|=O(1/N^2)$.
	Since the contour has length $O(N)$, we obtain
	\[
	\left| \int_{\Gamma^{(N)}} F(z)\,dz \right| \leq \frac{C}{N},
	\]
	for some constant $C$ independent of $N$.

	By Cauchy's residue theorem,
	\[
	\int_{\Gamma^{(N)}} F(z)\,dz
	= 2\pi i \left( \operatorname{Res}[F,i]+\operatorname{Res}[F,-i] + \sum_{n=-N}^N \operatorname{Res}[F,n]\right).
	\]
	Hence
	\[
	\left| \frac{\cosh(\pi-\theta)}{2\sinh \pi}
	- \sum_{n=-N}^N \frac{\cos(n\theta)}{1+n^2} \right| \leq \frac{C}{N}.
	\]
	Letting $N\to\infty$, we conclude
	\[
	\frac{\cosh(\pi-\theta)}{2\sinh \pi}
	= \sum_{n=-\infty}^\infty \frac{e^{in\theta}}{1+n^2}.
	\]

	This gives the Fourier series expansion, uniformly in $\theta$.
```

### CP-IV-0025

- chapter line: 3043
- atlas source solution flag: `unknown`
- linked source-solution candidates: `none`
- embedded solution marker in problem body: `NO`

```tex
Classify the singularities of
\[
\frac{z}{\sin z},\qquad
\sin\!\Big(\frac{\pi}{z^{2}}\Big),\qquad
\frac{1}{z^{2}}+\frac{1}{z^{2}+1},\qquad
\frac{1}{z^{2}}\cos\!\Big(\frac{\pi z}{z+1}\Big).
\]

At an isolated singularity $a$, if the Laurent expansion
$f(z)=\sum_{k=-m}^{\infty} c_k (z-a)^k$ has
(i) $m=0$ $\Rightarrow$ removable;
(ii) finitely many negative terms with highest $(z-a)^{-m}$ $\Rightarrow$ pole of order $m$;
(iii) infinitely many negative terms $\Rightarrow$ essential.

\medskip
\emph{(1) $\boldsymbol{z/\sin z}$.}
Near $0$, $\sin z=z-\frac{z^{3}}{6}+O(z^{5})$, so
\[
\frac{z}{\sin z}=1+\frac{z^{2}}{6}+O(z^{4}),
\]
hence $z=0$ is \textbf{removable} (define value $1$). At $z=n\pi$, $n\in\mathbb Z\setminus\{0\}$,
$\sin z$ has simple zeros and the numerator is nonzero, so each $n\pi$ is a \textbf{simple pole}.

\medskip
\emph{(2) $\boldsymbol{\sin(\pi/z^{2})}$.}
Using $\sin w=\sum_{k\ge0}\frac{(-1)^k w^{2k+1}}{(2k+1)!}$ with $w=\pi/z^{2}$,
\[
\sin\!\Big(\frac{\pi}{z^{2}}\Big)=\sum_{k=0}^{\infty}\frac{(-1)^k \pi^{2k+1}}{(2k+1)!}\,z^{-4k-2},
\]
which contains infinitely many negative powers. Thus $z=0$ is an \textbf{essential singularity}.
There are no other singularities.

\medskip
\emph{(3) $\boldsymbol{1/z^{2} + 1/(z^{2}+1)}$.}
At $z=0$ one has a \textbf{pole of order $2$}. At $z=\pm i$ (simple zeros of $z^{2}+1$) there are
\textbf{simple poles}. No other singularities occur.

\medskip
\emph{(4) $\boldsymbol{z^{-2}\cos\!\big(\pi z/(z+1)\big)}$.}
Let $h(z)=\dfrac{\pi z}{z+1}$.
Near $z=0$, $h(z)=\pi(z-z^{2}+z^{3}-\cdots)$, hence
\[
\cos h(z)=1-\tfrac12 h(z)^{2}+O(z^{3})=1-\tfrac{\pi^{2}}{2}z^{2}+O(z^{3}),
\]
and
\[
\frac{1}{z^{2}}\cos h(z)=\frac{1}{z^{2}}-\frac{\pi^{2}}{2}+O(z),
\]
so $z=0$ is a \textbf{pole of order $2$}. At $z=-1$, $h$ has a simple pole; since
$\cos w=\tfrac12(e^{iw}+e^{-iw})$, composition with a pole yields an \textbf{essential singularity}
at $z=-1$. There are no other singularities.
```

### CP-IV-0048

- chapter line: 3146
- atlas source solution flag: `unknown`
- linked source-solution candidates: `none`
- embedded solution marker in problem body: `NO`

```tex
â€” area from a $1$-form (what $\tfrac12(x\,dy-y\,dx)$ measures)

Set
\[
\alpha \;=\; \frac12\,(x\,dy - y\,dx).
\]
Then
\[
d\alpha
=
\frac12\,(dx\wedge dy + dy\wedge dx)
=
dx\wedge dy.
\]
Hence, by Stokes/Green,
\[
\oint_{C} \alpha
=
\iint_{D} dx\wedge dy
=
\operatorname{Area}(D)
=
\pi R^2.
\]
Therefore,
\[
\boxed{\ \frac12 \oint_{C} (x\,dy - y\,dx)\;=\;\operatorname{Area}(D)\;=\;\pi R^2\ }.
\]

	\par\noindent\textbullet\quad Pick $\mathbf F=(L,M)$ $\Rightarrow$ $1$-form $L\,dx+M\,dy$.
	\par\noindent\textbullet\quad Circulation (line integral on $C$) equals total curl over $D$.
	\par\noindent\textbullet\quad If $\;M_x-L_y\equiv 0$ on $D$, then $\displaystyle \oint_{C}(L\,dx+M\,dy)=0$ (path-independence on simply connected $D$).
	\par\noindent\textbullet\quad The special $1$-form $\tfrac12(x\,dy - y\,dx)$ integrates to the enclosed area.
```

### CP-IV-0053

- chapter line: 3183
- atlas source solution flag: `unknown`
- linked source-solution candidates: `none`
- embedded solution marker in problem body: `NO`

```tex
Consider the meromorphic function
\[
F(z) = \frac{1}{1+z^2} \frac{\cos[(\pi-\theta)z]}{2\sin(\pi z)}.
\]

The poles occur at $z=\pm i$ and $z=n$, $n\in\mathbb{Z}$.
At $z=\pm i$:
\[
\operatorname{Res}[F,\pm i] = -\frac{\cosh(\pi-\theta)}{4\sinh \pi}.
\]
At $z=n\in\mathbb{Z}$:
\[
\operatorname{Res}[F,n] = \frac{\cos(n\theta)}{2\pi(1+n^2)}.
\]

\subsection*{b) The contour $\Gamma^{(N)}$}
Define
\[
\Gamma^{(N)}_1(t) = \Big(N+\tfrac{1}{2}\Big)(1+it), \quad -1\leq t\leq 1,
\]
\[
\Gamma^{(N)}_2(t) = \Big(N+\tfrac{1}{2}\Big)(-t+i), \quad -1\leq t\leq 1,
\]
\[
\Gamma^{(N)}_3(t) = \Big(N+\tfrac{1}{2}\Big)(-1-it), \quad -1\leq t\leq 1,
\]
\[
\Gamma^{(N)}_4(t) = \Big(N+\tfrac{1}{2}\Big)(t-i), \quad -1\leq t\leq 1.
\]
Then $\Gamma^{(N)}$ is the closed square contour with vertices
$\pm(N+\tfrac{1}{2}) \pm i(N+\tfrac{1}{2})$.
It encloses the poles at $\pm i$ and all integers $n$ with $|n|\leq N$.

On $\Gamma^{(N)}$, $|z|\sim N$, so $|F(z)|=O(1/N^2)$.
Since the contour has length $O(N)$, we obtain
\[
\left| \int_{\Gamma^{(N)}} F(z)\,dz \right| \leq \frac{C}{N},
\]
for some constant $C$ independent of $N$.

By Cauchy's residue theorem,
\[
\int_{\Gamma^{(N)}} F(z)\,dz
= 2\pi i \left( \operatorname{Res}[F,i]+\operatorname{Res}[F,-i] + \sum_{n=-N}^N \operatorname{Res}[F,n]\right).
\]
Hence
\[
\left| \frac{\cosh(\pi-\theta)}{2\sinh \pi}
- \sum_{n=-N}^N \frac{\cos(n\theta)}{1+n^2} \right| \leq \frac{C}{N}.
\]
Letting $N\to\infty$, we conclude
\[
\frac{\cosh(\pi-\theta)}{2\sinh \pi}
= \sum_{n=-\infty}^\infty \frac{e^{in\theta}}{1+n^2}.
\]

This gives the Fourier series expansion, uniformly in $\theta$.
```

### CP-IV-0062

- chapter line: 3246
- atlas source solution flag: `unknown`
- linked source-solution candidates: `none`
- embedded solution marker in problem body: `NO`

```tex
\par\noindent\textbullet\quad Define
	\[
	g(z):=f(z)-z .
	\]
	Then $g$ is entire and $g(1/n)=0$ for all $n$. Since $1/n\to 0$ (an interior point),
	the identity theorem gives $g\equiv 0$, hence $f(z)\equiv z$.

	\medskip
```

### CP-IV-0070

- chapter line: 3258
- atlas source solution flag: `unknown`
- linked source-solution candidates: `none`
- embedded solution marker in problem body: `NO`

```tex
\par\noindent\textbullet\quad Show that $F$ has poles at $z=\pm i$ and at each integer $z=n$, $n\in\mathbb{Z}$. Compute the residues at these poles and verify that
	\[
	\operatorname{Res}(F,\pm i)
	= -\frac{\cosh(\pi-\theta)}{4\sinh\pi},
	\qquad
	\operatorname{Res}(F,n)
	= \frac{\cos(n\theta)}{2\pi\,(1+n^2)}.
	\]

	\par\noindent\textbullet\quad For each $N\in\mathbb{N}$ define four curves $\Gamma^{(N)}_j$ on $[-1,1]$ by
	\[
	\Gamma^{(N)}_1(t) = \Bigl(N+\tfrac12\Bigr)(1+it),\qquad
	\Gamma^{(N)}_2(t) = \Bigl(N+\tfrac12\Bigr)(-t+i),
	\]
	\[
	\Gamma^{(N)}_3(t) = \Bigl(N+\tfrac12\Bigr)(-1-it),\qquad
	\Gamma^{(N)}_4(t) = \Bigl(N+\tfrac12\Bigr)(t-i),
	\]
	and let $\Gamma^{(N)}$ be the closed contour obtained by following
	$\Gamma^{(N)}_1,\Gamma^{(N)}_2,\Gamma^{(N)}_3,\Gamma^{(N)}_4$ in turn.
	Sketch $\Gamma^{(N)}$ in the complex plane and indicate the locations of the poles of $F$ relative to this rectangle.

	\par\noindent\textbullet\quad Show that there exists a constant $C>0$, independent of $N$, such that for all integers $N\ge 1$ and all $\theta\in[0,2\pi]$,
	\[
	\left| \int_{\Gamma^{(N)}} F(z)\,dz \right|
	\le \frac{C}{N}.
	\]

	\par\noindent\textbullet\quad Using Cauchyâ€™s residue theorem applied to $\Gamma^{(N)}$, show that for $0\le\theta\le 2\pi$,
	\[
	\left|
	\frac{\cosh(\pi-\theta)}{2\sinh\pi}
	- \sum_{n=-N}^N \frac{e^{in\theta}}{1+n^2}
	\right|
	\le \frac{C}{N},
	\]
	and deduce that
	\[
	\frac{\cosh(\pi-\theta)}{2\sinh\pi}
	= \sum_{n=-\infty}^{\infty} \frac{e^{in\theta}}{1+n^2},
	\]
	with the series converging uniformly in $\theta\in[0,2\pi]$.

The function $F$ is meromorphic on $\mathbb{C}$, being the product of the entire function
$\cos\bigl((\pi-\theta)z\bigr)$ with the factors $(1+z^2)^{-1}$ and $(\sin\pi z)^{-1}$.
The only singularities of $F$ are poles arising from zeros of $1+z^2$ and $\sin(\pi z)$.

The equation $1+z^2=0$ has solutions $z=\pm i$, which give simple poles of $F$.
The function $\sin(\pi z)$ vanishes simply at each integer $z=n\in\mathbb{Z}$, so
$(\sin\pi z)^{-1}$ has simple poles there. Since $1+z^2$ does not vanish at any integer,
$F$ also has simple poles at all $z=n\in\mathbb{Z}$.

For a simple pole at $a\in\mathbb{C}$, the residue is given by
\[
\operatorname{Res}(F,a) = \lim_{z\to a} (z-a)\,F(z).
\]
At an integer $n$ one uses the local behaviour
$\sin(\pi z) = \pi(-1)^n(z-n) + O\bigl((z-n)^2\bigr)$ and evaluates the remaining factors at $z=n$.
At $z=\pm i$ one factors $1+z^2=(z-i)(z+i)$ and again evaluates the remaining analytic part at the pole.

The contour $\Gamma^{(N)}$ is a rectangle with vertices
\[
\pm\Bigl(N+\tfrac12\Bigr)\pm i,
\]
with horizontal sides at $\Im z=\pm1$ and vertical sides at $\Re z=\pm(N+\tfrac12)$.
For each fixed $N$, the contour encloses the poles at $z=\pm i$ and at the integers $n$ with $|n|\le N$.

Cauchyâ€™s residue theorem states that for such a closed contour,
\[
\int_{\Gamma^{(N)}} F(z)\,dz
= 2\pi i \sum_{a\in\mathcal{P}_N} \operatorname{Res}(F,a),
\]
where $\mathcal{P}_N$ is the finite set of poles of $F$ inside $\Gamma^{(N)}$.
Here $\mathcal{P}_N=\{-i,+i\}\cup\{n\in\mathbb{Z}:|n|\le N\}$.

To estimate the integral along $\Gamma^{(N)}$ one uses the estimation lemma
\[
\left|\int_{\Gamma^{(N)}} F(z)\,dz\right|
\le \sup_{z\in\Gamma^{(N)}} |F(z)|\cdot \operatorname{length}(\Gamma^{(N)}).
\]
On the vertical segments, $z = \pm\bigl(N+\tfrac12\bigr) + it$ with $-1\le t\le 1$, the factor
$1/(1+z^2)$ is of order $1/N^2$, whereas $\cos\bigl((\pi-\theta)z\bigr)$ and
$1/\sin(\pi z)$ are uniformly bounded in $N$, since $\Im z$ stays in a compact set.
On the horizontal segments, $\Re z$ is bounded and $\Im z=\pm1$, so $F$ remains uniformly bounded.
Combining these facts gives a bound of the form
\[
\left|\int_{\Gamma^{(N)}} F(z)\,dz\right|
\le \frac{C}{N}
\]
for some constant $C$ independent of $N$ and $\theta$.

Substituting the residue computations into the residue theorem gives an identity of the form
\[
\frac{\cosh(\pi-\theta)}{2\sinh\pi}
- \sum_{n=-N}^N \frac{e^{in\theta}}{1+n^2}
= \frac{1}{2\pi i}\int_{\Gamma^{(N)}} F(z)\,dz,
\]
so that the absolute value of the difference is bounded by $C/N$.
Letting $N\to\infty$ shows that the Fourier series
\[
\sum_{n=-\infty}^{\infty} \frac{e^{in\theta}}{1+n^2}
\]
converges uniformly in $\theta\in[0,2\pi]$ and represents $\cosh(\pi-\theta)/(2\sinh\pi)$.
```

### CP-IV-0076

- chapter line: 3367
- atlas source solution flag: `unknown`
- linked source-solution candidates: `none`
- embedded solution marker in problem body: `NO`

```tex
Find the Laurent expansion (in powers of $z$, i.e.\ about $0$) of
\[
\frac{1}{z^{2}-3z+2}=\frac{1}{(z-1)(z-2)}
\]
in the regions $\{|z|<1\}$, $\{1<|z|<2\}$, and $\{|z|\ge 2\}$.

Partial fractions:
\[
\frac{1}{(z-1)(z-2)}=-\frac{1}{z-1}+\frac{1}{z-2}.
\]
Geometric expansions:
\[
\frac{1}{1-w}=\sum_{n=0}^{\infty}w^{n}\quad(|w|<1),\qquad
\frac{1}{z-a}=\frac{1}{z}\cdot\frac{1}{1-\frac{a}{z}}
=\sum_{n=0}^{\infty}\frac{a^{n}}{z^{n+1}}\quad(|z|>|a|).
\]

\emph{(A) For $|z|<1$.}
\[
-\frac{1}{z-1}=\frac{1}{1-z}=\sum_{n=0}^{\infty}z^{n},\qquad
\frac{1}{z-2}=-\frac{1}{2}\frac{1}{1-\frac{z}{2}}
=-\sum_{n=0}^{\infty}\frac{z^{n}}{2^{\,n+1}}.
\]
Hence
\[
\boxed{\ \frac{1}{z^{2}-3z+2}=\sum_{n=0}^{\infty}\Big(1-2^{-(n+1)}\Big)z^{n},\quad |z|<1.\ }
\]

\medskip
\emph{(B) For $1<|z|<2$.}
\[
-\frac{1}{z-1}=-\frac{1}{z}\frac{1}{1-\frac{1}{z}}
=-\sum_{n=1}^{\infty} z^{-n},\qquad
\frac{1}{z-2}=-\sum_{n=0}^{\infty}\frac{z^{n}}{2^{\,n+1}}.
\]
Thus
\[
\boxed{\ \frac{1}{z^{2}-3z+2}
	=-\sum_{n=1}^{\infty} z^{-n}-\sum_{n=0}^{\infty}\frac{z^{n}}{2^{\,n+1}},
	\quad 1<|z|<2.\ }
\]

\medskip
\emph{(C) For $|z|>2$.}
\[
-\frac{1}{z-1}=-\sum_{m=1}^{\infty} z^{-m},\qquad
\frac{1}{z-2}=\frac{1}{z}\frac{1}{1-\frac{2}{z}}
=\sum_{m=1}^{\infty}\frac{2^{\,m-1}}{z^{m}}.
\]
Therefore
\[
\boxed{\ \frac{1}{z^{2}-3z+2}
	=\sum_{m=1}^{\infty}\big(2^{\,m-1}-1\big)z^{-m},\quad |z|>2.\ }
\]
```

### CP-IV-0079

- chapter line: 3426
- atlas source solution flag: `unknown`
- linked source-solution candidates: `none`
- embedded solution marker in problem body: `NO`

```tex
(restated).

Let $p(z)=z^{n}+a_{n-1}z^{n-1}+\cdots+a_1 z+a_0$ be a polynomial of degree $n$ and set
$A=\max\{|a_0|,\dots,|a_{n-1}|\}$. Prove that $p$ has $n$ zeros
(counting multiplicity) in the disk $\{|z|<A+1\}$.

Let $p(z)=z^{n}+a_{n-1}z^{n-1}+\cdots+a_0$ and $A=\max_{k}|a_k|$. For $|z|\ge A+1$,
\[
|p(z)|\ge |z|^{n}-\sum_{k=0}^{n-1}|a_k||z|^{k}
\ge |z|^{n}-A\,\frac{|z|^{n}-1}{|z|-1}>0.
\]
Hence $p$ has no zeros for $|z|\ge A+1$, so all (exactly $n$) zeros lie in $|z|<A+1$.

\medskip
```

### CP-IV-0098

- chapter line: 3444
- atlas source solution flag: `unknown`
- linked source-solution candidates: `none`
- embedded solution marker in problem body: `NO`

```tex
â€” Solution

We consider, for fixed $\theta\in[0,2\pi]$, the meromorphic function
\[
F(z) = \frac{1}{1+z^2}\,\frac{\cos\bigl((\pi-\theta)z\bigr)}{2\sin(\pi z)}.
\]

The factor $\cos\bigl((\pi-\theta)z\bigr)$ is entire, so the singularities of $F$
arise from the denominators $1+z^2$ and $\sin(\pi z)$.

	\par\noindent\textbullet\quad The zeros of $1+z^2$ are $z=\pm i$, and these are simple.
	\par\noindent\textbullet\quad The zeros of $\sin(\pi z)$ are the integers $z=n\in\mathbb{Z}$,
	and each zero is simple, so $(\sin\pi z)^{-1}$ has simple poles at all integers.

Thus $F$ has simple poles at $z=\pm i$ and at each $z=n\in\mathbb{Z}$.

For a simple pole at $a$, we have
\[
\operatorname{Res}(F,a) = \lim_{z\to a}(z-a)F(z).
\]

We factor
\[
1+z^2=(z-i)(z+i).
\]
Hence the residue of $(1+z^2)^{-1}$ at $z=i$ is
\[
\operatorname{Res}\Bigl(\frac{1}{1+z^2},i\Bigr)
=\frac{1}{2i}, \qquad
\operatorname{Res}\Bigl(\frac{1}{1+z^2},-i\Bigr)
=-\frac{1}{2i}.
\]
Using $\cos(ix)=\cosh x$ and $\sin(ix)=i\sinh x$ we have
\[
\cos\bigl((\pi-\theta)i\bigr)=\cosh(\pi-\theta),
\qquad
\sin(\pi i)=i\sinh\pi,
\qquad
\sin(-\pi i)=-i\sinh\pi.
\]
Therefore
\[
\operatorname{Res}(F,i)
=\frac{1}{2i}\cdot\frac{\cosh(\pi-\theta)}{2\sin(\pi i)}
=\frac{1}{2i}\cdot\frac{\cosh(\pi-\theta)}{2i\sinh\pi}
=-\frac{\cosh(\pi-\theta)}{4\sinh\pi},
\]
and
\[
\operatorname{Res}(F,-i)
=-\frac{1}{2i}\cdot\frac{\cosh(\pi-\theta)}{2\sin(-\pi i)}
=-\frac{1}{2i}\cdot\frac{\cosh(\pi-\theta)}{-2i\sinh\pi}
=-\frac{\cosh(\pi-\theta)}{4\sinh\pi}.
\]
Thus
\[
\operatorname{Res}(F,\pm i)=-\frac{\cosh(\pi-\theta)}{4\sinh\pi}.
\]

Let $n\in\mathbb{Z}$. Near $z=n$ we have
\[
\sin(\pi z)
=\sin\bigl(\pi n + \pi(z-n)\bigr)
=\sin(\pi n)\cos(\pi(z-n))
+\cos(\pi n)\sin(\pi(z-n)).
\]
Since $\sin(\pi n)=0$ and $\cos(\pi n)=(-1)^n$, it follows that
\[
\sin(\pi z)
=(-1)^n\pi(z-n) + O\bigl((z-n)^2\bigr),
\]
and therefore
\[
\frac{1}{\sin(\pi z)}
=\frac{(-1)^n}{\pi}\frac{1}{z-n}+O(1).
\]
The other factors are analytic at $z=n$, so
\[
\operatorname{Res}(F,n)
=\frac{1}{1+n^2}\cdot\frac{\cos\bigl((\pi-\theta)n\bigr)}{2}
\cdot\frac{(-1)^n}{\pi}.
\]
Using
\[
\cos\bigl((\pi-\theta)n\bigr)
=\cos(\pi n-n\theta)
=\cos(\pi n)\cos(n\theta)+\sin(\pi n)\sin(n\theta)
=(-1)^n\cos(n\theta),
\]
we obtain
\[
\operatorname{Res}(F,n)
=\frac{(-1)^n}{2\pi(1+n^2)}\cdot (-1)^n\cos(n\theta)
=\frac{\cos(n\theta)}{2\pi(1+n^2)}.
\]

\subsection*{(b) The contour $\Gamma^{(N)}$}

For $N\in\mathbb{N}$, the four curves
\[
\Gamma^{(N)}_1(t)=\Bigl(N+\tfrac12\Bigr)(1+it),\quad
\Gamma^{(N)}_2(t)=\Bigl(N+\tfrac12\Bigr)(-t+i),
\]
\[
\Gamma^{(N)}_3(t)=\Bigl(N+\tfrac12\Bigr)(-1-it),\quad
\Gamma^{(N)}_4(t)=\Bigl(N+\tfrac12\Bigr)(t-i),
\qquad -1\le t\le 1,
\]
form the sides of the rectangle whose vertices are
\[
\pm\Bigl(N+\tfrac12\Bigr)\pm i.
\]
We denote by $\Gamma^{(N)}$ the closed contour obtained by successively
traversing $\Gamma^{(N)}_1,\dots,\Gamma^{(N)}_4$.

This rectangle encloses the poles at $z=\pm i$ and at $z=n$ for all integers
$n$ with $|n|\le N$.

A schematic picture is shown in Figure~\ref{fig:contour-poles}.
\input{figures/part04/tikz/cp_iv_0098_source_figure_01.tex}


We claim that there exists a constant $C>0$, independent of $N$ and $\theta$,
such that
\[
\left|\int_{\Gamma^{(N)}} F(z)\,dz\right|\le \frac{C}{N}
\qquad\text{for all } N\ge1.
\]

A standard way to see this is to decompose $\Gamma^{(N)}$ into its four sides
and apply the estimation lemma.

On the vertical sides we have $z=\pm\bigl(N+\tfrac12\bigr)+it$ with $|t|\le1$.
Then $|z|^2\asymp N^2$ and hence
\[
\left|\frac{1}{1+z^2}\right|\le \frac{C_1}{N^2}.
\]
Moreover, for such $z$ the imaginary part is bounded, so both
$\cos\bigl((\pi-\theta)z\bigr)$ and $1/\sin(\pi z)$ are uniformly bounded in
$N$. The length of each vertical side is $2$, so the total contribution of the
vertical sides is $O(N^{-2})$.

On the horizontal sides we have $z=x\pm i$ with
$-(N+\tfrac12)\le x\le N+\tfrac12$. Using explicit expressions for
$\cos\bigl((\pi-\theta)(x\pm i)\bigr)$ and $\sin\bigl(\pi(x\pm i)\bigr)$, one
checks that
\[
|F(x+i)-F(x-i)| \le \frac{C_2}{1+|x|^3}
\qquad\text{for all }x\in\mathbb{R},
\]
and that $|F(x\pm i)|\le C_3/(1+x^2)$ for large $|x|$. Writing the integral
over the two horizontal sides as
\[
\int_{-(N+1/2)}^{N+1/2} \bigl(F(x+i)-F(x-i)\bigr)\,dx,
\]
one sees that the tail for $|x|\ge N$ is $O(N^{-2})$, while the integral over
$|x|\le N$ remains bounded independently of $N$. Altogether this yields a
bound of the form
\[
\left|\int_{\Gamma^{(N)}} F(z)\,dz\right|
\le \frac{C}{N}
\]
for some constant $C$ independent of $N$.

By Cauchyâ€™s residue theorem,
\[
\int_{\Gamma^{(N)}} F(z)\,dz
=2\pi i\sum_{a\in\mathcal{P}_N}\operatorname{Res}(F,a),
\]
where $\mathcal{P}_N=\{-i,+i\}\cup\{n\in\mathbb{Z}:|n|\le N\}$ is the set of
poles inside the rectangle. Using the residues computed in part (a),
\[
\sum_{a\in\mathcal{P}_N}\operatorname{Res}(F,a)
= \operatorname{Res}(F,i)+\operatorname{Res}(F,-i)
+\sum_{n=-N}^N \operatorname{Res}(F,n)
= -\frac{\cosh(\pi-\theta)}{2\sinh\pi}
+\sum_{n=-N}^N \frac{\cos(n\theta)}{2\pi(1+n^2)}.
\]
Therefore
\[
\int_{\Gamma^{(N)}} F(z)\,dz
= 2\pi i\left(
-\frac{\cosh(\pi-\theta)}{2\sinh\pi}
+\sum_{n=-N}^N \frac{\cos(n\theta)}{2\pi(1+n^2)}
\right),
\]
or equivalently
\[
\frac{\cosh(\pi-\theta)}{2\sinh\pi}
-\sum_{n=-N}^N \frac{\cos(n\theta)}{2\pi(1+n^2)}
= -\frac{1}{2\pi i}\int_{\Gamma^{(N)}} F(z)\,dz.
\]

Using the estimate from part (c) we obtain
\[
\left|
\frac{\cosh(\pi-\theta)}{2\sinh\pi}
-\sum_{n=-N}^N \frac{\cos(n\theta)}{2\pi(1+n^2)}
\right|
\le \frac{1}{2\pi}
\left|\int_{\Gamma^{(N)}} F(z)\,dz\right|
\le \frac{C}{N}.
\]
Since
\[
\frac{1}{2\pi}\sum_{n=-N}^N \frac{\cos(n\theta)}{1+n^2}
= \Re\left(\sum_{n=-N}^N \frac{e^{in\theta}}{1+n^2}\right),
\]
we can rewrite this in the complex exponential form
\[
\left|
\frac{\cosh(\pi-\theta)}{2\sinh\pi}
-\sum_{n=-N}^N \frac{e^{in\theta}}{1+n^2}
\right|
\le \frac{C}{N}.
\]
Letting $N\to\infty$ gives, uniformly in $\theta\in[0,2\pi]$,
\[
\frac{\cosh(\pi-\theta)}{2\sinh\pi}
=\sum_{n=-\infty}^{\infty} \frac{e^{in\theta}}{1+n^2},
\]
which is the desired Fourier series representation.


\bigskip
\noindent\rule{\textwidth}{0.4pt}
\medskip

We first recall the residues already computed:
\begin{align*}
	\operatorname{Res}(F,\pm i) &= -\,\frac{\cosh(\pi-\theta)}{4\sinh\pi},\\[4pt]
	\operatorname{Res}(F,n) &= \frac{\cos(n\theta)}{2\pi(1+n^2)}, \qquad n\in\mathbb{Z}.
\end{align*}

The set of poles inside $\Gamma^{(N)}$ is
\[
\mathcal{P}_N = \{-i,+i\}\cup\{n\in\mathbb{Z}:|n|\le N\},
\]
so
\begin{equation*}
	\sum_{a\in\mathcal{P}_N} \operatorname{Res}(F,a)
	= \operatorname{Res}(F,i)+\operatorname{Res}(F,-i)+\sum_{n=-N}^{N}\operatorname{Res}(F,n).
\end{equation*}

Now substitute the explicit formulas and simplify **step by step**:
\begin{align*}
	\sum_{a\in\mathcal{P}_N} \operatorname{Res}(F,a)
	&= \left(-\frac{\cosh(\pi-\theta)}{4\sinh\pi}\right)
	+\left(-\frac{\cosh(\pi-\theta)}{4\sinh\pi}\right)
	+\sum_{n=-N}^{N}\frac{\cos(n\theta)}{2\pi(1+n^2)}\\[6pt]
	&= -\frac{\cosh(\pi-\theta)}{4\sinh\pi}
	-\frac{\cosh(\pi-\theta)}{4\sinh\pi}
	+\sum_{n=-N}^{N}\frac{\cos(n\theta)}{2\pi(1+n^2)}\\[6pt]
	&= -\left(
	\frac{\cosh(\pi-\theta)}{4\sinh\pi}
	+\frac{\cosh(\pi-\theta)}{4\sinh\pi}
	\right)
	+\sum_{n=-N}^{N}\frac{\cos(n\theta)}{2\pi(1+n^2)}\\[6pt]
	&= -\frac{2\cosh(\pi-\theta)}{4\sinh\pi}
	+\sum_{n=-N}^{N}\frac{\cos(n\theta)}{2\pi(1+n^2)}\\[6pt]
	&= -\frac{\cosh(\pi-\theta)}{2\sinh\pi}
	+\sum_{n=-N}^{N}\frac{\cos(n\theta)}{2\pi(1+n^2)}.
\end{align*}

Hence
\[
\boxed{
	\sum_{a\in\mathcal{P}_N} \operatorname{Res}(F,a)
	= -\frac{\cosh(\pi-\theta)}{2\sinh\pi}
	+\sum_{n=-N}^{N}\frac{\cos(n\theta)}{2\pi(1+n^2)}.
}\]

\bigskip
\noindent\rule{\textwidth}{0.4pt}
\medskip

\clearpage

\bigskip
\noindent\rule{\textwidth}{0.4pt}
\medskip

\clearpage

\[
\frac{\cosh\pi}{2\sinh\pi}
= \sum_{n=-\infty}^{\infty}\frac{1}{1+n^2}.
\]

\[
1 + 2\sum_{n=1}^{\infty}\frac{1}{1+n^2}
= \frac{\cosh\pi}{2\sinh\pi},
\qquad
\sum_{n=1}^{\infty}\frac{1}{1+n^2}
= \frac{1}{2}\Bigl(\frac{\cosh\pi}{2\sinh\pi}-1\Bigr).
\]
```

### CP-IV-0099

- chapter line: 3744
- atlas source solution flag: `unknown`
- linked source-solution candidates: `none`
- embedded solution marker in problem body: `NO`

```tex
Fourier transforms and inverse verification

We use the convention \(\displaystyle \widehat f(\xi)=\int_{-\infty}^{\infty} f(x)\,e^{-i\xi x}\,dx\) and
	\(\displaystyle f(x)=\frac{1}{2\pi}\int_{-\infty}^{\infty}\widehat f(\xi)\,e^{i\xi x}\,d\xi\).

	\subsection*{(a) \(f(x)=e^{-|x|}\) â€” Transform and step-by-step inverse}
	\textit{Transform:}
	\[
	\widehat f(\xi)
	=\int_{0}^{\infty}e^{-(1+i\xi)x}\,dx+\int_{-\infty}^{0}e^{(1-i\xi)x}\,dx
	=\frac{1}{1+i\xi}+\frac{1}{1-i\xi}
	=\boxed{\frac{2}{1+\xi^{2}}}.
	\]

	\textit{Inverse by residues (two cases):}
	\begin{align*}
		f(x)
		&=\frac{1}{2\pi}\int_{\mathbb R}\frac{2\,e^{i\xi x}}{1+\xi^{2}}\,d\xi
		=\frac{1}{2\pi}\int_{\mathbb R}\frac{2\,e^{i\xi x}}{(\xi-i)(\xi+i)}\,d\xi.
		\\[0.25em]
		\textbf{Case }x>0:\quad
		f(x)
		&=\frac{1}{2\pi}\oint_{\Gamma^+}\frac{2\,e^{i\xi x}}{(\xi-i)(\xi+i)}\,d\xi
		&&\text{(close upward; Jordanâ€™s lemma)}\\
		&=\frac{1}{2\pi}(2\pi i)\,\operatorname{Res}_{\xi=i}\!\left(\frac{2\,e^{i\xi x}}{(\xi-i)(\xi+i)}\right)
		=\frac{i\,2\,e^{ix}}{2i( i+i)}=\;e^{-x}.
		\\[0.35em]
		\textbf{Case }x<0:\quad
		f(x)
		&=\frac{1}{2\pi}\oint_{\Gamma^-}\frac{2\,e^{i\xi x}}{(\xi-i)(\xi+i)}\,d\xi
		&&\text{(close downward)}\\
		&=\frac{1}{2\pi}(2\pi i)\,\operatorname{Res}_{\xi=-i}\!\left(\frac{2\,e^{i\xi x}}{(\xi-i)(\xi+i)}\right)
		=\;e^{\,x}.
	\end{align*}
	Therefore \(\boxed{\,f(x)=e^{-|x|}\,}\).

	\subsection*{(b) \(f(x)=e^{-a^{2}x^{2}}\) (\(a>0\)) â€” Transform and step-by-step inverse}
	\textit{Transform:}
	\begin{align*}
		\widehat f(\xi)
		&=\int_{\mathbb R}e^{-a^{2}x^{2}-i\xi x}\,dx
		= e^{-\xi^{2}/(4a^{2})}\int_{\mathbb R}e^{-a^{2}\left(x+i\frac{\xi}{2a^{2}}\right)^{2}}dx\\
		&\phantom{=} \qquad \Rightarrow\qquad
		\boxed{\,\widehat f(\xi)=\frac{\sqrt{\pi}}{a}\,e^{-\xi^{2}/(4a^{2})}\, }.
	\end{align*}
	(Justify by integrating over a large rectangle whose vertical sides are the real line and
	the line shifted up by \(i\,\xi/(2a^{2})\); the horizontal sides vanish by Gaussian decay.)

	\textit{Inverse by a rectangular shift (explicit steps):}
	\begin{align*}
		f(x)
		&=\frac{1}{2\pi}\int_{\mathbb R}\frac{\sqrt{\pi}}{a}\,e^{-\xi^{2}/(4a^{2})}\,e^{i\xi x}\,d\xi\\
		&=\frac{1}{2\pi}\cdot\frac{\sqrt{\pi}}{a}\,
		\int_{\mathbb R} \exp\!\left(-\frac{1}{4a^{2}}(\xi-2ia^{2}x)^{2}\right)\,
		\exp\!\left(-a^{2}x^{2}\right)\,d\xi
		&&\text{(complete the square)}\\
		&=\frac{1}{2\pi}\cdot\frac{\sqrt{\pi}}{a}\,e^{-a^{2}x^{2}}
		\int_{\mathbb R+2ia^{2}x} \exp\!\left(-\frac{u^{2}}{4a^{2}}\right)\,du
		&&\text{(shift contour vertically)}\\
		&=\frac{1}{2\pi}\cdot\frac{\sqrt{\pi}}{a}\,e^{-a^{2}x^{2}}
		\int_{\mathbb R} \exp\!\left(-\frac{u^{2}}{4a^{2}}\right)\,du
		&&\text{(no poles; horizontal sides vanish)}\\
		&=\frac{1}{2\pi}\cdot\frac{\sqrt{\pi}}{a}\,e^{-a^{2}x^{2}}\cdot 2a\sqrt{\pi}
		\;=\;e^{-a^{2}x^{2}}.
	\end{align*}

	\bigskip\hrule\bigskip
```

### CP-IV-0110

- chapter line: 3817
- atlas source solution flag: `unknown`
- linked source-solution candidates: `none`
- embedded solution marker in problem body: `NO`

```tex
Consider the meromorphic function
\[
F(z) = \frac{1}{1+z^2} \frac{\cos[(\pi-\theta)z]}{2\sin(\pi z)}.
\]

The poles occur at $z=\pm i$ and $z=n$, $n\in\mathbb{Z}$.
...

\begin{center}

\end{center}

\textit{Legend.} Red dots = poles at integers, Blue dots = poles at $\pm i$, dashed square = contour $\Gamma^{(N)}$.

---

...

\begin{center}

\end{center}

\textit{Legend.} Blue curve = exact hyperbolic expression, red dashed = Fourier sum with $N=1$, green dashed = Fourier sum with $N=5$.

	To recall the behavior of basic meromorphic functions near poles,
	we show plots of $f(z) = 1/z$ and $f(z) = 1/z^2$ on the real line.
	Both have a pole at $z=0$, with $1/z$ being of order $1$ and
	$1/z^2$ being of order $2$. Clearly, $(1/z)^2 = 1/z^2$.

	\subsection*{Chart: $f(x)=1/x$ on $\mathbb{R}\setminus\{0\}$}
	\begin{center}

		\hspace{1cm}

	\end{center}

	\textit{Legend.} Function $1/x$ has a simple pole at $x=0$. The left and right limits
	blow up to $\mp\infty$.

	---

	\begin{center}

		\hspace{1cm}

	\end{center}

	\textit{Legend.} Function $1/x^2$ has a pole of order 2 at $x=0$.
	It diverges to $+\infty$ on both sides of the pole.
	Clearly, $(1/x)^2 = 1/x^2$.

	\subsection*{Example 1: $f(z) = \tfrac{1}{z}$}

	\textbf{Description.}
	For $z = re^{i\theta}$ we have
	\[
	\frac{1}{z} = \frac{1}{r} e^{-i\theta}.
	\]
	Thus $f(z)$ inverts the magnitude ($r \mapsto 1/r$) and reflects the angle
	($\theta \mapsto -\theta$). The unit circle maps to itself with reversed orientation.
	Lines through the origin are mapped to lines through the origin, reflected in the real axis.

	\begin{center}

		\hspace{1cm}

	\end{center}

	\textit{Legend.} Left: domain ($z$-plane). Right: image ($w=1/z$).
	The unit circle is preserved, rays reflect across the real axis.

	---

\subsection*{Example: $f(z)=\tfrac{1}{z}$}

\textbf{Description.}
For $z = re^{i\theta}$ we have
\[
\frac{1}{z} = \frac{1}{r} e^{-i\theta}.
\]
Thus the mapping $f(z)=1/z$ has the following geometric effects:

	\par\noindent\textbullet\quad \textbf{Inversion of radii:} $r \mapsto 1/r$.
	\par\noindent\textbullet\quad \textbf{Reflection of angles:} $\theta \mapsto -\theta$.
	\par\noindent\textbullet\quad The unit circle $|z|=1$ is invariant, but orientation is reversed.
	\par\noindent\textbullet\quad The interior of the unit disk $|z|<1$ maps to the exterior $|w|>1$, and vice versa.
	\par\noindent\textbullet\quad Rays through the origin map to reflected rays across the real axis.
	\par\noindent\textbullet\quad More generally, lines not through the origin map to circles, and circles not through the origin map to circles (inversion geometry).

\begin{center}

	\hspace{1.5cm}

\end{center}

\textit{Legend.}
Blue: unit circle (invariant).
Red: ray at $\theta=\pi/4$ mapping to $\theta=-\pi/4$.
Green dashed: vertical line $\Re z=1$ maps to a circle through the origin.

\subsection*{Example: $f(z)=\tfrac{1}{z+1}$}

\textbf{Description.}
This mapping is a shifted inversion. Let $w=z+1$. Then
\[
f(z) = \frac{1}{z+1} = \frac{1}{w}.
\]
Thus the inversion is centered at $z=-1$ instead of $z=0$.
The function has a simple pole at $z=-1$.
As $|z|\to\infty$, $f(z)\to 0$.
Key geometric effects:

	\par\noindent\textbullet\quad Pole at $z=-1$ corresponds to $w=0$ under translation.
	\par\noindent\textbullet\quad The unit circle $|z|=1$ no longer maps to itself, but to another circle in the $w$-plane.
	\par\noindent\textbullet\quad Lines and circles not passing through $z=-1$ map to circles.
	\par\noindent\textbullet\quad Rays and bands relative to $z=-1$ are inverted accordingly.

\begin{center}

	\hspace{1.5cm}

\end{center}

\textit{Legend.}
Left: domain ($z$-plane) with unit circle (blue), pole at $z=-1$ (red), and imaginary axis (green dashed).
Right: schematic image under $f(z)=1/(z+1)$: unit circle maps to another circle, imaginary axis maps to a circle through the origin, and $z=-1$ maps to infinity.

\subsection*{Example: $f(z)=\tfrac{1}{z^2}$}

\textbf{Description.}
For $z = re^{i\theta}$ we have
\[
f(z) = \frac{1}{z^2} = \frac{1}{r^2} e^{-2i\theta}.
\]
Thus the mapping $f(z)=1/z^2$ has the following geometric effects:

	\par\noindent\textbullet\quad \textbf{Inversion of radii (squared):} $r \mapsto 1/r^2$.
	\par\noindent\textbullet\quad \textbf{Angle doubling and reflection:} $\theta \mapsto -2\theta$.
	\par\noindent\textbullet\quad The unit circle $|z|=1$ is invariant (maps to itself).
	\par\noindent\textbullet\quad The interior of the unit disk $|z|<1$ maps to the exterior $|w|>1$, and vice versa.
	\par\noindent\textbullet\quad Rays at angle $\theta$ map to rays at angle $-2\theta$.
	\par\noindent\textbullet\quad There is a pole of order 2 at $z=0$.

\begin{center}

	\hspace{1.5cm}

\end{center}

\textit{Legend.}
Blue: unit circle (invariant).
Red: sample rays mapped under $\theta \mapsto -2\theta$.
Black dot: pole of order 2 at $z=0$.
```

### CP-IV-0137

- chapter line: 4064
- atlas source solution flag: `unknown`
- linked source-solution candidates: `none`
- embedded solution marker in problem body: `NO`

```tex
(cotangent trick and square contour).

Let $N\in\mathbb N$ and let $\gamma_N$ be the square contour with vertices
$(\pm1\pm i)\bigl(N+\tfrac12\bigr)$, oriented positively.

	\par\noindent\textbullet\quad Show that there exists a constant $C>0$, independent of $N$, such that
	\[
	|\cot(\pi z)|<C \qquad \text{for all } z\in\gamma_N .
	\]
	\par\noindent\textbullet\quad By integrating $\displaystyle \frac{\pi\cot(\pi z)}{z^{2}+1}$ around $\gamma_N$,
	prove that
	\[
	\sum_{n=0}^{\infty}\frac{1}{n^{2}+1}\;=\;\frac{1+\pi\coth\pi}{2}\, .
	\]
	\par\noindent\textbullet\quad Evaluate the alternating series
	\[
	\sum_{n=0}^{\infty}\frac{(-1)^{n}}{n^{2}+1}\, .
	\]

With $z=x+iy$ one has
\[
|\sin(\pi z)|^{2}=\sin^{2}(\pi x)+\sinh^{2}(\pi y),\qquad
|\cos(\pi z)|^{2}=\cos^{2}(\pi x)+\sinh^{2}(\pi y).
\]
On the \emph{vertical} sides $x=\pm(N+\tfrac12)$ we get
$\sin(\pi x)=\pm1$, $\cos(\pi x)=0$, hence
\[
\cot(\pi z)=-i\,\tanh(\pi y),\qquad |\cot(\pi z)|\le 1.
\]
On the \emph{horizontal} sides $y=\pm(N+\tfrac12)$,
\[
|\cot(\pi z)|^{2}
=\frac{\cos^{2}(\pi x)+\sinh^{2}(\pi y)}{\sin^{2}(\pi x)+\sinh^{2}(\pi y)}
\le 1+\frac{1}{\sinh^{2}(\pi|y|)}
\le 1+\frac{1}{\sinh^{2}(\pi/2)}.
\]
Thus there is a constant
$C=\max\!\big\{1,\sqrt{1+\sinh^{-2}(\pi/2)}\big\}$, independent of $N$, such that
$|\cot \pi z|<C$ on $\gamma_N$.

\medskip
\paragraph{(ii) $\displaystyle \sum_{n=0}^{\infty}\frac{1}{n^{2}+1}$.}
Let $F(z)=\dfrac{\pi\cot(\pi z)}{z^{2}+1}$. Then on $\gamma_N$,
$|F(z)|\lesssim C/|z|^{2}$, so $\int_{\gamma_N}F(z)\,dz\to0$ as $N\to\infty$.
Residues:
\[
\operatorname{Res}(F;n)=\frac{1}{n^{2}+1}\quad(n\in\mathbb Z),
\qquad
\operatorname{Res}(F;i)=\operatorname{Res}(F;-i)=\frac{\pi\cot(\pi i)}{2i}.
\]
Since $\cot(\pi i)=-i\,\coth\pi$, we have
$\operatorname{Res}(F;i)+\operatorname{Res}(F;-i)=-\pi\coth\pi$.
Hence, letting $N\to\infty$,
\[
0=\int_{\gamma_N}F
=2\pi i\!\left(\sum_{n\in\mathbb Z}\frac{1}{n^{2}+1}-\pi\coth\pi\right)
\ \Rightarrow\
\sum_{n\in\mathbb Z}\frac{1}{n^{2}+1}=\pi\coth\pi.
\]
By symmetry,
\[
\boxed{\ \sum_{n=0}^{\infty}\frac{1}{n^{2}+1}=\frac{1+\pi\coth\pi}{2}\ }.
\]

\medskip
\paragraph{(iii) $\displaystyle \sum_{n=0}^{\infty}\frac{(-1)^{n}}{n^{2}+1}$.}
Set $G(z)=\dfrac{\pi\csc(\pi z)}{z^{2}+1}$.
Again $\int_{\gamma_N}G\to0$ and
\[
\operatorname{Res}(G;n)=\frac{(-1)^{n}}{n^{2}+1}\quad(n\in\mathbb Z),
\qquad
\csc(\pi i)=\frac{1}{\sin(\pi i)}=\frac{1}{i\sinh\pi}=-i\,\mathrm{csch}\,\pi.
\]
Therefore
\[
\operatorname{Res}(G;i)+\operatorname{Res}(G;-i)
=\frac{\pi\csc(\pi i)}{2i}+\frac{\pi\csc(-\pi i)}{-2i}
=-\pi\,\mathrm{csch}\,\pi.
\]
Thus
\[
\sum_{n\in\mathbb Z}\frac{(-1)^{n}}{n^{2}+1}
=\pi\,\mathrm{csch}\,\pi,
\qquad
\boxed{\ \sum_{n=0}^{\infty}\frac{(-1)^{n}}{n^{2}+1}
	=\frac{1+\pi\,\mathrm{csch}\,\pi}{2}\ }.
\]


\emph{Core identities.} For $z=x+iy$,
\[
\sin(\pi z)=\sin(\pi x)\cosh(\pi y)+i\cos(\pi x)\sinh(\pi y),\quad
\cos(\pi z)=\cos(\pi x)\cosh(\pi y)-i\sin(\pi x)\sinh(\pi y),
\]
hence
\[
|\sin(\pi z)|^2=\sin^2(\pi x)+\sinh^2(\pi y),\qquad
|\cos(\pi z)|^2=\cos^2(\pi x)+\sinh^2(\pi y).
\]
Also
\[
\cot z=i\,\coth(iz)=i\,\frac{e^{2iz}+1}{e^{2iz}-1}.
\]

\emph{Poles, residues, partial fractions.}
$\cot$ has simple poles at $k\pi$ with residue $1$; $\pi\cot(\pi z)$ has simple poles at integers with residue $1$.
\[
\pi\cot(\pi z)=\sum_{n\in\mathbb Z}\frac{1}{z-n}.
\]

\medskip
\paragraph{Images of horizontal lines $y=\text{const}$.}
Write
\[
\cot(x+iy)=\frac{\sin 2x - i\,\sinh 2y}{\cosh 2y - \cos 2x}=u(x)+iv(x).
\]
Eliminating $x$ yields the circle
\[
\boxed{\ u^2+\big(v+\coth 2y\big)^2=\csch^2 2y\ },
\]
i.e.\ for fixed $y$ the image is a circle centered at $-i\,\coth 2y$ with radius $\csch 2y$ (orthogonal to the imaginary axis). As $y\to\pm\infty$ this circle collapses to the point $\mp i$; as $y\to0$ it expands and approaches the real axis.

\medskip
\paragraph{Images of vertical lines $x=\text{const}$.}
For fixed $x$, as $y$ varies,
\[
\cot(x+iy)\to -\,i\ (y\to+\infty),\qquad \cot(x+iy)\to +\,i\ (y\to-\infty),
\]
and $\cot(x+0i)=\cot x\in\mathbb R$. Thus the image is a circular arc joining $\pm i$ and crossing the real axis at $\cot x$ (orthogonal to the family in the previous paragraph).

\medskip

Because $\cot z=\tan(\tfrac{\pi}{2}-z)$, the vertical strip $\{0<\Re z<\pi\}$ is mapped bijectively onto $\mathbb C$, and periodicity $\cot(z+\pi)=\cot z$ tiles the plane by such strips.
Via $e^{2iz}=e^{-2y}e^{2ix}$ a horizontal strip $y\in(y_1,y_2)$ maps to an annulus; the MĂ¶bius map $w\mapsto i\frac{w+1}{w-1}$ then sends annuli to circular bands bounded by the circles $u^2+(v+\coth 2y)^2=\csch^2 2y$.

\medskip

On the square with vertices $(\pm1\pm i)(N+\tfrac12)$,
\[
|\cot(\pi z)|\le 1 \ \text{on vertical edges},\qquad
|\cot(\pi z)|^2\le 1+\frac{1}{\sinh^2(\pi/2)} \ \text{on horizontal edges},
\]
so there is a constant $C$ independent of $N$ with $|\cot(\pi z)|<C$ on the boundary.

\medskip
\emph{Asymptotics and symmetries.}
$\cot(-z)=-\cot z$, $\overline{\cot(\bar z)}=\cot z$, and $\cot(x+iy)\to\mp i$ as $y\to\pm\infty$.
These give quick qualitative sketches of level sets and images.

Let $z=x+iy$ and set
\[
\cot z=\frac{\sin 2x-i\,\sinh 2y}{\cosh 2y-\cos 2x}=u+iv,\qquad
D:=\cosh 2y-\cos 2x,\ S:=\sinh 2y,\ C:=\cosh 2y.
\]
Then
\[
u=\frac{\sin 2x}{D},\qquad v=-\frac{S}{D}\ \Longrightarrow\ D=-\frac{S}{v}.
\]
Hence
\[
\sin 2x=uD=-\frac{uS}{v},\qquad \cos 2x = C - D = C+\frac{S}{v}.
\]
Now
\[
u^{2}+\Bigl(v+\frac{C}{S}\Bigr)^{2}
=\frac{1}{D^{2}}\!\left[\sin^{2}2x+\frac{(1-C\cos 2x)^{2}}{S^{2}}\right].
\]
Using $D=C-\cos 2x$ and $\cosh^{2}2y-\sinh^{2}2y=1$ we get
\[
S^{2}\sin^{2}2x+(1-C\cos 2x)^{2}=(C-\cos 2x)^{2}=D^{2}.
\]
Therefore
\[
\boxed{\,u^{2}+\bigl(v+\coth 2y\bigr)^{2}=\csch^{2}2y\,},
\]
i.e.\ for fixed $y$ the image is a circle centered at $-i\,\coth(2y)$ with radius $\csch(2y)$.

\[
\csch x=\frac{1}{\sinh x}=\frac{2}{e^{x}-e^{-x}},\qquad
\sech x=\frac{1}{\cosh x},\quad
\coth x=\frac{\cosh x}{\sinh x}.
\]
Parity and derivatives:
\[
\csch(-x)=-\csch x,\qquad
\frac{d}{dx}\csch x=-\csch x\,\coth x,\qquad
\frac{d}{dx}\coth x=-\csch^{2}x.
\]
Identity and asymptotics:
\[
\coth^{2}x-\csch^{2}x=1,\qquad
\csch x\sim 2e^{-|x|}\quad (|x|\to\infty).
\]

\emph{Core identities.} For $z=x+iy$,
\[
\sin z=\sin x\,\cosh y+i\,\cos x\,\sinh y,\qquad
|\sin z|^{2}=\sin^{2}x+\sinh^{2}y.
\]
Symmetries: $\overline{\sin\bar z}=\sin z$, $\sin(-z)=-\sin z$, $\sin(z+2\pi)=\sin z$.
Zeros are simple at $z=n\pi$ ($n\in\mathbb Z$) since $\sin'(n\pi)=\cos(n\pi)\neq0$.

\medskip
\paragraph{Images of horizontal lines $y=\text{const}$.}
Let $w=\sin z=u+iv$. For fixed $y$,
\[
u=\sin x\,\cosh y,\qquad v=\cos x\,\sinh y.
\]
Eliminating $x$ gives the ellipse
\[
\boxed{\ \Big(\tfrac{u}{\cosh y}\Big)^{2}+\Big(\tfrac{v}{\sinh y}\Big)^{2}=1\ }.
\]
Thus the image is an ellipse centered at $0$ with semiaxes $\cosh y$ (real axis) and $\sinh y$ (imaginary axis).
Since $\cosh^{2}y-\sinh^{2}y=1$, the foci lie at $\pm1$, and
\[
|w-1|+|w+1|=2\cosh y.
\]

\medskip
\paragraph{Images of vertical lines $x=\text{const}$.}
For fixed $x$,
\[
u=\sin x\,\cosh y,\qquad v=\cos x\,\sinh y
\]
and eliminating $y$ using $\cosh^{2}y-\sinh^{2}y=1$ yields
\[
\boxed{\ \Big(\tfrac{u}{\sin x}\Big)^{2}-\Big(\tfrac{v}{\cos x}\Big)^{2}=1\ } \quad
(\sin x\,\cos x\ne0).
\]
Hence the image is a hyperbola with the same foci $\pm1$.
Degenerate cases:
$x=n\pi$ gives $u=0$ (imaginary axis) and $x=\frac{\pi}{2}+n\pi$ gives $v=0$ (real axis).

\medskip

One may take the fundamental strip $S=\{\,0<\Re z<\pi\,\}$. On $x=0$ or $x=\pi$
the image is purely imaginary; in the interior the images of horizontal/vertical lines
form the orthogonal confocal families of ellipses and hyperbolas with foci $\pm1$.
(Branches of $\arcsin$ use the slits $(-\infty,-1]\cup[1,\infty)$.)

\emph{Core identities.} For $z=x+iy$,
\[
\cos z=\cos x\,\cosh y - i\,\sin x\,\sinh y,\qquad
|\cos z|^{2}=\cos^{2}x+\sinh^{2}y.
\]
Symmetries: $\overline{\cos\bar z}=\cos z$, $\cos(-z)=\cos z$, $\cos(z+2\pi)=\cos z$.
Zeros are simple at $z=\tfrac{\pi}{2}+n\pi$ since $\cos'(z)=-\sin z$.

\medskip
\paragraph{Images of horizontal lines $y=\text{const}$.}
Let $w=\cos z=u+iv$. For fixed $y$,
\[
u=\cos x\,\cosh y,\qquad v=-\,\sin x\,\sinh y.
\]
Eliminating $x$ gives the ellipse
\[
\boxed{\ \Big(\tfrac{u}{\cosh y}\Big)^{2}+\Big(\tfrac{v}{\sinh y}\Big)^{2}=1\ }.
\]
Thus the image is an ellipse centered at $0$ with semiaxes $\cosh y$ (real axis) and $\sinh y$ (imaginary axis); since $\cosh^{2}y-\sinh^{2}y=1$, the foci are $\pm1$ and
\[
|w-1|+|w+1|=2\cosh y.
\]

\medskip
\paragraph{Images of vertical lines $x=\text{const}$.}
For fixed $x$,
\[
u=\cos x\,\cosh y,\qquad v=-\,\sin x\,\sinh y.
\]
Eliminating $y$ using $\cosh^{2}y-\sinh^{2}y=1$ yields
\[
\boxed{\ \Big(\tfrac{u}{\cos x}\Big)^{2}-\Big(\tfrac{v}{\sin x}\Big)^{2}=1\ } \quad
(\sin x\,\cos x\ne0),
\]
a hyperbola with the same foci $\pm1$.
Degenerate cases:
$x=n\pi$ gives $v=0$ (real axis) and $x=\tfrac{\pi}{2}+n\pi$ gives $u=0$ (imaginary axis).

\medskip

A fundamental strip is $S=\{\,0<\Re z<\pi\,\}$. On $x=0$ or $x=\pi$ the image is real; inside $S$ the images of horizontal/vertical lines form orthogonal confocal ellipses and hyperbolas with foci $\pm1$.
(Branches of $\arccos$ use the slits $(-\infty,-1]\cup[1,\infty)$.)

\emph{Core identities.} For $z=x+iy$,
\[
\tan z=\frac{\sin z}{\cos z}
=\frac{\sin 2x + i\,\sinh 2y}{\cos 2x+\cosh 2y}.
\]
Thus, writing $w=\tan z=u+iv$,
\[
u=\frac{\sin 2x}{\cos 2x+\cosh 2y},\qquad
v=\frac{\sinh 2y}{\cos 2x+\cosh 2y}.
\]

\emph{Zeros, poles, residues.}
$\tan z$ has simple zeros at $z=n\pi$ and simple poles at $z=\tfrac{\pi}{2}+n\pi$ ($n\in\mathbb Z$).
At each pole, $\mathrm{Res}(\tan;z_0)=1$. The partial fraction expansion is
\[
\pi\,\tan(\pi z)=\sum_{n\in\mathbb Z}\frac{1}{\,z-(n+\tfrac12)\,}.
\]
Symmetries: $\tan(-z)=-\tan z$, $\overline{\tan\bar z}=\tan z$, and $\tan(z+\pi)=\tan z$.
As $|y|\to\infty$, $\tan(x+iy)\to i\,\mathrm{sgn}(y)$.

\medskip
\paragraph{Images of horizontal lines $y=\text{const}$.}
Fix $y$ and set $C=\cosh(2y)$, $S=\sinh(2y)$, $D=\cos(2x)+C$. Then
\[
u=\frac{\sin 2x}{D},\qquad v=\frac{S}{D}.
\]
Eliminating $x$ (using $D=S/v$) yields the circle
\[
\boxed{\ u^{2}+\Bigl(v-\frac{\cosh(2y)}{\sinh(2y)}\Bigr)^{2}=\frac{1}{\sinh^{2}(2y)}\ }.
\]
Hence the image is a circle centered at $-i\,\dfrac{\cosh(2y)}{\sinh(2y)}$ on the imaginary axis (note the sign in $u+iv$) with radius $\dfrac{1}{|\sinh(2y)|}$.
As $y\to\pm\infty$ the circle shrinks to $\pm i$; as $y\to0$ it expands toward the real axis.

\medskip
\paragraph{Images of vertical lines $x=\text{const}$.}
For fixed $x$, as $y$ varies,
\[
\tan(x+iy)\to i \ (y\to+\infty),\qquad \tan(x+iy)\to -i \ (y\to-\infty),
\]
and $\tan(x+0i)=\tan x\in\mathbb R$. Thus the image is a circular arc joining $\pm i$ and crossing the real axis at $\tan x$ (orthogonal to the family above).

\medskip

The vertical strip $S=\{\, -\tfrac{\pi}{2}<\Re z<\tfrac{\pi}{2}\,\}$ is mapped bijectively onto $\mathbb C$ by $\tan$; its boundary lines map to $\infty$ (simple poles). Periodicity $\tan(z+\pi)=\tan z$ tiles the plane by translates of $S$.
```

### CP-IV-0004

- chapter line: 4440
- atlas source solution flag: `unknown`
- linked source-solution candidates: `none`
- embedded solution marker in problem body: `NO`

```tex
\par\noindent\textbullet\quad \textbf{(c)}\;
	Consider instead the branch
	\[
	f(z) \;=\; (r_{1}r_{2})^{1/2} \, e^{\,i(\theta_{1}+\theta_{2})/2},
	\qquad -\tfrac{3\pi}{2}<\theta_{1}\le \tfrac{\pi}{2},\quad
	-\tfrac{\pi}{2}<\theta_{2}\le \tfrac{3\pi}{2}.
	\]
	State the values of \((\theta_{1}+\theta_{2})/2\) on either side of the imaginary axis,
	and hence compute \(f(\pm0+iy)\) in terms of \(y\) for \(y\in\mathbb{R}\).
	Deduce that the branch cut is along the imaginary axis
	from \(z=-i\infty\) to \(z=-i\) and from \(z=i\) to \(z=i\infty\).
	Compute \(f(x)\) in terms of \(x\) for \(x\in\mathbb{R}\).
	Show that
	\[
	f(z)\sim
	\begin{cases}
		z,  & \text{as } |z|\to\infty \text{ with } \Re(z)>0,\\[2pt]
		-z,  & \text{as } |z|\to\infty \text{ with } \Re(z)<0.
	\end{cases}
	\]
	Sketch the images of the half-planes \(\Re(z)>0\) and \(\Re(z)<0\) under the map \(\zeta=f(z)\).

	\bigskip\hrule\bigskip
```

### CP-IV-0007

- chapter line: 4469
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

We use principal branches of $\log$ and $\sqrt{\cdot}$ with branch cut $(-\infty,0]$ unless stated otherwise.
For each inverse, the principal domain is obtained by slitting the $w$â€“plane along the images of the multiple values.

\bigskip\hrule\bigskip

 \mbox{}\\[2pt]
\BoxEq{ \arcsin w = -\,i\,\log\!\Big(i\,w+\sqrt{\,1-w^{2}\,}\Big) }

 \mbox{}\\[2pt]
Branch points at $w=\pm1$; principal cuts along $(-\infty,-1]\cup[1,\infty)$.

 \mbox{}\\[2pt]
\BoxEq{ \arcsin:\ \mathbb C\setminus\big((-\infty,-1]\cup[1,\infty)\big)\ \longrightarrow\ \{\,|\Re z|<\tfrac{\pi}{2}\,\} }
For $w\in(-1,1)$, $\arcsin w\in(-\tfrac{\pi}{2},\tfrac{\pi}{2})\subset\mathbb R$.
For $w>1$,
$\arcsin w=\tfrac{\pi}{2}-i\,\operatorname{arcosh} w$ (hence $\Re=\tfrac{\pi}{2}$);
for $w<-1$,
$\arcsin w=-\tfrac{\pi}{2}+i\,\operatorname{arcosh}(-w)$ (hence $\Re=-\tfrac{\pi}{2}$).

 \mbox{}\\[2pt]
Approaching the cuts $[1,\infty)$ or $(-\infty,-1]$ forces $\Re \arcsin w\to \pm\tfrac{\pi}{2}$ and $|\Im \arcsin w|\to\infty$.
The real axis segment $(-1,1)$ maps to the real segment $(-\tfrac{\pi}{2},\tfrac{\pi}{2})$.

\bigskip\hrule\bigskip

 \mbox{}\\[2pt]
\BoxEq{ \arccos w = \frac{\pi}{2}-\arcsin w }
\BoxEq{ \arccos w = \frac{1}{i}\,\log\!\Big(w+\sqrt{w-1}\,\sqrt{w+1}\Big) }

 \mbox{}\\[2pt]
Same as $\arcsin$: branch points $\pm1$; cuts $(-\infty,-1]\cup[1,\infty)$.

 \mbox{}\\[2pt]
\BoxEq{ \arccos:\ \mathbb C\setminus\big((-\infty,-1]\cup[1,\infty)\big)\ \longrightarrow\ \{\,0<\Re z<\pi\,\} }
For $w\in(-1,1)$, $\arccos w\in(0,\pi)\subset\mathbb R$.
For $w>1$, $\arccos w=i\,\operatorname{arcosh} w$ (so $\Re=0$);
for $w<-1$, $\arccos w=\pi - i\,\operatorname{arcosh}(-w)$ (so $\Re=\pi$).

 \mbox{}\\[2pt]
The two slits map to the vertical strip boundaries $\Re z=0$ and $\Re z=\pi$.
The central interval $(-1,1)$ maps to the real segment $(0,\pi)$.

\bigskip\hrule\bigskip

 \mbox{}\\[2pt]
\BoxEq{ \arctan w = \frac{1}{2i}\,\log\!\left(\frac{1+i\,w}{\,1-i\,w\,}\right) }

 \mbox{}\\[2pt]
Branch points at $w=\pm i$; principal cuts $i(-\infty,-1]\cup i[1,\infty)$ along the imaginary axis beyond $\pm i$.

 \mbox{}\\[2pt]
\BoxEq{ \arctan:\ \mathbb C\setminus i\big((-\infty,-1]\cup[1,\infty)\big)\ \longrightarrow\ \{\,|\Re z|<\tfrac{\pi}{2}\,\} }
On $\mathbb R$, $\arctan \mathbb R=(-\tfrac{\pi}{2},\tfrac{\pi}{2})$.
Approaching $w=\pm i\,t$ ($t\ge1$) drives $\Re \arctan w\to \pm\tfrac{\pi}{2}$ and $|\Im|\to\infty$.

 \mbox{}\\[2pt]
$\arctan(-w)=-\arctan w$; conjugation across the real axis preserves values away from cuts.

\bigskip\hrule\bigskip

 \mbox{}\\[2pt]
\BoxEq{ \arccot w = \frac{1}{2i}\,\log\!\left(\frac{w+i}{\,w-i\,}\right) }
\BoxEq{ \arccot w = \frac{\pi}{2}-\arctan w }

 \mbox{}\\[2pt]
As for $\arctan$: branch points at $w=\pm i$; cuts $i(-\infty,-1]\cup i[1,\infty)$.

 \mbox{}\\[2pt]
\BoxEq{ \arccot:\ \mathbb C\setminus i\big((-\infty,-1]\cup[1,\infty)\big)\ \longrightarrow\ \{\,0<\Re z<\pi\,\} }
On $\mathbb R$, $\arccot \mathbb R=(0,\pi)$.
Approaching the cuts pins the image to $\Re z=0$ or $\Re z=\pi$ with $|\Im|\to\infty$.

\bigskip\hrule\bigskip

\[
\arcsin w + \arccos w = \frac{\pi}{2},\qquad
\arctan w + \arccot w = \frac{\pi}{2}.
\]
\[
\arcsin w = -\,i\,\operatorname{arsinh}(i w),\qquad
\arccos w = \operatorname{arcosh} w \cdot \frac{1}{i}\ \ (\text{on }[1,\infty)).
\]
\[
\arctan w = \frac{1}{2i}\big(\log(1+i w)-\log(1-i w)\big),\quad
\arccot w = \frac{1}{2i}\big(\log(w+i)-\log(w-i)\big).
\]

\medskip

	\par\noindent\textbullet\quad $\arcsin$: real on $(-1,1)$; the cuts map to $\Re z=\pm\tfrac{\pi}{2}$.
	\par\noindent\textbullet\quad $\arccos$: real on $(-1,1)$; the cuts map to $\Re z=0,\ \pi$.
	\par\noindent\textbullet\quad $\arctan$: real on $\mathbb R$; the imaginary-axis cuts beyond $\pm i$ map to $\Re z=\pm\tfrac{\pi}{2}$.
	\par\noindent\textbullet\quad $\arccot$: real on $\mathbb R$; the same cuts map to $\Re z=0,\ \pi$.

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

### CP-IV-0008

- chapter line: 5247
- atlas source solution flag: `unknown`
- linked source-solution candidates: `none`
- embedded solution marker in problem body: `NO`

```tex
(Gaussian curvature formula and isolated zeros)

Let a minimal surface be given by Weierstrass data $(f,g)$ as in Problem 8:
	\[
	X(z)=\Re\int^z \Big(\tfrac12 f(1-g^2),\ \tfrac{i}{2}f(1+g^2),\ fg\Big)\,dz.
	\]

	\medskip
	\textbf{Step 1: induced metric.}
	In the parameter $z=u+iv$ the parametrization is conformal and one has
	\[
	ds^2=\lambda^2|dz|^2,\qquad
	\lambda=\frac{|f|(1+|g|^2)}{2},
	\]
	equivalently
	\[
	E=G=\lambda^2=\frac{|f|^2(1+|g|^2)^2}{4},\qquad F=0.
	\]

	\medskip
	\textbf{Step 2: Gauss map and stereographic projection.}
	For a minimal surface, the Gauss map $N:S\to S^2$ is conformal in conformal coordinates, and its stereographic
	coordinate is precisely $g$. The round metric on $S^2$ written in the stereographic coordinate $g$ is
	\[
	ds^2_{S^2}=\frac{4}{(1+|g|^2)^2}|dg|^2,
	\]
	so the pullback satisfies
	\[
	|N_u|^2+|N_v|^2=\frac{4}{(1+|g|^2)^2}\bigl(|g_u|^2+|g_v|^2\bigr).
	\]
	Since $g$ is holomorphic (meromorphic), $g_u=g'(z)$ and $g_v=i g'(z)$, hence
	\[
	|g_u|^2+|g_v|^2=2|g'(z)|^2,
	\]
	and therefore
	\[
	|N_u|^2+|N_v|^2=\frac{8|g'|^2}{(1+|g|^2)^2}.
	\]

	\medskip
	\textbf{Step 3: relate $K$ to $dN$ for minimal surfaces.}
	In an orthonormal basis of $T_pS$, the eigenvalues of $dN_p$ are $-k_1,-k_2$.
	For a minimal surface $k_2=-k_1$, so $K=k_1k_2=-k_1^2\le 0$ and
	\[
	\|dN\|^2=k_1^2+k_2^2=2k_1^2=-2K,
	\qquad\text{hence}\qquad
	K=-\frac12\|dN\|^2.
	\]
	In conformal coordinates, an orthonormal basis is $e_1=X_u/\lambda$, $e_2=X_v/\lambda$, so
	\[
	\|dN\|^2=\frac{|N_u|^2+|N_v|^2}{\lambda^2}.
	\]
	Thus
	\[
	K=-\frac12\frac{|N_u|^2+|N_v|^2}{\lambda^2}
	=-\frac12\frac{\frac{8|g'|^2}{(1+|g|^2)^2}}{\frac{|f|^2(1+|g|^2)^2}{4}}
	=-\frac{16|g'|^2}{|f|^2(1+|g|^2)^4}.
	\]
	Equivalently,
	\[
	K=-\left(\frac{4|g'|}{|f|(1+|g|^2)^2}\right)^2.
	\]

	\medskip
	\textbf{Zeros of $K$.}
	Assume the surface is regular (no branch points), so $f\neq 0$.
	Then $K(p)=0$ iff $g'(p)=0$.
	But $g'$ is holomorphic wherever $g$ is holomorphic, hence either $g'\equiv 0$ or its zeros are isolated.
	If $g'\equiv 0$, then $g$ is constant, the Gauss map is constant, and the surface is a plane, so $K\equiv 0$.
	Otherwise, the zeros of $g'$ (hence of $K$) are isolated.
```

### CP-IV-0016

- chapter line: 5323
- atlas source solution flag: `unknown`
- linked source-solution candidates: `none`
- embedded solution marker in problem body: `NO`

```tex
â€” Conformal mappings

\noindent
	(a)\; $D$ is the region exterior to the two circles $|z-1|=1$ and $|z+1|=1$.
	Find a conformal mapping from $D$ to the exterior of the unit circle.\\
	\emph{Hint:} First apply an inversion with respect to the origin $(z\mapsto 1/z)$,
	then rotate and scale so as to use the exponential function to get to a half plane,
	from where use MĂ¶bius.

	\medskip
	\noindent
	(b)\; Find a conformal map from the unit disc $|z|<1$ onto the strip $-\pi/2<\eta<\pi/2$,
	taking the origin to the origin, $1$ to $\xi=+\infty$, $-1$ to $\xi=-\infty$.
	(Thus, the upper half of the unit circle maps to $\eta=\pi/2$ and the lower half to $\eta=-\pi/2$.)

	\medskip
	\noindent
	(c)\; Find a conformal map of the quarter-disc $0<|z|<1,\ 0<\arg z<\pi/2$
	to the upper half-plane $\eta>0$, taking $0$ to $0$, $1$ to $1$, and $i$ to $\infty$.

	\bigskip\hrule\bigskip

		\setlength{\itemsep}{0.4em}
		\par\noindent\textbullet\quad \textbf{Invert.} Let $w=1/z$. Then the circles through $0$ become lines:
		\[
		|z-1|=1 \Rightarrow \Re w=\tfrac12,\qquad
		|z+1|=1 \Rightarrow \Re w=-\tfrac12.
		\]
		Hence $D$ maps to the vertical strip $S=\{-\tfrac12<\Re w<\tfrac12\}$.
		\par\noindent\textbullet\quad \textbf{Rotate/scale to a horizontal strip.} Put $s=i\pi w$.
		Then $|\Im s|<\pi/2$.
		\par\noindent\textbullet\quad \textbf{Exponential to a half-plane.} Let $u=e^{\,s}$.
		Then $|\Im s|<\pi/2 \;\Longrightarrow\; \Re u>0$.
		\par\noindent\textbullet\quad \textbf{MĂ¶bius to exterior unit disk.} Use

	\[
	\Phi(u)=\frac{u+1}{u-1},\qquad \operatorname{Re} u>0 \longmapsto |\zeta|>1.
	\]

	Therefore a concrete map is
	\[
	\boxed{\ \zeta=\Phi\!\big(e^{\,i\pi/z}\big)=\dfrac{e^{\,i\pi/z}+1}{e^{\,i\pi/z}-1}\ }.
	\]

	\bigskip

		\setlength{\itemsep}{0.4em}
		\par\noindent\textbullet\quad \textbf{Disk to right half-plane (Cayley).}
		\[
		w=\frac{1+z}{1-z},\qquad |z|<1 \mapsto \Re w>0,
		\]
		and $z=0\mapsto w=1$, $z=1\mapsto w=\infty$, $z=-1\mapsto w=0$.
		\par\noindent\textbullet\quad \textbf{Log to a horizontal strip.}
		\[
		\zeta=\log w \quad (\text{principal branch}),\qquad \Im\zeta\in\big(-\tfrac{\pi}{2},\tfrac{\pi}{2}\big).
		\]
		Then $\zeta(0)=0$, $\zeta(1)=+\infty$, $\zeta(-1)=-\infty$.

	Hence
	\[
	\boxed{\ \zeta=\log\!\left(\frac{1+z}{1-z}\right)\ }.
	\]

	\bigskip

		\setlength{\itemsep}{0.4em}
		\par\noindent\textbullet\quad \textbf{Square to upper semicircle.}
		\[
		t=z^{2}:\quad \{0<|z|<1,\ 0<\arg z<\tfrac{\pi}{2}\}
		\longmapsto \{|t|<1,\ \Im t>0\}.
		\]
		Moreover $0\mapsto0$, $1\mapsto1$, $i\mapsto-1$.
		\par\noindent\textbullet\quad \textbf{Real MĂ¶bius to upper half-plane.}
		Find $M(t)$ with $M(-1)=\infty$, $M(0)=0$, $M(1)=1$.
		A suitable choice is
		\[
		M(t)=\frac{2t}{t+1}.
		\]

	Therefore
	\[
	\boxed{\ \zeta=M(z^{2})=\frac{2z^{2}}{z^{2}+1}\ }.
	\]
	It maps the quarter-disk conformally onto $\Im\zeta>0$ and has
	$\zeta(0)=0$, $\zeta(1)=1$, $\zeta(i)=\infty$.

	\section*{6(c)\quad Quarter-disk $0<|z|<1,\ 0<\arg z<\tfrac{\pi}{2}$
		$\longrightarrow$ upper half-plane $\Im\zeta>0$,
		with $0\mapsto0$, $1\mapsto1$, $i\mapsto\infty$}

	Construct an explicit conformal map $\zeta=\zeta(z)$ that maps the open quarter-disk
	\[
	Q=\{\,z:\ 0<|z|<1,\ 0<\arg z<\tfrac{\pi}{2}\,\}
	\]
	onto the upper half-plane $\mathbb H=\{\zeta:\ \Im\zeta>0\}$, sending the three marked boundary
	points
	\[
	z=0 \longmapsto \zeta=0,\qquad
	z=1 \longmapsto \zeta=1,\qquad
	z=i \longmapsto \zeta=\infty .
	\]

	Let
	\[
	t=z^{2}.
	\]
	Write $z=re^{i\theta}$ with $0<r<1$ and $0<\theta<\frac{\pi}{2}$. Then
	\[
	t=r^{2}e^{i(2\theta)}\quad\Rightarrow\quad |t|<1,\ \ 0<\arg t<\pi \iff \Im t>0.
	\]
	Therefore the squaring map $z\mapsto t=z^{2}$ sends $Q$ \emph{bijectively and conformally}
	onto the \emph{open upper semicircle}
	\[
	S=\{\,t:\ |t|<1,\ \Im t>0\,\}.
	\]
	On the boundary rays/arcs we have
	\[
	0\mapsto 0,\qquad 1\mapsto 1,\qquad i\mapsto -1.
	\]
	(Conformality is immediate, since $(z^{2})'=2z\neq 0$ on $Q$.)

	Seek a real-coefficient MĂ¶bius transformation
	\[
	M(t)=\frac{a t+b}{c t+d},\qquad a,b,c,d\in\mathbb R,\ \ ad-bc\neq0,
	\]
	such that
	\[
	M(-1)=\infty,\qquad M(0)=0,\qquad M(1)=1.
	\]
	Imposing the conditions:

		\par\noindent\textbullet\quad $M(-1)=\infty \ \Rightarrow\ c(-1)+d=0 \ \Rightarrow\ d=c$.
		\par\noindent\textbullet\quad $M(0)=0 \ \Rightarrow\ b/d=0 \ \Rightarrow\ b=0$.
		\par\noindent\textbullet\quad $M(1)=1 \ \Rightarrow\ a/(c+d)=1 \ \Rightarrow\ a=c+d=2c$.

	Up to an overall nonzero constant (which does not change the map), we can take $c=1$ and obtain
	\[
	\boxed{\,M(t)=\frac{2t}{t+1}\,}.
	\]

	Let $t=x+iy$ with $y>0$. Then
	\[
	M(t)=\frac{2t}{1+t},\qquad
	\Im M(t)=\frac{2\,\Im\big(t(1+\overline{t})\big)}{|1+t|^{2}}
	=\frac{2\,\Im t}{|1+t|^{2}}
	=\frac{2y}{|1+t|^{2}}
	>0.
	\]
	Hence $M$ maps $\{\,\Im t>0\,\}$ into itself; in particular it maps the upper semicircle $S$
	(which lies in $\Im t>0$) into the upper half-plane. Moreover
	\[
	M'(t)=\frac{2}{(1+t)^{2}}\neq0\quad\text{on}\ S,
	\]
	so $M$ is conformal (locally injective) there. The three-point normalization guarantees that it
	sends the three distinguished boundary points as prescribed:
	\[
	M(-1)=\infty,\qquad M(0)=0,\qquad M(1)=1.
	\]

	Define the desired map
	\[
	\boxed{\ \zeta(z)=M\big(z^{2}\big)=\frac{2z^{2}}{z^{2}+1}\ }.
	\]
	Then the normalization follows immediately:
	\[
	\zeta(0)=0,\qquad \zeta(1)=1,\qquad \zeta(i)=\infty .
	\]
	Because $t=z^{2}$ has $\Im t>0$ on $Q$ and $\Im M(t)>0$ for $\Im t>0$, we have
	\[
	\Im \zeta(z)=\Im\big(M(z^{2})\big)>0\quad\text{for all }z\in Q.
	\]
	Also $\zeta'(z)=M'(z^{2})\cdot 2z=\dfrac{4z}{(1+z^{2})^{2}}\neq0$ on $Q$, hence the map is conformal
	throughout the domain.

		\par\noindent\textbullet\quad The \emph{real radius} segment $\{\,0<z<1\,\}$ maps by $t=z^{2}$ to $(0,1)$ and then by $M$
		to $(0,1)\subset\mathbb R$; thus that edge lands on the real axis between $0$ and $1$.
		\par\noindent\textbullet\quad The \emph{imaginary radius} segment $\{\,0<iz<i\,\}$ maps by $t=z^{2}$ to $(0,-1)$ and then by $M$
		to $(0,\infty)$ on $\mathbb R$; thus the edge $0\to i$ lands on the ray $[0,\infty)$.
		\par\noindent\textbullet\quad The \emph{circular arc} $\{\,e^{i\theta}: 0<\theta<\tfrac{\pi}{2}\,\}$ maps by $t=z^{2}$ to the unit
		semicircle $\{\,e^{i\phi}: 0<\phi<\pi\,\}$ and then by $M$ to the real line as a boundary set.

	The interior of the quarter-disk maps onto $\Im\zeta>0$ by the positivity computation for $\Im M(t)$.

	The composition
	\[
	\boxed{\ \zeta(z)=\frac{2z^{2}}{z^{2}+1}\ }
	\]
	is a conformal bijection from the open quarter-disk $Q$ onto the upper half-plane $\mathbb H$,
	satisfying the three mapping conditions $0\mapsto0$, $1\mapsto1$, $i\mapsto\infty$.

	\subsection*{(b) Unit disk $\to$ strip $-\dfrac{\pi}{2}<\Im\zeta<\dfrac{\pi}{2}$}

	\textbf{Disk to right half-plane (Cayley).}
	\[
	w=\frac{1+z}{1-z},\qquad |z|<1 \;\Longrightarrow\; \operatorname{Re} w>0,
	\]
	and on the marked points
	\[
	z=0 \mapsto w=1,\qquad z=1 \mapsto w=\infty,\qquad z=-1 \mapsto w=0.
	\]
	Moreover, the unit circle $|z|=1\setminus\{1\}$ maps to the imaginary axis $\operatorname{Re} w=0$.

	\medskip
	\textbf{Log to a horizontal strip.}
	Use the principal logarithm on the right half-plane:
	\[
	\zeta=\log w=\ln|w|+i\,\arg(w),\qquad \arg(w)\in\big(-\tfrac{\pi}{2},\tfrac{\pi}{2}\big),
	\]
	so
	\[
	-\frac{\pi}{2} < \Im \zeta < \frac{\pi}{2}.
	\]
	At the marked points:
	\[
	\zeta(0)=\log 1=0,\qquad
	\zeta(1)=\log(\infty)=+\infty,\qquad
	\zeta(-1)=\log(0)=-\infty.
	\]

	\medskip
	\textbf{Which boundary goes where.}
	For $z=e^{i\theta}$,
	\[
	w=\frac{1+e^{i\theta}}{1-e^{i\theta}}
	= -\,i\,\cot\!\left(\frac{\theta}{2}\right)\in i\mathbb{R}.
	\]
	Hence
	\[
	0<\theta<\pi\ (\text{upper semicircle}) \Rightarrow \Im w<0 \Rightarrow \Im \zeta=-\frac{\pi}{2},
	\]
	\[
	\pi<\theta<2\pi\ (\text{lower semicircle}) \Rightarrow \Im w>0 \Rightarrow \Im \zeta=+\frac{\pi}{2}.
	\]
	(If one wants the upper semicircle to land on $\Im\zeta=+\pi/2$, use $\zeta=-\log\!\left(\frac{1+z}{1-z}\right)$.)

	\medskip
	\textbf{Hence}
	\[
	\boxed{\ \zeta=\log\!\left(\frac{1+z}{1-z}\right)\ }
	\]
	is a conformal bijection from $|z|<1$ onto the strip $-\pi/2<\Im\zeta<\pi/2$ with
	$0\mapsto 0$, $1\mapsto +\infty$, $-1\mapsto -\infty$.

	\subsection*{(a) Exterior of the two circles $\boldsymbol{|z-1|=1}$ and $\boldsymbol{|z+1|=1}$
		$\;\longrightarrow\;$ exterior of $\boldsymbol{|\zeta|=1}$}

	Let
	\[
	D=\big\{z\in\mathbb C:\ |z-1|\ge 1,\ |z+1|\ge 1\big\}\setminus\big(\{|z-1|=1\}\cup\{|z+1|=1\}\big),
	\]
	the region \emph{exterior to both} unit circles centered at $\pm1$.
	Construct an explicit conformal bijection $F:D\to\{\zeta:\ |\zeta|>1\}$.

	Let $w=\dfrac{1}{z}$.
	For any $a\in\mathbb C$, the circle $\{|z-a|=|a|\}$ (which passes through $0$) satisfies
	\[
	|z-a|=|a|
	\iff \left|\frac{1}{w}-a\right|=|a|
	\iff |1-aw|=|a||w|
	\iff 1=2\,\Re(aw).
	\]
	Hence circles through $0$ invert to \emph{lines}.
	For $a=1$ and $a=-1$ we obtain
	\[
	|z-1|=1 \iff \Re w=\frac{1}{2},
	\qquad
	|z+1|=1 \iff \Re w=-\frac{1}{2}.
	\]

	\emph{Which side is the exterior?}  Using $|1-aw|^{2}=(1-2\Re(aw)+|a|^{2}|w|^{2})$ we compute
	\[
	|z-1|>1
	\iff |1-w|>|w|
	\iff 1-2\Re w>0
	\iff \Re w<\frac{1}{2},
	\]
	\[
	|z+1|>1
	\iff |1+ w|>|w|
	\iff 1+2\Re w>0
	\iff \Re w>-\frac{1}{2}.
	\]
	Therefore the inversion $w=1/z$ sends $D$ bijectively onto the \emph{vertical strip}
	\[
	S=\Big\{\,w\in\mathbb C:\ -\tfrac12<\Re w<\tfrac12\,\Big\}.
	\]
	(Since $z\neq 0$ on $D$, the inversion is analytic and injective there.)

	Define
	\[
	s=i\pi w.
	\]
	Write $w=u+iv$ with $-\tfrac12<u<\tfrac12$. Then $s=i\pi(u+iv)=-\pi v+i\pi u$, so
	\[
	|\Im s|=|\pi u|<\frac{\pi}{2}.
	\]
	Consequently $S$ is mapped conformally onto the horizontal strip
	\[
	T=\Big\{\,s\in\mathbb C:\ |\Im s|<\frac{\pi}{2}\,\Big\}.
	\]

	Set
	\[
	u=e^{\,s}.
	\]
	If $s=\sigma+i\tau$ with $|\tau|<\pi/2$, then
	\[
	\Re u = \Re\big(e^{\sigma}(\cos\tau+i\sin\tau)\big)=e^{\sigma}\cos\tau>0,
	\]
	because $\cos\tau>0$ on $(-\pi/2,\pi/2)$.
	Hence $e^{(\cdot)}$ maps $T$ conformally and bijectively onto the \emph{right half-plane}
	\[
	H=\{\,u\in\mathbb C:\ \Re u>0\,\},
	\]
	and the boundary lines $\Im s=\pm\pi/2$ go to the imaginary axis $\Re u=0$.

	Consider
	\[
	\Phi(u)=\frac{u+1}{u-1}.
	\]
	For $u\in H$ we have the equivalence
	\[
	|\Phi(u)|>1
	\iff |u+1|>|u-1|
	\iff (u+1)(\bar u+1)>(u-1)(\bar u-1)
	\iff 4\,\Re u>0,
	\]
	which holds precisely on $H$. Thus $\Phi$ maps $H$ conformally onto $\{\zeta:\ |\zeta|>1\}$ and
	sends the imaginary axis to the unit circle $|\zeta|=1$.

	The composition of the four conformal bijections yields
	\[
	F:D \xrightarrow{\,z\mapsto w=1/z\,} S
	\xrightarrow{\,w\mapsto s=i\pi w\,} T
	\xrightarrow{\,s\mapsto u=e^{\,s}\,} H
	\xrightarrow{\,u\mapsto \Phi(u)\,} \{|\zeta|>1\}.
	\]
	Therefore an explicit mapping is
	\[
	\boxed{\quad \zeta = F(z) = \Phi\!\big(e^{\,i\pi/z}\big)
		= \frac{e^{\,i\pi/z}+1}{\,e^{\,i\pi/z}-1\,}\quad }.
	\]
	Every factor is analytic and injective on the relevant domain; hence $F$ is conformal and bijective from $D$ onto $\{|\zeta|>1\}$.

	As $z\to\infty$ we have $e^{\,i\pi/z}=1+\dfrac{i\pi}{z}+O(z^{-2})$, so
	\[
	\zeta
	=\frac{2+\dfrac{i\pi}{z}+O(z^{-2})}{\dfrac{i\pi}{z}+O(z^{-2})}
	= \frac{2}{i\pi}\,z\,\Big(1+O(z^{-1})\Big)
	= -\,\frac{2i}{\pi}\,z\Big(1+O(z^{-1})\Big),
	\]
	which confirms that far out in $D$ the map behaves like an affine scaling of $z$, as expected.

		\par\noindent\textbullet\quad The line $\Re w=\tfrac12$ (image of $|z-1|=1$) becomes $\Im s=\tfrac{\pi}{2}$,
		then the imaginary axis, and finally the unit circle $|\zeta|=1$.
		\par\noindent\textbullet\quad The line $\Re w=-\tfrac12$ (image of $|z+1|=1$) becomes $\Im s=-\tfrac{\pi}{2}$,
		then the same imaginary axis, and again $|\zeta|=1$.
		\par\noindent\textbullet\quad The interior $-\tfrac12<\Re w<\tfrac12$ maps to $|\Im s|<\tfrac{\pi}{2}$,
		then to $\Re u>0$, and finally to $|\zeta|>1$.

	This completes the construction and detailed verification.
```

### CP-IV-0019

- chapter line: 5690
- atlas source solution flag: `unknown`
- linked source-solution candidates: `none`
- embedded solution marker in problem body: `NO`

```tex
\par\noindent\textbullet\quad Inversion in a circle is \emph{anti-conformal} (it involves complex conjugation), and the composition of two inversions is conformal; in particular, any composition of an \emph{even} number of inversions is holomorphic (hence MĂ¶bius on $\widehat{\mathbb C}$).
```

### CP-IV-0023

- chapter line: 5697
- atlas source solution flag: `unknown`
- linked source-solution candidates: `none`
- embedded solution marker in problem body: `NO`

```tex
\par\noindent\textbullet\quad \textbf{(b)}\;
	Consider the branch defined by
	\[
	f(z) \;=\; (r_{1}r_{2})^{1/2} \, e^{\,i(\theta_{1}+\theta_{2})/2},
	\qquad -\tfrac{\pi}{2}<\theta_{1},\ \theta_{2}\le \tfrac{3\pi}{2}.
	\]
	State the values of \((\theta_{1}+\theta_{2})/2\) on either side of the imaginary axis,
	and hence compute \(f(\pm0+iy)\) in terms of \(y\) for \(y\in\mathbb{R}\).
	Deduce that the branch cut is
	\[
	S \;=\; \{\,x+iy:\ x=0,\ |y|\le 1\,\}.
	\]
	Show that \(f(z)\sim z\) as \(|z|\to\infty\)
	(i.e.\ \(f(z)/z\to 1\) as \(|z|\to\infty\)).
	Sketch the image of the cut \(z\)-plane \(\mathbb{C}\setminus S\) under the map \(\zeta=f(z)\).

	\medskip
```

### CP-IV-0043

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

### CP-IV-0052

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

### CP-IV-0086

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

### CP-IV-0107

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

### CP-IV-0124

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

### CP-IV-0135

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

### CP-IV-0138

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

### CP-IV-0001

- chapter line: 7409
- atlas source solution flag: `unknown`
- linked source-solution candidates: `none`
- embedded solution marker in problem body: `NO`

```tex
$f_n(x)=x^n$ on $[0,1]$ converges pointwise to $f=\mathbf{1}_{\{1\}}$ but not uniformly on $(0,1)$.
	\par\noindent\textbullet\quad Pointwise limit of uniformly continuous functions need not be uniformly continuous.
```

### CP-IV-0002

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

### CP-IV-0003

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

### CP-IV-0006

- chapter line: 7460
- atlas source solution flag: `unknown`
- linked source-solution candidates: `none`
- embedded solution marker in problem body: `NO`

```tex
\par\noindent (ii)\quad Let $g$ be an entire function such that $|f(z)|\le |g(z)|$ for all $z\in\mathbb C$.
	Show that there exists $c\in\mathbb C$ such that $f(z)=c\,g(z)$ for all $z\in\mathbb C$.

\bigskip\hrule\bigskip
```

### CP-IV-0010

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

### CP-IV-0011

- chapter line: 7526
- atlas source solution flag: `unknown`
- linked source-solution candidates: `none`
- embedded solution marker in problem body: `NO`

```tex
\par\noindent\textbullet\quad If $f_n \Rightarrow f$ uniformly on $\mathbb{R}$, prove that $f$ is uniformly continuous.
```

### CP-IV-0013

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

### CP-IV-0021

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

### CP-IV-0022

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

### CP-IV-0026

- chapter line: 7615
- atlas source solution flag: `unknown`
- linked source-solution candidates: `none`
- embedded solution marker in problem body: `NO`

```tex
\par\noindent\textbullet\quad $\{(x,y): y\ne 0\}$.
```

### CP-IV-0030

- chapter line: 7643
- atlas source solution flag: `unknown`
- linked source-solution candidates: `none`
- embedded solution marker in problem body: `NO`

```tex
\par\noindent\textbullet\quad $\{(x,0): 0\le x\le 1\}$.
```

### CP-IV-0032

- chapter line: 7648
- atlas source solution flag: `unknown`
- linked source-solution candidates: `none`
- embedded solution marker in problem body: `NO`

```tex
$f(x)=x^2$ on $\mathbb{R}$ is not uniformly continuous.
	\par\noindent\textbullet\quad Pointwise convergence $\nRightarrow$ uniform convergence.
```

### CP-IV-0033

- chapter line: 7654
- atlas source solution flag: `unknown`
- linked source-solution candidates: `none`
- embedded solution marker in problem body: `NO`

```tex
\par\noindent\textbullet\quad Show that the map $f \mapsto \displaystyle\Big(x\mapsto \int_a^x f(y)\,dy\Big)$ is a continuous map from $C^k([a,b])$ to $C^{k+1}([a,b])$.
```

### CP-IV-0038

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

### CP-IV-0040

- chapter line: 7670
- atlas source solution flag: `unknown`
- linked source-solution candidates: `none`
- embedded solution marker in problem body: `NO`

```tex
\par\noindent\textbullet\quad $A=\{f\in C([0,1]) : f(1/2)=0\}$;
```

### CP-IV-0041

- chapter line: 7675
- atlas source solution flag: `unknown`
- linked source-solution candidates: `none`
- embedded solution marker in problem body: `NO`

```tex
\par\noindent\textbullet\quad If $X=\mathbb{N}$, show that $(f_n)$ has a pointwise convergent subsequence.
```

### CP-IV-0042

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

### CP-IV-0046

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

### CP-IV-0050

- chapter line: 7816
- atlas source solution flag: `unknown`
- linked source-solution candidates: `none`
- embedded solution marker in problem body: `NO`

```tex
\par\noindent\textbullet\quad $f_n(x)=x e^{-nx}$ on $X=[0,\infty)$.
```

### CP-IV-0054

- chapter line: 7821
- atlas source solution flag: `unknown`
- linked source-solution candidates: `none`
- embedded solution marker in problem body: `YES`

```tex
\par\noindent\textbullet\quad (\textbf{CR in matrix form})
	Show $T$ is complex-linear iff $a=d$ and $b=-c$.
	\emph{Solution.} From Ex.\ 1, $B=0\iff a=d,\ c=-b$, i.e.\ matrix $\begin{psmallmatrix}a&-t\\ t&a\end{psmallmatrix}$.
```

### CP-IV-0055

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

### CP-IV-0056

- chapter line: 7841
- atlas source solution flag: `unknown`
- linked source-solution candidates: `none`
- embedded solution marker in problem body: `NO`

```tex
\par\noindent\textbullet\quad $\{(x,y): y/x\in\mathbb{N}\}\ \cup\ \{(x,y): x=0\}$.
```

### CP-IV-0058

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

### CP-IV-0059

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

### CP-IV-0063

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

### CP-IV-0067

- chapter line: 7982
- atlas source solution flag: `unknown`
- linked source-solution candidates: `none`
- embedded solution marker in problem body: `NO`

```tex
\par\noindent\textbullet\quad Show that $C^k([a,b])$ is a complete metric space.
```

### CP-IV-0068

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

### CP-IV-0071

- chapter line: 7995
- atlas source solution flag: `unknown`
- linked source-solution candidates: `none`
- embedded solution marker in problem body: `NO`

```tex
\par\noindent\textbullet\quad $f_n(x)=x^{2n}$ on $X=(0,1)$.
```

### CP-IV-0075

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

### CP-IV-0081

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

### CP-IV-0083

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

### CP-IV-0085

- chapter line: 8177
- atlas source solution flag: `unknown`
- linked source-solution candidates: `none`
- embedded solution marker in problem body: `NO`

```tex
\par\noindent\textbullet\quad $\{(x,0): 0< x< 1\}$.
```

### CP-IV-0087

- chapter line: 8182
- atlas source solution flag: `unknown`
- linked source-solution candidates: `none`
- embedded solution marker in problem body: `NO`

```tex
\par\noindent\textbullet\quad $\{(x,y): y>0\}$.
```

### CP-IV-0088

- chapter line: 8187
- atlas source solution flag: `unknown`
- linked source-solution candidates: `none`
- embedded solution marker in problem body: `NO`

```tex
\par\noindent (i)\quad Show that $X$ is totally bounded.
```

### CP-IV-0091

- chapter line: 8192
- atlas source solution flag: `unknown`
- linked source-solution candidates: `none`
- embedded solution marker in problem body: `NO`

```tex
â€” constant curl, easy numbers

Take $\mathbf F=(-y,x)$. Then $L=-y$, $M=x$ and
\[
M_x - L_y \;=\; \partial_x(x) - \partial_y(-y) \;=\; 1 - (-1) \;=\; 2 \quad(\text{constant}).
\]
Area integral:
\[
\iint_{D} (M_x-L_y)\,dA
\;=\;
\iint_{D} 2\,dA
\;=\; 2\,\pi R^2.
\]
Line integral (check by parametrizing $C$):
\[
dx=-R\sin t\,dt,\qquad dy=R\cos t\,dt,
\]
\[
L\,dx+M\,dy
=
(-y)\,dx + (x)\,dy
=
(-R\sin t)(-R\sin t)\,dt + (R\cos t)(R\cos t)\,dt
=
R^2\,dt,
\]
\[
\oint_{C} (L\,dx+M\,dy)
=
\int_{0}^{2\pi} R^2\,dt
=
2\pi R^2.
\]
Both sides match: $2\pi R^2$.
```

### CP-IV-0093

- chapter line: 8230
- atlas source solution flag: `unknown`
- linked source-solution candidates: `none`
- embedded solution marker in problem body: `YES`

```tex
\par\noindent\textbullet\quad (\textbf{Operator norm and singular values})
	Show the maximal and minimal stretch factors (singular values) of $T$ are
	\[
	\sigma_{\max}=|A|+|B|,\qquad \sigma_{\min}=\bigl||A|-|B|\bigr|.
	\]
	\emph{Solution (sketch).} Write $T(z)=A\bigl(z+\tfrac{B}{A}\bar z\bigr)$ if $A\neq0$; by rotating/scaling the domain and range one reduces to $A\ge0$, $B\ge0$ real. Then $T$ acts by stretching along two orthogonal directions with factors $A\pm B$, giving the claim. General case follows by unitary conjugation.
```

### CP-IV-0094

- chapter line: 8240
- atlas source solution flag: `unknown`
- linked source-solution candidates: `none`
- embedded solution marker in problem body: `NO`

```tex
\par\noindent\textbullet\quad \textbf{Derivative not continuous from $(C^1,\|\cdot\|_\infty)$ to $(C,\|\cdot\|_\infty)$.}

	Take $f_n(x)=\tfrac{1}{n}\sin(n^2 x)$ on $[0,1]$.
	We have
	\[
	\|f_n\|_\infty=\frac{1}{n}\longrightarrow 0,
	\qquad
	\|f_n'\|_\infty = n \longrightarrow \infty .
	\]
	Hence $D$ is discontinuous with these norms.

	\medskip
```

### CP-IV-0095

- chapter line: 8256
- atlas source solution flag: `unknown`
- linked source-solution candidates: `none`
- embedded solution marker in problem body: `NO`

```tex
$|x|^3$ is $C^2$ with
$f'(x)=3x^2$ for $x>0$ and $f'(x)=-3x^2$ for $x<0$,
$f''(x)=6x$ for $x>0$ and $f''(x)=-6x$ for $x<0$, both extending continuously at $0$ by $0$,
while $f^{(3)}(x)=6$ for $x>0$ and $f^{(3)}(x)=-6$ for $x<0$, so $f^{(3)}$ has a jump at $0$.
```

### CP-IV-0100

- chapter line: 8264
- atlas source solution flag: `unknown`
- linked source-solution candidates: `none`
- embedded solution marker in problem body: `NO`

```tex
\par\noindent\textbullet\quad \textbf{Integration map is Lipschitz $C^k\!\to C^{k+1}$.}

	For $f,g\in C^k$ put $F=T(f)$ and $G=T(g)$ with
	\[
	F(x)=\int_a^x f(y)\,dy, \qquad G(x)=\int_a^x g(y)\,dy .
	\]
	Then
	\[
	\|F-G\|_\infty \;\le\; (b-a)\,\|f-g\|_\infty,
	\]
	and for $1\le j\le k+1$,
	\[
	\|F^{(j)}-G^{(j)}\|_\infty \;=\; \|f^{(j-1)}-g^{(j-1)}\|_\infty .
	\]
	Consequently,
	\[
	d_{C^{k+1}}(T(f),T(g))
	\;\le\; \max\{1,b-a\}\; d_{C^k}(f,g).
	\]

	\medskip
```

### CP-IV-0101

- chapter line: 8289
- atlas source solution flag: `unknown`
- linked source-solution candidates: `none`
- embedded solution marker in problem body: `YES`

```tex
\par\noindent\textbullet\quad (\textbf{Wirtinger derivatives})
	For $T(z)=Az+B\bar z$, compute $\partial T/\partial z$ and $\partial T/\partial\bar z$.
	\emph{Solution.} $\displaystyle \frac{\partial T}{\partial z}=A,\qquad \frac{\partial T}{\partial\bar z}=B$.
```

### CP-IV-0103

- chapter line: 8296
- atlas source solution flag: `unknown`
- linked source-solution candidates: `none`
- embedded solution marker in problem body: `YES`

```tex
\par\noindent\textbullet\quad (\textbf{Matrix from $A,B$})
	Given $T(z)=Az+B\bar z$ with $A=\alpha+i\beta$, $B=\gamma+i\delta$ ($\alpha,\beta,\gamma,\delta\in\mathbb{R}$), show the real matrix is
	\[
	\begin{pmatrix}
		\alpha+\gamma & -\beta+\delta\\
		\beta+\delta & \alpha-\gamma
	\end{pmatrix}.
	\]
	\emph{Solution.} Expand $Az+B\bar z$ with $z=x+iy$ and collect $(x,y)$ coefficients.
```

### CP-IV-0105

- chapter line: 8336
- atlas source solution flag: `unknown`
- linked source-solution candidates: `none`
- embedded solution marker in problem body: `NO`

```tex
Show that the following functions do not have antiderivatives on the indicated domains:
\[
\text{(a)}\; f(z)=\frac{1}{z}-\frac{1}{z-1}\quad\text{on } \{\,0<|z|<1\,\},\qquad
\text{(b)}\; g(z)=\frac{z}{1+z^{2}}\quad\text{on } \{\,1<|z|<\infty\,\}.
\]
```

### CP-IV-0108

- chapter line: 8345
- atlas source solution flag: `unknown`
- linked source-solution candidates: `none`
- embedded solution marker in problem body: `NO`

```tex
Let $T:\mathbb{R}^2\to\mathbb{R}^2$ be a real-linear map. Regard $T$ as a map $\mathbb{C}\to\mathbb{C}$ via $(x,y)\leftrightarrow x+iy$.
	Show that there exist unique $A,B\in\mathbb{C}$ such that
	\[
	T(z)=Az+B\overline{z}\qquad(\forall\,z\in\mathbb{C}),
	\]
	and that $T$ is complex differentiable (i.e.\ $\mathbb{C}$-linear) iff $B=0$.
```

### CP-IV-0115

- chapter line: 8470
- atlas source solution flag: `unknown`
- linked source-solution candidates: `none`
- embedded solution marker in problem body: `NO`

```tex
Take
	\[
	a = 0.5 + 0.2i, \qquad \theta = \frac{\pi}{4},
	\]
	and define
	\[
	\phi(z) = \phi_{a,\theta}(z)
	= e^{i\pi/4}\,\frac{z-a}{1-\overline{a}\,z}.
	\]
	Then $\phi(a)=0$, and $\phi$ maps $\mathbb D$ onto itself while
	distorting the radial/circular grid in a non-trivial way.

	Figures~\ref{fig:disk-auto-z} and \ref{fig:disk-auto-w} show the unit
	disk and its image under $\phi$.
```

### CP-IV-0119

- chapter line: 8502
- atlas source solution flag: `unknown`
- linked source-solution candidates: `none`
- embedded solution marker in problem body: `NO`

```tex
(Conjugation).

Let $T(z)=\bar z$. Then $A=0$, $B=1$.
The unit circle is fixed as a set, but orientation is reversed. $T$ is not complex-differentiable since $B\neq0$.
```

### CP-IV-0120

- chapter line: 8510
- atlas source solution flag: `unknown`
- linked source-solution candidates: `none`
- embedded solution marker in problem body: `NO`

```tex
\par\noindent\textbullet\quad \textbf{Total boundedness still fails (infinite dimension).}

	Closed balls in $(C^k,d_{C^k})$ are complete but not totally bounded.
	For instance, translate a fixed bump function to disjoint locations;
	the resulting family lies in the unit ball and remains pairwise well separated.
```

### CP-IV-0121

- chapter line: 8519
- atlas source solution flag: `unknown`
- linked source-solution candidates: `none`
- embedded solution marker in problem body: `NO`

```tex
Compute $\displaystyle \int_{0}^{2\pi} e^{\,e^{it}}\,dt$.

Let $z=e^{it}$ so that $|z|=1$ and $dt=\frac{dz}{iz}$. Then
\[
\int_{0}^{2\pi} e^{e^{it}}\,dt
=\frac1i\oint_{|z|=1}\frac{e^{z}}{z}\,dz.
\]
By Cauchyâ€™s integral formula for $f(z)=e^{z}$,
\[
\oint_{|z|=1}\frac{e^{z}}{z}\,dz=2\pi i\,f(0)=2\pi i.
\]
Hence
\[
\boxed{\displaystyle \int_{0}^{2\pi} e^{\,e^{it}}\,dt=2\pi }.
\]

Since $e^{e^{it}}=\sum_{n=0}^\infty \frac{e^{int}}{n!}$, the integral over $[0,2\pi]$
kills all terms with $n\neq0$ and equals $2\pi$.
```

### CP-IV-0122

- chapter line: 8541
- atlas source solution flag: `unknown`
- linked source-solution candidates: `none`
- embedded solution marker in problem body: `NO`

```tex
\par\noindent\textbullet\quad $U=(0,1)\cup(2,3)$.
```

### CP-IV-0127

- chapter line: 8575
- atlas source solution flag: `unknown`
- linked source-solution candidates: `none`
- embedded solution marker in problem body: `NO`

```tex
\par\noindent\textbullet\quad \textbf{Concrete identity.}

	With $f(x)=\sin x$ on $[0,1]$,
	\[
	T(f)(x)=\int_0^x\sin y\,dy = 1-\cos x,
	\]
	so $D(T(f))=f$, while $D(f)=\cos x$ and
	\[
	T(D(f))(x)=\int_0^x \cos y\,dy=\sin x=f(x).
	\]
```

### CP-IV-0130

- chapter line: 8614
- atlas source solution flag: `unknown`
- linked source-solution candidates: `none`
- embedded solution marker in problem body: `NO`

```tex
\par\noindent\textbullet\quad \textbf{Derivative map is $1$-Lipschitz $C^{k+1}\!\to C^{k}$.}

	For $f,g\in C^{k+1}$ we have
	\[
	d_{C^{k}}(f',g')
	=\sum_{j=0}^{k} \|f^{(j+1)}-g^{(j+1)}\|_\infty
	\;\le\;
	\sum_{j=0}^{k+1} \|f^{(j)}-g^{(j)}\|_\infty
	= d_{C^{k+1}}(f,g).
	\]

	\medskip
```

### CP-IV-0132

- chapter line: 8663
- atlas source solution flag: `unknown`
- linked source-solution candidates: `none`
- embedded solution marker in problem body: `NO`

```tex
$f_n(x)=\arctan(nx)$ (each UC) $\to$ a step function, which is not UC.
```

### CP-IV-0136

- chapter line: 8668
- atlas source solution flag: `unknown`
- linked source-solution candidates: `none`
- embedded solution marker in problem body: `NO`

```tex
â€” gradient field (curl $=0$), circulation $=0$

Let $\phi(x,y)=x^2+y^3$ and $\mathbf F=\nabla\phi=(2x,\,3y^2)$.
Then
\[
M_x - L_y
=
\partial_x(3y^2)-\partial_y(2x)
=
0-0
=
0,
\]
so
\[
\oint_{C} (2x\,dx+3y^2\,dy)
=
\iint_{D} 0\,dA
=
0.
\]
\emph{Interpretation:} exact/gradient fields do no net work around closed curves.
```

### CP-IV-0060

- chapter line: 8733
- atlas source solution flag: `unknown`
- linked source-solution candidates: `none`
- embedded solution marker in problem body: `NO`

```tex
(Weierstrass data for catenoid and helicoid)

We use the Weierstrass representation in the $(f,g)$-form:
	\[
	X(z)=\Re\int^z \Big(\tfrac12 f(1-g^2),\ \tfrac{i}{2}f(1+g^2),\ fg\Big)\,dz,
	\]
	where $g$ is meromorphic, $f$ is holomorphic, and the resulting parametrization is conformal and minimal.

	\medskip
	\textbf{Choice of complex parameter.}
	For the given real parameters $(u,v)$, the catenoid/helicoid are conformal in $(u,v)$, and it is convenient to set
	\[
	z=v+iu.
	\]
	Thus a suitable domain is the strip
	\[
	D=\{z=v+iu\in\mathbb{C}:\ v\in\mathbb{R},\ 0<u<2\pi\}.
	\]

	\medskip
	\textbf{Catenoid.}
	Take
	\[
	g(z)=e^{z},\qquad f(z)=a e^{-z}.
	\]
	Then
	\[
	\tfrac12 f(1-g^2)=\frac{a}{2}(e^{-z}-e^{z})=-a\sinh z,\qquad
	\tfrac{i}{2}f(1+g^2)=\frac{ia}{2}(e^{-z}+e^{z})=i a\cosh z,
	\]
	and $fg=a$. Hence
	\[
	X(z)=\Re\bigl(-a\cosh z,\ i a\sinh z,\ a z\bigr).
	\]
	With $z=v+iu$ this becomes (up to a rigid motion in the $xy$-plane)
	\[
	X(u,v)=\bigl(a\cosh v\cos u,\ a\cosh v\sin u,\ a v\bigr),
	\]
	which is exactly the given catenoid parametrization (possibly after rotating by $\pi$ about the $z$-axis).

	\medskip
	\textbf{Helicoid.}
	Keep the same $g(z)=e^{z}$ but replace $f$ by $if$:
	\[
	g(z)=e^{z},\qquad f(z)= i a e^{-z}.
	\]
	This is the classical associate surface construction. Substituting yields a parametrization which, after a rigid motion
	and a harmless shift of $u$, is the given helicoid
	\[
	\phi(u,v)=\bigl(a\sinh v\cos u,\ a\sinh v\sin u,\ a u\bigr).
	\]
	(Geometrically: multiplying $f$ by $i$ rotates the Weierstrass integrand by $90^\circ$ in the associate family.)

	\bigskip
```

