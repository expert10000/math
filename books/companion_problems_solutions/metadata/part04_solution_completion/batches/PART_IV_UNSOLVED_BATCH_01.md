# Part IV Unsolved Solution Authoring Batch 01

- problems in batch: 20
- IDs: CP-IV-0009, CP-IV-0012, CP-IV-0014, CP-IV-0017, CP-IV-0034, CP-IV-0035, CP-IV-0037, CP-IV-0039, CP-IV-0047, CP-IV-0051, CP-IV-0065, CP-IV-0066, CP-IV-0069, CP-IV-0084, CP-IV-0089, CP-IV-0096, CP-IV-0097, CP-IV-0102, CP-IV-0106, CP-IV-0116

Author canonical worked solutions for these problems. Do not alter the problem statements.

## CP-IV-0009


- chapter line: 56
- atlas source solution flag: `unknown`
- linked source-solution candidates: `none`
- embedded solution marker in problem body: `NO`

```tex
\par\noindent\textbullet\quad \textbf{Removable:} $f$ is bounded near $a$ $\Rightarrow$ $f$ extends holomorphically to $a$ (Riemann).
```

## CP-IV-0012


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

## CP-IV-0014


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

## CP-IV-0017


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

## CP-IV-0034


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

## CP-IV-0035


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

## CP-IV-0037


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

## CP-IV-0039


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

## CP-IV-0047


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

## CP-IV-0051


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

## CP-IV-0065


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

## CP-IV-0066


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

## CP-IV-0069


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

## CP-IV-0084


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

## CP-IV-0089


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

## CP-IV-0096


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

## CP-IV-0097


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

## CP-IV-0102


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

## CP-IV-0106


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

## CP-IV-0116


- chapter line: 2778
- atlas source solution flag: `unknown`
- linked source-solution candidates: `none`
- embedded solution marker in problem body: `NO`

```tex
(Rotationâ€“scaling; holomorphic).

Let $T(z)=\lambda z$ with $\lambda=1.3 e^{i\pi/6}$. Then $A=\lambda$, $B=0$.
The image of the unit circle is a circle of radius $1.3$ rotated by $\pi/6$, and $T$ preserves angles and orientation.
```

