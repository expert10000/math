# Part III missing-solution batch 01

- problems: **11**
- IDs: CP-III-0001, CP-III-0003, CP-III-0008, CP-III-0010, CP-III-0017, CP-III-0021, CP-III-0004, CP-III-0005, CP-III-0011, CP-III-0013, CP-III-0014

## CP-III-0001

```tex
\label{prob:cp-iii-0001}
\begin{example}[More meager/comeager examples]
	\leavevmode
	\begin{enumerate}
		\item In $\mathbb R$:
		\begin{itemize}
			\item $\mathbb R\setminus\mathbb Q$ is comeager (since $\mathbb Q$ is countable $\Rightarrow$ meager).
			\item The set of Liouville numbers is a dense $G_\delta$ (comeager) but has Lebesgue measure $0$.
			\item The Cantor set (standard or “fat”) is nowhere dense; hence meager (the fat one has positive measure).
		\end{itemize}
		\item In $C([0,1])$ (sup norm):
		\begin{itemize}
			\item The set of nowhere differentiable functions is comeager.
			\item The set of functions of bounded variation is meager; thus “typically” functions have infinite total variation.
			\item The set of $f$ with a unique global maximum (resp.\ minimum) is comeager.
			\item For each $\alpha>0$, the Hölder class $C^{0,\alpha}$ is meager; hence a generic $f$ is not Hölder of any exponent on any interval.
		\end{itemize}
		\item In any infinite-dimensional Banach space $X$:
		\begin{itemize}
			\item $\bigcup_{n=1}^\infty E_n$ with each $E_n$ finite-dimensional is meager.
			\item Consequently, the set of points not lying in any finite-dimensional subspace is comeager.
		\end{itemize}
		\item In $\mathbb R^n$:
		\begin{itemize}
			\item The complement of a countable union of hyperplanes is comeager.
		\end{itemize}
	\end{enumerate}
\end{example}
```

## CP-III-0003

```tex
\label{prob:cp-iii-0003}
\textbf{Statement.}
Let $(E,\mathcal E,\mu)$ be a measure space and let $f,g:E\to\mathbb C$ be measurable.

\begin{enumerate}[(a)]
	\item If $1\le p,q,r\le\infty$ satisfy $p^{-1}+q^{-1}=r^{-1}$, then
	\[
	\|fg\|_{L^r}\le \|f\|_{L^p}\,\|g\|_{L^q}.
	\]
	\item For $1\le p\le\infty$,
	\[
	\|f+g\|_{L^p}\le \|f\|_{L^p}+\|g\|_{L^p}.
	\]
\end{enumerate}
\textbf{Theory (quick toolkit).}

\begin{itemize}
	\item \textbf{Conjugate exponents.} \(p,q\in[1,\infty]\) are conjugate if \(\frac1p+\frac1q=1\) (with \(1/\infty=0\)).
	\item \textbf{Young’s inequality (products).} For \(a,b\ge0\) and conjugate \(p,q\):
	\[
	ab \;\le\; \frac{a^{p}}{p} \;+\; \frac{b^{q}}{q}.
	\]
	\item \textbf{Hölder (classical, \(r=1\)).} If \(1\le p,q\le\infty\), \(1/p+1/q=1\), then
	\[
	\int |uv| \,\mathrm d\mu \;\le\; \|u\|_{L^{p}}\|v\|_{L^{q}}.
	\]
	\item \textbf{Minkowski (triangle).} For \(1\le p\le\infty\):
	\[
	\|u+v\|_{L^{p}} \;\le\; \|u\|_{L^{p}} + \|v\|_{L^{p}}.
	\]
\end{itemize}


\bigskip
\textbf{Proof of (a).}

\emph{Step 1: Special case $r=1$.}
Assume $1<p,q<\infty$ and $1/p+1/q=1$ (the endpoints are immediate).
For $A=\frac{|u|}{\|u\|_p}$ and $B=\frac{|v|}{\|v\|_q}$, Young’s inequality gives
$AB\le \frac{A^p}{p}+\frac{B^q}{q}$. Multiplying by $\|u\|_p\|v\|_q$ and integrating,
\[
\int |uv|
\le \frac{\|v\|_q}{p}\int |u|^p\|u\|_p^{1-p}
+ \frac{\|u\|_p}{q}\int |v|^q\|v\|_q^{1-q}
= \|u\|_p\|v\|_q.
\]
Thus $\|uv\|_1\le \|u\|_p\|v\|_q$.

\emph{Step 2: General $r$.}
Let $1\le r<\infty$ and $1/p+1/q=1/r$. Set $U=|f|^{\,r}$ and $V=|g|^{\,r}$.
Then $U\in L^{p/r}$, $V\in L^{q/r}$ and $\frac{r}{p}+\frac{r}{q}=1$. Applying Step~1 to $U,V$,
\[
\int |fg|^{\,r} = \int UV \le \|U\|_{p/r}\,\|V\|_{q/r}
= \|f\|_{p}^{r}\|g\|_{q}^{r}.
\]
Taking the $r$-th root yields $\|fg\|_{r}\le \|f\|_{p}\|g\|_{q}$.
For $r=\infty$, the estimate $\|fg\|_{\infty}\le \|f\|_{\infty}\|g\|_{\infty}$ is immediate.

\bigskip
\textbf{Proof of (b) (Minkowski).}

For $p=\infty$ or $p=1$, the claim follows from the pointwise triangle inequality and linearity.
Assume $1<p<\infty$ and let $p'=\frac{p}{p-1}$. If $\|f+g\|_p=0$ there is nothing to prove.
Otherwise define
\[
h=\frac{|f+g|^{p-1}\operatorname{sgn}(f+g)}{\|f+g\|_p^{p-1}} \quad\Rightarrow\quad \|h\|_{p'}=1
\ \text{ and }\ \int (f+g)h=\|f+g\|_p.
\]
Then, using Hölder twice,
\[
\|f+g\|_p
= \int (f+g)h
\le \int |f||h|+\int |g||h|
\le \|f\|_p\|h\|_{p'}+\|g\|_p\|h\|_{p'}
= \|f\|_p+\|g\|_p.
\]
This proves Minkowski.

\bigskip
\textbf{Examples.}

\emph{(i) Powers on $[0,1]$.}
Let $f(x)=x^{\alpha}$, $g(x)=x^{\beta}$ with $\alpha>-1/p$, $\beta>-1/q$, $1/p+1/q=1/r$. Then
\[
\|f\|_{p}^{p}=\frac{1}{\alpha p+1},\qquad
\|g\|_{q}^{q}=\frac{1}{\beta q+1},\qquad
\|fg\|_{r}^{r}=\frac{1}{(\alpha+\beta)r+1},
\]
and one checks $\|fg\|_{r}\le \|f\|_{p}\|g\|_{q}$.

\emph{(ii) $\ell^p$ endpoint.}
Let $a_n=1/n$ and $b_n\equiv 1$. For $p=r$ and $q=\infty$,
$\|ab\|_{p}=\|a\|_{p}\le \|a\|_{p}\|b\|_{\infty}$ with equality.


% Put packages and spacing helpers in your preamble (as earlier).

\par\medskip\noindent\textbf{Background definitions}\quad


	\textbf{Set.}
	A collection of elements. We denote the ambient set by $E$.

	\textbf{$\sigma$-algebra.}
	A family $\mathcal E\subseteq \mathcal P(E)$ such that:
	(i) $E\in\mathcal E$; \;
	(ii) $A\in\mathcal E \Rightarrow A^{c}\in\mathcal E$; \;
	(iii) $A_1,A_2,\dots\in\mathcal E \Rightarrow \bigcup_{n=1}^\infty A_n\in\mathcal E$.
	Members of $\mathcal E$ are called \emph{measurable sets}.

	\textbf{Measurable space.}
	A pair $(E,\mathcal E)$ with $E$ a set and $\mathcal E$ a $\sigma$-algebra on $E$.

	\textbf{Measure.}
	A map $\mu:\mathcal E\to[0,\infty]$ such that $\mu(\varnothing)=0$ and, for pairwise disjoint
	$A_1,A_2,\dots\in\mathcal E$,
	\[
	\mu\!\left(\bigcup_{n=1}^\infty A_n\right) \;=\; \sum_{n=1}^\infty \mu(A_n).
	\]

	\textbf{Measure space.}
	A triple $(E,\mathcal E,\mu)$ where $\mu$ is a measure on $(E,\mathcal E)$.

	\textbf{Measurable function.}
	A function $f:(E,\mathcal E)\to(\mathbb C,\mathcal B(\mathbb C))$ is measurable if
	$f^{-1}(B)\in\mathcal E$ for every Borel set $B$.
	(For real-valued $f$, replace $\mathbb C$ by $\mathbb R$.)

	\textbf{Almost everywhere (a.e.).}
	A statement holds a.e.\ if the set where it fails has measure $0$.

	\textbf{$L^{p}$ spaces.}
	For $1\le p<\infty$,
	\[
	L^{p}(E,\mu) \;=\; \Bigl\{ f \text{ measurable} : \int_E |f|^{p}\,d\mu < \infty \Bigr\}
	\big/ \text{(equality a.e.)}.
	\]
	For $p=\infty$, $L^\infty(E,\mu)$ consists of (equivalence classes of) essentially bounded $f$.

	\textbf{$L^{p}$ norms.}
	For $1\le p<\infty$,
	\[
	\|f\|_{L^{p}}=\Bigl(\int_E |f|^{p}\,d\mu\Bigr)^{1/p},
	\]
	and
	\[
	\|f\|_{L^{\infty}}=\operatorname*{ess\,sup}_{x\in E} |f(x)|
	\;=\; \inf\{ M\ge 0 : \mu(\{x:|f(x)|>M\})=0\}.
	\]
```

## CP-III-0008

```tex
\label{prob:cp-iii-0008}
This yields Minkowski's integral inequality in full generality
	for all $1 \le p < \infty$.


\par\smallskip\noindent\textbf{From Fenchel--Young to Hölder's inequality.}\quad

The Fenchel--Young inequality for the convex function
$\Phi(x)=x^p/p$ and its conjugate $\Phi^*(y)=y^q/q$ reads
\[
xy \le \frac{x^p}{p} + \frac{y^q}{q},
\qquad x,y\ge 0.
\]
Applying this pointwise with $x=|f(x)|$ and $y=|g(x)|$ gives
\[
|f(x)g(x)|
\le \frac{|f(x)|^p}{p} + \frac{|g(x)|^q}{q},
\qquad x\in\mathbb{R}^n.
\]
Integrating over $\mathbb{R}^n$ yields
\[
\int_{\mathbb{R}^n} |f(x)g(x)|\,dx
\le \frac1p \int_{\mathbb{R}^n} |f(x)|^p\,dx
+ \frac1q \int_{\mathbb{R}^n} |g(x)|^q\,dx
= \frac{\|f\|_{L^p}^p}{p} + \frac{\|g\|_{L^q}^q}{q}.
\]
If $\|f\|_{L^p},\|g\|_{L^q}>0$, apply this to
$\tilde f = f/\|f\|_{L^p}$ and $\tilde g = g/\|g\|_{L^q}$ to obtain
\[
\int_{\mathbb{R}^n}
\bigl|\tilde f(x)\tilde g(x)\bigr|\,dx
\le \frac1p + \frac1q = 1,
\]
and hence
\[
\int_{\mathbb{R}^n} |f(x)g(x)|\,dx
\le \|f\|_{L^p}\,\|g\|_{L^q}.
\]
This recovers Hölder's inequality directly from the
Fenchel--Young inequality for $\Phi(x)=x^p/p$.


\par\medskip\noindent\textbf{Examples for Exercise 2.5}\quad

\par\smallskip\noindent\textbf{(i) Example for Young's inequality}\quad

Take $p=q=2$ and $a=3$, $b=4$.  Young's inequality states that
\[
ab \le \frac{a^p}{p} + \frac{b^q}{q}.
\]
Here
\[
ab = 3\cdot 4 = 12,
\]
while
\[
\frac{a^2}{2} + \frac{b^2}{2}
= \frac{9}{2} + \frac{16}{2}
= \frac{25}{2} = 12.5.
\]
Thus
\[
12 = ab \le 12.5 = \frac{a^2}{2} + \frac{b^2}{2},
\]
which illustrates the inequality for a specific choice of parameters.

\bigskip

\par\smallskip\noindent\textbf{(ii) Example for Hölder's inequality}\quad

Let $p=q=2$ and define functions on $\mathbb{R}$ by
\[
f(x) = 1_{[0,1]}(x), \qquad
g(x) = x\,1_{[0,1]}(x).
\]
Then
\[
f(x)g(x) = x\,1_{[0,1]}(x),
\]
and
\[
\int_{\mathbb{R}} |f(x)g(x)|\,dx
= \int_0^1 x\,dx = \frac12.
\]
The norms are
\[
\|f\|_{L^2}^2 = \int_0^1 1^2\,dx = 1
\quad\Longrightarrow\quad
\|f\|_{L^2} = 1,
\]
and
\[
\|g\|_{L^2}^2 = \int_0^1 x^2\,dx = \frac13
\quad\Longrightarrow\quad
\|g\|_{L^2} = \frac{1}{\sqrt{3}}.
\]
Thus
\[
\int_{\mathbb{R}} |f(x)g(x)|\,dx = \frac12
\le \frac{1}{\sqrt{3}} = \|f\|_{L^2}\,\|g\|_{L^2},
\]
which confirms Hölder's inequality in this concrete case (with strict
inequality).

\bigskip

\par\smallskip\noindent\textbf{(iii) Example for Minkowski's integral inequality}\quad

Let $F:\mathbb{R}\times\mathbb{R}\to\mathbb{R}$ be given by
\[
F(x,y) = 1_{[0,1]}(x)\,1_{[0,1]}(y),
\]
and take $p=2$.
Define
\[
u(x) := \int_{\mathbb{R}} F(x,y)\,dy.
\]
Then
\[
u(x) = \int_{\mathbb{R}} 1_{[0,1]}(x)1_{[0,1]}(y)\,dy
= 1_{[0,1]}(x)\cdot 1,
\]
so $u(x)=1$ for $x\in[0,1]$ and $u(x)=0$ otherwise. Hence
\[
\left(\int_{\mathbb{R}} |u(x)|^2\,dx\right)^{1/2}
= \left(\int_0^1 1\,dx\right)^{1/2}
= 1.
\]

On the other hand,
\[
\int_{\mathbb{R}}
\left(\int_{\mathbb{R}} |F(x,y)|^2\,dx\right)^{1/2} dy
\]
is computed as follows. Since $F^2=F$,
\[
\int_{\mathbb{R}} |F(x,y)|^2\,dx
= \int_{\mathbb{R}} 1_{[0,1]}(x)1_{[0,1]}(y)\,dx
= 1_{[0,1]}(y)\cdot 1.
\]
Thus
\[
\left(\int_{\mathbb{R}} |F(x,y)|^2\,dx\right)^{1/2}
= 1_{[0,1]}(y),
\]
and therefore
\[
\int_{\mathbb{R}}
\left(\int_{\mathbb{R}} |F(x,y)|^2\,dx\right)^{1/2} dy
= \int_0^1 1\,dy = 1.
\]
In this example both sides of Minkowski's integral inequality are equal to
$1$, so equality holds.
```

## CP-III-0010

```tex
\label{prob:cp-iii-0010}
\textbf{Statement.}
	Let $\mathcal R_{\mathbb Q}$ be the family of rectangles $(a_1,b_1]\times\cdots\times(a_n,b_n]$ with all $a_i,b_i\in\mathbb Q$.
	Let $\mathcal S_{\mathbb Q}$ be the set of finite sums
	\[
	s(x)=\sum_{k=1}^{N}(\alpha_k+i\beta_k)\,\mathbf 1_{R_k}(x),
	\qquad R_k\in\mathcal R_{\mathbb Q},\ \alpha_k,\beta_k\in\mathbb Q.
	\]
	(a) For $1\le p<\infty$, show $\mathcal S_{\mathbb Q}$ is dense in $L^p(\mathbb R^n)$ and conclude $L^p(\mathbb R^n)$ is separable.
	(b) Show $L^\infty(\mathbb R^n)$ is not separable.


	\textbf{Theory (quick toolkit).}
	\begin{itemize}
		\item Lebesgue measure is regular: for measurable $A$ of finite measure,
		$\mu(A)=\sup\{\mu(K):K\subset A,\ K\text{ compact}\}=\inf\{\mu(U):A\subset U,\ U\text{ open}\}$.
		Every open set is a countable union of rectangles with rational endpoints.
		\item For measurable $A,B$ and $1\le p<\infty$,
		$\|\mathbf 1_A-\mathbf 1_B\|_{L^p}=\mu(A\triangle B)^{1/p}$.
		\item Truncation/localization: for $f\in L^p(\mathbb R^n)$, $f_R:=f\mathbf 1_{B(0,R)}\to f$ in $L^p$,
		and $f^{(M)}:=\max(-M,\min(f,M))\to f$ in $L^p$.
	\end{itemize}


	\textbf{Proof of (a) (density).}
	Let $f\in L^{p}$ and $\varepsilon>0$.
	Choose $R$ so that $\|f-f_R\|_{p}<\varepsilon/3$ and then $M$ so that $\|f_R-f_R^{(M)}\|_{p}<\varepsilon/3$.
	It suffices to approximate a bounded function $g:=f_R^{(M)}$ supported in $B(0,R)$.

	Partition $B(0,R)$ by finitely many rectangles $Q_j$ with rational endpoints and small diameter.
	Pick $c_j\in\mathbb Q+i\mathbb Q$ with $\sup_{x\in Q_j\cap B(0,R)}|g(x)-c_j|\le\eta$ and set
	$s=\sum_j c_j\,\mathbf 1_{Q_j}\in\mathcal S_{\mathbb Q}$.
	Then
	\[
	\|g-s\|_{L^p}\le \eta\,|B(0,R)|^{1/p}.
	\]
	Choosing $\eta$ (and the grid) suitably small gives $\|g-s\|_{L^p}<\varepsilon/3$.
	Therefore $\|f-s\|_{L^p}<\varepsilon$, proving density.

	Since $\mathcal R_{\mathbb Q}$ and $\mathbb Q+i\mathbb Q$ are countable, the set $\mathcal S_{\mathbb Q}$ is countable.
	Thus $L^p(\mathbb R^n)$ is separable.

	\medskip

	\textbf{Proof of (b) ($L^\infty$ not separable).}
	Define $A_t=[0,1/2)+t \pmod 1\subset[0,1)$ for $t\in[0,1)$, and set $X=\{\mathbf 1_{A_t}: t\in[0,1)\}\subset L^\infty(\mathbb R)$.
	If $s\ne t$, then $\mu(A_s\triangle A_t)>0$, hence
	\[
	\|\mathbf 1_{A_s}-\mathbf 1_{A_t}\|_{L^\infty}
	= \operatorname*{ess\,sup} |\mathbf 1_{A_s}-\mathbf 1_{A_t}| = 1 .
	\]
	Therefore $X$ is an uncountable $1$-separated set, so $L^\infty(\mathbb R^n)$ is not separable.


\par\medskip\noindent\textbf{Theory: separability and the rational simple class $\mathcal S_{\mathbb Q}$}\quad


	\textbf{Separable metric spaces.}
	A metric space $(X,d)$ is \emph{separable} if there exists a countable dense subset $D\subset X$,
	i.e.\ $\overline D=X$.

	\textbf{Rational rectangles and simple functions.}
	Let $\mathcal R_{\mathbb Q}$ be the family of axis-parallel rectangles
	$(a_1,b_1]\times\cdots\times(a_n,b_n]$ with $a_i,b_i\in\mathbb Q$.
	Define
	\[
	\mathcal S_{\mathbb Q}
	= \left\{\, s=\sum_{k=1}^N (\alpha_k+i\beta_k)\,\mathbf 1_{R_k}
	: N\in\mathbb N,\ R_k\in\mathcal R_{\mathbb Q},\ \alpha_k,\beta_k\in\mathbb Q \right\}.
	\]

	\textbf{Countability.}
	$\mathcal R_{\mathbb Q}$ is countable (finite tuples of rationals).
	Finite sequences of elements of a countable set, with rational coefficients, form a countable set.
	Hence $\mathcal S_{\mathbb Q}$ is countable.

	\textbf{Density in $L^p$, $1\le p<\infty$.}
	Given $f\in L^p(\mathbb R^n)$ and $\varepsilon>0$:
	\begin{enumerate}[label=\arabic*)]
		\item \emph{Localization:} pick $R$ so that $\|f-f\,\mathbf 1_{B(0,R)}\|_{L^p}<\varepsilon/3$.
		\item \emph{Truncation:} pick $M$ so that
		$\|f\,\mathbf 1_{B(0,R)}-\operatorname{clip}_{[-M,M]}(f)\,\mathbf 1_{B(0,R)}\|_{L^p}<\varepsilon/3$.
		\item \emph{Rational simple approximation:}
		approximate the bounded, compactly supported function $g$ from 2) by
		$s\in\mathcal S_{\mathbb Q}$ using regularity of Lebesgue measure (or Lusin’s theorem) so that
		$\|g-s\|_{L^p}<\varepsilon/3$.
	\end{enumerate}
	By the triangle inequality, $\|f-s\|_{L^p}<\varepsilon$.
	Thus $\overline{\mathcal S_{\mathbb Q}}^{\,L^p}=L^p(\mathbb R^n)$.

	\textbf{Consequence.}
	Since $\mathcal S_{\mathbb Q}$ is countable and dense, $L^p(\mathbb R^n)$ is separable for $1\le p<\infty$.

	\textbf{Contrast with $L^\infty$.}
	The family $X=\{\mathbf 1_{[0,1/2)+t \ \mathrm{mod}\ 1}: t\in[0,1)\}$ is uncountable and
	$1$-separated in $L^\infty$, hence $L^\infty(\mathbb R^n)$ is not separable.


\par\smallskip\noindent\textbf{Rational rectangles and complex coefficients.}\quad
Fix $n\in\mathbb N$. Let $\mathcal R_{\mathbb Q}$ be the family of axis–parallel rectangles
\[
R=(a_1,b_1]\times\cdots\times(a_n,b_n]\subset\mathbb R^{n},
\qquad a_i,b_i\in\mathbb Q.
\]
Define the class of \emph{rational simple functions} with complex coefficients by
\[
\mathcal S_{\mathbb Q}
= \Bigl\{\, s:\mathbb R^{n}\to\mathbb C \ \Big|\
s(x)=\sum_{k=1}^{N} (\alpha_k+i\beta_k)\,\mathbf 1_{R_k}(x),\
N\in\mathbb N,\ R_k\in\mathcal R_{\mathbb Q},\
\alpha_k,\beta_k\in\mathbb Q \Bigr\}.
\]
Here:
\begin{itemize}
	\item $n$ is the \emph{dimension} of the ambient space $\mathbb R^{n}$ (the domain of all functions).
	\item $N$ is the \emph{finite number of terms} in the sum (not a dimension).
	\item $\mathbf 1_{R_k}$ denotes the indicator of $R_k$; half–open endpoints avoid overlaps on boundaries (which are null sets).
	\item $(\alpha_k+i\beta_k)\in\mathbb Q+i\mathbb Q\subset\mathbb C$ are \emph{complex rational} coefficients.
\end{itemize}
\noindent
\textbf{Real-valued variant.} For real $L^p$ spaces, take $\beta_k=0$ (so coefficients are in $\mathbb Q$) and the same arguments apply, since
\[
L^{p}(\mathbb R^{n};\mathbb C)
\cong L^{p}(\mathbb R^{n};\mathbb R)\ \oplus\ i\,L^{p}(\mathbb R^{n};\mathbb R)
\]
isometrically, and density can be shown on real and imaginary parts separately.

\par\smallskip\noindent\textbf{Evaluation of a simple function on $\mathbb R^{n}$.}\quad
Let $R_1,\dots,R_N\subset \mathbb R^{n}$ be (half-open) rectangles and let each $R_k$
carry a complex coefficient $c_k\in\mathbb C$. Define
\[
s(x) \;=\; \sum_{k=1}^{N} c_k\,\mathbf 1_{R_k}(x), \qquad x\in\mathbb R^{n}.
\]
For any point $x\in\mathbb R^{n}$, exactly one of the following occurs:
\[
s(x)=
\begin{cases}
	\displaystyle \sum_{k:\,x\in R_k} c_k, & \text{if $x$ belongs to one or more rectangles},\\[8pt]
	0, & \text{if $x\notin \bigcup_{k=1}^{N} R_k$}.
\end{cases}
\]
\emph{Remark (disjointization).}
If the rectangles are chosen pairwise disjoint (e.g.\ by partitioning into half-open boxes),
then for almost every $x$ there is at most one index $j$ with $x\in R_j$, and hence
$s(x)=c_j$ (or $s(x)=0$ if $x$ is in none).

\par\smallskip\noindent\textbf{“Belongs to a rectangle” and evaluation.}\quad
A rectangle $R=(a_1,b_1]\times\cdots\times(a_n,b_n]\subset\mathbb R^n$
contains $x=(x_1,\dots,x_n)$ iff $a_i < x_i \le b_i$ for all $i$.
Given $s(x)=\sum_{k=1}^N c_k\,\mathbf 1_{R_k}(x)$ with $c_k\in\mathbb C$,
\[
s(x) \;=\; \sum_{k:\,x\in R_k} c_k,
\]
with the convention that the sum is $0$ if $x\notin\bigcup_{k=1}^N R_k$.
If the $R_k$ are pairwise disjoint (e.g.\ a half-open partition), then
$s(x)=c_j$ for the unique $j$ with $x\in R_j$ (or $0$ if none).

\par\medskip\noindent\textbf{Problem 4 — Dual formula for $\|f\|_{p}$ and Minkowski’s integral inequality}\quad


	\textbf{Statement.} Let $1\le p<\infty$ and $q$ be conjugate ($\tfrac1p+\tfrac1q=1$).
	\begin{enumerate}[(a)]
		\item For measurable $f:\mathbb R^{n}\to\mathbb C$,
		\[
		\|f\|_{L^{p}}
		= \sup\Big\{ \int_{\mathbb R^{n}} f(x)g(x)\,dx : g\in L^{q}(\mathbb R^{n}),\ \|g\|_{L^{q}}\le1 \Big\}.
		\]
		\item Let $F:\mathbb R^{n}\times\mathbb R^{n}\to\mathbb C$ be integrable and set
		$G(y)=\int_{\mathbb R^{n}} F(x,y)\,dx$.
		Show that for any $g\in L^{q}$ with $\|g\|_{L^{q}}\le1$,
		\[
		\int_{\mathbb R^{n}} |G(y)|\,|g(y)|\,dy
		\le \int_{\mathbb R^{n}} \Big(\int_{\mathbb R^{n}} |F(x,y)|^{p}\,dy\Big)^{1/p} dx.
		\]
		Deduce Minkowski’s integral inequality
		\[
		\Bigg(\int_{\mathbb R^{n}} \Big|\int_{\mathbb R^{n}} F(x,y)\,dx\Big|^{p} dy\Bigg)^{\!1/p}
		\le \int_{\mathbb R^{n}} \Big(\int_{\mathbb R^{n}} |F(x,y)|^{p} dy\Big)^{1/p} dx.
		\]
	\end{enumerate}


	\textbf{Theory (toolkit).}
	Hölder’s inequality (complex form):
	$\int |uv|\le \|u\|_{p}\|v\|_{q}$; equality for $1<p<\infty$ when $v=\mathrm{sgn}(u)\,|u|^{p-1}/\|u\|_{p}^{p-1}$.
	Tonelli/Fubini applies since $F\in L^{1}(\mathbb R^{n}\times\mathbb R^{n})$.


	\textbf{Proof of (a).}
	By Hölder, $\int f g \le \|f\|_{p}$ for all $\|g\|_{q}\le1$, hence the supremum is at most $\|f\|_{p}$.
	For $1<p<\infty$, define
	\[
	g_0(x)=
	\begin{cases}
		e^{-i\arg f(x)}\,\dfrac{|f(x)|^{p-1}}{\|f\|_{p}^{\,p-1}}, & f(x)\neq0,\\[8pt]
		0,& f(x)=0,
	\end{cases}
	\]
	so that $\|g_0\|_{q}=1$ and $\int f g_0=\|f\|_{p}$.
	For $p=1$, take $g_0=e^{-i\arg f}\in L^{\infty}$ to get $\int f g_0=\|f\|_{1}$.
	Thus the supremum equals $\|f\|_{p}$.

	\medskip

	\textbf{Proof of (b) and Minkowski.}
	Triangle inequality and Fubini give
	\[
	\int |G(y)|\,|g(y)|\,dy
	\le \int \!\!\int |F(x,y)|\,|g(y)|\,dx\,dy
	= \int \Big(\int |F(x,y)|\,|g(y)|\,dy\Big)\,dx.
	\]
	For each fixed $x$, Hölder in $y$ yields
	\[
	\int |F(x,y)|\,|g(y)|\,dy \le
	\Big(\int |F(x,y)|^{p}dy\Big)^{1/p}\|g\|_{q}\le
	\Big(\int |F(x,y)|^{p}dy\Big)^{1/p}.
	\]
	Integrate in $x$ to obtain the displayed bound. Taking the supremum over all $\|g\|_{q}\le1$ and using part (a) for $G$,
	\[
	\|G\|_{L^{p}_y}
	\le \int \Big(\int |F(x,y)|^{p}dy\Big)^{1/p} dx,
	\]
	which is Minkowski’s integral inequality.


\par\medskip\noindent\textbf{Lp spaces: theory, norms, examples and counterexamples}\quad


	\textbf{Definitions.}
	Let $(E,\mathcal E,\mu)$ be a measure space. For $0<p<\infty$,
	\[
	L^p(E)=\{ f\ \text{measurable}:\ \|f\|_{L^p}^p:=\int_E |f|^p\,d\mu<\infty\}
	\big/ \text{(a.e.\ equality)}.
	\]
	For $p\ge 1$, $\|\cdot\|_{L^p}$ is a norm; for $0<p<1$ it is a quasi–norm:
	$\|f+g\|_{L^p}^p\le \|f\|_{L^p}^p+\|g\|_{L^p}^p$ (triangle fails).
	Define
	\[
	L^\infty(E)=\{ f:\ \|f\|_{L^\infty}=\operatorname*{ess\,sup}_{x\in E}|f(x)|<\infty\}.
	\]

	\textbf{Basic facts.}
	For $1\le p\le\infty$, $L^p$ is complete (Banach). For $0<p<1$, $L^p$ is complete w.r.t.
	$d(f,g)=\|f-g\|_{L^p}^p$ but not locally convex.
	If $1<p<\infty$ and $q$ is conjugate ($\tfrac1p+\tfrac1q=1$), then $(L^p)^*\cong L^q$ via
	$f\mapsto (g\mapsto \int fg)$; $L^p$ is reflexive. For $p=1$, $(L^1)^*=L^\infty$; for $p=\infty$,
	$(L^\infty)^*$ strictly contains $L^1$.

	\textbf{Inequalities.}
	Hölder: $\int |uv|\le \|u\|_p\|v\|_q$.
	Minkowski: $\|u+v\|_p\le \|u\|_p+\|v\|_p$.
	On finite measure spaces, if $1\le q\le p\le\infty$ then
	$\|h\|_{L^q}\le \mu(E)^{\frac1q-\frac1p}\|h\|_{L^p}$.

	\textbf{Separability.}
	If $(E,\mu)$ is $\sigma$-finite, $L^p(E)$ is separable for $1\le p<\infty$
	(dense subset: rational simple functions). $L^\infty$ is not separable on
	$([0,1],\lambda)$ or $(\mathbb R^n,\lambda)$.

	\textbf{Uniform convexity.}
	$L^p$ is uniformly convex for $1<p<\infty$ (Clarkson), hence strictly convex and reflexive.

	\textbf{Density of nice functions on $\mathbb R^n$.}
	For $1\le p<\infty$, $C_c^\infty(\mathbb R^n)$ is dense in $L^p(\mathbb R^n)$.

	\medskip
	\textbf{Membership tests on $\mathbb R^n$.}
	Let $B=\{x:|x|\le 1\}$.

	\emph{Near the origin:} for $\beta\in\mathbb R$,
	\[
	f(x)=|x|^{-\beta}\mathbf 1_{B}(x)\in L^p(\mathbb R^n)
	\iff \beta p < n.
	\]

	\emph{At infinity:} for $\alpha\in\mathbb R$,
	\[
	g(x)=(1+|x|)^{-\alpha}\in L^p(\mathbb R^n)
	\iff \alpha p > n.
	\]

	\emph{Borderline with logs:}
	\[
	h(x)=|x|^{-n/p}\!\left(\log\frac{e}{|x|}\right)^{-\gamma}\mathbf 1_{B}
	\in L^p \iff \gamma>\tfrac1p,
	\]
	and similarly at infinity with $\left(\log(e+|x|)\right)^{-\gamma}$.

	\medskip
	\textbf{Examples and counterexamples.}
	\begin{itemize}
		\item \emph{No global inclusion for $p\ne q$ on $\mathbb R^n$.}
		If $p>q$, take $g(x)=(1+|x|)^{-\alpha}$ with $\tfrac{n}{p}<\alpha\le\tfrac{n}{q}$:
		$g\in L^p\setminus L^q$.
		If $p<q$, take $f(x)=|x|^{-\beta}\mathbf 1_{B}$ with $\tfrac{n}{q}<\beta\le\tfrac{n}{p}$:
		$f\in L^q\setminus L^p$.
		\item \emph{$L^\infty$ not separable.}
		The uncountable family $\{\mathbf 1_{[0,1/2)+t\ \mathrm{mod}\ 1}:t\in[0,1)\}$ is $1$-separated in $L^\infty$.
		\item \emph{Failure of triangle for $0<p<1$.}
		For $A,B$ disjoint with finite measure and $p\in(0,1)$:
		$\|\mathbf 1_{A\cup B}\|_p^p=\mu(A)+\mu(B)=\|\mathbf 1_A\|_p^p+\|\mathbf 1_B\|_p^p$,
		hence $\|\mathbf 1_{A\cup B}\|_p=\big(\|\mathbf 1_A\|_p^p+\|\mathbf 1_B\|_p^p\big)^{1/p}
		< \|\mathbf 1_A\|_p+\|\mathbf 1_B\|_p$.
	\end{itemize}

	\textbf{Convergence principles.}
	Monotone, Fatou, and Dominated Convergence Theorems govern limits of integrals.
	If $1<p<\infty$, bounded subsets of $L^p$ are weakly relatively compact (reflexivity).
	Uniform integrability plus convergence in measure $\Rightarrow L^1$ convergence (Vitali).


	\par\medskip\noindent\textbf{Concrete $L^p$ examples and counterexamples}\quad

	\bigskip
	\textbf{1. On a finite interval $[0,1]$.}

	\medskip
	\emph{Power singularities.}
	For $a\in\mathbb{R}$ and $1\le p<\infty$,
	\[
	x^{-a}\in L^p([0,1])
	\iff \int_0^1 x^{-ap}\,dx <\infty
	\iff ap<1 \ \ (\text{i.e.\ } a<1/p).
	\]
	\emph{Borderline with logs.}
	\[
	x^{-1/p}\!\left(\log\frac{e}{x}\right)^{-\gamma}\in L^p([0,1])
	\iff \gamma>\frac1p.
	\]

	\medskip
	\emph{Mild singularities.}
	$|\log x|^\beta\in L^p([0,1])$ for all $\beta\in\mathbb{R}$ and all $1\le p<\infty$.

	\medskip
	\emph{Examples.}
	\[
	\frac{1}{\sqrt{x}}\in L^p([0,1]) \iff p<2
	\quad\Rightarrow\quad
	\frac{1}{\sqrt{x}}\in L^1\setminus L^2.
	\]
	\[
	\mathbf 1_{[0,1]}\in L^p([0,1]) \ \text{for all } 1\le p\le\infty.
	\]
	$L^\infty$ on $[0,1]$ consists of essentially bounded functions; e.g.\ $\sin(1/x)\in L^\infty$,
	whereas $x^{-a}\notin L^\infty$ for $a>0$.

	\bigskip
	\textbf{2. On $\mathbb{R}^n$.}

	\medskip
	\emph{Decay at infinity.}
	For $\alpha>0$ and $1\le p<\infty$,
	\[
	(1+|x|)^{-\alpha} \in L^p(\mathbb{R}^n)
	\iff \int_1^\infty r^{n-1-\alpha p}\,dr<\infty
	\iff \alpha p>n.
	\]
	\emph{Borderline with logs.}
	\[
	(1+|x|)^{-n/p}\!\left(\log(e+|x|)\right)^{-\gamma}\in L^p(\mathbb{R}^n)
	\iff \gamma>\frac1p.
	\]

	\medskip
	\emph{Singularity at the origin (radial power).}
	For $\beta\in\mathbb{R}$,
	\[
	|x|^{-\beta}\,\mathbf 1_{B(0,1)}(x)\in L^p(\mathbb{R}^n)
	\iff \int_0^1 r^{n-1-\beta p}\,dr<\infty
	\iff \beta p<n.
	\]

	\medskip
	\emph{Canonical families.}
	\begin{itemize}
		\item $e^{-|x|^2}\in L^p(\mathbb{R}^n)$ for every $1\le p\le\infty$ (Gaussian decays super-polynomially).
		\item $e^{-|x|}\in L^p(\mathbb{R})$ for every $1\le p\le\infty$.
		\item Polynomials $x^k$ do not belong to $L^p(\mathbb{R})$ for any finite $p$ (no decay).
		\item Compactly supported but unbounded:
		$|x|^{-a}\mathbf 1_{|x|<1}\in L^p$ iff $ap<n$, but never in $L^\infty$ for $a>0$.
	\end{itemize}

	\bigskip
	\textbf{3. Crisp ``in / out'' templates.}

	\medskip
	\[
	(1+|x|)^{-(\frac{n}{p}+\varepsilon)} \in L^p(\mathbb{R}^n),\qquad
	(1+|x|)^{-n/p} \notin L^p(\mathbb{R}^n),
	\]
	\[
	|x|^{-\beta}\mathbf 1_{B(0,1)} \in L^p(\mathbb{R}^n)\iff \beta<\frac{n}{p}.
	\]

	\medskip
	\emph{Separating different exponents on $\mathbb{R}^n$.}
	For $p\neq q$,
	\begin{itemize}
		\item if $p>q$, choose $\alpha$ with $\tfrac{n}{p}<\alpha\le \tfrac{n}{q}$:
		$(1+|x|)^{-\alpha}\in L^p\setminus L^q$;
		\item if $p<q$, choose $\beta$ with $\tfrac{n}{q}<\beta\le \tfrac{n}{p}$:
		$|x|^{-\beta}\mathbf 1_{B(0,1)}\in L^q\setminus L^p$.
	\end{itemize}

	\bigskip
	\textbf{4. Sup norm (essential bound).}

	\medskip
	A function $f$ belongs to $L^\infty(E)$ iff there exists $M<\infty$ with
	$\mu(\{|f|>M\})=0$.
	Examples:
	\begin{itemize}
		\item $\sin(1/x)\in L^\infty([0,1])$ (bounded oscillatory).
		\item $(1+|x|)^{-\alpha}\in L^\infty(\mathbb{R}^n)$ for any $\alpha>0$ (bounded by $1$).
		\item $|x|^{-a}\mathbf 1_{B(0,1)}\notin L^\infty$ for $a>0$ (unbounded near $0$).
	\end{itemize}


\par\smallskip\noindent\textbf{Closed-form computation of the $L^p$ norm.}\quad
Consider
\[
f(x) = (1 + |x|)^{-\alpha}, \qquad x \in \mathbb{R},
\]
with parameters $\alpha>0$ and $p>0$.
The $L^p$ norm is
\[
\|f\|_p^p
= \int_{-\infty}^{\infty} |f(x)|^p\,dx
= 2\int_0^\infty (1+x)^{-\alpha p}\,dx.
\]
For $\alpha p > 1$, the integral converges and can be evaluated exactly:
\[
\int_0^\infty (1+x)^{-\alpha p}\,dx
= \frac{1}{\alpha p - 1}.
\]
Hence
\[
\boxed{\|f\|_p^p = \frac{2}{\alpha p - 1}}
\qquad\text{and}\qquad
\boxed{\|f\|_p = \left(\frac{2}{\alpha p - 1}\right)^{1/p}}.
\]

\par\smallskip\noindent\textbf{Validity.}\quad
The formula holds precisely when $\alpha p > 1$, since otherwise the integral diverges near infinity.
If $\alpha p \le 1$, then $(1+|x|)^{-\alpha p}$ decays too slowly and
$f \notin L^p(\mathbb{R})$.

\par\smallskip\noindent\textbf{Example.}\quad
For $\alpha = 1.5$ and $p = 2$,
\[
\|f\|_2 = \left(\frac{2}{3 - 1}\right)^{1/2} = 1.
\]

\par\smallskip\noindent\textbf{Remark.}\quad
A \emph{closed form} means the expression can be written exactly using
elementary operations (addition, multiplication, powers) without needing
series expansions or numerical integration.


\clearpage
% ---------- Concrete calculations for the Statement (readable layout) ----------

\par\medskip\noindent\textbf{Example A (for part (a)): \boldmath $f(x)=e^{-|x|}$ on $\mathbb{R}$}\quad
Let $1\le p<\infty$ and $q$ be conjugate $\bigl(\tfrac1p+\tfrac1q=1\bigr)$.
\begin{itemize}
	\item \textbf{$L^p$-norm.}
	\[
	\|f\|_{L^p}^p
	= \int_{\mathbb{R}} e^{-p|x|}\,dx
	= 2\!\int_0^\infty e^{-px}\,dx
	= \frac{2}{p}
	\qquad\Longrightarrow\qquad
	\boxed{\ \|f\|_{L^p} = \bigl(\tfrac{2}{p}\bigr)^{1/p}\ }.
	\]

	\item \textbf{Maximizer in the dual formula.}
	\[
	g_0(x) \;=\; \frac{f(x)^{\,p-1}}{\|f\|_{L^p}^{\,p-1}}
	\;=\; \frac{e^{-(p-1)|x|}}{\bigl((2/p)^{1/p}\bigr)^{p-1}},
	\qquad \|g_0\|_{L^q}=1.
	\]

	\item \textbf{Supremum equals the norm (equality case).}
	\[
	\int_{\mathbb{R}} f\,g_0
	\;=\; \frac{\int_{\mathbb{R}} e^{-p|x|}\,dx}{\|f\|_{L^p}^{\,p-1}}
	\;=\; \frac{2/p}{\bigl((2/p)^{1/p}\bigr)^{p-1}}
	\;=\; \bigl(\tfrac{2}{p}\bigr)^{1/p}
	\;=\; \|f\|_{L^p}.
	\]
\end{itemize}
Thus
\[
\|f\|_{L^p}
\;=\; \sup\Bigl\{\textstyle\int_{\mathbb{R}} f(x)g(x)\,dx \;:\; g\in L^q(\mathbb{R}),\ \|g\|_{L^q}\le 1\Bigr\}.
\]

\vspace{0.75\baselineskip}
\hrule
\vspace{0.75\baselineskip}
```

## CP-III-0017

```tex
\label{prob:cp-iii-0017}
density of simple functions in $L^p$.
We now describe this relation step by step.

\par\smallskip\noindent\textbf{1. Simple functions as the foundational case}\quad

A simple function has the form
\[
F(x,y) = \sum_{k=1}^m a_k\,1_{A_k}(x)\,1_{B_k}(y), \qquad a_k\ge 0.
\]
For such $F$, all integrals become finite sums:
\[
\int_{\mathbb{R}^n}\int_{\mathbb{R}^n} F(x,y)\,dy\,dx
= \sum_{k=1}^m a_k\,|A_k|\,|B_k|.
\]
Thus Minkowski's inequality for $p=1$ is an equality for simple functions.

\par\smallskip\noindent\textbf{2. Approximation of general nonnegative measurable functions}\quad

Every nonnegative measurable function $F$ on $\mathbb{R}^n\times\mathbb{R}^n$
admits an increasing sequence of simple functions $F_n$ such that
\[
F_n(x,y) \uparrow F(x,y) \qquad\text{for all }(x,y).
\]
This construction is canonical and works for every $F\ge 0$.

\par\smallskip\noindent\textbf{3. The Monotone Convergence Theorem connects the two}\quad

By the Monotone Convergence Theorem,
\[
\int F_n \to \int F,
\qquad
\int \Bigl|\int F_n(\cdot,y)\,dy\Bigr| \to
\int \Bigl|\int F(\cdot,y)\,dy\Bigr|.
\]
Since Minkowski holds exactly for each $F_n$, taking limits shows it holds
for $F$ as well.

\par\smallskip\noindent\textbf{4. Sign--changing regular functions}\quad

If $F$ is a smooth or regular function that takes both signs, use the
triangle inequality:
\[
\left|\int_{\mathbb{R}^n}F(x,y)\,dy\right|
\le \int_{\mathbb{R}^n}|F(x,y)|\,dy.
\]
Thus the sign--changing case reduces to the nonnegative case by replacing
$F$ with $|F|$.

\par\smallskip\noindent\textbf{5. Regular functions (Gaussians, trigonometric, polynomials)}\quad

Regular functions such as
\[
e^{-x^2-y^2},\qquad (1+x^2)(1+y^2)e^{-x^2-y^2},\qquad
\sin^2 x\,\sin^2 y,
\]
lie in every $L^p$, and satisfy
\[
F_n \uparrow F \quad \text{or} \quad F_n\to F \text{ in } L^p.
\]
Therefore all results established for simple functions extend to these
regular functions by approximation.

\bigskip
\noindent
\textbf{Summary.} Simple functions form the atomic building blocks. Every
regular function is a limit of simple ones. Minkowski's inequality is
verified first on the atoms, and then passed to the limit using monotone
or dominated convergence.


\par\smallskip\noindent\textbf{(i) $L^p$--spaces and Hölder conjugates.}\quad
```

## CP-III-0021

```tex
\label{prob:cp-iii-0021}
\begin{example}
	In $\mathbb R$: $\mathbb Q$ is meager $\Rightarrow$ $\mathbb R\setminus\mathbb Q$ is comeager.
	The set of Liouville numbers is a dense $G_\delta$ (comeager) but has Lebesgue measure $0$.
	A fat Cantor set is meager yet can have positive Lebesgue measure.
\end{example}
```

## CP-III-0004

```tex
\label{prob:cp-iii-0004}
We use the convention
\[
\mathcal{F}[f](\xi) = \widehat{f}(\xi)
:= \int_{\mathbb{R}^n} f(x)e^{-ix\cdot\xi}\,dx,
\qquad
\mathcal{F}^{-1}[g](x)
= \frac{1}{(2\pi)^n}\int_{\mathbb{R}^n} g(\xi)e^{ix\cdot\xi}\,d\xi.
\]

\par\smallskip\noindent\textbf{(a) Plancherel identity.}\quad
For $f,g\in\mathcal{S}(\mathbb{R}^n)$, using inversion we write
\[
f(x) = \frac{1}{(2\pi)^n}
\int_{\mathbb{R}^n} \widehat{f}(\xi)e^{ix\cdot\xi}\,d\xi,
\]
so
\[
(f,g)
= \int_{\mathbb{R}^n} f(x)\,\overline{g(x)}\,dx
= \frac{1}{(2\pi)^n}
\int_{\mathbb{R}^n}
\widehat{f}(\xi)\left(\int_{\mathbb{R}^n} e^{ix\cdot\xi}
\overline{g(x)}\,dx\right)d\xi.
\]
The inner integral equals $\overline{\widehat{g}(\xi)}$, hence
\[
(f,g) = \frac{1}{(2\pi)^n}
\int_{\mathbb{R}^n} \widehat{f}(\xi)\,
\overline{\widehat{g}(\xi)}\,d\xi
= \frac{1}{(2\pi)^n}(\widehat{f},\widehat{g}).
\]
By density of $\mathcal{S}$ in $L^2$ and continuity of $\mathcal{F}$ on
$L^2$, the formula extends to arbitrary $f,g\in L^2(\mathbb{R}^n)$.

\par\smallskip\noindent\textbf{(b) Double transform and bijectivity.}\quad
For $f\in\mathcal{S}$,
\[
\widehat{f}(\xi) = \int_{\mathbb{R}^n} f(x)e^{-ix\cdot\xi}\,dx,
\]
and
\[
\mathcal{F}[\widehat{f}](y)
= \int_{\mathbb{R}^n} \widehat{f}(\xi)e^{-iy\cdot\xi}\,d\xi
= \int_{\mathbb{R}^n}\!\!\int_{\mathbb{R}^n}
f(x)e^{-ix\cdot\xi}e^{-iy\cdot\xi}\,dx\,d\xi.
\]
Swapping the integrals and using that
$\int_{\mathbb{R}^n}e^{-i(x+y)\cdot\xi}\,d\xi = (2\pi)^n\delta(x+y)$ gives
\[
\mathcal{F}[\widehat{f}](y)
= (2\pi)^n f(-y)
= (2\pi)^n \check{f}(y).
\]
By continuity this identity holds for all $f\in L^2$.  In particular,
$\mathcal{F}$ is injective and its range is all of $L^2$; thus
$\mathcal{F}:L^2\to L^2$ is a bijection.  The inverse is bounded by the
Plancherel identity.

\par\smallskip\noindent\textbf{(c) Truncated integrals in $L^2$.}\quad
For $R>0$ set
\[
\widehat{f}_R(\xi)
:= \int_{B_R(0)} f(x)e^{-ix\cdot\xi}\,dx
= \mathcal{F}[\chi_{B_R}f](\xi).
\]
Then
\[
\widehat{f}_R - \widehat{f}
= \mathcal{F}[(\chi_{B_R}-1)f],
\]
and by Plancherel,
\[
\|\widehat{f}_R - \widehat{f}\|_{L^2}
= (2\pi)^{n/2}\,\|(\chi_{B_R}-1)f\|_{L^2}.
\]
Since $\chi_{B_R}\to 1$ pointwise and $|\chi_{B_R}|\le 1$, dominated
convergence gives $\|(\chi_{B_R}-1)f\|_{L^2}\to 0$ as $R\to\infty$, hence
$\widehat{f}_R\to\widehat{f}$ in $L^2(\mathbb{R}^n)$.

\par\smallskip\noindent\textbf{(d) Differentiation.}\quad
First assume $f\in\mathcal{S}(\mathbb{R}^n)$.  Then
\[
\mathcal{F}[D_j f](\xi)
= \int_{\mathbb{R}^n} (\partial_{x_j}f(x))e^{-ix\cdot\xi}\,dx
= -\int_{\mathbb{R}^n} f(x)\,\partial_{x_j}(e^{-ix\cdot\xi})\,dx
= i\xi_j\widehat{f}(\xi),
\]
since boundary terms vanish due to rapid decay.  For
$f\in C^1(\mathbb{R}^n)$ with $f,D_j f\in L^2$, choose a sequence
$f_k\in\mathcal{S}$ such that $f_k\to f$ and $D_j f_k\to D_j f$ in $L^2$.
The identity for $f_k$, together with the boundedness of $\mathcal{F}$ on
$L^2$, allows passage to the limit and yields
\[
\mathcal{F}[D_j f](\xi) = i\xi_j\widehat{f}(\xi)
\]
and hence $\xi_j\widehat{f}\in L^2$.

\par\smallskip\noindent\textbf{(e) The function $f(x)=\sin x/x$.}\quad
\par\smallskip\noindent\textbf{(i) $f\in L^2(\mathbb{R})$.}\quad
Near $x=0$ one has $\sin x\sim x$, so $\sin x/x$ is bounded and continuous.
For large $|x|$,
\[
\left|\frac{\sin x}{x}\right|
\le \frac{1}{|x|},
\]
hence
\[
\left|\frac{\sin x}{x}\right|^2 \le \frac{1}{x^2},
\]
and $\int_{|x|>1} x^{-2}\,dx<\infty$.  Therefore $f\in L^2(\mathbb{R})$.

\par\smallskip\noindent\textbf{(ii) Fourier transform.}\quad
Let $g(\xi)=\mathbf{1}_{(-1,1)}(\xi)$.  Then
\[
\mathcal{F}^{-1}[g](x)
= \frac{1}{2\pi}\int_{-1}^{1} e^{ix\xi}\,d\xi
= \frac{1}{2\pi}\left(\frac{e^{ix}-e^{-ix}}{ix}\right)
= \frac{1}{\pi}\frac{\sin x}{x}.
\]
Thus
\[
\frac{\sin x}{x}
= \pi\,\mathcal{F}^{-1}[\mathbf{1}_{(-1,1)}](x).
\]
Applying $\mathcal{F}$ and using $\mathcal{F}\circ\mathcal{F}^{-1}=\mathrm{Id}$
on $L^2$, we obtain
\[
\mathcal{F}\left[\frac{\sin x}{x}\right](\xi)
= \pi\,\mathbf{1}_{(-1,1)}(\xi)
=
\begin{cases}
	\pi, & -1<\xi<1,\\[0.3em]
	0,   & |\xi|\ge 1.
\end{cases}
\]

\par\smallskip\noindent\textbf{(f) Convolution.}\quad
\par\smallskip\noindent\textbf{(i) Pointwise bound.}\quad
For $x\in\mathbb{R}^n$,
\[
(f*g)(x) = \int_{\mathbb{R}^n} f(x-y)g(y)\,dy.
\]
By Cauchy--Schwarz,
\[
|f*g(x)|
\le \left(\int_{\mathbb{R}^n} |f(x-y)|^2 dy\right)^{1/2}
\left(\int_{\mathbb{R}^n} |g(y)|^2 dy\right)^{1/2}
= \|f\|_{L^2}\|g\|_{L^2}.
\]

\par\smallskip\noindent\textbf{(ii) Continuity and Fourier representation.}\quad
For $h\in\mathbb{R}^n$,
\[
(f*g)(x+h)-(f*g)(x)
= \int_{\mathbb{R}^n} [f(x+h-y)-f(x-y)]g(y)\,dy.
\]
Again by Cauchy--Schwarz,
\[
|(f*g)(x+h)-(f*g)(x)|
\le \|f(\cdot+h)-f\|_{L^2}\,\|g\|_{L^2},
\]
and since translations are continuous in $L^2$, the right-hand side tends to
$0$ as $h\to 0$, so $f*g$ is continuous.

If $f,g\in\mathcal{S}$, the convolution theorem gives
\[
\mathcal{F}[f*g](\xi) = \widehat{f}(\xi)\,\widehat{g}(\xi),
\]
and thus
\[
f*g = \mathcal{F}^{-1}[\widehat{f}\,\widehat{g}].
\]
For $f,g\in L^2$, one approximates by Schwartz functions and uses the
boundedness of $\mathcal{F}$ and density of $\mathcal{S}$ in $L^2$ to extend
this identity.

\par\medskip\noindent\textbf{Exercise 4.4 (Yukawa Green's function in $\mathbb{R}^3$)}\quad

Work in $\mathbb{R}^3$. For $k>0$, define
\[
G(x) = \frac{e^{-k|x|}}{4\pi |x|}, \qquad x\in\mathbb{R}^3\setminus\{0\}.
\]

\begin{enumerate}[(a)]
	\item Show that $G \in L^{1}(\mathbb{R}^3)$.

	\item Show that
	\[
	\widehat{G}(\xi) = \frac{1}{|\xi|^2 + k^2},
	\qquad \xi\in\mathbb{R}^3.
	\]
\end{enumerate}

\noindent\emph{Hint:} Use Exercise~4.2, part (c).
```

## CP-III-0005

```tex
\label{prob:cp-iii-0005}
Suppose $f,g\in L^{2}(\mathbb{R}^{n})$, and denote the Fourier--Plancherel
transform by $\mathcal{F}$.  You may assume any results already established
for the classical Fourier transform.

\begin{enumerate}[(a)]

	\item Show that
	\[
	(f,g)
	= \frac{1}{(2\pi)^{n}}
	\bigl(\,\mathcal{F}[g],\mathcal{F}[g]\,\bigr).
	\]

	\item Recall that $\check{f}(y)=f(-y)$.  Show that
	\[
	\mathcal{F}[\mathcal{F}[f]] = (2\pi)^{n}\,\check{f}.
	\]
	Hence, or otherwise, deduce that
	$\mathcal{F}:L^{2}(\mathbb{R}^{n})\to L^{2}(\mathbb{R}^{n})$ is a bijection,
	and that
	$\mathcal{F}^{-1}:L^{2}(\mathbb{R}^{n})\to L^{2}(\mathbb{R}^{n})$ is a
	bounded linear map.

	\item Show that
	\[
	\mathcal{F}[f](\xi)
	= \lim_{R\to\infty} \int_{B_{R}(0)} f(x)e^{-ix\cdot\xi}\,dx,
	\]
	with convergence in $L^{2}(\mathbb{R}^{n})$.

	\item Suppose that $f\in C^{1}(\mathbb{R}^{n})$ and
	$f, D_{j}f\in L^{2}(\mathbb{R}^{n})$.  Show that
	$\xi_{j}\,\mathcal{F}[f](\xi)\in L^{2}(\mathbb{R}^{n})$ and
	\[
	\mathcal{F}[D_{j}f](\xi)
	= i\xi_{j}\mathcal{F}[f](\xi).
	\]

	\item For $x\in\mathbb{R}$ let $f(x)=\dfrac{\sin x}{x}$.
	\begin{enumerate}[i.]
		\item Show that $f\in L^{2}(\mathbb{R})$.
		\item Show that
		\[
		\mathcal{F}[f](\xi)
		=
		\begin{cases}
			\pi, & -1<\xi<1,\\[0.3em]
			0,   & |\xi|\ge 1.
		\end{cases}
		\]
	\end{enumerate}

	\item
	\begin{enumerate}[i.]
		\item Show that for all $x\in\mathbb{R}^{n}$,
		\[
		|f*g(x)| \le \|f\|_{L^{2}}\|g\|_{L^{2}}.
		\]

		\item Show that $f*g\in C^{0}(\mathbb{R}^{n})$ and that
		\[
		f*g = \mathcal{F}^{-1}\bigl[\widehat{f}\,\widehat{g}\bigr],
		\]
		where
		\[
		\mathcal{F}^{-1}[h](x)
		= \frac{1}{(2\pi)^{n}} \int_{\mathbb{R}^{n}} h(\xi)\,e^{ix\cdot\xi}\,d\xi.
		\]
	\end{enumerate}

\end{enumerate}

\medskip
\noindent\emph{Hint for parts (a), (b), (d), (f):} approximate by Schwartz functions.
```

## CP-III-0011

```tex
\label{prob:cp-iii-0011}
example.
One sees that the curves coincide: translating in physical space does not
change the modulus of the Fourier transform.
This visualises the fact that ${\mathcal F}[\tau_a f](\xi)
= e^{-ia\xi}\widehat{f}(\xi)$, so only a phase factor is introduced, while the
spectrum’s magnitude remains invariant.
```

## CP-III-0013

```tex
\label{prob:cp-iii-0013}
Suppose $f,g\in L^{2}(\mathbb{R}^{n})$, and denote the Fourier--Plancherel
transform by $\mathcal{F}$.  You may assume any results already established
for the classical Fourier transform.

\begin{enumerate}[(a)]

	\item Show that
	\[
	(f,g)
	= \frac{1}{(2\pi)^{n}}
	\bigl(\,\mathcal{F}[g],\mathcal{F}[g]\,\bigr).
	\]

	\item Recall that $\check{f}(y)=f(-y)$.  Show that
	\[
	\mathcal{F}[\mathcal{F}[f]] = (2\pi)^{n}\,\check{f}.
	\]
	Hence, or otherwise, deduce that
	$\mathcal{F}:L^{2}(\mathbb{R}^{n})\to L^{2}(\mathbb{R}^{n})$ is a bijection,
	and that
	$\mathcal{F}^{-1}:L^{2}(\mathbb{R}^{n})\to L^{2}(\mathbb{R}^{n})$ is a
	bounded linear map.

	\item Show that
	\[
	\mathcal{F}[f](\xi)
	= \lim_{R\to\infty} \int_{B_{R}(0)} f(x)e^{-ix\cdot\xi}\,dx,
	\]
	with convergence in $L^{2}(\mathbb{R}^{n})$.

	\item Suppose that $f\in C^{1}(\mathbb{R}^{n})$ and
	$f, D_{j}f\in L^{2}(\mathbb{R}^{n})$.  Show that
	$\xi_{j}\,\mathcal{F}[f](\xi)\in L^{2}(\mathbb{R}^{n})$ and
	\[
	\mathcal{F}[D_{j}f](\xi)
	= i\xi_{j}\mathcal{F}[f](\xi).
	\]

	\item For $x\in\mathbb{R}$ let $f(x)=\dfrac{\sin x}{x}$.
	\begin{enumerate}[i.]
		\item Show that $f\in L^{2}(\mathbb{R})$.
		\item Show that
		\[
		\mathcal{F}[f](\xi)
		=
		\begin{cases}
			\pi, & -1<\xi<1,\\[0.3em]
			0,   & |\xi|\ge 1.
		\end{cases}
		\]
	\end{enumerate}

	\item
	\begin{enumerate}[i.]
		\item Show that for all $x\in\mathbb{R}^{n}$,
		\[
		|f*g(x)| \le \|f\|_{L^{2}}\|g\|_{L^{2}}.
		\]

		\item Show that $f*g\in C^{0}(\mathbb{R}^{n})$ and that
		\[
		f*g = \mathcal{F}^{-1}\bigl[\widehat{f}\,\widehat{g}\bigr],
		\]
		where
		\[
		\mathcal{F}^{-1}[h](x)
		= \frac{1}{(2\pi)^{n}} \int_{\mathbb{R}^{n}} h(\xi)\,e^{ix\cdot\xi}\,d\xi.
		\]
	\end{enumerate}

\end{enumerate}

\medskip
\noindent\emph{Hint for parts (a), (b), (d), (f):} approximate by Schwartz functions.

\par\medskip\noindent\textbf{Theory: Relation between $\mathcal{S}(\mathbb{R}^n)$ and $L^{2}(\mathbb{R}^n)$}\quad

We recall that the Schwartz space $\mathcal{S}(\mathbb{R}^n)$ consists of all
smooth functions $f\in C^\infty(\mathbb{R}^n)$ such that for every pair of
multi-indices $\alpha,\beta$,
\[
\sup_{x\in\mathbb{R}^n} |x^\alpha D^\beta f(x)| < \infty.
\]
Thus $f$ and all its derivatives decay faster than any polynomial.  This leads
to four fundamental relations between $\mathcal{S}$, $L^2$, and the
Fourier--Plancherel transform.

\par\smallskip\noindent\textbf{1. Inclusion $\mathcal{S}\subset L^2$}\quad
From the defining estimate, for each $N\in\mathbb{N}$ there exists $C_N>0$ such
that
\[
|f(x)| \le C_N (1+|x|)^{-N}.
\]
Choosing $N>\frac{n}{2}$ yields
\[
\int_{\mathbb{R}^n} |f(x)|^2\,dx
\le C_N^2 \int_{\mathbb{R}^n} (1+|x|)^{-2N} dx < \infty.
\]
Hence
\[
\mathcal{S}(\mathbb{R}^n) \subset L^2(\mathbb{R}^n),
\]
and the inclusion map is continuous with respect to the natural topologies.

\par\smallskip\noindent\textbf{2. Density of $\mathcal{S}$ in $L^2$}\quad
A key property is that $\mathcal{S}(\mathbb{R}^n)$ is dense in
$L^2(\mathbb{R}^n)$:
for every $f\in L^2$ there exists $(f_k)\subset\mathcal{S}$ such that
$\|f_k-f\|_{L^2}\to 0$.

One standard construction proceeds as follows:
\begin{enumerate}
	\item Truncate $f$ to a large ball:
	$f^{(R)}(x) := f(x)\mathbf{1}_{\{|x|\le R\}}$.
	Then $f^{(R)} \to f$ in $L^2$ as $R\to\infty$.
	\item Mollify: choose a smooth compactly supported mollifier $\eta_\varepsilon$,
	and set $f^{(R,\varepsilon)} = f^{(R)} * \eta_\varepsilon$.
	Then $f^{(R,\varepsilon)}\in C_c^\infty(\mathbb{R}^n)$ and
	$f^{(R,\varepsilon)}\to f^{(R)}$ in $L^2$ as $\varepsilon\to 0$.
\end{enumerate}
Since $C_c^\infty(\mathbb{R}^n)\subset\mathcal{S}(\mathbb{R}^n)$, this proves
that
\[
\overline{\mathcal{S}(\mathbb{R}^n)}^{\,L^2} = L^2(\mathbb{R}^n).
\]

\par\smallskip\noindent\textbf{3. Extension of the Fourier transform to $L^2$ (Fourier--Plancherel theorem)}\quad

On the Schwartz space the Fourier transform is given by
\[
\widehat{f}(\xi)
= \int_{\mathbb{R}^n} f(x) e^{-ix\cdot\xi} \, dx,
\]
and satisfies:
\begin{itemize}
	\item $\mathcal{F}:\mathcal{S} \to \mathcal{S}$ is a bijection.
	\item \emph{Parseval identity:}
	\[
	\int_{\mathbb{R}^n} f(x)\overline{g(x)}\,dx
	= \frac{1}{(2\pi)^n}
	\int_{\mathbb{R}^n} \widehat{f}(\xi)\,
	\overline{\widehat{g}(\xi)}\,d\xi.
	\]
	\item Therefore,
	\[
	\|\widehat{f}\|_{L^2}
	= (2\pi)^{n/2} \|f\|_{L^2}.
	\]
\end{itemize}

This shows that $\mathcal{F}:\mathcal{S}\to L^2$ is an isometry up to
$(2\pi)^{n/2}$.
Since $\mathcal{S}$ is dense in $L^2$, there exists a unique extension
\[
\mathcal{F}: L^2(\mathbb{R}^n) \to L^2(\mathbb{R}^n)
\]
that is bounded and satisfies the same norm identity.
The extension is called the \emph{Fourier--Plancherel transform}.

On $\mathcal{S}$ we have the identity
\[
\mathcal{F}[\mathcal{F}[f]](\xi) = (2\pi)^n f(-\xi),
\]
and by continuity this holds for all $f\in L^2$.
In particular $\mathcal{F}$ is invertible and its inverse is the inverse Fourier
transform.

\par\smallskip\noindent\textbf{4. Why approximation by Schwartz functions works}\quad

For many identities one proves the formula first for
$f\in\mathcal{S}(\mathbb{R}^n)$, where the Fourier transform is defined by an
absolutely convergent integral and all operations are legal.
Then, using:
\begin{itemize}
	\item the density $\mathcal{S}\subset L^2$,
	\item the fact that $\mathcal{F}:L^2\to L^2$ is bounded,
\end{itemize}
one may pass to the limit and obtain the corresponding identity for general
$f\in L^2$.

More precisely, if $f_k\in\mathcal{S}$ and $f_k\to f$ in $L^2$, and if an
identity
\[
\mathcal{G}(f_k) = \mathcal{H}(f_k)
\]
holds for all $k$, and the operators $\mathcal{G}$ and $\mathcal{H}$ are
continuous on $L^2$, then the same identity holds for $f$.
This mechanism underlies the proofs of Parseval's identity, the differentiation
rule $\mathcal{F}[D_j f]= i\xi_j \widehat{f}$, the convolution theorem, and
other statements used in Fourier--Plancherel theory.

\par\medskip\noindent\textbf{Theory: Tempered Distributions and the Fourier Transform on $\mathcal{S}'(\mathbb{R}^n)$}\quad

The Schwartz space $\mathcal{S}(\mathbb{R}^n)$ consists of rapidly decaying
smooth functions.  Its topological dual,
\[
\mathcal{S}'(\mathbb{R}^n)
:= \{\text{continuous linear functionals }
T:\mathcal{S}(\mathbb{R}^n)\to\mathbb{C}\},
\]
is called the space of \emph{tempered distributions}.
Tempered distributions include all $L^p$ functions ($1\le p\le\infty$),
all locally integrable functions with at most polynomial growth, the Dirac
delta and its derivatives, principal value kernels, and many oscillatory
objects.

\par\smallskip\noindent\textbf{1. Basic Examples}\quad
\begin{itemize}
	\item \textbf{Dirac delta:}
	$\langle\delta,\varphi\rangle = \varphi(0)$.
	\item \textbf{Derivative of delta:}
	$\langle\delta',\varphi\rangle = -\varphi'(0)$.
	\item \textbf{Polynomial growth functions:}
	if $|f(x)|\le C(1+|x|)^N$ and $f$ is locally integrable, then
	\[
	\langle f,\varphi\rangle := \int_{\mathbb{R}^n} f(x)\varphi(x)\,dx
	\]
	defines a tempered distribution.
	\item \textbf{Principal value kernels:}
	$\mathrm{p.v.}(1/x)$, the Hilbert transform kernel, etc., belong to
	$\mathcal{S}'$.
\end{itemize}

\par\smallskip\noindent\textbf{2. Fourier Transform on $\mathcal{S}'$}\quad
Since $\mathcal{F}:\mathcal{S}\to\mathcal{S}$ is a bijection, we define the
Fourier transform of $T\in\mathcal{S}'$ by duality:
\[
\boxed{
	\langle \mathcal{F}T, \varphi \rangle
	:= \langle T, \mathcal{F}\varphi \rangle,
	\qquad \varphi\in\mathcal{S}.
}
\]
This makes $\mathcal{F}:\mathcal{S}'\to\mathcal{S}'$ a continuous bijection.
The inversion formula continues to hold:
\[
\mathcal{F}^{-1}T = \check{\mathcal{F}T}\,/(2\pi)^n,
\]
where $\check{T}(\varphi):=T(\check{\varphi})$ and $\check{\varphi}(x)=\varphi(-x)$.

\par\smallskip\noindent\textbf{3. Fourier Transform Identities in $\mathcal{S}'$}\quad
The usual differentiation and multiplication rules extend to tempered
distributions:
\[
\mathcal{F}[D^\alpha T](\xi)
= (i\xi)^\alpha \widehat{T}(\xi),
\qquad
\mathcal{F}[x^\alpha T](\xi)
= i^{|\alpha|} D^\alpha_{\xi}\widehat{T}(\xi).
\]
Convolution with a Schwartz function is always well-defined and produces
another tempered distribution.

\par\smallskip\noindent\textbf{4. Examples of Fourier Transforms in $\mathcal{S}'$}\quad
\begin{align*}
	\widehat{\delta} &= 1, \\
	\widehat{\delta'} &= i\xi, \\
	\widehat{1} &= (2\pi)^n \delta, \\
	\widehat{\mathrm{p.v.}\tfrac1x} &= -i\pi\,\mathrm{sgn}(\xi), \\
	\widehat{\tfrac1{|x|}}(\xi) &= \frac{4\pi}{|\xi|^2}
	\qquad (\text{in }\mathbb{R}^3).
\end{align*}
Such identities cannot be understood within $L^1$ or $L^2$ alone, but follow
naturally in the framework of tempered distributions.

Tempered distributions thus provide the natural and maximal domain on which
the Fourier transform is an automorphism, preserving the full symmetry between
differentiation, multiplication, convolution, and decay.
```

## CP-III-0014

```tex
\label{prob:cp-iii-0014}
Consider the ODE
\begin{equation}
	-\phi''(x) + \phi(x) = f(x), \qquad f:\mathbb{R}\to\mathbb{C}.
\end{equation}

\par\smallskip\noindent\textbf{(a)}\quad
Consider the ODE
\begin{equation}
	-\phi''(x) + \phi(x) = f(x), \qquad f:\mathbb{R}\to\mathbb{C}.
\end{equation}

\par\smallskip\noindent\textbf{(a)}\quad
Assume $f\in\mathcal{S}(\mathbb{R})$.
Taking the Fourier transform of both sides gives
\[
\widehat{-\phi'' + \phi}(\xi)
= -\,\widehat{\phi''}(\xi) + \widehat{\phi}(\xi).
\]

Using the standard identities
\[
\widehat{g'}(\xi) = (2\pi i\xi)\,\widehat{g}(\xi),
\qquad
\widehat{g''}(\xi) = -(2\pi\xi)^{2}\widehat{g}(\xi)
= -4\pi^{2}\xi^{2}\widehat{g}(\xi),
\]
we obtain
\[
-\widehat{\phi''}(\xi) + \widehat{\phi}(\xi)
= 4\pi^{2}\xi^{2}\widehat{\phi}(\xi) + \widehat{\phi}(\xi)
= (4\pi^{2}\xi^{2} + 1)\widehat{\phi}(\xi).
\]

Thus the transformed equation is
\[
(4\pi^{2}\xi^{2} + 1)\,\widehat{\phi}(\xi) = \widehat{f}(\xi),
\]
and hence
\[
\boxed{
	\widehat{\phi}(\xi)
	= \frac{\widehat{f}(\xi)}{1 + 4\pi^{2}\xi^{2}}.
}
\]

Since the multiplier $(1+4\pi^{2}\xi^{2})^{-1}$ is smooth and rapidly decaying,
multiplication by it preserves the Schwartz class.
Thus $\phi\in\mathcal{S}(\mathbb{R})$.

The homogeneous equation $-\psi''+\psi=0$ has solutions
$\psi(x)=Ce^{x}+De^{-x}$, none of which lie in $\mathcal{S}$ unless $C=D=0$.
Hence the solution in $\mathcal{S}$ is unique.

\medskip
\noindent
It comes from the Fourier transform of derivatives.
Start with
\[
-\phi''(x)+\phi(x)=f(x).
\]
Taking the Fourier transform in $x$ and using linearity,
\[
\widehat{-\phi''+\phi}(\xi)
= -\,\widehat{\phi''}(\xi) + \widehat{\phi}(\xi).
\]

We use the standard identity (with the convention
$\widehat{g}(\xi)=\int_{\mathbb{R}} e^{-2\pi i x\xi} g(x)\,dx$):
\[
\widehat{g'}(\xi) = (2\pi i\xi)\,\widehat{g}(\xi).
\]
Applying it twice gives
\[
\widehat{g''}(\xi)
= (2\pi i\xi)^2 \widehat{g}(\xi)
= -4\pi^{2}\xi^{2}\widehat{g}(\xi).
\]

Taking $g=\phi$, we obtain
\[
\widehat{\phi''}(\xi) = -4\pi^{2}\xi^{2}\widehat{\phi}(\xi).
\]

Substituting this into the transformed equation,
\[
\widehat{-\phi''+\phi}(\xi)
= -\,\widehat{\phi''}(\xi) + \widehat{\phi}(\xi)
= -\big(-4\pi^{2}\xi^{2}\widehat{\phi}(\xi)\big) + \widehat{\phi}(\xi)
= (4\pi^{2}\xi^{2}+1)\widehat{\phi}(\xi).
\]

\par\smallskip\noindent\textbf{(b)}\quad
Define the Green's function
\[
G(x)=
\begin{cases}
	\frac12 e^{x}, & x<0,\\[0.3em]
	\frac12 e^{-x}, & x\ge 0.
\end{cases}
\]
A direct calculation yields
\[
\widehat{G}(\xi) = \frac{1}{1+4\pi^{2}\xi^{2}}.
\]
Thus
\[
\widehat{\phi}(\xi)
= \widehat{f}(\xi)\,\widehat{G}(\xi)
= \widehat{f*G}(\xi),
\]
and by injectivity of the Fourier transform,
\[
\boxed{
	\phi(x) = (f*G)(x)
	= \int_{\mathbb{R}} f(y)\,G(x-y)\,dy.
}
\]

\bigskip

\par\smallskip\noindent\textbf{Illustrations}\quad

\par\smallskip\noindent\textbf{1. Compactly supported bump function and its Fourier transform.}\quad


\par\smallskip\noindent\textbf{2. Green's function for $-\phi''+\phi=f$.}\quad


\par\smallskip\noindent\textbf{3. Example convolution $f*G$.}\quad


\clearpage

\par\medskip\noindent\textbf{Exercise 4.2 (Radial Fourier Transform in $\mathbb{R}^{3}$)}\quad

Suppose $f \in L^{1}(\mathbb{R}^{3})$ is a radial function, i.e.\ $f(Rx) = f(x)$
whenever $R \in SO(3)$ is a rotation.

\begin{enumerate}[(a)]
	\item Show that $\widehat{f}$ is radial.

	\item Suppose that $\xi = (0,0,\zeta)$. By writing the Fourier integral in
	spherical coordinates, show that
	\[
	\widehat{f}(\xi)
	= \int_{r=0}^{\infty}\int_{\theta=0}^{\pi}\int_{\phi=0}^{2\pi}
	f(r)\,e^{-i\zeta r \cos\theta}\,r^{2}\sin\theta\,d\phi\,d\theta\,dr.
	\]

	\item Making the substitution $s=\cos\theta$, and using the fact that
	$\widehat{f}$ is radial, deduce that
	\[
	\widehat{f}(\xi)
	= 4\pi \int_{0}^{\infty}
	f(r)\,\frac{\sin(r|\xi|)}{r|\xi|}\,r^{2}\,dr
	\]
	for any $\xi \in \mathbb{R}^{3}$.
\end{enumerate}


Suppose $f\in L^{1}(\mathbb{R}^{3})$ is a radial function, i.e.\ $f(Rx)=f(x)$ for all rotations
$R\in SO(3)$.

\par\smallskip\noindent\textbf{(a)}\quad
To show that $\widehat{f}$ is radial, take any $R\in SO(3)$:
\[
\widehat{f}(R\xi)
= \int_{\mathbb{R}^{3}} f(x)e^{-2\pi i x\cdot (R\xi)}\,dx.
\]
With the substitution $x=Ry$ (Jacobian $=1$),
\[
\widehat{f}(R\xi)
= \int_{\mathbb{R}^{3}} f(Ry)e^{-2\pi i (Ry)\cdot (R\xi)}\,dy.
\]
Since $f$ is radial, $f(Ry)=f(y)$, and rotations preserve dot products:
$(Ry)\cdot (R\xi)=y\cdot\xi$. Hence
\[
\widehat{f}(R\xi)=\int_{\mathbb{R}^{3}} f(y)e^{-2\pi i y\cdot\xi}\,dy=\widehat{f}(\xi),
\]
showing that $\widehat{f}$ is radial.

\par\smallskip\noindent\textbf{(b)}\quad
Since $\widehat{f}$ is radial, we may assume $\xi=(0,0,\zeta)$ with
$\zeta=|\xi|$. In spherical coordinates
$x=(r,\theta,\phi)$, one has
\[
x\cdot\xi=r\zeta\cos\theta,
\qquad
dx=r^{2}\sin\theta\,dr\,d\theta\,d\phi,
\qquad
f(x)=f(r).
\]
Thus
\[
\widehat{f}(\xi)
=\int_{0}^{\infty}\int_{0}^{\pi}\int_{0}^{2\pi}
f(r)e^{-i\zeta r\cos\theta}\,
r^{2}\sin\theta\;d\phi\,d\theta\,dr.
\]

\par\smallskip\noindent\textbf{(c)}\quad
Substituting $s=\cos\theta$ gives
\[
\int_{0}^{\pi} e^{-i\zeta r\cos\theta}\sin\theta\,d\theta
=\int_{-1}^{1} e^{-i\zeta r s}\,ds
=2\frac{\sin(\zeta r)}{\zeta r}.
\]
Since $\int_{0}^{2\pi} d\phi = 2\pi$, we obtain
\[
\widehat{f}(\xi)
=4\pi \int_{0}^{\infty}
f(r)\,\frac{\sin(r|\xi|)}{r|\xi|}\,r^{2}\,dr.
\]
Thus $\widehat{f}$ is radial and given by
\[
\boxed{
	\widehat{f}(\xi)
	=4\pi\int_{0}^{\infty} f(r)\,\frac{\sin(r|\xi|)}{r|\xi|}\,r^{2}\,dr.
}
\]


\par\smallskip\noindent\textbf{Theory: Radial Fourier transform in $\mathbb{R}^3$}\quad

A function $f:\mathbb{R}^{3}\to\mathbb{C}$ is called \emph{radial} if
there is $F:[0,\infty)\to\mathbb{C}$ such that
\[
f(x) = F(|x|)\qquad\text{for all }x\in\mathbb{R}^{3}.
\]
Equivalently, $f$ is invariant under all rotations:
\[
f(Rx) = f(x)\qquad\text{for all }R\in SO(3).
\]

\par\smallskip\noindent\textbf{Fourier transform and rotations.}\quad
The Fourier transform in $\mathbb{R}^{3}$ is
\[
\widehat{f}(\xi)
= \int_{\mathbb{R}^{3}} f(x)\,e^{-2\pi i x\cdot\xi}\,dx.
\]
For any rotation $R\in SO(3)$, one has
\[
\widehat{f\circ R}(\xi)
= \widehat{f}(R^{-1}\xi).
\]
Indeed,
\begin{center}
\resizebox{\linewidth}{!}{$\displaystyle
\widehat{f\circ R}(\xi)
= \int_{\mathbb{R}^{3}} f(Rx)e^{-2\pi i x\cdot\xi}\,dx
= \int_{\mathbb{R}^{3}} f(y)e^{-2\pi i (Ry)\cdot\xi}\,dy
= \int_{\mathbb{R}^{3}} f(y)e^{-2\pi i y\cdot (R^{-1}\xi)}\,dy
= \widehat{f}(R^{-1}\xi),
$}
\end{center}
where we used the change of variables $x=Ry$ and the fact that rotations
preserve dot products. If $f$ is radial, then $f\circ R=f$ for all $R$, hence
\[
\widehat{f}(R\xi) = \widehat{f}(\xi)\qquad\forall R\in SO(3),
\]
and thus $\widehat{f}$ is radial as well.

\par\smallskip\noindent\textbf{Spherical coordinates.}\quad
Since $\widehat{f}$ is radial, its value at $\xi$ depends only on $|\xi|$.
Given $\xi\in\mathbb{R}^{3}$ with $|\xi|>0$, we choose a rotation $R$ such that
\[
R\xi = (0,0,|\xi|).
\]
Using radiality of $\widehat{f}$ we may compute $\widehat{f}(R\xi)$ instead of
$\widehat{f}(\xi)$; in spherical coordinates $x=(r,\theta,\phi)$ we have
\[
x\cdot R\xi = r|\xi|\cos\theta,
\qquad
dx = r^{2}\sin\theta\,dr\,d\theta\,d\phi,
\qquad
f(x)=f(r).
\]
Therefore,
\begin{equation}\label{eq:radial-FT-spherical}
	\widehat{f}(\xi)
	= \int_{0}^{\infty}\int_{0}^{\pi}\int_{0}^{2\pi}
	f(r)\,e^{-i r|\xi|\cos\theta}\,r^{2}\sin\theta\,
	d\phi\,d\theta\,dr.
\end{equation}

\par\smallskip\noindent\textbf{Angular integration and the 3D radial kernel.}\quad
The $\phi$--integral is trivial:
\[
\int_{0}^{2\pi} d\phi = 2\pi.
\]
For the $\theta$--integral we use the substitution $s=\cos\theta$,
$ds=-\sin\theta\,d\theta$, which gives
\[
\int_{0}^{\pi} e^{-i r|\xi|\cos\theta}\sin\theta\,d\theta
= \int_{-1}^{1} e^{-i r|\xi| s}\,ds
= 2\,\frac{\sin(r|\xi|)}{r|\xi|}.
\]
Inserting these into \eqref{eq:radial-FT-spherical} yields
\[
\widehat{f}(\xi)
= 4\pi \int_{0}^{\infty}
f(r)\,\frac{\sin(r|\xi|)}{r|\xi|}\,r^{2}\,dr,
\]
which is the standard formula for the Fourier transform of a radial
$L^{1}$-function in $\mathbb{R}^{3}$.

\par\smallskip\noindent\textbf{Remark (connection with Bessel functions).}\quad
In general dimension $n$, the Fourier transform of a radial function involves
Bessel functions and can be written as
\[
\widehat{f}(\xi)
= (2\pi)^{n/2}|\xi|^{-(n/2-1)}
\int_{0}^{\infty} f(r)\,
J_{n/2-1}(2\pi r|\xi|)\,r^{n/2}\,dr.
\]
For $n=3$ this reduces to the above formula, since the corresponding Bessel
function combination is
\[
\frac{\sin(r|\xi|)}{r|\xi|},
\]
the spherical Bessel function of order $0$.

\par\smallskip\noindent\textbf{Examples of radial Fourier transforms in $\mathbb{R}^3$}\quad

\par\smallskip\noindent\textbf{Example 1 (Indicator of a ball).}\quad
Let
\[
f(x) = \mathbf{1}_{\{|x|\le a\}}(x), \qquad a>0.
\]
Then $f$ is radial with $f(r)=1$ for $0\le r\le a$ and $0$ otherwise, and the
radial Fourier transform formula gives
\[
\widehat{f}(\xi)
=4\pi\int_0^a \frac{\sin(r|\xi|)}{r|\xi|}\,r^2\,dr
=\frac{4\pi}{|\xi|}\int_0^a r\sin(r|\xi|)\,dr.
\]
Using
\[
\int r\sin(\rho r)\,dr
= -\frac{r\cos(\rho r)}{\rho}
+\frac{\sin(\rho r)}{\rho^2} + C,
\]
we obtain, with $\rho=|\xi|$,
\[
\int_0^a r\sin(\rho r)\,dr
= -\frac{a\cos(\rho a)}{\rho}
+\frac{\sin(\rho a)}{\rho^2}.
\]
Hence
\[
\widehat{f}(\xi)
=4\pi\left(
\frac{\sin(a|\xi|)}{|\xi|^3}
-\frac{a\cos(a|\xi|)}{|\xi|^2}
\right),
\qquad \xi\neq 0.
\]
The value at $\xi=0$ is given by continuity and equals the volume of the ball,
$\widehat{f}(0)=\frac{4\pi a^3}{3}$.

\par\smallskip\noindent\textbf{Example 2 (Gaussian).}\quad
Consider the radial Gaussian
\[
f(x)=e^{-|x|^2}, \qquad x\in\mathbb{R}^3.
\]
Using the one-dimensional identity
\[
\int_{\mathbb{R}} e^{-x^2} e^{-i x\xi}\,dx
= \sqrt{\pi}\,e^{-\xi^2/4},
\]
and the factorisation $e^{-|x|^2}=e^{-x_1^2}e^{-x_2^2}e^{-x_3^2}$, we obtain
\[
\widehat{f}(\xi)
= \bigl(\sqrt{\pi} e^{-\xi_1^2/4}\bigr)
\bigl(\sqrt{\pi} e^{-\xi_2^2/4}\bigr)
\bigl(\sqrt{\pi} e^{-\xi_3^2/4}\bigr)
= \pi^{3/2} e^{-|\xi|^2/4}.
\]
Thus
\[
\boxed{
	\widehat{e^{-|x|^2}}(\xi)
	= \pi^{3/2} e^{-|\xi|^2/4},
}
\]
which is manifestly radial. This is consistent with the radial integral
\[
\widehat{f}(\xi)
= 4\pi\int_0^\infty e^{-r^2}
\frac{\sin(r|\xi|)}{r|\xi|}\,r^2\,dr.
\]

\par\smallskip\noindent\textbf{Example 3 (Yukawa kernel).}\quad
Let
\[
f(x) = \frac{e^{-|x|}}{|x|}, \qquad x\in\mathbb{R}^3,
\]
so that $f(r)=e^{-r}/r$ is radial and integrable. Then
\[
\widehat{f}(\xi)
= 4\pi\int_0^\infty \frac{e^{-r}}{r}\,
\frac{\sin(r|\xi|)}{r|\xi|}\,r^2\,dr
= 4\pi\frac{1}{|\xi|}
\int_0^\infty e^{-r}\sin(r|\xi|)\,dr.
\]
Using the Laplace transform identity
\[
\int_0^\infty e^{-r}\sin(\rho r)\,dr
= \frac{\rho}{1+\rho^2},
\]
with $\rho=|\xi|$, we find
\[
\widehat{f}(\xi)
= \frac{4\pi}{1+|\xi|^2}.
\]
This radial function is (up to constants) the Fourier symbol of the resolvent
$(-\Delta+1)^{-1}$.

\par\smallskip\noindent\textbf{Figures: Yukawa Kernel and its Fourier Transform}\quad


\par\smallskip\noindent\textbf{Comparison: Coulomb Kernel vs. Yukawa Kernel}\quad

The Coulomb kernel in $\mathbb{R}^3$ is
\[
K_{\mathrm{C}}(x) = \frac{1}{|x|},
\]
and the Yukawa kernel is
\[
K_{\mathrm{Y}}(x) = \frac{e^{-|x|}}{|x|}.
\]
Both are radial functions of $r=|x|$. The Yukawa kernel introduces exponential
screening of the long-range $1/r$ interaction.
```
