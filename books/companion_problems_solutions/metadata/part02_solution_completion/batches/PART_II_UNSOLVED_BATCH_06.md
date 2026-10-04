# Part II missing-solution batch 06

- problems: **20**
- IDs: CP-II-0554, CP-II-0568, CP-II-0010, CP-II-0032, CP-II-0048, CP-II-0055, CP-II-0059, CP-II-0088, CP-II-0132, CP-II-0135, CP-II-0212, CP-II-0298, CP-II-0325, CP-II-0354, CP-II-0417, CP-II-0428, CP-II-0433, CP-II-0435, CP-II-0436, CP-II-0473

## CP-II-0554

- chapter line: 9179

```tex
\label{prob:cp-ii-0554}
\par\noindent\textbullet\quad $U=[0,1]$. What if we replace the metric space $\mathbb{R}$ by the metric space $[-1,1]$, the metric space $(0,1)$, or the metric space $[0,2]$, in each case with the subspace metric inherited from the Euclidean metric?
```

## CP-II-0568

- chapter line: 9333

```tex
\label{prob:cp-ii-0568}
\par\noindent\textbullet\quad \emph{Stronger converse (extreme values).}
	If, in addition, every continuous $f:E\to\mathbb R$ attains its maximum on $E$, then $E$ is
	compact: closedness follows as above, boundedness from $x\mapsto\|x\|$, and now Heine--Borel.
```

## CP-II-0010

- chapter line: 9578

```tex
\label{prob:cp-ii-0010}
Assume $f:\mathbb{R}\to\mathbb{R}$ differentiable with $|f'(x)|\le M$ for all $x$.

\par\noindent\textbullet\quad $|f(x)-f(y)|\le M|x-y|$ by MVT.
\par\noindent\textbullet\quad Hence $f$ is uniformly continuous (Lipschitz with constant $M$).
```

## CP-II-0032

- chapter line: 9610

```tex
\label{prob:cp-ii-0032}
Let $f:\mathbb{R}^2\to\mathbb{R}$ and $(x_0,y_0)\in\mathbb{R}^2$.

		\par\noindent\textbullet\quad Suppose $\partial_1 f$ exists and is continuous in an open ball around $(x_0,y_0)$,
		and $\partial_2 f$ exists at $(x_0,y_0)$. Show that $f$ is differentiable at $(x_0,y_0)$.
		\par\noindent\textbullet\quad Suppose instead $\partial_1 f$ exists and is bounded in an open ball around $(x_0,y_0)$,
		and that for fixed $x$, the map $y\mapsto f(x,y)$ is continuous.
		Show that $f$ is continuous at $(x_0,y_0)$.


	\textbf{Theory.}
	A function $f:\mathbb{R}^2\to\mathbb{R}$ is differentiable at $(x_0,y_0)$ if
	there exists a linear map $L(h,k)=a h+b k$ with
	\[
	\lim_{(h,k)\to(0,0)}
	\frac{f(x_0+h,y_0+k)-f(x_0,y_0)-a h-b k}{\sqrt{h^2+k^2}}=0.
	\]
	Continuous partials near a point guarantee differentiability there.
	Bounded partials plus separate continuity imply overall continuity.
```

## CP-II-0048

- chapter line: 9704

```tex
\label{prob:cp-ii-0048}
Consider the map $f:\mathbb{R}^n\to\mathbb{R}^n$ given by
	\[
	f(x)=\frac{x}{\|x\|}\ \text{for }x\ne0,\qquad f(0)=0.
	\]

		\par\noindent\textbullet\quad Using the definition of derivative, show that $x\mapsto\|x\|^2$ is differentiable and compute its derivative.
		\textit{(Avoid using partial derivatives.)}
		\par\noindent\textbullet\quad Using part (a) and questions 5(b)--5(c), show that $f$ is differentiable except at $0$ and that
		\[
		Df|_x(h)=\frac{h}{\|x\|}-\frac{x(x\!\cdot\!h)}{\|x\|^3}.
		\]
		\textit{(Avoid using partial derivatives.)}
		\par\noindent\textbullet\quad Verify that $Df|_x(h)$ is orthogonal to $x$ and explain geometrically why.


	\textbf{Theory.}
	Differentiability in $\mathbb{R}^n$ means
	\[
	f(x+h)-f(x)=Df|_x(h)+o(\|h\|).
	\]
	For $g(x)=\langle x,x\rangle=\|x\|^2$ we use the product rule of the inner product.
	For $f(x)=x/\|x\|$ we use the scalar–vector product and the chain rule.
```

## CP-II-0055

- chapter line: 9731

```tex
\label{prob:cp-ii-0055}
\par\noindent\textbullet\quad The Gaussian $f(x)=e^{-|x|^2}$ belongs to $\mathcal{S}(\mathbb{R}^n)$,
	since each derivative is a polynomial times $e^{-|x|^2}$.
```

## CP-II-0059

- chapter line: 9737

```tex
\label{prob:cp-ii-0059}
Define $f:M_n\to M_n$ by $f(A)=A^2$.

		\par\noindent\textbullet\quad Show that $f$ is continuously differentiable on the whole of $M_n$.
		\par\noindent\textbullet\quad Deduce that there is a continuous square-root function on some neighbourhood of the identity~$\mathrm{Id}$;
		that is, show that there exists an open ball $B_\varepsilon(\mathrm{Id})$ and a continuous function
		$g:B_\varepsilon(\mathrm{Id})\to M_n$ such that $g(A)^2=A$ for all $A\in B_\varepsilon(\mathrm{Id})$.
		\par\noindent\textbullet\quad Is it possible to define a continuous square-root function on the whole of $M_n$?


	\textbf{Theory.}
	Matrix multiplication $(A,B)\mapsto AB$ is bilinear and continuous on $M_n\times M_n$.
	Hence polynomial maps in $A$ are continuously differentiable.
	The derivative of $A\mapsto A^2$ at $A$ is given by
	\[
	Df|_A(H)=AH+HA.
	\]
	The Inverse Function Theorem in Banach spaces guarantees a local inverse of $f$ near points where $Df|_A$ is invertible.
```

## CP-II-0088

- chapter line: 9823

```tex
\label{prob:cp-ii-0088}
Derivative filters.

If $g = f'$, then formally
\[
f * f'
= \frac{d}{dx}\,(f*f).
\]
More generally, for a multiindex $\alpha$,
\[
\partial^\alpha(f*g)
= (\partial^\alpha f)*g
= f*(\partial^\alpha g).
\]

\medskip
\noindent$\Rightarrow$ \emph{Effect:} convolution propagates derivatives
and can act as a differentiating filter.

\bigskip\hrule\bigskip
```

## CP-II-0132

- chapter line: 9978

```tex
\label{prob:cp-ii-0132}
— Matrix squaring and local square root

\textbf{Statement.}\quad

Define $f:\mathcal{M}_n\to\mathcal{M}_n$ by $f(A)=A^2$.
Show that $f$ is continuously differentiable on $\mathcal{M}_n$.
Deduce that there exists $\varepsilon>0$ such that, on the open ball
$B_\varepsilon(I)\subset\mathcal{M}_n$, there is a continuous map
\[
g:B_\varepsilon(I)\longrightarrow \mathcal{M}_n
\]
satisfying $g(A)^2=A$ for all $A\in B_\varepsilon(I)$.
Discuss whether one can define a continuous square-root function on the whole $\mathcal{M}_n$.

\bigskip\hrule\bigskip

\textbf{Theory \& Solution.}\quad

\textbf{(Derivative of $f$).}\;
For $A,H\in\mathcal{M}_n$,
\[
f(A+H)=(A+H)^2=A^2+AH+HA+H^2,
\]
hence
\[
Df(A)(H)=AH+HA.
\]
This is linear in $H$ and depends continuously on $A$,
so $f$ is $C^1$ on $\mathcal{M}_n$.

\medskip

\textbf{(Local inverse near $I$).}\;
At $A=I$, $Df(I)(H)=2H$, which is invertible as a linear map on $\mathcal{M}_n$.
By the inverse function theorem, there exist $\varepsilon>0$
and a $C^1$ map $g:B_\varepsilon(I)\to\mathcal{M}_n$ such that
$g(I)=I$ and $f(g(A))=A$, i.e.\ $g(A)^2=A$ for all $A$ in $B_\varepsilon(I)$.

\medskip

\textbf{(Global impossibility).}\;
A continuous square-root map cannot exist globally on $\mathcal{M}_n$:
for example, $\det(g(A))^2=\det(A)$ forces $\det(g(A))$ to change sign
discontinuously when $\det(A)$ crosses $0$.

\bigskip\hrule\bigskip

\textbf{Examples.}\quad
 \setlength{\itemsep}{6pt}
	\par\noindent\textbullet\quad For scalars ($n=1$), $f(x)=x^2$ and $Df(1)=2$.
	By the inverse function theorem, $x\mapsto\sqrt{x}$ exists and is smooth near $1$,
	but no continuous square root exists on all of $\mathbb{R}$.
	\par\noindent\textbullet\quad For matrices, the same holds: locally near $I$, each $A$ close to $I$ has a
	unique square root $g(A)$ obtained by a convergent binomial series.
```

## CP-II-0135

- chapter line: 10036

```tex
\label{prob:cp-ii-0135}
Parabola $y^2 - x = 0$

Consider
	\[
	f(x,y) = y^2 - x.
	\]
	We study where the Implicit Function Theorem (IFT) allows us to express the curve as a function.

	\[
	f_x = -1,
	\qquad
	f_y = 2y.
	\]

		\par\noindent\textbullet\quad At $(0,0)$: $f_y(0,0)=0$ (bad for $y=g(x)$), but $f_x(0,0)=-1\neq0$ (good for $x=h(y)$).
		\par\noindent\textbullet\quad At a point with $y_0\neq0$: $f_y(x_0,y_0)=2y_0\neq0$ (good for $y=g(x)$).

	The IFT gives a unique $x=h(y)$ with $h(0)=0$ and $f(h(y),y)=0$.
	From $y^2 - x = 0$, we get
	\[
	\boxed{x = h(y) = y^2.}
	\]
	Differentiate using the IFT formula (solving for the first variable):
	\[
	h'(y) = -\frac{f_y}{f_x}\Big|_{(h(y),y)} = -\frac{2y}{-1} = 2y,
	\qquad
	h''(y) = 2.
	\]

	The IFT gives a local branch $y=g(x)$ through $(x_0,y_0)$ with
	\[
	\boxed{g'(x) = -\frac{f_x}{f_y}\Big|_{(x,g(x))} = \frac{1}{2g(x)}.}
	\]
	Concretely, the two branches are $y=\pm\sqrt{x}$, so on the upper one
	\[
	g'(x) = \frac{1}{2\sqrt{x}}
	\]
	which blows up as $x\to 0^+$.

	IFT does not apply (e.g.\ at cusps).
	For this parabola, that never happens on the curve except at the vertex where
	$f_y=0$ but $f_x\neq0$, so we still solve for $x$ as $h(y)=y^2$.
```

## CP-II-0212

- chapter line: 10353

```tex
\label{prob:cp-ii-0212}
\par\noindent\textbullet\quad In particular $f\in L^p(\mathbb{R}^n)$ for all $1\le p\le\infty$,
	and the same holds for all derivatives $D^\alpha f$.
```

## CP-II-0298

- chapter line: 10549

```tex
\label{prob:cp-ii-0298}
\par\noindent\textbullet\quad If $f\in\mathcal{S}$, then all derivatives $D^\alpha f$,
	translations $x\mapsto f(x-a)$, and polynomial multiples
	$x\mapsto P(x)f(x)$ also lie in $\mathcal{S}$.

Let $f\in\mathcal{S}(\mathbb{R}^n)$.
```

## CP-II-0325

- chapter line: 10627

```tex
\label{prob:cp-ii-0325}
Show that $f:\mathbb{R}^2\to\mathbb{R}$ is everywhere differentiable and compute the differential.

	\par\noindent\textbullet\quad $f(x,y)=x^2+y^2-x-xy$.
	\[
	Df(x,y)=(2x-1-y,\;2y-x).
	\]

	\par\noindent\textbullet\quad $f(x,y)=\dfrac{1}{\sqrt{1+x^2+y^2}}$.
	\[
	Df(x,y)=\left(-\frac{x}{(1+x^2+y^2)^{3/2}},\; -\frac{y}{(1+x^2+y^2)^{3/2}}\right).
	\]

	\par\noindent\textbullet\quad $f(x,y)=x^5y^2$.
	\[
	Df(x,y)=(5x^4y^2,\;2x^5y).
	\]
```

## CP-II-0354

- chapter line: 10675

```tex
\label{prob:cp-ii-0354}
For $x=(1,0,0)$, $Df(x)(h)=h-(h_1,0,0)=(0,h_2,h_3)$, tangent to $S^2$ at $(1,0,0)$.
\hfill$\Box$

\bigskip\hrule\bigskip

\section*{Problem 6 -- Differentiability of $|x||y|$ and $\dfrac{xy}{\sqrt{x^2+y^2}}$}

Partial derivatives:
\[
f_x(x,y)=\operatorname{sgn}(x)|y|,\qquad
f_y(x,y)=|x|\operatorname{sgn}(y).
\]
Hence $f$ is differentiable wherever $x\ne0$ and $y\ne0$.
On the axes, $\operatorname{sgn}$ is discontinuous, so $f$ fails to be differentiable there.

\par\medskip\noindent\textbf{(b) Function $g(x,y)=\dfrac{xy}{\sqrt{x^2+y^2}}$, $g(0,0)=0$.}\quad
In polar form, $x=r\cos\theta$, $y=r\sin\theta$:
\[
g(x,y)=r\cos\theta\sin\theta=\tfrac{r}{2}\sin(2\theta).
\]
Then $g\to0$ as $r\to0$, so $g$ is continuous at $0$.
However,
\[
\frac{|g(x,y)|}{\sqrt{x^2+y^2}}=|\cos\theta\sin\theta|
\]
depends on $\theta$, hence the derivative at $0$ does not exist.
Thus $g$ is differentiable everywhere except at $(0,0)$.
\hfill$\Box$

\bigskip\hrule\bigskip
```

## CP-II-0417

- chapter line: 10768

```tex
\label{prob:cp-ii-0417}
— Local inversion on the curve $x^3+y^3-3xy=0$

\textbf{Statement.}\quad

Let $C=\{(x,y)\in\mathbb{R}^2:\; x^3+y^3-3xy=0\}$ and define
\[
F:\mathbb{R}^2\longrightarrow\mathbb{R}^2,\qquad F(x,y)=(x,\,x^3+y^3-3xy).
\]
Show that $F$ is locally $C^1$-invertible at every point of
$C\setminus\{(0,0),(\tfrac{2}{3},\tfrac{2}{3})\}$.
That is, for such $(x_0,y_0)$ there are open sets
$U,V$ with $F:U\to V$ a $C^1$ bijection.
Find the derivative of the inverse and deduce that near each such point
the curve $C$ is the graph of a $C^1$ function $y=g(x)$.

\bigskip\hrule\bigskip

\textbf{Theory \& Solution.}\quad

Compute the Jacobian:
\[
DF(x,y)=
\begin{pmatrix}
	1 & 0\\[4pt]
	3x^2-3y & 3y^2-3x
\end{pmatrix},
\qquad
J(x,y)=\det DF(x,y)=3(y^2-x^2+y-x).
\]
The determinant vanishes when $y^2-x^2+y-x=0$, i.e.\
along the lines $y=x$ and $y=1-x$.

\medskip

\textbf{(Points where $DF$ is invertible).}\;
On $C$, the points where $J(x,y)\ne0$
correspond to $(x,y)$ not lying on those lines simultaneously,
which occurs except at $(0,0)$ and $(\tfrac{2}{3},\tfrac{2}{3})$.
Hence by the inverse function theorem, $F$ is locally a $C^1$ diffeomorphism there.

\medskip

\textbf{(Derivative of the inverse).}\;
For invertible $DF(x_0,y_0)$,
\[
D(F^{-1})(F(x_0,y_0)) = [DF(x_0,y_0)]^{-1}.
\]
Thus the slope of the corresponding branch of $C$,
viewed as $y=g(x)$, is given by
\[
g'(x_0)= -\,\frac{F_y(x_0,y_0)}{F_x(x_0,y_0)}
= \frac{3y_0^2-3x_0}{3x_0^2-3y_0}.
\]

\bigskip\hrule\bigskip

\textbf{Examples.}\quad
 \setlength{\itemsep}{6pt}
	\par\noindent\textbullet\quad At $(1,0)$, $g'(1)=\tfrac{-3}{3-0}=-1$.
	\par\noindent\textbullet\quad At $(0,1)$, $g'(0)=\tfrac{3-0}{0-3}=-1$ (symmetric branch).
	Thus near these points $C$ is a smooth curve crossing the axes with slope $-1$.

\section*{Problem 14\textsuperscript{*} — Maximum principles for C\textsuperscript{2} functions}

\textbf{(i) Local maximum: gradient and Hessian.}\quad

Let $f$ be a real-valued $C^2$ function on an open $U\subset\mathbb{R}^2$.
If $f$ has a local maximum at $a\in U$ (i.e.\ $\exists\,\rho>0$ with $B_\rho(a)\subset U$ and $f(x)\le f(a)$ for $x\in B_\rho(a)$),
then
\[
\nabla f(a)=0
\quad\text{and}\quad
H(a):=\big(D_{ij}f(a)\big)\ \text{is negative semidefinite.}
\]

\bigskip\hrule\bigskip

\textbf{Proof.}\quad
For any unit $v$, consider $g(t)=f(a+tv)$ for small $t$.
Then $g$ has a local maximum at $0$, hence $g'(0)=0$ and $g''(0)\le 0$.
But $g'(0)=\nabla f(a)\!\cdot v$ and $g''(0)=v^\top H(a)\,v$.
Thus $\nabla f(a)\!\cdot v=0$ for all unit $v$, giving $\nabla f(a)=0$, and $v^\top H(a)\,v\le0$ for all $v$, so $H(a)\preceq 0$.
\hfill$\square$

\bigskip\hrule\bigskip

\textbf{(ii) Weak maximum principle for $\Delta + aD_1 + bD_2 + c$.}\quad

Let $U\subset\mathbb{R}^2$ be bounded and open, and let $f:\overline U\to\mathbb{R}$ be continuous on $\overline U$ and $C^2$ in $U$.
Assume
\[
\Delta f + a\,D_1 f + b\,D_2 f + c\,f \ \ge\ 0 \quad \text{in } U,
\]
where $\Delta f=D_{11}f+D_{22}f$, and $a,b,c$ are real-valued on $U$ with $c<0$ on $U$.
If $f$ is positive somewhere in $\overline U$, then
\[
\sup_{\overline U} f \;=\; \sup_{\partial U} f .
\]

\bigskip\hrule\bigskip

\textbf{Proof.}\quad
Let $M=\sup_{\overline U} f$.
If $M\le 0$, the claim is trivial.
Assume $M>0$.
If $M$ is attained at $x_0\in U$, then (i) gives $\nabla f(x_0)=0$ and $\Delta f(x_0)\le 0$.
Hence
\[
\big(\Delta f + aD_1 f + bD_2 f + c f\big)(x_0)
= \Delta f(x_0) + c(x_0) f(x_0)
\le c(x_0) M \;<\; 0,
\]
contradicting the assumed inequality.
Therefore every positive maximum is on $\partial U$, i.e.\ $\sup_{\overline U} f=\sup_{\partial U} f$.
\hfill$\square$

\bigskip\hrule\bigskip

\textbf{Uniqueness for the Dirichlet problem.}\quad

If $a,b,c$ are as above with $c<0$, $\varphi:\partial U\to\mathbb{R}$ is continuous, and $g:\mathbb{R}^2\to\mathbb{R}$ is given,
then there is \emph{at most one} continuous $f$ on $\overline U$, $C^2$ in $U$, solving
\[
\Delta f + aD_1 f + bD_2 f + c f = g \quad\text{in } U,
\qquad
f=\varphi \quad\text{on } \partial U.
\]
Indeed, if $f_1,f_2$ solve it, $h=f_1-f_2$ satisfies $\Delta h + aD_1 h + bD_2 h + c h=0$ in $U$ and $h=0$ on $\partial U$.
Applying the maximum principle to $h$ and $-h$ shows $h\equiv 0$.

\bigskip\hrule\bigskip

\textbf{Examples.}\quad

 \setlength{\itemsep}{6pt}
	\par\noindent\textbullet\quad If $a=b=0$ and $c=-\lambda<0$, the operator is $\Delta - \lambda$.
	Any interior positive maximum would give $(\Delta - \lambda)f(x_0)\le -\lambda f(x_0)<0$, a contradiction.
	\par\noindent\textbullet\quad In one dimension ($U=(0,1)$), the statement reduces to:
	if $f\in C^2(0,1)\cap C[0,1]$ and $f'' - \lambda f \ge 0$ with $\lambda>0$, then
	$\max_{[0,1]} f = \max\{f(0),f(1)\}$.

\noindent\textbf{Example A (harmonic):} $u(x,y)=x^2-y^2$ on the unit disk
$D=\{x^2+y^2<1\}$.

	\par\noindent\textbullet\quad \textbf{Laplacian:} $\Delta u = u_{xx}+u_{yy}=2-2=0 \;\Rightarrow\; u$ is \emph{harmonic}.
	\par\noindent\textbullet\quad \textbf{Maximum principle (harmonic):} If $u$ is harmonic on a bounded domain and continuous on $\overline D$, then $u$
	attains its max/min \emph{only on $\partial D$} unless $u$ is constant.
	\par\noindent\textbullet\quad \textbf{Boundary values (polar coords).} With $x=\cos\theta$, $y=\sin\theta$ on $\partial D$,
	\[
	u(\cos\theta,\sin\theta)=\cos^2\theta-\sin^2\theta=\cos(2\theta).
	\]
	Hence on $\partial D$: $\max u=1$ at $\theta=0,\pi$ (points $(\pm1,0)$),
	and $\min u=-1$ at $\theta=\tfrac{\pi}{2},\tfrac{3\pi}{2}$ (points $(0,\pm1)$).
	\par\noindent\textbullet\quad \textbf{Interior critical point:} $\nabla u=(2x,-2y)=0 \Rightarrow (0,0)$.
	The Hessian $D^2u=\begin{pmatrix}2&0\\[2pt]0&-2\end{pmatrix}$ is indefinite $\Rightarrow$ \emph{saddle}, not extremum.

\medskip\hrule\medskip

\noindent\textbf{Example B (subharmonic):} $v(x,y)=x^2+y^2$ on the unit disk $D$.

	\par\noindent\textbullet\quad \textbf{Laplacian:} $\Delta v = 2+2=4 \ge 0 \;\Rightarrow\; v$ is \emph{subharmonic}.
	\par\noindent\textbullet\quad \textbf{Maximum principle (subharmonic):} A subharmonic function attains its \emph{maximum} on $\partial D$ (unless constant).
	Interior maxima are forbidden.
	\par\noindent\textbullet\quad \textbf{Values:} On $\partial D$ ($r=1$): $v=1$ $\Rightarrow$ \emph{global maximum}. At the center: $v(0,0)=0$
	$\Rightarrow$ \emph{global minimum} (allowed for subharmonic).
```

## CP-II-0428

- chapter line: 10937

```tex
\label{prob:cp-ii-0428}
— Differentiability of the determinant function

\textbf{Statement.}\quad

Let $\mathcal{M}_n$ be the space of $n\times n$ real matrices with a norm.
Show that the determinant function
\[
\det:\mathcal{M}_n \longrightarrow \mathbb{R}
\]
is differentiable at the identity matrix $I$ with
\[
D\det(I)(H)=\operatorname{tr}(H).
\]
Deduce that $\det$ is differentiable at any invertible matrix $A$ with
\[
D\det(A)(H)=\det(A)\,\operatorname{tr}(A^{-1}H).
\]
Show further that $\det$ is twice differentiable at $I$ and find $D^2\det(I)$ as a bilinear map.

\bigskip\hrule\bigskip

\textbf{Theory \& Solution.}\quad

\textbf{(Derivative at the identity).}\;
For $A(t)=I+tH$, expand the determinant polynomially:
\[
\det(I+tH)=1+t\,\operatorname{tr}(H)+o(t).
\]
Hence $D\det(I)(H)=\operatorname{tr}(H)$.

\medskip

\textbf{(Derivative at a general invertible matrix).}\;
Write $\det(A+H)=\det(A)\det(I+A^{-1}H)$.
By the previous step,
\[
\det(I+A^{-1}H)=1+\operatorname{tr}(A^{-1}H)+o(\|H\|),
\]
so
\[
D\det(A)(H)=\det(A)\,\operatorname{tr}(A^{-1}H).
\]

\medskip

\textbf{(Second derivative at $I$).}\;
Expand further:
\[
\det(I+tH)=1+t\,\operatorname{tr}(H)
+\tfrac{1}{2}\big((\operatorname{tr}H)^2-\operatorname{tr}(H^2)\big)t^2+o(t^2).
\]
Therefore
\[
D^2\det(I)(H,K)
=\operatorname{tr}(H)\operatorname{tr}(K)-\operatorname{tr}(HK),
\]
which is symmetric and bilinear. \hfill$\square$

\bigskip\hrule\bigskip

\textbf{Examples.}\quad
 \setlength{\itemsep}{6pt}
	\par\noindent\textbullet\quad For $n=2$,
	\[
	\det\!\begin{pmatrix}1+t a & t b\\ t c & 1+t d\end{pmatrix}
	=1+t(a+d)+t^2(ad-bc),
	\]
	giving $D\det(I)(H)=a+d=\operatorname{tr}(H)$ and
	$D^2\det(I)(H,H)=2(ad-bc)=(\operatorname{tr}H)^2-\operatorname{tr}(H^2)$.
```

## CP-II-0433

- chapter line: 11044

```tex
\label{prob:cp-ii-0433}
— Bounded Derivative and a Classical Oscillating Example

If $|f'(x)|\le M$ on $\mathbb R$, then by the Mean Value Theorem
\[
|f(x)-f(y)|=|f'(\xi)||x-y|\le M|x-y|,
\]
so $f$ is Lipschitz, hence uniformly continuous.

For $x\ne 0$,
\[
g'(x)=2x\sin(1/x^2)-\frac{2\cos(1/x^2)}{x},\qquad
g'(0)=\lim_{x\to0}\frac{x^2\sin(1/x^2)}{x}=0.
\]
Thus $g$ is differentiable, but $g'$ is unbounded near $0$.
Since $g$ is continuous on the compact interval $[-1,1]$, it is uniformly continuous there.

\bigskip
```

## CP-II-0435

- chapter line: 11065

```tex
\label{prob:cp-ii-0435}
Suppose $f:\mathbb{R}\to\mathbb{R}$ has the intermediate value property (IVP): if $a,b\in\mathbb{R}$ and $f(a)<c<f(b)$, then there exists $y\in(a,b)$ with $f(y)=c$.

\textbf{Claim:} $f$ need not be continuous.

\textbf{Counterexample.} Define
\[
f(x)=\begin{cases}
	\sin\!\left(\tfrac{1}{x}\right), & x\neq 0,\\
	0, & x=0.
\end{cases}
\]
This function has the IVP (as it is a derivative on $\mathbb{R}\setminus\{0\}$), but is not continuous at $0$.
Thus the IVP does not imply continuity.

Now assume additionally that $f^{-1}(q)$ is closed for every $q\in\mathbb{Q}$.

Suppose, for contradiction, that $f$ is not continuous at some $x_0$.
Then there exists $\varepsilon>0$ and a sequence $x_n\to x_0$ with $|f(x_n)-f(x_0)|>\varepsilon$.

By the IVP, between $f(x_0)$ and $f(x_n)$ the function takes all intermediate values, hence in particular some rational $q$.
Thus there exist points arbitrarily close to $x_0$ with $f(x)=q$.
Therefore $x_0$ is a limit point of $f^{-1}(q)$.
Since $f^{-1}(q)$ is closed, $x_0\in f^{-1}(q)$, i.e.\ $f(x_0)=q$.

Repeating this with infinitely many different rationals leads to a contradiction.
Hence $f$ must be continuous at $x_0$.

\textbf{Conclusion.} With the closed-preimage assumption, $f$ is continuous everywhere.
```

## CP-II-0436

- chapter line: 11098

```tex
\label{prob:cp-ii-0436}
Let $\Omega=\{(x,y)^t\in\mathbb{R}^2:x>0\}$ and
\[
f(x,y)=\begin{pmatrix}x\sin y\\ x\cos y\end{pmatrix}.
\]

	\par\noindent\textbullet\quad Compute derivatives:
	\[
	Df(\xi,\eta)=
	\begin{pmatrix}
		\sin \eta & \xi\cos \eta\\
		\cos \eta & -\xi \sin \eta
	\end{pmatrix}.
	\]
	Thus $f$ is differentiable everywhere.

	\par\noindent\textbullet\quad $\det Df(\xi,\eta)=-\xi\neq 0$ for $(\xi,\eta)\in \Omega$, hence invertible.

	\par\noindent\textbullet\quad $f$ is not injective since $f(x,y)=f(x,y+2\pi)$.
	So invertibility of the derivative does not imply global injectivity.
	This illustrates the local nature of the Inverse Function Theorem.
```

## CP-II-0473

- chapter line: 11215

```tex
\label{prob:cp-ii-0473}
— One partial continuous near $a$ + the other exists at $a$ $\Rightarrow$ differentiability at $a$

\textbf{Statement.}\quad

Let $f:\mathbb{R}^2\to\mathbb{R}$ and $a=(x_0,y_0)\in\mathbb{R}^2$.
Assume $D_1 f$ exists on an open ball $B(a,r)$ and is continuous at $a$, and $D_2 f(a)$ exists.
Show that $f$ is differentiable at $a$.

\bigskip\hrule\bigskip

\textbf{Theory \& Solution.}\quad

\textbf{(Increment decomposition and line integration).}\;
For $h=(h_1,h_2)$ small,
\[
\begin{aligned}
	f(x_0+h_1,y_0+h_2)-f(x_0,y_0)
      &= \bigl[f(x_0+h_1,y_0+h_2)-f(x_0,y_0+h_2)\bigr] \\
      &\quad + \bigl[f(x_0,y_0+h_2)-f(x_0,y_0)\bigr] \\
      &= \int_{0}^{h_1}
         D_1 f(x_0+t,y_0+h_2)\,dt \\
      &\quad + \bigl(f(x_0,y_0+h_2)-f(x_0,y_0)\bigr).
\end{aligned}
\]
Continuity of $D_1 f$ at $a$ gives
\[
\int_{0}^{h_1} D_1 f(x_0+t,y_0+h_2)\,dt
= D_1 f(a)\,h_1 + o(\|h\|).
\]
Since $D_2 f(a)$ exists,
\[
f(x_0,y_0+h_2)-f(x_0,y_0)= D_2 f(a)\,h_2 + o(\|h\|).
\]
Therefore
\[
f(a+h)-f(a) = D_1 f(a)\,h_1 + D_2 f(a)\,h_2 + o(\|h\|),
\]
so $f$ is Fr\'echet differentiable at $a$ with gradient $(D_1 f(a),D_2 f(a))$. \hfill$\square$

\bigskip\hrule\bigskip
\quad

$f(x,y)=x^2|y|$: $D_1 f=2x|y|$ is continuous; $D_2 f(0,0)=0$ exists; hence $f$ is differentiable at $(0,0)$.
```
