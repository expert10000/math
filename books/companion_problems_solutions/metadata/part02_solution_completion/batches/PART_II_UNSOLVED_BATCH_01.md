# Part II missing-solution batch 01

- problems: **20**
- IDs: CP-II-0006, CP-II-0008, CP-II-0013, CP-II-0017, CP-II-0021, CP-II-0022, CP-II-0028, CP-II-0029, CP-II-0035, CP-II-0052, CP-II-0062, CP-II-0072, CP-II-0082, CP-II-0090, CP-II-0092, CP-II-0100, CP-II-0122, CP-II-0127, CP-II-0131, CP-II-0133

## CP-II-0006

- chapter line: 13

```tex
\label{prob:cp-ii-0006}
\par\noindent (a)\quad Show that $\mathcal{S}$ is a vector subspace of
	$\mathcal{E}(\mathbb{R}^n)$.  Show that if
	$\{\phi_j\}_{j=1}^\infty$ is a sequence of rapidly
	decreasing functions which tends to zero in $\mathcal{S}$,
	then $\phi_j \to 0$ in $\mathcal{E}(\mathbb{R}^n)$.

	\par\noindent (b)\quad Show that $\mathcal{D}(\mathbb{R}^n)$ is a vector subspace
	of $\mathcal{S}$.  Show that if $\{\phi_j\}_{j=1}^\infty$
	is a sequence of compactly supported functions which tends
	to zero in $\mathcal{D}(\mathbb{R}^n)$, then
	$\phi_j \to 0$ in $\mathcal{S}$.

	\par\noindent (c)\quad Give an example of a sequence
	$\{\phi_j\}_{j=1}^\infty \subset C_0^\infty(\mathbb{R}^n)$
	such that

		\par\noindent (i)\quad $\phi_j \to 0$ in $\mathcal{S}$, but
		$\{\phi_j\}$ has no limit in
		$\mathcal{D}(\mathbb{R}^n)$;
		\par\noindent (ii)\quad $\phi_j \to 0$ in $\mathcal{E}(\mathbb{R}^n)$,
		but $\{\phi_j\}$ has no limit in $\mathcal{S}$.
```

## CP-II-0008

- chapter line: 38

```tex
\label{prob:cp-ii-0008}
\renewcommand\labelenumi{(\alph{enumi})}
\par\noindent\textbullet\quad If $U_1,U_2$ are open, then $U_1\cup U_2$ and $U_1\cap U_2$ are open.
\par\noindent\textbullet\quad If $E_1,E_2$ are closed, then $E_1\cup E_2$ and $E_1\cap E_2$ are closed.
\par\noindent\textbullet\quad For any collection $\mathcal U$ of open sets: $\bigcup\mathcal U$ is open; $\bigcap\mathcal U$ need not be open (e.g.\ $\cap_{n\ge1}(-1/n,1/n)=\{0\}$).
For closed sets: arbitrary intersections are closed, finite unions are closed, infinite unions need not be closed.
```

## CP-II-0013

- chapter line: 47

```tex
\label{prob:cp-ii-0013}
Let $C[0,1]$ be the metric space of continuous functions $f:[0,1]\to\mathbb{R}$ with the distance
\[
d(f,g) = \sup_{x\in[0,1]} |f(x)-g(x)|.
\]

For $f,g\in C[0,1]$, consider $h(x)=|f(x)-g(x)|$.
$h$ is continuous on the compact set $[0,1]$, so by the Weierstrass theorem it attains its maximum.
Thus
\[
d(f,g)=\max_{x\in[0,1]}|f(x)-g(x)|.
\]

Let $X=\{f\in C[0,1]: f(x)\in[0,1]\ \forall x\in[0,1]\}$.
Consider the sequence $f_n(x)=x^n$. Then $f_n\in X$.

Pointwise, $f_n(x)\to f(x)$ where
\[
f(x)=\begin{cases}
	0 & 0\leq x<1,\\
	1 & x=1.
\end{cases}
\]
This limit function is not continuous. Hence the sequence cannot converge uniformly in $C[0,1]$.

Moreover, any subsequence $(f_{n_k})$ has the same pointwise limit, so no subsequence converges uniformly to a continuous function.
Thus $X$ is not sequentially compact.

Since compactness and sequential compactness are equivalent in metric spaces, $X$ is not compact.

Explicit open cover: For each $n\in\mathbb{N}$, define
\[
U_n=\{f\in X : f(1) > 1 - \tfrac{1}{n}\}.
\]
Also let
\[
V=\{f\in X : f(1)<1\}.
\]
Then $\{V\}\cup\{U_n: n\in\mathbb{N}\}$ is an open cover of $X$.

The constant function $f(x)=1$ belongs only to the sets $U_n$, and to cover it one needs infinitely many such $U_n$. Hence there is no finite subcover.

Therefore $X$ is not compact.
```

## CP-II-0017

- chapter line: 94

```tex
\label{prob:cp-ii-0017}
\par\noindent\textbullet\quad On $C([0,1])$,
	$\|h\|_{L^1}\le \|h\|_{L^2}\le \|h\|_{L^\infty}$ on a set of measure $1$.
	The same argument shows any two of these norm limits must coincide.

The phenomenon of having \emph{two different limits} under two norms does not rely on the supremum
norm itself. It arises whenever we choose two \emph{non-equivalent} and \emph{non-comparable} norms
on the same vector space, so that the identity map between the two normed spaces is not continuous.

\medskip
\noindent\textbf{Example beyond supremum norms.}
Consider the vector space $\mathcal{P}$ of real polynomials on $[0,1]$.
Define two different weighted $L^2$ norms:
\[
\|p\|_{2,w_1}=\Big(\int_0^{1/2}|p(t)|^2\,dt\Big)^{1/2},
\qquad
\|p\|_{2,w_2}=\Big(\int_{1/2}^{1}|p(t)|^2\,dt\Big)^{1/2}.
\]
Let $f\in C([0,1])$ satisfy $f|_{[0,1/2]}=0$ and $f|_{[1/2,1]}=1$,
and choose polynomials $p_n\to f$ uniformly (by the Weierstrass theorem).
Then
\[
\|p_n\|_{2,w_1}\to 0,
\qquad
\|p_n-1\|_{2,w_2}\to 0.
\]
Hence the same sequence $(p_n)$ converges to $0$ under $\|\cdot\|_{2,w_1}$
and to $1$ under $\|\cdot\|_{2,w_2}$,
even though neither of these norms is a supremum norm.

\medskip
\noindent\textbf{What is special about the standard norms.}
On standard spaces such as $\ell^p$ or $C([0,1])$ with the usual $L^1,L^2,L^\infty$ norms, we have
\[
\|h\|_{1}\le\|h\|_{2}\le\|h\|_{\infty}.
\]
These norms are \emph{comparable and compatible}, so convergence in any two of them
forces convergence to the \emph{same} limit.
Therefore, different limits can occur only when the norms are \emph{not equivalent}
and not ordered by inequality, not because the supremum norm is involved.
```

## CP-II-0021

- chapter line: 137

```tex
\label{prob:cp-ii-0021}
\par\noindent\textbullet\quad \textbf{Uniformly continuous:} yes. $f(x)=d(x,\{n^2\})$ is a distance to a closed set,
	hence $|f(x)-f(y)|\le|x-y|$ (1-Lipschitz).
	\textbf{Unbounded:} at $x=\tfrac{n^2+(n+1)^2}{2}$ we have $f(x)=\tfrac{2n+1}{2}\to\infty$.
```

## CP-II-0022

- chapter line: 144

```tex
\label{prob:cp-ii-0022}
Closed sets in $C([0,1])$ under $\|\cdot\|_\infty$ vs.\ $\|\cdot\|_1$

Is the set $\{f: f(1/2)=0\}$ closed in the space $\big(C([0,1]),\|\cdot\|_\infty\big)$?
What about the set $\{f:\int_0^1 f=0\}$?
In each case, does the answer change if we replace the uniform norm with the norm $\|\cdot\|_1$?

In a normed space, the zero set of a continuous linear functional is closed.
For $C([0,1])$,
the evaluation functional $E_{x_0}(f)=f(x_0)$ is continuous under $\|\cdot\|_\infty$ (since $|f(x_0)|\le\|f\|_\infty$),
but not under $\|\cdot\|_1$.
The integral functional $I(f)=\int_0^1 f$ is continuous under both norms, because
$|I(f)|\le\int_0^1 |f|\le \|f\|_\infty$ and also $|I(f)|\le \|f\|_1$.

	\par\noindent \textbf{A.}\quad $A=\{f\in C([0,1]): f(1/2)=0\}$.

		\par\noindent\textbullet\quad Under $\|\cdot\|_\infty$: $A=E_{1/2}^{-1}(\{0\})$ with $E_{1/2}$ continuous, hence $A$ is closed.
		\par\noindent\textbullet\quad Under $\|\cdot\|_1$: $A$ is not closed. Define $g\equiv 1$. For $n\ge 2$ let $f_n$ equal $1$ outside $[1/2-1/n,\,1/2+1/n]$, and on this interval let $f_n$ be the linear tent with $f_n(1/2)=0$ and $f_n(1/2\pm 1/n)=1$. Then $f_n\in A$ and
		$\|f_n-g\|_1$ equals the area of the tent, $\frac12\cdot \frac{2}{n}\cdot 1=\frac1n\to 0$, so $f_n\to g$ in $\|\cdot\|_1$ while $g\notin A$.

	\par\noindent \textbf{B.}\quad $B=\{f\in C([0,1]): \int_0^1 f=0\}$.

		\par\noindent\textbullet\quad Under $\|\cdot\|_\infty$: $B=I^{-1}(\{0\})$ with $I$ continuous since $|\int_0^1 f|\le \|f\|_\infty$, hence $B$ is closed.
		\par\noindent\textbullet\quad Under $\|\cdot\|_1$: likewise $|\int_0^1 f|\le \|f\|_1$, so $I$ is continuous and $B$ is closed.

\[
\begin{array}{c|c|c}
	\text{Set} & (C([0,1]),\|\cdot\|_\infty) & (C([0,1]),\|\cdot\|_1)\\ \hline
	\{f: f(1/2)=0\} & \text{closed} & \text{not closed}\\
	\{f: \int_0^1 f=0\} & \text{closed} & \text{closed}
\end{array}
\]
```

## CP-II-0028

- chapter line: 179

```tex
\label{prob:cp-ii-0028}
\par\noindent\textbullet\quad \textbf{Not complete in $\|\cdot\|_{1}$.}
	Let $h=\mathbf{1}_{[0,1/2]}$ (discontinuous). Choose $h_k\in C([0,1])$ that converge to $h$ in $L^{1}$,
	e.g.\ smooth ramps replacing the jump over width $1/k$. Then $\|h_k-h\|_{1}\to 0$, so $(h_k)$ is Cauchy in
	$\|\cdot\|_{1}$ but its limit is not continuous. Thus $\big(C([0,1]),\|\cdot\|_{1}\big)$ is not complete.
```

## CP-II-0029

- chapter line: 187

```tex
\label{prob:cp-ii-0029}
Suppose $f \in L^p_{\mathrm{loc}}(\mathbb{R}^n)$ is a periodic function.
Fix $\varepsilon>0$, and define
\[
Q = \{x\in\mathbb{R}^n : |x_j| < 1,\ j=1,\dots,n\},
\qquad
q = \{x\in\mathbb{R}^n : |x_j| < \tfrac12,\ j=1,\dots,n\}.
\]

Show that there exists $h_\varepsilon \in C^\infty(\mathbb{R}^n)$ with
$\operatorname{supp} h_\varepsilon \subset Q$ such that
\[
\|f\,\mathbf{1}_q - h_\varepsilon\|_{L^p(\mathbb{R}^n)} < \varepsilon.
\]
Define
\[
f_\varepsilon = \sum_{g\in\mathbb{Z}^n} \tau_g h_\varepsilon.
\]

Show that $f_\varepsilon$ is smooth and periodic.

Show that there exists a constant $c_n$, depending only on $n$, such that
\[
\|f - f_\varepsilon\|_{L^p(q)} < c_n\,\varepsilon.
\]

Let $f\in L^p_{\mathrm{loc}}(\mathbb{R}^n)$ be a periodic function with
period lattice $\mathbb{Z}^n$.  It is natural to think of $f$ as a
function on the torus $\mathbb{T}^n=\mathbb{R}^n/\mathbb{Z}^n$.  The
goal of Exercise~5.4 is to approximate $f$ in $L^p$ on a fundamental
domain by smooth periodic functions.

We work with the cubes
\[
Q = \{x\in\mathbb{R}^n : |x_j|<1,\ j=1,\dots,n\},
\qquad
q = \{x\in\mathbb{R}^n : |x_j|<\tfrac12,\ j=1,\dots,n\}.
\]
A standard fact in $L^p$--theory is that $C_c^\infty(\mathbb{R}^n)$ is
dense in $L^p(\mathbb{R}^n)$ for $1\le p<\infty$.  In particular, any
$L^p$-function supported in a bounded set can be approximated in $L^p$
by smooth compactly supported functions with support in a slightly
larger set.  Applying this to $f\mathbf{1}_q$ gives, for each
$\varepsilon>0$, the existence of $h_\varepsilon\in C^\infty(\mathbb{R}^n)$
with $\operatorname{supp}h_\varepsilon\subset Q$ and
$\|f\mathbf{1}_q-h_\varepsilon\|_{L^p(\mathbb{R}^n)}<\varepsilon$.

The function
\[
f_\varepsilon(x) := \sum_{g\in\mathbb{Z}^n} h_\varepsilon(x-g)
\]
is then well-defined, because at each $x$ only finitely many translates
$x-g$ lie in $Q$ and contribute to the sum.  Being locally a finite sum
of smooth functions, $f_\varepsilon$ is smooth.  Moreover,
$f_\varepsilon$ is $\mathbb{Z}^n$--periodic, since for any $k\in\mathbb{Z}^n$
\[
f_\varepsilon(x+k)
= \sum_{g\in\mathbb{Z}^n} h_\varepsilon(x+k-g)
= \sum_{h\in\mathbb{Z}^n} h_\varepsilon(x-h)
= f_\varepsilon(x),
\]
after the change of variables $h=g-k$.

To control $\|f-f_\varepsilon\|_{L^p(q)}$ one uses the periodicity of $f$
and the fact that $h_\varepsilon$ approximates $f\mathbf{1}_q$ on each
translate $q+g$ in the same way.  Since at most a bounded number of
translates of $Q$ overlap a given point (a constant depending only on
$n$), the total error on $q$ is controlled by a finite multiple of the
error $\|f\mathbf{1}_q-h_\varepsilon\|_{L^p}$.  This yields a bound
$\|f - f_\varepsilon\|_{L^p(q)} \le c_n\varepsilon$, where $c_n>0$
depends only on the dimension.
```

## CP-II-0035

- chapter line: 300

```tex
\label{prob:cp-ii-0035}
In higher dimensions, let $f(x,y)=\tfrac{1}{1+x^2+y^2}$ on the closed disk
		$E=\{(x,y):x^2+y^2\leq 10\}$.
		The domain is compact and $f$ is continuous, so $f$ is uniformly continuous.
```

## CP-II-0052

- chapter line: 307

```tex
\label{prob:cp-ii-0052}
(exact).

Let $f:[a,b]\to\mathbb{R}$ be bounded. Recall that Lebesgue's theorem says that $f$ is Riemann integrable on $[a,b]$ if and only if the set $D_f$ of points in $[a,b]$ where $f$ is discontinuous has Lebesgue measure zero. (By definition, a set $D\subset\mathbb{R}$ has Lebesgue measure zero if for every $\varepsilon>0$, there is a countable collection of open intervals $I_j=(a_j,b_j)$ such that $D\subset\bigcup_{j=1}^\infty I_j$ and $\sum_{j=1}^\infty |I_j|<\varepsilon$, where $|I_j|=b_j-a_j$.) As an optional exercise, prove this theorem by completing the outline below. We shall use the notation as in lectures, so $U(P,f),L(P,f)$ denote the upper and lower sums for $f$ relative to a partition $P$ of $[a,b]$.

	\par\noindent\textbullet\quad Show that $y\in D_f\cap(a,b)$ (i.e.\ $y$ is an interior discontinuity) if and only if there exists $\varepsilon=\varepsilon_y>0$ such that $\sup_I f-\inf_I f>\varepsilon$ for every open interval $I\subset (a,b)$ with $y\in I$. Hence $D_f\cap(a,b)=\bigcup_{j=1}^\infty E_j$, where $E_j=\{y\in(a,b):\ \sup_I f-\inf_I f>j^{-1}\ \text{for every open interval }I\text{ with }y\in I\}$.
	\par\noindent\textbullet\quad Suppose that $f$ is Riemann integrable. It suffices to show that $E_j$ has Lebesgue measure zero for each $j$ (Why?). Fix $j$, let $\varepsilon>0$ and choose a partition $P=\{a=a_0<a_1<\cdots<a_n=b\}$ such that $U(P,f)-L(P,f)<j^{-1}\varepsilon$. Let $K=\{k:\ E_j\cap(a_k,a_{k+1})\neq\emptyset\}$. Then $E_j\setminus\{a_0,a_1,\dots,a_n\}\subset\bigcup_{k\in K}(a_k,a_{k+1})$. Show that $\sum_{k\in K}(a_{k+1}-a_k)<\varepsilon$. Deduce that $E_j$ has Lebesgue measure zero.
	\par\noindent\textbullet\quad Now suppose that $D_f$ has Lebesgue measure zero. Let $\varepsilon>0$, and choose open intervals $I_j\subset\mathbb{R}$, $j=1,2,\dots$, with $D_f\subset\bigcup_{j=1}^\infty I_j$ and $\sum_{j=1}^\infty |I_j|<\varepsilon$. Let $F=[a,b]\setminus\bigcup_{j=1}^\infty I_j$. Show that there exists $\delta>0$ such that the following holds: $x\in F,\ y\in F,\ |x-y|<\delta \Rightarrow |f(x)-f(y)|<\varepsilon$. [This is a strengthening of the theorem we proved in lecture that says that a continuous function on a closed, bounded interval (or more generally on a compact metric space) is uniformly continuous, but the same contradiction argument we used in fact works here.] Let $P=\{a=a_0<a_1<\cdots<a_n=b\}$ be any partition of $[a,b]$ such that $a_{j+1}-a_j<\delta$, and let $J=\{j:\ [a_j,a_{j+1}]\cap F\neq\emptyset\}$. Show that $\sup_{[a_j,a_{j+1}]} f-\inf_{[a_j,a_{j+1}]} f<2\varepsilon$ for each $j\in J$, and that $\bigcup_{j\notin J}(a_j,a_{j+1})\subset\bigcup_{j=1}^\infty I_j$. Conclude that $U(P,f)-L(P,f)<2(b-a+\sup_{[a,b]}|f|)\varepsilon$, and hence that $f$ is Riemann integrable on $[a,b]$.

 \mbox{}\par

For a partition $P=\{a=a_0<\cdots<a_n=b\}$ and bounded $f$,
\begin{center}
\resizebox{\linewidth}{!}{$\displaystyle
U(P,f)=\sum_{k=0}^{n-1} M_k\,(a_{k+1}-a_k),\qquad
M_k=\sup_{[a_k,a_{k+1}]} f,\qquad
L(P,f)=\sum_{k=0}^{n-1} m_k\,(a_{k+1}-a_k),\qquad
m_k=\inf_{[a_k,a_{k+1}]} f.
$}
\end{center}
Let the \emph{oscillation} on an interval $I$ be $\omega(f;I)=\sup_I f-\inf_I f$.
Then
\[
U(P,f)-L(P,f)=\sum_{k=0}^{n-1} \omega\!\big(f;[a_k,a_{k+1}]\big)\,(a_{k+1}-a_k).
\]
A bounded $f$ is Riemann integrable iff $\forall \eta>0$ there exists $P$ with $U(P,f)-L(P,f)<\eta$.

 \mbox{}\par

The \emph{oscillation at a point} $x$ is
\[
\omega(f;x)=\inf_{\delta>0}\ \sup\{|f(u)-f(v)|:\ u,v\in (x-\delta,x+\delta)\cap[a,b]\}.
\]
Then $f$ is continuous at $x$ iff $\omega(f;x)=0$.
Equivalently: $x\in D_f$ iff $\exists\,\varepsilon>0$ such that $\omega(f;I)>\varepsilon$
for every interval $I\ni x$.
Define
\[
E_j=\Big\{x\in(a,b):\ \omega(f;I)>\tfrac{1}{j}\ \text{for every open }I\ni x\Big\}.
\]
Then $D_f\cap(a,b)=\bigcup_{j=1}^\infty E_j$.

 \mbox{}\par

A set $N\subset\mathbb{R}$ has Lebesgue measure zero iff
for every $\varepsilon>0$ there exist open intervals $I_j$ with
$N\subset \bigcup_{j=1}^\infty I_j$ and $\sum_{j=1}^\infty |I_j|<\varepsilon$.
If $E\subset \bigcup_{k\in K}(a_k,a_{k+1})$, then
\[
\lambda(E)\le \sum_{k\in K}(a_{k+1}-a_k).
\]

 \mbox{}\par
If $F\subset [a,b]$ is closed, then $F$ is compact.
If $f$ is continuous at each point of $F$, then $f|_F$ is continuous $F\to\mathbb{R}$,
hence (Heine--Cantor) uniformly continuous on $F$:
\[
\forall \varepsilon>0\ \exists\,\delta>0\ \forall x,y\in F\quad
|x-y|<\delta \ \Longrightarrow\ |f(x)-f(y)|<\varepsilon.
\]

  \mbox{}\par
For $y\in(a,b)$ define the oscillation
\[
\omega(f;y):=\inf_{\delta>0}\Big(\sup_{(y-\delta,y+\delta)\cap[a,b]} f
-\inf_{(y-\delta,y+\delta)\cap[a,b]} f\Big).
\]
It is standard that $f$ is continuous at $y$ iff $\omega(f;y)=0$.

\emph{($\Rightarrow$)} Suppose $y\in D_f\cap(a,b)$. If no $\varepsilon_y>0$ satisfied
$\sup_I f-\inf_I f>\varepsilon_y$ for every open interval $I\ni y$, then for each $m\in\mathbb N$
we could choose an interval $I_m\ni y$ with $\sup_{I_m} f-\inf_{I_m} f\le 1/m$. Taking $I_m=(y-\delta_m,y+\delta_m)$ with $\delta_m\downarrow 0$ gives $\omega(f;y)\le 1/m$ for all $m$, hence $\omega(f;y)=0$, a contradiction. Thus there exists $\varepsilon_y>0$ such that
$\sup_I f-\inf_I f>\varepsilon_y$ for every open interval $I\ni y$.

\emph{($\Leftarrow$)} Conversely, if there exists $\varepsilon_y>0$ with
$\sup_I f-\inf_I f>\varepsilon_y$ for every open interval $I\ni y$, then for all $\delta>0$,
\[
\sup_{(y-\delta,y+\delta)} f-\inf_{(y-\delta,y+\delta)} f\ge \varepsilon_y,
\]
so $\omega(f;y)\ge \varepsilon_y>0$ and hence $f$ is discontinuous at $y$.

Consequently,
\[
D_f\cap(a,b)=\bigcup_{j=1}^\infty E_j,
\qquad
E_j:=\Big\{y\in(a,b):\ \sup_I f-\inf_I f>\tfrac1j \ \text{for every open interval } I\ni y\Big\}.
\]
Indeed, $y\in D_f\cap(a,b)$ iff $\omega(f;y)>0$, i.e.\ iff $1/j<\omega(f;y)$ for some $j$,
which is equivalent to $y\in E_j$ for some $j$.

  \mbox{}\par
Fix $j\in\mathbb N$ and $\varepsilon>0$. Take a partition
$P=\{a=a_0<\cdots<a_n=b\}$ with $U(P,f)-L(P,f)<\varepsilon/j$.
Let $K=\{k:\ E_j\cap(a_k,a_{k+1})\neq\emptyset\}$.
For $k\in K$, pick $y_k\in E_j\cap(a_k,a_{k+1})$; then with $I=(a_k,a_{k+1})$,
\[
\sup_I f-\inf_I f>\tfrac1j,
\]
hence $M_k-m_k\ge\tfrac1j$. Therefore
\[
\sum_{k\in K}(a_{k+1}-a_k)
\le j\sum_{k\in K}(M_k-m_k)(a_{k+1}-a_k)
\le j\big(U(P,f)-L(P,f)\big)<\varepsilon.
\]
Thus $E_j\setminus\{a_0,\dots,a_n\}$ is covered by $\bigcup_{k\in K}(a_k,a_{k+1})$ of
total length $<\varepsilon$, so $E_j$ has measure zero.

 \mbox{}\par
Let $\varepsilon>0$ and choose open intervals $I_\ell$ with
$D_f\subset\bigcup_\ell I_\ell$ and $\sum_\ell |I_\ell|<\varepsilon$.
Put $F=[a,b]\setminus\bigcup_\ell I_\ell$.
Then $F$ is compact and $f|_F$ is uniformly continuous:
$\exists\delta>0$ such that $x,y\in F$, $|x-y|<\delta\Rightarrow |f(x)-f(y)|<\varepsilon$.

Refine a partition $P=\{a=a_0<\cdots<a_n=b\}$ so that
(i) $a_{k+1}-a_k<\delta$ for all $k$, and
(ii) every endpoint of every $I_\ell$ is a partition point.
Let $J=\{k:\ [a_k,a_{k+1}]\subset F\}$.
For $k\in J$,
\[
\sup_{[a_k,a_{k+1}]} f - \inf_{[a_k,a_{k+1}]} f < \varepsilon.
\]
For $k\notin J$ we have $[a_k,a_{k+1}]\subset I_\ell$ for some $\ell$, hence
$\sum_{k\notin J}(a_{k+1}-a_k)\le \sum_\ell |I_\ell|<\varepsilon$.
Let $M=\sup_{[a,b]}|f|$. Then
\[
\begin{aligned}
	U(P,f)-L(P,f)
	&=\sum_{k=0}^{n-1}\big(\sup_{[a_k,a_{k+1}]} f-\inf_{[a_k,a_{k+1}]} f\big)\,(a_{k+1}-a_k)\\
	&< \varepsilon\sum_{k\in J}(a_{k+1}-a_k)+2M\sum_{k\notin J}(a_{k+1}-a_k)\\
	&\le \varepsilon(b-a)+2M\,\varepsilon.
\end{aligned}
\]
Since $\varepsilon>0$ is arbitrary, $U(P,f)-L(P,f)$ can be made arbitrarily small; hence
$f$ is Riemann integrable on $[a,b]$.
```

## CP-II-0062

- chapter line: 445

```tex
\label{prob:cp-ii-0062}
\par\noindent\textbullet\quad Compactly supported mollifiers $\phi_\varepsilon$ live in
	$\mathcal{D}(\mathbb{R}^n)$ and are suitable for regularizing
	arbitrary distributions in $\mathcal{D}'(\mathbb{R}^n)$ (at least
	away from the boundary in a domain).
```

## CP-II-0072

- chapter line: 521

```tex
\label{prob:cp-ii-0072}
\par\noindent\textbullet\quad $f\in L^\infty$ with compact support (e.g.\ $(1+x^2)^{-1}\mathbf 1_{[-5,5]}$):
	the same argument applies since $f\in L^1$.

\bigskip\hrule\bigskip
```

## CP-II-0082

- chapter line: 624

```tex
\label{prob:cp-ii-0082}
Let $f(x) = x^2$ on $E=[-5,5]$.
		Polynomials are continuous, and since $E$ is compact, $f$ is uniformly continuous.
```

## CP-II-0090

- chapter line: 1001

```tex
\label{prob:cp-ii-0090}
\par\noindent\textbullet\quad Suppose $f \in H^{s}(\mathbb{R}^n)$ has compact support.
	Show that there exists a sequence $\varphi_j \in C_0^\infty(\mathbb{R}^n)$ such that
	\[
	\varphi_j \longrightarrow f \quad\text{in } H^{s}(\mathbb{R}^n).
	\]
```

## CP-II-0092

- chapter line: 1010

```tex
\label{prob:cp-ii-0092}
The line with two origins

Let
	\[
	X=\{(x,y)\in\mathbb{R}^2: y=\pm1\}
	\]
	with the subspace topology from $\mathbb{R}^2$, and define an equivalence relation on $X$ by
	\[
	(x,y)\sim(x',y') \iff x'=x\neq 0 \ \text{ and }\ y'=-y.
	\]
	Let $Q=X/\!\sim$ and $q:X\to Q$ be the quotient map. Denote
	\[
	o_+=q(0,1),\qquad o_-=q(0,-1).
	\]

	\subsection*{(a) Every point of $Q$ has a neighborhood homeomorphic to $\mathbb{R}$}

	Fix $a\neq0$ and choose $\varepsilon>0$ so that $(a-\varepsilon,a+\varepsilon)$ does not meet $0$.
	Then
	\[
	U = q\big((a-\varepsilon,a+\varepsilon)\times\{1\}\big)
	= q\big((a-\varepsilon,a+\varepsilon)\times\{-1\}\big)
	\]
	and the map $t\mapsto q(t,1)$ is a homeomorphism $(a-\varepsilon,a+\varepsilon)\xrightarrow{\cong} U$.

	For small $\varepsilon>0$, define
	\[
	\phi_+:(-\varepsilon,\varepsilon)\longrightarrow Q,\qquad
	\phi_+(t)=
	\begin{cases}
		q(t,1), & t\le 0,\\[2pt]
		q(t,-1), & t>0.
	\end{cases}
	\]
	Then $\phi_+$ is continuous, bijective onto $U_+=\phi_+((-\varepsilon,\varepsilon))$, and its inverse is continuous (it pulls back opens to unions of opens in the two lines). Hence $U_+\cong\mathbb{R}$.

	Define
	\[
	\phi_-:(-\varepsilon,\varepsilon)\to Q,\qquad
	\phi_-(t)=
	\begin{cases}
		q(t,-1), & t\le 0,\\[2pt]
		q(t,1),  & t>0.
	\end{cases}
	\]
	Then $U_-=\phi_-((-\varepsilon,\varepsilon))$ is a neighborhood of $o_-$ homeomorphic to $\mathbb{R}$.

	Thus each point of $Q$ has a neighborhood homeomorphic to $\mathbb{R}$.

	Let $U\ni o_+$ and $V\ni o_-$ be arbitrary open neighborhoods. By the constructions above,
	for all sufficiently small $t>0$ we have $q(t,1)=q(t,-1)\in U$ and also $q(t,1)=q(t,-1)\in V$.
	Hence $U\cap V\neq\varnothing$, so $o_+$ and $o_-$ cannot be separated by disjoint open sets.
	Therefore $Q$ is not Hausdorff.

	$Q$ is the classical ``line with two origins'': it is locally homeomorphic to $\mathbb{R}$, but it fails to be Hausdorff.

		\par\noindent \textbf{(10)}\quad $X=[0,1]\cup[2,3]$ with $1\sim2$.

			\par\noindent\textbullet\quad Classes: $\{x\}$ for every $x\in X\setminus\{1,2\}$, and the special class $\{1,2\}$.

		\par\noindent \textbf{(11b)}\quad $X\times Y$ with $(x,y)\sim(x',y')\iff x=x'$ (assume $Y\neq\varnothing$).

			\par\noindent\textbullet\quad Classes: for each $x\in X$, the vertical fiber $\{x\}\times Y$.

		\par\noindent \textbf{(12)}\quad $\mathbb{R}^2$ with $(x,y)\sim(x',y')\iff (x-x',y-y')\in\mathbb{Z}^2$.

			\par\noindent\textbullet\quad Classes: lattice cosets $(x,y)+\mathbb{Z}^2=\{(x+m,y+n):m,n\in\mathbb{Z}\}$.
			\par\noindent\textbullet\quad Equivalently: one representative in $[0,1)\times[0,1)$, with opposite edges identified.

		\par\noindent \textbf{(13)}\quad $X=\{(x,y)\in\mathbb{R}^2:y=\pm1\}$ with $(x,y)\sim(x',y')\iff x=x'\neq0,\ y'=-y$.

			\par\noindent\textbullet\quad Classes: for $x\neq0$, the pair $\{(x,1),(x,-1)\}$; for $x=0$, the singletons $\{(0,1)\}$ and $\{(0,-1)\}$.
```

## CP-II-0100

- chapter line: 1086

```tex
\label{prob:cp-ii-0100}
— Global diffeomorphism under $\|Df - I\| \le \mu < 1$

\textbf{Statement.}\quad

Let $f:\mathbb{R}^n \to \mathbb{R}^n$ be $C^1$ and assume
\[
\|Df(x) - I\| \le \mu \quad \text{for some } \mu\in(0,1) \text{ and all } x.
\]
Show:
 \setlength{\itemsep}{6pt}
	\par\noindent\textbullet\quad $f$ maps open sets to open sets.
	\par\noindent\textbullet\quad For all $x,y$,
	\[
	(1-\mu)\,\|x-y\| \;\le\; \|f(x)-f(y)\| \;\le\; (1+\mu)\,\|x-y\|.
	\]
	Hence $f$ is injective and $f(\mathbb{R}^n)$ is closed.
	\par\noindent\textbullet\quad Conclude that $f$ is a diffeomorphism of $\mathbb{R}^n$.
	\par\noindent\textbullet\quad Explain why the conclusion can fail if one only assumes $\|Df(x)-I\|\le 1$.

\bigskip\hrule\bigskip

\textbf{Theory \& Solution.}\quad

\textbf{(Two–sided Lipschitz via line integration).}\;
Let $h:=y-x$ and $g(t):=f(x+th)$. Then
\[
f(y)-f(x)=\int_{0}^{1} Df(x+th)\,h\,dt
= h + \int_{0}^{1} (Df(x+th)-I)\,h\,dt.
\]
Hence
\[
\|f(y)-f(x)-h\|
\;\le\; \int_{0}^{1} \|Df(x+th)-I\|\,\|h\|\,dt
\;\le\; \mu\,\|h\|.
\]
By the triangle inequality,
\[
(1-\mu)\,\|h\|\ \le\ \|f(y)-f(x)\|\ \le\ (1+\mu)\,\|h\|.
\]
\emph{Injectivity} follows from the lower bound (if $f(x)=f(y)$ then $x=y$).

\medskip

\textbf{(Local diffeomorphism).}\;
Since $\|Df(x)-I\|<1$, each $Df(x)$ is invertible (Neumann series).
By the inverse function theorem, $f$ is a local $C^1$ diffeomorphism and therefore
\emph{maps open sets to open sets}.

\medskip

\textbf{(Closed range).}\;
If $f(x_k)\to y$ and $(x_k)$ is bounded, the lower Lipschitz bound gives
$\|x_k-x_\ell\|\le \tfrac{1}{1-\mu}\,\|f(x_k)-f(x_\ell)\|$, so $(x_k)$ is Cauchy
and converges to some $x$ with $f(x)=y$. Thus $f(\mathbb{R}^n)$ is closed.

\medskip

\textbf{(Surjectivity and global diffeo).}\;
The image $f(\mathbb{R}^n)$ is nonempty, open (local diffeo) and closed (previous step)
in the connected space $\mathbb{R}^n$, hence $f(\mathbb{R}^n)=\mathbb{R}^n$.
Thus $f$ is bijective; by the inverse function theorem $f^{-1}$ is $C^1$.
Therefore $f$ is a global $C^1$ \emph{diffeomorphism}.

\bigskip\hrule\bigskip

\textbf{Why not with Ă˘â‚¬Ĺ›$\le 1$Ă˘â‚¬ĹĄ only?}\quad

If $\|Df-I\|\le 1$, invertibility of $Df$ can fail somewhere.
In $n=1$, let $\phi$ be a $C^\infty$ bump with $0\le \phi \le 1$ and set
$f'(x)=1-\phi(x)$ so that $|f'(x)-1|\le 1$ but $f'(0)=0$.
Then $f$ is not locally invertible near $0$, and the two–sided Lipschitz bound can fail.

\bigskip\hrule\bigskip

\textbf{Examples.}\quad

 \setlength{\itemsep}{6pt}
	\par\noindent\textbullet\quad \emph{Scalar case:} $f(x)=x-\tanh x$ on $\mathbb{R}$.
	Then $f'(x)=1-\operatorname{sech}^2 x\in(0,1)$, so $\|Df-I\|=\sup_x|f'(x)-1|<1$.
	The bounds give $(1-\mu)|x-y|\le|f(x)-f(y)|\le(1+\mu)|x-y|$,
	and $f$ is a global $C^1$ diffeomorphism of $\mathbb{R}$.

	\par\noindent\textbullet\quad \emph{Vector case:} $f(x)=x+g(x)$ with $\|Dg(x)\|\le \mu<1$ (e.g.\ $g(x)=\varepsilon\sin x$ componentwise).
	Then $\|Df-I\|\le\mu$ and all conclusions apply; $f$ is bi-Lipschitz and globally invertible.
```

## CP-II-0122

- chapter line: 2304

```tex
\label{prob:cp-ii-0122}
— Extending a uniform polynomial limit from an annulus

Let $A=\{z: \tfrac12\le|z|\le1\}$ and $f:A\to\mathbb C$ be continuous, holomorphic on
$\{ \tfrac12<|z|<1\}$. If polynomials $p_n\to f$ uniformly on $A$, prove that there is
$g\in C(\{|z|\le1\})$, holomorphic on $|z|<1$, with $g=f$ on $A$.

Fix $\varepsilon>0$. From uniform convergence on $A$, choose $N$ so that
$\sup_{A}|p_n-p_m|<\varepsilon$ for $n,m\ge N$. By the maximum modulus principle on the annulus,
$\sup_{\tfrac12\le|z|\le1}|p_n-p_m|<\varepsilon$. On the disk $|z|\le\tfrac12$,
\[
\sup_{|z|\le\tfrac12}|p_n-p_m|
\le \sup_{|z|=\tfrac12}|p_n-p_m|<\varepsilon.
\]
Therefore $\sup_{|z|\le1}|p_n-p_m|<\varepsilon$, so $\{p_n\}$ is uniformly Cauchy on $|z|\le1$,
hence converges uniformly to some $g\in C(\{|z|\le1\})$, holomorphic on $|z|<1$.
Uniform convergence on $A$ gives $g=f$ on $A$.

\noindent\rule{\textwidth}{0.4pt}

A subset $J\subset \mathbb{R}^2$ is a \emph{Jordan curve} if there exists a continuous
injective map $\gamma:\mathbb{S}^1\to\mathbb{R}^2$ such that $J=\gamma(\mathbb{S}^1)$.
Equivalently, $J$ is a simple closed curve (continuous, no self-intersections).

A \emph{Jordan arc} is the image of a homeomorphism $\eta:[a,b]\to\mathbb{R}^2$.
A \emph{Jordan domain} is a bounded open set $D\subset\mathbb{R}^2$ whose boundary
$\partial D$ is a Jordan curve (typically oriented positively).

Every Jordan curve $J$ divides $\mathbb{R}^2$ into exactly two connected components,
an interior and an exterior, with $J$ as their common boundary.

\noindent\rule{\textwidth}{0.4pt}

Let $K\subset\mathbb{C}$ be compact with \textbf{connected complement} $\mathbb{C}\setminus K$.
If $f$ is continuous on $K$ and holomorphic in the interior $K^\circ$, then there exists
a sequence of \textbf{polynomials} $p_n$ with
\[
\sup_{z\in K} |f(z)-p_n(z)| \;\longrightarrow\; 0.
\]

	\par\noindent\textbullet\quad If $K^\circ=\varnothing$ (for example, $K$ is a Jordan curve or arc),
	the condition Ă˘â‚¬Ĺ›holomorphic in the interiorĂ˘â‚¬ĹĄ is vacuous; every continuous $f$ on $K$
	is uniformly approximable by polynomials.
	\par\noindent\textbullet\quad If $\mathbb{C}\setminus K$ is not connected (i.e., $K$ has holes),
	polynomials are in general \emph{not} dense, but \textbf{rational functions with poles outside $K$}
	are dense (Runge--Oka--Weil).

	\par\noindent\textbullet\quad \textbf{Runge--Oka--Weil (rational form).}
	For any compact $K$ and any finite set $E$ meeting every bounded component
	of $\mathbb{C}\setminus K$, functions holomorphic near $K$ can be uniformly approximated
	on $K$ by rational functions with all poles in $E$.
	\par\noindent\textbullet\quad \textbf{Mergelyan on Jordan domains.}
	If $K=\overline{\Omega}$ with $\Omega$ a bounded Jordan domain,
	then every $f\in A(\Omega)$ (continuous on $\overline{\Omega}$, holomorphic on $\Omega$)
	is a uniform limit of polynomials.
	\par\noindent\textbullet\quad \textbf{Maximum modulus transfer.}
	Uniform convergence on $K$ of polynomials implies uniform convergence
	on compact subsets of $K^\circ$ of their derivatives (by Cauchy estimates).

	\par\noindent\textbullet\quad On an \emph{annulus} $K=\{r\le |z|\le R\}$,
	the complement $\mathbb{C}\setminus K$ has two components,
	so polynomials are not generally dense; but rational functions with poles at $0$ (or $\infty$)
	are dense (Runge).
	\par\noindent\textbullet\quad If $f$ \emph{extends holomorphically across the holes},
	one can enlarge $K$ to a compact with connected complement and then apply Mergelyan.

	\par\noindent\textbullet\quad Consider the uniform algebra $P(K)$ (uniform closure of polynomials on $K$).
	\par\noindent\textbullet\quad If $\mathbb{C}\setminus K$ is connected, $K$ is \emph{polynomially convex};
	by deep results (Mergelyan 1951), any $f\in A(K)$ can be uniformly approximated in $P(K)$.
	\par\noindent\textbullet\quad Tools behind the proof include RungeĂ˘â‚¬â„˘s theorem, peak functions,
	and the theory of uniform algebras.

\noindent\rule{\textwidth}{0.4pt}

The theorem was proved by S.\ N.\ Mergelyan in 1951 and generalizes earlier
approximation results of Weierstrass (on intervals) and Runge (on rational approximation).
It represents the final step in characterizing all compact sets $K$ in $\mathbb{C}$
for which polynomials are dense in $A(K)$.
```

## CP-II-0127

- chapter line: 2385

```tex
\label{prob:cp-ii-0127}
$\mathcal{E}(\mathbb{R}^n) = C^\infty(\mathbb{R}^n)$ with seminorms
\[
p_{K,\beta}(f) = \sup_{x \in K} |\partial^\beta f(x)|, \qquad K \Subset \mathbb{R}^n.
\]
$\mathcal{S}(\mathbb{R}^n)$ with seminorms
\[
q_{\alpha,\beta}(f) = \sup_{x \in \mathbb{R}^n} |x^\alpha \partial^\beta f(x)|.
\]
$\mathcal{D}(\mathbb{R}^n) = C_c^\infty(\mathbb{R}^n)$ with the LF topology:
a sequence $f_j \to 0$ in $\mathcal{D}$ if and only if there exists a compact set
$K \Subset \mathbb{R}^n$ such that $\operatorname{supp} f_j \subset K$ for all sufficiently large $j$,
and
\[
\sup_{x \in K} |\partial^\beta f_j(x)| \to 0
\quad \text{for every multiindex } \beta.
\]

If $f\in\mathcal S$, then for each $\beta$, $q_{0,\beta}(f)=\sup_{\mathbb R^n}|\partial^\beta f|<\infty$, hence $f\in C^\infty(\mathbb R^n)=\mathcal E$.
Linearity of $\mathcal S$ follows from linearity of the seminorms.
If $f_j\to0$ in $\mathcal S$, then for any compact $K$ and any $\beta$,
\[
p_{K,\beta}(f_j)=\sup_{x\in K}|\partial^\beta f_j(x)|\le \sup_{x\in\mathbb R^n}|\partial^\beta f_j(x)|
=q_{0,\beta}(f_j)\xrightarrow[j\to\infty]{}0,
\]
so $f_j\to0$ in $\mathcal E$.

If $f\in C_c^\infty$ with $\mathrm{supp}\,f\subset K$, then for any $\alpha,\beta$,
\[
q_{\alpha,\beta}(f)=\sup_{x\in K}|x^\alpha\partial^\beta f(x)|
\le \Big(\sup_{x\in K}|x^\alpha|\Big)\cdot \sup_{x\in K}|\partial^\beta f(x)|<\infty,
\]
hence $f\in\mathcal S$. Linearity is obvious.
If $f_j\to0$ in $\mathcal D$, choose a compact $K$ containing $\mathrm{supp}\,f_j$ for large $j$;
then
\[
q_{\alpha,\beta}(f_j)=\sup_{x\in\mathbb R^n}|x^\alpha\partial^\beta f_j(x)|
=\sup_{x\in K}|x^\alpha\partial^\beta f_j(x)|
\le \Big(\sup_{x\in K}|x^\alpha|\Big)\cdot \sup_{x\in K}|\partial^\beta f_j(x)|\xrightarrow[j\to\infty]{}0,
\]
so $f_j\to0$ in $\mathcal S$.

Fix $\psi\in C_c^\infty(\mathbb R^n)$, $\psi\not\equiv0$, with $\mathrm{supp}\,\psi\subset B(0,1)$.
Let $e_1=(1,0,\dots,0)$ and define
\[
\phi_j(x):=e^{-j^2}\,\psi(x-je_1).
\]
For any $\alpha,\beta$ there is $C_\beta$ with
$\sup_x |x^\alpha \partial^\beta \phi_j(x)| \le C_\beta e^{-j^2}(1+j)^{|\alpha|}\to0$; thus $\phi_j\to0$ in $\mathcal S$.
However $\mathrm{supp}\,\phi_j\subset B(je_1,1)$ escapes to infinity, so no compact $K$ contains the supports eventually; therefore $\phi_j$ does not converge to $0$ in $\mathcal D$.

With the same $\psi$, set
\[
\phi_j(x):=\psi(x-je_1).
\]
For any fixed compact $K$, $K\cap\mathrm{supp}\,\phi_j=\varnothing$ for $j$ large, hence for every $\beta$,
$\sup_{x\in K}|\partial^\beta \phi_j(x)|=0$. Thus $\phi_j\to0$ in $\mathcal E$.
On the other hand, for $\alpha\neq0$ and $\beta=0$,
\[
q_{\alpha,0}(\phi_j)\ge \sup_{|y|\le 1}|(je_1+y)^\alpha|\,|\psi(y)| \gtrsim j^{|\alpha|}\to\infty,
\]
so $\phi_j$ has no limit in $\mathcal S$.

A smooth function $f:\mathbb{R}^n\to\mathbb{C}$ is called \emph{rapidly decreasing} if for every pair of multiindices $\alpha,\beta$ one has
\[
\sup_{x\in\mathbb{R}^n}\big|\,x^\alpha\,\partial^\beta f(x)\,\big|<\infty
\quad\text{and}\quad
\lim_{|x|\to\infty}\big|\,x^\alpha\,\partial^\beta f(x)\,\big|=0.
\]
Equivalently, for each $N\in\mathbb{N}$ and each $\beta$ there exists $C_{N,\beta}$ such that
\[
|\partial^\beta f(x)|\le C_{N,\beta}\,(1+|x|)^{-N}\qquad(\forall x\in\mathbb{R}^n).
\]

The Schwartz space $\mathcal{S}(\mathbb{R}^n)$ consists of all rapidly decreasing $C^\infty$ functions and is a Fr\'echet space with seminorms
\[
q_{\alpha,\beta}(f):=\sup_{x\in\mathbb{R}^n}\big|x^\alpha\,\partial^\beta f(x)\big|,\qquad \alpha,\beta\in\mathbb{N}^n.
\]
The Fourier transform is a topological automorphism of $\mathcal{S}(\mathbb{R}^n)$.

A Fr\'echet space is a complete metrizable locally convex space; equivalently, its topology is induced by a countable family of seminorms $(p_k)_{k\in\mathbb{N}}$, and it is complete for the metric
\[
d(x,y)=\sum_{k=1}^\infty 2^{-k}\,\frac{p_k(x-y)}{1+p_k(x-y)}.
\]
The spaces $\mathcal{E}(\mathbb{R}^n)=C^\infty(\mathbb{R}^n)$ and $\mathcal{S}(\mathbb{R}^n)$ are Fr\'echet with the standard seminorm families
\[
\mathcal{E}:\; p_{K,\beta}(f)=\sup_{x\in K}|\partial^\beta f(x)| \quad (K\Subset\mathbb{R}^n),
\qquad
\mathcal{S}:\; q_{\alpha,\beta}(f)=\sup_{x\in\mathbb{R}^n}|x^\alpha\partial^\beta f(x)|.
\]

The Gaussian $x\mapsto e^{-|x|^2}$ and any compactly supported $C^\infty$ function belong to $\mathcal{S}(\mathbb{R}^n)$.
Functions like $(1+|x|)^{-1}$ or $\sin|x|$ do not: the former decays too slowly, the latter does not decay.

For $k\in\mathbb{N}$ and $1\le p\le\infty$ the Sobolev space is
\[
W^{k,p}(\mathbb{R}^n)=\big\{f\in L^p(\mathbb{R}^n): \partial^\alpha f\in L^p \ \text{for all }|\alpha|\le k\big\},
\qquad
\|f\|_{W^{k,p}}=\sum_{|\alpha|\le k}\|\partial^\alpha f\|_{L^p}.
\]

For $p=2$ and $s\in\mathbb{R}$ one defines the Bessel potential spaces
\[
H^s(\mathbb{R}^n)=\left\{f\in\mathcal{S}'(\mathbb{R}^n):\ (1+|\xi|^2)^{s/2}\,\widehat{f}(\xi)\in L^2(\mathbb{R}^n)\right\},
\qquad
\|f\|_{H^s}^2=\int_{\mathbb{R}^n}(1+|\xi|^2)^s\,|\widehat{f}(\xi)|^2\,d\xi.
\]

One has $\mathcal{S}(\mathbb{R}^n)\subset H^s(\mathbb{R}^n)\subset \mathcal{S}'(\mathbb{R}^n)$ for all $s\in\mathbb{R}$,
and $\mathcal{S}(\mathbb{R}^n)$ is dense in $W^{k,p}(\mathbb{R}^n)$ for $1\le p<\infty$.
The dual $\mathcal{S}'(\mathbb{R}^n)$ is the space of tempered distributions.

\subsection*{The LF topology on $\mathcal{D}(\mathbb{R}^n)$}

For a compact set $K\Subset\mathbb{R}^n$ define
\[
\mathcal{D}(K)=\{\,f\in C^\infty(\mathbb{R}^n):\ \operatorname{supp}f\subset K\,\},
\qquad
\|f\|_{K,m}:=\max_{|\beta|\le m}\ \sup_{x\in K}|\partial^\beta f(x)|\quad(m\in\mathbb N).
\]
Each $\mathcal{D}(K)$ is a Fr\'echet space with the seminorms $\|\cdot\|_{K,m}$.
Fix an exhaustion by compacts $K_1\Subset K_2\Subset\cdots$ with $\bigcup_{m\ge1}K_m=\mathbb{R}^n$; then
\[
\mathcal{D}(\mathbb{R}^n)=\bigcup_{m\ge1}\mathcal{D}(K_m)
\]
endowed with the finest locally convex topology making the inclusions $\mathcal{D}(K_m)\hookrightarrow\mathcal{D}(\mathbb{R}^n)$ continuous.
This locally convex space is the strict inductive limit (LF space) of the Fr\'echet spaces $\mathcal{D}(K_m)$.

A sequence $f_j$ converges to $0$ in $\mathcal{D}(\mathbb{R}^n)$ if and only if there exists a compact $K\Subset\mathbb{R}^n$ such that $\operatorname{supp}f_j\subset K$ for all sufficiently large $j$, and for every multiindex $\beta$ one has
\[
\sup_{x\in K}|\partial^\beta f_j(x)|\ \xrightarrow[j\to\infty]{}\ 0.
\]
Equivalently, all derivatives of $f_j$ tend to $0$ uniformly on a fixed compact set that eventually contains the supports.

The space $\mathcal{D}(\mathbb{R}^n)$ is complete, nuclear and Montel; it is neither normable nor metrizable when $\mathbb{R}^n$ is non-compact.
One has the continuous dense embeddings $\mathcal{D}(\mathbb{R}^n)\subset \mathcal{S}(\mathbb{R}^n)\subset \mathcal{E}(\mathbb{R}^n)$, and $\mathcal{D}(\mathbb{R}^n)$ is dense in both $\mathcal{S}(\mathbb{R}^n)$ and $\mathcal{E}(\mathbb{R}^n)$.
For density in $\mathcal{E}$ on $\mathbb{R}^n$, given $f\in C^\infty$ and a compact $K$, choose $\chi_R\in C_c^\infty$ with $\chi_R\equiv1$ on $K$ and $\operatorname{supp}\chi_R\subset B(0,R)$; then $\chi_R f\in \mathcal{D}$ and for each multiindex $\beta$,
\[
\sup_{x\in K}|\partial^\beta(\chi_R f - f)(x)|=0\quad \text{for $R$ sufficiently large,}
\]
so $\chi_R f\to f$ in $\mathcal{E}$.
For density in $\mathcal{S}$ one first cut off $f$ at infinity and then mollify to achieve rapid decay of all derivatives.
```

## CP-II-0131

- chapter line: 2557

```tex
\label{prob:cp-ii-0131}
(exact).

	\par\noindent\textbullet\quad Show that $\|f\|_{1}=\int_{0}^{1}|f|$ defines a norm on the vector space $C([0,1])$.
	Is it Lipschitz equivalent to the uniform norm? Is $C([0,1])$ with norm $\|\cdot\|_{1}$ complete?

	\par\noindent\textbullet\quad Let $R([0,1])$ denote the vector space of all bounded Riemann integrable functions on $[0,1]$.
	Does $\|f\|_{1}=\int_{0}^{1}|f|$ define a norm on $R([0,1])$? If so, is $R([0,1])$ complete with this norm?
	What if we replace $\|\cdot\|_{1}$ with $\|f\|_{\infty}=\sup\{|f(x)|:x\in[0,1]\}$?

\noindent\rule{\linewidth}{0.6pt}

	\par\noindent\textbullet\quad On a finite–measure set (here length $1$): $\displaystyle \|f\|_{1}\le \|f\|_{\infty}$.
	\par\noindent\textbullet\quad A norm must satisfy positivity, homogeneity, triangle inequality, and \emph{definiteness}
	($\|f\|=0 \Rightarrow f=0$ in the underlying space).
	\par\noindent\textbullet\quad Uniform limits of bounded Riemann–integrable functions are Riemann–integrable (boundedness preserved).
	\par\noindent\textbullet\quad $C([0,1])$ is dense in $L^{1}([0,1])$; the $\|\cdot\|_{1}$–completion of $C([0,1])$ is $L^{1}$.

\noindent\rule{\linewidth}{0.6pt}
```

## CP-II-0133

- chapter line: 2579

```tex
\label{prob:cp-ii-0133}
(Quickies) — Statements and Theory

	\par\noindent\textbullet\quad Use the equivalence of norms on a finite dimensional vector space to show that for each $n$, there is a constant $C$ such that the following holds: for every polynomial $p$ of degree $\le n$ there is $x_0 \in [0,1/n]$ such that
	\[
	|p(x)| \le C\,|p(x_0)| \qquad \text{for every } x \in [0,1].
	\]
	\par\noindent\textbullet\quad If $(X,d)$ is a metric space and $A$ is a non-empty subset of $X$, show that the distance from $x\in X$ to $A$ defined by
	\[
	\rho(x)=\inf_{y\in A} d(x,y)
	\]
	is a Lipschitz function on $X$ with Lipschitz constant $\le 1$.
	\par\noindent\textbullet\quad If $(x_n)$, $(y_n)$ are Cauchy sequences in a metric space $(X,d)$, show that $\big(d(x_n,y_n)\big)$ is convergent (in $\mathbb{R}$).

	\par\noindent\textbullet\quad \textbf{Equivalence of norms on finite-dimensional spaces.}
	If $V$ is finite dimensional, any two norms $\|\cdot\|_\alpha,\|\cdot\|_\beta$ on $V$ are equivalent:
	$\exists\,c,C>0$ with $c\|v\|_\beta \le \|v\|_\alpha \le C\|v\|_\beta$ for all $v\in V$.
	In particular, on $\mathcal P_n$ (polynomials of degree $\le n$), the sup-norms
	\[
	\|p\|_{[0,1]}:=\sup_{x\in[0,1]}|p(x)|, \qquad
	\|p\|_{[0,1/n]}:=\sup_{x\in[0,1/n]}|p(x)|
	\]
	are equivalent. The compactness of the unit sphere
	$S=\{p\in\mathcal P_n:\|p\|_{[0,1/n]}=1\}$ and continuity of $p\mapsto \|p\|_{[0,1]}$
	give a finite $C=\max_{p\in S}\|p\|_{[0,1]}$, yielding
	$\|p\|_{[0,1]}\le C\,\|p\|_{[0,1/n]}$.
	Since a nonzero polynomial cannot vanish on infinitely many points, each sup is attained:
	$\|p\|_{[0,1/n]}=|p(x_0)|$ for some $x_0\in[0,1/n]$.

	\par\noindent\textbullet\quad \textbf{Distance to a set is $1$-Lipschitz.}
	For any $x,x'\in X$ and $y\in A$,
	\[
	\rho(x)\le d(x,y)\le d(x,x')+d(x',y)\quad\Rightarrow\quad
	\rho(x)-\rho(x')\le d(x,x').
	\]
	Swapping $x,x'$ gives $|\rho(x)-\rho(x')|\le d(x,x')$.

	\par\noindent\textbullet\quad \textbf{Distances of Cauchy sequences form a Cauchy sequence in $\mathbb R$.}
	For all $m,n$,
	\[
	\big|d(x_n,y_n)-d(x_m,y_m)\big|
	\le d(x_n,x_m)+d(y_n,y_m)
	\]
	by the triangle inequality. Thus if $(x_n)$ and $(y_n)$ are Cauchy, then $(d(x_n,y_n))$ is Cauchy in
	$\mathbb R$ and hence convergent (completeness of $\mathbb R$).

Let $\mathcal P_n=\{p:\deg p\le n\}$. Define
\[
\|p\|_{[0,1]}:=\sup_{x\in[0,1]}|p(x)|,\qquad
\|p\|_{[0,1/n]}:=\sup_{x\in[0,1/n]}|p(x)|.
\]
These are norms on $\mathcal P_n$ (a nonzero polynomial cannot vanish on an infinite set).
Since $\mathcal P_n$ is finite dimensional, the norms are equivalent: there exists $C=C(n)$ with
\[
\|p\|_{[0,1]}\le C\,\|p\|_{[0,1/n]}\qquad(\forall\,p\in\mathcal P_n).
\]
Indeed, on the compact sphere $S=\{p:\|p\|_{[0,1/n]}=1\}$ the continuous map
$p\mapsto \|p\|_{[0,1]}$ attains a maximum $C$. For $p\ne0$,
$\|p\|_{[0,1]}\le C\|p\|_{[0,1/n]}$. Choosing $x_0\in[0,1/n]$ with
$|p(x_0)|=\|p\|_{[0,1/n]}$ yields $|p(x)|\le C\,|p(x_0)|$ for all $x\in[0,1]$.

For nonempty $A\subset X$, define $\rho(x)=\inf_{y\in A} d(x,y)$. For any $x,x'\in X$ and $y\in A$,
$\rho(x)\le d(x,y)\le d(x,x')+d(x',y)$, hence $\rho(x)-\rho(x')\le d(x,x')$; swapping $x,x'$
gives $|\rho(x)-\rho(x')|\le d(x,x')$.

If $(x_n)$ and $(y_n)$ are Cauchy in $(X,d)$, then
\[
\big|d(x_n,y_n)-d(x_m,y_m)\big|\le d(x_n,x_m)+d(y_n,y_m)\xrightarrow[n,m\to\infty]{}0,
\]
so $(d(x_n,y_n))$ is Cauchy in $\mathbb R$ and hence convergent.

\bigskip
```
