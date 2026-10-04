# Part II missing-solution authoring packet

- total Part II problems: **570**
- current paired solutions: **165**
- missing solutions: **405**
- multiple-solution anomalies: **0**

Author canonical worked solutions from these exact current local problem statements.
Do not alter the problem statements.

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

## CP-II-0136

- chapter line: 2654

```tex
\label{prob:cp-ii-0136}
Compactness of Cocountable vs.\ Cofinite Topologies

On a set $X$, let
	\[
	\tau=\{\varnothing\}\cup\{\,U\subseteq X:\ X\setminus U\ \text{is countable}\,\}
	\quad\text{and}\quad
	\rho=\{\varnothing\}\cup\{\,U\subseteq X:\ X\setminus U\ \text{is finite}\,\}.
	\]

		\par\noindent\textbullet\quad If $X$ is finite, then every subset is open (discrete topology), hence $(X,\tau)$ is compact.
		\par\noindent\textbullet\quad If $X$ is infinite, then $(X,\tau)$ is \emph{not} compact.
		Choose a countably infinite subset $A=\{a_1,a_2,\dots\}\subseteq X$.
		For $n\ge1$ set $C_n=\{a_n,a_{n+1},\dots\}$ (countable) and $U_n=X\setminus C_n\in\tau$.
		Then $\bigcup_{n\ge1}U_n=X$ since $\bigcap_{n\ge1} C_n=\varnothing$, but for each $k$,
		\[
		\bigcup_{n=1}^k U_n=X\setminus\Big(\bigcap_{n=1}^k C_n\Big)=X\setminus\{a_k,a_{k+1},\dots\}\neq X,
		\]
		so no finite subcover exists. Hence $(X,\tau)$ is compact iff $X$ is finite (the empty space is compact as usual).

	$(X,\rho)$ is compact for \emph{every} $X$.
	Indeed, given an open cover $\{U_\alpha\}_{\alpha\in A}$ of $X$, pick a nonempty $U_{\alpha_0}$.
	Then $F=X\setminus U_{\alpha_0}$ is finite. For each $x\in F$ choose $U_{\alpha(x)}$ with $x\in U_{\alpha(x)}$.
	Thus
	\[
	X=U_{\alpha_0}\ \cup\ \bigcup_{x\in F} U_{\alpha(x)}
	\]
	is a finite subcover.

	On $X=\mathbb{R}$ the cocountable topology is not compact (use the $U_n=\mathbb{R}\setminus\{a_n,a_{n+1},\dots\}$ cover for a countably infinite subset $\{a_n\}$), while the cofinite topology is compact. If $X$ is finite, both topologies coincide with the discrete topology and are compact.
```

## CP-II-0137

- chapter line: 2687

```tex
\label{prob:cp-ii-0137}
— Positive distributions have order $0$

Suppose $u\in\mathcal D'(\mathbb R^n)$ is positive, i.e.\ $u[\phi]\ge 0$ for all $\phi\in\mathcal D(\mathbb R^n)$ with $\phi\ge 0$.
Show that $u$ has order $0$: for each compact $K\subset\mathbb R^n$ there exists $C_K>0$ such that
\[
|u[\phi]|\le C_K\,\sup_{x\in K}|\phi(x)|,\qquad \forall\,\phi\in C_c^\infty(K).
\]

Fix compact $K$. Define
\[
C_K:=\sup\{\,u[\psi]:\ \psi\in C_c^\infty(K),\ 0\le \psi\le 1\,\}.
\]
Approximating the indicator $\mathbf 1_K$ from below by smooth cutoffs shows $C_K<\infty$ by monotone convergence and positivity.
For any $\phi\in C_c^\infty(K)$ write $\phi=\phi^+-\phi^-$ with $\phi^\pm\ge 0$ and
$\|\phi^\pm\|_{L^\infty(K)}\le \|\phi\|_{L^\infty(K)}$. Then
\[
|u[\phi]|\le u[\phi^+]+u[\phi^-]
\le \|\phi\|_{L^\infty(K)}\,
\sup\{u[\psi]:\ 0\le\psi\le 1,\ \operatorname{supp}\psi\subset K\}
= C_K\,\|\phi\|_{L^\infty(K)}.
\]
Thus $u$ is of order $0$ on $K$. Equivalently, by the Riesz--Markov representation, $u$ is integration against a finite Radon measure on $K$.

\bigskip
\bigskip
```

## CP-II-0138

- chapter line: 2716

```tex
\label{prob:cp-ii-0138}
Let $A+B:=\{a+b:a\in A,\ b\in B\}$ and
	$B_r(x)=\{y\in\mathbb{R}^n:\|y-x\|<r\}$,
	$\overline{B_r(x)}=\{y:\|y-x\|\le r\}$.

		\par\noindent\textbullet\quad Prove the following identities for $r,s>0$ and $x\in\mathbb{R}^n$:

			\par\noindent\textbullet\quad $B_r(x)+B_s(0)=B_{r+s}(x)$;
			\par\noindent\textbullet\quad $\overline{B_r(x)}+B_s(0)=B_{r+s}(x)$;
			\par\noindent\textbullet\quad $\overline{B_r(x)}+\overline{B_s(0)}=\overline{B_{r+s}(x)}$.

		\par\noindent\textbullet\quad Suppose that $A,B\subset\mathbb{R}^n$.
		Show that:

			\par\noindent\textbullet\quad If one of $A$ or $B$ is open, then so is $A+B$.
			\par\noindent\textbullet\quad If $A$ and $B$ are both bounded, then so is $A+B$.
			\par\noindent\textbullet\quad If $A$ is closed and $B$ is compact, then $A+B$ is closed.
			\par\noindent\textbullet\quad If $A$ and $B$ are both compact, then so is $A+B$.

\begin{proof}
	(a)\,(i)\;
	Let $z\in B_r(x)+B_s(0)$, so $z=y+u$ with $\|y-x\|<r$ and $\|u\|<s$.
	Then
	\[
	\|z-x\|\le \|y-x\|+\|u\|<r+s,
	\]
	hence $z\in B_{r+s}(x)$.

	Conversely, let $z\in B_{r+s}(x)$, so $\|z-x\|<r+s$.
	Set
	\[
	y:=x+\frac{r}{r+s}(z-x), \qquad
	u:=z-y=\frac{s}{r+s}(z-x).
	\]
	Then
	\[
	\|y-x\|=\frac{r}{r+s}\|z-x\|<r,\qquad
	\|u\|=\frac{s}{r+s}\|z-x\|<s,
	\]
	so $y\in B_r(x)$, $u\in B_s(0)$ and $z=y+u\in B_r(x)+B_s(0)$.
	Thus $B_r(x)+B_s(0)=B_{r+s}(x)$.

	\smallskip
	(ii)\;
	If $z=y+u$ with $\|y-x\|\le r$ and $\|u\|<s$, then
	\[
	\|z-x\|\le \|y-x\|+\|u\|\le r+\|u\|<r+s,
	\]
	so $z\in B_{r+s}(x)$ and
	$\overline{B_r(x)}+B_s(0)\subset B_{r+s}(x)$.

	Conversely, if $z\in B_{r+s}(x)$, part (i) gives $z=y+u$ with
	$y\in B_r(x)\subset\overline{B_r(x)}$ and $u\in B_s(0)$, hence
	$z\in\overline{B_r(x)}+B_s(0)$. Therefore
	$\overline{B_r(x)}+B_s(0)=B_{r+s}(x)$.

	\smallskip
	(iii)\;
	If $z=y+u$ with $\|y-x\|\le r$, $\|u\|\le s$, then
	$\|z-x\|\le r+s$, so
	$\overline{B_r(x)}+\overline{B_s(0)}\subset\overline{B_{r+s}(x)}$.

	For the reverse inclusion, let $\|z-x\|<r+s$. Then
	$z\in B_{r+s}(x)$ and by (i) we have $z=y+u$ with
	$y\in B_r(x)\subset\overline{B_r(x)}$ and
	$u\in B_s(0)\subset\overline{B_s(0)}$, so
	$z\in\overline{B_r(x)}+\overline{B_s(0)}$.

	If $\|z-x\|=r+s$, set $z_t=x+t(z-x)$, $0<t<1$.
	Then $\|z_t-x\|=t(r+s)<r+s$, hence $z_t\in B_{r+s}(x)$ and thus
	$z_t\in\overline{B_r(x)}+\overline{B_s(0)}$.
	The set $\overline{B_r(x)}+\overline{B_s(0)}$ is compact (sum of two
	compact sets), hence closed, so $z=\lim_{t\to1}z_t$ also belongs to it.
	Therefore $\overline{B_{r+s}(x)}\subset
	\overline{B_r(x)}+\overline{B_s(0)}$ and
	\[
	\overline{B_r(x)}+\overline{B_s(0)}=\overline{B_{r+s}(x)}.
	\]

	\medskip
	(b)\;
	Assume $A$ is open (the case where $B$ is open is analogous).
	Let $z\in A+B$, so $z=a+b$ with $a\in A$, $b\in B$.
	Since $A$ is open, there exists $r>0$ with $B_r(a)\subset A$.
	If $\|y-z\|<r$ and we set $a':=a+(y-z)$, then
	$\|a'-a\|=\|y-z\|<r$, so $a'\in B_r(a)\subset A$, and
	$y=a'+b\in A+B$. Thus $B_r(z)\subset A+B$ and $A+B$ is open.

	\medskip
	(c)\;
	Suppose $A\subset B_M(0)$ and $B\subset B_N(0)$ for some $M,N>0$.
	If $z=a+b\in A+B$, then
	\[
	\|z\|\le\|a\|+\|b\|\le M+N,
	\]
	so $A+B\subset B_{M+N}(0)$ and $A+B$ is bounded.

	\medskip
	(d)\;
	Assume $A$ is closed and $B$ is compact. Let $(z_k)$ be a sequence in
	$A+B$ with $z_k\to z$. Write $z_k=a_k+b_k$ with
	$a_k\in A$ and $b_k\in B$.

	By compactness of $B$, there is a subsequence $(b_{k_j})$ such that
	$b_{k_j}\to b\in B$. Then
	\[
	a_{k_j}=z_{k_j}-b_{k_j}\longrightarrow z-b.
	\]
	Since $A$ is closed and $a_{k_j}\in A$, we have $z-b\in A$, hence
	$z=(z-b)+b\in A+B$. Therefore $A+B$ is closed.

	\medskip
	(e)\;
	If $A$ and $B$ are compact, then $A\times B$ is compact and the map
	\[
	f:A\times B\to\mathbb{R}^n,\qquad f(a,b)=a+b
	\]
	is continuous. Hence $A+B=f(A\times B)$ is compact as the continuous
	image of a compact set.
\end{proof}

Figure~\ref{fig:triangle-plus-ball} gives a concrete picture: if $A$ is a closed triangle and $B$ a small closed ball, then $A+B$ is a uniformly thickened version of $A$.

\begin{figure}[ht]
	\centering
	\begin{tikzpicture}[scale=1.7]

		% axes (optional)
		\draw[->,gray!60] (-0.6,0) -- (2.6,0) node[below] {$x_1$};
		\draw[->,gray!60] (0,-0.6) -- (0,2.0) node[left] {$x_2$};

		% --- compact set A: a triangle ---
		\coordinate (A1) at (0.2,0.0);
		\coordinate (A2) at (2.0,0.0);
		\coordinate (A3) at (1.1,1.6);

		\fill[blue!10] (A1)--(A2)--(A3)--cycle;
		\draw[blue!70!black,thick] (A1)--(A2)--(A3)--cycle;
		\node[blue!70!black] at (1.1,0.2) {$A$};

		% --- small ball B centred at the origin ---
		\def\r{0.35}
		\fill[red!10] (0,0) circle (\r);
		\draw[red!70!black,thick] (0,0) circle (\r);
		\node[red!70!black] at (-0.15,-0.45) {$B$};

		% --- Minkowski sum A+B (schematic outline) ---
		% (offset triangle by radius r; this is only illustrative)
		\draw[green!50!black,thick,dashed]
		($(A1)+(-\r,0)$) arc (180:360:\r) -- ($(A2)+(0,\r)$)
		arc (-90:30:\r) -- ($(A3)+(\r*0.5,\r*0.866)$)
		arc (30:150:\r) -- ($(A1)+(-\r*0.5,\r*0.866)$)
		arc (150:210:\r) -- cycle;

		\node[green!50!black] at (1.3,1.3) {$A+B$};

	\end{tikzpicture}
	\caption{Minkowski sum of a compact set $A$ (triangle) with a small ball $B$.
		Geometrically, $A+B$ is obtained by ``thickening'' $A$ by the radius of $B$.
		Since both $A$ and $B$ are compact, their sum $A+B$ is compact as well.}
	\label{fig:triangle-plus-ball}
\end{figure}

Let $A = B_1(0) = \{x\in\mathbb{R}^2 : \|x\|<1\}$ and let $b\in\mathbb{R}^2$.
Define
\[
B = \{0,b\}.
\]
Then
\[
A+B = \{a+p : a\in A,\ p\in B\}
= A + \{0,b\}
= A \cup (A+b).
\]
In particular, for the two specific choices
\[
b_1=(2,0), \qquad b_2=(0,2),
\]
we obtain
\[
A+\{0,b_1\} = B_1(0)\cup B_1\bigl((2,0)\bigr), \qquad
A+\{0,b_2\} = B_1(0)\cup B_1\bigl((0,2)\bigr).
\]
In each case $A$ is open, $B$ is finite, and $A+B$ is the union of two
open discs, hence open but not connected.

Let
\[
A = B_1(0) = \{x\in\mathbb{R}^2 : \|x\|<1\}
\]
and choose two vectors
\[
b_1 = (2,0), \qquad b_2 = (0,2).
\]
Define
\[
B = \{b_1, b_2\}.
\]
Then the Minkowski sum is
\[
\begin{aligned}
	A+B
	&= \{a+p : a\in A,\ p\in B\}
	= A + \{b_1,b_2\} \\
	&= (A+b_1)\ \cup\ (A+b_2) \\
	&= B_1\bigl((2,0)\bigr)\ \cup\ B_1\bigl((0,2)\bigr).
\end{aligned}
\]
Thus $A+B$ is the union of two open discs, hence open but not connected.
Note that, in contrast with the case $B=\{0,b_1,b_2\}$, there is now no
disc centred at the origin, because $0\notin B$.
```

## CP-II-0145

- chapter line: 2930

```tex
\label{prob:cp-ii-0145}
\par\noindent\textbullet\quad Lebesgue measure $m$ on $\mathbb{R}^n$ is a complete Radon Borel measure.
```

## CP-II-0146

- chapter line: 2935

```tex
\label{prob:cp-ii-0146}
s.

\par\noindent\textbullet\quad Conversely, from $a\|x\|_1\le\|x\|_2$, we get
	$B_2(x_0,r)\subseteq B_1(x_0,r/a)$.

So open balls in one norm contain open balls of the other.
Hence both topologies have the same open sets.

\par\medskip\noindent\textbf{(2)$\Rightarrow$(3).}\quad
If the two topologies coincide, then convergence (defined by open neighborhoods)
is identical. Thus a sequence converges in one norm if and only if it converges in the other.

\par\medskip\noindent\textbf{(3)$\Rightarrow$(1).}\quad
Assume the same convergent sequences.
We show existence of $a,b>0$.

Define $f(x)=\|x\|_2$.
If no $b$ exists with $\|x\|_2\le b\|x\|_1$,
we could find a sequence $x_n$ with $\|x_n\|_1=1$ and $\|x_n\|_2>n$.
Then $x_n/n\to 0$ in $\|\cdot\|_1$ but not in $\|\cdot\|_2$, contradicting (3).
Thus $\exists b>0$ s.t.\ $\|x\|_2\le b\|x\|_1$.

Similarly, interchanging norms gives $a>0$ s.t.\ $a\|x\|_1\le\|x\|_2$.
Hence the norms are equivalent.
```

## CP-II-0153

- chapter line: 2963

```tex
\label{prob:cp-ii-0153}
— Positive separation

Let \(K\subset \mathbb{R}^2\) be compact and let \(F\subset \mathbb{R}^2\) be closed with \(K\cap F=\varnothing\).

Show that there exists \(\delta>0\) such that \(d(x,y)\ge \delta\) for every \(x\in K\) and every \(y\in F\).

Give two proofs: one from compactness of \(K\), and one using sequential compactness.

\bigskip

For \(A\subset\mathbb{R}^2\) and \(x\in\mathbb{R}^2\),
\[
\operatorname{dist}(x,A)=\inf\{\|x-a\|:a\in A\}.
\]
If \(A\) is closed and \(x\notin A\), then \(\operatorname{dist}(x,A)>0\).

Compactness: every open cover has a finite subcover.

Sequential compactness: every sequence in \(K\) has a convergent subsequence with limit in \(K\).

Closed sets are sequentially closed.

\bigskip

For each \(x\in K\), since \(x\notin F\) and \(F\) is closed, we have \(\operatorname{dist}(x,F)>0\).
Let
\[
r_x=\tfrac12\,\operatorname{dist}(x,F).
\]
Then \(B(x,r_x)\cap F=\varnothing\).
The family \(\{B(x,r_x):x\in K\}\) covers \(K\).

By compactness of \(K\), choose \(x_1,\dots,x_m\in K\) with
\[
K\subset \bigcup_{i=1}^{m} B(x_i,r_{x_i}).
\]
Set
\[
\delta=\min_{1\le i\le m} r_{x_i}>0.
\]
If \(x\in K\) and \(y\in F\), choose \(i\) so that \(x\in B(x_i,r_{x_i})\).
Because \(B(x_i,r_{x_i})\cap F=\varnothing\), we have \(d(x,y)\ge r_{x_i}\ge\delta\).
Thus \(d(x,y)\ge\delta\) for all \(x\in K,\; y\in F\).

\bigskip

Assume no such \(\delta>0\) exists.
Then for each \(n\in\mathbb{N}\) there exist \(x_n\in K\) and \(y_n\in F\) with
\[
d(x_n,y_n)<\tfrac{1}{n}.
\]
By sequential compactness, there is a subsequence \(x_{n_k}\to x\in K\).
Since \(d(x_{n_k},y_{n_k})\to 0\), it follows that \(y_{n_k}\to x\).
Because \(F\) is closed and all \(y_{n_k}\in F\), we have \(x\in F\).
Hence \(x\in K\cap F\), a contradiction.

Therefore some \(\delta>0\) exists.

\bigskip

If \(K=\{(x,y):x^2+y^2=1\}\) and \(F=\{(3,t):t\in\mathbb{R}\}\), then the minimal distance is \(2\).

If compactness of \(K\) is dropped, the claim may fail; there are disjoint closed sets with zero infimum distance.

A topological space \(X\) is sequentially compact if every sequence in \(X\) has a convergent subsequence with limit in \(X\).

\bigskip

\par\noindent\textbullet\quad Closed and bounded subsets of \(\mathbb{R}^n\) (e.g.\ \([0,1]^n\), spheres, closed balls). By Bolzano--Weierstrass.
\par\noindent\textbullet\quad Any compact metric space (in metric spaces, compact \(\Leftrightarrow\) sequentially compact).
\par\noindent\textbullet\quad Finite spaces (every sequence is eventually constant).

\medskip

\par\noindent\textbullet\quad \((0,1)\subset\mathbb{R}\): the sequence \(x_n=1/n\) has no convergent subsequence in \((0,1)\).
\par\noindent\textbullet\quad \([0,\infty)\): the sequence \(x_n=n\) has no convergent subsequence.
\par\noindent\textbullet\quad \([0,1]\cap\mathbb{Q}\): rationals \(q_n\to\sqrt{2}\) (in \(\mathbb{R}\)) yield no convergent subsequence in the space.

\medskip

\par\noindent\textbullet\quad An uncountable set with the co-countable topology.

Any sequence has a convergent subsequence (indeed, often converges to every point), so the space is sequentially compact.
The open cover \(\{\,X\setminus\{x\}\,:\,x\in X\,\}\) has no finite subcover, so the space is not compact.

\smallskip

\par\noindent\textbullet\quad The Cantor cube \(2^{\mathbb{R}}\) (product of \(\{0,1\}\) over an uncountable index set).

Compact by Tychonoff, but not sequentially compact; there exist sequences with no convergent subsequence (product convergence is coordinatewise and can be made to oscillate on infinitely many coordinates).

\par\noindent\textbullet\quad The Stone--Ă„Ĺšech compactification \(\beta\mathbb{N}\).

Compact Hausdorff, yet not sequentially compact.

\medskip

\noindent\textbf{Summary.}
In metric spaces, compactness and sequential compactness coincide. In general topological spaces, neither implies the other.

\noindent\textbf{Compact.}
Every open cover has a finite subcover.

\smallskip

\noindent\textbf{Paracompact.}
Every open cover has a locally finite open refinement
(i.e., each point meets only finitely many sets of the refinement).

\smallskip

\noindent\textbf{Precompact (totally bounded / relatively compact).}
In a metric (or uniform) space: for every \(\varepsilon>0\) there exist finitely many
\(\varepsilon\)-balls covering the space.
Equivalently, the closure in the completion is compact.

\smallskip

\noindent\textbf{Sequentially compact.}
Every sequence has a convergent subsequence with limit in the space.

\smallskip

\noindent\textbf{Lindel\"of.}
Every open cover admits a countable subcover.

\smallskip

\noindent\textbf{General spaces.}
\[
\text{Compact} \;\Rightarrow\; \text{Lindel\"of} \quad\text{and}\quad
\text{Compact} \;\Rightarrow\; \text{Paracompact}.
\]
The converses need not hold.

\smallskip

\noindent\textbf{Metric spaces.}
\[
\text{Compact} \;\Longleftrightarrow\; \text{Sequentially compact}
\;\Longleftrightarrow\; \text{Complete}+\text{Totally bounded (Precompact)}.
\]
Also, every metric space is paracompact, and
\[
\text{Separable} \;\Longleftrightarrow\; \text{Second countable}
\;\Longleftrightarrow\; \text{Lindel\"of}.
\]

\smallskip

\noindent\emph{Precompact but not compact:} \((0,1)\subset\mathbb{R}\).

\smallskip

\noindent\emph{Lindel\"of but not compact:} \(\mathbb{R}\) with the usual topology.

\smallskip

\noindent\emph{Compact hence paracompact:} any compact Hausdorff space.

\smallskip

\noindent\emph{Sequentially compact} \(=\) \emph{compact (metric):} closed intervals \([a,b]\subset\mathbb{R}\).
```

## CP-II-0166

- chapter line: 3160

```tex
\label{prob:cp-ii-0166}
Identity property of the Dirac distribution

\noindent
(a)\; Show that if $\phi \in \mathcal{D}(\mathbb{R}^n)$ then
\[
\delta_0 * \phi = \phi .
\]

\medskip
\noindent
(b)\; Show that if $u \in \mathcal{D}'(\mathbb{R}^n)$ has compact support, then
\[
\delta_0 * u = u .
\]
```

## CP-II-0168

- chapter line: 3178

```tex
\label{prob:cp-ii-0168}
\textbf{Approximating $1/z$ on $U=B_2(1)\setminus B_1(0)$.}

		\par\noindent (i)\quad (Compacts in $U$.) Runge with poles at $\{0,\infty\}$ allows Laurent polynomials.
		For $f(z)=1/z$ the constant sequence
		\[
		r_n(z)\equiv \frac{1}{z}
		\]
		already works and converges uniformly to $1/z$ on every compact $K\subset U$.

		If $K\subset B_1(1)$ (so $|z-1|<1$ on $K$), the \emph{polynomials}
		\[
		p_N(z)=\sum_{k=0}^N (-1)^k(z-1)^k
		\]
		satisfy $p_N\to 1/z$ uniformly on $K$ by the geometric series
		$\frac{1}{1+w}=\sum_{k\ge0}(-w)^k$ with $w=z-1$.

		\par\noindent (ii)\quad (No polynomials on all of $U$.) Suppose $p_n$ were polynomials with
		$p_n\to 1/z$ uniformly on $U$. For the loop $\gamma(t)=e^{it}$,
		\[
		\int_\gamma p_n(z)\,dz \longrightarrow \int_\gamma \frac{1}{z}\,dz=2\pi i,
		\]
		but each $\int_\gamma p_n(z)\,dz=0$, contradiction. Hence no polynomial sequence
		converges to $1/z$ uniformly on $U$ (and the same holds even if $1/z$ extends past $\overline U$).
```

## CP-II-0180

- chapter line: 3205

```tex
\label{prob:cp-ii-0180}
— Which duals contain $u_f$ for $f(x)=e^x\cos(e^x)$?

Let $f:\mathbb R\to\mathbb R$, $f(x)=e^x\cos(e^x)$, and let $u_f[\phi]=\int_{\mathbb R} f(x)\phi(x)\,dx$.
Decide whether $u_f$ belongs to $\mathcal D'(\mathbb R)$, $\mathcal S'(\mathbb R)$, and $\mathcal E'(\mathbb R)$.

\smallskip

$\mathcal D'(\mathbb R)$: For $\phi\in\mathcal D(\mathbb R)$ the support is compact, hence $\int f\phi$ is finite and depends continuously on $\phi$.
Thus $u_f\in\mathcal D'(\mathbb R)$.

\smallskip

$\mathcal E'(\mathbb R)$: Elements of $\mathcal E'$ are compactly supported distributions. Since $f$ is not compactly supported,
the regular distribution $u_f$ is not in $\mathcal E'(\mathbb R)$.

\smallskip

$\mathcal S'(\mathbb R)$: A regular distribution is tempered iff its defining function has at most polynomial growth.
Here $|f(x)|\le e^x$, so the growth is exponential. To see non–temperateness directly, set
\[
\phi_k(x)=\frac{e^{-(x-k)^2}}{(1+k)^M},\qquad k\in\mathbb N,
\]
with $M$ chosen large enough that all Schwartz seminorms of $\phi_k$ remain bounded in $k$.
Then
\[
\int_{\mathbb R} e^x\cos(e^x)\,\phi_k(x)\,dx
= \frac{e^{k}}{(1+k)^M}\int_{\mathbb R} e^{-(y^2-y)}\cos(e^{k+y})\,dy,
\]
whose absolute value is $\gtrsim e^{k}/(1+k)^M\to\infty$.
Hence the functional is not continuous on $\mathcal S$, so $u_f\notin\mathcal S'(\mathbb R)$.

$u_f\in\mathcal D'(\mathbb R)$, but $u_f\notin\mathcal S'(\mathbb R)$ and $u_f\notin\mathcal E'(\mathbb R)$.

\bigskip
\bigskip
```

## CP-II-0185

- chapter line: 3244

```tex
\label{prob:cp-ii-0185}
Every bounded sequence has a convergent subsequence

Let $V$ be a normed space in which every bounded sequence has a convergent subsequence.

	\par\noindent\textbullet\quad Show that this property is equivalent to the sequential compactness of the unit sphere
	$S=\{x\in V:\|x\|=1\}$.
	\par\noindent\textbullet\quad Show that $V$ must be complete.
	\par\noindent \textnormal{(c)$^*$}\quad Show further that $V$ must be finite--dimensional.

\emph{Hint for (c).} For every finite--dimensional subspace $V_0$ of $V$, there exists $x\in V$
with $\|x+y\|>\|x\|/2$ for each $y\in V_0$.

Sequential compactness means every sequence has a convergent subsequence.
Cauchy sequences are bounded; if a Cauchy sequence has one convergent subsequence, then the whole sequence converges.
A Riesz--lemma variant: if $V_0$ is finite--dimensional (hence closed) and $0<\alpha<1$, there exists $x$ with $\|x\|=1$ and
$\operatorname{dist}(x,V_0)>\alpha$; equivalently, $\|x+y\|>\alpha$ for all $y\in V_0$.

	\par\noindent\textbullet\quad
	Assume every bounded sequence in $V$ has a convergent subsequence. Then the unit sphere $S$ is bounded,
	so any sequence in $S$ has a convergent subsequence in $V$. If $x_{n_k}\to x$, then
	$\|x\|=\lim_k\|x_{n_k}\|=1$, hence $x\in S$. Thus $S$ is sequentially compact.

	Conversely, suppose $S$ is sequentially compact. Let $(x_n)$ be bounded in $V$ and set $r_n=\|x_n\|$.
	Passing to a subsequence we may assume $(r_n)$ converges to $r\ge 0$.
	For each $n$ with $x_n\neq 0$ define $u_n=x_n/\|x_n\|\in S$; for $x_n=0$ define $u_n$ arbitrarily in $S$.
	By sequential compactness of $S$, $(u_n)$ admits a convergent subsequence $u_{n_k}\to u\in S$.
	Then $x_{n_k}=r_{n_k}u_{n_k}\to r u$ in $V$. Hence every bounded sequence has a convergent subsequence.

	\par\noindent\textbullet\quad
	Let $(y_n)$ be Cauchy in $V$. Then $(y_n)$ is bounded, so it has a convergent subsequence $y_{n_k}\to y$.
	Fix $\varepsilon>0$. Choose $N$ such that $\|y_n-y_m\|<\varepsilon/2$ for all $m,n\ge N$,
	and choose $k$ with $n_k\ge N$ and $\|y_{n_k}-y\|<\varepsilon/2$.
	For $n\ge N$ we have
	\[
	\|y_n-y\|\le \|y_n-y_{n_k}\|+\|y_{n_k}-y\|<\varepsilon.
	\]
	Thus $y_n\to y$, so $V$ is complete.

	\par\noindent \textnormal{(c)$^*$}\quad
	Suppose $V$ were infinite--dimensional. Construct inductively a sequence $(x_n)\subset V$ with
	$\|x_n\|=1$ and
	\[
	\operatorname{dist}(x_{n+1},V_n)>\tfrac12,
	\qquad
	V_n=\operatorname{span}\{x_1,\dots,x_n\}.
	\]
	This is possible by the Riesz--lemma variant (applied to the finite--dimensional subspace $V_n$ with $\alpha=\tfrac12$).
	Then for $j>i$ we have $x_i\in V_{j-1}$, hence
	\[
	\|x_j-x_i\|\ge \operatorname{dist}(x_j,V_{j-1})>\tfrac12 .
	\]
	Therefore $(x_n)$ is bounded (all have norm $1$) but has no Cauchy subsequence, because any two distinct
	terms of any tail are at distance $>1/2$.
	This contradicts the hypothesis that every bounded sequence has a convergent subsequence.
	Hence $V$ must be finite--dimensional.
```

## CP-II-0191

- chapter line: 3303

```tex
\label{prob:cp-ii-0191}
Let $f:\mathbb{R}^m\to\mathbb{R}^n$ be a function such that:

		\par\noindent\textbullet\quad the image of every path-connected subset of $\mathbb{R}^m$ is path-connected;
		\par\noindent\textbullet\quad the image of every compact subset of $\mathbb{R}^m$ is compact.

	Show that $f$ is continuous.


	\textbf{Theory.}
	A continuous map between Hausdorff spaces preserves compactness and connectedness.
	Conversely, if a map preserves both compactness and (path-)connectedness in $\mathbb{R}^m$,
	then discontinuities would produce separated image pieces—contradicting path-connectedness.
	Hence these two preservation properties together imply continuity.
```

## CP-II-0203

- chapter line: 3321

```tex
\label{prob:cp-ii-0203}
\par\noindent\textbullet\quad For $\mu=m$ and $\nu=f\,m+\sum_{k\ge1} a_k\delta_{x_k}$ with $f\in L^1(m)$, $a_k\ge0$,
		the decomposition is $\nu_a=f\,m$ and $\nu_s=\sum_{k\ge1} a_k\delta_{x_k}$.

	A measure $\mu$ on $(E,\mathcal E)$ is \emph{finite} if $\mu(E)<\infty$.
	Finite measures are automatically $\sigma$-finite, and the Radon--Nikodym and
	Lebesgue decomposition theorems hold in this setting.

	\bigskip

	Let $X$ be a locally compact Hausdorff space (often second countable).
	A (positive) Borel measure $\mu$ on $X$ is a \emph{Radon measure} if it is
	\emph{inner regular} ($\mu(A)=\sup\{\mu(K):K\subset A,~K\text{ compact}\}$),
	\emph{outer regular} ($\mu(A)=\inf\{\mu(U):A\subset U,~U\text{ open}\}$),
	and \emph{locally finite}. Typical examples include Lebesgue measure on
	$\mathbb R^n$, counting measure on a discrete LCH space, and surface measure on smooth manifolds.

	\bigskip

	If $G$ is a locally compact topological group, a \emph{Haar measure} is a nonzero
	Radon measure $\eta$ that is left invariant: $\eta(gA)=\eta(A)$ for all Borel $A$ and $g\in G$.
	Haar measure is unique up to a positive scalar multiple.
	Examples: on $\mathbb R^n$, Haar measure equals Lebesgue measure; on a compact group
	(e.g.\ $\mathbb T^n$), Haar measure can be normalized to total mass $1$; on discrete groups, Haar is counting measure.

	\bigskip

	For measures $\nu,\mu$ on $(E,\mathcal E)$:
```

## CP-II-0218

- chapter line: 3400

```tex
\label{prob:cp-ii-0218}
Hausdorffness and Second Countability are Topological Invariants

Show that the Hausdorff property and second countability are preserved under homeomorphisms.

A homeomorphism $f:X\to Y$ is a bijection such that both $f$ and $f^{-1}$ are continuous. Such a map carries open sets to open sets and bases to bases via images.

Assume $f:X\to Y$ is a homeomorphism and $X$ is Hausdorff. For $y_1\neq y_2$ in $Y$, set $x_i=f^{-1}(y_i)$. Since $X$ is Hausdorff there exist disjoint open sets $U_i\ni x_i$. Then $f(U_i)$ are disjoint open neighbourhoods of $y_i$, so $Y$ is Hausdorff. The converse follows by applying the same argument to $f^{-1}$.

Let $\mathcal{B}=\{B_n:n\in\mathbb{N}\}$ be a countable base for $X$. Because $f$ is open and bijective, $\{f(B_n):n\in\mathbb{N}\}$ is a countable base for $Y$. Conversely, apply the same reasoning to $f^{-1}$.
```

## CP-II-0223

- chapter line: 3413

```tex
\label{prob:cp-ii-0223}
\par\noindent\textbullet\quad If $U_1,U_2$ are open, then $U_1\cup U_2$ and $U_1\cap U_2$ are open.
\par\noindent\textbullet\quad If $E_1,E_2$ are closed, then $E_1\cup E_2$ and $E_1\cap E_2$ are closed.
\par\noindent\textbullet\quad For any collection $\mathcal U$ of open sets: $\bigcup\mathcal U$ is open; $\bigcap\mathcal U$ need not be open (e.g.\ $\cap_{n\ge1}(-1/n,1/n)=\{0\}$);
for closed sets: arbitrary intersections are closed, finite unions are closed, infinite unions need not be closed.
```

## CP-II-0229

- chapter line: 3421

```tex
\label{prob:cp-ii-0229}
\par\noindent\textbullet\quad Suppose that $(u_i)_{i=1}^\infty$ is a sequence with
	$u_i\in H_0^1(\Omega)$ and $u_i\rightharpoonup u$ weakly in $H_0^1(\Omega)$.
	Show that
	\[
	E[u]\le \liminf_{i\to\infty}E[u_i].
	\]

	\par\noindent\textbullet\quad Consider the set
	\[
	\mathcal{E}_1=\{E[u]:u\in H_0^1(\Omega),\ \|u\|_{L^2}=1\}.
	\]
	Let $\lambda_1:=\inf\mathcal{E}_1$. Show that there exists
	$w_1\in H_0^1(\Omega)$ with $\|w_1\|_{L^2}=1$ and $E[w_1]=\lambda_1$, and
	deduce that $\lambda_1>0$.

	\par\noindent\textbullet\quad Deduce that
	\[
	\lambda_1\|u\|_{L^2}^2\le \int_\Omega |Du|^2\,dx
	\]
	holds for all $u\in H_0^1(\Omega)$, with equality for $u=w_1$.
	This is Poincar\'e's inequality.

	\par\noindent\textbullet\quad By considering $u=w_1+t\varphi$ for $t\in\mathbb{R}$ and
	$\varphi\in\mathcal{D}(\Omega)=C_c^\infty(\Omega)$, or otherwise,
	show that $w_1$ satisfies
	\[
	-\Delta w_1=\lambda_1 w_1
	\]
	in the sense of distributions, i.e.\ in $\mathcal{D}'(\Omega)$.

	\par\noindent \textnormal{(e)}\quad Suppose $\chi\in C_c^\infty(\Omega)$ and put $v=\chi w_1$.
	Show that $v$ satisfies
	\[
	-\Delta v + v = f
	\]
	in $\mathcal{S}'(\mathbb{R}^n)$, where $f\in L^2(\mathbb{R}^n)$.
	Deduce that $v\in H^2(\mathbb{R}^n)$. By iterating this argument, deduce that
	\[
	w_1\in H_0^1(\Omega)\cap C^\infty(\Omega).
	\]

	\par\noindent \textnormal{(f)}\quad Consider
	\[
	\mathcal{E}_2=\{E[u]:u\in H_0^1(\Omega),\ \|u\|_{L^2}=1,\ (u,w_1)_{L^2}=0\}.
	\]
	Show that there exist $\lambda_2\ge\lambda_1$ and
	$w_2\in H_0^1(\Omega)\cap C^\infty(\Omega)$ with
	$w_2\neq w_1$, $\|w_2\|_{L^2}=1$ and
	\[
	-\Delta w_2=\lambda_2 w_2.
	\]

The space $H_0^1(\Omega)$ is the closure of $C_c^\infty(\Omega)$ in the
Sobolev norm
\[
\|u\|_{H^1}^2=\|u\|_{L^2}^2+\|Du\|_{L^2}^2.
\]
The functional $E[u]=\|Du\|_{L^2}^2$ is convex and weakly lower semicontinuous
on $H_0^1(\Omega)$. Since $\Omega$ is bounded, the embedding
$H_0^1(\Omega)\hookrightarrow L^2(\Omega)$ is compact (Rellich--Kondrachov).

The Dirichlet Laplacian $-\Delta$ with domain $H_0^1(\Omega)$ has discrete
spectrum
\[
0<\lambda_1\le\lambda_2\le\cdots\to\infty,
\]
and the first eigenvalue admits the variational characterisation
\[
\lambda_1 = \inf\left\{
\frac{\int_\Omega |Du|^2}{\int_\Omega |u|^2}
: u\in H_0^1(\Omega),\,u\neq 0\right\}.
\]
Minimisers are eigenfunctions solving $-\Delta u=\lambda_1 u$.

For the constant–coefficient elliptic operator $-\Delta+I$ on $\mathbb{R}^n$
the equation $(-\Delta+I)v=f$ with $f\in L^2(\mathbb{R}^n)$ implies
$v\in H^2(\mathbb{R}^n)$. By iterating and using Sobolev embedding, one
derives interior smoothness for solutions of $-\Delta u = \lambda u$.
```

## CP-II-0257

- chapter line: 4148

```tex
\label{prob:cp-ii-0257}
Convolution of regular and general distributions

\noindent
(a)\; Show that for $f,g\in C_0^\infty(\mathbb{R}^n)$,
\[
T_{f*g} = T_f * T_g .
\]

\medskip
\noindent
(b)\; Show that convolution is linear in both of its arguments, i.e.\ if
$u_i\in\mathcal{D}'(\mathbb{R}^n)$ and $u_3,u_4$ have compact support, then
for any $a\in\mathbb{C}$,
\[
(u_1 + a u_2)\,*\,u_3 = u_1*u_3 + a\,u_2*u_3,
\]
and
\[
u_1 * (u_3 + a u_4) = u_1*u_3 + a\,u_1*u_4.
\]
```

## CP-II-0265

- chapter line: 4205

```tex
\label{prob:cp-ii-0265}
— Strict contractions on complete vs compact spaces; non-expansive maps

\noindent\textbf{Task.}
 \setlength{\itemsep}{4pt}
	\par\noindent\textbullet\quad Give a non-empty complete metric space $(X,d)$ and a map $f:X\to X$ with
	$d(f(x),f(y))<d(x,y)$ for all $x\neq y$, but \emph{no fixed point}.
	\par\noindent\textbullet\quad Now assume $X\subset\mathbb{R}^n$ is non-empty and \emph{compact} (Euclidean metric).
	Show that such an $f$ \emph{must} have a fixed point (and decide uniqueness).
	\par\noindent\textbullet\quad If $g:X\to X$ only satisfies $d(g(x),g(y))\le d(x,y)$ for all $x,y$, must $g$ have a fixed point?

\bigskip
\hrule
\bigskip

\noindent\textbf{Theory youĂ˘â‚¬â„˘ll use.}
 \setlength{\itemsep}{6pt}
	\par\noindent\textbullet\quad A metric space is \emph{complete} if every Cauchy sequence converges.
	\par\noindent\textbullet\quad On a compact metric space, any continuous map $h:X\to\mathbb{R}$ attains its minimum
	(apply this to $h(x)=d(f(x),x)$).
	\par\noindent\textbullet\quad \emph{EdelsteinĂ˘â‚¬â„˘s fixed point theorem.} On a compact metric space, a map
	$f$ with $d(f(x),f(y))<d(x,y)$ for all $x\neq y$ has a \emph{unique} fixed point.
	\par\noindent\textbullet\quad If $a_n=d(x_{n+1},x_n)$ and $a_{n+1}<a_n$, then $(a_n)$ is strictly decreasing
	and converges to some $L\ge0$.

\bigskip
\hrule
\bigskip

\noindent\textbf{Part 1 — Strictly contractive, complete, no fixed point (example).}

\medskip
\noindent Let $X=(0,\infty)$ and define
\[
d(x,y):=\big|\ln x-\ln y\big|\qquad (x,y>0).
\]
Then $(X,d)$ is complete because $(0,\infty)$ with this metric is isometric to
$(\mathbb{R},|\cdot|)$ via $x\mapsto \ln x$.

\medskip
\noindent Define $f(x)=x+1$. For $x\neq y$, by the mean value theorem there exist
$\xi$ between $x+1$ and $y+1$ and $\eta$ between $x$ and $y$ with
\[
\big|\ln(x+1)-\ln(y+1)\big|=\frac{|x-y|}{\xi},
\qquad
\big|\ln x-\ln y\big|=\frac{|x-y|}{\eta}.
\]
Since $\xi>\eta>0$, we have
\[
d\big(f(x),f(y)\big)=\frac{|x-y|}{\xi}\;<\;\frac{|x-y|}{\eta}=d(x,y)
\quad\text{for all }x\ne y.
\]
But $f(x)=x+1$ has no fixed point. Hence we have a complete space with a strict
contraction (in the pointwise sense) without a fixed point.

\bigskip
\hrule
\bigskip

\noindent\textbf{Part 2 — Compact $X\subset\mathbb{R}^n$: existence and uniqueness.}

\medskip
\noindent Let $X\subset\mathbb{R}^n$ be non-empty and compact (Euclidean metric).
Suppose $f:X\to X$ satisfies $d(f(x),f(y))<d(x,y)$ for all $x\ne y$.

\medskip
\noindent\emph{Existence.}
Pick any $x_0\in X$ and iterate $x_{k+1}=f(x_k)$. Set $a_k=d(x_{k+1},x_k)$.
Then
\[
a_{k+1}=d\big(f(x_{k+1}),f(x_k)\big)\;<\;d(x_{k+1},x_k)=a_k,
\]
so $(a_k)$ decreases to some $L\ge0$. By compactness, there is a subsequence
$x_{n_j}\to p\in X$. Then $x_{n_j+1}=f(x_{n_j})\to f(p)$, and by continuity of $d$,
\[
L=\lim_{j\to\infty} d\big(x_{n_j+1},x_{n_j}\big)
= d\big(f(p),p\big).
\]
If $L>0$, applying the strict inequality to $(p,f(p))$ gives
\[
d\big(f(f(p)),f(p)\big)\;<\;d\big(p,f(p)\big)=L,
\]
but the left-hand side equals $\lim_j d(x_{n_j+2},x_{n_j+1})=L$, a contradiction.
Hence $L=0$ and $f(p)=p$.

\medskip
\noindent\emph{Uniqueness.}
If $p\ne q$ are fixed points, then
\[
d\big(f(p),f(q)\big)=d(p,q)\;<\;d(p,q),
\]
impossible. Therefore the fixed point is \emph{unique}.

\bigskip
\hrule
\bigskip

\noindent\textbf{Part 3 — Non-expansive maps ($\le$) need not have fixed points.}

\medskip
\noindent Let $X=S^1\subset\mathbb{R}^2$ be the unit circle with the Euclidean metric,
and let $g$ be rotation by a nonzero angle. Then
\[
d\big(g(x),g(y)\big)=d(x,y)\le d(x,y)\quad\text{for all }x,y\in S^1,
\]
but $g$ has no fixed point. Thus the condition $d(g(x),g(y))\le d(x,y)$
does \emph{not} ensure a fixed point, even on compact sets.

\bigskip
\hrule
\bigskip
```

## CP-II-0268

- chapter line: 4319

```tex
\label{prob:cp-ii-0268}
— Statements and Theory

	\par\noindent\textbullet\quad Is the set $(1,2]$ an open subset of the metric space $\mathbb{R}$ with the metric $d(x,y)=|x-y|$? Is it closed?
	What if we replace the metric space $\mathbb{R}$ with the space $[0,2]$, the space $(1,3)$ or the space $(1,2]$, in each case with the metric $d$?
	\par\noindent\textbullet\quad Let $X$ be a set equipped with the discrete metric, and $Y$ any metric space. Describe all open subsets of $X$, closed subsets of $X$, compact subsets of $X$, Cauchy sequences in $X$, continuous functions $f:X\to Y$ and continuous functions $f:Y\to X$.

	\par\noindent\textbullet\quad \textbf{Subspace topology / metric.}
	If $M\subset Z$ and $Z$ is metric with $d_Z$, the subspace metric on $M$ is
	$d_M(x,y)=d_Z(x,y)$. A set $U\subset M$ is open in $M$ iff $U=M\cap O$ for some open $O\subset Z$.
	Closedness is analogous.

	\par\noindent\textbullet\quad \textbf{Open/closed in the line.}
	With $d(x,y)=|x-y|$ on $\mathbb R$, an interval of the form $(\alpha,\beta)$ is open, $[\alpha,\beta]$ is closed; a half-open interval like $(1,2]$ is neither open (no ball around $1$ stays inside) nor closed (its complement is not open).

	\par\noindent\textbullet\quad \textbf{Discrete metric.}
	The discrete metric is $d(x,y)=\mathbf 1_{x\ne y}$. Then every singleton $\{x\}$ is open; hence \emph{every subset of $X$ is open and also closed}. Compact subsets are exactly the finite subsets (an infinite discrete space is not compact). A sequence in $X$ is Cauchy iff it is eventually constant (for $\varepsilon=\tfrac12$). Every function $f:X\to Y$ is continuous (domain is discrete). For maps into a discrete space, $f:Y\to X$ is continuous iff for each $x\in X$, the fibre $f^{-1}(\{x\})$ is open in $Y$ (equivalently, $f$ is \emph{locally constant}; in particular, if $Y$ is connected then $f$ is constant).

With the usual metric $d(x,y)=|x-y|$:

\par\noindent\textbullet\quad In $\mathbb R$, $(1,2]$ is neither open nor closed:
it is not open because the point $2\in(1,2]$ has no $\varepsilon$-ball contained in $(1,2]$;
it is not closed because $1$ is a limit point (e.g. $1+1/n\to1$) not belonging to the set.

	\par\noindent\textbullet\quad As a subspace of $[0,2]$, $(1,2]$ is both open ($[0,2]\cap (1,\infty)$) and closed (complement $[0,1]$ is open in $[0,2]$).
\par\noindent\textbullet\quad As a subspace of $(1,3)$, the set $(1,2]$ is \emph{closed} because it can be written as the
intersection of the subspace with a closed subset of $\mathbb{R}$:
\[
(1,2]=(1,3)\cap(-\infty,2].
\]
Since $(-\infty,2]$ is closed in $\mathbb{R}$, the intersection is closed in the subspace $(1,3)$.
Equivalently, the complement $(1,3)\setminus(1,2]=(2,3)$ is open in $(1,3)$ (it is $(1,3)\cap(2,\infty)$),
so $(1,2]$ is closed but not open in the subspace.

	\par\noindent\textbullet\quad In the space $(1,2]$ itself, it is clopen (the whole space).

If $X$ has the discrete metric $d(x,y)=\mathbf 1_{x\ne y}$ and $Y$ is any metric space, then:

	\par\noindent\textbullet\quad Every subset of $X$ is open (hence also closed).
	\par\noindent\textbullet\quad The compact subsets of $X$ are exactly the finite subsets.
	\par\noindent\textbullet\quad A sequence in $X$ is Cauchy iff it is eventually constant.
	\par\noindent\textbullet\quad Every function $f:X\to Y$ is continuous.
```

## CP-II-0269

- chapter line: 4364

```tex
\label{prob:cp-ii-0269}
Let $f(x) = \sqrt{x}$ on $E=[0,1]$.
		Here $E$ is compact and $f$ is continuous.
		By Heine--Cantor, $f$ is uniformly continuous, even though $f'(x)=\tfrac{1}{2\sqrt{x}}$ is unbounded near $0$.
```

## CP-II-0271

- chapter line: 4371

```tex
\label{prob:cp-ii-0271}
\par\noindent\textbullet\quad In metric spaces, $F$ is l.s.c.\ (resp.\ u.s.c.) iff for all $x_n\to x$,
		$\displaystyle F(x)\le\liminf_n F(x_n)$ (resp.\ $\displaystyle F(x)\ge\limsup_n F(x_n)$).

	Let $X$ be a Banach space.
```

## CP-II-0282

- chapter line: 4379

```tex
\label{prob:cp-ii-0282}
Diagonals and Equality Sets

Let $(X,\tau)$ and $(Y,\rho)$ be topological spaces with $(Y,\rho)$ Hausdorff.

	\par\medskip\noindent\textbf{Statement.}\
		Show that $\Delta=\{(y,y):y\in Y\}\subset Y\times Y$ is closed (product topology).
	\par

	\begin{proof}
		Let $(y_1,y_2)\in (Y\times Y)\setminus\Delta$, so $y_1\ne y_2$. Since $Y$ is Hausdorff, there exist disjoint open sets $U\ni y_1$ and $V\ni y_2$ with $U\cap V=\varnothing$. Then
		\[
		(y_1,y_2)\in U\times V \subset (Y\times Y)\setminus \Delta,
		\]
		because for any $(u,v)\in U\times V$ we cannot have $u=v$ (that would force $u\in U\cap V=\varnothing$). Hence $(Y\times Y)\setminus \Delta$ is open and $\Delta$ is closed.
	\end{proof}

	\begin{remark}
		The converse holds: $Y$ is Hausdorff if and only if $\Delta$ is closed in $Y\times Y$.
	\end{remark}

	\par\medskip\noindent\textbf{Statement.}\
		Let $f,g:X\to Y$ be continuous. Show that $E=\{x\in X:\ f(x)=g(x)\}$ is closed in $X$.
	\par

	\begin{proof}
		Consider $F=(f,g):X\to Y\times Y$, which is continuous in the product topology. Then
		\[
		E=F^{-1}(\Delta).
		\]
		By part (a), $\Delta$ is closed in $Y\times Y$, hence $E$ is the preimage of a closed set under a continuous map and is therefore closed in $X$.
	\end{proof}

		\par\noindent\textbullet\quad If $Y=\mathbb{R}$ and $f,g:X\to\mathbb{R}$ are continuous, then
		\[
		E=\{x:\ f(x)=g(x)\}=(f-g)^{-1}(\{0\}),
		\]
		which is closed since $\{0\}$ is closed and $f-g$ is continuous.
		\par\noindent\textbullet\quad On $X=\mathbb{R}$, $f(x)=x^3-1$ and $g(x)=x-1$ give $E=\{1\}$, a closed set.

	Let $Y=\{a,b\}$ with the indiscrete topology. Then $Y$ is not Hausdorff and $\Delta\subset Y\times Y$ is not closed. Take any space $X$ and a non-closed set $A\subset X$ (e.g.\ $X=\mathbb{R}$, $A=(0,1)$). Define
	\[
	f(x)\equiv a,\qquad
	g(x)=\begin{cases}
		a,& x\in A,\\
		b,& x\notin A.
	\end{cases}
	\]
	Every map into an indiscrete space is continuous, so $f,g$ are continuous. But
	$E=\{x:\ f(x)=g(x)\}=A$, which is not closed. Thus the Hausdorff hypothesis in (b) is essential.

	Let $X$ be a topological space and $\Delta_X=\{(x,x):x\in X\}\subseteq X\times X$ its diagonal.

		\par\noindent\textbullet\quad $X$ is \emph{Hausdorff} $\iff$ $\Delta_X$ is \emph{closed} in $X\times X$.
		\par\noindent\textbullet\quad $X$ has a \emph{$G_\delta$-diagonal} if there exist open sets $U_n\subseteq X\times X$ such that
		\[
		\Delta_X=\bigcap_{n=1}^\infty U_n .
		\]

		\par\noindent\textbullet\quad \textbf{Metric spaces have $G_\delta$-diagonals.}
		If $(X,d)$ is metric, the function $(x,y)\mapsto d(x,y)$ is continuous on $X\times X$, hence
		\[
		\Delta_X=\bigcap_{m=1}^{\infty}\bigl\{(x,y)\in X\times X: d(x,y)<1/m\bigr\}
		\]
		is a $G_\delta$ subset of $X\times X$.
		\par\noindent\textbullet\quad \textbf{First countable Hausdorff $\Rightarrow G_\delta$-diagonal.}
		If $X$ is Hausdorff and for each $x\in X$ there is a countable neighborhood base $\{B_n(x)\}_{n\in\mathbb{N}}$, then
		\[
		U_n=\bigcup_{x\in X} B_n(x)\times B_n(x)\qquad(n\in\mathbb{N})
		\]
		are open in $X\times X$ and $\Delta_X=\bigcap_{n} U_n$.
		\par\noindent\textbullet\quad \textbf{SneiderĂ˘â‚¬â„˘s Theorem (compact case).}
		A compact Hausdorff space $K$ is metrizable if and only if $\Delta_K$ is a $G_\delta$ in $K\times K$.

		\par\noindent\textbullet\quad $\mathbb{R}^n$ with its Euclidean topology: Hausdorff and metric $\Rightarrow$ $\Delta$ is closed and a $G_\delta$.
		\par\noindent\textbullet\quad Any compact metrizable space (e.g.\ the Cantor set, the $n$-torus $(S^1)^n$) has a $G_\delta$-diagonal.
		\par\noindent\textbullet\quad The Niemytzki (Moore) plane: Hausdorff and first countable, hence has a $G_\delta$-diagonal, but is not normal; consequently not metrizable.

		\par\noindent\textbullet\quad For uncountable $I$, the Tikhonoff cube $[0,1]^I$ is compact Hausdorff but not metrizable; hence by Sneider, $\Delta_{[0,1]^I}$ is \emph{not} a $G_\delta$ in $[0,1]^I\times[0,1]^I$.
		\par\noindent\textbullet\quad The indiscrete space on $\{a,b\}$ is not Hausdorff; $\Delta$ is not closed (and not $G_\delta$).
		\par\noindent\textbullet\quad The cofinite topology on an infinite set is $T_1$ but not Hausdorff; $\Delta$ is not closed (hence not $G_\delta$).
```

## CP-II-0286

- chapter line: 4463

```tex
\label{prob:cp-ii-0286}
— Smoothness and bounds for $\widehat f$ with compact support

Let $f\in L^1(\mathbb R^n)$ with $\operatorname{supp}f\subset B_R(0)$ for some $R>0$.
Show that $\widehat f\in C^\infty(\mathbb R^n)$ and that, for every multi-index $\alpha$,
\[
\sup_{\xi\in\mathbb R^n}\big|D_\xi^\alpha \widehat f(\xi)\big|
\;\le\; R^{|\alpha|}\,\|f\|_{L^1}.
\]
```

## CP-II-0291

- chapter line: 4475

```tex
\label{prob:cp-ii-0291}
— Distributions with zero derivative are constants

Suppose \(u\in\mathcal D'(\mathbb R)\) satisfies \(Du=0\). Show that there exists \(\lambda\in\mathbb C\) such that
\[
u[\phi]=\lambda\int_{\mathbb R}\phi(x)\,dx,\qquad\forall\,\phi\in\mathcal D(\mathbb R).
\]
\emph{(Extend the result to \(\mathbb R^n\) for \(n>1\)).}

The hypothesis \(Du=0\) means \(u[\phi']=0\) for all \(\phi\in\mathcal D(\mathbb R)\).
Fix \(\phi_0\in\mathcal D(\mathbb R)\) with \(\int_{\mathbb R}\phi_0=1\). For any \(\phi\in\mathcal D(\mathbb R)\), set \(c_\phi=\int_{\mathbb R}\phi\) and define
\[
\psi(x)=\int_{-\infty}^x\big(\phi(t)-c_\phi\phi_0(t)\big)\,dt.
\]
Then \(\psi\in\mathcal D(\mathbb R)\) and \(\psi'=\phi-c_\phi\phi_0\). Therefore
\[
u[\phi]=u[\psi']+c_\phi\,u[\phi_0]=c_\phi\,u[\phi_0]=\lambda\int_{\mathbb R}\phi,
\]
with \(\lambda:=u[\phi_0]\).

If \(D_j u=0\) for all \(j=1,\dots,n\), then \(u[\partial_j\phi]=0\) for all \(\phi\in\mathcal D(\mathbb R^n)\).
Choose \(\phi_0\in\mathcal D(\mathbb R^n)\) with \(\int\phi_0=1\).

 For any \(\phi\), write \(\phi=\nabla\cdot F+c_\phi\phi_0\) with \(c_\phi=\int\phi\) and \(F\in\mathcal D(\mathbb R^n;\mathbb C^n)\) such that \(\nabla\cdot F=\phi-c_\phi\phi_0\) (possible because the right-hand side has integral \(0\)).

 Then
\[
u[\phi]=u[\nabla\cdot F]+c_\phi\,u[\phi_0]=\lambda\int_{\mathbb R^n}\phi.
\]

If \(u\) is induced by \(f\in L^1_{\mathrm{loc}}(\mathbb R)\), then \(Du=0\) implies \(f' = 0\) in the distributional sense, hence \(f\) is a.e.\ constant and \(u[\phi]=\lambda\int\phi\).
By contrast, \(D\delta\ne0\), since \(D\delta[\phi]=-\phi'(0)\).

Let $X$ be a locally convex space over $\mathbb K$ and let $X'$ denote its continuous dual.
The weak-$^\ast$ topology on $X'$, denoted $\sigma(X',X)$, is the coarsest topology on $X'$ for which every evaluation map
\[
e_x:X'\to\mathbb K,\qquad e_x(f)=f(x)\quad(x\in X),
\]
is continuous. Equivalently, it is the initial topology induced by the family $\{e_x:x\in X\}$.

\bigskip

A net $(f_\alpha)\subset X'$ converges to $f\in X'$ in $\sigma(X',X)$ if and only if
\[
f_\alpha(x)\longrightarrow f(x)\qquad\text{for every }x\in X.
\]

\smallskip

For $x\in X$ and an open set $U\subset\mathbb K$, the sets
\[
e_x^{-1}(U)=\{\,f\in X':\ f(x)\in U\,\}
\]
form a subbasis. A typical $0$-neighborhood is
\[
V(x_1,\dots,x_m;\varepsilon)
=\bigl\{\,f\in X':\ |f(x_j)|<\varepsilon\ \text{for }j=1,\dots,m\,\bigr\}.
\]

\smallskip

If $X$ is normed, the closed unit ball of $X'$ is compact in $\sigma(X',X)$ (Banach--Alaoglu).
If $X$ is separable, the weak-$^\ast$ topology is metrizible on norm-bounded subsets of $X'$.
The weak topology on $X$ is $\sigma(X,X')$, while the weak-$^\ast$ topology on $X'$ is $\sigma(X',X)$.
The canonical embedding $J:X\to X''$ is weak-to-weak-$^\ast$ continuous; it is onto if and only if $X$ is reflexive.

\smallskip

For $X=\ell^1$ and $X'=\ell^\infty$, $\sigma(\ell^\infty,\ell^1)$ is pointwise convergence on $\ell^1$:
$y^{(\alpha)}\to y$ iff $\sum_k y^{(\alpha)}_k x_k\to\sum_k y_k x_k$ for all $x\in\ell^1$.

For $X=C_0(\Omega)$ (locally compact Hausdorff), $X'=M(\Omega)$; the topology $\sigma(M(\Omega),C_0(\Omega))$
is narrow convergence of measures: $\int f\,d\mu_\alpha\to\int f\,d\mu$ for all $f\in C_0(\Omega)$.

For distributions, $\sigma(\mathcal D'(\mathbb R^n),\mathcal D(\mathbb R^n))$ and
$\sigma(\mathcal S'(\mathbb R^n),\mathcal S(\mathbb R^n))$ coincide with test-functionwise convergence.
```

## CP-II-0293

- chapter line: 4554

```tex
\label{prob:cp-ii-0293}
A sequence $(x_i)\subset\mathbb{R}^n$ is Cauchy if $\forall\varepsilon>0\,\exists N:\ i,j\ge N\Rightarrow \|x_i-x_j\|<\varepsilon$.

\renewcommand\labelenumi{(\alph{enumi})}
\par\noindent\textbullet\quad If $x_i\to x$, then $(x_i)$ is Cauchy. \textit{Proof.} Triangle inequality with $\varepsilon/2$.
\par\noindent\textbullet\quad If $(x_i)$ is Cauchy, then it is bounded. \textit{Proof.} Take $\varepsilon=1$.
\par\noindent\textbullet\quad Every Cauchy sequence in $\mathbb{R}^n$ converges. \textit{Proof.} Bounded $\Rightarrow$ has a convergent subsequence; use Cauchy property to pass to the full sequence.

\textbf{Remark.} In $\mathbb{R}$, $\mathbb{R}^n$, and $\mathbb{C}\cong\mathbb{R}^2$, a sequence is convergent iff it is Cauchy (completeness). In incomplete spaces (e.g.\ $\mathbb{Q}$), Cauchy does not imply convergent.
```

## CP-II-0297

- chapter line: 4566

```tex
\label{prob:cp-ii-0297}
\par\noindent\textbullet\quad If one takes $f_n(x)=\mathbf 1_{[0,1]}(x-n)$, it also works;
		all translations of the same shape have $\|f_n\|_1=1$ and no weak limit.

	Let $X$ be a topological space and $F:X\to(-\infty,+\infty]$.
```

## CP-II-0300

- chapter line: 4601

```tex
\label{prob:cp-ii-0300}
Let $K_1 \supset K_2 \supset K_3 \supset \cdots$ be a decreasing sequence of non-empty,
	connected, compact subsets of a Hausdorff space $X$.
	Let
	\[
	K = \bigcap_{n=1}^{\infty} K_n.
	\]

		\par\noindent\textbullet\quad Show that $K$ is non-empty.
		\par\noindent\textbullet\quad Show that $K$ is connected.
		\par\noindent\textbullet\quad Give an example with $X=\mathbb{R}^2$ showing that part (b)
		fails if the $K_n$ are only closed instead of compact.


	\textbf{Theory.}
	In any Hausdorff space, the intersection of a decreasing sequence
	of non-empty compact sets is non-empty (finite intersection property).
	Connectedness is preserved under nested intersections of connected sets.
	Compactness is required for non-emptiness; without it, closed sets
	may shrink or split into disconnected limits.


	\textbf{Solutions.}

	\textit{(a) Non-emptiness.}
	Each $K_n$ is compact and non-empty, $K_{n+1}\subseteq K_n$.
	Thus the family $\{K_n\}$ has the finite intersection property.
	By compactness, $\bigcap_n K_n \neq \varnothing$.

	\medskip

	\textit{(b) Connectedness.}
	Assume $K=A\cup B$ with $A,B$ non-empty and disjoint, open in $K$.
	Then $A=U\cap K$, $B=V\cap K$ for some disjoint open $U,V\subset X$.
	For each $n$, $K_n=(K_n\cap U)\cup(K_n\cap V)$.
	Since $K_n$ is connected, one of these intersections is empty for all $n$.
	Hence one of $A,B$ is empty—contradiction. So $K$ is connected.

	\medskip

	\textit{(c) Failure without compactness.}
	Let $X=\mathbb{R}^2$ and define
	\[
	L_n=\{(x,y):y=\tfrac{1}{n}x,\ x>0\}
	\cup
	\{(x,y):y=-\tfrac{1}{n}x,\ x>0\}.
	\]
	Each $L_n$ is closed in $\mathbb{R}^2$ and connected.
	They form a decreasing sequence, but
	\[
	\bigcap_n L_n = \{(x,0):x>0\},
	\]
	which is disconnected in $\mathbb{R}^2$.
	Thus compactness (not mere closedness) is essential.


	\textbf{Summary.}

	\begin{center}
		\resizebox{\linewidth}{!}{%
		\begin{tabular}{c|l|c|l}
			Part & Statement & Result & Key Idea\\\hline
			(a) & $K$ non-empty & Yes & Nested compact sets $\Rightarrow$ finite intersection property\\
			(b) & $K$ connected & Yes & Intersection preserves connectedness\\
			(c) & Closed instead of compact & No & May lose connectedness (counterexample in $\mathbb{R}^2$)
		\end{tabular}}
	\end{center}

	\par\medskip\noindent\textbf{Problem 8 — Antipodal Points on the Circle (Borsuk–Ulam in 1D)}\par
```

## CP-II-0303

- chapter line: 4712

```tex
\label{prob:cp-ii-0303}
— Compactness and sequential compactness in $C[0,1]$

Let $C[0,1]$ be the metric space consisting of all continuous functions $f:[0,1]\to\mathbb{R}$,
with distance
\[
d(f,g)=\sup_{x\in[0,1]}|f(x)-g(x)|.
\]

\bigskip

Let $h(x)=|f(x)-g(x)|$. Since $h$ is continuous on the compact interval $[0,1]$,
the Extreme Value Theorem ensures that $h$ attains its maximum and minimum values.
Therefore
\[
d(f,g)=\sup_{x\in[0,1]}|f(x)-g(x)|=\max_{x\in[0,1]}|f(x)-g(x)|.
\]

\bigskip

Let
\[
X=\{\, f\in C[0,1] : f([0,1])\subseteq[0,1]\,\}.
\]
Consider the sequence $f_n(x)=x^n$ for $x\in[0,1]$.
Each $f_n$ lies in $X$ because $x^n\in[0,1]$ for $x\in[0,1]$.

For any fixed $x\in[0,1)$, $f_n(x)=x^n\to 0$, while $f_n(1)=1$.
Hence $f_n$ converges pointwise to
\[
f(x)=
\begin{cases}
	0, & 0\le x<1,\\[3pt]
	1, & x=1,
\end{cases}
\]
which is discontinuous at $x=1$.

Since the limit function is not continuous, the convergence cannot be uniform.
No subsequence can converge uniformly either (every subsequence has the same pointwise limit).
Thus $(f_n)$ has no convergent subsequence in $C[0,1]$ under $d(f,g)=\|f-g\|_\infty$.

Therefore $X$ is not sequentially compact.

\bigskip

In metric spaces, compactness $\Leftrightarrow$ sequential compactness,
so $X$ is not compact. Nevertheless, we can give an explicit open cover with no finite subcover.

For each $n\in\mathbb{N}$, define
\[
U_n = \{\, f\in X : f(1) > 1 - \tfrac{1}{n} \,\}.
\]
Each $U_n$ is open in the sup-norm topology.
The collection $\{U_n : n\in\mathbb{N}\}$ covers $X$, since for every $f\in X$,
$f(1)\in[0,1]$ so $f(1)>1-1/n$ for some $n$.

However, no finite subcollection covers $X$.
If $U_{n_1},\dots,U_{n_k}$ are finitely many, let $N=\max\{n_i\}$.
Then the constant function $f(x)\equiv 1-\tfrac{1}{2N}$ lies in $X$ but satisfies
$f(1)=1-\tfrac{1}{2N}<1-\tfrac{1}{N}$, hence $f\notin U_N$.
Thus this cover has no finite subcover.

\bigskip

	\par\noindent\textbullet\quad The sequence $f_n(x)=x^n$ is a classical example in $C[0,1]$ showing failure of compactness.
	\par\noindent\textbullet\quad The family $X$ is bounded and closed but not equicontinuous; by the Arzelà–Ascoli theorem it is not relatively compact.
	\par\noindent\textbullet\quad $C[0,1]$ with $\|\cdot\|_\infty$ is complete but infinite-dimensional, hence non-compact.

\noindent\textbf{Definitions.}
For $S\subset\mathbb{R}$:

	\par\noindent\textbullet\quad The \emph{maximum} $\max S$ is a number $m\in S$ with $s\le m$ for all $s\in S$.
	\par\noindent\textbullet\quad The \emph{supremum} $\sup S$ is the least upper bound: the smallest $\alpha\in\mathbb{R}$ such that $s\le \alpha$ for all $s\in S$.

If $\max S$ exists, then $\sup S=\max S$. The supremum need not belong to $S$.

\smallskip

\noindent\textbf{Examples.}

	\par\noindent\textbullet\quad $S=(0,1)$: $\sup S=1$ but $\max S$ does not exist (1 is not in $S$).
	\par\noindent\textbullet\quad $S=[0,1]$: $\sup S=\max S=1$ (attained).
	\par\noindent\textbullet\quad $S=\{1-\tfrac1n:n\in\mathbb{N}\}$: $\sup S=1$, no maximum (1 is only a limit point).
	\par\noindent\textbullet\quad $S=\{0,1,2,\dots,100\}$: $\sup S=\max S=100$.
	\par\noindent\textbullet\quad $S=(-\infty,0)$: $\sup S=0$, no maximum.

\smallskip

\noindent\textbf{For functions.}
If $f:[a,b]\to\mathbb{R}$ is continuous and $[a,b]$ is compact, then by the Extreme Value Theorem
\[
\sup_{x\in[a,b]} f(x) \;=\; \max_{x\in[a,b]} f(x).
\]
If the domain is not compact, or $f$ is not continuous, the supremum may fail to be attained:

	\par\noindent\textbullet\quad $f(x)=x$ on $(0,1)$: $\sup f=1$ but $f$ has no maximum.
	\par\noindent\textbullet\quad $f(x)=\sin x$ on $\bigl(-\tfrac{\pi}{2},\tfrac{\pi}{2}\bigr)$: $\sup f=1$ but no maximum (endpoints excluded).

\smallskip

\noindent\textbf{Application to $C[0,1]$.}
For $f,g\in C[0,1]$, the function $h(x)=|f(x)-g(x)|$ is continuous on the compact interval $[0,1]$.
Hence
\[
\sup_{x\in[0,1]} |f(x)-g(x)| \;=\; \max_{x\in[0,1]} |f(x)-g(x)|.
\]

\noindent\textbf{Statement.}
Let $K\subset\mathbb{R}^n$ be compact and let $f:K\to\mathbb{R}$ be continuous.
Then there exist points $x_{\min},x_{\max}\in K$ such that
\[
f(x_{\min})=\min_{x\in K} f(x), \qquad f(x_{\max})=\max_{x\in K} f(x).
\]
Equivalently,
\[
\sup_{x\in K} f(x)=\max_{x\in K} f(x), \qquad \inf_{x\in K} f(x)=\min_{x\in K} f(x).
\]

\smallskip

\noindent\textbf{Proof sketch.}
Let $M=\sup_{x\in K} f(x)$. Choose $x_n\in K$ with $f(x_n)\to M$.
By compactness, some subsequence $x_{n_k}\to x^*\in K$.
By continuity, $f(x^*)=\lim_{k\to\infty} f(x_{n_k})=M$, so the supremum is attained.
Apply the same argument to $-f$ to get a minimum.

\smallskip

\noindent\textbf{Why the hypotheses are needed.}

	\par\noindent\textbullet\quad If the domain is not compact, even continuous functions may fail to attain extrema:
	$f(x)=x$ on $(0,1)$ has $\sup=1$ but no maximum.
	\par\noindent\textbullet\quad If $f$ is not continuous, attainment can fail even on compact sets (pathologies exist).

\bigskip

For $f,g\in C[0,1]$,

 set $h(x)=|f(x)-g(x)|$.

Then $h$ is continuous on the compact interval $[0,1]$.
By the EVT,
\[
\sup_{x\in[0,1]} |f(x)-g(x)| \;=\; \max_{x\in[0,1]} |f(x)-g(x)|.
\]
Hence the metric $d(f,g)=\sup_{x\in[0,1]}|f(x)-g(x)|$ is the maximum value of $|f-g|$ on $[0,1]$.

Let $X=\{f\in C[0,1]: 0\le f(x)\le 1 \text{ for all }x\in[0,1]\}$ with the sup norm.

\smallskip

\noindent\textbf{Define the cover.}
For each $n\in\mathbb{N}$ set
\[
U_n=\bigl\{\,f\in X:\ f(1)>1-\tfrac1n\,\bigr\}.
\]

\noindent\emph{$U_n$ is open.}
The evaluation functional $E_1:C[0,1]\to\mathbb{R}$, $E_1(f)=f(1)$, is continuous since
$|E_1(f)-E_1(g)|=|f(1)-g(1)|\le \|f-g\|_\infty$.
Thus $U_n=E_1^{-1}\bigl((1-\tfrac1n,\infty)\bigr)$ is open.

\smallskip

\noindent\emph{$\{U_n\}_{n\in\mathbb{N}}$ covers $X$.}
If $f\in X$ then $f(1)\in[0,1]$, hence there exists $n$ with $1-\tfrac1n<f(1)$, i.e.\ $f\in U_n$.

\smallskip

\noindent\textbf{No finite subcover.}
Given finitely many $U_{n_1},\dots,U_{n_k}$, let $N=\max\{n_1,\dots,n_k\}$ and consider
the constant function $f_N(x)\equiv 1-\tfrac{1}{2N}$.
Then $f_N\in X$ but
\[
f_N(1)=1-\tfrac{1}{2N}\le 1-\tfrac1N,
\]
so $f_N\notin U_N$, hence $f_N$ is not contained in the finite union $U_{n_1}\cup\cdots\cup U_{n_k}$.
Therefore no finite subcollection covers $X$.

\smallskip

Consequently, $X$ is not compact.

For $f:\mathbb{R}\to\mathbb{R}$ and $q\in\mathbb{R}$, the \emph{fiber} (level set) at $q$ is
\[
f^{-1}(q)=\{x\in\mathbb{R}:\ f(x)=q\}.
\]
A \emph{rational fiber} means $q\in\mathbb{Q}$.

\smallskip

\noindent\textbf{Key mechanism (with IVP).}
Assume $f$ has the intermediate value property and that each rational fiber $f^{-1}(q)$ is closed.
Fix $q\in\mathbb{Q}$. Then the sublevel and superlevel sets
\[
U_q=f^{-1}((-\infty,q)),\qquad V_q=f^{-1}((q,\infty))
\]
are open. Indeed, if $x_0\in U_q$ but every neighborhood of $x_0$ contains points with values $\ge q$,
the IVP forces points with value exactly $q$ arbitrarily close to $x_0$, hence $x_0\in\overline{f^{-1}(q)}$.
Since $f^{-1}(q)$ is closed, $x_0\in f^{-1}(q)$, contradicting $f(x_0)<q$.
Thus $U_q$ is open; similarly $V_q$ is open.

\smallskip

For rationals $r<s$,
\[
f^{-1}((r,s))=V_r\cap U_s
\]
is open. Because intervals with rational endpoints form a base of $\mathbb{R}$,
the preimage of every open set is open; hence $f$ is continuous.

\bigskip

\noindent\textbf{Examples.}

	\par\noindent\textbullet\quad \emph{IVP but some rational fiber not closed (discontinuous):}
	$f(x)=\sin(1/x)$ for $x\ne 0$, $f(0)=0$. For $q=\tfrac12$, $f^{-1}(q)$ accumulates at $0$ but does not contain $0$.
	\par\noindent\textbullet\quad \emph{Closed rational fibers but no IVP (discontinuous):}
	$f(x)=\mathbf{1}_{[0,\infty)}(x)$. Fibers at $q=0,1$ are closed; others are empty (closed). Yet $f$ is discontinuous at $0$.
	\par\noindent\textbullet\quad \emph{Continuous:} any continuous $f$ has all fibers $f^{-1}(q)$ closed for every $q\in\mathbb{R}$ and satisfies IVP.
```

## CP-II-0304

- chapter line: 4936

```tex
\label{prob:cp-ii-0304}
(Fourier transform of a compactly supported $L^1$ function)

Suppose $f \in L^{1}(\mathbb{R}^{n})$ with $\operatorname{supp} f \subset B_{R}(0)$ for some $R>0$.

	\par\noindent\textbullet\quad Show that $\widehat{f} \in C^{\infty}(\mathbb{R}^{n})$ and that for any multi–index $\alpha$,
	\[
	\sup_{\xi \in \mathbb{R}^{n}} \left| D^{\alpha} \widehat{f}(\xi) \right|
	\le R^{|\alpha|} \, \|f\|_{L^{1}(\mathbb{R}^{n})}.
	\]

	\par\noindent\textbullet\quad Show that $\widehat{f}$ is real analytic, with an infinite radius of convergence, i.e.
	\[
	\widehat{f}(\xi)
	= \sum_{\alpha} \frac{D^{\alpha} \widehat{f}(0)}{\alpha!} \, \xi^{\alpha}
	\qquad \text{for all } \xi \in \mathbb{R}^{n}.
	\]

	\par\noindent\textbullet\quad Show that if $\widehat{f}(\xi)$ vanishes on an open set, then it must vanish everywhere.
	\hfill\textit{(Hint: use part (i) of Lemma 3.2.)}

You may assume the following version of Taylor's theorem: if $g \in C^{k+1}(B_{r}(0))$, then for $x \in B_{r}(0)$,
\[
g(x)
= \sum_{|\alpha|\le k} D^{\alpha} g(0)\,\frac{x^{\alpha}}{\alpha!}
+ \sum_{|\beta| = k+1} R_{\beta}(x)\,x^{\beta},
\]
where the remainder satisfies
\[
|R_{\beta}(x)|
\le \frac{1}{\beta!}
\max_{|\alpha|=|\beta|}
\max_{y\in B_{r}(0)} |D^{\alpha} g(y)|.
\]

Suppose $f\in L^1(\mathbb{R}^n)$, with $\mathrm{supp}\,f\subset B_R(0)$ for some $R>0$,
and define
\[
\widehat f(\xi):=\int_{\mathbb{R}^n} e^{-2\pi i x\cdot \xi} f(x)\,dx.
\]

We first show that $\widehat f\in C^\infty(\mathbb{R}^n)$ and that, for any
multi-index $\alpha$,
\[
\sup_{\xi\in\mathbb{R}^n}\big|D^\alpha \widehat f(\xi)\big|
\le R^{|\alpha|}\,\|f\|_{L^1(\mathbb{R}^n)}.
\]

\emph{Proof.}
Because $f$ has compact support, for each multi-index $\alpha$ we may differentiate
under the integral sign:
\[
D^\alpha_\xi \widehat f(\xi)
= \int_{\mathbb{R}^n} D^\alpha_\xi\!\big(e^{-2\pi i x\cdot \xi}\big) f(x)\,dx
= \int_{\mathbb{R}^n} (-2\pi i x)^\alpha e^{-2\pi i x\cdot \xi} f(x)\,dx.
\]
Hence
\[
|D^\alpha \widehat f(\xi)|
\le \int_{\mathbb{R}^n} |x^\alpha|\,|f(x)|\,dx.
\]
On the support of $f$ we have $|x_k|\le R$ for each coordinate, so
$|x^\alpha|\le R^{|\alpha|}$. Therefore
\[
|D^\alpha \widehat f(\xi)|
\le R^{|\alpha|} \int_{\mathbb{R}^n}|f(x)|\,dx
= R^{|\alpha|}\,\|f\|_{L^1(\mathbb{R}^n)},
\]
and this upper bound is independent of $\xi$. Thus
\[
\sup_{\xi\in\mathbb{R}^n}|D^\alpha\widehat f(\xi)|
\le R^{|\alpha|}\,\|f\|_{L^1}.
\]
Since each derivative is obtained as an $L^1$–limit under the integral,
$D^\alpha\widehat f$ is continuous, and hence $\widehat f\in C^\infty(\mathbb{R}^n)$.


We show that $\widehat f$ is real analytic with infinite radius of convergence, i.e.
\[
\widehat f(\xi) = \sum_{\alpha} \frac{D^\alpha \widehat f(0)}{\alpha!}\,\xi^\alpha
\qquad\text{for all }\xi\in\mathbb{R}^n.
\]

\emph{Proof.}
Apply the multivariable Taylor theorem to
\[
g(\xi):=\widehat f(\xi)
\]
at the point $0\in\mathbb{R}^n$. For $x\in B_r(0)$ we have
\[
\widehat f(x)
= \sum_{|\alpha|\le k} D^\alpha \widehat f(0)\,\frac{x^\alpha}{\alpha!}
+ \sum_{|\beta|=k+1} R_\beta(x)\,x^\beta,
\]
where each remainder term satisfies
\[
|R_\beta(x)|
\le \frac{1}{\beta!}
\max_{|\gamma|=|\beta|}
\max_{y\in B_r(0)} |D^\gamma \widehat f(y)|.
\]
Using the estimate from part (a) we obtain
\[
|R_\beta(x)|
\le \frac{1}{\beta!}\,R^{|\beta|}\,\|f\|_{L^1}.
\]
Hence, for $|x|<r$,
\[
\begin{aligned}
	\left|\sum_{|\beta|=k+1} R_\beta(x)\,x^\beta\right|
	&\le \sum_{|\beta|=k+1}
	\frac{R^{|\beta|}\|f\|_{L^1}}{\beta!}\,|x|^{|\beta|} \\
	&\le \|f\|_{L^1}
	\sum_{m=k+1}^\infty \frac{(C R|x|)^m}{m!},
\end{aligned}
\]
where $C>0$ depends only on the dimension (via the number of multi-indices of
length $m$). The last sum is the tail of an exponential series and therefore
tends to $0$ as $k\to\infty$, for every $x\in\mathbb{R}^n$ (no restriction on $|x|$).

Letting $k\to\infty$ we conclude that
\[
\widehat f(\xi)
= \sum_{\alpha} \frac{D^\alpha \widehat f(0)}{\alpha!}\,\xi^\alpha
\qquad\text{for all }\xi\in\mathbb{R}^n,
\]
so $\widehat f$ is real analytic with infinite radius of convergence.


Suppose that $\widehat f(\xi)=0$ for all $\xi$ in some nonempty open set
$\Omega\subset\mathbb{R}^n$. Choose $\xi_0\in\Omega$ and let $B_r(\xi_0)\subset\Omega$ be
a ball contained in $\Omega$. On $B_r(\xi_0)$ we have $\widehat f\equiv 0$, and hence,
for every multi-index $\alpha$,
\[
D^\alpha \widehat f(\xi_0)=0.
\]

By part (b), the Taylor expansion of $\widehat f$ at $\xi_0$ has infinite radius of
convergence:
\[
\widehat f(\xi)
= \sum_{\alpha} \frac{D^\alpha \widehat f(\xi_0)}{\alpha!}\,
(\xi-\xi_0)^\alpha
\qquad\text{for all }\xi\in\mathbb{R}^n.
\]
Since all derivatives at $\xi_0$ vanish, every coefficient in this series is zero,
and consequently $\widehat f(\xi)=0$ for all $\xi\in\mathbb{R}^n$.

Thus, if $\widehat f$ vanishes on any nonempty open set, it must vanish identically.


In one dimension, let
\[
f(x) = \mathbf{1}_{[-1,1]}(x).
\]
Then $f\in L^{1}(\mathbb{R})$ and $\mathrm{supp}\,f\subset[-1,1]=B_{1}(0)$, so $R=1$
and $\|f\|_{L^{1}}=2$. With the Fourier transform
\[
\widehat{f}(\xi)
= \int_{\mathbb{R}} e^{-2\pi i x\xi} f(x)\,dx,
\]
we compute
\[
\widehat{f}(\xi)
= \int_{-1}^{1} e^{-2\pi i x\xi}\,dx
= \frac{\sin(2\pi\xi)}{\pi\xi},
\]
where $\widehat{f}(0)$ is defined by continuity, giving $\widehat{f}(0)=2$.

For any $k\in\mathbb{N}$ we have
\[
\widehat{f}^{(k)}(\xi)
= \int_{-1}^{1} (-2\pi i x)^{k} e^{-2\pi i x\xi}\,dx,
\]
so that
\[
\big|\widehat{f}^{(k)}(\xi)\big|
\le \int_{-1}^{1} |2\pi x|^{k}\,dx
\le (2\pi)^{k} \int_{-1}^{1} |x|^{k}\,dx
\le (2\pi)^{k} \cdot 2.
\]
This is of the form
\[
\sup_{\xi\in\mathbb{R}} \big|\widehat{f}^{(k)}(\xi)\big|
\le C^{k} \|f\|_{L^{1}},
\]
and illustrates the bound from part (a) of Exercise~3.7 with $R=1$.

Around $\xi=0$ we expand
\[
e^{-2\pi i x\xi} = \sum_{m=0}^{\infty}
\frac{(-2\pi i x\xi)^{m}}{m!},
\]
and since $|x|\le 1$ on the support of $f$, we may integrate term-by-term:
\[
\widehat{f}(\xi)
= \sum_{m=0}^{\infty} \frac{(-2\pi i \xi)^{m}}{m!}
\int_{-1}^{1} x^{m}\,dx.
\]
The inner integral is
\[
\int_{-1}^{1} x^{m}\,dx
=
\begin{cases}
	0, & m \text{ odd},\\[0.3em]
	\dfrac{2}{m+1}, & m \text{ even},
\end{cases}
\]
so
\[
\widehat{f}(\xi)
= \sum_{k=0}^{\infty}
\frac{(-2\pi i \xi)^{2k}}{(2k)!}\,\frac{2}{2k+1}.
\]
This is a power series in $\xi$ which converges for all $\xi\in\mathbb{R}$, and
precisely recovers $\widehat{f}(\xi)=\sin(2\pi\xi)/(\pi\xi)$. It is a concrete
instance of the statement in part (b) that $\widehat{f}$ is real analytic with
infinite radius of convergence.

Note also that $\widehat{f}(\xi)$ has only isolated zeros (at $\xi=k/2$,
$k\in\mathbb{Z}\setminus\{0\}$), so it does \emph{not} vanish on any nonempty
open interval. This is consistent with part (c): if $\widehat{f}$ vanished on an
open set, analyticity would force all derivatives at a point of that set to be
zero and hence $\widehat{f}\equiv 0$.

Let
\[
f(x)=
\begin{cases}
	e^{-\frac{1}{1-x^{2}}}, & |x|<1,\\[0.3em]
	0, & |x|\ge 1 ,
\end{cases}
\qquad f\in C^\infty_c(\mathbb{R}),\ \mathrm{supp}(f)\subset[-1,1].
\]
Its Fourier transform is
\[
\widehat{f}(\xi)
= \int_{-1}^{1} e^{-2\pi i x\xi}\, e^{-\frac{1}{1-x^{2}}}\,dx,
\]
which does not admit a simple closed form, but it satisfies all conclusions of Exercise~3.7:

	\par\noindent (a)\quad \textbf{Differentiating under the integral.}
	For every integer $k\ge0$,
	\[
	\widehat{f}^{(k)}(\xi)
	= \int_{-1}^{1} (-2\pi i x)^{k} e^{-2\pi i x\xi}\, e^{-\frac{1}{1-x^{2}}}\,dx.
	\]
	Since $|x|\le 1$,
	\[
	\big|\widehat{f}^{(k)}(\xi)\big|
	\le \int_{-1}^{1} |2\pi x|^{k} e^{-\frac{1}{1-x^{2}}}\,dx
	\le C^{k}\,\|f\|_{L^{1}},
	\qquad
	\sup_{\xi\in\mathbb{R}}\big|\widehat{f}^{(k)}(\xi)\big| <\infty.
	\]
	This matches exactly the estimate
	\[
	\sup_{\xi\in\mathbb{R}^{n}} |D^\alpha \widehat{f}(\xi)|
	\le R^{|\alpha|}\,\|f\|_{L^{1}},
	\qquad R=1.
	\]

	\par\noindent (b)\quad \textbf{Real analyticity.}
	Expanding the exponential,
	\[
	e^{-2\pi i x\xi}
	= \sum_{m=0}^{\infty} \frac{(-2\pi i x\xi)^{m}}{m!},
	\]
	and since $|x|\le 1$ on $\operatorname{supp}(f)$, the series converges absolutely for all $\xi$.
	Thus the integral may be computed term-by-term:
	\[
	\widehat{f}(\xi)
	= \sum_{m=0}^{\infty}
	\frac{(-2\pi i\xi)^{m}}{m!}
	\int_{-1}^{1} x^{m}\, e^{-\frac{1}{1-x^{2}}}\,dx.
	\]
	This is a power series in $\xi$ with infinite radius of convergence, exactly as stated in Exercise~3.7(b).

	\par\noindent (c)\quad \textbf{Vanishing on an open set implies $\widehat{f}\equiv 0$.}
	If $\widehat{f}$ vanished on an open interval, real analyticity would force all derivatives
	at a point of that interval to vanish, making all coefficients in the Taylor series zero.
	Hence $\widehat{f}\equiv 0$.
	But
	\[
	\widehat{f}(0)=\int_{-1}^{1} f(x)\,dx >0,
	\]
	so this cannot happen for the bump function.
	This fully matches Exercise~3.7(c).
```

## CP-II-0309

- chapter line: 5227

```tex
\label{prob:cp-ii-0309}
s.

\par\noindent\textbullet\quad If \(\nu=\gamma\) is the Cantor measure, then \(\nu_a=0\) and \(\nu_s=\gamma\).

	Let $X$ be a topological space and $\mu$ a (Borel) measure on $X$.
	We say $\mu$ is \emph{locally finite} if every $x\in X$ has a neighborhood $U$
	with $\mu(U)<\infty$.
	Lebesgue measure on $\mathbb{R}^n$ and counting measure on a discrete space are locally finite.
	A measure that assigns $+\infty$ to every nonempty open set is not locally finite.

	\bigskip

	A Borel measure $\mu$ on a Hausdorff space $X$ is
	\emph{outer regular} if for every Borel set $A$,
	\[
	\mu(A)=\inf\{\mu(U): A\subset U,\ U\text{ open}\},
	\]
	and \emph{inner regular} if for every Borel set $A$,
	\[
	\mu(A)=\sup\{\mu(K): K\subset A,\ K\text{ compact}\}.
	\]
	A \emph{Radon measure} is a Borel measure that is locally finite, outer regular, and inner regular.
	Classical examples include Lebesgue measure on $\mathbb{R}^n$, surface measure on smooth manifolds,
	and counting measure on discrete locally compact spaces.

	\bigskip

	A \emph{topological group} is a group $G$ endowed with a Hausdorff topology such that
	multiplication $(g,h)\mapsto gh$ and inversion $g\mapsto g^{-1}$ are continuous.
	If $G$ is \emph{locally compact}, then there exists a nonzero Radon measure $\eta$
	(Haar measure) such that $\eta(gA)=\eta(A)$ for all Borel $A$ and all $g\in G$.
	Haar measure is unique up to a positive scalar multiple.
	If also $\eta(Ag)=\eta(A)$ for all $g$, then $G$ is \emph{unimodular}
	(e.g.\ all abelian, discrete, and compact groups).
	On $\mathbb{R}^n$, Haar measure coincides with Lebesgue measure.

	\bigskip

	For measures $\mu,\nu$ on $(X,\mathcal{B})$, we write $\nu\perp\mu$ if there exists
	$S\in\mathcal{B}$ with $\mu(S)=0$ and $\nu(X\setminus S)=0$.
	This is the measure-theoretic notion often called ``orthogonality'' of measures.
	Examples: $\delta_x\perp m$ on $\mathbb{R}^n$, and the Cantor measure $\gamma$ on $[0,1]$ satisfies $\gamma\perp m$.

	\bigskip

	On a locally compact Hausdorff space with a Radon reference measure $\mu$ (e.g.\ Haar measure on a group),
	any finite Borel measure $\nu$ decomposes uniquely as $\nu=\nu_a+\nu_s$ with $\nu_a\ll\mu$ and $\nu_s\perp\mu$.
	In particular, on $\mathbb{R}^n$ with $\mu=m$ (Lebesgue), the absolutely continuous part has the
	form $\nu_a=f\,m$ for some $f\in L^1(m)$, while $\nu_s$ is concentrated on an $m$-null set.

	Let $X$ be a topological space. The \emph{Borel $\sigma$-algebra} $\mathcal{B}(X)$
	is the smallest $\sigma$-algebra containing all open sets of $X$.
	Equivalently, $\mathcal{B}(X)$ is generated by the open sets (and hence contains
	all closed sets, $G_\delta$ and $F_\sigma$ sets, and all sets obtained from these
	by countable unions, intersections, and complements).

	\bigskip

	A measure $\mu$ defined on $\mathcal{B}(X)$ is called a \emph{Borel measure}.
	If, in addition, $\mu$ is \emph{locally finite} and both \emph{outer} and \emph{inner regular},
	then $\mu$ is a \emph{Radon measure}.

	\bigskip

	Given a Borel measure $\mu$, its \emph{completion} adds to the $\sigma$-algebra
	all subsets of $\mu$-null sets. Lebesgue measure on $\mathbb{R}^n$ is precisely
	the completion of a Borel measure (often called the Borel--Lebesgue measure).

	\bigskip
```

## CP-II-0310

- chapter line: 5300

```tex
\label{prob:cp-ii-0310}
Slices and a quotient of a product

Let $X,Y$ be topological spaces and endow $X\times Y$ with the product topology.

	\subsection*{(a) For each $y\in Y$, $X\times\{y\}\cong X$}
	Define
	\[
	i_y:X\to X\times\{y\},\quad i_y(x)=(x,y),
	\qquad
	p_y:X\times\{y\}\to X,\quad p_y(x,y)=x.
	\]
	Then $i_y$ is continuous (product of $\mathrm{id}_X$ with the constant map $y$),
	$p_y$ is the restriction of the continuous projection $\pi_X$, and
	\[
	p_y\circ i_y=\mathrm{id}_X,\qquad i_y\circ p_y=\mathrm{id}_{X\times\{y\}}.
	\]
	Hence $i_y$ is a homeomorphism $X\cong X\times\{y\}$.

	Define $(x,y)\sim(x',y')$ iff $x=x'$. Let $q:X\times Y\to (X\times Y)/\!\sim$ be the quotient map and
	$\pi_X:X\times Y\to X$ the first projection. Since $\pi_X$ is continuous and constant on $\sim$-classes,
	the universal property yields a unique continuous
	\[
	\tilde\pi:(X\times Y)/\!\sim \longrightarrow X \quad\text{such that}\quad \tilde\pi\circ q=\pi_X.
	\]

	Fix $y_0\in Y$ and define $s:X\to (X\times Y)/\!\sim$ by $s(x)=q(x,y_0)$.
	Then $s$ is continuous (it equals $q\circ i_{y_0}$).

	For $x\in X$, $\tilde\pi\circ s(x)=\tilde\pi(q(x,y_0))=\pi_X(x,y_0)=x$.
	For any $(x,y)\in X\times Y$ we have $(x,y)\sim(x,y_0)$, hence
	\[
	s\circ\tilde\pi\big(q(x,y)\big)=s(x)=q(x,y_0)=q(x,y).
	\]
	Thus $s=(\tilde\pi)^{-1}$ and $\tilde\pi$ is a homeomorphism.
	Therefore $(X\times Y)/\!\sim\ \cong X$.

	\begin{tikzcd}
		X\times Y \arrow[d, "q"'] \arrow[dr, "\pi_X"] & \\
		Q \arrow[r, "\tilde{\pi}"'] & X
	\end{tikzcd}

\medskip

\begin{tikzcd}
		X \arrow[r, "i_{y_0}"] \arrow[rr, bend right=20, "\mathrm{id}_X"'] &
		X\times Y \arrow[r, "q"] \arrow[dr, "\pi_X"'] &
		Q \arrow[d, "\tilde{\pi}"] \arrow[loop right, "s\circ\tilde{\pi}"'] \\
		& & X
	\end{tikzcd}

		\par\noindent\textbullet\quad $X=\mathbb{R}$, $Y=[0,1]$. For any $t\in[0,1]$, the map
		$i_t:\mathbb{R}\to \mathbb{R}\times\{t\}$, $x\mapsto(x,t)$,
		is a homeomorphism with inverse $(x,t)\mapsto x$.
		\par\noindent\textbullet\quad $X=S^1$, $Y=\mathbb{R}$. Each slice $S^1\times\{y\}$ is homeomorphic to $S^1$.
		\par\noindent\textbullet\quad $X=\{1,2,3\}$ (discrete), arbitrary $Y$. Each $\{1,2,3\}\times\{y\}$ is a 3--point discrete space $\cong X$.
		\par\noindent\textbullet\quad $X$ arbitrary, $Y$ non-Hausdorff (e.g.\ indiscrete). Still $X\times\{y\}\cong X$; the slice homeomorphism does not use separation axioms.

	Let $(x,y)\sim(x',y')$ iff $x=x'$ and assume $Y\neq\varnothing$.

		\par\noindent\textbullet\quad $X=\mathbb{R}$, $Y=[0,1]$. Each vertical segment $\{x\}\times[0,1]$ collapses to one point; the quotient is $\mathbb{R}$.
		\par\noindent\textbullet\quad $X=S^1$, $Y=\{0,1\}$. The two parallel circles collapse columnwise; the quotient is $S^1$.
		\par\noindent\textbullet\quad $X=\{1,2,3\}$ (discrete), $Y=\{a,b,c\}$. The $3\times3$ grid collapses each column to one point; the quotient is a 3--point discrete space $\cong X$.
		\par\noindent\textbullet\quad $X$ arbitrary, $Y$ indiscrete nonempty. Despite $X\times Y$ not being Hausdorff, the quotient by vertical fibers is homeomorphic to $X$ via the factorization of $\pi_X$.

	If $Y=\varnothing$ then $X\times Y=\varnothing$ and $(X\times Y)/\!\sim=\varnothing\not\cong X$ unless $X=\varnothing$.

	\section*{Problem 12: $\mathbb{R}^2/\mathbb{Z}^2$ is a torus}

	Let $\sim$ on $\mathbb{R}^2$ be given by
	\[
	(x,y)\sim(z,w)\quad\Longleftrightarrow\quad x-z\in\mathbb{Z}\ \text{ and }\ y-w\in\mathbb{Z}.
	\]
	Show that $\mathbb{R}^2/\!\sim$ is homeomorphic to the embedded torus
	\[
	T=\Bigl\{\bigl((2+\cos\theta)\cos\phi,\ (2+\cos\theta)\sin\phi,\ \sin\theta\bigr)\ :\ \theta,\phi\in[0,2\pi]\Bigr\}\subset\mathbb{R}^3.
	\]

	Define
	\[
	F:\mathbb{R}^2\longrightarrow S^1\times S^1,\qquad
	F(x,y)=\bigl(e^{2\pi i x},\,e^{2\pi i y}\bigr).
	\]
	Then:

		\par\noindent\textbullet\quad $F$ is continuous.
		\par\noindent\textbullet\quad $F$ is constant on $\sim$-classes (adding integers to $x$ or $y$ does not change the exponentials).

	Hence $F$ descends to a unique continuous
	\[
	\tilde F:\ \mathbb{R}^2/\!\sim\ \longrightarrow\ S^1\times S^1
	\quad\text{with}\quad
	\tilde F\circ q=F \ \ (q \text{ the quotient map}).
	\]

	Given $(u,v)\in S^1\times S^1$, choose arguments $u=e^{2\pi i x}$, $v=e^{2\pi i y}$.
	Different choices differ by integers, hence determine the same class. Therefore $\tilde F$ is bijective.

	$\mathbb{R}^2/\!\sim$ is compact (homeomorphic to $[0,1]^2$ with opposite edges identified), and $S^1\times S^1$ is Hausdorff.
	A continuous bijection from a compact space onto a Hausdorff space is a homeomorphism; thus $\tilde F$ is a homeomorphism.

	\par\medskip\noindent\textbf{Step 4 (embed into $\mathbb{R}^3$).}\quad
	Define
	\[
	\Phi: S^1\times S^1\to T,\qquad
	\Phi\bigl(e^{i\theta},e^{i\phi}\bigr)
	=\bigl((2+\cos\theta)\cos\phi,\ (2+\cos\theta)\sin\phi,\ \sin\theta\bigr).
	\]
	$\Phi$ is a homeomorphism onto $T$. Therefore
	\[
	\mathbb{R}^2/\!\sim\ \cong\ S^1\times S^1\ \cong\ T.
	\]

	\bigskip

	\par\medskip\noindent\textbf{Step 1 (define a $\mathbb{Z}^2$-periodic map).}\quad
	Set
	\[
	G:\mathbb{R}^2\to T,\qquad
	G(x,y)=\Bigl((2+\cos(2\pi x))\cos(2\pi y),\ (2+\cos(2\pi x))\sin(2\pi y),\ \sin(2\pi x)\Bigr).
	\]
	Then $G$ is continuous and satisfies $G(x+m,y+n)=G(x,y)$ for all $m,n\in\mathbb{Z}$, so $G$ is constant on $\sim$-classes and factors through a continuous
	\[
	\tilde G:\ \mathbb{R}^2/\!\sim\ \longrightarrow\ T.
	\]

	For any $(\theta,\phi)\in[0,2\pi]^2$, the point of $T$ with those angles equals
	\[
	G\!\left(\frac{\theta}{2\pi},\,\frac{\phi}{2\pi}\right).
	\]
	Changing $(\theta,\phi)$ by integer multiples of $2\pi$ changes $(x,y)$ by integers, i.e.\ stays in the same class.
	Thus $\tilde G$ is bijective.

	As above, $\mathbb{R}^2/\!\sim$ is compact and $T$ is Hausdorff (subspace of $\mathbb{R}^3$), hence the continuous bijection $\tilde G$ is a homeomorphism.

	\bigskip

		\par\noindent\textbullet\quad $\mathbb{R}/\mathbb{Z}\cong S^1$ (the 1-torus).
		\par\noindent\textbullet\quad $\mathbb{R}^n/\mathbb{Z}^n\cong (S^1)^n$ (the $n$-torus).
		\par\noindent\textbullet\quad Identifying only the $y$-coordinate modulo $\mathbb{Z}$ gives the cylinder $\mathbb{R}\times S^1$.

	\par\medskip\noindent\textbf{Description of the map $G:\mathbb{R}^2\to T$.}\quad
	Define
	\[
	G(x,y)=\Big((2+\cos(2\pi x))\cos(2\pi y),\ (2+\cos(2\pi x))\sin(2\pi y),\ \sin(2\pi x)\Big).
	\]

	Set
	\[
	\theta=2\pi x,\qquad \phi=2\pi y.
	\]
	Then
	\[
	G(x,y)=\bigl((2+\cos\theta)\cos\phi,\ (2+\cos\theta)\sin\phi,\ \sin\theta\bigr),
	\]
	which is the standard parametrization of the embedded torus $T\subset\mathbb{R}^3$
	with major radius $2$ and minor radius $1$.
	Here $\theta$ moves around the small circular cross--section (the ``tube''),
	producing the vertical coordinate $z=\sin\theta$ and the tube radius $1$,
	while $\phi$ rotates the cross--section around the $z$--axis; the distance from the
	$z$--axis is $2+\cos\theta$ and multiplying by $(\cos\phi,\sin\phi)$ sweeps the big circle.

	For every $(m,n)\in\mathbb{Z}^2$,
	\[
	G(x+m,y+n)=G(x,y),
	\]
	since only $2\pi x$ and $2\pi y$ appear in trigonometric functions.
	Thus $G$ is constant on cosets of $\mathbb{Z}^2$ in $\mathbb{R}^2$, i.e.\ on the equivalence
	classes for the relation $(x,y)\sim(x',y')\iff (x-x',y-y')\in\mathbb{Z}^2$.
	Let $q:\mathbb{R}^2\to\mathbb{R}^2/\mathbb{Z}^2$ be the quotient map.
	By the universal property of the quotient, there exists a unique continuous
	\[
	\tilde G:\ \mathbb{R}^2/\mathbb{Z}^2 \longrightarrow T \quad\text{such that}\quad \tilde G\circ q = G.
	\]

	Given any point of $T$ written as
	\[
	\bigl((2+\cos\theta)\cos\phi,\ (2+\cos\theta)\sin\phi,\ \sin\theta\bigr)
	\quad (\theta,\phi\in[0,2\pi]),
	\]
	choose $(x,y)=(\theta/2\pi,\ \phi/2\pi)\in\mathbb{R}^2$; then $G(x,y)$ equals that point.
	Different choices of $(\theta,\phi)$ differ by integer multiples of $2\pi$ and hence change
	$(x,y)$ by integers only; therefore they lie in the same class in $\mathbb{R}^2/\mathbb{Z}^2$.
	Consequently $\tilde G$ is bijective.

	The space $\mathbb{R}^2/\mathbb{Z}^2$ is compact (homeomorphic to the unit square $[0,1]^2$
	with opposite edges identified), and $T\subset\mathbb{R}^3$ is Hausdorff.
	Hence the continuous bijection $\tilde G:\mathbb{R}^2/\mathbb{Z}^2\to T$ is a homeomorphism.

	The relation $(x,y)\sim(x+m,y+n)$, $m,n\in\mathbb{Z}$, identifies opposite edges of the unit square
	$[0,1]^2$, producing the compact surface $[0,1]^2/\!\sim$ which is homeomorphic to $S^1\times S^1$,
	i.e.\ a (topological) torus. The set
	\[
	T=\{((2+\cos\theta)\cos\phi,(2+\cos\theta)\sin\phi,\sin\theta):\theta,\phi\in[0,2\pi]\}\subset\mathbb{R}^3
	\]
	is a standard embedded model of this torus. The map
	\[
	G(x,y)=\big((2+\cos 2\pi x)\cos 2\pi y,\ (2+\cos 2\pi x)\sin 2\pi y,\ \sin 2\pi x\big)
	\]
	is $\,\mathbb{Z}^2$–periodic and hence factors through the quotient, yielding a homeomorphism
	$\tilde G:\mathbb{R}^2/\mathbb{Z}^2\to T$.
```

## CP-II-0321

- chapter line: 5618

```tex
\label{prob:cp-ii-0321}
(Local submersion theorem and consequences)

The \emph{canonical submersion} is the standard projection $\mathbb{R}^k\to\mathbb{R}^\ell$ for $k\ge \ell$,
\[
(x_1,\dots,x_k)\longmapsto (x_1,\dots,x_\ell).
\]
Let $f$ be a submersion and $y=f(x)$. Show:

	\par\noindent\textbullet\quad there exist local coordinates around $x$ and $y$ such that $f$ becomes the canonical submersion;
	\par\noindent\textbullet\quad submersions are open maps;
	\par\noindent\textbullet\quad if $X$ is compact and $Y$ connected, then every submersion $f:X\to Y$ is surjective;
	\par\noindent\textbullet\quad decide whether there exist submersions from compact manifolds into Euclidean spaces.

A smooth map $f:X^k\to Y^\ell$ is a \emph{submersion at $x$} if $df_x:T_xX\to T_{f(x)}Y$ is surjective.
Equivalently, $\operatorname{rank}(df_x)=\ell$ (so $\ell\le k$). The constant rank theorem gives a local normal form.

Since $f$ is a submersion at $x$, we have $\operatorname{rank}(df_x)=\ell$.
By the constant rank theorem, there exist coordinate charts $(U,\varphi)$ about $x$ and $(V,\psi)$ about $y=f(x)$
such that in these coordinates
\[
(\psi\circ f\circ \varphi^{-1})(u_1,\dots,u_k)=(u_1,\dots,u_\ell),
\]
i.e.\ $f$ becomes the canonical projection $\mathbb{R}^k\to\mathbb{R}^\ell$.


Let $U\subset X$ be open. Fix $x\in U$ and choose local coordinates as in (i), so that locally $f$ is the projection
$\pi(u_1,\dots,u_k)=(u_1,\dots,u_\ell)$. The projection $\pi:\mathbb{R}^k\to\mathbb{R}^\ell$ is an open map.
Since coordinate changes are diffeomorphisms (hence homeomorphisms), they preserve openness. Therefore $f(U)$ is open in $Y$.
Thus every submersion is an open map.


Let $f:X\to Y$ be a submersion. Since $X$ is compact and $f$ is continuous, $f(X)$ is compact.
Because manifolds are Hausdorff, compact sets are closed, hence $f(X)$ is closed in $Y$.
On the other hand, by (ii), $f(X)=f(\,X\,)$ is open in $Y$ (since $X$ is open in itself).
Assuming $X\neq\emptyset$, the set $f(X)$ is nonempty. Hence $f(X)$ is a nonempty subset of $Y$ that is both open and closed.
If $Y$ is connected, this forces $f(X)=Y$. Thus $f$ is surjective.


Let $X$ be compact and suppose $f:X\to\mathbb{R}^\ell$ is a submersion with $\ell\ge 1$.
Then $\mathbb{R}^\ell$ is connected, so by (iii) the map must be surjective: $f(X)=\mathbb{R}^\ell$.
But $f(X)$ is compact, hence cannot equal the non-compact space $\mathbb{R}^\ell$.
This contradiction shows that no such submersion exists for $\ell\ge 1$.
(For $\ell=0$, the target is a point and any smooth map is trivially a submersion.)


A \emph{normal form} is the expression of a smooth map after choosing suitable local coordinates
in the domain and codomain.

	\par\noindent\textbullet\quad \textbf{Immersion normal form.}
	If $f:M^k\to N^n$ is an immersion at $x$ (so $df_x$ is injective, rank $k$), then there exist
	local coordinates $u$ near $x$ and $v$ near $y=f(x)$ such that
	\[
	(v\circ f\circ u^{-1})(u_1,\dots,u_k)=(u_1,\dots,u_k,0,\dots,0).
	\]
	Geometrically, $f(M)$ looks locally like a coordinate $k$-plane in $N$.

	\par\noindent\textbullet\quad \textbf{Submersion normal form.}
	If $f:X^k\to Y^\ell$ is a submersion at $x$ (so $df_x$ is surjective, rank $\ell$), then there exist
	local coordinates $u$ near $x$ and $v$ near $y=f(x)$ such that
	\[
	(v\circ f\circ u^{-1})(u_1,\dots,u_k)=(u_1,\dots,u_\ell).
	\]
	Geometrically, the fibers $f^{-1}(c)$ are locally the coordinate slices
	$\{u_1=c_1,\dots,u_\ell=c_\ell\}$, hence smooth manifolds of dimension $k-\ell$.
```

## CP-II-0323

- chapter line: 5810

```tex
\label{prob:cp-ii-0323}
\par\noindent\textbullet\quad \emph{Sequential compactness route.}
	From boundedness, every sequence in $E$ lies in a bounded subset of $\mathbb R^n$,
	hence has a convergent subsequence $(x_{n_k})\to q\in\mathbb R^n$.
	If $q\notin E$, the function $x\mapsto 1/\|x-q\|$ would be an unbounded continuous map on $E$,
	contradiction. Thus every sequence in $E$ has a convergent subsequence whose limit lies in $E$,
	so $E$ is sequentially compact, hence compact.
```

## CP-II-0326

- chapter line: 5820

```tex
\label{prob:cp-ii-0326}
Let $E\subset\mathbb{R}^n$ be compact and $f:E\to\mathbb{R}^m$ continuous.

\renewcommand\labelenumi{(\alph{enumi})}
\par\noindent\textbullet\quad $f(E)$ is bounded. \textit{Proof.} Each component $f^j$ attains its max/min on $E$.
\par\noindent\textbullet\quad $f(E)$ is closed, hence compact. \textit{Proof.} Use sequential closedness via compactness of $E$.
\par\noindent\textbullet\quad If $E$ is merely closed, $f(E)$ need not be closed; e.g.\ $f(x)=\arctan x$ on $E=\mathbb{R}$.
```

## CP-II-0330

- chapter line: 5830

```tex
\label{prob:cp-ii-0330}
\par\noindent\textbullet\quad The sequence $(f_n)$ is bounded but \emph{translates to infinity}.
		This shows that the $L^1$ unit ball is not weakly compact.
```

## CP-II-0332

- chapter line: 5836

```tex
\label{prob:cp-ii-0332}
Closure vs.\ Sequential Closure

For $A\subseteq X$, the \emph{sequential closure} $\operatorname{scl}(A)$ is the set of all limits of sequences $(x_n)$ with $x_n\in A$.
	We say $A$ is \emph{sequentially closed} if $\operatorname{scl}(A)\subseteq A$, i.e.\ whenever $x_n\in A$ and $x_n\to x$ in $X$, then $x\in A$.

	Assume $X$ is uncountable and $\tau=\{\varnothing\}\cup\{\,U\subseteq X:\ X\setminus U\ \text{is countable}\,\}$ (the co-countable topology).

	\begin{lemma}
		In $(X,\tau)$, a sequence $(x_n)$ converges to $x$ if and only if it is eventually constant equal to $x$.
	\end{lemma}
	\begin{proof}
		($\Rightarrow$) Let $(x_n)\to x$. Any neighborhood of $x$ is of the form $X\setminus C$ with $C$ countable and $x\notin C$; thus for each such $C$, $\{n:\ x_n\in C\}$ is finite.
		Let $S$ be the set of values taken by the tail of $(x_n)$; $S$ is countable. If $x\notin S$, take $C=S$ and get a contradiction. Hence $x\in S$. Taking $C=S\setminus\{x\}$ forces $x_n\in\{x\}$ eventually.
		($\Leftarrow$) If $x_n=x$ eventually, then every neighborhood of $x$ contains all sufficiently large $n$, so $x_n\to x$.
	\end{proof}

	\begin{proposition}
		Every subset $A\subseteq X$ is sequentially closed, but an uncountable proper subset $A$ is not closed.
	\end{proposition}
	\begin{proof}
		If $x_n\in A$ and $x_n\to x$, the lemma shows $x_n=x$ eventually, hence $x\in A$; thus $A$ is sequentially closed.
		Closed sets in the co-countable topology are precisely the countable sets together with $X$; therefore any uncountable proper $A$ is not closed.
	\end{proof}

	On $X=\mathbb{R}$ with the co-countable topology, $A=\mathbb{R}\setminus\mathbb{Q}$ is sequentially closed but not closed.

	\begin{proposition}
		If $(X,\tau)$ is second countable, then for every $A\subseteq X$ we have $\operatorname{scl}(A)=\overline{A}$. In particular, $A$ is sequentially closed iff $A$ is closed.
	\end{proposition}
	\begin{proof}
		Let $\mathcal{B}=\{B_1,B_2,\dots\}$ be a countable base for $X$. Fix $x\in X$ and enumerate $\mathcal{B}_x=\{B\in\mathcal{B}: x\in B\}$ as $(C_n)_{n\ge1}$.
		Define $U_n=\bigcap_{k=1}^n C_k$. Then $(U_n)$ is a decreasing countable neighborhood base at $x$.
		If $x\in\overline{A}$, then $A\cap U_n\neq\varnothing$ for all $n$; choose $x_n\in A\cap U_n$.
		By construction $x_n\to x$. Hence every point of $\overline{A}$ is a sequential limit of points of $A$, so $\operatorname{scl}(A)\supseteq\overline{A}$.
		The reverse inclusion is always true. Therefore $\operatorname{scl}(A)=\overline{A}$, and the equivalence follows.
	\end{proof}

	In $(\mathbb{R},\text{usual})$ the set $A=(0,1)$ is not sequentially closed since $x_n=1/n\to 0\notin A$.
	In contrast, in the co-countable $\mathbb{R}$ every subset is sequentially closed, while uncountable proper subsets are not closed.
```

## CP-II-0333

- chapter line: 5879

```tex
\label{prob:cp-ii-0333}
Small Metric Spaces and Isometric Embeddings

Let $(X,d)$ be a metric space.

		\par\noindent\textbullet\quad If $X=\{p_1,p_2,p_3\}$ has only three points, show that $X$ admits an
		isometric embedding into the Euclidean plane $(\mathbb{R}^2,d_{\mathrm{eucl}})$.

		\par\noindent\textbullet\quad Show that the four-point space
		\[
		X=\{p_1,p_2,p_3,q\}
		\]
		with distances
		\[
		d(p_i,p_j)=2L \quad(1\le i<j\le 3),\qquad
		d(p_1,q)=2L,\qquad d(p_2,q)=d(p_3,q)=L
		\]
		is a metric space which admits no isometric embedding into any Euclidean
		space $\mathbb{R}^n$.

		\par\noindent\textbullet\quad Let $L=\pi/4$ in \textnormal{(b)}.  Show that $X$ isometrically embeds
		in the unit sphere $(S^2,d_{S^2})\subset\mathbb{R}^3$, where $d_{S^2}$ is
		great-circle distance, and deduce that no subset of $S^2$ containing an open
		hemisphere admits an isometric embedding into the plane
		$(\mathbb{R}^2,d_{\mathrm{eucl}})$.

	A map $F:(X,d_X)\to(Y,d_Y)$ is an \emph{isometric embedding} if it is
	injective and
	\[
	d_Y(F(x),F(x'))=d_X(x,x')\quad\forall\,x,x'\in X.
	\]
	Any three-point metric space satisfying the triangle inequalities can be
	realised as a Euclidean triangle.  In Euclidean space, distance constraints
	give quadratic equations; for small configurations one can solve them
	explicitly and detect contradictions (e.g.\ a negative ``squared length'').

	On the unit sphere $S^2\subset\mathbb{R}^3$ with the intrinsic metric,
	the distance between unit vectors $u,v$ is
	\[
	d_{S^2}(u,v)=\arccos(u\cdot v),
	\]
	where $\cdot$ denotes the Euclidean dot product.  Rotations of $\mathbb{R}^3$
	preserve both $S^2$ and $d_{S^2}$, so any finite configuration can be rotated
	into a given open hemisphere.

	Let
	\[
	a=d(p_1,p_2),\quad b=d(p_1,p_3),\quad c=d(p_2,p_3).
	\]
	By the triangle inequality the three numbers $a,b,c$ satisfy
	\[
	a\le b+c,\quad b\le a+c,\quad c\le a+b.
	\]

	Place
	\[
	F(p_1)=(0,0),\qquad F(p_2)=(a,0)\in\mathbb{R}^2
	\]
	and seek $F(p_3)=(x,y)$ with
	\[
	\|F(p_3)-F(p_1)\|=b,\qquad \|F(p_3)-F(p_2)\|=c.
	\]
	Equivalently,
	\[
	x^2+y^2=b^2,\qquad (x-a)^2+y^2=c^2.
	\]
	Subtracting gives
	\[
	a^2-2ax=c^2-b^2,\qquad
	x=\frac{a^2+b^2-c^2}{2a}.
	\]
	Then
	\[
	y^2=b^2-x^2
	=\frac{(a+b+c)(a+b-c)(a-b+c)(-a+b+c)}{16a^2}\ge 0,
	\]
	by the triangle inequalities.  Hence there exists $y\in\mathbb{R}$ and an
	isometric embedding $F:X\to\mathbb{R}^2$.

	Suppose, for a contradiction, that there exists an isometric embedding
	$F:X\to\mathbb{R}^n$.  Let
	\[
	P_i=F(p_i),\qquad Q=F(q).
	\]
	The points $P_1,P_2,P_3$ form an equilateral triangle of side $2L$.  After a
	rigid motion we may assume
	\[
	P_1=(0,0,0,\dots),\quad
	P_2=(2L,0,0,\dots),\quad
	P_3=(L,\sqrt{3}\,L,0,\dots).
	\]
	Write $Q=(x,y,u)$ with $(x,y)\in\mathbb{R}^2$ and $u\in\mathbb{R}^{n-2}$; set
	$\|u\|^2=U\ge0$.

	The distance conditions become
	\begin{align*}
		(x-2L)^2+y^2+U &= L^2, \tag{1}\\
		(x-L)^2+(y-\sqrt{3}L)^2+U &= L^2, \tag{2}\\
		x^2+y^2+U &= 4L^2. \tag{3}
	\end{align*}
	Subtracting \textnormal{(2)} from \textnormal{(1)} yields
	\[
	-2Lx+2\sqrt{3}Ly=0,\qquad x=\sqrt{3}\,y.
	\]
	Subtracting \textnormal{(1)} from \textnormal{(3)} gives
	\[
	x^2-(x-2L)^2=3L^2,\qquad 4Lx-4L^2=3L^2,
	\]
	so $x=7L/4$ and hence $y=7L/(4\sqrt{3})$.

	From \textnormal{(1)},
	\[
	(x-2L)^2+y^2+U=L^2
	\]
	implies
	\[
	U = L^2 - \frac{L^2}{16}-\frac{49L^2}{48}
	= -\frac{L^2}{12}<0,
	\]
	contradicting $U=\|u\|^2\ge0$.  Thus no isometric embedding of $X$ into any
	$\mathbb{R}^n$ exists.

	Set $L=\pi/4$ and consider the unit sphere $S^2\subset\mathbb{R}^3$ with
	intrinsic distance
	\[
	d_{S^2}(u,v)=\arccos(u\cdot v).
	\]

	Choose
	\[
	P_1=(1,0,0),\quad P_2=(0,1,0),\quad P_3=(0,0,1)\in S^2.
	\]
	These are pairwise orthogonal, so
	\[
	d_{S^2}(P_i,P_j)=\arccos(0)=\frac{\pi}{2}=2L
	\quad (1\le i<j\le 3).
	\]
	Let
	\[
	Q=\left(0,\frac{1}{\sqrt{2}},\frac{1}{\sqrt{2}}\right)\in S^2.
	\]
	Then
	\[
	P_1\cdot Q=0,\qquad
	P_2\cdot Q=P_3\cdot Q=\frac{1}{\sqrt{2}},
	\]
	so
	\[
	d_{S^2}(P_1,Q)=\frac{\pi}{2}=2L,\qquad
	d_{S^2}(P_2,Q)=d_{S^2}(P_3,Q)=\frac{\pi}{4}=L.
	\]
	Therefore the map $F$ defined by $F(p_i)=P_i$, $F(q)=Q$ is an isometric
	embedding of $X$ into $(S^2,d_{S^2})$.

	Now let $Y\subset S^2$ contain an open hemisphere $H$.  Since rotations of
	$S^2$ are isometries and $H$ is open, we can rotate the above four-point
	configuration so that all four points lie in $H\subset Y$.  Thus $Y$
	contains a subset isometric to $X$.

	If there were an isometric embedding $\Phi:Y\to\mathbb{R}^2$, its restriction
	to this four-point subset would be an isometric embedding of $X$ into
	$\mathbb{R}^2$, contradicting part \textnormal{(b)}.  Hence no subset of $S^2$
	containing an open hemisphere admits an isometric embedding into the plane.


	Let $X=\{a,b\}$ with $d(a,b)=\ell>0$.  An isometric embedding into
	$\mathbb{R}$ is given by
	\[
	F(a)=0,\qquad F(b)=\ell,
	\]
	since $|F(a)-F(b)|=\ell=d(a,b)$.  Likewise, into $\mathbb{R}^2$ we may choose
	$G(a)=(0,0)$ and $G(b)=(\ell,0)$.  Any map which sends $a,b$ to points at a
	different distance, or fails to be injective (for instance $K(a)=K(b)=0$), is
	\emph{not} an isometric embedding.

	Let $X=\{p_1,p_2,p_3\}$ and set
	\[
	a=d(p_1,p_2),\quad b=d(p_1,p_3),\quad c=d(p_2,p_3).
	\]
	Because $d$ is a metric, the triangle inequalities hold:
	\[
	a\le b+c,\quad b\le a+c,\quad c\le a+b.
	\]
	We now construct an isometric embedding $F:X\to\mathbb{R}^2$.

	Place
	\[
	F(p_1)=(0,0),\qquad F(p_2)=(a,0),
	\]
	and write $F(p_3)=(x,y)$.  The distance constraints become
	\[
	x^2+y^2=b^2,\qquad (x-a)^2+y^2=c^2.
	\]
	Subtracting the equations gives
	\[
	a^2-2ax=c^2-b^2,\qquad
	x=\frac{a^2+b^2-c^2}{2a}.
	\]
	Then
	\[
	y^2=b^2-x^2
	=b^2-\left(\frac{a^2+b^2-c^2}{2a}\right)^2
	=\frac{(a+b+c)(a+b-c)(a-b+c)(-a+b+c)}{16a^2}\ge 0.
	\]
	Thus $y\in\mathbb{R}$ exists and the three points
	\[
	F(p_1)=(0,0),\quad F(p_2)=(a,0),\quad F(p_3)=(x,y)
	\]
	form a Euclidean triangle whose side lengths are exactly
	$a,b,c$.  Hence every three-point metric space satisfying the triangle
	inequalities can be realised as a Euclidean triangle via an isometric
	embedding into $\mathbb{R}^2$.

	Let $(X,d_X)$ and $(Y,d_Y)$ be metric spaces.

	A \emph{topological embedding} is a continuous map $f:X\to Y$ which is
	injective and a homeomorphism from $X$ onto its image $f(X)$, equipped with
	the subspace topology.  Such a map may distort distances; it preserves only
	the topology.

	An \emph{isometric embedding} is a map $f:X\to Y$ satisfying
	\[
	d_Y(f(x),f(y)) = d_X(x,y)\qquad\text{for all }x,y\in X.
	\]
	This condition preserves the metric exactly.  In particular, if $f$ is
	distance-preserving then it is automatically injective: if $f(x)=f(y)$ then
	\[
	0 = d_Y(f(x),f(y)) = d_X(x,y),
	\]
	and since $d_X$ is a metric we must have $x=y$.  Thus an isometric embedding
	is a special kind of topological embedding which preserves all distances and
	hence all geometric information encoded by the metric.

	When we speak of an ``embedding'' we want to regard $X$ as a copy of a
	subspace of $Y$.  This requires a one-to-one correspondence between points of
	$X$ and points of the image $f(X)\subset Y$; otherwise different points of $X$
	would be identified in $Y$ and the structure of $X$ would be lost.  For
	general topological embeddings injectivity is imposed by definition; for
	isometric embeddings it follows automatically from the metric property.
```

## CP-II-0334

- chapter line: 6121

```tex
\label{prob:cp-ii-0334}
Topological vs.\ metric properties

Each item makes sense for a metric space $(X,d)$. Decide which are \emph{topological}
(depend only on the open sets) and justify.

	\par\noindent\textbullet\quad \textbf{Boundedness of a subset of $X$} — \emph{Not topological.}
On $\mathbb R$, the metrics $d(x,y)=|x-y|$ and $d'(x,y)=\min\{1,|x-y|\}$ generate the same
	topology. Then $(\mathbb R,d')$ is bounded (diameter $\le 1$) while $(\mathbb R,d)$ is unbounded.

	\par\noindent\textbullet\quad \textbf{Closedness of a subset of $X$} — \emph{Topological.}

	Closed sets are complements of open sets; hence determined by the topology alone.

	\par\noindent\textbullet\quad \textbf{“Closed and bounded” for a subset of $X$} — \emph{Not topological.}

	Closed is topological, bounded is not. With $d,d'$ as in (i), $\mathbb R$ is closed in itself and
	bounded in $(\mathbb R,d')$ but not in $(\mathbb R,d)$.

	\par\noindent\textbullet\quad \textbf{Total boundedness of $X$} — \emph{Not topological.}

	Let $h:\mathbb R\to(0,1)$ be a homeomorphism, and define $d_h(x,y)=|h(x)-h(y)|$. Then $d_h$
	induces the usual topology on $\mathbb R$, but $(\mathbb R,d_h)$ is isometric to $(0,1)$ and thus
	totally bounded, while $(\mathbb R,|\cdot|)$ is not.

	\par\noindent\textbullet\quad \textbf{Completeness of $X$} — \emph{Not topological.}

	Let $h:(0,1)\to\mathbb R$ be a homeomorphism and $\rho(x,y)=|h(x)-h(y)|$. Then $\rho$ induces the
	usual topology on $(0,1)$, but $(0,1,\rho)$ is complete (isometric to $\mathbb R$), whereas
	$(0,1,|\cdot|)$ is not complete.

	\par\noindent\textbullet\quad \textbf{“$X$ is complete and totally bounded$\,\,$”} — \emph{Topological (for metric spaces).}

	In metric spaces,
	\[
	\text{complete and totally bounded}\quad\Longleftrightarrow\quad\text{compact}.
	\]
	Compactness is a topological property; hence the conjunction is topological.
	(Neither completeness nor total boundedness alone is topological; see (iv)–(v).)
```

## CP-II-0357

- chapter line: 6189

```tex
\label{prob:cp-ii-0357}
/ Non-Example

$(\mathbb{R},\text{usual})$ is Hausdorff and second countable, while $(\mathbb{R},\text{cofinite})$ is $T_1$ but neither Hausdorff nor second countable. Therefore they are not homeomorphic, illustrating invariance.

\bigskip

\subsection*{Problem 4: Equality of the Euclidean Metric Topology and the Product Topology on $\mathbb{R}^n$}

Show that the topology on $\mathbb{R}^n$ induced by the Euclidean metric equals the product topology inherited from $\mathbb{R}$ with its usual metric.

Let $\|\cdot\|_2$ be the Euclidean norm and $\|\cdot\|_\infty$ the sup-norm on $\mathbb{R}^n$. For all $v\in\mathbb{R}^n$,
\[
\|v\|_\infty \le \|v\|_2 \le \sqrt{n}\,\|v\|_\infty.
\]
Hence for balls centered at $x\in\mathbb{R}^n$ and $r>0$,
\[
B_2(x,r)\subseteq B_\infty(x,r)\subseteq B_2\!\bigl(x,\sqrt{n}\,r\bigr).
\]
Basic product-open sets are the open boxes $\prod_{i=1}^n (a_i,b_i)=B_\infty(x,r)$.
```

## CP-II-0365

- chapter line: 6212

```tex
\label{prob:cp-ii-0365}
\par\noindent\textbullet\quad The set \((0.2,0.7)\) \emph{is} open in \(X\).

\smallskip

In Problem~4 we defined a new metric on \(X\) by
\[
d(x,y)=\left|\frac{1}{x}-\frac{1}{y}\right|.
\]

The key property required was:
\begin{center}
\resizebox{\linewidth}{!}{$\displaystyle
\text{a subset of } X \text{ is open with respect to } d
\quad\text{iff}\quad
\text{it is open in the usual Euclidean subspace topology.}
$}
\end{center}

\smallskip

That means:
\[
\text{$d$-open sets on $X$} \;=\; \text{open sets of the subspace topology from $\mathbb{R}$.}
\]

So the metric \(d\) does not change which sets are open;
it only changes the distances so that completeness is recovered.

\medskip
```

## CP-II-0367

- chapter line: 6245

```tex
\label{prob:cp-ii-0367}
\par\noindent\textbullet\quad Hence $f,g \in C_0^0(\mathbb{R})$ (continuous with compact support, $k=0$).

Their convolution is
\[
(f*g)(x) = \int_{\mathbb{R}} f(x-y)\,g(y)\,dy,
\]
which is a continuous Ă˘â‚¬Ĺ›rounded tentĂ˘â‚¬â„˘Ă˘â‚¬â„˘ supported in the interval $[-2,2]$.
```

## CP-II-0372

- chapter line: 6256

```tex
\label{prob:cp-ii-0372}
— Polynomial (vs.\ rational) approximation on a punctured disc

paragraph{Problem (exact).}
Let $B_r(z)$ denote the open disc of radius $r$ about $z\in\mathbb C$ and set
\[
U \;=\; B_2(1)\setminus B_1(0).
\]
Suppose $f$ is holomorphic on $U$.

	\par\noindent\textbullet\quad Prove that there exists a sequence of \emph{rational functions} which converges to $f$
	uniformly on compact subsets of $U$.
	\par\noindent\textbullet\quad Must there be a sequence of \emph{polynomials} which converges to $f$ uniformly on $U$?
	\par\noindent\textbullet\quad If, in addition, $f$ is holomorphic on some open set containing $\overline U$,
	must there be a sequence of \emph{polynomials} which converges to $f$ uniformly on $U$?

We will use the following results.

	\par\noindent\textbullet\quad \textbf{RungeĂ˘â‚¬â„˘s theorem (rational form).}
	Let $K\subset\mathbb C$ be compact and let $E=\widehat{\mathbb C}\setminus K$.
	If $E$ has finitely many components, then every function holomorphic on a neighborhood
	of $K$ can be uniformly approximated on $K$ by rational functions whose poles lie in a
	prescribed finite set containing at least one point from each bounded component of $E$.
	If $E$ is connected and contains $\infty$, the approximants can be chosen to be polynomials.
	\par\noindent\textbullet\quad \textbf{MergelyanĂ˘â‚¬â„˘s theorem (polynomial form).}
	If $K\subset\mathbb C$ is compact with connected complement and $f$ is continuous on $K$
	and holomorphic in $\operatorname{int}K$, then there exists a sequence of polynomials
	converging uniformly to $f$ on $K$.
	\par\noindent\textbullet\quad \textbf{Cauchy integral test for non-approximability.}
	If $p_n\to g$ uniformly on a simple closed curve $\Gamma$, then
	$\int_\Gamma p_n(z)\,dz\to\int_\Gamma g(z)\,dz$.
	For every polynomial $p$, $\int_\Gamma p(z)\,dz=0$.
	\par\noindent\textbullet\quad \textbf{Geometry of $U$.}
	The complement of $U$ in the Riemann sphere has two components:
	the unbounded $\mathbb C\setminus B_2(1)$ (containing $\infty$) and the bounded
	$\overline{B_1(0)}$ (containing $0$). Thus RungeĂ˘â‚¬â„˘s theorem yields rational
	approximation on compacts of $U$ with all poles placed in the bounded component
	(e.g.\ at $0$), but not, in general, polynomial approximation on all of $U$ unless
	$f$ extends holomorphically across the hole so that the relevant compact has
	connected complement.

Let $B_r(z)$ be the open disc of radius $r$ about $z\in\mathbb C$ and
$U=B_2(1)\setminus B_1(0)$. Assume $f$ is holomorphic on $U$.

The complement $\widehat{\mathbb C}\setminus U$ has two components:
the unbounded $\mathbb C\setminus B_2(1)$ and the bounded $\overline{B_1(0)}$.
By RungeĂ˘â‚¬â„˘s theorem, for every compact $K\Subset U$ there exist rational functions $r_n$
with all poles in $\overline{B_1(0)}$ (indeed at $0$) such that $r_n\to f$
uniformly on $K$. Thus $f$ is locally uniformly approximable by rational functions with poles at $0$.
\emph{(If the statement asks for polynomials, this is false in general; see (ii).)}

\emph{No.} Consider $f(z)=1/z\in O(U)$. Suppose polynomials $p_n$ satisfy $p_n\to f$
uniformly on $U$. Let $\Gamma=\{\,|z|=r\,\}$ with $1<r<2$ and $\Gamma\subset U$.
Then
\[
\int_\Gamma p_n(z)\,dz \longrightarrow \int_\Gamma \frac{1}{z}\,dz = 2\pi i,
\]
whereas for all polynomials $p_n$ we have $\int_\Gamma p_n(z)\,dz=0$ by CauchyĂ˘â‚¬â„˘s theorem,
a contradiction. Hence, in general, no such polynomial sequence exists.

Assume $f$ is holomorphic on some open set $W\supset \overline U$.
Then $f$ is holomorphic on a neighborhood of the compact set $K=\overline{B_2(1)}$,
whose complement is connected and contains $\infty$.
By RungeĂ˘â‚¬â„˘s theorem (or MergelyanĂ˘â‚¬â„˘s theorem),
there are polynomials $p_n$ with $p_n\to f$ uniformly on $K$; in particular,
$p_n\to f$ uniformly on $U$.
Therefore under this additional assumption the answer is \emph{yes}.
```

## CP-II-0375

- chapter line: 6326

```tex
\label{prob:cp-ii-0375}
\par\noindent\textbullet\quad \emph{Compact}: every open cover has a finite subcover (equivalently in metric spaces: sequentially compact).

\bigskip

Fix the scale sequence $\varepsilon_m := 2^{-m}$ for $m\in\mathbb{N}$.

\medskip

\emph{Step 1 (first thinning).} By total boundedness, $X$ can be covered by finitely many balls of radius $\varepsilon_1$.
One of these balls contains infinitely many terms of $(x_k)$. Pass to that infinite subsequence and relabel it $(x^{(1)}_k)$.

\medskip

\emph{Step 2 (iterated thinning).} Again by total boundedness, cover $X$ by finitely many balls of radius $\varepsilon_2$.
One such ball contains infinitely many terms of $(x^{(1)}_k)$. Pass to that infinite subsequence and relabel it $(x^{(2)}_k)$.

\medskip

\emph{Step 3 (continue).} Proceed inductively: after step $m$ we have an infinite subsequence
$(x^{(m)}_k)$ contained in a single ball of radius $\varepsilon_m$.

\medskip

\emph{Step 4 (diagonal choice).} Define the diagonal subsequence $y_m := x^{(m)}_m$.
Then $y_m$ lies inside a ball of radius $\varepsilon_m$ that contains all but finitely many terms of the previous stage.
In particular,
\[
d(y_{m+1},y_m) \;<\; \varepsilon_m \qquad \text{for all } m\in\mathbb{N}.
\]

\medskip

\emph{Step 5 (Cauchy property).} Let $\varepsilon>0$ and choose $M$ with $\varepsilon_M<\varepsilon/2$.
For $n>m\ge M$, the points $y_m,y_n$ both lie in a ball of radius $\varepsilon_m\le \varepsilon_M<\varepsilon/2$,
so $d(y_m,y_n)\le 2\varepsilon_M<\varepsilon$. Hence $(y_m)$ is Cauchy.

\medskip

Thus every sequence in a totally bounded metric space admits a Cauchy subsequence.

\bigskip

\emph{($\Rightarrow$) Compact $\Rightarrow$ complete and totally bounded.}
Compact metric spaces are sequentially compact. A Cauchy sequence has a convergent subsequence;
Cauchy $+$ convergent subsequence forces the whole sequence to converge, hence completeness.
Total boundedness follows since otherwise some $\varepsilon$-net would require infinitely many balls,
contradicting compactness (use a standard Lebesgue number/covering argument).

\medskip

\emph{($\Leftarrow$) Complete and totally bounded $\Rightarrow$ compact.}
Let $(x_k)$ be any sequence in $X$. By (a), it has a Cauchy subsequence; by completeness this subsequence converges in $X$.
Hence $X$ is sequentially compact. In metric spaces, sequential compactness is equivalent to compactness.
Therefore $X$ is compact.

\hfill$\Box$
```

## CP-II-0393

- chapter line: 6543

```tex
\label{prob:cp-ii-0393}
\par\noindent\textbullet\quad Haar measure on a locally compact topological group $G$ is a Radon Borel measure on $\mathcal{B}(G)$.

	\bigskip\bigskip

	\[
	\text{Topology on } X
	\ \Longrightarrow\
	\mathcal{B}(X)
	\ \xrightarrow{\ \text{measure}\ }\
	\text{Borel measure}
	\ \xRightarrow[\text{locally finite}]{\text{inner/outer regular}}
	\ \text{Radon measure}.
	\]

	On a locally compact group $G$, a Radon Borel measure that is left-invariant
	is Haar measure (unique up to scale). Given a reference Radon measure $\mu$
	(e.g.\ Lebesgue or Haar), any finite measure $\nu$ admits the \emph{Lebesgue decomposition}
	$\nu=\nu_a+\nu_s$ with $\nu_a\ll\mu$ and $\nu_s\perp\mu$.
```

## CP-II-0395

- chapter line: 6565

```tex
\label{prob:cp-ii-0395}
Let $X$ be a reflexive Banach space, and let $Y\subset X$ be a closed subspace. Show that $Y$ is reflexive.

	In a reflexive Banach space, the closed unit ball is weakly compact.
	Since $B_Y=B_X\cap Y$ is closed, bounded and convex, it is weakly compact in the relative weak topology of $Y$.
	By KakutaniĂ˘â‚¬â„˘s theorem (or JamesĂ˘â‚¬â„˘ criterion), $Y$ is reflexive.
	Equivalently, the canonical map $J_Y:Y\to Y''$ is surjective because every bounded sequence in $Y$ admits a weakly convergent subsequence; its limit represents the image under $J_Y$.

	Any closed subspace of $L^p(\Omega)$ ($1<p<\infty$), e.g.\ $W^{1,p}_0(\Omega)$, is reflexive;
	any closed subspace of $\ell^2$ is reflexive.

	Let $X$ be a Banach space, $X'$ its dual, and $X''=(X')'$ its bidual.
	The canonical map $J_X:X\to X''$ is given by
	\[
	J_X(x)(\varphi)=\varphi(x)\qquad(\varphi\in X').
	\]
	It is linear and isometric. We say that $X$ is \emph{reflexive} if $J_X$ is surjective
	(equivalently $X\cong X''$ isometrically).

		\par\noindent\textbullet\quad \textbf{Kakutani.} $X$ is reflexive $\iff$ the closed unit ball $B_X$ is weakly compact.
		\par\noindent\textbullet\quad \textbf{Eberlein--\v{S}mulian.} In Banach spaces, weak compactness $\iff$ weak sequential compactness.
		Hence $X$ is reflexive $\iff$ every bounded sequence in $X$ has a weakly convergent subsequence.
		\par\noindent\textbullet\quad \textbf{James.} $X$ is reflexive $\iff$ every $\varphi\in X'$ attains its norm on $B_X$.
		\par\noindent\textbullet\quad \textbf{Dual stability.} $X$ is reflexive $\iff$ $X'$ is reflexive.
		\par\noindent\textbullet\quad \textbf{Uniform convexity (Milman--Pettis).} If $X$ is uniformly convex, then $X$ is reflexive.

	If $X$ is reflexive and $Y\subset X$ is a closed subspace, then $Y$ is reflexive.
	Moreover, the quotient $X/Y$ is also reflexive.

		\par\noindent\textbullet\quad \textbf{Reflexive.} Every finite dimensional normed space; every Hilbert space;
		$L^{p}(\Omega)$ for $1<p<\infty$; $\ell^{p}$ for $1<p<\infty$; Sobolev spaces
		$W^{k,p}(\Omega)$ for $1<p<\infty$, and closed subspaces like $W^{1,p}_0(\Omega)$.
		\par\noindent\textbullet\quad \textbf{Non-reflexive.} $L^{1}(\Omega)$ and $L^{\infty}(\Omega)$;
		$\ell^{1}$, $\ell^{\infty}$, and $c_{0}$; $C(K)$ with $\|\cdot\|_\infty$ for infinite compact $K$.

		\par\noindent\textbullet\quad If $H$ is a Hilbert space, any closed subspace $M\subset H$ is reflexive
		(it is itself a Hilbert space with the induced inner product).
		\par\noindent\textbullet\quad In $L^{p}(\Omega)$, $1<p<\infty$, examples include:

			\par\noindent\textbullet\quad $W^{1,p}_0(\Omega)$ (closure of $C_c^\infty$ in $W^{1,p}$),
			\par\noindent\textbullet\quad kernels of bounded operators (e.g.\ $\{f:\int_\Omega f=0\}$),
			\par\noindent\textbullet\quad ranges/orthogonal complements when $p=2$.

		All are reflexive since they are closed subspaces of a reflexive space.
		\par\noindent\textbullet\quad In a non-reflexive space (e.g.\ $L^{1}$), closed subspaces can be
		\emph{either} reflexive (finite-dimensional) \emph{or} non-reflexive
		(e.g.\ a closed subspace isomorphic to $\ell^{1}$).

	If $X$ is reflexive, every bounded sequence admits a weakly convergent subsequence.
	Minimization of weakly lower semicontinuous convex functionals on closed, convex, bounded sets
	is therefore well-posed (direct method of the calculus of variations).

		\par\noindent\textbullet\quad Finite-dimensional $\Rightarrow$ reflexive.
		\par\noindent\textbullet\quad Uniformly convex (e.g.\ Hilbert, $L^p$ with $1<p<\infty$) $\Rightarrow$ reflexive.
		\par\noindent\textbullet\quad Unit ball weakly compact / every bounded sequence has a weakly convergent subsequence $\Rightarrow$ reflexive.
		\par\noindent\textbullet\quad Presence of subspaces isomorphic to $\ell^1$ or $c_0$ often signals non-reflexivity.

	Let $X$ be a Banach space, $X'$ its dual and $X''=(X')'$ its bidual.
	The canonical map $J_X:X\to X''$ is
	\[
	J_X(x)(\varphi)=\varphi(x)\qquad(\varphi\in X').
	\]
	Then $J_X$ is linear and isometric. We call $X$ \emph{reflexive} if $J_X$ is surjective
	(equivalently $X\cong X''$ isometrically).

	The following are equivalent:

		\par\noindent\textbullet\quad (Kakutani) The closed unit ball $B_X$ is weakly compact.
		\par\noindent\textbullet\quad (Eberlein--\v{S}mulian) Every bounded sequence in $X$ admits a weakly convergent subsequence.
		\par\noindent\textbullet\quad (James) Every $\varphi\in X'$ attains its norm on $B_X$.

	Moreover, if $X$ is uniformly convex (e.g.\ $L^p$, $1<p<\infty$), then $X$ is reflexive (Milman--Pettis).

	\par\noindent\textbullet\quad \textbf{Dual.} $(L^p)'\cong L^{p'}$ via $g\mapsto\big[f\mapsto\!\int f g\,d\mu\big]$, with $1/p+1/p'=1$.
	\par\noindent\textbullet\quad \textbf{Bidual.} $(L^p)''\cong (L^{p'})'\cong L^p$.
	\par\noindent\textbullet\quad \textbf{Why onto?} The canonical $J_{L^p}$ is an isometric isomorphism because $L^p$ is uniformly convex (Milman--Pettis) and the duality pairing is full. \textbf{Hence reflexive.}

	\par\noindent\textbullet\quad \textbf{Dual.} $(L^1)'\cong L^\infty$ (pointwise multiplier functionals).
	\par\noindent\textbullet\quad \textbf{Bidual.} $(L^1)''\cong (L^\infty)'$, but $(L^\infty)'=\mathrm{ba}(\mu)$ (bounded finitely additive signed measures, Yosida--Hewitt), which strictly contains $L^1$. The canonical embedding $L^1\hookrightarrow (L^\infty)'$ hits only the countably additive part.
	\par\noindent\textbullet\quad \textbf{Conclusion.} $J_{L^1}$ is not onto (except in essentially finite cases), so \textbf{$L^1$ is non-reflexive}.

	\par\noindent\textbullet\quad \textbf{Dual.} $(L^\infty)'=\mathrm{ba}(\mu)$ (strictly larger than $L^1$).
	\par\noindent\textbullet\quad \textbf{Bidual.} $(L^\infty)''$ is huge; the canonical map is not surjective. \textbf{Thus non-reflexive.}

	\par\noindent\textbullet\quad \textbf{Dual.} $(\ell^p)'\cong \ell^{p'}$ via $\phi_y(x)=\sum_{k=1}^\infty x_k\overline{y_k}$.
	\par\noindent\textbullet\quad \textbf{Bidual.} $(\ell^p)''\cong \ell^p$.
	\par\noindent\textbullet\quad \textbf{Conclusion.} Uniformly convex $\Rightarrow J_{\ell^p}$ onto $\Rightarrow$ \textbf{reflexive}.

	\par\noindent\textbullet\quad \textbf{Dual.} $(\ell^1)'\cong \ell^\infty$.
	\par\noindent\textbullet\quad \textbf{Bidual.} $(\ell^1)''\cong (\ell^\infty)'$ (far larger than $\ell^1$).
	\par\noindent\textbullet\quad \textbf{Conclusion.} $J_{\ell^1}$ not onto $\Rightarrow$ \textbf{non-reflexive}.

	\par\noindent\textbullet\quad \textbf{Dual.} $c_0'=\ell^1$.
	\par\noindent\textbullet\quad \textbf{Bidual.} $c_0''=(\ell^1)'=\ell^\infty$. The canonical embedding $c_0\hookrightarrow\ell^\infty$ is the inclusion, which is not onto.
	\par\noindent\textbullet\quad \textbf{Conclusion.} $c_0$ is \textbf{non-reflexive}.

	\par\noindent\textbullet\quad \textbf{Dual.} $C(K)'\cong M(K)$ (finite regular Borel measures, Riesz--Markov).
	\par\noindent\textbullet\quad \textbf{Bidual.} $C(K)''\cong M(K)'$; the canonical map is onto iff $C(K)$ is finite-dimensional.
	\par\noindent\textbullet\quad \textbf{Conclusion.} $C(K)$ is \textbf{reflexive iff $K$ is finite} (then $C(K)\cong \mathbb{K}^n$).

If $X$ is reflexive and $Y\subset X$ is closed, then $Y$ and $X/Y$ are reflexive. Hence closed subspaces of $L^p$, $1<p<\infty$ (e.g.\ $W^{1,p}_0(\Omega)$, mean-zero subspaces, kernels of bounded maps) are reflexive.

	\textbf{Theorem.} Let $(x_n)$ be a sequence in a Banach space $X$ with $x_n \rightharpoonup x$.
	Then there exist finite convex combinations of the tails
	\[
	y_k=\sum_{n\ge k}\alpha^{(k)}_n\,x_n,\qquad \alpha^{(k)}_n\ge 0,\ \sum_{n\ge k}\alpha^{(k)}_n=1,
	\]
	such that $y_k \to x$ in norm.

	\textbf{Equivalent form.} For any convex $C\subset X$,
	\[
	\overline{C}^{\,\mathrm{weak}}=\overline{C}^{\,\|\cdot\|}.
	\]

	\textbf{Sketch of proof.} If no convex averages converge strongly, the sets
	$A_k=\overline{\mathrm{co}}\{x_n:n\ge k\}$ stay a positive distance from $x$.
	By Hahn–Banach, separate $x$ from $A_k$ with $\varphi_k\in X'$, contradicting
	$\varphi_k(x_n)\to\varphi_k(x)$ (weak convergence). Hence some convex averages converge in norm.

	\textbf{Examples.}

		\par\noindent\textbullet\quad $X=L^p(\Omega)$, $1\le p<\infty$: if $f_n\rightharpoonup f$, then $\exists$ convex averages $g_k$ with $\|g_k-f\|_p\to 0$.
		\par\noindent\textbullet\quad $X=H$ Hilbert: if $x_n\rightharpoonup x$, then Ces\`aro means of a subsequence converge to $x$ in norm.

	\bigskip

	\textbf{Theorem.} Let $X$ be a Banach space, $K\subset X$ open and convex, $C\subset X$ closed and convex,
	and $K\cap C=\varnothing$. Then there exist $\Lambda\in X'\setminus\{0\}$ and $\alpha\in\mathbb R$ such that
	\[
	\Re\Lambda(c)\le \alpha \quad\text{for all } c\in C, \qquad
	\inf_{k\in K}\Re\Lambda(k)>\alpha.
	\]
	In particular, if $C=M$ is a closed subspace disjoint from $K$, then $N:=\ker\Lambda$ is a closed
	hyperplane (codimension one) containing $M$ and disjoint from $K$.

	\textbf{Examples.}

		\par\noindent\textbullet\quad $X=\mathbb R^2$, $K=B((0,1),1)$, $M=\{(t,0):t\in\mathbb R\}$.
		With $\Lambda(x,y)=y$ we have $\Lambda(M)=\{0\}$ and $\Lambda(K)=(0,2)$.
		\par\noindent\textbullet\quad $X=\ell^2$, $M=\mathrm{span}\{e_1\}$, $K=B(e_2,\tfrac12)$.
		The functional $\Lambda(x)=\langle x,e_1\rangle$ and a suitable translation yield a separating hyperplane $N=\ker\Lambda$.

	\bigskip

		\par\noindent\textbullet\quad \emph{Closure of convex sets:} MazurĂ˘â‚¬â„˘s lemma $\Rightarrow$ weak and strong closures of convex sets coincide.
		\par\noindent\textbullet\quad \emph{Optimization:} Direct method—weak limits of minimizing sequences can be averaged to obtain strong convergence.
		\par\noindent\textbullet\quad \emph{Spaces:} All Banach spaces (e.g.\ Hilbert, $L^p$ with $1\le p\le\infty$, Sobolev spaces) admit both results.

	For $1\le p<\infty$,
	\[
	\ell^p := \Bigl\{ x=(x_k)_{k\ge1} : \sum_{k=1}^{\infty} |x_k|^p < \infty \Bigr\},
	\qquad
	\|x\|_{\ell^p} := \Bigl( \sum_{k=1}^{\infty} |x_k|^p \Bigr)^{1/p}.
	\]
	For $p=\infty$,
	\[
	\ell^\infty := \Bigl\{ x=(x_k): \sup_{k} |x_k| < \infty \Bigr\},
	\qquad
	\|x\|_{\ell^\infty} := \sup_{k} |x_k|.
	\]
	Then $(\ell^p,\|\cdot\|_{\ell^p})$ is a Banach space for all $1\le p\le\infty$.
	In particular,
	\[
	\ell^2 \text{ is a Hilbert space with }
	\langle x,y\rangle := \sum_{k=1}^\infty x_k \overline{y_k}.
	\]
	For $1<p<\infty$, the dual space $(\ell^p)'$ is isometrically isomorphic to $\ell^{p'}$,
	where $1/p+1/p'=1$, via $y\mapsto[x\mapsto \sum_k x_k \overline{y_k}]$.

	Let $(\Omega,\mathcal F,\mu)$ be a measure space. For $1\le p<\infty$,
	\[
	L^p(\mu) := \Bigl\{ [f] : f \text{ measurable},\ \int_\Omega |f|^p\,d\mu < \infty \Bigr\},
	\qquad
	\|f\|_{L^p} := \Bigl( \int_\Omega |f|^p\, d\mu \Bigr)^{1/p}.
	\]
	Elements are equivalence classes modulo equality $\mu$-a.e.
	For $p=\infty$,
	\[
	L^\infty(\mu) := \Bigl\{ [f] : \operatorname*{ess\,sup}_{\Omega} |f| < \infty \Bigr\},
	\qquad
	\|f\|_{L^\infty} := \operatorname*{ess\,sup}_{\Omega} |f|.
	\]
	Then $L^p(\mu)$ is a Banach space for $1\le p\le\infty$. For $1<p<\infty$:
	\begin{align*}
		\text{(H\"older)}\quad & \int_\Omega |fg|\,d\mu \le \|f\|_{L^p}\,\|g\|_{L^{p'}},\\
		\text{(Minkowski)}\quad & \|f+g\|_{L^p} \le \|f\|_{L^p}+\|g\|_{L^p},\\
		\text{(Duality)}\quad & (L^p(\mu))' \cong L^{p'}(\mu),\quad \tfrac1p+\tfrac1{p'}=1,
	\end{align*}
	via $g\mapsto \bigl[f\mapsto \int_\Omega f\,g\,d\mu\bigr]$.
```

## CP-II-0396

- chapter line: 6757

```tex
\label{prob:cp-ii-0396}
Gluing (Pasting) Continuous Maps

Let $(X,\tau)$ be a topological space with $X=A\cup B$ and $(Y,\rho)$ another space.
	Let $g:A\to Y$ and $h:B\to Y$ be continuous (with subspace topologies) and suppose $g=h$ on $A\cap B$.
	Define
	\[
	f(x)=
	\begin{cases}
		g(x),& x\in A,\\
		h(x),& x\in B.
	\end{cases}
	\]

	\begin{proof}
		Let $C\subseteq Y$ be closed. Since $g$ is continuous, $g^{-1}(C)$ is closed in $A$, so $g^{-1}(C)=A\cap F$ for some closed $F\subseteq X$.
		Similarly $h^{-1}(C)=B\cap G$ for some closed $G\subseteq X$.
		Then
		\[
		f^{-1}(C)=\big(A\cap g^{-1}(C)\big)\cup\big(B\cap h^{-1}(C)\big)=(A\cap F)\cup(B\cap G),
		\]
		a union of closed subsets of $X$. Hence $f^{-1}(C)$ is closed for every closed $C$, so $f$ is continuous.
	\end{proof}

\textit{Counterexample.}
Let \(X=(0,2]\) with the subspace topology from \(\mathbb{R}\).
Take \(A=(0,1)\) (not closed in \(X\)) and \(B=[1,2]\) (closed).

Define \(g\equiv 0\) on \(A\) and \(h\equiv 1\) on \(B\).
They agree on \(A\cap B=\varnothing\), so the glued map
\[
f(x)=
\begin{cases}
	0, & x\in A,\\[4pt]
	1, & x\in B
\end{cases}
\]
is well-defined.

For the open set \(U=\bigl(\tfrac12,\tfrac32\bigr)\subset\mathbb{R}\) we have
\[
f^{-1}(U)=B=[1,2],
\]
which is not open in \(X\) (every neighborhood of \(1\) in \(X\) meets \(A\)).

Thus \(f\) is not continuous.

	If $A$ and $B$ are both \emph{open} in $X$, then for any open $U\subseteq Y$,
	\[
	f^{-1}(U)=(A\cap g^{-1}(U))\cup(B\cap h^{-1}(U)),
	\]
	and each term is open in $X$ (since $g^{-1}(U)$ is open in $A$, it equals $A\cap G$ for some open $G\subseteq X$).
	Hence $f$ is continuous when $A,B$ form an open cover as well.
```

## CP-II-0406

- chapter line: 6813

```tex
\label{prob:cp-ii-0406}
Connected sums \(\#^k(S^3\times S^3)\) (dimension \(6\))

Let
\[
M=\#^k(S^3\times S^3).
\]
Then \(M\) is closed oriented of dimension \(6\), and the middle degree is \(3\).
For connected sums in dimension \(\ge 3\),
\[
H_3\!\left(\#^k(S^3\times S^3);\mathbb Q\right)
\cong
\bigoplus_{j=1}^k H_3(S^3\times S^3;\mathbb Q)
\cong
(\mathbb Q^2)^{\oplus k}\cong \mathbb Q^{2k}.
\]
Thus
\[
\dim_{\mathbb Q} H_3(M;\mathbb Q)=2k,
\]
again even. This gives a large family where the middle Betti number can be any even integer.

\subsubsection{Example 5: Products \(\Sigma_g\times S^{4n}\) (general \(n\ge 1\))}

Let \(n\ge 1\) and set
\[
M=\Sigma_g\times S^{4n}.
\]
Then \(\dim M=2+4n=4n+2\), and the middle degree is \(2n+1\).
By K\"unneth over \(\mathbb Q\),
\[
H_{2n+1}(M;\mathbb Q)
\cong
\bigoplus_{i+j=2n+1} H_i(\Sigma_g;\mathbb Q)\otimes H_j(S^{4n};\mathbb Q).
\]
But the only nonzero rational homology of \(S^{4n}\) is in degrees \(0\) and \(4n\), so the only possible
summands would require \(j=0\) or \(j=4n\), i.e.
\[
i=2n+1 \quad \text{or}\quad i=2n+1-4n=1-2n.
\]
For \(n\ge 1\), both indices are impossible for \(\Sigma_g\) (the first is \(>2\), the second is negative), so
\[
H_{2n+1}(\Sigma_g\times S^{4n};\mathbb Q)=0.
\]
Hence the middle Betti number is \(0\), which is even.

The evenness argument uses a nondegenerate \emph{alternating} pairing on \(H^{2n+1}(M;\mathbb Q)\).
Over a field of characteristic \(2\), Ă˘â‚¬Ĺ›skew-symmetricĂ˘â‚¬ĹĄ and Ă˘â‚¬Ĺ›symmetricĂ˘â‚¬ĹĄ coincide, and one can no longer
conclude that the dimension must be even. This is why the clean parity statement is formulated over
\(\mathbb Q\) (or any field of characteristic \(\neq 2\)).

An \(n\)-manifold \(M\) is \textbf{closed} if it is \emph{compact} and has \emph{empty boundary}:
\[
M \text{ closed}\quad \Longleftrightarrow\quad M \text{ compact and }\partial M=\varnothing.
\]
Examples: \(S^n\), \(T^n\), \(\mathbb{CP}^m\).
Non-examples: \(D^n\) (has boundary), \(\mathbb R^n\) (not compact).

A manifold \(M\) is \textbf{orientable} if one can choose a consistent orientation on all coordinate
charts (equivalently, all transition maps between oriented charts have positive Jacobian determinant in the smooth case).
There are several equivalent algebraic-topological characterizations.

\begin{remark}[Homology characterization for closed connected manifolds]
	If \(M\) is a connected closed \(n\)-manifold, then
	\[
	M \text{ orientable}\quad \Longleftrightarrow\quad H_n(M;\mathbb Z)\cong \mathbb Z,
	\]
	and
	\[
	M \text{ nonorientable}\quad \Longleftrightarrow\quad H_n(M;\mathbb Z)=0.
	\]
\end{remark}

Saying that \(M\) is \textbf{\(\mathbb Z\)-orientable} means that \(M\) admits a fundamental class with integer coefficients.
For a connected closed \(n\)-manifold this is exactly the usual notion of orientability:
\[
\mathbb Z\text{-orientable}\quad \Longleftrightarrow\quad \text{orientable}.
\]

Let \(F\) be a field. A connected closed \(n\)-manifold \(M\) is called \textbf{\(F\)-orientable} if it admits a fundamental class
\([M]_F\in H_n(M;F)\), equivalently
\[
H_n(M;F)\cong F.
\]
In particular, \(M\) is \textbf{\(\mathbb Q\)-orientable} if
\[
H_n(M;\mathbb Q)\cong \mathbb Q.
\]

\begin{remark}[Relations between \(\mathbb Z\)- and \(\mathbb Q\)-orientability]
	For closed connected manifolds one has
	\[
	\mathbb Z\text{-orientable}\ \Longrightarrow\ \mathbb Q\text{-orientable}.
	\]
	Moreover, since \(\mathbb Q\) has characteristic \(\neq 2\), for manifolds one actually has the equivalence
	\[
	\mathbb Q\text{-orientable}\ \Longleftrightarrow\ \mathbb Z\text{-orientable}\ \Longleftrightarrow\ \text{orientable}.
	\]
\end{remark}

Over the field \(\mathbb F_2\), signs disappear (\(-1=+1\)), and every manifold becomes orientable.

\begin{remark}[\(\mathbb F_2\)-orientability]
	Every connected closed manifold \(M\) is \(\mathbb F_2\)-orientable:
	\[
	H_n(M;\mathbb F_2)\cong \mathbb F_2.
	\]
	For example, \(\mathbb{RP}^2\) is not \(\mathbb Z\)-orientable (so \(H_2(\mathbb{RP}^2;\mathbb Z)=0\)),
	but it is \(\mathbb F_2\)-orientable (so \(H_2(\mathbb{RP}^2;\mathbb F_2)\cong \mathbb F_2\)).
\end{remark}

Let \(M\) be a connected closed \(n\)-manifold and let \(F\) be a field.
If \(M\) is \(F\)-orientable, then Poincar\'e duality holds with coefficients in \(F\):
\[
H^i(M;F)\cong H_{n-i}(M;F),
\]
via cap product with the fundamental class \([M]_F\).
In particular:

	\par\noindent\textbullet\quad If \(M\) is orientable, then duality holds over \emph{any} field \(F\) (including \(\mathbb Q\)).
	\par\noindent\textbullet\quad For an arbitrary (possibly nonorientable) manifold, duality always holds over \(\mathbb F_2\).

For connected closed manifolds:
\[
\text{orientable}\ \Longleftrightarrow\ \mathbb Z\text{-orientable}\ \Longleftrightarrow\ \mathbb Q\text{-orientable},
\]
while
\[
\text{every manifold is } \mathbb F_2\text{-orientable}.
\]
```

## CP-II-0411

- chapter line: 6966

```tex
\label{prob:cp-ii-0411}
Finite Products of Metrizable Spaces

Show that a finite product of metrizable topological spaces is metrizable. (Hint: start with two metric spaces and define a metric on the product.)

Let $(X,d)$ and $(Y,e)$ be metric spaces. Set $\displaystyle d_1(x,x')=\min\{1,d(x,x')\}$ and $\displaystyle e_1(y,y')=\min\{1,e(y,y')\}$, which induce the same topologies as $d$ and $e$ but are bounded by $1$.
Define
\[
D\big((x,y),(x',y')\big)=d_1(x,x')+e_1(y,y').
\]
Then $D$ is a metric on $X\times Y$.

We claim that the topology induced by $D$ equals the product topology.

(i) If $D((x,y),(x',y'))<r$, then $d_1(x,x')<r$ and $e_1(y,y')<r$, hence
\[
B_D((x,y),r)\subseteq B_{d_1}(x,r)\times B_{e_1}(y,r),
\]
so every $D$-open set is product-open.

(ii) Conversely, let $U=B_{d_1}(x,\alpha)$ and $V=B_{e_1}(y,\beta)$. For $r=\min\{\alpha,\beta\}/2$ we have
\[
B_D((x,y),r)\subseteq U\times V,
\]
so every basic product-open set is $D$-open.

Thus the two topologies coincide, and $X\times Y$ is metrizable.

If $(X_i,d_i)$ for $i=1,\dots,n$ are metric,

 define on $X=\prod_{i=1}^n X_i$ the metric
\[
D\big((x_i),(x_i')\big)=\sum_{i=1}^n \min\{1,d_i(x_i,x_i')\}.
\]
Exactly the same containment argument shows that $D$ induces the product topology on $X$. Hence any finite product of metrizable spaces is metrizable.

	\par\noindent\textbullet\quad $\mathbb{R}^n$ is metrizable (finite product of $(\mathbb{R},|\cdot|)$).
	\par\noindent\textbullet\quad A finite product of discrete spaces is again discrete (hence metrizable).
	\par\noindent\textbullet\quad $S^1\times[0,1]$ is metrizable; for instance, with
	\[
	d\big((\theta,t),(\phi,s)\big)
	=\sqrt{\,d_{S^1}(\theta,\phi)^2 + |t-s|^2\,},
	\]
	where $d_{S^1}$ is the arc-length distance on the circle.
```

## CP-II-0413

- chapter line: 7013

```tex
\label{prob:cp-ii-0413}
— Stability of translations and difference quotients

Let
\[
X\in\bigl\{\mathcal D(\mathbb R^n),\ \mathcal S(\mathbb R^n),\ \mathcal E(\mathbb R^n)\bigr\},
\qquad \phi\in X.
\]
Establish the following properties.

\bigskip

\textbf{(a)} If $x_\ell\in\mathbb R^n$ with $x_\ell\to0$, then
\[
\tau_{x_\ell}\phi\longrightarrow\phi
\qquad\text{in }X\text{ as }\ell\to\infty,
\]
where the translation operator $\tau_x$ is defined by
\[
(\tau_x\phi)(y):=\phi(y-x).
\]

\bigskip

\textbf{(b)} If $h_\ell\in\mathbb R$ with $h_\ell\to0$, then
\[
\Delta_i^{h_\ell}\phi\longrightarrow D_i\phi
\qquad\text{in }X\text{ as }\ell\to\infty,
\]
where
\[
\Delta_i^{h}\phi
:=h^{-1}\bigl(\tau_{h e_i}\phi-\phi\bigr)
=\frac{\phi(\cdot-h e_i)-\phi}{h}
\]
is the \emph{difference quotient} in the $i$-th coordinate direction.

\bigskip

In words: small translations of a smooth function tend to zero in the topology of $X$, and the difference quotients converge to the partial derivative $D_i\phi$ in the same sense.

\bigskip

\textit{Case $X=\mathcal E(\mathbb R^n)$.}
Fix a compact $K\Subset\mathbb R^n$ and $m\in\mathbb N$. For any multi-index $\alpha$ with $|\alpha|\le m$,
\[
\sup_{y\in K}\big|D^\alpha(\tau_{x_\ell}\phi-\phi)(y)\big|
=\sup_{y\in K}\big|D^\alpha\phi(y-x_\ell)-D^\alpha\phi(y)\big|.
\]
Choose a compact $K'$ containing $K\cup(K-x_\ell)$ for all large $\ell$. Since $D^\alpha\phi$ is uniformly continuous on $K'$, the right-hand side tends to $0$ as $\ell\to\infty$. Hence $\tau_{x_\ell}\phi\to\phi$ in $\mathcal E$.

\bigskip

\textit{Case $X=\mathcal D(\mathbb R^n)$.}
Choose a compact $K$ with $\operatorname{supp}\phi\subset K^\circ$. For $\ell$ large,
\[
\operatorname{supp}(\tau_{x_\ell}\phi)\subset K+x_\ell\subset K'',
\]
for some fixed compact $K''$. Applying the estimate from the $\mathcal E$ case on $K''$ yields, for every $m$,
\[
\sup_{y\in K''}\big|D^\alpha(\tau_{x_\ell}\phi-\phi)(y)\big|\xrightarrow[\ell\to\infty]{}0
\quad\text{for all }|\alpha|\le m,
\]
and the supports remain in the common compact $K''$. Therefore $\tau_{x_\ell}\phi\to\phi$ in $\mathcal D$.

\bigskip

\textit{Case $X=\mathcal S(\mathbb R^n)$.}
For any $\alpha,\beta$,
\[
x^\alpha D^\beta\big(\tau_{x_\ell}\phi-\phi\big)(x)
=(x^\alpha-(x-x_\ell)^\alpha)D^\beta\phi(x-x_\ell)
+(x-x_\ell)^\alpha\big(D^\beta\phi(x-x_\ell)-D^\beta\phi(x)\big).
\]
The polynomial difference satisfies
\[
|x^\alpha-(x-x_\ell)^\alpha|\le C_\alpha |x_\ell|\,(1+|x|)^{|\alpha|-1},
\]
and all derivatives of $\phi$ are rapidly decreasing; hence the first term tends to $0$ uniformly in $x$.
For the second term, the uniform continuity of $D^\beta\phi$ together with rapid decrease implies that, for every $N$,
\[
\sup_{x\in\mathbb R^n}(1+|x|)^{-N}\,
\big|x^\alpha D^\beta\big(\tau_{x_\ell}\phi-\phi\big)(x)\big|\longrightarrow 0
\qquad (\ell\to\infty).
\]
Thus every Schwartz seminorm goes to $0$, and $\tau_{x_\ell}\phi\to\phi$ in $\mathcal S(\mathbb R^n)$.

\bigskip

Fix $i$ and a multi-index $\alpha$. For any $h\neq 0$,
\[
D^\alpha\Delta_i^{h}\phi
=\frac{D^\alpha\phi(\,\cdot-h e_i)-D^\alpha\phi}{h}.
\]

\medskip

\textit{Case $X=\mathcal E$ (and inside a fixed $\mathcal D_K\subset\mathcal D$).}
Let $K\Subset\mathbb R^n$. By the mean value theorem along $e_i$,
\[
\frac{D^\alpha\phi(x-he_i)-D^\alpha\phi(x)}{h}-D^{\alpha+e_i}\phi(x)
=\int_0^1\big(D^{\alpha+e_i}\phi(x-th e_i)-D^{\alpha+e_i}\phi(x)\big)\,dt.
\]
Hence
\begin{center}
\resizebox{\linewidth}{!}{$\displaystyle
\sup_{x\in K}\left|D^\alpha\Delta_i^h\phi(x)-D^{\alpha+e_i}\phi(x)\right|
\le \sup_{0\le t\le 1}\ \sup_{x\in K}
\left|D^{\alpha+e_i}\phi(x-th e_i)-D^{\alpha+e_i}\phi(x)\right|
\longrightarrow 0 \quad \text{as } h\to 0.
$}
\end{center}
For $\mathcal D$, the supports remain in a common compact set for $|h|$ small, so the same uniform estimate yields convergence in $\mathcal D$.

\bigskip

\textit{Case $X=\mathcal S$.}
For any $\alpha,\beta$,
\[
x^\beta\big(D^\alpha\Delta_i^{h}\phi-D^{\alpha+e_i}\phi\big)(x)
= A_{\alpha,\beta,h}(x)+B_{\alpha,\beta,h}(x),
\]
where
\[
A_{\alpha,\beta,h}(x)
=\frac{x^\beta-(x-he_i)^\beta}{h}\,
\]
\[
B_{\alpha,\beta,h}(x)
=(x-he_i)^\beta\!\left(\frac{D^\alpha\phi(x-he_i)-D^\alpha\phi(x)}{h}-D^{\alpha+e_i}\phi(x)\right).
\]
\medskip

For $A_{\alpha,\beta,h}$, expand the polynomial difference:
\[
\frac{x^\beta-(x-he_i)^\beta}{h}
=\sum_{|\gamma|\le |\beta|-1} c_{\beta,\gamma}(h)\,x^\gamma, \qquad |c_{\beta,\gamma}(h)|\le C_\beta,
\]
so that
\[
|A_{\alpha,\beta,h}(x)|
\le C_\beta (1+|x|)^{|\beta|-1}\,|D^\alpha\phi(x-he_i)|.
\]
Since $D^\alpha\phi$ is rapidly decreasing, the right-hand side defines a family bounded in every Schwartz seminorm and tends to $0$ as $h\to0$.

\medskip

For $B_{\alpha,\beta,h}$, the integral remainder form of the mean value theorem gives
\[
\frac{D^\alpha\phi(x-he_i)-D^\alpha\phi(x)}{h}-D^{\alpha+e_i}\phi(x)
=\int_0^1\!\big(D^{\alpha+e_i}\phi(x-th e_i)-D^{\alpha+e_i}\phi(x)\big)\,dt,
\]
whence
\[
|B_{\alpha,\beta,h}(x)|
\le (1+|x|)^{|\beta|}\int_0^1
\big|D^{\alpha+e_i}\phi(x-th e_i)-D^{\alpha+e_i}\phi(x)\big|\,dt.
\]
The integrand tends to $0$ uniformly in $x$ by the uniform continuity of $D^{\alpha+e_i}\phi$, and the polynomial factor is absorbed by the rapid decay of the derivatives of $\phi$. Consequently, for every pair $(\alpha,\beta)$,
\[
q_{\alpha,\beta}(\Delta_i^{h}\phi-D_i\phi)\longrightarrow 0 \qquad (h\to0).
\]

\bigskip

This proves $\Delta_i^{h}\phi\to D_i\phi$ in $\mathcal E$, $\mathcal D$, and $\mathcal S$.

\bigskip
Let $\phi(x)=e^{-|x|^2}\in\mathcal S(\mathbb R^n)$. Then, for any translation vector $x_\ell\to0$,
\[
(\tau_{x_\ell}\phi)(y)=e^{-|y-x_\ell|^2}
\longrightarrow e^{-|y|^2}=\phi(y)
\]
together with all derivatives, because every derivative of $\phi$ is a polynomial times $e^{-|y|^2}$,
which is uniformly continuous and rapidly decreasing. Hence each Schwartz seminorm
\[
q_{\alpha,\beta}(\tau_{x_\ell}\phi-\phi)
=\sup_{y\in\mathbb R^n}|\,y^\alpha D^\beta(\tau_{x_\ell}\phi-\phi)(y)\,|
\]
tends to $0$ as $\ell\to\infty$.

\medskip

For the difference quotient,
\[
\Delta_i^{h}\phi(x)=\frac{\phi(x-h e_i)-\phi(x)}{h},
\]
Taylor's theorem gives
\[
\phi(x-h e_i)=\phi(x)-h\,D_i\phi(x)+\tfrac{h^2}{2}D_i^2\phi(x-\theta h e_i),
\qquad 0<\theta<1,
\]
so that
\[
\Delta_i^{h}\phi(x)-D_i\phi(x)
=\tfrac{h}{2}\,D_i^2\phi(x-\theta h e_i)\to0
\]
uniformly with all derivatives. Therefore $\Delta_i^{h}\phi\to D_i\phi$ in $\mathcal S(\mathbb R^n)$.

\bigskip
\bigskip
Let $\phi\in\mathcal D(\mathbb R)$ be compactly supported in $[-1,1]$. For small $|h|$,
\[
\operatorname{supp}(\phi(\cdot-h))\subset[-1+h,1+h]\subset[-2,2].
\]
Hence every difference quotient
\[
\Delta^{h}\phi(x)=\frac{\phi(x-h)-\phi(x)}{h}
\]
has support contained in a fixed compact interval, and all derivatives converge uniformly:
\[
\sup_{x\in[-2,2]}|D^m(\Delta^{h}\phi-\phi')(x)|\longrightarrow0
\quad\text{as }h\to0.
\]
Thus $\Delta^{h}\phi\to\phi'$ in the $\mathcal D$-topology.

\bigskip
```

## CP-II-0415

- chapter line: 7233

```tex
\label{prob:cp-ii-0415}
On $C^\infty(\mathbb R^n)$, the seminorms
	$p_{K,m}(f)=\sup_{x\in K,\,|\alpha|\le m}|D^\alpha f(x)|$ (compact $K$, $m\in\mathbb N$)
	generate the usual Fréchet topology. Convergence $f_k\to f$ means
	$p_{K,m}(f_k-f)\to0$ for all $K,m$ (uniform convergence of all derivatives on compacts).

	\bigskip
```

## CP-II-0424

- chapter line: 7243

```tex
\label{prob:cp-ii-0424}
s.

\par\noindent\textbullet\quad For $1\le p\le\infty$, the \textbf{weak topology} on $L^{p}(\Omega)$ is
		$\sigma(L^{p},L^{p'})$: the coarsest topology making all linear functionals
		\[
		T_h(f)\;:=\;\int_{\Omega} f\,h\,d\mu
		\qquad (\,h\in L^{p'}(\Omega)\,)
		\]
		continuous.

		\vspace{0.25em}
		A sequence $f_j$ converges weakly to $f$ iff
		\[
		\int_{\Omega} f_j\,h\,d\mu \;\longrightarrow\; \int_{\Omega} f\,h\,d\mu
		\qquad \text{for every } h\in L^{p'}.
		\]

	\medskip
	\noindent\emph{Reflexivity.}
	If $1<p<\infty$, $L^{p}$ is reflexive; hence bounded sets are relatively weakly compact
	(Banach--Alaoglu + Eberlein--\v{S}mulian). For $p=1$ or $p=\infty$ this fails in general.

	\medskip
	\noindent\emph{Indicators and density.}
	Let $\mathcal S$ denote the linear span of indicators of bounded measurable sets:
	\[
	\mathcal S := \left\{\, g=\sum_{k=1}^{m} a_k\,\mathbf 1_{E_k}\ :\ m<\infty,\ a_k\in\mathbb R,\ \mu(E_k)<\infty \,\right\}.
	\]
	Then $\mathcal S$ is exactly the class of bounded simple functions with bounded support,
	and for $1<p<\infty$ one has the density
	\[
	\overline{\mathcal S}^{\,L^{p'}} = L^{p'}(\Omega).
	\]

	\noindent\emph{Proof sketch of density.}
	Given $h\in L^{p'}$, define the truncations $h^N := h\,\mathbf 1_{\{|h|\le N\}\cap B_N}$,
	where $B_N$ is a set of finite measure increasing to $\Omega$ (e.g.\ balls of radius $N$ if $\Omega=\mathbb R^n$).
	Then $\|h-h^N\|_{p'}\to0$ by dominated convergence and monotone convergence.
	Each bounded, finitely supported $h^N$ is approximated in $L^{p'}$ by simple functions via range partitioning:
	$h^N=\lim_{m\to\infty}\sum_\ell c_{\ell,m}\,\mathbf 1_{E_{\ell,m}}$.
	Hence $\mathcal S$ is dense.

	\medskip
	\noindent\emph{Consequences.}
	If $(f_j)$ is bounded in $L^{p}$ and $\int (f_j-f)\,\mathbf 1_E\to0$ for every bounded $E$,
	then by linearity the convergence holds for all $g\in\mathcal S$; by density and H\"older,
	\[
	\Big|\!\int (f_j-f)h\Big|
	\le \Big|\!\int (f_j-f)g\Big| + \|f_j-f\|_{p}\,\|h-g\|_{p'} \;\xrightarrow[j\to\infty]{}\; \|f_j-f\|_{p}\,\|h-g\|_{p'}.
	\]
	Let $g\to h$ in $L^{p'}$ to conclude $\int (f_j-f)h\to0$ for all $h\in L^{p'}$, i.e.\ $f_j\rightharpoonup f$.

	\bigskip
```

## CP-II-0426

- chapter line: 7300

```tex
\label{prob:cp-ii-0426}
\par\noindent\textbullet\quad Every compactly supported smooth function is Schwartz, so
	$\mathcal{D}(\mathbb{R}^n)\subset\mathcal{S}(\mathbb{R}^n)$.
```

## CP-II-0434

- chapter line: 7306

```tex
\label{prob:cp-ii-0434}
\par\noindent (ii)\quad Using the definition of compactness, show that $X$ is not compact.
```

## CP-II-0441

- chapter line: 7311

```tex
\label{prob:cp-ii-0441}
\par\noindent\textbullet\quad \textbf{Completeness with $\|\cdot\|_{1}$.}
	Since $\|\cdot\|_{1}$ is not a norm on the pointwise space $R([0,1])$, completeness as a normed space
	is not applicable. Passing to equivalence classes a.e.\ gives $L^{1}$, which is complete.
```

## CP-II-0443

- chapter line: 7318

```tex
\label{prob:cp-ii-0443}
Let $f(x) = \sin(x)$ on $E=[0,100]$.
		$E$ is compact, $f$ is continuous, hence uniformly continuous.
```

## CP-II-0445

- chapter line: 7324

```tex
\label{prob:cp-ii-0445}
\par\noindent *d)\quad By considering a suitable sequence of functions $f$, or otherwise,
	deduce that there exists no constant $C$, independent of $u$, such that
	the estimate
	\[
	\sup_{S_T} (|u|+|u_t|)
	\le C \sup_{\Sigma_0} (|u|+|u_t|)
	\]
	holds for all solutions $u\in C^2(S_T)$ of the wave equation which vanish
	for large $|x|$.

\par\medskip\noindent\textbf{\textbf{Goal.}}\quad
Show that if $u(r,t) = v(r,t)/r$ is radial, then $u$ solves
$-u_{tt} + \Delta u = 0$ on $\mathbb{R}^3_*\times(-T,T)$ if and only if
$v$ solves the one-dimensional wave equation
$-v_{tt}+v_{rr}=0$ on $(0,\infty)\times(-T,T)$.

\par\medskip\noindent\textbf{\textbf{Computation.}}\quad
Let $u(r,t) = v(r,t)/r$. Then
\[
u_r = \frac{v_r}{r} - \frac{v}{r^2},
\qquad
u_{rr}
= \frac{v_{rr}}{r} - \frac{2v_r}{r^2} + \frac{2v}{r^3},
\qquad
u_{tt} = \frac{v_{tt}}{r}.
\]
Using the radial Laplacian,
\[
\Delta u
= u_{rr} + \frac{2}{r}u_r
= \left(\frac{v_{rr}}{r} - \frac{2v_r}{r^2} + \frac{2v}{r^3}\right)
+ \frac{2}{r}\left(\frac{v_r}{r} - \frac{v}{r^2}\right)
= \frac{v_{rr}}{r}.
\]
Thus the wave equation
\[
-u_{tt} + \Delta u = 0
\]
becomes
\[
-\frac{v_{tt}}{r} + \frac{v_{rr}}{r} = 0
\quad\Longleftrightarrow\quad
-v_{tt} + v_{rr} = 0,
\]
for $r>0$. This proves the equivalence.

\par\medskip\noindent\textbf{\textbf{Goal.}}\quad
Use d'Alembert's formula for the one-dimensional wave equation to
construct radial solutions in $\mathbb{R}^3$.

\par\medskip\noindent\textbf{\textbf{D'Alembert solution.}}\quad
For the one-dimensional wave equation $-v_{tt}+v_{rr}=0$ on $\mathbb{R}$,
the general solution is
\[
v(r,t) = f(r+t) + g(r-t),
\]
for some functions $f,g$.

\par\medskip\noindent\textbf{\textbf{Conclusion.}}\quad
If $f,g\in C_c^2(\mathbb{R})$, set
\[
v(r,t) = f(r+t) + g(r-t),
\qquad
u(r,t) = \frac{v(r,t)}{r}
= \frac{f(r+t)}{r} + \frac{g(r-t)}{r}.
\]
Then $v$ solves the one-dimensional wave equation, and by part~(a),
$u$ solves the three-dimensional wave equation on $S_{*,T}$.

Since $f,g$ are compactly supported, there exists $R>0$ such that
$f(s)=g(s)=0$ whenever $|s|\ge R$. For fixed $t\in(-T,T)$ and for $r$
sufficiently large, both $r+t$ and $r-t$ lie outside the supports of
$f$ and $g$, so $u(r,t)=0$. Hence $u$ vanishes for large $|x|$.

\par\medskip\noindent\textbf{\textbf{Goal.}}\quad
Assume $f\in C_c^3(\mathbb{R})$ is odd ($f(-s)=-f(s)$). Show that
\[
u(r,t) := \frac{f(r+t)+f(r-t)}{2r}
\]
extends to a $C^2$ solution on $S_T$ and satisfies $u(0,t)=f'(t)$.

\par\medskip\noindent\textbf{\textbf{Construction.}}\quad
Define
\[
v(r,t) := \frac12\bigl(f(r+t)+f(r-t)\bigr).
\]
Then $v\in C^3$ and solves $-v_{tt}+v_{rr}=0$ on $(0,\infty)\times(-T,T)$.
By part~(a), $u(r,t)=v(r,t)/r$ solves the wave equation on
$\mathbb{R}^3_*\times(-T,T)$.

Because $f$ is odd,
\[
v(0,t)
= \frac12\bigl(f(t)+f(-t)\bigr)
= \frac12\bigl(f(t)-f(t)\bigr)
= 0.
\]
Thus $v(r,t)$ vanishes at $r=0$ for each $t$.

Differentiating,
\[
v_r(r,t) = \frac12\bigl(f'(r+t)+f'(r-t)\bigr),
\]
so
\[
v_r(0,t)
= \frac12\bigl(f'(t)+f'(-t)\bigr).
\]
Since $f$ is odd, $f'$ is even, hence $f'(-t)=f'(t)$ and
\[
v_r(0,t) = f'(t).
\]

\par\medskip\noindent\textbf{\textbf{Extension and regularity.}}\quad
Near $r=0$ we have the Taylor expansion
\[
v(r,t) = v_r(0,t)\,r + O(r^3) = f'(t)\,r + O(r^3),
\]
so
\[
u(r,t) = \frac{v(r,t)}{r} = f'(t) + O(r^2),
\]
which has a finite limit as $r\to0$. Define
\[
u(0,t) := f'(t).
\]
This defines a $C^2$ function $u$ on $S_T$ which coincides with the
radial solution for $r>0$ and therefore solves the wave equation on all
of $S_T$.

\par\medskip\noindent\textbf{\textbf{Claim.}}\quad
There is no constant $C>0$ such that
\[
\sup_{S_T} (|u|+|u_t|)
\le C \sup_{\Sigma_0} (|u|+|u_t|),
\]
for all solutions $u\in C^2(S_T)$ of the wave equation that vanish for
large $|x|$.

\par\medskip\noindent\textbf{\textbf{Reduction to a one-dimensional inequality.}}\quad
For solutions of the form in part~(c),
\[
u(r,t) = \frac{f(r+t)+f(r-t)}{2r}
\]
with $f\in C_c^3(\mathbb{R})$ odd, we have
\[
u(0,t) = f'(t).
\]
At $t=0$,
\[
u(r,0) = \frac{f(r)+f(r)}{2r} = \frac{f(r)}{r},
\qquad
u_t(r,0) = 0,
\]
since $f'$ is even. Therefore,
\[
\sup_{\Sigma_0} (|u|+|u_t|)
= \sup_{r>0}\left|\frac{f(r)}{r}\right|.
\]
On the other hand,
\[
\sup_{S_T} (|u|+|u_t|)
\ge \sup_{t\in(-T,T)} |u(0,t)|
= \sup_{t\in(-T,T)} |f'(t)|.
\]

If the estimate above held for all such $u$, then for all odd
$f\in C_c^3(\mathbb{R})$ we would have
\[
\sup_{t\in(-T,T)} |f'(t)|
\le C \sup_{r>0}\left|\frac{f(r)}{r}\right|.
\tag{$\dagger$}
\]

\par\medskip\noindent\textbf{\textbf{Construction of a contradicting sequence.}}\quad
Fix a nonzero $\psi\in C_c^3(\mathbb{R})$ supported in $(-1,1)$, and
define for $R>1$:
\[
f_R(s) := \psi(s-R) - \psi(-s-R).
\]
Then $f_R\in C_c^3(\mathbb{R})$ is odd (one checks $f_R(-s)=-f_R(s)$),
and its support is contained in two disjoint intervals located near
$s\approx \pm R$.

Since $f_R'$ is just a translate of $\psi'$, we have
\[
\sup_{s\in\mathbb{R}} |f_R'(s)|
= \sup_{s\in\mathbb{R}} |\psi'(s)| =: M > 0,
\]
independent of $R$.

However, for $s$ in the support of $f_R$ we have $|s|\ge R-1$, so
\[
\left|\frac{f_R(s)}{s}\right|
\le \frac{\sup_{|y|\le 1}|\psi(y)|}{R-1},
\]
and hence
\[
\sup_{r>0}\left|\frac{f_R(r)}{r}\right|
\le \frac{C_0}{R-1},
\]
for some constant $C_0$ independent of $R$.

\par\medskip\noindent\textbf{\textbf{Contradiction.}}\quad
If $(\dagger)$ held for all odd $f$, it would hold for $f_R$:
\[
M \le C \sup_{r>0}\left|\frac{f_R(r)}{r}\right|
\le C\,\frac{C_0}{R-1}.
\]
Letting $R\to\infty$ forces the right-hand side to $0$, while $M>0$ is
fixed. This is impossible, and therefore no such constant $C$ can exist.

\par\medskip\noindent\textbf{\textbf{Conclusion.}}\quad
The wave equation in three dimensions does not satisfy a global
maximum-principle-type estimate of the form above; the size of the
solution at later times cannot be controlled solely by the supremum of
its initial data.
```

## CP-II-0453

- chapter line: 7545

```tex
\label{prob:cp-ii-0453}
Extra Examples and Sequential Spaces

In the co-countable topology on an uncountable set $X$, a sequence converges iff it is eventually constant.
	Hence every subset $A\subseteq X$ is sequentially closed, while the closed sets are exactly the countable subsets and $X$ itself.

		\par\noindent\textbullet\quad $X=\mathbb{R}$, $A=\mathbb{R}\setminus\mathbb{Q}$: sequentially closed, not closed.
		\par\noindent\textbullet\quad $X=\mathbb{R}$, $A=(0,1)\cup\{\pi\}$: sequentially closed, not closed.
		\par\noindent\textbullet\quad $X$ uncountable, $A=X\setminus C$ with nonempty countable $C$: sequentially closed, not closed.
		\par\noindent\textbullet\quad Any countably infinite $C\subset X$ is closed; its sequential closure equals $C$.

	\emph{Non-example.} If $X$ is finite with the co-countable topology, then $X$ is discrete; sequentially closed sets are exactly the closed sets.

	In every second countable space (hence first countable), $A$ is sequentially closed iff $A$ is closed.

		\par\noindent\textbullet\quad $\mathbb{R}^n$: $(0,1)$ is not sequentially closed (since $1/n\to0\notin(0,1)$); $[0,1]$ is sequentially closed (closed).
		\par\noindent\textbullet\quad Any metric space (Polish spaces, manifolds, graphs with path metric, metric CW-complexes): same equivalence.
		\par\noindent\textbullet\quad Subspaces of second countable spaces: e.g.\ $S^1\subset\mathbb{R}^2$. The set $S^1\setminus\{1\}$ is not sequentially closed (points approach $1$).
		\par\noindent\textbullet\quad Countable products of second countable spaces (e.g.\ $\mathbb{R}^{\mathbb N}$ with product topology): still second countable; sequentially closed $\Leftrightarrow$ closed.

	\emph{Non-examples.} For uncountable $I$, $\mathbb{R}^I$ (product topology) is not second countable; there are subsets whose topological closure strictly contains their sequential closure. Likewise, $\mathbb{R}$ with the co-countable topology is not first/second countable; every set is sequentially closed but many are not closed.

	\begin{definition}
		A topological space $X$ is \emph{sequential} if for all $A\subseteq X$,
		\[
		\overline{A}=\operatorname{scl}(A),
		\]
		i.e.\ $A$ is closed iff $A$ is sequentially closed.
	\end{definition}

		\par\noindent\textbullet\quad Every first countable space (in particular, every metric or second countable space) is sequential.
		\par\noindent\textbullet\quad The Arens--Fort space is sequential but not first countable.
		\par\noindent\textbullet\quad Quotients of metric spaces are sequential.
		\par\noindent\textbullet\quad Products of sequential spaces need not be sequential.

		\par\noindent\textbullet\quad The Tikhonoff cube $[0,1]^I$ with $I$ uncountable is not sequential.
		\par\noindent\textbullet\quad The Stone--\v{C}ech compactification $\beta\mathbb{N}$ is not sequential.
		\par\noindent\textbullet\quad The Fortissimo space is not sequential (fails countable tightness).
		\par\noindent\textbullet\quad $\mathbb{R}$ with the co-countable topology is not sequential (every set is sequentially closed, many are not closed).

	\begin{definition}
		Let $f:X\to Y$ be a map between topological spaces.

			\par\noindent\textbullet\quad $f$ is \emph{sequentially continuous at $x\in X$} if for every sequence $(x_n)$ with $x_n\to x$ in $X$ we have $f(x_n)\to f(x)$ in $Y$.
			\par\noindent\textbullet\quad $f$ is \emph{continuous} if $f^{-1}(U)$ is open in $X$ for every open $U\subseteq Y$.

	\end{definition}

	\begin{proposition}
		If $X$ is a sequential space (e.g.\ first countable, metric, or second countable), then $f:X\to Y$ is continuous iff it is sequentially continuous.
	\end{proposition}
```

## CP-II-0458

- chapter line: 7599

```tex
\label{prob:cp-ii-0458}
(Degree mod $2$ and surjectivity)

Let $X$ be a compact manifold without boundary and $Y$ a connected manifold with the same dimension as $X$.

	\par\noindent \textbf{(i)}\quad Suppose that $f : X \to Y$ has $\deg_2(f) \neq 0$. Prove that $f$ is onto.
	\par\noindent \textbf{(ii)}\quad If $Y$ is not compact, prove that $\deg_2(f) = 0$ for all smooth maps $f : X \to Y$.

Let $X$ be a compact smooth $n$-manifold without boundary and let $Y$ be a connected smooth $n$-manifold with $\dim X=\dim Y=n$.
Let $f:X\to Y$ be smooth.

\medskip
\noindent\textbf{Regular values and finite fibres.}
A point $y\in Y$ is a \emph{regular value} of $f$ if for every $x\in f^{-1}(y)$ the differential
\[
df_x:T_xX\longrightarrow T_yY
\]
is surjective. Since $\dim X=\dim Y=n$, surjectivity is equivalent to $df_x$ being an isomorphism; equivalently $\det(df_x)\neq 0$ in local coordinates.
By Sard's theorem, regular values exist and form a dense subset of $Y$.
If $y$ is a regular value, then $f^{-1}(y)$ is a $0$-dimensional submanifold of $X$, hence a discrete subset of $X$.
Because $X$ is compact, every discrete subset is finite, so
\[
f^{-1}(y)=\{x_1,\dots,x_k\}\quad\text{for some }k<\infty.
\]

\medskip
\noindent\textbf{Definition of $\deg_2(f)$.}
For any regular value $y\in Y$, define the \emph{degree mod $2$} of $f$ by
\[
\deg_2(f)\;:=\;|f^{-1}(y)|\pmod 2\ \in\ \mathbb Z/2.
\]
Thus $\deg_2(f)=0$ means that $|f^{-1}(y)|$ is even, and $\deg_2(f)=1$ means that $|f^{-1}(y)|$ is odd.
(If $f^{-1}(y)=\varnothing$, then $y$ is automatically a regular value and the above gives $\deg_2(f)=0$.)

\medskip
\noindent\textbf{Why this is well-defined (independence of $y$).}
We show that $|f^{-1}(y)|\pmod 2$ does not depend on the chosen regular value $y$.
Let $y_0,y_1\in Y$ be regular values. Since $Y$ is connected, choose a smooth path $\gamma:[0,1]\to Y$ with $\gamma(0)=y_0$ and $\gamma(1)=y_1$.
By a small perturbation (generic choice), we may assume $\gamma$ is transverse to $f$.
Consider the subset
\[
\widetilde M \;:=\;\{(x,t)\in X\times[0,1]\;:\; f(x)=\gamma(t)\}.
\]
Define $H:X\times[0,1]\to Y\times Y$ by $H(x,t)=(f(x),\gamma(t))$ and let $\Delta\subset Y\times Y$ be the diagonal.
Then $\widetilde M=H^{-1}(\Delta)$, and transversality of $\gamma$ to $f$ implies $H$ is transverse to $\Delta$.
Hence $\widetilde M$ is a smooth submanifold of $X\times[0,1]$ of dimension
\[
\dim(X\times[0,1])-\codim(\Delta)=(n+1)-n=1,
\]
so $\widetilde M$ is a compact smooth $1$-manifold (compactness because $X\times[0,1]$ is compact).

\medskip
\noindent\textbf{Boundary computation.}
A point $(x,t)\in \widetilde M$ lies in the boundary of $X\times[0,1]$ iff $t\in\{0,1\}$, so
\[
\partial \widetilde M \;=\;\widetilde M\cap \bigl(X\times\{0,1\}\bigr)
\;\cong\; f^{-1}(y_0)\;\sqcup\; f^{-1}(y_1).
\]
Therefore
\[
|\partial \widetilde M|=|f^{-1}(y_0)|+|f^{-1}(y_1)|.
\]

\medskip
\noindent\textbf{Lemma (boundary points of a compact $1$-manifold come in pairs).}
Every compact smooth $1$-manifold is a finite disjoint union of circles $S^1$ and closed intervals $[0,1]$.
Each circle has empty boundary, and each interval has exactly two boundary points. Hence every compact $1$-manifold has an even number of boundary points:
\[
|\partial \widetilde M|\equiv 0 \pmod 2.
\]

\medskip
\noindent\textbf{Conclusion (well-definedness).}
Combining the two displays above gives
\[
|f^{-1}(y_0)|+|f^{-1}(y_1)|\equiv 0 \pmod 2,
\]
hence
\[
|f^{-1}(y_0)|\equiv |f^{-1}(y_1)|\pmod 2.
\]
Thus $\deg_2(f)$ is independent of the choice of regular value $y$ and is therefore well-defined.

\medskip
\noindent\textbf{Relation to the usual integer degree (oriented case).}
If $X$ and $Y$ are oriented, one can define the usual degree $\deg(f)\in\mathbb Z$ by
\[
\deg(f)=\sum_{x\in f^{-1}(y)} \operatorname{sign}\bigl(\det(df_x)\bigr),
\]
for any regular value $y$. Reducing this identity modulo $2$ gives
\[
\deg_2(f)\equiv \deg(f)\pmod 2,
\]
since $\operatorname{sign}(\det(df_x))\in\{\pm 1\}\equiv 1 \pmod 2$.
In particular, $\deg_2$ is the ``orientation-free'' version of degree: it is defined without choosing orientations.

	\par\noindent \textbf{(i)}\quad
	Assume for contradiction that $f$ is not onto. Then there exists $y\in Y\setminus f(X)$. For this $y$ we have
	$f^{-1}(y)=\varnothing$. In particular $y$ is a regular value (vacuously), and therefore
	\[
	\deg_2(f)\equiv |f^{-1}(y)|\equiv 0 \pmod 2,
	\]
	contradicting the assumption $\deg_2(f)\neq 0$. Hence $f$ must be onto.

	\par\noindent \textbf{(ii)}\quad
	Since $X$ is compact and $f$ is continuous, the image $f(X)\subset Y$ is compact. If $Y$ is not compact then
	$f(X)\neq Y$, so choose $y\in Y\setminus f(X)$. Then $f^{-1}(y)=\varnothing$, hence (as above) $y$ is a regular value and
	\[
	\deg_2(f)\equiv |f^{-1}(y)|\equiv 0 \pmod 2.
	\]
	Thus $\deg_2(f)=0$ for every smooth map $f:X\to Y$ whenever $Y$ is non-compact.

	\par\noindent\textbullet\quad The antipodal map $A:S^n\to S^n$, $A(x)=-x$, satisfies $|A^{-1}(y)|=1$ for every $y$, hence $\deg_2(A)=1$, so $A$ is onto.
	\par\noindent\textbullet\quad If $Y$ is non-compact and $X$ is compact, then every smooth $f:X\to Y$ has $\deg_2(f)=0$ by part \textbf{(ii)}.
```

## CP-II-0460

- chapter line: 7716

```tex
\label{prob:cp-ii-0460}
{Runge approximation on a punctured domain}{runge-annulus}
	Let $B_r(z)$ be the open disc of radius $r$ about $z\in\mathbb C$, and set
	$U:=B_2(1)\setminus B_1(0)$. Suppose $f$ is holomorphic on $U$.

		\par\noindent (i)\quad Show there exists a sequence converging to $f$ uniformly on compact subsets of $U$.
		\par\noindent (ii)\quad Must there be a sequence of polynomials converging to $f$ uniformly on $U$?
		\par\noindent (iii)\quad If, moreover, $f$ is holomorphic on an open set containing $\overline U$, must there be a sequence
		of polynomials converging to $f$ uniformly on $U$?
```

## CP-II-0467

- chapter line: 7728

```tex
\label{prob:cp-ii-0467}
Let $E\subset\mathbb{R}^n$ be compact and $f:E\to\mathbb{R}^m$ continuous.

\par\noindent\textbullet\quad $f(E)$ is bounded. \textit{Proof.} Each component $f^j$ attains its max/min on $E$.
\par\noindent\textbullet\quad $f(E)$ is closed, hence compact. \textit{Proof.} Use sequential closedness via compactness of $E$.
\par\noindent\textbullet\quad If $E$ is merely closed, $f(E)$ need not be closed; e.g.\ $f(x)=\arctan x$ on $E=\mathbb{R}$.
```

## CP-II-0468

- chapter line: 7737

```tex
\label{prob:cp-ii-0468}
\par\noindent\textbullet\quad On disjoint compact sets $K_1,K_2\subset[0,1]$ there exists $f\in C([0,1])$ with
	$f|_{K_1}\equiv0$ and $f|_{K_2}\equiv1$ (Urysohn on $[0,1]$).
	By Weierstrass, there are polynomials $p_n\to f$ uniformly on $[0,1]$.
```

## CP-II-0471

- chapter line: 7744

```tex
\label{prob:cp-ii-0471}
Norms on $C^1([0,1])$ and $C^1_0([0,1])$

	\par\noindent\textbullet\quad Let $C^{1}([0,1])$ be the vector space of real continuous functions on $[0,1]$ with
	continuous first derivatives. Define functions $\alpha,\beta,\gamma,\delta:C^{1}([0,1])\to\mathbb{R}$ by
	\[
	\alpha(f)=\sup_{x\in[0,1]}|f(x)|+\sup_{x\in[0,1]}|f'(x)|,\qquad
	\beta(f)=\sup_{x\in[0,1]} \big(|f(x)|+|f'(x)|\big),
	\]
	\[
	\gamma(f)=\sup_{x\in[0,1]}|f(x)|,\qquad
	\delta(f)=\sup_{x\in[0,1]}|f'(x)|.
	\]
	Which of these define norms on $C^{1}([0,1])$?
	Out of those that define norms, which pairs are Lipschitz equivalent?

	\par\noindent\textbullet\quad Let $C^{1}_{0}([0,1])$ be the set of functions $f\in C^{1}([0,1])$ such that
	$f(x)=0$ for $x$ in some neighborhood of the end points $0$ and $1$. Verify that
	$C^{1}_{0}([0,1])$ is a vector space. How would your answers in (a) change if we replace
	$C^{1}([0,1])$ by $C^{1}_{0}([0,1])$ (equivalently $C^{1}_{c}((0,1))$)?

\noindent\rule{\linewidth}{0.6pt}

	\par\noindent\textbullet\quad A norm requires positivity, absolute homogeneity, triangle inequality, and
	\emph{definiteness} ($\|f\|=0\Rightarrow f=0$ in the underlying space).
	\par\noindent\textbullet\quad For any functions $A(x),B(x)$:
	$\sup(A+B)\le \sup A+\sup B$ and $\sup A\le \sup(A+B)$, $\sup B\le \sup(A+B)$.
	\par\noindent\textbullet\quad Mean–Value Theorem: $|f(x)-f(t)|\le |x-t|\;\sup|f'|$.
	\par\noindent\textbullet\quad Lipschitz equivalence of norms $\|\cdot\|_a,\|\cdot\|_b$:
	$\exists\,c,C>0$ with $c\|f\|_a\le \|f\|_b\le C\|f\|_a$ for all $f$.

Define
\[
\alpha(f)=\|f\|_\infty+\|f'\|_\infty,\qquad
\beta(f)=\big\|\,|f|+|f'|\,\big\|_\infty,\qquad
\gamma(f)=\|f\|_\infty,\qquad
\delta(f)=\|f'\|_\infty.
\]
Then $\alpha,\beta,\gamma$ are norms on $C^1([0,1])$, while $\delta$ is not (constants have
$\delta=0$ but are nonzero). Moreover,
\[
\beta(f)\le \alpha(f)\le 2\beta(f),
\]
so $\alpha\sim\beta$. The uniform norm $\gamma$ is not equivalent to $\alpha$ or $\beta$:
take smooth spikes $f_n$ with $\|f_n\|_\infty=1$ and $\|f'_n\|_\infty\to\infty$, giving
$\gamma(f_n)=1$ yet $\alpha(f_n)\to\infty$.

The set $C^1_0([0,1])=\{f\in C^1([0,1]): f=0\ \text{on neighborhoods of }0,1\}$ is a vector space.
Now $\delta$ is a norm: if $\|f'\|_\infty=0$, then $f$ is constant; since $f=0$ near an endpoint,
$f\equiv0$. For $f\in C^1_0$ we have $\|f\|_\infty\le \|f'\|_\infty$ (choose $t$ with $f(t)=0$ and apply MVT),
hence
\[
\delta(f)\le \beta(f)\le \alpha(f)\le 2\,\delta(f).
\]
Therefore $\alpha,\beta,\delta$ are pairwise equivalent on $C^1_0([0,1])$, while $\gamma$
is dominated by $\delta$ but not equivalent to it (spike example).
Replacing $C^1_0([0,1])$ by $C^1_c((0,1))$ yields the same conclusions.

\section*{Problem 6: Open and Closed Subsets of $\mathbb{R}^2$}

Which of the following subsets of $\mathbb{R}^2$ with the Euclidean norm are open? Which are closed? (And why?)

	\par\noindent\textbullet\quad $\{(x,0): 0\le x\le 1\}$;
	\par\noindent\textbullet\quad $\{(x,0): 0< x< 1\}$;
	\par\noindent\textbullet\quad $\{(x,y): y\ne 0\}$;
	\par\noindent\textbullet\quad $\{(x,y): x\in\mathbb{Q}\ \text{or}\ y\in\mathbb{Q}\}$;
	\par\noindent\textbullet\quad $\{(x,y): y=nx \text{ for some } n\in\mathbb{N}\}\ \cup\ \{(x,y): x=0\}$;
	\par\noindent\textbullet\quad $\{(x,f(x)) : x\in\mathbb{R}\}$, where $f:\mathbb{R}\to\mathbb{R}$ is a continuous function.

A set $U\subset\mathbb{R}^2$ is open iff every $p\in U$ admits $\varepsilon>0$ with $B_\varepsilon(p)\subset U$.
A set $F\subset\mathbb{R}^2$ is closed iff it contains all its limit points (equivalently, $\mathbb{R}^2\setminus F$ is open).
If $g$ is continuous, then $g^{-1}(C)$ is closed whenever $C$ is closed, and $g^{-1}(O)$ is open whenever $O$ is open.
Graphs of continuous functions are closed: $\{(x,y): y=f(x)\}=\{(x,y): y-f(x)=0\}$ is the zero set of a continuous map.

	\par\noindent\textbullet\quad Not open (a ball around any point leaves the segment). Closed: image of compact $[0,1]$ under $x\mapsto(x,0)$, hence compact in $\mathbb{R}^2$, thus closed. \emph{Answer:} closed, not open.

	\par\noindent\textbullet\quad Not open (no interior). Not closed: the limit points $(0,0)$ and $(1,0)$ are missing. \emph{Answer:} neither.

	\par\noindent\textbullet\quad Complement is $\{(x,0)\}$, which is closed as $\{(x,y):y=0\}=(\pi_2)^{-1}(\{0\})$ where $\pi_2(x,y)=y$ is continuous. Hence the set is open. It is not closed since points with $y\to 0$ converge to the $x$-axis. \emph{Answer:} open, not closed.

	\par\noindent\textbullet\quad Not open: every open ball contains a point with both coordinates irrational. The complement
	$(\mathbb{R}\setminus\mathbb{Q})\times(\mathbb{R}\setminus\mathbb{Q})$ is not open for the same reason, so the set is not closed. \emph{Answer:} neither.

	\par\noindent\textbullet\quad Each line $\{(x,y):y=nx\}$ and $\{x=0\}$ is closed. Let $(x_k,n_k x_k)\to(x_0,y_0)$ with $n_k\in\mathbb{N}$ or $x_k=0$.
	If $x_0=0$, the limit lies on $\{x=0\}$. If $x_0\neq 0$, then $n_k=\frac{n_k x_k}{x_k}\to \frac{y_0}{x_0}$, forcing $\frac{y_0}{x_0}\in\mathbb{N}$; hence $(x_0,y_0)$ lies on one of the listed lines. Thus the union is closed. It is not open (lines have empty interior). \emph{Answer:} closed, not open.

	\par\noindent\textbullet\quad The graph $\{(x,f(x))\}$ equals $\{(x,y): y-f(x)=0\}$, the zero set of the continuous map $(x,y)\mapsto y-f(x)$. Hence it is closed. It has empty interior in $\mathbb{R}^2$, so it is not open. \emph{Answer:} closed, not open.

Line segments and lines have empty interior; removing a closed line (the $x$-axis) leaves an open set;
in (iv) both the set and its complement are dense with empty interior; graphs of continuous functions are closed.
```

## CP-II-0475

- chapter line: 7837

```tex
\label{prob:cp-ii-0475}
\par\noindent\textbullet\quad The hypothesis Ă˘â‚¬Ĺ›every continuous $f:E\to\mathbb R$ is boundedĂ˘â‚¬â„˘Ă˘â‚¬â„˘ is called
	\emph{pseudocompactness}. In metric spaces (in particular in $\mathbb R^n$),
	pseudocompact $\Longleftrightarrow$ compact; our proof used Heine--Borel.
```

## CP-II-0494

- chapter line: 7879

```tex
\label{prob:cp-ii-0494}
Continuity of Linear Operators between Normed Spaces

Let $X,Y$ be normed spaces and $T:X\to Y$ a linear map. Prove that the following are equivalent:

	\par\noindent\textbullet\quad $T$ is continuous;
	\par\noindent\textbullet\quad $T$ is continuous at $0$;
	\par\noindent\textbullet\quad $T$ is bounded: $\exists M>0$ such that $\|Tx\|_Y\le M\|x\|_X$ for all $x\in X$;
	\par\noindent\textbullet\quad $T$ is uniformly continuous on $X$.

For a linear map $T$, continuity at a single point implies continuity everywhere, since
$T(x+h)-T(x)=T(h)$. A linear operator is called \emph{bounded} if
$\|Tx\|\le M\|x\|$ for some $M$. The smallest such $M$ is
\[
\|T\|=\sup_{\|x\|\le 1}\|Tx\|.
\]
Boundedness is equivalent to continuity, and implies uniform continuity:
\(\|Tx-Ty\|=\|T(x-y)\|\le\|T\|\|x-y\|\).

	\par\noindent (1)$\Rightarrow$(2)\quad Immediate.

	\par\noindent (2)$\Rightarrow$(3)\quad Assume $T$ is continuous at $0$.
	Then $\exists\delta>0$ such that $\|x\|<\delta\Rightarrow\|Tx\|<1$.
	For arbitrary $x\ne0$ let $y=\frac{\delta}{2\|x\|}x$.
	Then $\|y\|<\delta$ and $\|Ty\|<1$, so
	\[
	\|Tx\|=\frac{2\|x\|}{\delta}\|Ty\|<\frac{2}{\delta}\|x\|.
	\]
	Hence $T$ is bounded with $M=2/\delta$.

	\par\noindent (3)$\Rightarrow$(1)\quad If $T$ is bounded, for all $x,h$ we have
	$\|T(x+h)-T(x)\|=\|Th\|\le M\|h\|$, so $T$ is continuous everywhere.

	\par\noindent (3)$\Leftrightarrow$(4)\quad From boundedness, $\|Tx-Ty\|\le M\|x-y\|$, so $T$ is uniformly continuous.
	Uniform continuity implies continuity at $0$, hence boundedness as before.

	\par\noindent\textbullet\quad $T:\mathbb{R}^2\to\mathbb{R}$, $T(x,y)=x+y$ is bounded with $\|T\|\le\sqrt2$, so continuous.
	\par\noindent\textbullet\quad $T:\ell^1\to\ell^\infty$, $T((x_n))=(n x_n)$ is linear but unbounded, hence not continuous.
```

## CP-II-0495

- chapter line: 7920

```tex
\label{prob:cp-ii-0495}
(with integrand chart)

The integrand is $f(u)=e^{-u^2}$.
It is symmetric, maximised at $u=0$ with $f(0)=1$, and decays rapidly to $0$ as $|u|\to\infty$.
This rapid decay ensures convergence of the Gaussian integral.

\begin{center}

\end{center}

This graph shows the bell-shaped curve of $e^{-u^2}$.
It is clear that the function is bounded and rapidly decays to zero outside a neighbourhood of $0$, so the area under the curve converges.
Indeed,
\[
I=\int_{-\infty}^{\infty} e^{-u^2}\,du = \sqrt{\pi}.
\]

To evaluate
\[
I=\int_{-\infty}^{\infty} e^{-u^2}\,du,
\]
we square it:
\[
I^2=\left(\int_{-\infty}^{\infty} e^{-u^2}\,du\right)
\left(\int_{-\infty}^{\infty} e^{-v^2}\,dv\right)
=\iint_{\mathbb{R}^2} e^{-(u^2+v^2)}\,du\,dv.
\]

Since the integrand depends only on $u^2+v^2=r^2$, we switch to polar coordinates:
\[
u=r\cos\theta,\quad v=r\sin\theta, \qquad du\,dv = r\,dr\,d\theta.
\]

Thus
\[
I^2=\int_0^{2\pi}\int_0^\infty e^{-r^2}\,r\,dr\,d\theta
= \left(\int_0^{2\pi} d\theta\right)\left(\int_0^\infty r e^{-r^2}\,dr\right).
\]

Let $t=r^2$, $dt=2r\,dr$:
\[
\int_0^\infty r e^{-r^2}\,dr=\tfrac{1}{2}\int_0^\infty e^{-t}\,dt=\tfrac{1}{2}.
\]

So
\[
I^2=2\pi\cdot \tfrac{1}{2}=\pi,\qquad I=\sqrt{\pi}.
\]

	\begin{theorem}[Heine--Cantor]
		Suppose that $E \subset \mathbb{R}^n$ is compact and $f:E \to \mathbb{R}^m$ is continuous on $E$.
		Then $f$ is uniformly continuous on $E$.
	\end{theorem}

	---
```

## CP-II-0498

- chapter line: 7979

```tex
\label{prob:cp-ii-0498}
\par\noindent\textbullet\quad Smooth $f\in C_c^\infty$ have rapidly decaying Haar coefficients, illustrating completeness.

	\section*{Problem 12$^{\ast}$ — Lebesgue decomposition}

	\textbf{Statement.}
	Let $(E,\mathcal{E})$ be a measurable space and let $\mu,\nu$ be finite measures on $(E,\mathcal{E})$.
	Show that there exist \emph{unique} finite measures $\nu_a,\nu_s$ such that
	\[
	\nu=\nu_a+\nu_s,\qquad \nu_a\ll \mu,\qquad \nu_s\perp \mu.
	\]

	\bigskip

	\textbf{Theory.}
```

## CP-II-0500

- chapter line: 7997

```tex
\label{prob:cp-ii-0500}
$^*$: Absolute convergence characterizes completeness

Let $(V,\|\cdot\|)$ be a normed space. Show that $V$ is complete if and only if
for every sequence $(x_n)$ in $V$ with $\sum_{j=1}^\infty \|x_j\|$ convergent,
the series $\sum_{n=1}^\infty x_n$ is convergent.
\emph{Hint.} If $(x_n)$ is Cauchy, then there is a subsequence $(x_{n_j})$
such that $\sum_j \|x_{n_{j+1}}-x_{n_j}\|<\infty$.

A series $\sum x_n$ converges iff its partial sums $s_N=\sum_{n=1}^N x_n$ converge.
If $\sum \|x_n\|<\infty$, then $(s_N)$ is Cauchy since
$\|s_m-s_n\|\le\sum_{k=n+1}^m \|x_k\|$.
In a complete space, every Cauchy sequence converges.
From a Cauchy sequence one can extract a subsequence with summable differences.

\textbf{($\Rightarrow$)} Suppose $V$ is complete and $\sum_{n=1}^\infty \|x_n\|<\infty$.
Then for $m>n$,
\[
\|s_m-s_n\|=\Big\|\sum_{k=n+1}^m x_k\Big\|
\le \sum_{k=n+1}^m \|x_k\|\xrightarrow[n,m\to\infty]{}0,
\]
so $(s_N)$ is Cauchy and converges in $V$. Hence $\sum x_n$ converges.

\textbf{($\Leftarrow$)} Assume every absolutely convergent series converges in $V$.
Let $(y_n)$ be Cauchy. Choose a subsequence $(y_{n_j})$ with
$\|y_{n_{j+1}}-y_{n_j}\|\le 2^{-j}$.
Then $\sum_{j=1}^\infty \|y_{n_{j+1}}-y_{n_j}\|\le 1$, so by the assumption the series
$\sum_{j=1}^\infty (y_{n_{j+1}}-y_{n_j})$ converges.
Its $m$-th partial sum equals $y_{n_m}-y_{n_1}$; hence $y_{n_j}\to y$ for some $y\in V$.

To prove $y_n\to y$, fix $\varepsilon>0$. Since $(y_n)$ is Cauchy, there exists $N$ such that
$\|y_n-y_m\|<\varepsilon/2$ for all $n,m\ge N$.
Choose $j$ with $n_j\ge N$ and $\|y_{n_j}-y\|<\varepsilon/2$.
Then for all $n\ge N$,
\[
\|y_n-y\|\le \|y_n-y_{n_j}\|+\|y_{n_j}-y\|<\varepsilon/2+\varepsilon/2=\varepsilon.
\]
Hence $y_n\to y$ and $V$ is complete.


Let $c_{00}$ be the space of finitely supported sequences with the $\ell^1$-norm.
Take $x_n=\frac{1}{2^n}e_n$. Then $\sum\|x_n\|_1=1$ but
$\sum x_n=(\frac{1}{2^n})_{n\ge1}\notin c_{00}$.
So absolute convergence does not imply convergence in $c_{00}$, and $c_{00}$ is not complete.

In a normed space, an absolutely convergent series always has Cauchy partial sums, but it
\emph{converges in the space} if and only if the space is complete.

\textbf{Counterexample.}
Let $c_{00}$ be the space of finitely supported sequences with the $\ell^{1}$-norm.
Define
\[
x_n = \frac{1}{2^{n}} e_n, \qquad (n\ge1),
\]
where $e_n$ is the sequence with $1$ in position $n$ and zeros elsewhere.
Then
\[
\sum_{n=1}^\infty \|x_n\|_1 = \sum_{n=1}^\infty \frac{1}{2^n} = 1 < \infty,
\]
so the series $\sum x_n$ is \emph{absolutely convergent}.
Its partial sums are
\[
s_N = \sum_{n=1}^N x_n = \bigg(\frac12, \frac14, \dots, \frac{1}{2^N}, 0, 0, \dots\bigg),
\]
which converge (in $\ell^1$) to
\[
s = \bigg(\frac12, \frac14, \frac18, \dots\bigg).
\]
However, $s\notin c_{00}$ (it is not finitely supported), so $\sum x_n$
does \emph{not} converge in $c_{00}$.

\textbf{Conclusion.}
Absolute convergence does not guarantee convergence in an incomplete space.
In contrast, in any Banach space (complete normed space), every absolutely
convergent series converges in the space.
```

## CP-II-0506

- chapter line: 8075

```tex
\label{prob:cp-ii-0506}
\par\noindent\textbullet\quad \textbf{With the sup norm $\|\cdot\|_{\infty}$.}
	$\|\cdot\|_{\infty}$ is a norm on $R([0,1])$. If $(f_n)$ is $\|\cdot\|_{\infty}$–Cauchy, then
	$f_n\to f$ uniformly for some bounded $f$, and uniform limits of Riemann–integrable functions are
	Riemann–integrable; thus $f\in R([0,1])$. Therefore $R([0,1])$ is closed in the complete space of bounded
	functions and is itself complete in $\|\cdot\|_{\infty}$.
```

## CP-II-0514

- chapter line: 8194

```tex
\label{prob:cp-ii-0514}
Which of the following subsets of $\mathbb{R}^2$ with the Euclidean topology are connected?
	Which are path-connected? (And why?)

		\par\noindent\textbullet\quad $\{(x,y)\in\mathbb{R}^2:\|(x,y)-(-1,0)\|\le1
		\text{ or }\|(x,y)-(1,0)\|<1\}$

		\par\noindent\textbullet\quad $\{(x,y)\in\mathbb{R}^2:\ x=0
		\text{ or }y=qx\text{ for }q\in\mathbb{Q}\}$

		\par\noindent\textbullet\quad $\{(x,y)\in\mathbb{R}^2:\ x=0
		\text{ or }y=qx\text{ for }q\in\mathbb{Q}\}\setminus\{(0,0)\}$

		\par\noindent\textbullet\quad $S\subset\mathbb{R}^2$ any star-shaped domain,
		i.e.\ there exists $x_0\in S$ such that for all $x\in S$
		the line segment $[x_0,x]\subset S$.


	\textbf{Theory.}
	A subset $A\subset\mathbb{R}^2$ is \emph{connected} if it cannot be written
	as the disjoint union of two non-empty open subsets in the subspace topology.
	It is \emph{path-connected} if for every $x,y\in A$ there exists a continuous
	$\gamma:[0,1]\to A$ with $\gamma(0)=x$, $\gamma(1)=y$.
	In $\mathbb{R}^n$, path-connected $\Rightarrow$ connected, but not conversely.


	\textbf{Solutions.}

	\textit{(a) Two tangent disks.}
	Let $D_1=\{(x,y):\|(x,y)-(-1,0)\|\le1\}$,
	$D_2=\{(x,y):\|(x,y)-(1,0)\|<1\}$.
	They intersect at $(0,0)$.
	Each disk is convex and hence path-connected;
	their intersection is non-empty,
	so $D_1\cup D_2$ is both connected and path-connected.

	\medskip

	\textit{(b) Rational-slope lines.}
	$A=\{(x,y):x=0\text{ or }y=qx,\ q\in\mathbb{Q}\}$.
	Each line $y=qx$ and the $y$-axis are path-connected and meet at $(0,0)$.
	Thus their union is path-connected (hence connected).

	\medskip

	\textit{(c) Same family minus the origin.}
	$B=A\setminus\{(0,0)\}$.
	Removing $(0,0)$ disconnects the family:
	each branch $L_q=\{(x,y):y=qx,\ x\neq0\}$ and $L_0=\{(0,y):y\neq0\}$
	is still path-connected, but the branches are disjoint.
	No path can move from one branch to another without passing through $(0,0)$.
	Hence $B$ is disconnected.
	Each component (each branch) remains path-connected.

	\medskip

	\textit{(d) Star-shaped domain.}
	If $S$ is star-shaped with center $x_0$,
	then for each $x\in S$ the path
	$\gamma_x(t)=(1-t)x_0+t\,x$ ($t\in[0,1]$)
	lies in $S$, joining $x_0$ and $x$.
	Thus $S$ is path-connected, hence connected.


	\textbf{Summary table.}

	\begin{center}
		\begin{tabular}{c|l|c|c}
			Case & Description & Connected & Path-connected\\\hline
			(a) & Two tangent disks & Yes & Yes\\
			(b) & Rational-slope lines (fan) & Yes & Yes\\
			(c) & Fan without the origin & No & No (each branch yes)\\
			(d) & Star-shaped domain & Yes & Yes
		\end{tabular}
	\end{center}

	\par\medskip\noindent\textbf{Problem 7 — Intersection of Nested Compact Connected Sets}\par
```

## CP-II-0523

- chapter line: 8320

```tex
\label{prob:cp-ii-0523}
\par\noindent\textbullet\quad if $x,y\le R+1$: done by compact uniform continuity on $[0,R+1]$;
```

## CP-II-0530

- chapter line: 8325

```tex
\label{prob:cp-ii-0530}
— Wiener and Vitali covering lemmas

\textbf{(a) Finite family, factor $3$.}
Given open balls $B_1,\dots,B_N\subset\mathbb{R}^n$, there exist indices $i_1,\dots,i_k$ with
$B_{i_1},\dots,B_{i_k}$ pairwise disjoint such that
\[
\bigcup_{i=1}^{N} B_i \subset \bigcup_{j=1}^{k} 3B_{i_j},
\qquad\text{hence}\qquad
\Bigl|\bigcup_{i=1}^{N} B_i\Bigr| \le 3^n\sum_{j=1}^{k}|B_{i_j}|.
\]

\textit{Proof.}
Select greedily a ball of maximal radius, delete all balls it meets, and iterate.
The selected family is disjoint.
If $B$ was deleted because it meets a selected ball $B^\ast$ with radius $\ge$ radius$(B)$,
then $B\subset 3B^\ast$.
Therefore $\bigcup_i B_i \subset \bigcup_j 3B_{i_j}$ and $|3B|=3^n|B|$ yields the measure bound.

\medskip
\textbf{(b) Vitali, factor $5$.}
Let $\{B_j:j\in J\}$ be any family of balls with $\operatorname{rad}(B_j)\le R$.
There exists a countable disjoint subfamily $\{B_j:j\in J'\}$ with
\[
\bigcup_{i\in J} B_i \subset \bigcup_{j\in J'} 5B_j .
\]

\textit{Proof.}
Order by decreasing radius and run the same greedy algorithm; radii $\le R$ imply
a maximal disjoint subfamily is countable (each contains a distinct rational point).
If $x\in B$ for some original $B$ that is not chosen, then when $B$ was removed it met
a chosen ball $B^\ast$ with radius $\ge$ radius$(B)$, whence $B\subset 5B^\ast$ by a geometric estimate.
Thus the stated inclusion holds.

\clearpage
\subsection*{Examples of functions in $L^r(\mathbb{R}^n)\cap L^\infty(\mathbb{R}^n)$}

Here are several illustrative examples of measurable functions on $\mathbb{R}^n$
that belong to both $L^r$ and $L^\infty$ for some fixed $1\le r<\infty$.
Each example includes a short justification and (where possible) explicit norms.

\bigskip

If $\mathrm{supp}\,f\subset E$ with $|E|<\infty$ and $\|f\|_\infty=M<\infty$, then
\[
\|f\|_{L^r} \le M\,|E|^{1/r}
\qquad\Longrightarrow\qquad
f\in L^r\cap L^\infty.
\]
\textbf{Concrete example.} The indicator of a unit ball:
\[
f(x)=\mathbf{1}_{B(0,1)}(x)
\quad\Rightarrow\quad
\|f\|_\infty=1,\quad
\|f\|_{L^r}=|B(0,1)|^{1/r}=(\omega_n)^{1/r}.
\]
\textbf{Another example.} A ``hat'' (Lipschitz) bump:
\[
f(x)=\max\{0,1-|x|\},
\qquad
\mathrm{supp}\,f\subset B(0,1),\quad
\|f\|_\infty=1,\ f\in L^r.
\]

\bigskip

\[
f(x)=(1+|x|)^{-\alpha},\qquad \alpha>\frac{n}{r}.
\]
Then $0<f\le1\Rightarrow f\in L^\infty$, and
in spherical coordinates
\[
\int_{\mathbb{R}^n}(1+|x|)^{-\alpha r}dx
<\infty \quad\Longleftrightarrow\quad
\alpha r>n.
\]
Hence $f\in L^r$ whenever $\alpha>n/r$.
\textbf{Easy pick:} $\alpha=\tfrac{n}{r}+1$ works for any $r,n$.

\bigskip

\[
f(x)=\frac{\sin|x|}{(1+|x|)^{\alpha}},\qquad \alpha>\frac{n}{r}.
\]
Then $|f(x)|\le (1+|x|)^{-\alpha}$, so the same integrability condition applies.
Boundedness is clear from $|\sin|x||\le1$.

\bigskip

\[
f(x)=\min(1,|x|^{-\beta}),\qquad \beta>\frac{n}{r}.
\]
Then $f\le1\Rightarrow f\in L^\infty$.
Away from the origin, $\int_{|x|\ge1}|x|^{-\beta r}dx<\infty$ when $\beta r>n$, so $f\in L^r$.
Near $0$, $f=1$ is bounded, hence no singularity occurs.

\bigskip

Let $(Q_k)_{k\ge1}$ be disjoint cubes with finite measure, and define
\[
f(x)=\sum_{k=1}^\infty a_k\,\mathbf{1}_{Q_k}(x),
\qquad |a_k|\le1,\quad
\sum_{k=1}^\infty |a_k|^r|Q_k|<\infty.
\]
Then $\|f\|_\infty\le1$ and $\|f\|_{L^r}^r=\sum_k |a_k|^r|Q_k|<\infty$,
so $f\in L^r\cap L^\infty$.

\bigskip

 \par\noindent\textbullet\quad sep4pt
	\par\noindent\textbullet\quad $f\equiv1$: in $L^\infty$ but not in $L^r$ on $\mathbb{R}^n$ (non-integrable tail).
	\par\noindent\textbullet\quad $f(x)=|x|^{-\beta}\mathbf{1}_{\{|x|\le1\}}$, $0<\beta<\tfrac{n}{r}$:
	in $L^r$ but not in $L^\infty$ (unbounded at $0$).

\par\medskip\noindent\textbf{Examples in $L^r(\mathbb{R}^n)\cap L^\infty(\mathbb{R}^n)$.}\quad

	\par\noindent\textbullet\quad $\mathbf 1_{B(0,1)}$: $\|\,\cdot\,\|_\infty=1$, $\|\,\cdot\,\|_{L^r}=\omega_n^{1/r}$.
	\par\noindent\textbullet\quad $(1+|x|)^{-\alpha}$ with $\alpha>n/r$ (bounded and $\alpha r>n$ ensures $L^r$).
	\par\noindent\textbullet\quad $\dfrac{\sin|x|}{(1+|x|)^\alpha}$ with $\alpha>n/r$.
	\par\noindent\textbullet\quad $\min\!\bigl(1,\,|x|^{-\beta}\bigr)$ with $\beta>n/r$.
	\par\noindent\textbullet\quad $\displaystyle f=\sum_{k\ge1} a_k\,\mathbf 1_{Q_k}$, $|a_k|\le1$, disjoint $Q_k$, and
	$\sum |a_k|^r|Q_k|<\infty$.
```

## CP-II-0532

- chapter line: 8450

```tex
\label{prob:cp-ii-0532}
{Polynomial characterization of holomorphicity on Runge domains}{poly-char}
	Let $U\subset\mathbb C$ be bounded, open, and suppose $\mathbb C\setminus U$ is connected.
	Show that $f:U\to\mathbb C$ is holomorphic iff for every compact $K\Subset U$ and every
	$\varepsilon>0$ there exists a polynomial $P$ with
	\[
	\sup_{z\in K}|f(z)-P(z)|<\varepsilon.
	\]
```

## CP-II-0533

- chapter line: 8461

```tex
\label{prob:cp-ii-0533}
Let $(X,d)$ be a metric space. In the definition of the topology of $(X,d)$, why donĂ˘â‚¬â„˘t we require arbitrary (possibly infinite) intersections of open sets to be open? Give a counterexample with $X=\mathbb{R}$.

In a metric space $(X,d)$, a set $U\subset X$ is open if for every $x\in U$ there exists $r>0$ such that the open ball $B(x,r)=\{y\in X:\ d(x,y)<r\}\subset U$. It follows immediately that:

\par\noindent\textbullet\quad arbitrary unions of open sets are open;
\par\noindent\textbullet\quad finite intersections of open sets are open (take the minimum of finitely many witness radii).

However, these arguments do not extend to infinite families of open sets.
```

## CP-II-0539

- chapter line: 8473

```tex
\label{prob:cp-ii-0539}
\par\noindent\textbullet\quad \textbf{Mixed measure:}
		Let $\mu=m$ (Lebesgue) on $\mathbb R$, and set
		$\displaystyle \nu = f\,m \;+\; \sum_{k=1}^\infty a_k\,\delta_{x_k}$
		with $f\in L^1(m)$ and $a_k\ge0$.
		Then the Lebesgue decomposition of $\nu$ w.r.t.\ $\mu$ is
		$\nu_a=f\,m$ and $\nu_s=\sum_{k\ge1} a_k\,\delta_{x_k}$.

	\bigskip

	The Lebesgue decomposition and Radon--Nikodym theorems both extend to $\sigma$-finite measures.
	For signed or complex measures, combine the Jordan (Hahn) decomposition with the Lebesgue decomposition.
	In harmonic analysis, decomposing a Borel measure on a locally compact group into its absolutely continuous
	part w.r.t.\ Haar measure and its singular part is fundamental (e.g.\ spectral decompositions).

	We write \(m\) for Lebesgue measure on \(\mathbb{R}^n\).
	The notation \(\int_A f\,dm\) means integration with respect to \(m\)
	(i.e.\ \(\int_A f(x)\,dx\) in classical notation), explicitly indicating the underlying measure.

	\bigskip

	Let \(f\in L^1(m)\) and define \(\nu(A):=\int_A f\,dm\) for Borel \(A\).
	If \(m(A)=0\), then \(\int_A |f|\,dm=0\), hence
	\[
	|\nu(A)|=\left|\int_A f\,dm\right|\le \int_A |f|\,dm=0,
	\]
	so \(\nu(A)=0\). Therefore \(\nu\ll m\).
	This remains true for signed or complex \(f\in L^1(m)\) by using \(\int_A |f|\,dm\).

	\bigskip

	A measure \(\mu\) on \((E,\mathcal E)\) is \(\sigma\)-finite if
	\(E=\bigcup_{k=1}^\infty E_k\) with \(\mu(E_k)<\infty\) for all \(k\).
	Lebesgue measure \(m\) on \(\mathbb{R}^n\) is \(\sigma\)-finite since
	\(\mathbb{R}^n=\bigcup_{k=1}^\infty [-k,k]^n\) and each cube has finite measure.
	The Radon--Nikodym and Lebesgue decomposition theorems hold under \(\sigma\)-finiteness.

	\bigskip

	For \(x\in E\), the Dirac measure \(\delta_x\) is defined by \(\delta_x(A)=\mathbf{1}_A(x)\).
	On \(\mathbb{R}^n\) with Lebesgue measure \(m\), we have \(\delta_x\perp m\),
	since \(\delta_x\) is supported on the \(m\)-null set \(\{x\}\).
	In general, any atomic part \(\sum_k a_k \delta_{x_k}\) of a measure is singular w.r.t.\ \(m\).

	\bigskip

	Let \(C\subset[0,1]\) be the middle-third Cantor set.
	The Cantor measure \(\gamma\) is the unique Borel probability measure satisfying
	\[
	\gamma(A)=\tfrac12\,\gamma(3A)+\tfrac12\,\gamma(3A-2),
	\]
	equivalently, the measure whose distribution function is the Devil's staircase.
	It is \emph{singular continuous}: it has no atoms (\(\gamma(\{x\})=0\) for all \(x\))
	and is supported on \(C\) with \(m(C)=0\). Hence \(\gamma\perp m\).

	\bigskip

	On \(\mathbb{R}^n\) with background measure \(m\), any finite measure \(\nu\) decomposes uniquely as
	\[
	\nu=\nu_a+\nu_s,\qquad \nu_a\ll m,\quad \nu_s\perp m.
	\]
	Typical instances:
```

## CP-II-0540

- chapter line: 8538

```tex
\label{prob:cp-ii-0540}
\par\noindent (b)\quad For each $i\in\{1,\dots,n\}$ and $h\neq 0$ the difference
		quotient operator
		\[
		(\Delta_i^h\phi)(x)
		:= \frac{\phi(x+he_i)-\phi(x)}{h}
		\]
		is a continuous linear map on $\mathcal{E}(\mathbb{R}^n)$, and
		for every $\phi\in\mathcal{E}(\mathbb{R}^n)$ one has
		\[
		\Delta_i^h\phi \longrightarrow D_i\phi
		\quad\text{in }\mathcal{E}(\mathbb{R}^n)
		\quad\text{as } h\to 0.
		\]



\begin{proof}
	Fix a compact $K\subset\mathbb{R}^n$ and $m\in\mathbb{N}$.

	\emph{(a) Translations.}
	For $|\alpha|\le m$ we have
	\[
	D^\alpha(\tau_x\phi)(y)=D^\alpha\phi(y-x).
	\]
	If $x_l\to 0$, choose a compact set $K'$ containing $K$ and $K-x_l$ for
	all $l$ large.  Then $D^\alpha\phi$ is uniformly continuous on $K'$, so
	given $\varepsilon>0$ there exists $\delta>0$ such that
	$|z-z'|<\delta\Rightarrow |D^\alpha\phi(z)-D^\alpha\phi(z')|<\varepsilon$
	for all $z,z'\in K'$.  For $l$ large enough we have $|x_l|<\delta$ and
	therefore
	\[
	\sup_{y\in K} |D^\alpha\phi(y-x_l)-D^\alpha\phi(y)|
	\le \varepsilon.
	\]
	Taking the supremum over $|\alpha|\le m$ yields
	$p_{K,m}(\tau_{x_l}\phi-\phi)\to 0$, i.e.\ $\tau_{x_l}\phi\to\phi$ in
	$\mathcal{E}(\mathbb{R}^n)$.

	\medskip\noindent
	\emph{(b) Difference quotients.}
	Let $g(x) := D^\alpha\phi(x)$ for some $|\alpha|\le m$.  Then
	\[
	D^\alpha(\Delta_i^h\phi)(x)
	= \frac{g(x+he_i)-g(x)}{h}.
	\]
	By the mean value theorem,
	\[
	\frac{g(x+he_i)-g(x)}{h} = D_i g(x+\theta h e_i)
	\]
	for some $\theta=\theta(x,h)\in(0,1)$.  Choosing a compact $K'$ containing
	$K$ and $K+he_i$ for all $|h|$ small, we see that $D_i g$ is uniformly
	continuous on $K'$.  Hence for every $\varepsilon>0$ there exists
	$\delta>0$ such that for $|h|<\delta$,
	\[
	\sup_{x\in K}
	\bigl|D^\alpha(\Delta_i^h\phi)(x)-D_iD^\alpha\phi(x)\bigr|
	= \sup_{x\in K}
	|D_i g(x+\theta h e_i)-D_i g(x)|
	< \varepsilon.
	\]
	Taking the supremum over $|\alpha|\le m$ shows that
	$p_{K,m}(\Delta_i^h\phi - D_i\phi)\to 0$ as $h\to 0$, which is precisely
	$\Delta_i^h\phi\to D_i\phi$ in $\mathcal{E}(\mathbb{R}^n)$.
\end{proof}
```

## CP-II-0544

- chapter line: 8606

```tex
\label{prob:cp-ii-0544}
\par\noindent\textbullet\quad \textbf{Bounded:} $|f(x)|\le 1/(x+1)\le1$.
	\textbf{Uniformly continuous:} yes. Given $\varepsilon>0$, choose $R$ with $2/(R+1)<\varepsilon/2$.
	If $x,y\ge R$ then $|f(x)-f(y)|\le 2/(R+1)<\varepsilon/2$.
	On $[0,R+1]$, $f$ is continuous on a compact set, hence uniformly continuous;
	choose $\delta\le1$ to combine the cases.

\bigskip
```

## CP-II-0545

- chapter line: 8617

```tex
\label{prob:cp-ii-0545}
\par\noindent\textbullet\quad \emph{Cauchy sequence}: $(y_n)$ is Cauchy if for every $\varepsilon>0$ there exists $N$ such that
	$d(y_m,y_n)<\varepsilon$ for all $m,n\ge N$.
```

## CP-II-0547

- chapter line: 8623

```tex
\label{prob:cp-ii-0547}
\par\noindent\textbullet\quad \emph{Complete}: every Cauchy sequence converges in $X$.
```

## CP-II-0548

- chapter line: 8628

```tex
\label{prob:cp-ii-0548}
Let $(X,d)$ be a metric space.

Show that the union of any collection of open subsets of $X$ must be open (regardless of whether
the collection is finite, countable or uncountable), and that the intersection of any finite
collection of open subsets is again open. Formulate and prove similar properties about the
closed subsets of $X$.

Let $E$ be a subset of $X$. Show that there is a unique largest open subset $E^\circ$ of $X$
contained in $E$, i.e.\ a unique open subset $E^\circ$ of $X$ such that $E^\circ\subset E$ and if
$G$ is any open subset of $X$ with $G\subset E$ then $G\subset E^\circ$. The set $E^\circ$ is
called the \emph{interior} of $E$ in $X$. Show also that there is a unique smallest closed subset
$\overline{E}$ of $X$ containing $E$, i.e.\ a unique closed subset $\overline{E}$ of $X$ with
$E\subset \overline{E}$ and if $F$ is any closed subset of $X$ with $E\subset F$ then
$\overline{E}\subset F$. The set $\overline{E}$ is called the \emph{closure} of $E$ in $X$.

Show that
\begin{center}
\resizebox{\linewidth}{!}{$\displaystyle
E^\circ=\{\,x\in X:\ B_\varepsilon(x)\subset E\ \text{for some }\varepsilon>0\,\}
\qquad\text{and}\qquad
\overline{E}=\{\,x\in X:\ x_n\to x\ \text{for some sequence }(x_n)\subset E\,\}.
$}
\end{center}

\bigskip
\noindent\textbf{Theory (tools and facts).}

	\par\noindent\textbullet\quad \textbf{Open/closed set algebra.}

		\par\noindent\textbullet\quad Arbitrary unions of open sets are open; finite intersections of open sets are open.
		\par\noindent\textbullet\quad Arbitrary intersections of closed sets are closed; finite unions of closed sets are closed.
		\par\noindent\textbullet\quad Complement duality: $U$ open $\Leftrightarrow$ $X\setminus U$ closed.

	\par\noindent\textbullet\quad \textbf{Open balls.} For $x\in X$ and $\varepsilon>0$,
	\[
	B_\varepsilon(x)=\{y\in X:\ d(x,y)<\varepsilon\}
	\]
	is open; every open set is a union of open balls.

	\par\noindent\textbullet\quad \textbf{Interior.}
	\[
	E^\circ=\bigcup\{\,G\subset X:\ G\ \text{open and } G\subset E\,\}
	\]
	is open, satisfies $E^\circ\subset E$, and is the largest open subset of $E$.
	Metric characterisation:
	\[
	x\in E^\circ\ \Longleftrightarrow\ \exists\,\varepsilon>0:\ B_\varepsilon(x)\subset E.
	\]

	\par\noindent\textbullet\quad \textbf{Closure.}
	\[
	\overline{E}=\bigcap\{\,F\subset X:\ F\ \text{closed and } E\subset F\,\}
	\]
	is closed, contains $E$, and is the smallest closed set containing $E$.
	Equivalent characterisations:
	\[
	x\in\overline{E}\ \Longleftrightarrow\ \forall\,\varepsilon>0,\ B_\varepsilon(x)\cap E\neq\varnothing
	\ \Longleftrightarrow\ \exists\ (x_n)\subset E\ \text{with } x_n\to x.
	\]

	\par\noindent\textbullet\quad \textbf{Limit points.} $x$ is a limit (accumulation) point of $E$ iff every ball
	$B_\varepsilon(x)$ intersects $E\setminus\{x\}$; then $x\in\overline{E}$.

	\par\noindent\textbullet\quad \emph{Arbitrary union of open sets is open.}
	If $x\in\bigcup_{i\in I}U_i$ with each $U_i$ open, then $x\in U_j$ for some $j$,
	so $\exists\,\varepsilon>0$ with $B_\varepsilon(x)\subset U_j\subset\bigcup_{i\in I}U_i$.
	\par\noindent\textbullet\quad \emph{Finite intersection of open sets is open.}
	If $x\in\bigcap_{k=1}^m U_k$, pick $\varepsilon_k>0$ with $B_{\varepsilon_k}(x)\subset U_k$.
	Then $B_{\min_k \varepsilon_k}(x)\subset\bigcap_{k=1}^m U_k$.
	\par\noindent\textbullet\quad \emph{Closed sets (duals).}
	Arbitrary intersections of closed sets are closed, and finite unions of closed sets are closed
	(by complements of the two statements above).

\noindent\hrulefill

Define
\[
E^\circ=\bigcup\{G\subset X:\ G\ \text{open and}\ G\subset E\},\qquad
\overline E=\bigcap\{F\subset X:\ F\ \text{closed and}\ E\subset F\}.
\]
Then $E^\circ$ is open, $E^\circ\subset E$, and if $G$ is open with $G\subset E$ then $G\subset E^\circ$;
hence $E^\circ$ is the unique largest open subset of $X$ contained in $E$.
Also $\overline E$ is closed, $E\subset\overline E$, and if $F$ is closed with $E\subset F$,
then $\overline E\subset F$; hence $\overline E$ is the unique smallest closed subset of $X$
containing $E$.

\noindent\hrulefill

\begin{align*}
	E^\circ&=\{x\in X:\ \exists\,\varepsilon>0\ \text{with}\ B_\varepsilon(x)\subset E\},\\
	\overline E&=\{x\in X:\ \exists\ (x_n)\subset E\ \text{with}\ x_n\to x\}.
\end{align*}
\emph{Proof of the first:} If $x\in E^\circ$, then $x$ lies in some open $G\subset E$, so
$B_\varepsilon(x)\subset G\subset E$ for some $\varepsilon>0$.
Conversely, if $B_\varepsilon(x)\subset E$, then $x$ lies in the open set $B_\varepsilon(x)\subset E$,
hence $x\in E^\circ$.

\emph{Proof of the second:} If $x\in\overline E$, then every ball $B_{1/n}(x)$ meets $E$; pick
$x_n\in E\cap B_{1/n}(x)$ to get $x_n\to x$. Conversely, if $x_n\in E$ and $x_n\to x$, then every
neighbourhood of $x$ contains some $x_n\in E$, so every ball around $x$ meets $E$, hence
$x\in\overline E$.
```

## CP-II-0549

- chapter line: 8733

```tex
\label{prob:cp-ii-0549}
— Characterization on a Runge domain

Let $U\subset\mathbb C$ be bounded and assume $\mathbb C\setminus U$ is connected.
Show that $f:U\to\mathbb C$ is holomorphic iff for every compact $K\subset U$ and $\varepsilon>0$
there exists a polynomial $P$ with $\sup_{K}|f-P|<\varepsilon$.

If $\mathbb C\setminus U$ is connected, $U$ is a Runge domain; by the
Runge–Oka–Weil theorem, holomorphic functions on $U$ can be uniformly approximated on compacts
by polynomials. Uniform limits of holomorphic functions on open sets are holomorphic.

($\Rightarrow$) For $f\in\mathcal O(U)$ and $K\Subset U$, Runge–Oka–Weil yields a polynomial $P$
with $\sup_{K}|f-P|<\varepsilon$.
($\Leftarrow$) If for each $K\Subset U$ there are polynomials $P_n$ with $P_n\to f$ uniformly on $K$,
then by Weierstrass $f$ is holomorphic on $K^\circ$, hence on $U$.

\noindent\rule{\textwidth}{0.4pt}

\bigskip
```

## CP-II-0551

- chapter line: 8755

```tex
\label{prob:cp-ii-0551}
— Riesz' Lemma and non-compactness of the unit ball

Let $X$ be a normed space, $V\subset X$ a proper closed subspace, and $0<\alpha<1$.
	There exists $x\in X$ with $\|x\|=1$ such that $\|x-y\|\ge \alpha$ for all $y\in V$.

	\emph{Proof.}
	Pick $x_{0}\notin V$ and set $d:=\operatorname{dist}(x_{0},V)>0$.
	Choose $v\in V$ with $\|x_{0}-v\|<d/\alpha$, and define $x:=(x_{0}-v)/\|x_{0}-v\|$.
	For any $y\in V$,
	\[
	\|x-y\|
	=\frac{\|x_{0}-(v+\|x_{0}-v\|\,y)\|}{\|x_{0}-v\|}
	\ge \frac{d}{\|x_{0}-v\|}>\alpha,
	\]
	since $v+\|x_{0}-v\|\,y\in V$. Hence $\|x-y\|\ge\alpha$ for all $y\in V$.


	Let $X$ be an infinite-dimensional Banach space.

	Inductively construct $(x_{k})$ in the unit sphere by applying Riesz' lemma with $\alpha=\tfrac12$
	to the nested closed subspaces $V_{k}=\overline{\operatorname{span}}\{x_{1},\dots,x_{k}\}$.

	Then $\|x_{i}-x_{j}\|\ge\tfrac12$ for $i\ne j$, so the unit ball contains a sequence with no
	Cauchy (hence no convergent) subsequence. Therefore the unit ball of $X$ is not compact.

	Every bounded sequence in a finite dimensional normed space has a convergent subsequence.
	Equivalently, the closed unit ball is compact.

	If $X$ is infinite dimensional, the closed unit ball of $X$ is not compact (indeed, not sequentially compact).
	There exists a bounded sequence with no Cauchy subsequence.

		\par\noindent\textbullet\quad In $\ell^2$, let $e_n$ be the standard basis. Then $\|e_n\|=1$ and
		$\|e_n-e_m\|=\sqrt{2}$ for $n\neq m$; hence no Cauchy subsequence exists.
		\par\noindent\textbullet\quad In $L^p$ $(1\le p<\infty)$, choose pairwise disjoint measurable sets $E_n$ with $0<m(E_n)<\infty$, and set
		$x_n:=\mathbf 1_{E_n}/\|\mathbf 1_{E_n}\|_p$. Then $\|x_n\|_p=1$ and
		$\|x_n-x_m\|_p=(\|x_n\|_p^p+\|x_m\|_p^p)^{1/p}=2^{1/p}$ for $n\ne m$.

	\bigskip

	Let $X$ be a normed space, $V\subset X$ a proper closed subspace, and $0<\alpha<1$.
	There exists $x\in X$ with $\|x\|=1$ and $\operatorname{dist}(x,V)\ge \alpha$.

	With $V_k=\overline{\operatorname{span}}\{x_1,\dots,x_k\}$ and $\alpha=\tfrac12$,
	one can construct a sequence $(x_k)$ in the unit sphere such that
	$\|x_i-x_j\|\ge \tfrac12$ for $i\ne j$, proving the unit ball of an infinite dimensional Banach space is not compact.

		\par\noindent\textbullet\quad \textbf{In $\ell^2$:} take $V_k=\operatorname{span}\{e_1,\dots,e_k\}$ and $x_{k+1}=e_{k+1}$;
		then $\operatorname{dist}(x_{k+1},V_k)=1$.
		\par\noindent\textbullet\quad \textbf{In $L^p$:} pick disjoint sets $(E_k)$ with $0<m(E_k)<\infty$, set
		\[
		x_k=\frac{\mathbf 1_{E_k}}{\|\mathbf 1_{E_k}\|_p},\qquad V_k=\operatorname{span}\{x_1,\dots,x_k\}.
		\]
		For any $y\in V_k$, $y=0$ a.e.\ on $E_{k+1}$, so
		\[
		\|x_{k+1}-y\|_p^p \ge \int_{E_{k+1}} |x_{k+1}|^p = 1,
		\]
		hence $\operatorname{dist}(x_{k+1},V_k)=1$ and $\|x_i-x_j\|_p=2^{1/p}$ for $i\ne j$.

	\bigskip

	To produce the nested closed subspaces used with Riesz' lemma in the $L^p$ setting, fix disjoint measurable sets
	$E_k$ with $0<m(E_k)<\infty$ and define
	\[
	x_k:=\frac{\mathbf 1_{E_k}}{\|\mathbf 1_{E_k}\|_p},\qquad
	V_k:=\overline{\operatorname{span}}\{x_1,\dots,x_k\}.
	\]
	Then $x_{k+1}$ has distance $1$ from $V_k$, giving a concrete Riesz sequence and proving the unit ball is not compact.

	Let $(\Omega,\mathcal{F},\mu)$ be a $\sigma$-finite measure space and $1\le p\le\infty$.
	We construct nested finite-dimensional subspaces $V_k$ and a sequence $(x_k)$ in the unit sphere
	with $\operatorname{dist}(x_{k+1},V_k)=1$ for all $k$, yielding a concrete ``Riesz sequence''
	and the non-compactness of the unit ball.

	\bigskip

	Because $\mu$ is $\sigma$-finite, we can choose pairwise disjoint measurable sets
	$(E_k)_{k\ge1}$ with $0<\mu(E_k)<\infty$.

		\par\noindent\textbullet\quad On $(\mathbb{R}^n,\mathcal{B},m)$, one convenient choice is the dyadic cubes
		\[
		E_k = \bigl((k-1,k]\times(0,1]^{n-1}\bigr) \quad (k\ge1),
		\]
		or on $[0,1]$ the dyadic subintervals
		$E_k = \bigl((2^{-k},2^{-(k-1)}]\bigr)$.
		\par\noindent\textbullet\quad On a non-atomic probability space, recursively bisect any set of positive measure to obtain
		an infinite disjoint family of positive-measure sets.

	\bigskip

	For $1\le p<\infty$ define
	\[
	x_k := \frac{\mathbf{1}_{E_k}}{\|\mathbf{1}_{E_k}\|_{L^p}}
	= \frac{\mathbf{1}_{E_k}}{\mu(E_k)^{1/p}},
	\qquad \|x_k\|_{L^p}=1.
	\]
	For $p=\infty$, simply set $x_k:=\mathbf{1}_{E_k}$ so that $\|x_k\|_\infty=1$.

	\bigskip

	Let
	\[
	V_k := \operatorname{span}\{x_1,\dots,x_k\}.
	\]
	(Each $V_k$ is finite dimensional, hence closed, so the closure bar is superfluous:
	$\overline{\operatorname{span}}\{x_1,\dots,x_k\}=V_k$.)

	\bigskip

	Fix $k\ge1$ and $y\in V_k$, say $y=\sum_{j=1}^k a_j x_j$.
	Because the supports are disjoint, $y=0$ a.e.\ on $E_{k+1}$.
	Therefore
	\[
	\|x_{k+1}-y\|_{L^p}^p
	= \int_{E_{k+1}} |x_{k+1}|^p\,d\mu \;+\; \int_{\Omega\setminus E_{k+1}} |y|^p\,d\mu
	\ge \int_{E_{k+1}} |x_{k+1}|^p\,d\mu
	= 1.
	\]
	Taking $y=0$ shows the infimum is attained, hence
	\[
	\operatorname{dist}(x_{k+1},V_k)=\inf_{y\in V_k}\|x_{k+1}-y\|_{L^p}=1.
	\]
	Consequently, for $i\neq j$,
	\[
	\|x_i-x_j\|_{L^p}^p
	= \|x_i\|_{L^p}^p + \|x_j\|_{L^p}^p
	= 2 \quad\Longrightarrow\quad \|x_i-x_j\|_{L^p}=2^{1/p}.
	\]

	\bigskip

	For $y\in V_k$, again $y=0$ on $E_{k+1}$, so
	\[
	\|x_{k+1}-y\|_\infty
	= \operatorname*{ess\,sup}_{\omega\in\Omega} |x_{k+1}(\omega)-y(\omega)|
	\ge \operatorname*{ess\,sup}_{\omega\in E_{k+1}} |x_{k+1}(\omega)|
	= 1.
	\]
	With $y=0$ we get $\operatorname{dist}(x_{k+1},V_k)=1$, and for $i\neq j$,
	$\|x_i-x_j\|_\infty=1$ (since the values are $1$ on $E_i$, $0$ there for $x_j$, and vice versa).

	\bigskip

		\par\noindent\textbullet\quad \textbf{Riesz sequence.} The unit sphere of $L^p$ contains a sequence $(x_k)$ with
		$\|x_i-x_j\|\ge c_p$ for $i\ne j$, where $c_p=2^{1/p}$ for $1\le p<\infty$ and $c_\infty=1$.
		Thus the closed unit ball is not (sequentially) compact.
		\par\noindent\textbullet\quad \textbf{Explicit Riesz lemma step.} With $V_k$ as above and any $0<\alpha<1$,
		the vector $x_{k+1}$ satisfies $\|x_{k+1}\|=1$ and $\operatorname{dist}(x_{k+1},V_k)=1\ge\alpha$,
		giving the Riesz–lemma vector at step $k$ without any abstract selection.

	\bigskip

	Let $F_k$ be sets with $\mu(F_k)>0$ and $\mu(F_i\cap F_j)=0$ for $i\neq j$ \emph{except} possibly on
	small overlaps of measure at most $\varepsilon_k>0$. Define
	$x_k=\mathbf{1}_{F_k}/\mu(F_k)^{1/p}$ ($1\le p<\infty$).
	Then for $y\in V_k$,
	\[
	\|x_{k+1}-y\|_{L^p}^p
	\ge 1 - C_p\,\varepsilon_{k+1}
	\quad\text{with a constant }C_p \text{ depending only on }p.
	\]
	Choosing $\varepsilon_{k}\downarrow0$ fast, one still gets a sequence bounded away from $V_k$,
	showing non-compactness. This is sometimes convenient when one constructs localized bumps $\varphi_k$
	with small overlaps instead of strict indicators.

	\bigskip

	\noindent
	In Exercise~3 we considered a bounded linear functional
	$u:L^{p}(\Omega)\to\mathbb{R}$ and constructed from it the auxiliary map
	$\tilde u$ on nonnegative functions together with the linear functional
	\[
	w(f)=\tilde u(f^{+})-\tilde u(f^{-})
	\qquad (f\in L^{p}).
	\]
	The sequence $(x_k)$ and subspaces $(V_k)$ above give a concrete geometric
	framework in which one can \emph{visualize} the decomposition $u=w-(w-u)$
	into its positive and negative parts.

	\medskip

	\noindent
	Because the functions $x_k$ have pairwise disjoint supports, any
	$f\in V_k$ can be written uniquely as a finite linear combination
	\[
	f = a_1 x_1 + a_2 x_2 + \dots + a_k x_k,
	\qquad  a_j\in\mathbb{R}.
	\]
	On such simple functions, a bounded linear functional $u$
	is completely determined by its values on the basis $\{x_1,\dots,x_k\}$:
	\[
	u(f) = \sum_{j=1}^{k} a_j\,u(x_j).
	\]
	If we denote $c_j:=u(x_j)$, then the action of $u$ on $V_k$
	is given by the coordinate functional
	$f\mapsto\sum_{j=1}^{k} c_j a_j$.
	In this coordinate form, the \emph{positive} and \emph{negative} parts
	of $u$ simply correspond to the positive and negative coefficients $c_j$.

	\medskip

	\noindent
	Indeed, on $V_k$ we may define
	\[
	u_{+}(f)
	= \sum_{j=1}^{k} a_j\,c_j^{+},
	\qquad
	u_{-}(f)
	= \sum_{j=1}^{k} a_j\,c_j^{-},
	\qquad
	c_j^{\pm} := \max\{\pm c_j,0\}.
	\]
	Then $u(f)=u_{+}(f)-u_{-}(f)$, and both $u_{+}$ and $u_{-}$ are
	positive linear functionals on $V_k$.
	By density of $\operatorname{span}\{x_j\}$ in the $L^{p}$ space,
	this algebraic decomposition extends uniquely (by continuity) to
	all of $L^{p}(\Omega)$, yielding the decomposition $u=w-(w-u)$
	described abstractly in Exercise~3.

	\bigskip

	\noindent
	\textbf{Interpretation.}\;
	The sequence $(x_k)$ serves as a concrete ``basis'' of nonnegative,
	almost orthogonal directions that separates the positive and negative
	components of $u$:

		\par\noindent\textbullet\quad if $u(x_k)\ge 0$, the contribution of $x_k$ lies in $u_{+}$,
		\par\noindent\textbullet\quad if $u(x_k)<0$, the contribution lies in $u_{-}$.

	The functional $w$ constructed from $\tilde u$ captures precisely
	the accumulation of the positive coefficients $u(x_k)$, while $w-u$
	captures the negative ones.
	This explicit coordinate model clarifies the abstract Jordan decomposition
	of a functional on $L^{p}$ and shows that it mirrors the decomposition
	of a signed measure into its positive and negative parts.

	\bigskip

	\noindent
	\textbf{Summary.}\;
	The disjoint-support family $(x_k)$ realizes geometrically what the
	functional decomposition $u=u_{+}-u_{-}$ expresses analytically:
	each component acts as a ``measure'' supported on a disjoint sector
	of the space, so that the positivity or negativity of $u$
	can be analyzed one region at a time.
	This viewpoint unites the measure-theoretic intuition
	with the functional-analytic structure built in Exercise~3.

	We work on the measure space $([0,1],\mathcal B,m)$ with Lebesgue measure $m$.
	For $k\ge 1$ set
	\[
	E_k := (2^{-k},2^{-(k-1)}].
	\]
	Then the $E_k$ are pairwise disjoint and $m(E_k)=2^{-k}$.

	\bigskip

	Define
	\[
	x_k := \frac{\mathbf 1_{E_k}}{\sqrt{m(E_k)}}
	= 2^{k/2}\,\mathbf 1_{E_k} \in L^2[0,1].
	\]
	\textbf{Norm.}\quad
	\[
	\|x_k\|_2^2 = \int 4^{k/2}\,\mathbf 1_{E_k}
	= 2^{k} m(E_k) = 1
	\quad \Rightarrow \quad \|x_k\|_2 = 1.
	\]

	\textbf{Orthogonality.}\quad
	Since $x_i x_j=0$ a.e.\ for $i\ne j$ (disjoint supports),
	\[
	\langle x_i,x_j\rangle=\int x_i x_j = 0.
	\]
	Thus $\{x_k\}$ is an orthonormal set.

	\bigskip

	For $i\ne j$,
	\[
	\|x_i-x_j\|_2^2
	= \|x_i\|_2^2+\|x_j\|_2^2 - 2\langle x_i,x_j\rangle
	= 1+1-0=2,
	\]
	so
	\[
	\|x_i-x_j\|_2=\sqrt{2}.
	\]

	\bigskip

	Define
	\[
	u(f):=\int_0^1 f(t)\,dt.
	\]
	\textbf{Boundedness and norm.}\quad
	By Cauchy--Schwarz,
	\[
	|u(f)| = \Bigl|\int f\Bigr|
	\le \|f\|_2\,\|1\|_2
	= \|f\|_2,
	\]
	so $\|u\|=1$.

	\textbf{Values on the blocks.}\quad
	\[
	u(x_k)
	= \int x_k
	= \int 2^{k/2}\,\mathbf 1_{E_k}
	= 2^{k/2}\,m(E_k)
	= 2^{k/2}\cdot 2^{-k}
	= 2^{-k/2} > 0.
	\]
	Hence all coefficients $c_k:=u(x_k)$ are positive.

	\bigskip

	Let
	\[
	V_k := \operatorname{span}\{x_1,\dots,x_k\}.
	\]
	Any $y\in V_k$ vanishes a.e.\ on $E_{k+1}$, hence
	\[
	\|x_{k+1}-y\|_2^2
	\ge \int_{E_{k+1}}|x_{k+1}|^2
	= \int_{E_{k+1}}2^{k+1}\mathbf 1_{E_{k+1}}
	= 2^{k+1}m(E_{k+1}) = 1.
	\]
	Taking $y=0$ shows
	\[
	\operatorname{dist}(x_{k+1},V_k)=1.
	\]

	\bigskip

	For $f\ge0$, the functional $u(g)=\int g$ is monotone increasing in $g$.
	If $0\le g\le f$, the supremum of $\int g$ occurs for $g=f$, so
	\[
	\tilde u(f)
	= \sup_{0\le g\le f} \int g
	= \int f = u(f).
	\]
	Therefore
	\[
	w(f) = \tilde u(f^+) - \tilde u(f^-)
	= \int f^+ - \int f^- = \int f = u(f),
	\]
	and $w=u$, $w-u\equiv0$ (both positive).

	\bigskip

	Let $\phi=\sum_{k=1}^\infty s_k\,\mathbf 1_{E_k}$ with $s_k\in\{-1,+1\}$.
	Then $\|\phi\|_2^2=\sum_k m(E_k)=1$ and define
	\[
	u_\phi(f):=\int_0^1 f(t)\,\phi(t)\,dt.
	\]
	By Cauchy--Schwarz, $\|u_\phi\|=\|\phi\|_2=1$.
	For each block,
	\[
	u_\phi(x_k)
	= \int x_k\phi
	= \int 2^{k/2}\,\mathbf 1_{E_k}\,s_k
	= s_k\,2^{k/2}m(E_k)
	= s_k\,2^{-k/2}.
	\]
	Now some $u_\phi(x_k)$ are positive and some negative.

	For $f\ge0$,
	\[
	\tilde u_\phi(f)
	= \sup_{0\le g\le f}\int g\,\phi
	= \int f\,\phi_{+},
	\qquad \phi_{+}=\max(\phi,0).
	\]
	Hence
	\[
	w_\phi(f)
	= \tilde u_\phi(f^+) - \tilde u_\phi(f^-)
	= \int f\,\phi_{+},
	\qquad
	(w_\phi - u_\phi)(f)
	= \int f\,\phi_{-} \ge 0,
	\]
	where $\phi_-=\max(-\phi,0)$.
	Therefore $w_\phi$ and $w_\phi-u_\phi$ are positive and
	\[
	u_\phi = w_\phi - (w_\phi - u_\phi)
	\]
	is exactly the positive-minus-negative decomposition of $u_\phi$.

	\bigskip

	On the finite-dimensional space $V_k$ we can write
	\[
	u_\phi\!\left(\sum_{j=1}^{k} a_j x_j\right)
	= \sum_{j=1}^{k} a_j\,s_j\,2^{-j/2},
	\]
	so that
	\[
	(u_\phi)_+\!\left(\sum a_j x_j\right)
	= \sum a_j\,(s_j 2^{-j/2})^{+},
	\qquad
	(u_\phi)_-\!\left(\sum a_j x_j\right)
	= \sum a_j\,(s_j 2^{-j/2})^{-}.
	\]
	This makes the abstract decomposition $u=u_+-u_-$ completely explicit
	on the orthonormal basis $\{x_k\}$.

	\bigskip

		\par\noindent\textbullet\quad $\{x_k\}$ is an orthonormal family in $L^2[0,1]$,
		with $\|x_i-x_j\|_2=\sqrt{2}$ and
		$\operatorname{dist}(x_{k+1},V_k)=1$.
		\par\noindent\textbullet\quad For the positive functional $u(f)=\int f$, we have $w=u$ and $w-u=0$.
		\par\noindent\textbullet\quad For sign-changing densities $\phi$, we get
		$u_\phi=w_\phi-(w_\phi-u_\phi)$ with both parts positive.
		\par\noindent\textbullet\quad On $V_k$, $u_\phi$ acts as a coordinate functional with
		coefficients $s_k 2^{-k/2}$ separating positive and negative parts.

	\clearpage
```

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

## CP-II-0477

- chapter line: 11262

```tex
\label{prob:cp-ii-0477}
— Periodic Green’s function on the circle

Suppose that $f \in C^0(\mathbb{R})$ is a continuous function with period $2\pi$,
i.e.\ $f(\theta) = f(\theta + 2\pi)$. For $\theta \in [0,2\pi)$ define
\[
\psi(\theta)
:= \int_{0}^{\theta} f(\alpha)
\frac{\cosh(\pi - \theta + \alpha)}{2\sinh \pi}\,d\alpha
+ \int_{\theta}^{2\pi} f(\alpha)
\frac{\cosh(-\pi - \theta + \alpha)}{2\sinh \pi}\,d\alpha,
\]
and extend $\psi$ to a function on $\mathbb{R}$ by periodicity:
\[
\psi(\theta + 2\pi) = \psi(\theta), \qquad \theta\in\mathbb{R}.
\]

	\par\noindent\textbullet\quad Show that $\psi \in C^0(\mathbb{R})$.

	\par\noindent\textbullet\quad By differentiating the defining formula directly, show that
	\[
	\psi'(\theta)
	= - \int_{0}^{\theta} f(\alpha)
	\frac{\sinh(\pi - \theta + \alpha)}{2\sinh \pi}\,d\alpha
	- \int_{\theta}^{2\pi} f(\alpha)
	\frac{\sinh(-\pi - \theta + \alpha)}{2\sinh \pi}\,d\alpha,
	\]
	and deduce that $\psi \in C^1(\mathbb{R})$.

	\par\noindent\textbullet\quad Differentiating once more, show that
	\[
	\psi''(\theta) = - f(\theta) + \psi(\theta), \qquad \theta\in\mathbb{R},
	\]
	and conclude that $\psi \in C^2(\mathbb{R})$ is a $2\pi$-periodic solution
	of the inhomogeneous ODE
	\[
	\psi''(\theta) + f(\theta) = \psi(\theta), \qquad \theta\in\mathbb{R}.
	\]

Suppose that $f\in C^0(\mathbb{R})$ is a continuous function with period $2\pi$,
i.e.\ $f(\theta)=f(\theta+2\pi)$. For $\theta\in[0,2\pi]$ define
\[
\psi(\theta)
:= \int_0^\theta f(\alpha)\,
\frac{\cosh(\pi-\theta+\alpha)}{2\sinh\pi}\,d\alpha
+ \int_\theta^{2\pi} f(\alpha)\,
\frac{\cosh(-\pi-\theta+\alpha)}{2\sinh\pi}\,d\alpha,
\]
and extend $\psi$ to a function on $\mathbb{R}$ by periodicity:
$\psi(\theta)=\psi(\theta+2\pi)$.

For $(\theta,\alpha)\in[0,2\pi]\times[0,2\pi]$ set
\[
K_1(\theta,\alpha)
=\frac{\cosh(\pi-\theta+\alpha)}{2\sinh\pi},
\qquad
K_2(\theta,\alpha)
=\frac{\cosh(-\pi-\theta+\alpha)}{2\sinh\pi}.
\]
These kernels are continuous (indeed real-analytic) in both variables, and
$f$ is continuous. Thus the integrands
\[
(\theta,\alpha)\mapsto f(\alpha)K_1(\theta,\alpha),\qquad
(\theta,\alpha)\mapsto f(\alpha)K_2(\theta,\alpha)
\]
are continuous on the compact set $[0,2\pi]\times[0,2\pi]$. It follows from
the standard theorem on parameter-dependent integrals that
\[
\theta\mapsto \int_0^\theta f(\alpha)K_1(\theta,\alpha)\,d\alpha,
\qquad
\theta\mapsto \int_\theta^{2\pi} f(\alpha)K_2(\theta,\alpha)\,d\alpha
\]
are continuous on $(0,2\pi)$; hence $\psi$ is continuous on $(0,2\pi)$.

At the endpoints one checks that the one-sided limits agree with the
periodic extension. Using $2\pi$-periodicity of $f$ and the evenness of
$\cosh$, we obtain
\[
\lim_{\theta\to 0^+}\psi(\theta)
=\int_0^{2\pi} f(\alpha)\frac{\cosh(-\pi-\alpha)}{2\sinh\pi}\,d\alpha
=\int_0^{2\pi} f(\alpha)\frac{\cosh(-\pi+\alpha)}{2\sinh\pi}\,d\alpha
=\psi(2\pi).
\]
Together with the periodic extension $\psi(\theta+2\pi)=\psi(\theta)$ this
shows that $\psi\in C^0(\mathbb{R})$.

Write
\[
\psi(\theta)=I_1(\theta)+I_2(\theta),
\]
where
\[
I_1(\theta)=\int_0^\theta f(\alpha)K_1(\theta,\alpha)\,d\alpha,
\qquad
I_2(\theta)=\int_\theta^{2\pi} f(\alpha)K_2(\theta,\alpha)\,d\alpha.
\]
Since $K_1,K_2$ are smooth and $f$ is continuous, we may differentiate
under the integral sign using Leibniz' rule. For $I_1$ we obtain
\[
I_1'(\theta)
= f(\theta)K_1(\theta,\theta)
+ \int_0^\theta f(\alpha)\,\partial_\theta K_1(\theta,\alpha)\,d\alpha.
\]
A direct computation yields
\[
K_1(\theta,\theta)=\frac{\cosh\pi}{2\sinh\pi},\qquad
\partial_\theta K_1(\theta,\alpha)
= -\frac{\sinh(\pi-\theta+\alpha)}{2\sinh\pi},
\]
so that
\[
I_1'(\theta)
= f(\theta)\frac{\cosh\pi}{2\sinh\pi}
-\int_0^\theta f(\alpha)\,
\frac{\sinh(\pi-\theta+\alpha)}{2\sinh\pi}\,d\alpha.
\]

Similarly,
\[
I_2'(\theta)
= -f(\theta)K_2(\theta,\theta)
+ \int_\theta^{2\pi}f(\alpha)\,\partial_\theta K_2(\theta,\alpha)\,d\alpha,
\]
with
\[
K_2(\theta,\theta)=\frac{\cosh(-\pi)}{2\sinh\pi}
=\frac{\cosh\pi}{2\sinh\pi},
\qquad
\partial_\theta K_2(\theta,\alpha)
= -\frac{\sinh(-\pi-\theta+\alpha)}{2\sinh\pi}.
\]
Thus
\[
I_2'(\theta)
= -f(\theta)\frac{\cosh\pi}{2\sinh\pi}
-\int_\theta^{2\pi} f(\alpha)\,
\frac{\sinh(-\pi-\theta+\alpha)}{2\sinh\pi}\,d\alpha.
\]

Adding $I_1'(\theta)$ and $I_2'(\theta)$, the boundary terms cancel and we
obtain
\[
\psi'(\theta)
= -\int_0^\theta f(\alpha)\,
\frac{\sinh(\pi-\theta+\alpha)}{2\sinh\pi}\,d\alpha
-\int_\theta^{2\pi} f(\alpha)\,
\frac{\sinh(-\pi-\theta+\alpha)}{2\sinh\pi}\,d\alpha.
\]
The integrands are continuous in $(\theta,\alpha)$, so the same argument as
in part (a) shows that $\psi'$ is continuous on $\mathbb{R}$. Hence
$\psi\in C^1(\mathbb{R})$.

Set
\[
\widetilde K_1(\theta,\alpha)
= -\frac{\sinh(\pi-\theta+\alpha)}{2\sinh\pi},\qquad
\widetilde K_2(\theta,\alpha)
= -\frac{\sinh(-\pi-\theta+\alpha)}{2\sinh\pi},
\]
so that the formula above can be written as
\[
\psi'(\theta)
= \int_0^\theta f(\alpha)\,\widetilde K_1(\theta,\alpha)\,d\alpha
+\int_\theta^{2\pi} f(\alpha)\,\widetilde K_2(\theta,\alpha)\,d\alpha.
\]
Differentiating again and using Leibniz' rule once more, we obtain
\[
\psi''(\theta)
= f(\theta)\widetilde K_1(\theta,\theta)
-f(\theta)\widetilde K_2(\theta,\theta)
+\int_0^\theta f(\alpha)\,\partial_\theta\widetilde K_1(\theta,\alpha)\,d\alpha
+\int_\theta^{2\pi} f(\alpha)\,\partial_\theta\widetilde K_2(\theta,\alpha)\,d\alpha.
\]
A direct computation shows that
\[
\widetilde K_1(\theta,\theta)=-\frac{1}{2},\qquad
\widetilde K_2(\theta,\theta)=+\frac{1}{2},
\]
and
\[
\partial_\theta\widetilde K_1(\theta,\alpha)
= \frac{\cosh(\pi-\theta+\alpha)}{2\sinh\pi},\qquad
\partial_\theta\widetilde K_2(\theta,\alpha)
= \frac{\cosh(-\pi-\theta+\alpha)}{2\sinh\pi}.
\]
Hence
\[
f(\theta)\widetilde K_1(\theta,\theta)
- f(\theta)\widetilde K_2(\theta,\theta)
= -\frac12 f(\theta)-\frac12 f(\theta)
= -f(\theta),
\]
while
\[
\int_0^\theta f(\alpha)\,\partial_\theta\widetilde K_1(\theta,\alpha)\,d\alpha
+\int_\theta^{2\pi} f(\alpha)\,\partial_\theta\widetilde K_2(\theta,\alpha)\,d\alpha
= \psi(\theta).
\]
Therefore
\[
\psi''(\theta) = -f(\theta)+\psi(\theta)
\qquad (\theta\in(0,2\pi)),
\]
and by periodicity this holds for all $\theta\in\mathbb{R}$. The
right-hand side is continuous, so $\psi''\in C^0(\mathbb{R})$ and
$\psi\in C^2(\mathbb{R})$.
```

## CP-II-0499

- chapter line: 11471

```tex
\label{prob:cp-ii-0499}
Assume $f:\mathbb{R}\to\mathbb{R}$ differentiable with $|f'(x)|\le M$ for all $x$.

\renewcommand\labelenumi{(\alph{enumi})}
\par\noindent\textbullet\quad $|f(x)-f(y)|\le M|x-y|$ by MVT.
\par\noindent\textbullet\quad Hence $f$ is uniformly continuous (Lipschitz with constant $M$).
```

## CP-II-0559

- chapter line: 11544

```tex
\label{prob:cp-ii-0559}
derivative of Dirac $\delta_0'$.

The action of the derivative of the Dirac mass is
\[
\langle\delta_0',\varphi\rangle = -\varphi'(0).
\]
The next figure displays $\varphi$ and $\varphi'$ and highlights
$\varphi'(0)$.

\par\medskip\noindent\textbf{Example F: principal value $\mathrm{P.V.}(1/x)$.}\quad
The distribution $\mathrm{P.V.}(1/x)$ is defined by
\[
\left\langle \mathrm{P.V.}(1/x), \varphi \right\rangle
= \lim_{\varepsilon\to0^+}
\int_{|x|>\varepsilon} \frac{\varphi(x)}{x}\,dx.
\]
The graph below shows $\varphi(x)$ and the truncated integrand
$\varphi(x)/x$ for $|x|>\varepsilon$.
```

## CP-II-0565

- chapter line: 11566

```tex
\label{prob:cp-ii-0565}
s

\par\noindent\textbullet\quad Show that the map $f \mapsto f'$ is a continuous map from $C^{k+1}([a,b])$ to $C^k([a,b])$.

Let
\[
d_{C^k}(f,g)=\sum_{j=0}^k \sup_{x\in[a,b]} \bigl| f^{(j)}(x)-g^{(j)}(x)\bigr|
\quad\text{on } C^k([a,b]).
\]

Let $(f_n)$ be Cauchy in $d_{C^k}$. Then for each $j=0,\dots,k$ the sequence
$(f_n^{(j)})$ is Cauchy in $(C([a,b]),\|\cdot\|_\infty)$, hence converges uniformly to some
$g_j\in C([a,b])$.

Define inductively $g_{j-1}(x)=g_{j-1}(a)+\int_a^x g_j(t)\,dt$ for $j=k,k-1,\dots,1$.
By the uniform convergence of derivatives and the fundamental theorem of calculus,
$g_{j-1}$ is differentiable with $(g_{j-1})'=g_j$. Setting $f:=g_0$, we have
$f\in C^k([a,b])$ and $f^{(j)}=g_j$ for all $0\le j\le k$. Since
$f_n^{(j)}\to f^{(j)}$ uniformly for each $j$, it follows that
$d_{C^k}(f_n,f)\to 0$. Thus $C^k([a,b])$ is complete.

\par\medskip\noindent\textbf{(b) The map $T:C^k([a,b])\to C^{k+1}([a,b])$, $T(f)(x)=\int_a^x f(y)\,dy$, is continuous.}\quad
For $f,g\in C^k$ let $F=T(f)$ and $G=T(g)$. Then $F\in C^{k+1}$ with
$F^{(1)}=f$ and $F^{(j+1)}=f^{(j)}$ for $1\le j\le k$. Moreover,
\[
\|F-G\|_\infty \le (b-a)\,\|f-g\|_\infty,\qquad
\|F^{(j)}-G^{(j)}\|_\infty = \|f^{(j-1)}-g^{(j-1)}\|_\infty\ (1\le j\le k+1).
\]
Hence
\[
d_{C^{k+1}}(T(f),T(g))
\le \max\{b-a,1\}\,\Big(\|f-g\|_\infty+\sum_{j=1}^k \|f^{(j)}-g^{(j)}\|_\infty\Big)
= \max\{b-a,1\}\, d_{C^k}(f,g),
\]
so $T$ is Lipschitz and therefore continuous.

\par\medskip\noindent\textbf{(c) The derivative map $D:C^{k+1}([a,b])\to C^k([a,b])$, $D(f)=f'$, is continuous.}\quad
For $f,g\in C^{k+1}$,
\[
d_{C^k}(f',g')=\sum_{j=0}^k \|f^{(j+1)}-g^{(j+1)}\|_\infty
\le \sum_{j=0}^{k+1} \|f^{(j)}-g^{(j)}\|_\infty
= d_{C^{k+1}}(f,g).
\]
Thus $D$ is $1$-Lipschitz (hence continuous).

\section*{Examples and counterexamples for $C^k([a,b])$ with $d_{C^k}$}
```

## CP-II-0003

- chapter line: 11664

```tex
\label{prob:cp-ii-0003}
\par\noindent\textbullet\quad Both $f$ and $g$ are continuous, piecewise linear.
```

## CP-II-0004

- chapter line: 11669

```tex
\label{prob:cp-ii-0004}
\par\noindent\textbullet\quad In this exercise we prove a \emph{two--variable} version:
	\[
	\left\|
	\int_{\mathbb{R}^n} F(\cdot,y)\,dy
	\right\|_{L^p(\mathbb{R}^n)}
	\;\le\;
	\int_{\mathbb{R}^n}
	\|F(\cdot,y)\|_{L^p(\mathbb{R}^n)}\,dy.
	\]
```

## CP-II-0009

- chapter line: 11715

```tex
\label{prob:cp-ii-0009}
\par\noindent\textbullet\quad If $\tau$ is indiscrete and $\rho$ is discrete, then $\rho\nsubseteq\tau$; thus $\mathrm{id}:(X,\tau)\to(X,\rho)$ is \emph{not} continuous.
```

## CP-II-0011

- chapter line: 11720

```tex
\label{prob:cp-ii-0011}
\par\noindent\textbullet\quad Suppose $f,g\in C_c^2(\mathbb{R})$. Deduce that
	\[
	u(x,t) = \frac{f(r+t)}{r} + \frac{g(r-t)}{r}
	\]
	is a solution of the wave equation on $S_{*,T}$ which vanishes for
	large $|x|$.
```

## CP-II-0015

- chapter line: 11730

```tex
\label{prob:cp-ii-0015}
— Moving points and uniform convergence

Let $(f_n)$ be a sequence of real-valued continuous functions on a closed, bounded interval $[a,b]$,
and suppose that $f_n$ converges pointwise to a continuous function $f$.

For any sequence $x_n\in[a,b]$ with $x_n\to x$,
\[
|f_n(x_n)-f(x)|
\le |f_n(x_n)-f(x_n)|+|f(x_n)-f(x)|
\le \sup_{y\in[a,b]}|f_n(y)-f(y)|+|f(x_n)-f(x)|.
\]
The first term tends to $0$ by uniform convergence, the second by continuity of $f$ at $x$.
Hence $f_n(x_n)\to f(x)$.

Assume $f_n\nrightarrow f$ uniformly. Then there exists $\varepsilon>0$ such that for every $N$
one can find $n\ge N$ and $x\in[a,b]$ with
\[
|f_n(x)-f(x)|\ge \varepsilon.
\]
Inductively choose $n_k\uparrow\infty$ and $x_k\in[a,b]$ so that $|f_{n_k}(x_k)-f(x_k)|\ge \varepsilon$ for all $k$.
By compactness of $[a,b]$ there is a subsequence (relabeled) with $x_k\to x\in[a,b]$.
Since $f$ is continuous, $f(x_k)\to f(x)$, and therefore
\[
\liminf_{k\to\infty} |f_{n_k}(x_k)-f(x)|
\ge \liminf_{k}\Big(|f_{n_k}(x_k)-f(x_k)|-|f(x_k)-f(x)|\Big)
\ge \varepsilon.
\]
Thus $f_{n_k}(x_k)\not\to f(x)$. Defining $x_n$ by $x_{n_k}=x_k$ (and arbitrarily elsewhere) yields a sequence $x_n\to x$
with $f_n(x_n)\not\to f(x)$.
```

## CP-II-0024

- chapter line: 11847

```tex
\label{prob:cp-ii-0024}
\par\noindent\textbullet\quad If $\mu=m$ and $\nu=\gamma$ is the Cantor (middle–third) probability measure, then
		$\nu_a=0$ and $\nu_s=\gamma$ (purely singular).
```

## CP-II-0025

- chapter line: 11853

```tex
\label{prob:cp-ii-0025}
Let $A=[a_1,b_1]\times[a_2,b_2]\subset\mathbb{R}^2$ be a rectangle, and let $\mathcal{P}$ be a partition of $A$.
Suppose $f,g:A\to\mathbb{R}$ are bounded and $\lambda\geq 0$.

For a bounded function $f:A\to\mathbb{R}$ and a partition $\mathcal{P}$ of $A$ into rectangles $R$, the \emph{upper sum} is
\[
U(f,\mathcal{P})=\sum_{R\in \mathcal{P}} \big(\sup_{R} f\big)\,|R|,
\]
and the \emph{lower sum} is
\[
L(f,\mathcal{P})=\sum_{R\in \mathcal{P}} \big(\inf_{R} f\big)\,|R|,
\]
where $|R|$ denotes the area of the rectangle $R$.

These constructions satisfy simple algebraic rules:
- taking negatives exchanges suprema and infima,
- scaling by a positive constant factors out,
- suprema are subadditive, infima are superadditive.

	\par\noindent\textbullet\quad $U(-f,\mathcal{P})=-L(f,\mathcal{P})$, since $\sup_R(-f)=-\inf_R f$.
	\par\noindent\textbullet\quad $L(-f,\mathcal{P})=-U(f,\mathcal{P})$, since $\inf_R(-f)=-\sup_R f$.
	\par\noindent\textbullet\quad $U(\lambda f,\mathcal{P})=\lambda U(f,\mathcal{P})$, since $\sup_R(\lambda f)=\lambda\sup_R f$.
	\par\noindent\textbullet\quad $L(\lambda f,\mathcal{P})=\lambda L(f,\mathcal{P})$, since $\inf_R(\lambda f)=\lambda\inf_R f$.
	\par\noindent\textbullet\quad $U(f+g,\mathcal{P})\leq U(f,\mathcal{P})+U(g,\mathcal{P})$, since $\sup_R(f+g)\leq \sup_R f+\sup_R g$.
	\par\noindent\textbullet\quad $L(f+g,\mathcal{P})\geq L(f,\mathcal{P})+L(g,\mathcal{P})$, since $\inf_R(f+g)\geq \inf_R f+\inf_R g$.

Hence the algebraic properties of upper and lower sums hold as claimed.
```

## CP-II-0026

- chapter line: 11883

```tex
\label{prob:cp-ii-0026}
— Minimal-matching distance on unordered $q$-tuples

Let $q\ge 2$ and $n\ge 1$ be integers. Denote by $\mathcal{Q}$ the set of all unordered
$q$-tuples of points in $\mathbb{R}^n$ (repetitions allowed):
\[
\mathcal{Q}=\bigl\{\{x_1,x_2,\dots,x_q\}: x_j\in\mathbb{R}^n\bigr\}.
\]
Define $\mathcal{G}:\mathcal{Q}\times\mathcal{Q}\to\mathbb{R}$ by
\[
\mathcal{G}\!\left(\{x_1,\dots,x_q\},\{y_1,\dots,y_q\}\right)
=\inf_{\sigma\in S_q}\left(\sum_{j=1}^{q}\|\,y_j-x_{\sigma(j)}\,\|^{2}\right)^{1/2}.
\]

\smallskip

\noindent\textbf{(i)} Show that $\mathcal{G}$ is a metric on $\mathcal{Q}$.

\smallskip

\noindent\textbf{(ii)} Assume $n=1$. In this case, for any point
$x=\{x_1,\dots,x_q\}\in\mathcal{Q}$, relabel so that $x_1\le \cdots \le x_q$, and do likewise for
$y=\{y_1,\dots,y_q\}$. Is it true that
\[
\mathcal{G}\!\left(\{x_1,\dots,x_q\},\{y_1,\dots,y_q\}\right)
=\left(\sum_{j=1}^{q}(x_j-y_j)^2\right)^{1/2}\,?
\]

Fix $q\ge2$ and $n\ge1$. Let $\mathcal Q$ be the set of unordered $q$-tuples (multisets) of points in $\mathbb{R}^n$.
For $x=\{x_1,\dots,x_q\}$ and $y=\{y_1,\dots,y_q\}$ define
\[
\mathcal G(x,y)=\inf_{\sigma\in S_q}\Bigl(\sum_{j=1}^q \|y_j-x_{\sigma(j)}\|^2\Bigr)^{1/2}.
\]

\smallskip

\noindent\emph{Nonnegativity and symmetry} are immediate.

\smallskip

\noindent\emph{Identity of indiscernibles.}
If $\mathcal G(x,y)=0$, there exist permutations $\sigma_k$ with
$\sum_j\|y_j-x_{\sigma_k(j)}\|^2\to 0$, hence (passing to a subsequence of permutations if needed)
$y_j=x_{\sigma(j)}$ for all $j$, i.e.\ the multisets coincide.
Conversely, equal multisets give zero cost.

\smallskip

\noindent\emph{Triangle inequality.}
Let $\alpha,\beta\in S_q$. For each $i$,
$\|x_i-z_{\beta(i)}\|\le \|x_i-y_{\alpha(i)}\|+\|y_{\alpha(i)}-z_{\beta(i)}\|$.
Applying MinkowskiĂ˘â‚¬â„˘s inequality in $\mathbb{R}^{nq}$,
\[
\Bigl(\sum_{i=1}^q \|x_i-z_{\beta(i)}\|^2\Bigr)^{1/2}
\le
\Bigl(\sum_{i=1}^q \|x_i-y_{\alpha(i)}\|^2\Bigr)^{1/2}
+
\Bigl(\sum_{i=1}^q \|y_{\alpha(i)}-z_{\beta(i)}\|^2\Bigr)^{1/2}.
\]
Taking the infimum over $\alpha$ on the right and over $\beta$ on the left yields
$\mathcal G(x,z)\le \mathcal G(x,y)+\mathcal G(y,z)$.
Thus $\mathcal G$ is a metric.

\bigskip

Assume $n=1$ and label so that $x_1\le\cdots\le x_q$ and $y_1\le\cdots\le y_q$.
By the rearrangement inequality,
\[
\sum_{j=1}^{q}(x_j-y_j)^2 \ \le\ \sum_{j=1}^{q}(x_j-y_{\sigma(j)})^2
\qquad\text{for all }\sigma\in S_q.
\]
Hence the infimum in the definition of $\mathcal{G}$ is attained at $\sigma=\mathrm{id}$, and
\[
\mathcal{G}\bigl(\{x_1,\dots,x_q\},\{y_1,\dots,y_q\}\bigr)
=\Bigl(\sum_{j=1}^{q}(x_j-y_j)^2\Bigr)^{1/2}.
\]
```

## CP-II-0027

- chapter line: 11962

```tex
\label{prob:cp-ii-0027}
\par\noindent\textbullet\quad The inequality
	\[
	ab \le \frac{a^p}{p} + \frac{b^q}{q}
	\]
	is equivalent to the statement
	\[
	\log(ab)
	\;\le\;
	\log\!\left(\frac{a^p}{p} + \frac{b^q}{q}\right).
	\]
	Because $\log$ is concave, this inequality follows from Jensen's
	inequality applied to $\log$.
```

## CP-II-0031

- chapter line: 11978

```tex
\label{prob:cp-ii-0031}
— A pointwise–vanishing polynomial sequence outside $0$

Does there exist polynomials $p_n$ with $p_n(0)=1$ and $p_n(z)\to0$ for all $z\ne0$?

Enumerate a dense set $\{w_j\}_{j\ge1}\subset\mathbb Q(i)\setminus\{0\}$ and choose integers
$N_j\uparrow\infty$. Define partial products
\[
p_n(z)=\prod_{j=1}^{n}\big(1-\tfrac{z}{w_j}\big)^{N_j}.
\]
Then $p_n(0)=1$. For fixed $z\ne0$ there are infinitely many $j$ with
$|1-z/w_j|\le\frac12$; hence $|p_n(z)|\le\prod_{j\le n,\ |1-z/w_j|\le1/2}2^{-N_j}\to0$.
Therefore $p_n(z)\to0$ for each $z\ne0$.

Choosing $N_j=j$ suffices; taking $N_j=2^j$ accelerates decay.

\noindent\rule{\textwidth}{0.4pt}

\bigskip
```

## CP-II-0033

- chapter line: 12000

```tex
\label{prob:cp-ii-0033}
\renewcommand\labelenumi{(\alph{enumi})}
\par\noindent\textbullet\quad If $x_i\to x$ and $\|x_i\|<r$ for all $i$, then $\|x\|\le r$.\\
\textit{Proof.} Contradict $\|x\|>r$ using $\varepsilon=(\|x\|-r)/2$ and the reverse triangle inequality.
\par\noindent\textbullet\quad The closure of $B_r(y)=\{x:\|x-y\|<r\}$ is $\overline{B_r(y)}=\{x:\|x-y\|\le r\}$.\\
\textit{Proof.} Use (a) for the first inclusion; for boundary points take $x_i=y+(1-\tfrac1i)(x-y)$.
```

## CP-II-0034

- chapter line: 12009

```tex
\label{prob:cp-ii-0034}
\par\noindent\textbullet\quad Show that
	\[
	\|u(t,\cdot)\|_{H^2(\mathbb{R}^n)} = \|u_0\|_{H^2(\mathbb{R}^n)}.
	\]
```

## CP-II-0036

- chapter line: 12017

```tex
\label{prob:cp-ii-0036}
Let $S_n(x)=\sum_{k=0}^{n}x^k$.

		\par\noindent\textbullet\quad On $[0,b]$ with $0<b<1$: $\left\|\dfrac{1}{1-x}-S_n\right\|_{[0,b]}
		=\sup_{[0,b]}\frac{x^{n+1}}{1-x}\le \frac{b^{n+1}}{1-b}\to0$ (uniform).
		\par\noindent\textbullet\quad On $[0,1)$: not uniform, since $\sup_{x\in[0,1)}\dfrac{x^{n+1}}{1-x}=+\infty$.
```

## CP-II-0037

- chapter line: 12026

```tex
\label{prob:cp-ii-0037}
— Which $(f_n)$ converge uniformly on $X$?

	\par\noindent\textbullet\quad $f_n(x)=x^n$ on $X=(0,1)$.
	\par\noindent\textbullet\quad $f_n(x)=x^n$ on $X=(0,\tfrac12)$.
	\par\noindent\textbullet\quad $f_n(x)=x e^{-n x}$ on $X=[0,\infty)$.
	\par\noindent\textbullet\quad $f_n(x)=e^{-x^2}\sin(x/n)$ on $X=\mathbb{R}$.

Uniform convergence on $X$ means $\sup_{x\in X}|f_n(x)-f(x)|\to0$. If $|f_n(x)|\le M_n$ for all $x\in X$ with $M_n\to0$, then $f_n\to0$ uniformly. We shall also use $|\sin t|\le|t|$ and the calculus fact $\sup_{x\ge0} x e^{-a x}=1/(a e)$, attained at $x=1/a$.

For each $x\in(0,1)$ we have $x^n\to0$, but
\[
\sup_{x\in(0,1)} |x^n|=\sup_{x\in(0,1)} x^n=1,
\]
so the supremum does not tend to $0$. Therefore the convergence is not uniform on $(0,1)$.

For $x\in(0,\tfrac12)$,
\[
0\le x^n\le \Big(\tfrac12\Big)^n,
\]
hence
\[
\sup_{x\in(0,1/2)}|x^n|\le \Big(\tfrac12\Big)^n\to0.
\]
Thus $x^n\to0$ uniformly on $(0,\tfrac12)$.

For fixed $n$, the maximum of $x\mapsto x e^{-n x}$ on $[0,\infty)$ occurs at $x=1/n$, with value $1/(n e)$. Consequently
\[
\sup_{x\in[0,\infty)} |x e^{-n x}|=\frac{1}{n e}\to0,
\]
so $f_n\to0$ uniformly on $[0,\infty)$.

Using $|\sin t|\le |t|$,
\[
|f_n(x)|\le e^{-x^2}\frac{|x|}{n}.
\]
The function $g(x)=|x|e^{-x^2}$ is bounded on $\mathbb{R}$ with $\sup g=1/\sqrt{2e}$ (attained at $|x|=1/\sqrt2$). Hence
\[
\sup_{x\in\mathbb{R}} |f_n(x)|
\le \frac{1}{n}\sup_{x\in\mathbb{R}} |x|e^{-x^2}
= \frac{1}{n\sqrt{2e}}\to0,
\]
and $f_n\to0$ uniformly on $\mathbb{R}$.

(a) not uniform; (b) uniform; (c) uniform; (d) uniform.
```

## CP-II-0039

- chapter line: 12074

```tex
\label{prob:cp-ii-0039}
\par\noindent\textbullet\quad \textbf{Singular (atomic):}
		On $\mathbb R$, the Dirac measure $\delta_0$ is singular w.r.t.\ Lebesgue measure $m$,
		since it is supported on $\{0\}$ with $m(\{0\})=0$.
```

## CP-II-0040

- chapter line: 12081

```tex
\label{prob:cp-ii-0040}
\par\noindent\textbullet\quad \textbf{Positivity/definiteness:} $\|p\|_{I}\ge0$.
	If $\|p\|_{I}=0$ then $p(t)=0$ for all $t\in I$.
	Since $I$ is infinite and has a limit point in $[0,1]$, the identity theorem gives $p\equiv0$.
```

## CP-II-0042

- chapter line: 12088

```tex
\label{prob:cp-ii-0042}
(Defective).

$A=\begin{pmatrix}1&1\\0&1\end{pmatrix}$ has $p_A(\lambda)=(\lambda-1)^2$. The eigenspace is $\ker(A-I)=\mathrm{span}\{(1,0)^\top\}$, so $m_a(1)=2$ but $m_g(1)=1$; $A$ is not diagonalizable and is already a Jordan block.
```

## CP-II-0045

- chapter line: 12171

```tex
\label{prob:cp-ii-0045}
\par\noindent\textbullet\quad For every multi-index $\alpha$ and every $1\le p<\infty$,
	\[
	D^\alpha f\in L^p(\mathbb{R}^n).
	\]
	Indeed, for each $N$ we have
	$|D^\alpha f(x)|\le C_{\alpha,N}(1+|x|)^{-N}$, and choosing
	$N$ with $Np>n$ gives $|D^\alpha f|^p\in L^1$.
```

## CP-II-0046

- chapter line: 12182

```tex
\label{prob:cp-ii-0046}
\par\noindent\textbullet\quad Parts (a)--(d) assume $F$ is a \emph{positive simple function}:
	a finite linear combination of characteristic functions.
	On these, one may freely permute and decompose integrals.
```

## CP-II-0049

- chapter line: 12189

```tex
\label{prob:cp-ii-0049}
\par\noindent (a)\quad Show $\displaystyle \int_{\mathbb{R}}\psi_{n_1,k_1}\psi_{n_2,k_2}=\delta_{n_1n_2}\delta_{k_1k_2}$.
```

## CP-II-0050

- chapter line: 12194

```tex
\label{prob:cp-ii-0050}
\par\noindent\textbullet\quad $f(x,y)=(e^x\cos y,\,e^x\sin y)$ on $\mathbb{R}^2$:
	$\det Df(x,y)=e^{2x}\ne0$, hence locally invertible at every point.

\hfill$\Box$
```

## CP-II-0051

- chapter line: 12202

```tex
\label{prob:cp-ii-0051}
— Powers preserve uniform convergence

Let $f_n:[0,1]\to\mathbb{R}$ satisfy $f_n\to f$ uniformly on $[0,1]$, and suppose $f$ is bounded.
Show that for any integer $m\ge1$, the functions $g_n(t)=f_n(t)^m$ converge uniformly on $[0,1]$
to $g(t)=f(t)^m$.

For all $a,b\in\mathbb{R}$ and $m\ge1$,
\[
a^m-b^m=(a-b)\sum_{k=0}^{m-1}a^{m-1-k}b^{k},
\]
hence if $|a|,|b|\le M$ then $|a^m-b^m|\le m M^{m-1}|a-b|$.
Uniform convergence $f_n\to f$ implies $\|f_n-f\|_\infty\to0$.

Let $M=\|f\|_\infty<\infty$. Since $f_n\to f$ uniformly, there exists $N$ with
$\|f_n-f\|_\infty\le 1$ for all $n\ge N$. Then for $n\ge N$,
\[
\|f_n\|_\infty \le \|f\|_\infty+\|f_n-f\|_\infty \le M+1=:M'.
\]
For any $t\in[0,1]$,
\[
|f_n(t)^m-f(t)^m|
\le |f_n(t)-f(t)| \sum_{k=0}^{m-1} |f_n(t)|^{m-1-k} |f(t)|^{k}
\le m(M')^{m-1}\,|f_n(t)-f(t)|.
\]
Taking sup over $t$ yields
\[
\|f_n^m-f^m\|_\infty \le m(M')^{m-1}\,\|f_n-f\|_\infty \xrightarrow[n\to\infty]{} 0.
\]
Therefore $f_n^m\to f^m$ uniformly on $[0,1]$.


	\par\noindent\textbullet\quad $f_n(t)=t+\tfrac1n$, $f(t)=t$, $m=3$:
	$\|f_n^3-f^3\|_\infty \le 12/n \to 0$.
	\par\noindent\textbullet\quad $f_n(t)=\sin(nt)/n$, $f\equiv0$: for any $m\ge1$,
	$\|f_n^m-f^m\|_\infty=\|f_n\|_\infty^m \le (1/n)^m \to 0$.
```

## CP-II-0053

- chapter line: 12241

```tex
\label{prob:cp-ii-0053}
\par\noindent (c)\quad Is such a phenomenon possible in $\ell^1$ or $\ell^2$ when the two norms are chosen
	from the standard norms on $\ell^1,\ell^2,\ell^\infty$?
	What about in $C([0,1])$ when the two norms are chosen from $L^1,L^2,L^\infty$?

\bigskip
```

## CP-II-0054

- chapter line: 12250

```tex
\label{prob:cp-ii-0054}
(*)

\renewcommand\labelenumi{(\alph{enumi})}
\par\noindent\textbullet\quad If $f:\mathbb{R}^n\to\mathbb{R}^m$ is continuous and $U$ open in $\mathbb{R}^m$, then $f^{-1}(U)$ is open.
\par\noindent\textbullet\quad If $f^{-1}(U)$ is open for every open $U\subset\mathbb{R}^m$, then $f$ is continuous on $\mathbb{R}^n$.
```

## CP-II-0056

- chapter line: 12259

```tex
\label{prob:cp-ii-0056}
In $H=\ell^2$, the canonical basis $(e_i)$ satisfies $e_i\rightharpoonup0$
	but $\|e_i\|=1$.  Thus weak convergence does not imply norm convergence.

	\bigskip
```

## CP-II-0058

- chapter line: 12357

```tex
\label{prob:cp-ii-0058}
$f_n(x)=\sin(x+n)$ on $[0,2\pi]$ (Subsequences converge uniformly)
```

## CP-II-0060

- chapter line: 12362

```tex
\label{prob:cp-ii-0060}
— Distributions annihilated by a power of $x$

Suppose $u\in\mathcal D'(\mathbb R)$ satisfies $x\,u=0$. Show that $u=c\,\delta_0$ for some $c\in\mathbb C$.
Find the most general $u\in\mathcal D'(\mathbb R)$ such that $x^k u=0$ for some $k\in\mathbb N$.

Since $\langle x u,\phi\rangle=\langle u,x\phi\rangle$, the condition $x u=0$ says $u$ vanishes on $x\mathcal D(\mathbb R)$.
Thus $\operatorname{supp}u\subset\{0\}$ and $u=\sum_{m=0}^{M} c_m\,\delta_0^{(m)}$.
Moreover,
\[
x\delta_0^{(m)}=-m\,\delta_0^{(m-1)} \qquad (m\ge1),\qquad x\delta_0=0.
\]
Hence $0=x u=\sum_{m=1}^{M} c_m(-m)\delta_0^{(m-1)}$ forces $c_m=0$ for $m\ge1$, so $u=c_0\delta_0$.

Iterating,
\[
x^k\delta_0^{(m)}=(-1)^k m(m-1)\cdots(m-k+1)\,\delta_0^{(m-k)},
\]
which is zero iff $m<k$. Therefore
\[
\{u\in\mathcal D'(\mathbb R):\,x^k u=0\}
=\operatorname{span}\{\delta_0,\,\delta_0',\,\dots,\,\delta_0^{(k-1)}\}.
\]

\bigskip

\textbf{Example 1 ($xu=0$ forces a pure mass at $0$).}
For $u=c_0\delta_0$,
\[
\langle x u,\phi\rangle=\langle u,x\phi\rangle=c_0\,x\phi(0)=0,
\]
so $x u=0$. Conversely, if $xu=0$ and $u=\sum_{m=0}^M c_m\delta_0^{(m)}$,
then using $x\delta_0^{(m)}=-m\,\delta_0^{(m-1)}$,
\[
0=xu=\sum_{m=1}^M c_m(-m)\,\delta_0^{(m-1)}
\quad\Rightarrow\quad c_m=0\ \ (m\ge1),
\]
hence $u=c_0\delta_0$.

\medskip

\textbf{Example 2 (all solutions of $x^2 u=0$).}
Write $u=a\,\delta_0+b\,\delta_0'+\sum_{m\ge2} c_m\delta_0^{(m)}$.
Since $x^2\delta_0=0$ and $x^2\delta_0' = x(-\delta_0)=0$, while
\[
x^2\delta_0^{(m)}=x\big(-m\,\delta_0^{(m-1)}\big)
=m(m-1)\,\delta_0^{(m-2)}\neq0 \quad \text{for } m\ge2,
\]
we must have $c_m=0$ for $m\ge2$. Therefore the solution space is
$\operatorname{span}\{\delta_0,\delta_0'\}$.

\medskip

\textbf{Example 3 (general $k$).}
Using $x^k\delta_0^{(m)}=(-1)^k m(m-1)\cdots(m-k+1)\,\delta_0^{(m-k)}$, the product vanishes
iff $m<k$. Hence precisely the linear span
\[
\{u:\ x^k u=0\}=\operatorname{span}\{\delta_0,\delta_0',\dots,\delta_0^{(k-1)}\}.
\]

\medskip

\textbf{Example 4 (failure when $m\ge k$).}
Take $k=3$ and $u=\delta_0^{(3)}$. Then
$x^3 u = (-1)^3 3\cdot 2\cdot 1\,\delta_0 = -6\,\delta_0\neq 0$, so $u$ is not a solution.

\bigskip

If $x^2 u=0$ then $u=a\,\delta_0+b\,\delta_0'$. If $x u=0$ then $u=c\,\delta_0$.

\bigskip
\bigskip
```

## CP-II-0065

- chapter line: 12507

```tex
\label{prob:cp-ii-0065}
— Hat functions and piecewise–linear interpolation

For $n,r\in\mathbb{Z}$ and $n\ge1$, define $\Delta_{n,r}:[-1,1]\to\mathbb{R}$ by
\[
\Delta_{n,r}(x)=\max\{0,\; 1-n|x-rn^{-1}|\}.
\]
Sketch $\Delta_{n,r}$.
For $f:[-1,1]\to\mathbb{R}$, show that
\[
f_n(x)=\sum_{m=-n}^{n} f\!\left(\frac{m}{n}\right)\Delta_{n,m}(x)
\]
is piecewise linear with $f_n(r/n)=f(r/n)$.
Show that if $f$ is continuous, then $\|f_n-f\|_\infty\to0$ as $n\to\infty$.

Each $\Delta_{n,r}$ is a tent function supported on $[(r-1)/n,(r+1)/n]$ with value $1$
at $x=r/n$ and slopes $\pm n$. On each cell $[k/n,(k+1)/n]$, exactly two hats are nonzero,
$\Delta_{n,k}$ and $\Delta_{n,k+1}$, and they satisfy
$\Delta_{n,k}(x)+\Delta_{n,k+1}(x)=1$. If $f$ is continuous on $[-1,1]$, then its modulus
of continuity $\omega_f(\delta)=\sup_{|x-y|\le\delta}|f(x)-f(y)|$ obeys
$\omega_f(\delta)\to0$ as $\delta\downarrow0$.

\par\medskip\noindent\textbf{Sketch / explicit form of $\Delta_{n,r}$.}\quad
\[
\Delta_{n,r}(x)=
\begin{cases}
	n\big(x-\frac{r-1}{n}\big), & x\in\big[\frac{r-1}{n},\frac{r}{n}\big],\\[2pt]
	n\big(\frac{r+1}{n}-x\big), & x\in\big[\frac{r}{n},\frac{r+1}{n}\big],\\[2pt]
	0, & \text{otherwise.}
\end{cases}
\]

If $x\in[k/n,(k+1)/n]$, then
\[
\Delta_{n,k}(x)=\frac{k+1}{n}-x,\qquad
\Delta_{n,k+1}(x)=x-\frac{k}{n},
\]
and all other $\Delta_{n,m}(x)$ vanish. Hence
\[
f_n(x)=f\!\left(\frac{k}{n}\right)\Big(\frac{k+1}{n}-x\Big)
+f\!\left(\frac{k+1}{n}\right)\Big(x-\frac{k}{n}\Big),
\]
which is linear in $x$ on that interval. In particular,
$f_n(r/n)=f(r/n)$ for each $r$.

For $x\in[k/n,(k+1)/n]$ write $x=\lambda \frac{k}{n}+(1-\lambda)\frac{k+1}{n}$ with
$\lambda=\frac{k+1}{n}-x\in[0,1]$. Then
\[
f_n(x)=\lambda f\!\left(\frac{k}{n}\right)
+(1-\lambda)f\!\left(\frac{k+1}{n}\right),
\]
so
\[
|f(x)-f_n(x)|
\le \lambda\Big|f(x)-f\!\left(\frac{k}{n}\right)\Big|
+(1-\lambda)\Big|f(x)-f\!\left(\frac{k+1}{n}\right)\Big|
\le \omega_f\!\left(\frac{1}{n}\right).
\]
Therefore $\|f-f_n\|_\infty \le \omega_f(1/n)\to0$ as $n\to\infty$.

	\par\noindent\textbullet\quad $f(x)=x^2$: $f_n$ is the polygonal line through $\{(m/n,(m/n)^2)\}$;
	$\|f-f_n\|_\infty=\Theta(n^{-2})$.
	\par\noindent\textbullet\quad $f(x)=|x|$: convergence is uniform with $\|f-f_n\|_\infty=O(n^{-1})$ (Lipschitz $1$).
	\par\noindent\textbullet\quad $f=\operatorname{sign}(x)$ (discontinuous): $f_n$ does not converge uniformly to $f$;
	uniform convergence requires continuity.
```

## CP-II-0067

- chapter line: 12591

```tex
\label{prob:cp-ii-0067}
\par\noindent (a)\quad For each fixed $x\in\mathbb{R}^n$ the translation operator
		$\tau_x:\mathcal{E}(\mathbb{R}^n)\to\mathcal{E}(\mathbb{R}^n)$,
		defined by $(\tau_x\phi)(y)=\phi(y-x)$, is continuous.
		Moreover, if $x_l\to 0$ in $\mathbb{R}^n$ and $\phi\in\mathcal{E}$,
		then
		\[
		\tau_{x_l}\phi \longrightarrow \phi
		\quad\text{in }\mathcal{E}(\mathbb{R}^n).
		\]
```

## CP-II-0068

- chapter line: 12604

```tex
\label{prob:cp-ii-0068}
A sequence with $L^p$ convergence to $0$ but no pointwise limit

Construct a sequence $(f_j)$ of measurable functions on $I=(0,1)$ such that
\[
f_j \to 0 \quad \text{in } L^p(I)\ \text{for every } 1\le p<\infty,
\]
but for every $x\in(0,1)$ the numeric sequence $(f_j(x))$ does \emph{not} converge.
Also determine whether an analogous construction is possible for $p=\infty$.

\textbf{Setup.} Let $I=(0,1)$ and $1\le p<\infty$. Fix an irrational $\alpha\in(0,1)$ and define
\[
a_j=\{j\alpha\}\in[0,1), \qquad
I_j=(a_j,a_j+1/j)\ (\mathrm{mod}\ 1), \qquad
f_j=\mathbf 1_{I_j}.
\]

\textbf{$L^p$ convergence.} $\|f_j\|_{L^p(I)} = |I_j|^{1/p} = (1/j)^{1/p}\to 0$.

\textbf{No pointwise convergence anywhere.}
By DirichletĂ˘â‚¬â„˘s approximation, for every $x\in(0,1)$ there are infinitely many $j$ with
$\|j\alpha-x\|<1/j$, hence $x\in I_j$ infinitely often.
Therefore $f_j(x)$ takes the values $1$ and $0$ infinitely often and does not converge at any $x$.

\textbf{Case $p=\infty$.} If $\|f_j\|_{L^\infty}\to 0$ then $|f_j(x)|\le \|f_j\|_{L^\infty}\to 0$
for each $x$, so $f_j(x)\to 0$ everywhere. Thus no such sequence exists in $L^\infty$.

\bigskip\hrule\bigskip
```

## CP-II-0074

- chapter line: 12666

```tex
\label{prob:cp-ii-0074}
Trigonometric series

$f_i(x)=\dfrac{\sin(ix)}{i^2}$, $x\in[0,2\pi]$.
Bounded by $1/i^2$, series $\sum 1/i^2$ converges $\Rightarrow$ uniform convergence.

---
```

## CP-II-0078

- chapter line: 12676

```tex
\label{prob:cp-ii-0078}
\par\noindent\textbullet\quad This identity shows that multiplication by $g\in L^q$ defines a
	bounded linear functional on $L^p$ with operator norm $\|g\|_{L^q}$
	--- the starting point of $L^p$ duality.

\bigskip
```

## CP-II-0079

- chapter line: 12685

```tex
\label{prob:cp-ii-0079}
\par\noindent\textbullet\quad Use (A) to pass $x\to 1^-$ or to prove uniform convergence on $[r,1]$.
```

## CP-II-0081

- chapter line: 12711

```tex
\label{prob:cp-ii-0081}
\par\noindent\textbullet\quad \textbf{Moving bump (vanishing locally).}
		In $L^{p}(\mathbb R)$, $f_j=\mathbf 1_{(j,j+1)}$. Then $\|f_j\|_{p}=1$ and for any bounded $E$,
		eventually $\int_E f_j=0$, hence $f_j\rightharpoonup 0$ (but not strongly).
```

## CP-II-0084

- chapter line: 12718

```tex
\label{prob:cp-ii-0084}
\par\noindent\textbullet\quad \textbf{Uniform convergence on all of $X$.}
	Uniform convergence on $X=\mathbb{R}\setminus\mathbb{N}$ would require
	\[
	\sup_{x\in X}\ \sum_{m>n} (x-m)^{-2}\ \longrightarrow\ 0\qquad (n\to\infty).
	\]
	This fails because near $x=n+1$ the tail contains $(x-(n+1))^{-2}$, which can be arbitrarily large.
```

## CP-II-0087

- chapter line: 12728

```tex
\label{prob:cp-ii-0087}
\par\noindent\textbullet\quad no pathological behaviour can occur.

Once the inequality is established for simple functions, one extends it
to general measurable functions (continuous, $C^\infty$, polynomials,
Gaussians, trigonometric functions, etc.) by:
```

## CP-II-0089

- chapter line: 12737

```tex
\label{prob:cp-ii-0089}
\par\noindent\textbullet\quad \textbf{Exact uniform error.}
	For $P_n(x)=\sum_{j\le n}\gamma_j T_{3j}(x)$ with $\gamma_j\ge 0$,
	\[
	\|f-P_n\|_\infty = S_n:=\sum_{j>n}\gamma_j,
	\]
	and this value is attained at $x_k=\cos\!\big(\tfrac{k\pi}{3^{n+1}}\big)$.
```

## CP-II-0093

- chapter line: 12764

```tex
\label{prob:cp-ii-0093}
\par\noindent\textbullet\quad $F$ is \emph{lower semicontinuous (l.s.c.) at $x$} if
		$\displaystyle \liminf_{x'\to x} F(x') \ge F(x)$.
		Equivalently, each sublevel set $\{F\le \alpha\}$ is closed, or
		the epigraph $\operatorname{epi}F=\{(x,t):F(x)\le t\}$ is closed in $X\times\mathbb R$.
```

## CP-II-0094

- chapter line: 12772

```tex
\label{prob:cp-ii-0094}
Let $A\subset \mathbb{R}^n$ and $f,g:A\to\mathbb{R}$.

\renewcommand\labelenumi{(\alph{enumi})}
\par\noindent\textbullet\quad Suppose $f$ and $g$ are uniformly continuous and bounded on $A$. Then $fg$ is uniformly continuous and bounded on $A$.

\textit{Solution (boundedness).} If $|f|\le M_f$ and $|g|\le M_g$ on $A$, then $|fg|\le M_fM_g$.

\textit{Solution (uniform continuity).} Fix $\varepsilon>0$ and set
$\eta=\min\!\left(1,\frac{\varepsilon}{2(M_f+M_g+1)}\right)$.
By uniform continuity of $f$ and $g$, there exists $\delta>0$ such that
$\|x-y\|<\delta$ implies $|f(x)-f(y)|<\eta$ and $|g(x)-g(y)|<\eta$.
Then for such $x,y$,
\begin{align*}
|f(x)g(x)-f(y)g(y)|
&= |[f(x)-f(y)][g(x)-g(y)] + g(y)[f(x)-f(y)] + f(y)[g(x)-g(y)]|\\
&\le \eta^2 + M_g\,\eta + M_f\,\eta
\;\le\; (M_f+M_g+1)\eta \;\le\; \varepsilon.
\end{align*}
Hence $fg$ is uniformly continuous.

\par\noindent\textbullet\quad If $f$ and $g$ are uniformly continuous but not necessarily bounded, $fg$ need not be uniformly continuous.

\textit{Counterexample.} On $\mathbb{R}$, take $f(x)=x$ and $g(x)=\sin x$. Both are uniformly continuous (Lipschitz).
Assume $x\sin x$ were uniformly continuous. For $\varepsilon=1$, let $\delta>0$ be its modulus.
Set $t=\min(\delta/2,1)$ and take $y_k=k\pi$, $x_k=k\pi+t$.
Then $|x_k-y_k|=t<\delta$ but
\[
|x_k\sin x_k - y_k\sin y_k| = |(k\pi+t)\sin t| \ge k\pi \sin t \xrightarrow{k\to\infty} \infty,
\]
contradicting uniform continuity. Thus $x\sin x$ is not uniformly continuous.
```

## CP-II-0095

- chapter line: 12806

```tex
\label{prob:cp-ii-0095}
\par\noindent\textbullet\quad \textbf{Strict inequality in weak l.s.c.} In a Hilbert space,
		let $(e_n)$ be an orthonormal sequence. Then $e_n\rightharpoonup 0$ but
		$\|0\|=0<\liminf_n\|e_n\|=1$.
```

## CP-II-0097

- chapter line: 12813

```tex
\label{prob:cp-ii-0097}
Let $f(x)=|x|^{-n/p}\mathbf{1}_{\{|x|\le 1\}}(x)$.
	Then for $\lambda>1$,
	\[
	\{|f|>\lambda\}=\{|x|<\lambda^{-p/n}\},\qquad
	\mu(\{|f|>\lambda\})=c_n\,\lambda^{-p}.
	\]
	Thus $f\in L^{p,\infty}(\mathbb{R}^n)$ with $\|f\|_{p,\infty}\sim c_n^{1/p}$,
	but $f\notin L^p(\mathbb{R}^n)$ since
	\[
	\int_{|x|\le1}|x|^{-n}\,dx=\infty.
	\]
	A tail variant $|x|^{-n/p}\mathbf{1}_{\{|x|\ge1\}}$
	is also in $L^{p,\infty}$ but not in $L^p$.
```

## CP-II-0099

- chapter line: 12830

```tex
\label{prob:cp-ii-0099}
Algebra and differentiation of regular distributions

\noindent
(a)\; Show that if $f_1,f_2\in C^0(\Omega)$ and $a\in C^\infty(\Omega)$, then
\[
aT_{f_1} + T_{f_2} = T_{a f_1 + f_2}.
\]

\medskip\noindent
(b)\; Show that if $f\in C^k(\Omega)$ then
\[
D^\alpha T_f = T_{D^\alpha f}
\qquad\text{for all multiindices }\alpha\text{ with }|\alpha|\le k.
\]
Deduce that $\iota\circ D^\alpha = D^\alpha\circ\iota$, where
$\iota:C^k(\Omega)\to\mathcal{D}'(\Omega)$ is the natural embedding
$f\mapsto T_f$.

\medskip\noindent
(c)\; Deduce that if $f\in C^k(\Omega)$ then
\[
\sum_{|\alpha|\le k} a_\alpha D^\alpha T_f = T_{Lf},
\]
where
\[
Lf := \sum_{|\alpha|\le k} a_\alpha D^\alpha f
\]
and $a_\alpha\in C^\infty(\Omega)$.

\bigskip

Let $f\in C^0(\Omega)$ and
\[
T_f(\varphi) := \int_\Omega f(x)\,\varphi(x)\,dx.
\]
For $a\in C^\infty(\Omega)$ and $T\in\mathcal{D}'(\Omega)$ define
$(aT)(\varphi):=T(a\varphi)$. For a multiindex $\alpha$,
\[
\langle D^\alpha T,\varphi\rangle
:= (-1)^{|\alpha|}\langle T,D^\alpha\varphi\rangle.
\]

If $f_1,f_2\in C^0(\Omega)$ and $a\in C^\infty(\Omega)$, show
\[
aT_{f_1} + T_{f_2} = T_{af_1+f_2}.
\]
```

## CP-II-0101

- chapter line: 12880

```tex
\label{prob:cp-ii-0101}
\par\noindent\textbullet\quad The set \((0.2,0.7]\) is \emph{not} open in \(X\)
		because the point \(0.7\) would need a right-hand neighborhood inside \(X\),
		which does not exist.
```

## CP-II-0102

- chapter line: 12887

```tex
\label{prob:cp-ii-0102}
— Weak-* limits of $\sin(nx)$ and $\sin^2(nx)$

Recall that $L^\infty(\mathbb R)=(L^1(\mathbb R))'$. Consider the sequence $(f_n)_{n\ge1}\subset L^\infty(\mathbb R)$ given by
\[
f_n(x)=\sin(nx).
\]
Show that $f_n \stackrel{*}{\rightharpoonup} 0$ in $L^\infty(\mathbb R)$.
Show further that $f_n^2 \stackrel{*}{\rightharpoonup} g$ for some $g\in L^\infty(\mathbb R)$, and determine $g$.

Identify $L^\infty(\mathbb R)$ with $(L^1(\mathbb R))'$ via the pairing
$\langle g,\varphi\rangle=\int_{\mathbb R} g(x)\,\varphi(x)\,dx$ for $\varphi\in L^1$.
Let $f_n(x)=\sin(nx)$.

\smallskip

\par\medskip\noindent\textbf{(a) $f_n \overset{*}\rightharpoonup 0$.}\quad
For any $\varphi\in L^1(\mathbb R)$,
\[
\int_{\mathbb R}\sin(nx)\,\varphi(x)\,dx \xrightarrow[n\to\infty]{} 0
\]
by the Riemann--Lebesgue lemma. Hence $f_n \overset{*}\rightharpoonup 0$ in $L^\infty$.

\smallskip

\par\medskip\noindent\textbf{(b) $f_n^2 \overset{*}\rightharpoonup \tfrac12$.}\quad
Using $\sin^2(nx)=\frac12(1-\cos(2nx))$,
\[
\int \sin^2(nx)\,\varphi
= \frac12\int \varphi - \frac12\int \varphi(x)\cos(2nx)\,dx
\longrightarrow \frac12\int \varphi(x)\,dx.
\]
Therefore $f_n^2 \overset{*}\rightharpoonup g$ with $g(x)\equiv \frac12$ in $L^\infty(\mathbb R)$.

\bigskip
\bigskip
```

## CP-II-0107

- chapter line: 13085

```tex
\label{prob:cp-ii-0107}
{Powers preserve uniform convergence (under a bound).}{powers-uniform}
	Let $f_n:[0,1]\to\mathbb R$ converge uniformly to $f$. Suppose $f$ is bounded.
	Show that for every positive integer $m$,
	\[
	g_n(t):=f_n(t)^m \quad\text{converges uniformly on }[0,1]\text{ to }\quad
	g(t):=f(t)^m.
	\]
```

## CP-II-0109

- chapter line: 13096

```tex
\label{prob:cp-ii-0109}
Which functions are (i) continuous, (ii) uniformly continuous on their domains?

\renewcommand\labelenumi{(\alph{enumi})}
\par\noindent\textbullet\quad $f:\mathbb{R}\to\mathbb{R}$, $x\mapsto e^x$: continuous, not uniformly continuous.
\par\noindent\textbullet\quad $f:(0,1)\to\mathbb{R}$, $x\mapsto e^x$: continuous, uniformly continuous (MVT and $e^c\le e$).
\par\noindent\textbullet\quad $f:\mathbb{R}\to\mathbb{R}$, $x\mapsto\sin x$: continuous, uniformly continuous ($|\sin x-\sin y|\le |x-y|$).
\par\noindent\textbullet\quad $f:[0,\infty)\to\mathbb{R}$, $x\mapsto \sqrt{x}$: continuous, uniformly continuous ($|\sqrt{x}-\sqrt{y}|\le \sqrt{|x-y|}$).
\par\noindent \textit{f)}\quad $f:\mathbb{R}^n\setminus\{0\}\to\mathbb{R}^n$, $x\mapsto x/\|x\|$: continuous, not uniformly continuous (fails near $0$).
```

## CP-II-0110

- chapter line: 13108

```tex
\label{prob:cp-ii-0110}
(solutions)

Let $s>\tfrac12$ and $u\in\mathcal S(\mathbb R^n)$, $x=(x',x_n)$, $\xi=(\xi',\xi_n)$.

We have
\[
\widehat{Tu}(\xi')
= \int_{\mathbb R^{n-1}} e^{-ix'\cdot\xi'}u(x',0)\,dx'.
\]
Using the inverse Fourier representation of $u$,
\[
u(x',0)
= \frac{1}{(2\pi)^n}\int_{\mathbb R^{n-1}}\!\int_{\mathbb R}
e^{i(x'\cdot\eta'+0\cdot\eta_n)}\widehat u(\eta',\eta_n)\,d\eta_n d\eta',
\]
we obtain
\[
\widehat{Tu}(\xi')
= \frac{1}{(2\pi)^n}\int_{\mathbb R^{n-1}}\!\int_{\mathbb R}
\left(\int_{\mathbb R^{n-1}} e^{-ix'\cdot\xi'}e^{ix'\cdot\eta'}dx'\right)
\widehat u(\eta',\eta_n)\,d\eta_n d\eta'.
\]
The inner integral equals $(2\pi)^{n-1}\delta(\eta'-\xi')$, hence
\[
\widehat{Tu}(\xi') = \frac{1}{2\pi}\int_{\mathbb R}\widehat u(\xi',\xi_n)\,d\xi_n.
\]

From (a),
\[
\widehat{Tu}(\xi')
= \frac{1}{2\pi}\int_{\mathbb R}
(1+|\xi|^2)^{\frac{s}{2}}\widehat u(\xi',\xi_n)\,
(1+|\xi|^2)^{-\frac{s}{2}}\,d\xi_n.
\]
By the Cauchy--Schwarz inequality,
\[
\bigl|\widehat{Tu}(\xi')\bigr|^2
\le \frac{1}{(2\pi)^2}
\left(\int_{\mathbb R}(1+|\xi|^2)^s |\widehat u(\xi',\xi_n)|^2 d\xi_n\right)
\left(\int_{\mathbb R}\frac{d\xi_n}{(1+|\xi|^2)^s}\right).
\]

Set
\[
I(\xi'):=\int_{\mathbb R}\frac{d\xi_n}{(1+|\xi'|^2+\xi_n^2)^s}.
\]
With $L=\sqrt{1+|\xi'|^2}$ and $\xi_n=Lt$,
\[
I(\xi')=L^{1-2s}\int_{\mathbb R}\frac{dt}{(1+t^2)^s}
= C_s(1+|\xi'|^2)^{\frac12-s},
\]
where $C_s<\infty$ for $s>\tfrac12$. Using (b),
\[
\begin{aligned}
	\|Tu\|_{H^{s-\frac12}(\mathbb R^{n-1})}^2
	&= \int_{\mathbb R^{n-1}}(1+|\xi'|^2)^{s-\frac12}|\widehat{Tu}(\xi')|^2\,d\xi'\\
	&\le \frac{1}{(2\pi)^2}\int_{\mathbb R^{n-1}}(1+|\xi'|^2)^{s-\frac12}
	\left(\int_{\mathbb R}(1+|\xi|^2)^s|\widehat u(\xi',\xi_n)|^2 d\xi_n\right) I(\xi')\,d\xi'\\
	&= \frac{C_s}{(2\pi)^2}\iint_{\mathbb R^{n-1}\times\mathbb R}(1+|\xi|^2)^s
	|\widehat u(\xi',\xi_n)|^2 d\xi_n d\xi' \\
	&= C(s)\,\|u\|_{H^s(\mathbb R^n)}^2.
\end{aligned}
\]
Thus $\|Tu\|_{H^{s-\frac12}}\le C(s)\|u\|_{H^s}$.

The map $T:\mathcal S(\mathbb R^n)\to H^{s-\frac12}(\mathbb R^{n-1})$ is bounded by (c).
Since $\mathcal S(\mathbb R^n)$ is dense in $H^s(\mathbb R^n)$, $T$ extends uniquely by continuity to a bounded linear operator
\[
T:H^s(\mathbb R^n)\longrightarrow H^{s-\frac12}(\mathbb R^{n-1}),\quad s>\tfrac12.
\]

Let $\nu\in\mathcal S(\mathbb R^{n-1})$ and $\phi\in C_c^\infty(\mathbb R)$ satisfy
$\int_{\mathbb R}\phi(t)dt=\sqrt{2\pi}$. Define
\[
\widehat u(\xi',\xi_n)
:=\frac{\widehat\nu(\xi')}{\sqrt{1+|\xi'|^2}}\,
\phi\!\left(\frac{\xi_n}{\sqrt{1+|\xi'|^2}}\right).
\]
Then
\[
\begin{aligned}
	\|u\|_{H^s(\mathbb R^n)}^2
	&= \iint_{\mathbb R^{n-1}\times\mathbb R}
	(1+|\xi|^2)^s |\widehat u(\xi',\xi_n)|^2\,d\xi_n d\xi'\\
	&= \int_{\mathbb R^{n-1}} \frac{|\widehat\nu(\xi')|^2}{1+|\xi'|^2}
	\left(\int_{\mathbb R}(1+|\xi'|^2+\xi_n^2)^s
	\Bigl|\phi\!\Bigl(\frac{\xi_n}{\sqrt{1+|\xi'|^2}}\Bigr)\Bigr|^2 d\xi_n\right)d\xi'.
\end{aligned}
\]
With $L=\sqrt{1+|\xi'|^2}$ and $\xi_n=Lt$,
\[
\int_{\mathbb R}(1+|\xi'|^2+\xi_n^2)^s
\Bigl|\phi\!\Bigl(\frac{\xi_n}{L}\Bigr)\Bigr|^2 d\xi_n
= L^{2s+1}\int_{\mathbb R}(1+t^2)^s|\phi(t)|^2 dt
\le C_\phi (1+|\xi'|^2)^{s+\frac12},
\]
where $C_\phi:=\int_{\mathbb R}(1+t^2)^s|\phi(t)|^2dt$.
Hence
\[
\|u\|_{H^s(\mathbb R^n)}^2
\le C_\phi \int_{\mathbb R^{n-1}}|\widehat\nu(\xi')|^2(1+|\xi'|^2)^{s-\frac12}d\xi'
= C_\phi\,\|\nu\|_{H^{s-\frac12}(\mathbb R^{n-1})}^2.
\]

Using (a),
\[
\widehat{Tu}(\xi')
= \frac{1}{2\pi}\int_{\mathbb R}\widehat u(\xi',\xi_n)\,d\xi_n
= \frac{\widehat\nu(\xi')}{2\pi\sqrt{1+|\xi'|^2}}
\int_{\mathbb R}\phi\!\left(\frac{\xi_n}{\sqrt{1+|\xi'|^2}}\right)d\xi_n.
\]
With $\xi_n=Lt$, $L=\sqrt{1+|\xi'|^2}$,
\[
\int_{\mathbb R}\phi\!\left(\frac{\xi_n}{L}\right)d\xi_n
= L\int_{\mathbb R}\phi(t)dt = L\sqrt{2\pi}.
\]
Thus
\[
\widehat{Tu}(\xi') = \frac{\widehat\nu(\xi')}{2\pi\sqrt{1+|\xi'|^2}}L\sqrt{2\pi}
= \widehat\nu(\xi'),
\]
so $Tu=\nu$.
By density, this defines a bounded extension operator
$E:H^{s-\frac12}(\mathbb R^{n-1})\to H^s(\mathbb R^n)$ with $T\circ E = \mathrm{Id}$.
Therefore $T:H^s(\mathbb R^n)\to H^{s-\frac12}(\mathbb R^{n-1})$ is surjective.
```

## CP-II-0113

- chapter line: 13238

```tex
\label{prob:cp-ii-0113}
\par\noindent\textbullet\quad \textbf{Absolutely continuous:}
		If $f\in L^1(m)$ on $\mathbb R^n$ and $\nu(A)=\int_A f\,dm$, then $\nu\ll m$.
		Moreover, for every $\varepsilon>0$ there exists $\delta>0$ such that
		$\mu(A)<\delta\Rightarrow \nu(A)<\varepsilon$.
```

## CP-II-0120

- chapter line: 13556

```tex
\label{prob:cp-ii-0120}
Probability (sum of random variables).

Let $f$ be the density of a random variable $X$ and $g$ the density of an
independent random variable $Y$. Then the density of $X+Y$ is $f*g$:
\[
(f*g)(x)
= \int_{\mathbb{R}} f(x-y)\,g(y)\,dy.
\]

\medskip
\noindent$\Rightarrow$ \emph{Effect:} convolution describes the law of
sums of independent random variables.

\clearpage
```

## CP-II-0121

- chapter line: 13574

```tex
\label{prob:cp-ii-0121}
\par\noindent\textbullet\quad More generally, for the Dirac mass at $a\in\mathbb{R}^n$,
	\[
	(\delta_a*\phi)(x)
	= \langle\delta_a,\phi(x-\cdot)\rangle
	= \phi(x-a).
	\]
```

## CP-II-0123

- chapter line: 13584

```tex
\label{prob:cp-ii-0123}
\par\noindent\textbullet\quad $f(x)=x^3$ on $\mathbb{R}$: $Df(x)=3x^2$, invertible for $x\ne0$.
	Locally invertible near $x=1$ with inverse $f^{-1}(y)=y^{1/3}$.
```

## CP-II-0124

- chapter line: 13590

```tex
\label{prob:cp-ii-0124}
\par\noindent (a)\quad Show that $\|\cdot\|_{I}$ is a norm on $\mathcal{P}$.
```

## CP-II-0134

- chapter line: 13712

```tex
\label{prob:cp-ii-0134}
\par\noindent\textbullet\quad The classical Minkowski inequality
	\[
	\|f+g\|_{L^p}
	\le
	\|f\|_{L^p} + \|g\|_{L^p}
	\]
	is the triangle inequality for the $L^p$--norm.  Hölder's inequality
	is the main tool in its proof.
```

## CP-II-0140

- chapter line: 13724

```tex
\label{prob:cp-ii-0140}
\par\noindent\textbullet\quad If $y\in B_1(x_0,r)$, then $\|y-x_0\|_1 < r$.
	Hence $\|y-x_0\|_2 < br$, so $y\in B_2(x_0,br)$.
	Thus $B_1(x_0,r)\subseteq B_2(x_0,br)$.
```

## CP-II-0142

- chapter line: 13807

```tex
\label{prob:cp-ii-0142}
\par\noindent\textbullet\quad If $\|f\|_{L^p}=\|g\|_{L^q}=1$, the right side equals $1$.
```

## CP-II-0148

- chapter line: 13852

```tex
\label{prob:cp-ii-0148}
\par\noindent\textbullet\quad $\operatorname{supp}\phi \subset B(0,1)$,
```

## CP-II-0149

- chapter line: 13857

```tex
\label{prob:cp-ii-0149}
Let $X=\mathbb{R}$ with the co-countable topology and let $Y=\{0,1\}$ with the discrete topology. Define
		\[
		f(x)=\begin{cases}
			0,& x\in \mathbb{Q},\\
			1,& x\in \mathbb{R}\setminus \mathbb{Q}.
		\end{cases}
		\]
		In $X$, a sequence converges to $x$ iff it is eventually constant equal to $x$. Hence for any $x_n\to x$,
		the sequence $f(x_n)$ is eventually constant equal to $f(x)$, so $f$ is sequentially continuous.
		However, $\{0\}\subset Y$ is open while $f^{-1}(\{0\})=\mathbb{Q}$ is not open in the co-countable topology.
		Thus $f$ is not continuous.
```

## CP-II-0150

- chapter line: 13872

```tex
\label{prob:cp-ii-0150}
\par\noindent\textbullet\quad Suppose $u(x,t) = \frac{1}{r}v(r,t)$ for some function $v$.
	Show that $u$ solves the wave equation on $\mathbb{R}^3_*\times(-T,T)$
	if and only if $v$ satisfies the one-dimensional wave equation
	\[
	-\,\frac{\partial^2 v}{\partial t^2}(r,t)
	+ \frac{\partial^2 v}{\partial r^2}(r,t)
	= 0
	\quad\text{on } (0,\infty)\times(-T,T).
	\]
```

## CP-II-0151

- chapter line: 13885

```tex
\label{prob:cp-ii-0151}
\par\noindent\textbullet\quad \textbf{Norming functional.} For each $x\in X$, $x\neq0$, there is $\Lambda\in X'$ with
		$\|\Lambda\|=1$ and $\Lambda(x)=\|x\|$.
```

## CP-II-0152

- chapter line: 13891

```tex
\label{prob:cp-ii-0152}
— Moving points vs.\ uniform convergence on $[a,b]$

Let $(f_n)$ be a sequence of real-valued continuous functions on the compact interval $[a,b]$,
and suppose $f_n \to f$ pointwise with $f$ continuous on $[a,b]$.

	\par\noindent (i)\quad If $f_n \to f$ uniformly and $x_n \to x$ in $[a,b]$, prove that $f_n(x_n)\to f(x)$.
	\par\noindent (ii)\quad Conversely, if $f_n \not\to f$ uniformly on $[a,b]$, prove that there exist $x_n\to x$ in $[a,b]$
	such that $f_n(x_n)\not\to f(x)$.

We collect the tools used in the proofs.

\begin{definition}[Uniform convergence]
	A sequence $(f_n)$ of functions on $E$ converges uniformly to $f$ if
	\[
	\sup_{y\in E} |f_n(y)-f(y)| \xrightarrow[n\to\infty]{} 0.
	\]
\end{definition}

\begin{lemma}[Uniform convergence controls moving points]
	Let $E$ be a metric space. If $f_n\to f$ uniformly on $E$ and $x_n\to x$ in $E$ with $f$ continuous at $x$, then
	\[
	|f_n(x_n)-f(x)| \le \underbrace{|f_n(x_n)-f(x_n)|}_{\le \sup_E |f_n-f|} + \underbrace{|f(x_n)-f(x)|}_{\to 0}
	\longrightarrow 0.
	\]
\end{lemma}

\begin{lemma}[Compactness selection]
	If $(x_n)$ is a sequence in a compact set $K$, then there exists a convergent subsequence $x_{n_k}\to x\in K$.
\end{lemma}

\begin{lemma}[Witness for failure of uniform convergence]
	Let $K$ be compact. If $f_n \not\to f$ uniformly on $K$, then there exists $\varepsilon>0$, a strictly increasing $n_k$,
	and points $x_k\in K$ such that $|f_{n_k}(x_k)-f(x_k)|\ge \varepsilon$ for all $k$.
\end{lemma}

\begin{remark}[Equivalence on compact sets]
	Assume each $f_n$ is continuous on $[a,b]$ and $f$ is continuous. Then the following are equivalent:

		\par\noindent\textbullet\quad $f_n \to f$ uniformly on $[a,b]$.
		\par\noindent\textbullet\quad For every sequence $x_n\to x$ in $[a,b]$, we have $f_n(x_n)\to f(x)$.

	The direction (1)$\Rightarrow$(2) follows from uniform convergence together with continuity of $f$. The converse follows from (ii) below.
\end{remark}

Let $x_n\to x$ in $[a,b]$. By uniform convergence and continuity of $f$,
\[
|f_n(x_n)-f(x)| \le \sup_{y\in[a,b]}|f_n(y)-f(y)| + |f(x_n)-f(x)| \xrightarrow[n\to\infty]{} 0,
\]
because the first term $\to 0$ by uniform convergence and the second by continuity of $f$ at $x$.

Assume $f_n \not\to f$ uniformly on $[a,b]$. By the negation of uniform convergence there exist $\varepsilon>0$, indices $n_k\uparrow\infty$,
and points $x_k\in[a,b]$ such that
\[
|f_{n_k}(x_k)-f(x_k)| \ge \varepsilon \qquad \text{for all } k.
\]
By compactness of $[a,b]$, pass to a subsequence (not relabeled) with $x_k\to x\in[a,b]$.
Since $f$ is continuous, $f(x_k)\to f(x)$. Then
\[
\liminf_{k\to\infty} |f_{n_k}(x_k)-f(x)|
\;\ge\; \liminf_{k\to\infty}\Big(|f_{n_k}(x_k)-f(x_k)| - |f(x_k)-f(x)|\Big)
\;\ge\; \varepsilon - 0 \;=\; \varepsilon.
\]
Hence $f_{n_k}(x_k)\not\to f(x)$. Defining a sequence $(x_n)$ by $x_{n_k}=x_k$ and setting $x_n=x$ for other $n$
gives $x_n\to x$ with $f_n(x_n)\not\to f(x)$.

Let
\[
\phi(t) = \max\{1-|t|,\,0\}, \qquad t\in\mathbb{R}.
\]
Define $f_n:[0,1]\to\mathbb{R}$ by
\[
f_n(x) = \phi(nx-1).
\]
Then each $f_n$ is continuous, $f_n(x)\to 0$ for every $x\in[0,1]$ (so $f\equiv 0$), but
\[
\sup_{x\in[0,1]}|f_n(x)-f(x)|=\sup_{x\in[0,1]} f_n(x)=1 \quad \text{for all } n,
\]
so the convergence is \emph{not} uniform. Taking $x_n=1/n\to 0$ yields $f_n(x_n)=1\nrightarrow 0=f(0)$,
which witnesses the conclusion of (ii).

On $[0,1]$, let $f_n(x)=x^n$ and $f\equiv 0$. Then for any $\delta\in(0,1)$, $f_n\to f$ uniformly on $[0,1-\delta]$ with
\[
\sup_{x\in[0,1-\delta]}|f_n(x)-f(x)| \le (1-\delta)^n \to 0.
\]
Thus for any $x_n\to x\in[0,1-\delta]$, the moving-point estimate above gives $f_n(x_n)\to f(x)=0$.
(Contrast with the boundary case $x_n\to 1$, where uniformity fails on $[0,1]$ and moving-point convergence can fail.)

Let $f_n(x)=x e^{-n x}$ on $[0,\infty)$. Then
\[
\sup_{x\ge 0} |f_n(x)| = \frac{1}{n e}\to 0,
\]
so $f_n\to 0$ uniformly. Hence for any $x_n\to x\ge 0$ we have $f_n(x_n)\to 0$.

	\par\noindent\textbullet\quad The compactness of $[a,b]$ is crucial in (ii) to extract a convergent subsequence $(x_{n_k})$.
	\par\noindent\textbullet\quad The continuity of $f$ at the limit point is used twice: in the moving-point estimate and to conclude $f(x_k)\to f(x)$ in (ii).
	\par\noindent\textbullet\quad On compact domains, the equivalence above provides a practical test for uniform convergence: \emph{check moving points}.
```

## CP-II-0154

- chapter line: 13991

```tex
\label{prob:cp-ii-0154}
\par\noindent\textbullet\quad By contrast, for $1<p<\infty$, $L^p$ is reflexive and every bounded sequence
		admits a weakly convergent subsequence (Banach–Alaoglu + reflexivity).
```

## CP-II-0155

- chapter line: 13997

```tex
\label{prob:cp-ii-0155}
Consider the series $\sum_{n=1}^\infty (x-n)^{-2}$ for $x\in X:=\mathbb{R}\setminus\mathbb{N}$.

		\par\noindent\textbullet\quad Show that the series converges pointwise on $X$.
		\par\noindent\textbullet\quad Does the series converge uniformly on $X$?
		\par\noindent\textbullet\quad Show that the sum $f(x)=\sum_{n=1}^\infty (x-n)^{-2}$ is continuous on $X$.


	\textbf{(a) Pointwise convergence.}
	Fix $x\in X$.
	For $n>\lvert x\rvert+1$,
	$|x-n|\ge n-\lvert x\rvert\ge \tfrac{n}{2}$, hence
	\[
	0\le \frac{1}{(x-n)^2}\le \frac{4}{n^2}.
	\]
	Since $\sum 4/n^2$ converges, by comparison $\sum (x-n)^{-2}$ converges (absolutely) for the fixed $x$.
	Thus the series converges pointwise on $X$.

	\medskip

	\textbf{(b) Not uniformly convergent on $X$.}
	Uniform convergence would imply
	\[
	\sup_{x\in X}\sum_{n=N}^{M}\frac{1}{(x-n)^2}\xrightarrow[N,M\to\infty]{}0.
	\]
	But for any $N$ choose an integer $k\ge N$ and take $x=k+\delta$ with $0<\delta<1$.
	Then the tail contains the term $1/(x-k)^2=1/\delta^2$, which can be made arbitrarily large as $\delta\downarrow0$.
	Hence the supremum of the tail is infinite for every $N$, so the Cauchy criterion fails.
	Therefore the series is \emph{not} uniformly convergent on $X$.

	\medskip

	\textbf{(c) Continuity of the sum.}
	Fix $x_0\in X$ and set $\delta=\tfrac12\,\mathrm{dist}(x_0,\mathbb{N})>0$.
	On the interval $I=(x_0-\delta,x_0+\delta)\subset X$, the finitely many functions
	$(x-n)^{-2}$ with $n$ near $I$ are continuous, and for all sufficiently large $n$ and all $x\in I$,
	\[
	\frac{1}{(x-n)^2}\le \frac{4}{n^2}.
	\]
	By the Weierstrass M-test, the tail $\sum_{n>N}(x-n)^{-2}$ converges uniformly on $I$.
	Hence the whole series converges uniformly on $I$ to a continuous function.
	Since $x_0$ was arbitrary, the sum $f$ is continuous on $X$.


	\textbf{Conclusion.}
	The series converges pointwise and absolutely on $X$, is not uniformly convergent on $X$, and its sum belongs to $C(X)$ (local uniform convergence).

	\par\medskip\noindent\textbf{Convergence Criteria for Sequences and Series of Functions}\par

	\textbf{A) Sequences of functions $(f_n:X\to\mathbb R)$.}

		\par\noindent\textbullet\quad \emph{Pointwise convergence:} $f_n\to f$ if $\forall x\in X$, $f_n(x)\to f(x)$.
		\par\noindent\textbullet\quad \emph{Uniform convergence:} $f_n\to f$ uniformly if
		\[
		\sup_{x\in X}|f_n(x)-f(x)|\xrightarrow[n\to\infty]{}0.
		\]
		\par\noindent\textbullet\quad \emph{Uniform Cauchy criterion:} $f_n$ converges uniformly $\iff$
		$\sup_{x\in X}|f_m(x)-f_n(x)|\xrightarrow[m,n\to\infty]{}0$.
		\par\noindent\textbullet\quad \emph{Dini (compact $X$):} If $X$ compact, $f_n\in C(X)$, $f_n\downarrow f$ or $f_n\uparrow f$
		pointwise and $f\in C(X)$, then $f_n\to f$ uniformly.
		\par\noindent\textbullet\quad \emph{Uniform limit theorem:} If $f_n\in C(X)$ and $f_n\to f$ uniformly, then $f\in C(X)$.

	\textbf{Examples.}

		\par\noindent\textbullet\quad $f_n(x)=x^n$ on $[0,1]$: pointwise $\to \mathbf 1_{\{1\}}$, not uniform.
		\par\noindent\textbullet\quad Geometric partial sums $S_n(x)=\sum_{k=0}^n x^k$ on $[0,a]$ with $0<a<1$:
		$(S_n)$ is uniformly Cauchy $\Rightarrow$ uniform convergence.
		\par\noindent\textbullet\quad $f_n(x)=x^n$ on $[0,a]$ with $0<a<1$:
		monotone $\downarrow$ to $0\in C([0,a])$ $\Rightarrow$ uniform by Dini.


	\textbf{B) Series of functions $\sum_{n=1}^\infty f_n$.}

	Let $S_N=\sum_{n=1}^N f_n$.

		\par\noindent\textbullet\quad \emph{Pointwise convergence:} $S_N(x)\to S(x)$ for each $x\in X$.
		\par\noindent\textbullet\quad \emph{Uniform convergence (Cauchy form):} $\sum f_n$ converges uniformly $\iff$
		$\sup_{x\in X}\big|\sum_{k=m}^{n} f_k(x)\big|\xrightarrow[m,n\to\infty]{}0$.
		\par\noindent\textbullet\quad \emph{Weierstrass M-test (uniform absolute):} If $|f_n(x)|\le M_n$ on $X$ and
		$\sum M_n<\infty$, then $\sum f_n$ converges uniformly (hence absolutely).
		\par\noindent\textbullet\quad \emph{Leibniz alternating test (uniform):} If $f_n=(-1)^n a_n$ with $a_n\ge0$,
		$a_{n+1}(x)\le a_n(x)$ for all $x$ and $a_n\to0$ uniformly on $X$,
		then $\sum f_n$ converges uniformly on $X$.
		\par\noindent\textbullet\quad \emph{Dirichlet test (uniform):} If partial sums $A_N(x)=\sum_{n=1}^N a_n(x)$ are
		uniformly bounded on $X$, and $b_n(x)$ is monotone in $n$ for each $x$ with
		$b_n\to0$ uniformly, then $\sum a_n(x)b_n(x)$ converges uniformly.
		\par\noindent\textbullet\quad \emph{Abel test (uniform):} If $\sum a_n(x)$ converges uniformly on $X$ and
		$b_n(x)$ is uniformly bounded and monotone in $n$ for each $x$, then
		$\sum a_n(x)b_n(x)$ converges uniformly.
		\par\noindent\textbullet\quad \emph{Preservation:} If $f_n\in C(X)$ and $\sum f_n$ converges uniformly, then
		the sum $S\in C(X)$ (and $\int \sum f_n=\sum \int f_n$).

	\textbf{Examples.}

		\par\noindent\textbullet\quad (\emph{M-test}) $f_n(x)=\dfrac{x^n}{n^2}$ on $[0,1]$:
		$|f_n|\le 1/n^2$, $\sum 1/n^2<\infty$ $\Rightarrow$ uniform absolute convergence.
		\par\noindent\textbullet\quad (\emph{Leibniz}) $f_n(x)=(-1)^n\dfrac{x^n}{n}$ on $[0,1]$:
		$a_n=x^n/n\downarrow$ and $a_n\to0$ uniformly $\Rightarrow$ uniform convergence (not uniformly absolute).
		\par\noindent\textbullet\quad (\emph{Dirichlet}) $\sum_{n=1}^\infty \dfrac{\sin(nx)}{n}$ on $[\delta,2\pi-\delta]$:
		partial sums of $\sin(nx)$ uniformly bounded; $1/n\downarrow 0$ uniformly
		$\Rightarrow$ uniform convergence on those compact subintervals.
		\par\noindent\textbullet\quad (\emph{Pointwise but not uniform}) $\sum_{n=1}^\infty \dfrac{n^2x}{1+n^4x^2}$ on $[0,1]$:
		pointwise (absolute) convergence, not uniform on the whole interval.
		\par\noindent\textbullet\quad (\emph{Locally uniform}) $\sum_{n=1}^\infty (x-n)^{-2}$ on $X=\mathbb{R}\setminus\mathbb{N}$:
		not uniform on $X$, but uniform on neighborhoods avoiding integers $\Rightarrow$ sum is continuous.

	\par\medskip\noindent\textbf{What Uniform Convergence Buys You (and Key Tools)}\par

	\textbf{Uniform Limit Theorem.}
	If $X$ is a metric space, $f_n\in C(X)$, and $f_n\to f$ uniformly on $X$, then $f\in C(X)$.

	\textbf{Integration commutes with uniform limit (Riemann).}
	If $f_n:[a,b]\to\mathbb{R}$ are Riemann integrable and $f_n\to f$ uniformly on $[a,b]$, then
	\[
	\int_a^b f_n \,dx \to \int_a^b f \,dx .
	\]

	\textbf{Termwise integration of series.}
	If $\sum f_n$ converges uniformly on $[a,b]$ and each $f_n$ is Riemann integrable, then
	\[
	\int_a^b \Big(\sum_{n=1}^\infty f_n\Big)=\sum_{n=1}^\infty \int_a^b f_n.
	\]

	\textbf{Termwise differentiation (sufficient condition).}
	Let $I=[a,b]$. If $f_n\in C^1(I)$, $f_n'\to g$ uniformly on $I$, and $(f_n(x_0))_n$ converges for some $x_0\in I$, then
	$f_n\to f$ uniformly on $I$, $f\in C^1(I)$, and $f'=g$.

	\textbf{Power series.}
	For $\sum_{n=0}^\infty a_n (x-x_0)^n$ with radius $R>0$:
	uniform convergence on each closed $[x_0-r,x_0+r]\subset (x_0-R,x_0+R)$;
	termwise integration/differentiation valid on $(x_0-R,x_0+R)$; the derivative series has radius $R$.

	\textbf{DiniĂ˘â‚¬â„˘s theorem (compact $X$).}
	If $X$ is compact, $f_n\in C(X)$, and $f_n\downarrow f\in C(X)$ (or $f_n\uparrow f$), then $f_n\to f$ uniformly.

	\textbf{Arzel\`a--Ascoli.}
	If $X$ is compact and $\mathcal F\subset C(X)$ is equicontinuous and pointwise bounded, then every sequence in $\mathcal F$ has a uniformly convergent subsequence with continuous limit.

	\textbf{Uniform Dirichlet test.}
	If $A_N(x)=\sum_{n=1}^N a_n(x)$ are uniformly bounded on $X$, and $b_n(x)$ is monotone in $n$ for each $x$ with $b_n\to0$ uniformly, then $\sum a_n(x)b_n(x)$ converges uniformly.

	\textbf{Uniform Abel test.}
	If $\sum a_n(x)$ converges uniformly on $X$ and $b_n(x)$ is uniformly bounded and monotone in $n$ for each $x$, then $\sum a_n(x)b_n(x)$ converges uniformly.


	\textbf{Mini-examples.}

		\par\noindent\textbullet\quad (Uniform limit) $f_n(x)=x^n$ on $[0,a]$, $0<a<1$: $f_n\downarrow 0$ and $f_n\to 0$ uniformly (Dini).
		\par\noindent\textbullet\quad (M-test) $\sum \frac{x^n}{n^2}$ on $[0,1]$: $|f_n|\le 1/n^2$, so uniform absolute convergence; integrals may be swapped with sum.
		\par\noindent\textbullet\quad (Alternating uniform) $\sum (-1)^n \frac{x^n}{n}$ on $[0,1]$: uniform (Leibniz), but not uniformly absolute.
		\par\noindent\textbullet\quad (Dirichlet) $\sum \frac{\sin(nx)}{n}$: uniform on $[\delta,2\pi-\delta]$ for any $\delta>0$.
		\par\noindent\textbullet\quad (Arzel\`a--Ascoli) $f_n(x)=\sin(nx)/n$ on $[0,2\pi]$: equicontinuous and bounded $\Rightarrow$ a uniformly convergent subsequence.

	\textbf{Gotchas.}
	Pointwise convergence does not preserve continuity or integrals;
	 uniform convergence does.

	Uniform absolute $\Rightarrow$ uniform, but not conversely.

	Local uniform convergence suffices for continuity on open domains.

	\par\medskip\noindent\textbf{Decision Tree for Convergence of Sequences and Series of Functions}\par

	\textbf{Series of functions $\sum f_n$ on $X$.}

		\par\noindent\textbullet\quad \textit{Uniform bound by a summable scalar?} \\
		If $|f_n(x)|\le M_n$ on $X$ and $\sum M_n<\infty$ $\Rightarrow$ \textbf{Weierstrass M-test}:
		uniform absolute convergence.

		\par\noindent\textbullet\quad \textit{Alternating in $n$?} $f_n=(-1)^n a_n$. \\
		If $a_n(x)\ge0$, nonincreasing in $n$ for each $x$, and $a_n\to0$ uniformly on $X$ $\Rightarrow$
		\textbf{Leibniz (uniform)}: uniform convergence (typically not uniformly absolute).

		\par\noindent\textbullet\quad \textit{Product form $a_n(x)b_n(x)$?} \\
		\textbf{Dirichlet (uniform):} if $A_N(x)=\sum_{n=1}^N a_n(x)$ are uniformly bounded on $X$ and
		$b_n(x)$ is monotone in $n$ with $b_n\to0$ uniformly, then $\sum a_n b_n$ converges uniformly. \\
		\textbf{Abel (uniform):} if $\sum a_n(x)$ converges uniformly on $X$ and $b_n(x)$ is uniformly bounded
		and monotone in $n$, then $\sum a_n b_n$ converges uniformly.

		\par\noindent\textbullet\quad \textit{Power series / radius present?} \\
		Determine radius $R$ via root/ratio pointwise. Convergence is uniform on every closed subinterval
		strictly inside the radius; termwise differentiation/integration valid in $(x_0-R,x_0+R)$.

		\par\noindent\textbullet\quad \textit{Spikes or singularities at isolated points?} \\
		Expect global uniform \emph{fails}. Prove \textbf{local uniform} convergence on neighborhoods avoiding singularities
		to deduce continuity on the punctured domain.

		\par\noindent\textbullet\quad \textit{No pattern? Use uniform Cauchy on compacta.} \\
		Show tail $\sup_{x\in K}|\sum_{n>N} f_n(x)|\to0$ for each compact $K\subset X$.

		\par\noindent\textbullet\quad \textit{Absolute vs conditional.} \\
		If $\sum \|f_n\|_\infty<\infty$ $\Rightarrow$ uniform absolute. Alternating/Dirichlet/Abel often give uniform but not absolute.

	\textbf{Sequences of functions $(f_n)$.}

		\par\noindent\textbullet\quad \textbf{Dini (compact $X$):} If $f_n\in C(X)$ and $f_n\downarrow f\in C(X)$ (or $\uparrow$), then $f_n\to f$ uniformly.
		\par\noindent\textbullet\quad \textbf{Arzel\`a--Ascoli:} On compact $X$, equicontinuous and pointwise bounded families have uniformly convergent subsequences.
		\par\noindent\textbullet\quad \textbf{Uniform Cauchy:} $\sup_{x\in X}|f_m(x)-f_n(x)|\to0$ $\Rightarrow$ uniform convergence.
		\par\noindent\textbullet\quad \textbf{Power-series tails:} Use M-test on tails to get uniform convergence on compacta.


	\textbf{Micro-examples.}

		\par\noindent\textbullet\quad (M-test) $\displaystyle f_n(x)=\frac{x^n}{n^2}$ on $[0,1]$:
		$|f_n|\le 1/n^2$, so uniform absolute convergence.
		\par\noindent\textbullet\quad (Leibniz) $\displaystyle f_n(x)=(-1)^n\frac{x^n}{n}$ on $[0,1]$:
		$a_n=x^n/n$ decreases in $n$, $a_n\to0$ uniformly $\Rightarrow$ uniform, not uniformly absolute.
		\par\noindent\textbullet\quad (Dirichlet) $\displaystyle \sum_{n=1}^\infty \frac{\sin(nx)}{n}$:
		uniform on $[\delta,2\pi-\delta]$ for any $\delta>0$; not uniform on all of $[0,2\pi]$.
		\par\noindent\textbullet\quad (Local uniform) $\displaystyle \sum_{n=1}^\infty (x-n)^{-2}$ on $\mathbb R\setminus\mathbb N$:
		not uniform globally; locally uniform $\Rightarrow$ continuous sum on the punctured domain.
		\par\noindent\textbullet\quad (Dini) $f_n(x)=x^n$ on $[0,a]$, $0<a<1$: $f_n\downarrow 0\in C$ $\Rightarrow$ uniform.


	\textbf{What uniform convergence buys you.}
	Uniform limit of continuous functions is continuous; integrals pass to the limit.
	For series: uniform convergence $\Rightarrow$ termwise integration; with extra hypotheses on derivatives,
	termwise differentiation on compact intervals.

	\par\medskip\noindent\textbf{Problem 16 — Implicit Function Theorem via a block map}\par

	\textbf{Setup.}
	Let $U\subset\mathbb{R}^{n+m}$ be open and $f:U\to\mathbb{R}^m$ be $C^1$.
	Write $(x,y)\in\mathbb{R}^n\times\mathbb{R}^m$ and assume $(x_0,y_0)\in U$ with
	\[
	f(x_0,y_0)=0
	\qquad\text{and}\qquad
	J_y f\big|_{(x_0,y_0)}:=\det\!\Big[\tfrac{\partial f^i}{\partial y^j}\Big]_{i,j=1}^m\neq 0.
	\]

		\par\noindent \textbf{(a)}\quad \textbf{Local invertibility of $F$.}
		Define $F(x,y)=(x,f(x,y))$. Its Jacobian at $(x_0,y_0)$ is
		\[
		DF\big|_{(x_0,y_0)}=
		\begin{pmatrix}
			I_n & 0\\
			D_x f\big|_{(x_0,y_0)} & D_y f\big|_{(x_0,y_0)}
		\end{pmatrix}.
		\]
		This block–triangular matrix has
		$\det DF=\det(I_n)\,\det(D_y f)\neq0$,
		so by the inverse function theorem $F$ is a local $C^1$ diffeomorphism
		near $(x_0,y_0)$.

		\medskip

		\par\noindent \textbf{(b)}\quad \textbf{A property of the inverse $G$.}
		Let $G=(G^1,\dots,G^{n+m})$ be the local inverse of $F$ on a neighborhood
		$V\ni (x_0,0)$. For any $(X,0)\in V$,
		\[
		F\big(G(X,0)\big)=(X,0)
		\quad\Longrightarrow\quad
		\begin{cases}
			(G^1,\dots,G^n)(X,0)=X,\\[2pt]
			\displaystyle f\!\big(X,\;G^{n+1}(X,0),\dots,G^{n+m}(X,0)\big)=0.
		\end{cases}
		\]

		\medskip

		\par\noindent \textbf{(c)}\quad \textbf{Existence and uniqueness of the implicit function.}
		Define, for $X$ near $x_0$,
		\[
		g(X):=\big(G^{n+1}(X,0),\dots,G^{n+m}(X,0)\big).
		\]
		Then $f(X,g(X))=0$ and $g(x_0)=y_0$.
		If $f(X,y)=0$ with $X$ near $x_0$, $y$ near $y_0$, then
		$F(X,y)=(X,0)$, so $(X,y)=G(X,0)$ and hence $y=g(X)$ (uniqueness).

		\medskip

		\par\noindent \textbf{(d)}\quad \textbf{Differentiability and the formula for $Dg$.}
		Since $G$ is $C^1$, so is $g$. Differentiating $f(x,g(x))\equiv0$ gives
		\[
		D_x f(x,g(x)) \;+\; D_y f(x,g(x))\,Dg(x) \;=\; 0,
		\]
		and because $D_y f$ stays invertible nearby,
		\[
		\boxed{\; Dg(x) \;=\; -\big[D_y f(x,g(x))\big]^{-1} \, D_x f(x,g(x)) \; }.
		\]

		\medskip

		\par\noindent \textbf{(e)}\quad \textbf{Application: the folium $x^3+y^3-3xy=0$.}
		Let $f(x,y)=x^3+y^3-3xy$. Then
		\[
		\frac{\partial f}{\partial y}=3y^2-3x, \qquad
		\frac{\partial f}{\partial x}=3x^2-3y.
		\]
		On the level set $C=\{f=0\}$ the IFT yields a local graph $y=g(x)$ at points
		with $\frac{\partial f}{\partial y}\neq0$.
		Solving on $C$ the system $\{f=0,\ \partial f/\partial y=0\}$ gives
		$x=y^2$ and $y^6-2y^3=0$, so $(x,y)=(0,0)$ or $(2^{2/3},2^{1/3})$.
		Hence $C$ is locally a graph $y=g(x)$ away from small neighborhoods
		of these two exceptional points.

	\noindent
	Here is a visualization of the \emph{folium curve}
	\[
	x^{3}+y^{3}-3xy=0,
	\]
	showing the \textbf{exceptional points} $(0,0)$ and $(2^{2/3},\,2^{1/3})$ where IFT fails for
	$y=g(x)$. Indeed,
	\[
	\frac{\partial f}{\partial y}=3y^{2}-3x=0 \iff x=y^{2},
	\qquad
	f(x,y)=0 \iff y^{6}-2y^{3}=0 \iff y=0 \ \text{or}\ y^{3}=2.
	\]
	Everywhere else on the curve, $\partial f/\partial y\neq0$ and the set is locally a graph $y=g(x)$.

	\textbf{IFT (finite-dimensional $C^1$).}
	Let $U\subset\mathbb{R}^{n+m}$ be open and $f:U\to\mathbb{R}^m$ be $C^1$.
	Write $(x,y)\in\mathbb{R}^n\times\mathbb{R}^m$. Suppose $(x_0,y_0)\in U$ with
	\[
	f(x_0,y_0)=0,\qquad \det D_y f(x_0,y_0)\neq 0.
	\]
	Then there exist neighborhoods $W'\ni x_0$, $W''\ni y_0$ and a unique map $g:W'\to W''$,
	of class $C^1$, such that $g(x_0)=y_0$ and $f(x,g(x))=0$ on $W'$. Moreover
	\[
	Dg(x)= -\big[D_y f(x,g(x))\big]^{-1} D_x f(x,g(x)).
	\]
	If $f\in C^k$ (resp.\ real-analytic) then $g\in C^k$ (resp.\ analytic).

	\medskip
	\textbf{Geometric picture.}
	Near $(x_0,y_0)$, the zero set $f^{-1}(0)$ is a smooth $n$-dimensional surface; in suitable
	coordinates it is the graph $y=g(x)$.

	\medskip
	\textbf{Proof sketch.}
	Apply the inverse function theorem to $F(x,y)=(x,f(x,y))$:
	\[
	DF\big|_{(x_0,y_0)}=
	\begin{pmatrix}
		I_n & 0\\
		D_x f & D_y f
	\end{pmatrix}_{(x_0,y_0)}
	\]
	is invertible by hypothesis (block-triangular). Then $F$ has a local inverse $G$ and
	$g(x):=(G^{n+1},\dots,G^{n+m})(x,0)$.


	\textbf{Examples.}

	\emph{1) Circle.} $f(x,y)=x^2+y^2-1$. At $(0,1)$, $\partial f/\partial y=2\ne0$,
	so $y=g(x)$ exists locally (upper semicircle). At $(1,0)$ we cannot solve for $y$,
	but can solve for $x=h(y)$ since $\partial f/\partial x=2\ne0$.

	\emph{2) Parabola: solve for the right variable.}
	$f(x,y)=y^2-x$ at $(0,0)$ has $\partial f/\partial y=0$ (no $y=g(x)$),
	but $\partial f/\partial x=-1\ne0$; hence $x=h(y)=y^2$.

	\emph{3) Transcendental (Lambert $W$).}
	$f(x,y)=y e^y - x$. At $(0,0)$, $\partial f/\partial y=1$, so $y=g(x)=W(x)$ exists,
	analytic near $0$, with $g'(x)=\big(e^{g(x)}(1+g(x))\big)^{-1}$.

	\emph{4) Constraint manifolds.}
	If $\operatorname{rank} Df = m$ on $f^{-1}(0)$, the level set is an $n$-dimensional submanifold,
	locally a graph by IFT.


	\textbf{Failures / counterexamples.}

	\emph{(i) Cusp:} $f(x,y)=y^3-x^2$ at $(0,0)$ has $\partial f/\partial y=0$.
	The zero set has a cusp; it is not a graph $y=g(x)$ nor $x=h(y)$ there.

	\emph{(ii) Two branches:} $f(x,y)=y^2-x$ at $(0,0)$: cannot solve for $y$ (two values
	$\pm\sqrt{x}$), but can solve for $x$ as above. The condition must be on the variable you
	solve for.

	\emph{(iii) Lack of smoothness:} $f(x,y)=|y|-x$ at $(0,0)$ is not $C^1$ in $y$.
	The zero set is $y=\pm x$, not a single branch; IFT does not apply.

	\medskip
	\textbf{Banach-space version.}
	If $E,F$ are Banach spaces, $f:E\times F\to F$ is $C^1$ near $(x_0,y_0)$,
	$f(x_0,y_0)=0$, and $D_y f(x_0,y_0):F\to F$ is an isomorphism, then there exists a unique
	$C^1$ map $g$ near $x_0$ with $f(x,g(x))=0$ and
	$Dg(x)= -\big[D_y f(x,g(x))\big]^{-1} D_x f(x,g(x))$.

	Let $f(x,y)=x^2+y^2-1$. Then $\partial f/\partial x=2x$, $\partial f/\partial y=2y$.

	Since $\partial f/\partial y(0,1)=2\neq 0$, the IFT gives a unique $C^\infty$ function
	$g$ with $g(0)=1$ and $f(x,g(x))\equiv 0$ for $|x|$ small (upper semicircle).
	The IFT derivative formula (with $n=m=1$) yields
	\[
	g'(x)= -\frac{\partial f/\partial x}{\partial f/\partial y}\Big|_{(x,g(x))}
	= -\frac{2x}{2\,g(x)} = -\frac{x}{g(x)}.
	\]
	Hence $g'(0)=0$. Using the exact branch $g(x)=\sqrt{1-x^2}$ gives
	$g''(0)=-1$.

	Here $\partial f/\partial y(1,0)=0$ so we cannot solve $y=g(x)$,
	but $\partial f/\partial x(1,0)=2\neq0$ gives a unique $C^\infty$ function $x=h(y)$ with
	$h(0)=1$ and $f(h(y),y)\equiv 0$ (right semicircle).
	The derivative formula (solving for $x$) gives
	\[
	h'(y) = -\,\frac{\partial f/\partial y}{\partial f/\partial x}\Big|_{(h(y),y)}
	= -\,\frac{2y}{2\,h(y)} = -\frac{y}{h(y)},
	\]
	so $h'(0)=0$. With the exact branch $h(y)=\sqrt{1-y^2}$, one gets $h''(0)=-1$.

	Let $f(x,y)=y^2-x$. Then $\partial f/\partial x=-1$, $\partial f/\partial y=2y$.

	Since $\partial f/\partial y(0,0)=0$, we cannot solve $y=g(x)$ there (two values $\pm\sqrt{x}$ for $x>0$),
	but $\partial f/\partial x(0,0)=-1\neq0$ gives a unique $C^\infty$ function $x=h(y)$ with $h(0)=0$.
	The IFT formula (solving for $x$) yields
	\[
	h'(y) = -\,\frac{\partial f/\partial y}{\partial f/\partial x}\Big|_{(h(y),y)}
	= -\,\frac{2y}{-1} = 2y,
	\]
	so $h'(0)=0$ and $h''(y)=2$. In fact $h(y)=y^2$ exactly.

	If $y_0\neq 0$, then $\partial f/\partial y(x_0,y_0)=2y_0\neq 0$, so there is a unique branch
	$y=g(x)$ through $(x_0,y_0)$ with
	\[
	g'(x)= -\frac{\partial f/\partial x}{\partial f/\partial y}\Big|_{(x,g(x))}
	= \frac{1}{2g(x)}.
	\]
	These are the two smooth branches $y=\pm\sqrt{x}$ away from the vertex.

	We have $f_x=-2x$, $f_y=3y^2$, so $f_x(0,0)=f_y(0,0)=0$. The IFT hypothesis fails for both
	solving $y=g(x)$ and $x=h(y)$ at $(0,0)$.

	The zero set is $y^3=x^2$, i.e.\ $y=|x|^{2/3}\ (\ge0)$, a continuous but \emph{non-differentiable}
	graph over $x$ at $0$.
	Implicit differentiation gives $3y^2\,y'-2x=0$, so along the curve
	\[
	y'=\frac{2x}{3y^2}=\frac{2x}{3|x|^{4/3}}=\frac{2}{3}\,\mathrm{sgn}(x)\,|x|^{-1/3}\xrightarrow[x\to 0]{}\pm\infty,
	\]
	i.e.\ a vertical tangent and no $C^1$ graph $y=g(x)$ through $(0,0)$.
	Solving for $x$ yields two branches $x=\pm y^{3/2}$ for $y\ge0$; thus there is no single-valued
	implicit function $x=h(y)$ on a neighborhood of $(0,0)$. The zero set has a \emph{cusp}.

	Here $f_x=-1$, $f_y=2y$, so $f_y(0,0)=0$ (cannot solve $y=g(x)$: two values $y=\pm\sqrt{x}$ for $x>0$),
	but $f_x(0,0)=-1\neq0$ so the IFT applies to solve $x=h(y)$.
	Indeed $x=h(y)=y^2$ with
	\[
	h'(y)=-\frac{f_y}{f_x}\Big|_{(h(y),y)}=-\frac{2y}{-1}=2y,\qquad h''(y)=2.
	\]
	Thus the correct variable to solve for is dictated by which partial derivative is nonzero.
```

## CP-II-0157

- chapter line: 14473

```tex
\label{prob:cp-ii-0157}
\par\noindent\textbullet\quad \textbf{$L^p$ norms.} For $1\le p<\infty$, the map $f\mapsto\|f\|_{L^p}$ is weakly l.s.c.:
		if $f_n\rightharpoonup f$ in $L^p$, then $\|f\|_{p}\le \liminf_n \|f_n\|_{p}$.
```

## CP-II-0158

- chapter line: 14479

```tex
\label{prob:cp-ii-0158}
(Indicator; threshold $s<\tfrac12$ in 1D).

For $f=\mathbf 1_{(0,1)}$ one has
\(
\widehat f(\xi)=e^{-i\xi/2}\,\frac{2\sin(\xi/2)}{\xi}
\),
so $|\widehat f(\xi)|^2\sim 2/\xi^2$ as $|\xi|\to\infty$. Therefore
\[
\|f\|_{H^s(\mathbb R)}^2 \sim \int_{\mathbb R} (1+\xi^2)^s \frac{1}{\xi^2}\,d\xi<\infty
\iff s<\tfrac12.
\]
Equivalently, for $0<s<1$, the Gagliardo seminorm
$\iint \frac{|f(x)-f(y)|^2}{|x-y|^{1+2s}}dx\,dy$
converges iff $s<\tfrac12$.
```

## CP-II-0161

- chapter line: 14522

```tex
\label{prob:cp-ii-0161}
Gaussian smoothing.

Let
\[
g_\varepsilon(y)
= \frac{1}{\sqrt{\pi}\,\varepsilon}\,e^{-y^2/\varepsilon^2}.
\]
Then $f*g_\varepsilon$ is the \emph{Gaussian--blurred} version of $f$.

\medskip
\noindent$\Rightarrow$ \emph{Effect:} removes noise, increases
differentiability.

\bigskip\hrule\bigskip
```

## CP-II-0164

- chapter line: 14540

```tex
\label{prob:cp-ii-0164}
\par\noindent\textbullet\quad Tonelli--Fubini can be verified directly;
```

## CP-II-0165

- chapter line: 14545

```tex
\label{prob:cp-ii-0165}
\par\noindent\textbullet\quad \textbf{Singular (continuous):}
		The Cantor probability measure $\gamma$ is supported on the middle--third Cantor set $C$ with $m(C)=0$,
		hence $\gamma\perp m$ and has no atoms.
```

## CP-II-0167

- chapter line: 14552

```tex
\label{prob:cp-ii-0167}
— A Schauder basis for $C([-1,1])$ from hat functions

Using the result of Question~5, prove that there exists a sequence
$\{\phi_n\}_{n\ge0}\subset C([-1,1])$ such that for every $f\in C([-1,1])$ there exists a
\emph{unique} series $\sum_{n=0}^{\infty} a_n \phi_n$ which converges uniformly to $f$.

We recall the hat (tent) framework from Question~5 and collect the identities used in the proof.

	\par\noindent\textbullet\quad \textbf{Hat functions on a uniform grid.}
	For $n\in\mathbb{N}$ and $r\in\mathbb{Z}$ define
	\[
	\Delta_{n,r}(x)=\max\!\{0,\;1-n\lvert x-r/n\rvert\},\qquad x\in[-1,1].
	\]
	Then $\Delta_{n,r}$ is supported on $[(r-1)/n,(r+1)/n]$, satisfies
	$\Delta_{n,r}(r/n)=1$, is linear with slopes $\pm n$ on its support, and for each
	$x\in[k/n,(k+1)/n]$ one has
	\[
	\Delta_{n,k}(x)+\Delta_{n,k+1}(x)=1,\qquad
	\Delta_{n,m}(x)=0\ \text{for } m\notin\{k,k+1\}.
	\]
	Consequently, for any $f\in C([-1,1])$ the piecewise–linear interpolant
	\[
	f_n(x)=\sum_{m=-n}^{n} f\!\left(\frac{m}{n}\right)\Delta_{n,m}(x)
	\]
	is linear on each $[k/n,(k+1)/n]$, interpolates the data $f_n(m/n)=f(m/n)$, and
	satisfies the uniform error bound
	\[
	\|f-f_n\|_\infty\le \omega_f\!\left(\frac{1}{n}\right),
	\]
	where $\omega_f(\delta)=\sup_{|x-y|\le \delta}|f(x)-f(y)|$ is the modulus of continuity.

	\par\noindent\textbullet\quad \textbf{Dyadic refinement and midpoint hats (Faber–Schauder atoms).}
	On $[0,1]$ (with $u=\frac{x+1}{2}$) define the dyadic midpoint hats
	\[
	h_{k,m}(u)=\max\!\Big\{0,\;1-2^{k+1}\Big|u-\frac{2m-1}{2^{k+1}}\Big|\Big\},
	\qquad k\ge 0,\ m=1,\dots,2^{k}.
	\]
	Each $h_{k,m}$ is the tent of height $1$ with support
	$\big[(m-1)/2^{k},(m+1)/2^{k}\big]$ and peak at $(2m-1)/2^{k+1}$.
	Transport to $[-1,1]$ via $\phi_{k,m}(x)=h_{k,m}\big(\frac{x+1}{2}\big)$ and add two
	low-order functions $\phi_0(x)=1$, $\phi_1(x)=\frac{x+1}{2}$.

	\par\noindent\textbullet\quad \textbf{Telescoping of piecewise–linear interpolants.}
	Let $g(u)=f(2u-1)$ and let $g_{2^K}$ be the piecewise–linear interpolant on the dyadic
	grid $\{j/2^K\}_{j=0}^{2^K}$. Then
	\[
	g_{2^{K}}(u)
	= g_{2^{0}}(u)
	+ \sum_{k=0}^{K-1}\big(g_{2^{k+1}}(u)-g_{2^{k}}(u)\big),
	\]
	and each difference admits the representation
	\[
	g_{2^{k+1}}(u)-g_{2^{k}}(u)
	= \sum_{m=1}^{2^{k}} d_{k,m}\,h_{k,m}(u),
	\]
	with \emph{detail coefficients} (midpoint second differences)
	\[
	d_{k,m}
	= g\!\Big(\frac{2m-1}{2^{k+1}}\Big)
	-\frac{1}{2}\Bigg[
	g\!\Big(\frac{m-1}{2^{k}}\Big)
	+ g\!\Big(\frac{m}{2^{k}}\Big)\Bigg].
	\]
	Hence, for $K\ge1$,
	\[
	g_{2^{K}}(u) = a_0 + a_1 u + \sum_{k=0}^{K-1}\sum_{m=1}^{2^{k}} d_{k,m}\,h_{k,m}(u),
	\qquad a_0=g(0),\ \ a_1=g(1)-g(0).
	\]
	Pulling back to $[-1,1]$ yields
	\[
	f_{2^{K}}(x)= a_0\,\phi_0(x)+a_1\,\phi_1(x)
	+ \sum_{k=0}^{K-1}\sum_{m=1}^{2^{k}} d_{k,m}\,\phi_{k,m}(x).
	\]

	\par\noindent\textbullet\quad \textbf{Uniform convergence and uniqueness.}
	By the bound in (a), $f_{2^{K}}\to f$ uniformly as $K\to\infty$, hence
	\[
	f(x)= a_0\,\phi_0(x)+a_1\,\phi_1(x)
	+ \sum_{k=0}^{\infty}\sum_{m=1}^{2^{k}} d_{k,m}\,\phi_{k,m}(x)
	\]
	is a uniformly convergent series in $\{\phi_n\}\subset C([-1,1])$.
	Uniqueness of the coefficients follows from the triangular structure with respect to
	levels: if $\sum a_n\phi_n\equiv 0$, then $a_0=a_1=0$ (evaluation at the endpoints),
	and at each level $k$ the functions $\{\phi_{k,m}\}_m$ have disjoint supports and are
	the only basis elements nonzero at their midpoints; thus all detail coefficients vanish
	by induction.

\noindent\rule{\textwidth}{0.4pt}

Work on $[0,1]$ with $u\in[0,1]$ and define
\[
\psi_0(u)=1,\quad \psi_1(u)=u,\qquad
h_{k,m}(u)=\max\!\Big\{0,\;1-2^{k+1}\Big|u-\frac{2m-1}{2^{k+1}}\Big|\Big\}
\]
for $k\ge0$ and $m=1,\dots,2^k$.
Transport to $[-1,1]$ by $u=(x+1)/2$:
\[
\phi_0(x)=1,\qquad \phi_1(x)=\tfrac{x+1}{2},\qquad
\phi_{k,m}(x)=h_{k,m}\!\Big(\tfrac{x+1}{2}\Big).
\]
Enumerate $\{\phi_n\}$ as $(\phi_0,\phi_1,\phi_{0,1},\phi_{1,1},\phi_{1,2},\ldots)$.

Given $f\in C([-1,1])$, set $g(u)=f(2u-1)$. Define
\[
a_0=g(0),\qquad a_1=g(1)-g(0),
\]
and for $k\ge0$, $m=1,\dots,2^k$,
\[
d_{k,m}=g\!\Big(\frac{2m-1}{2^{k+1}}\Big)
-\frac12\Bigg[g\!\Big(\frac{m-1}{2^k}\Big)+g\!\Big(\frac{m}{2^k}\Big)\Bigg].
\]
Let $g_{2^K}$ be the piecewise–linear interpolant on the dyadic grid $\{j/2^K\}$.
Then the standard decomposition (telescoping across levels) gives
\[
g_{2^K}(u)=a_0+a_1 u+\sum_{k=0}^{K-1}\sum_{m=1}^{2^k} d_{k,m}\,h_{k,m}(u).
\]
Hence, on $[-1,1]$,
\[
f_{2^K}(x)=a_0\,\phi_0(x)+a_1\,\phi_1(x)
+\sum_{k=0}^{K-1}\sum_{m=1}^{2^k} d_{k,m}\,\phi_{k,m}(x).
\]

By Question~5, $f_{2^K}\to f$ uniformly on $[-1,1]$. Letting $K\to\infty$ yields the uniformly
convergent expansion
\[
f(x)=a_0\,\phi_0(x)+a_1\,\phi_1(x)
+\sum_{k=0}^{\infty}\sum_{m=1}^{2^k} d_{k,m}\,\phi_{k,m}(x),
\]
i.e. a series $\sum_{n\ge0} a_n\phi_n$ converging uniformly to $f$.

Suppose $\sum_{n\ge0} a_n\phi_n\equiv 0$. Evaluating at $x=-1$ and $x=1$ gives
$a_0=0$ and $a_1=0$. Proceeding by levels, at level $k$ the functions
$\{\phi_{k,m}\}_m$ have disjoint supports and each is the only basis function nonzero at
its own midpoint; hence each coefficient must be zero. By induction, all coefficients vanish,
so the representation is unique.

	\par\noindent\textbullet\quad $f(x)=ax+b$: all detail coefficients $d_{k,m}$ vanish; only the low–order terms
	$\phi_0,\phi_1$ remain.
	\par\noindent\textbullet\quad $f(x)=x^2$: $d_{k,m}=\frac14\,2^{-2k}$ for all $m$, giving a rapidly convergent sum of
	midpoint hats across levels.

The system $\{\phi_n\}$ is a Schauder basis for $C([-1,1])$ (the Faber–Schauder basis):
every continuous function admits a unique uniformly convergent series in these functions.
```

## CP-II-0170

- chapter line: 14713

```tex
\label{prob:cp-ii-0170}
{Polynomials $p_n$ with $p_n(0)=1$ and $p_n(z)\to0$ for $z\neq0$}{poly-vanish-off-zero}
	Does there exist a sequence of complex polynomials $(p_n)$ such that
	$p_n(0)=1$ for all $n$ and $p_n(z)\to 0$ for each $z\in\mathbb C\setminus\{0\}$?
```

## CP-II-0173

- chapter line: 14720

```tex
\label{prob:cp-ii-0173}
\par\noindent\textbullet\quad \textbf{Bounded:} yes, $|\sin|\le1$. \textbf{Not uniformly continuous.}
	Let $a_k=\sqrt{k\pi}$, $b_k=\sqrt{k\pi+\pi/2}$. Then $|a_k-b_k|\to0$ but
	$|f(a_k)-f(b_k)|=1$.
```

## CP-II-0175

- chapter line: 14727

```tex
\label{prob:cp-ii-0175}
\par\noindent\textbullet\quad \textbf{Not Lipschitz equivalent to $\|\cdot\|_{\infty}$.}
	Always $\|f\|_{1}\le \|f\|_{\infty}$. A reverse uniform bound
	$c\|f\|_{\infty}\le \|f\|_{1}$ fails: take continuous Ă˘â‚¬Ĺ›spikesĂ˘â‚¬ĹĄ
	\[
	f_n(x)=\begin{cases}
		1-\dfrac{|x-a_n|}{\ell_n}, & |x-a_n|\le \ell_n,\\[4pt]
		0, & \text{otherwise},
	\end{cases}
	\quad a_n\to 0,\ \ell_n\downarrow 0.
	\]
	Then $\|f_n\|_{\infty}=1$ but $\|f_n\|_{1}=\int_{a_n-\ell_n}^{a_n+\ell_n}\!\!\big(1-\frac{|x-a_n|}{\ell_n}\big)\,dx
	=\ell_n\to 0$. No $c>0$ works, so the norms are not Lipschitz equivalent.
```

## CP-II-0176

- chapter line: 14743

```tex
\label{prob:cp-ii-0176}
\par\noindent\textbullet\quad The subspace topology on \(X\) consists of all sets of the form \((a,b)\cap(0,1]\).

	For example:
```

## CP-II-0178

- chapter line: 14770

```tex
\label{prob:cp-ii-0178}
\par\noindent\textbullet\quad If $T=\delta_0$, then
	\[
	(\delta_0*\phi)(x)
	= \langle\delta_0,\phi(x-\cdot)\rangle
	= \phi(x-0) = \phi(x).
	\]
```

## CP-II-0179

- chapter line: 14780

```tex
\label{prob:cp-ii-0179}
\par\noindent\textbullet\quad Dyadic intervals: $I_{n,k}=[k2^{-n},(k+1)2^{-n})$.
```

## CP-II-0186

- chapter line: 14922

```tex
\label{prob:cp-ii-0186}
\par\noindent\textbullet\quad Integrating over $\mathbb{R}^n$ gives
	\[
	\int_{\mathbb{R}^n} |f(x)g(x)|\,dx
	\;\le\;
	\frac{1}{p}\int |f|^p + \frac{1}{q}\int |g|^q.
	\]
```

## CP-II-0188

- chapter line: 14989

```tex
\label{prob:cp-ii-0188}
Dirac mass $\delta_0$.

The Dirac distribution acts by evaluation:
\[
\langle\delta_0,\varphi\rangle = \varphi(0).
\]
The following figure shows a test function $\varphi$ together with the
highlighted value $\varphi(0)$.
```

## CP-II-0189

- chapter line: 15001

```tex
\label{prob:cp-ii-0189}
— Approximations of a Riemann–Integrable Function on $[0,1]$

Let $f$ be bounded and Riemann integrable on $[0,1]$.

	\par\noindent\textbullet\quad \textbf{No.} A uniform limit of continuous functions is continuous; a Riemann–integrable $f$ can be discontinuous.
	For example, $f=\mathbf 1_C$ (indicator of the Cantor set) is Riemann integrable with $\int f=0$ but is not continuous on $C$.
	\par\noindent\textbullet\quad \textbf{Yes.} Since $f\in\mathcal R[0,1]$, upper/lower sums approximate $f$ in $L^1$. Step functions are $L^1$–approximable by continuous functions (smooth their jumps in small neighborhoods). Hence there exist continuous $f_n$ with $\int_0^1|f_n-f|\to0$.
	\par\noindent\textbullet\quad \textbf{Yes.} From (b) approximate $f$ in $L^1$ by a continuous $g$. By Weierstrass, there exist polynomials $p_n$ with $\|p_n-g\|_\infty\to0$, so $\int_0^1|p_n-f|\le\|p_n-g\|_\infty+\int_0^1|g-f|\to0$.

\bigskip
```

## CP-II-0192

- chapter line: 15015

```tex
\label{prob:cp-ii-0192}
Convolution with Dirac delta.

\[
\delta_a * \phi = \phi(\cdot - a).
\]
```

## CP-II-0194

- chapter line: 15041

```tex
\label{prob:cp-ii-0194}
\par\noindent\textbullet\quad \textbf{Failure of convergence of means.}
		In $L^{p}[0,1]$, $f_j=(-1)^j$. Then $\int_{[0,1]} f_j$ does not converge, hence no weak limit exists.
```

## CP-II-0195

- chapter line: 15047

```tex
\label{prob:cp-ii-0195}
\par\noindent\textbullet\quad If \(\nu=f\,m+\sum_{k} a_k\delta_{x_k}\) with \(f\in L^1(m)\), then
		\(\nu_a=f\,m\) and \(\nu_s=\sum_{k} a_k\delta_{x_k}\).
```

## CP-II-0196

- chapter line: 15053

```tex
\label{prob:cp-ii-0196}
Convolution smooths distributions.

Convolving the principal value or $\delta'$ with a mollifier produces
smooth approximations.
```

## CP-II-0199

- chapter line: 15061

```tex
\label{prob:cp-ii-0199}
\par\noindent\textbullet\quad Counting measure on a discrete space (with the discrete topology) is a Radon Borel measure.
```

## CP-II-0201

- chapter line: 15083

```tex
\label{prob:cp-ii-0201}
For $[2;1,2,2,1,3]$ the convergents are
	\[
	\begin{array}{c|c|c|c|c}
		k & a_k & p_k & q_k & p_k/q_k\\ \hline
		0 & 2 & 2  & 1  & 2 \\
		1 & 1 & 3  & 1  & 3 \\
		2 & 2 & 8  & 3  & 8/3 \\
		3 & 2 & 19 & 7  & 19/7 \\
		4 & 1 & 27 & 10 & 27/10 \\
		5 & 3 & 100& 37 & \boxed{100/37}
	\end{array}
	\]
	(as expected for a rational, the expansion terminates at $k=5$).
```

## CP-II-0204

- chapter line: 15100

```tex
\label{prob:cp-ii-0204}
If $E\subset X$ has finite measure and
	$f=t^{-1/p}\mathbf{1}_E$ with $t=\mu(E)$, then
	\[
	\mu(\{|f|>\lambda\})=
	\begin{cases}
		t, & 0<\lambda<t^{-1/p},\\[4pt]
		0, & \lambda\ge t^{-1/p}.
	\end{cases}
	\]
	Hence
	\[
	\|f\|_{p,\infty}
	=\sup_{\lambda<t^{-1/p}} \lambda\, t^{1/p}=1.
	\]
```

## CP-II-0205

- chapter line: 15118

```tex
\label{prob:cp-ii-0205}
\begin{lemma}[Mollifiers in $\mathcal{S}'(\mathbb{R}^n)$]
	Let $(\eta_\varepsilon)_{\varepsilon>0}\subset\mathcal{S}(\mathbb{R}^n)$
	be a Schwartz approximate identity (e.g.\ Gaussian mollifiers), and let
	$U\in\mathcal{S}'(\mathbb{R}^n)$ be a tempered distribution. Define
	\[
	\langle \eta_\varepsilon * U, \psi\rangle
	:= \big\langle U, \check{\eta}_\varepsilon * \psi \big\rangle,
	\qquad \psi\in\mathcal{S}(\mathbb{R}^n),
	\]
	with $\check{\eta}_\varepsilon(x):=\eta_\varepsilon(-x)$. Then
	$\eta_\varepsilon * U\in\mathcal{S}(\mathbb{R}^n)$ for each
	$\varepsilon>0$, and
	\[
	\eta_\varepsilon * U \longrightarrow U
	\qquad\text{in }\mathcal{S}'(\mathbb{R}^n)\text{ as }\varepsilon\to0.
	\]
\end{lemma}
```

## CP-II-0207

- chapter line: 15166

```tex
\label{prob:cp-ii-0207}
Let $f(t)=\sin(2\pi t)+0.2t$ and $f_n(t)=f(t)+\frac{1}{n}\cos(6\pi t)$ on $[0,1]$.
	Then $\sup|f_n-f|\le 1/n$, so $f_n\to f$ uniformly and $f$ is bounded with
	$\sup|f|\le 1.2$. Taking $M=2.2$, for $m=3$,
	\[
	\sup|f_n^3-f^3|\le 3M^2\,\sup|f_n-f|\le \frac{14.52}{n}\to0.
	\]
	Thus $f_n^3\to f^3$ uniformly; the same argument works for any $m$.
```

## CP-II-0208

- chapter line: 15177

```tex
\label{prob:cp-ii-0208}
\par\noindent (c)\quad Deduce that $\{\psi_{n,k}\}$ is an orthonormal basis for $L^2(\mathbb{R})$.

 \par\noindent\textbullet\quad sep3pt
```

## CP-II-0209

- chapter line: 15184

```tex
\label{prob:cp-ii-0209}
\par\noindent\textbullet\quad $\phi\ge0$,
```

## CP-II-0210

- chapter line: 15189

```tex
\label{prob:cp-ii-0210}
{Uncountably many transcendental numbers via factorial-base decimals}-{uncountably-many-trans}
	Consider the set
	\[
	S\;:=\;\Bigl\{\,x_{\mathbf b}=\sum_{n=0}^{\infty}\frac{b_n}{10^{\,n!}} \;\Big|\; b_n\in\{1,2\}\ \text{for all }n\Bigr\}.
	\]
	Show that $S$ is uncountable and every $x_{\mathbf b}\in S$ is transcendental.
```

## CP-II-0211

- chapter line: 15199

```tex
\label{prob:cp-ii-0211}
{Irrationality and algebraicity}{irr-alg}

		\par\noindent\textbullet\quad \textbf{Irrational sums/powers.}

			\par\noindent\textbullet\quad $(\sqrt3+\sqrt5)\notin\mathbb Q$. If $\sqrt3+\sqrt5=r\in\mathbb Q$, then
			$r^2=8+2\sqrt{15}$, hence $\sqrt{15}=(r^2-8)/2\in\mathbb Q$, impossible.
			\par\noindent\textbullet\quad $e^2\notin\mathbb Q$. Suppose $e^2=a/b\in\mathbb Q$. For $N\ge\max\{2,b\}$,
			both $N!e^2$ and $N!\sum_{n=0}^{N}\frac{2^n}{n!}$ are integers, but
			\[
			0<N!\Bigl(e^2-\sum_{n=0}^{N}\frac{2^n}{n!}\Bigr)
			=\sum_{n=N+1}^{\infty}\frac{2^n N!}{n!}
			<\sum_{k=1}^{\infty}\Bigl(\frac{2}{N+1}\Bigr)^k<1,
			\]
			a contradiction.

		\par\noindent\textbullet\quad \textbf{Algebraic numbers and coefficients.}

			\par\noindent\textbullet\quad A real $\alpha$ is algebraic iff it is a zero of some nonzero polynomial
			with rational coefficients. ($\Leftarrow$) Clear after clearing denominators.
			($\Rightarrow$) Integers are rationals.
			\par\noindent\textbullet\quad \emph{False} that rational coefficients are forced. Example:
			$(x-\sqrt2)(x-\sqrt3)=x^2-(\sqrt2+\sqrt3)x+\sqrt6$. The roots are algebraic,
			but the coefficients are not rational.
```

## CP-II-0213

- chapter line: 15226

```tex
\label{prob:cp-ii-0213}
Find $A^\circ$, $\overline{A}$ and $\partial A$.

\renewcommand\labelenumi{(\alph{enumi})}
\par\noindent\textbullet\quad $A=\mathbb{R}^n$: $A^\circ=\mathbb{R}^n$, $\overline{A}=\mathbb{R}^n$, $\partial A=\varnothing$.
\par\noindent\textbullet\quad $A=\{0\}$: $A^\circ=\varnothing$, $\overline{A}=\{0\}$, $\partial A=\{0\}$.
\par\noindent\textbullet\quad $A=\{x:x^1\ge 0\}$: $A^\circ=\{x:x^1>0\}$, $\overline{A}=A$, $\partial A=\{x:x^1=0\}$.
\par\noindent\textbullet\quad $A=\{x:x^i\in[0,1]\ \forall i\}$: $A^\circ=\{x:x^i\in(0,1)\ \forall i\}$, $\overline{A}=A$, $\partial A=A\setminus A^\circ$.
\par\noindent\textbullet\quad $A=\{x:x^i\in\mathbb{Q}\ \forall i\}$: $A^\circ=\varnothing$, $\overline{A}=\mathbb{R}^n$, $\partial A=\mathbb{R}^n$.
```

## CP-II-0214

- chapter line: 15238

```tex
\label{prob:cp-ii-0214}
(Gaussian in all $H^s$).

Let $g(x)=e^{-|x|^2/2}$ on $\mathbb R^n$. Then
$\widehat g(\xi)=(2\pi)^{n/2}e^{-|\xi|^2/2}$ and
\[
\|g\|_{H^s}^2=(2\pi)^n\!\int_{\mathbb R^n}(1+|\xi|^2)^s e^{-|\xi|^2}\,d\xi<\infty
\quad\forall s\in\mathbb R.
\]
Hence $g\in H^s(\mathbb R^n)$ for every $s$.
```

## CP-II-0219

- chapter line: 15251

```tex
\label{prob:cp-ii-0219}
\par\noindent\textbullet\quad If $\tau$ is discrete and $\rho$ is indiscrete on $X$, then $\rho\subseteq\tau$; thus $\mathrm{id}:(X,\tau)\to(X,\rho)$ is continuous.
```

## CP-II-0221

- chapter line: 15301

```tex
\label{prob:cp-ii-0221}
Let
\[
F(x,y) = 1_{[0,1]^n}(x)\,1_{[0,1]^n}(y).
\]
Then
\[
\int_{\mathbb{R}^n} F(x,y)\,dy = 1_{[0,1]^n}(x),
\]
so
\[
\int_{\mathbb{R}^n}
\Bigl|\int_{\mathbb{R}^n} F(x,y)\,dy\Bigr|\,dx
= \int_{[0,1]^n} 1\,dx = 1.
\]
Moreover $|F|=F$, and
\[
\int_{\mathbb{R}^n}\int_{\mathbb{R}^n} |F(x,y)|\,dy\,dx
= \int_{[0,1]^n}\int_{[0,1]^n} 1\,dy\,dx
= 1.
\]
This concrete case illustrates that for $p=1$ and $F\ge0$ the inequality
is actually an equality.
```

## CP-II-0224

- chapter line: 15363

```tex
\label{prob:cp-ii-0224}
$f_n(x)=\sin(nx)$ on $[0,2\pi]$ (Not Equicontinuous)
```

## CP-II-0226

- chapter line: 15368

```tex
\label{prob:cp-ii-0226}
\par\noindent\textbullet\quad the Monotone or Dominated Convergence Theorem;
```

## CP-II-0228

- chapter line: 15394

```tex
\label{prob:cp-ii-0228}
\par\noindent\textbullet\quad For general nonnegative measurable $F$, approximate $F$ from below
	by simple functions and use the Monotone Convergence Theorem.
```

## CP-II-0231

- chapter line: 15400

```tex
\label{prob:cp-ii-0231}
\par\noindent\textbullet\quad More generally, for any polynomial $P$ we have
	$P(x)e^{-|x|^2}\in\mathcal{S}(\mathbb{R}^n)$.
```

## CP-II-0232

- chapter line: 15406

```tex
\label{prob:cp-ii-0232}
Let $A\subset \mathbb{R}^n$ and $f,g:A\to\mathbb{R}$.

\par\noindent\textbullet\quad Suppose $f$ and $g$ are uniformly continuous and bounded on $A$. Then $fg$ is uniformly continuous and bounded on $A$.

\textit{Solution (boundedness).} If $|f|\le M_f$ and $|g|\le M_g$ on $A$, then $|fg|\le M_fM_g$.

\textit{Solution (uniform continuity).} Fix $\varepsilon>0$ and set
$\eta=\min\!\left(1,\frac{\varepsilon}{2(M_f+M_g+1)}\right)$.
By uniform continuity of $f$ and $g$, there exists $\delta>0$ such that
$\|x-y\|<\delta$ implies $|f(x)-f(y)|<\eta$ and $|g(x)-g(y)|<\eta$.
Then for such $x,y$,
\begin{align*}
|f(x)g(x)-f(y)g(y)|
&= |[f(x)-f(y)][g(x)-g(y)] + g(y)[f(x)-f(y)] + f(y)[g(x)-g(y)]|\\
&\le \eta^2 + M_g\,\eta + M_f\,\eta
\;\le\; (M_f+M_g+1)\eta \;\le\; \varepsilon.
\end{align*}
Hence $fg$ is uniformly continuous.

\par\noindent\textbullet\quad If $f$ and $g$ are uniformly continuous but not necessarily bounded, $fg$ need not be uniformly continuous.

\textit{Counterexample.} On $\mathbb{R}$, take $f(x)=x$ and $g(x)=\sin x$. Both are uniformly continuous (Lipschitz).
Assume $x\sin x$ were uniformly continuous. For $\varepsilon=1$, let $\delta>0$ be its modulus.
Set $t=\min(\delta/2,1)$ and take $y_k=k\pi$, $x_k=k\pi+t$.
Then $|x_k-y_k|=t<\delta$ but
\[
|x_k\sin x_k - y_k\sin y_k| = |(k\pi+t)\sin t| \ge k\pi \sin t \xrightarrow{k\to\infty} \infty,
\]
contradicting uniform continuity. Thus $x\sin x$ is not uniformly continuous.
```

## CP-II-0233

- chapter line: 15439

```tex
\label{prob:cp-ii-0233}
(Diagonal).

$A=\begin{pmatrix}3&0\\0&1\end{pmatrix}$ has $p_A(\lambda)=(\lambda-3)(\lambda-1)$, eigenvectors $e_1$ for $\lambda=3$ and $e_2$ for $\lambda=1$. Here $m_a=m_g=1$ for each eigenvalue, so $A$ is diagonalizable.
```

## CP-II-0234

- chapter line: 15446

```tex
\label{prob:cp-ii-0234}
\par\noindent\textbullet\quad \emph{Mutual singularity:} $\nu\perp\mu$ means there is $S\in\mathcal E$ with $\mu(S)=0$ and $\nu(E\setminus S)=0$.
```

## CP-II-0235

- chapter line: 15451

```tex
\label{prob:cp-ii-0235}
\par\noindent\textbullet\quad Let $\eta \in \mathscr{S}(\mathbb{R}^n)$ satisfy
	\[
	\int_{\mathbb{R}^n} \eta(x)\,dx = 1,
	\]
	and define the mollifiers
	\[
	\eta_\varepsilon(x) := \varepsilon^{-n}\eta\!\left(\frac{x}{\varepsilon}\right),
	\qquad \varepsilon>0.
	\]
	Show that for every $f \in H^{s}(\mathbb{R}^n)$ one has
	\[
	\eta_\varepsilon * f \longrightarrow f
	\quad\text{in } H^{s}(\mathbb{R}^n)
	\quad\text{as } \varepsilon\to 0.
	\]
```

## CP-II-0236

- chapter line: 15470

```tex
\label{prob:cp-ii-0236}
\par\noindent\textbullet\quad The key idea is to define
	\[
	u(x) := \int_{\mathbb{R}^n} F(x,y)\,dy,
	\qquad
	G(y) := |u(y)|^{p-1}\operatorname{sgn}(u(y)),
	\]
	so that
	\[
	\|u\|_{L^p}^p = \int_{\mathbb{R}^n} u(x) G(x)\,dx.
	\]
```

## CP-II-0239

- chapter line: 15548

```tex
\label{prob:cp-ii-0239}
Suppose $A\subset\mathbb{R}^n$ and let $(f_i)_{i=0}^\infty$ with $f_i:A\to\mathbb{R}^m$ be a sequence of functions.
Assume $f_i\to f$ \emph{uniformly} on $A$. Show that if $B\subset A$, then $f_i\to f$ uniformly on $B$.

\textit{Solution.} By uniform convergence on $A$, for every $\varepsilon>0$ there exists $N\in\mathbb{N}$ such that
for all $i\ge N$ and all $x\in A$ we have $\|f_i(x)-f(x)\|<\varepsilon$. Since $B\subset A$, this inequality holds
for all $x\in B$ as well, with the \emph{same} $N$. Hence $f_i\to f$ uniformly on $B$. Equivalently,
\[
\sup_{x\in B}\|f_i(x)-f(x)\|\le \sup_{x\in A}\|f_i(x)-f(x)\|\xrightarrow{i\to\infty} 0.
\]
```

## CP-II-0240

- chapter line: 15561

```tex
\label{prob:cp-ii-0240}
\par\noindent\textbullet\quad Conclude that
		\[
		\widehat{K_t}(\xi) = e^{-it|\xi|^2}.
		\]
```

## CP-II-0241

- chapter line: 15569

```tex
\label{prob:cp-ii-0241}
Suppose $A\subset\mathbb{R}^n$ and let $(f_i)_{i=0}^\infty$ with $f_i:A\to\mathbb{R}^m$.
Classify whether each statement is equivalent to (i) pointwise convergence $f_i\to f$,
(ii) uniform convergence $f_i\to f$ uniformly, or (iii) neither.

\renewcommand\labelenumi{(\alph{enumi})}

\par\noindent\textbullet\quad Given $\varepsilon>0$, there exists $N\in\mathbb{N}$ such that for all $i\ge N$:
\[
\sup_{x\in A}\|f_i(x)-f(x)\|<\varepsilon.
\]
\textit{Classification: (ii) uniform convergence.} This is exactly the definition via the sup norm.

\par\noindent\textbullet\quad For all $x\in A$, for all $i\in\mathbb{N}$ there exists $\varepsilon>0$ such that
\[
\|f_i(x)-f(x)\|<\varepsilon.
\]
\textit{Classification: (iii) neither.} The statement is always true (take, e.g., $\varepsilon=\|f_i(x)-f(x)\|+1$), so it does not characterize convergence.

\par\noindent\textbullet\quad There exists $N\in\mathbb{N}$ such that for all $x\in A$, $i\ge N$, $\varepsilon>0$:
\[
\|f_i(x)-f(x)\|<\varepsilon.
\]
\textit{Classification: (iii) neither.} Since the left-hand side is nonnegative, the inequality for \emph{all} $\varepsilon>0$ forces $\|f_i(x)-f(x)\|=0$; i.e.\ there is $N$ with $f_i\equiv f$ on $A$ for all $i\ge N$. This condition is much stronger than uniform convergence and is not equivalent to it in general.

\par\noindent \textit{*}d)\quad $\forall\varepsilon>0\ \forall x\in A\ \exists N\in\mathbb{N}\ \forall i\ge N:\ \|f_i(x)-f(x)\|<\varepsilon$.\\
\textit{Classification: (i) pointwise convergence.} The quantifier order matches the definition; $N$ may depend on $x$ and $\varepsilon$.

\par\noindent \textit{*}e)\quad $\forall\varepsilon>0\ \exists N\in\mathbb{N}\ \forall x\in A\ \forall i\ge N:\ \|f_i(x)-f(x)\|<\varepsilon$.\\
\textit{Classification: (ii) uniform convergence.} Here $N$ works simultaneously for all $x\in A$.

\par\noindent \textit{*}f)\quad $\forall\varepsilon>0\ \exists N\in\mathbb{N}\ \forall x\in A:\ (\,i\ge N\ \Leftrightarrow\ \|f_i(x)-f(x)\|<\varepsilon\,)$.\\
\textit{Classification: (iii) neither.} This is far stronger than uniform convergence (it also demands that for $i<N$ the error is $\ge\varepsilon$ for every $x$), and it need not hold even when $f_i\to f$ uniformly.
```

## CP-II-0243

- chapter line: 15605

```tex
\label{prob:cp-ii-0243}
\par\noindent\textbullet\quad \textbf{Indicators.} For a set $C\subset X$, the indicator
		$I_C(x)=0$ if $x\in C$ and $+\infty$ otherwise is l.s.c.\ iff $C$ is closed;
		u.s.c.\ iff $C$ is open.
```

## CP-II-0244

- chapter line: 15612

```tex
\label{prob:cp-ii-0244}
\par\noindent\textbullet\quad Set $t = p^{-1}$ and consider the function
	\[
	\varphi(t) = \log\bigl[t a^p + (1-t)b^q\bigr].
	\]
	Because $\log$ is concave, Jensen's inequality yields
	\[
	\log\bigl[t a^p + (1-t)b^q\bigr]
	\;\ge\; t\log(a^p) + (1-t)\log(b^q)
	= p\,t\log a + q(1-t)\log b.
	\]
	Choosing $t=1/p$ (so $1-t=1/q$) gives
	\[
	\log\!\left(\frac{a^p}{p} + \frac{b^q}{q}\right)
	\;\ge\; \log a + \log b = \log(ab),
	\]
	which is precisely Young's inequality.

Let
\[
\Phi(x) = \frac{x^p}{p}, \qquad x\ge 0.
\]
Then $\Phi$ is convex and its Legendre transform (convex conjugate) is
\[
\Phi^*(y)
= \sup_{x\ge0}\bigl(xy - \Phi(x)\bigr)
= \frac{y^q}{q}, \qquad y\ge0,
\]
where $q$ is the Hölder conjugate of $p$, i.e.\ $\frac1p+\frac1q=1$.
The Fenchel--Young inequality asserts that
\[
xy \le \Phi(x) + \Phi^*(y), \qquad x,y\ge0.
\]
Substituting $\Phi(x)=x^p/p$ and $\Phi^*(y)=y^q/q$ yields
\[
xy \le \frac{x^p}{p} + \frac{y^q}{q},
\]
which is Young's inequality (with $x=a$, $y=b$).  Thus Young's
inequality expresses the Legendre duality between the functions
$x\mapsto x^p/p$ and $y\mapsto y^q/q$.

\bigskip
```

## CP-II-0245

- chapter line: 15657

```tex
\label{prob:cp-ii-0245}
\par\noindent\textbullet\quad For $t>0$, define $K_\varepsilon \in L^1_{\mathrm{loc}}(\mathbb{R}^n)$ by
	\[
	K_\varepsilon(x)
	= \frac{1}{(4\pi i t)^{n/2}} \, e^{\, i|x|^2 / 4t },
	\]
	where for $n$ odd we take the usual branch cut so that $i^{1/2}=e^{i\pi/4}$.
	For $\varepsilon>0$ set
	\[
	K_\varepsilon^t(x) = e^{-\varepsilon|x|^2}\, K_t(x).
	\]
```

## CP-II-0246

- chapter line: 15671

```tex
\label{prob:cp-ii-0246}
$f_n(x)=\sin(nx)/n$ on $[0,2\pi]$ (Equicontinuous, converges uniformly to 0)

---
```

## CP-II-0247

- chapter line: 15678

```tex
\label{prob:cp-ii-0247}
\par\noindent\textbullet\quad $f=\mathbf 1_{[0,1]}$. Then $F(x)=0$ for $x<0$, $F(x)=x$ on $[0,1]$, $F(x)=1$ for $x>1$.
	$F'(x)=1$ on $(0,1)$ and $0$ elsewhere; $x=0,1$ are the only non-Lebesgue points for $f$.
```

## CP-II-0248

- chapter line: 15684

```tex
\label{prob:cp-ii-0248}
\par\noindent\textbullet\quad Applying Hölder's inequality to the right-hand side gives
	\[
	\|u\|_{L^p}^p
	\le
	\|G\|_{L^q}
	\int_{\mathbb{R}^n}
	\left(
	\int_{\mathbb{R}^n} |F(x,y)|^p \, dx
	\right)^{1/p} dy,
	\]
	from which Minkowski's integral inequality follows.

\bigskip
```

## CP-II-0255

- chapter line: 15896

```tex
\label{prob:cp-ii-0255}
$f_n(x)=x^n$ on $[0,1]$ (Not equicontinuous)

---
```

## CP-II-0258

- chapter line: 15938

```tex
\label{prob:cp-ii-0258}
Trigonometric example.

On $[0,\pi]$ let
\[
F(x,y) = \sin^2 x\,\sin^2 y.
\]
Since $\displaystyle \int_0^\pi \sin^2 t\,dt = \frac{\pi}{2}$,
\[
\int_0^\pi \Bigl|\int_0^\pi F(x,y)\,dy\Bigr|dx
= \frac{\pi^2}{4}
= \int_0^\pi\int_0^\pi F(x,y)\,dy\,dx.
\]

These examples illustrate how regular, smooth functions behave exactly
like simple functions when $p=1$ and $F\ge 0$: the inequality becomes an
equality.
```

## CP-II-0259

- chapter line: 15958

```tex
\label{prob:cp-ii-0259}
(Smooth bump in all $H^s$).

Let $b(x)=e^{-1/(1-x^2)}$ for $|x|<1$ and $b=0$ otherwise.
Then $b\in C_c^\infty(\mathbb R)$ and for every $N$,
$|\widehat b(\xi)|\le C_N(1+|\xi|)^{-N}$. Hence
$\|b\|_{H^s}<\infty$ for all $s\in\mathbb R$.

\clearpage
```

## CP-II-0261

- chapter line: 15970

```tex
\label{prob:cp-ii-0261}
\par\noindent\textbullet\quad \textbf{Dirichlet energy.} On $H^1(\Omega)$,
		$E(u)=\int_\Omega |\nabla u|^2\,dx$ is weakly l.s.c.; hence minimizing sequences
		have weakly convergent subsequences with $E$-limit $\ge$ the value at the weak limit
		(direct method of the calculus of variations).
```

## CP-II-0263

- chapter line: 15978

```tex
\label{prob:cp-ii-0263}
\par\noindent\textbullet\quad Choose an orthonormal sequence $(e_i)_{i\ge1}\subset H$.
		Then for every $y\in H$,
		$\langle y,e_i\rangle\to0$ by BesselĂ˘â‚¬â„˘s inequality,
		hence $e_i\rightharpoonup0$.
		However $\|e_i\|=1$ for all $i$,
		so $e_i\nrightarrow0$ in norm.
```

## CP-II-0266

- chapter line: 16020

```tex
\label{prob:cp-ii-0266}
— Smooth Approximation of a Periodic $L^p$ Function

Let $f\in L^p_{\mathrm{loc}}(\mathbb{R}^n)$ be periodic.
Define the cubes
\[
Q = \{x : |x_j|<1\}, \qquad q = \{x : |x_j|<\tfrac12\}.
\]

\bigskip
\noindent\textbf{(a) Construction of $h_\varepsilon$}

Choose $\chi\in C_c^\infty(\mathbb{R}^n)$ with
$\chi\equiv 1$ on $q$ and $\operatorname{supp}\chi \subset Q$.
Set $g := f\chi$. Then $\operatorname{supp}g \subset Q$ and $g=f$ on $q$.

Since $C_c^\infty$ is dense in $L^p$, choose $h_\varepsilon\in C^\infty$ with
$\operatorname{supp}h_\varepsilon\subset Q$ and
\[
\|g - h_\varepsilon\|_{L^p(\mathbb{R}^n)} < \varepsilon.
\]
But $f1_q = g$, so
\[
\|f1_q - h_\varepsilon\|_{L^p(\mathbb{R}^n)} < \varepsilon.
\]

\bigskip
Define
\[
f_\varepsilon(x) := \sum_{g\in\mathbb{Z}^n} h_\varepsilon(x-g)
= \sum_{g\in\mathbb{Z}^n} \tau_g h_\varepsilon(x).
\]

\bigskip
\noindent\textbf{(b) $f_\varepsilon$ is smooth and periodic}

Since $\operatorname{supp}h_\varepsilon\subset Q$, at each $x$ only finitely many terms are nonzero.
Thus $f_\varepsilon\in C^\infty(\mathbb{R}^n)$.

For periodicity:
\[
f_\varepsilon(x+k)
= \sum_{g} h_\varepsilon(x+k-g)
= \sum_{h} h_\varepsilon(x-h)
= f_\varepsilon(x),
\]
after substituting $h=g-k$.
Thus $f_\varepsilon$ is $\mathbb{Z}^n$-periodic.

\bigskip
\noindent\textbf{(c) Estimate on $q$}

If $x\in q$ and $h_\varepsilon(x-g)\neq 0$, then $x-g\in Q$, so $g$ lies in the finite set
\[
G = \{g\in\mathbb{Z}^n : (Q+g)\cap q \neq \emptyset\}.
\]
Thus
\[
f_\varepsilon(x) = \sum_{g\in G} h_\varepsilon(x-g).
\]

Since $f$ is periodic,
\[
f(x-g)=f(x),
\]
and by translation invariance,
\[
\|f1_q - h_\varepsilon(\cdot - g)\|_{L^p(\mathbb{R}^n)} < \varepsilon,
\quad g\in G.
\]

On $q$,
\[
f(x)-f_\varepsilon(x)
= \sum_{g\in G} \bigl(f(x) - h_\varepsilon(x-g)\bigr),
\]
so
\[
\|f - f_\varepsilon\|_{L^p(q)}
\le \sum_{g\in G} \|f - h_\varepsilon(\cdot-g)\|_{L^p(q)}
\le (\#G)\varepsilon.
\]

Let $c_n := \#G$. Then
\[
\|f - f_\varepsilon\|_{L^p(q)} < c_n \varepsilon.
\]
```

## CP-II-0270

- chapter line: 16217

```tex
\label{prob:cp-ii-0270}
\par\noindent (b)\quad Show $\mathbf 1_I\in\overline{\mathrm{Span}}\{\psi_{n,k}\}$ for every finite interval $I$ (closure in $L^2$).
```

## CP-II-0272

- chapter line: 16222

```tex
\label{prob:cp-ii-0272}
(b,c)

	\setcounter{enumi}{1}
	\par\noindent\textbullet\quad Along $te_2=(0,t)$,
	\[
	D_1 f(0,t)=t \;\;\Rightarrow\;\;\frac{D_1 f(0,t)-D_1 f(0,0)}{t}=1.
	\]
	Along $te_1=(t,0)$,
	\[
	D_2 f(t,0)=-t \;\;\Rightarrow\;\;\frac{D_2 f(t,0)-D_2 f(0,0)}{t}=-1.
	\]

	\par\noindent\textbullet\quad Hence
	\[
	D_2D_1 f(0)=1, \quad D_1D_2 f(0)=-1.
	\]
	So both exist, but are not equal.
```

## CP-II-0274

- chapter line: 16316

```tex
\label{prob:cp-ii-0274}
\renewcommand\labelenumi{(\alph{enumi})}
\par\noindent\textbullet\quad Show that the inner product has the following properties for all $x,y,z\in\mathbb{R}^n$ and $a\in\mathbb{R}$:
\[
\langle x,y\rangle=\langle y,x\rangle,\qquad
\langle x+y,z\rangle=\langle x,z\rangle+\langle y,z\rangle,\qquad
\langle ax,y\rangle=a\langle x,y\rangle.
\]
\textit{Solution.} These follow from the Euclidean inner product $\langle x,y\rangle=\sum_{i=1}^n x_i y_i$.

\par\noindent\textbullet\quad For $t\in\mathbb{R}$ and $x,y\in\mathbb{R}^n$ show
\[
\|x+ty\|^2=\|x\|^2+2t\langle x,y\rangle+t^2\|y\|^2\ge 0.
\]
\textit{Solution.} Expand $\langle x+ty,x+ty\rangle$.

\par\noindent\textbullet\quad Deduce Cauchy--Schwarz: $|\langle x,y\rangle|\le \|x\|\,\|y\|$.\\
\textit{Solution.} View $\|x+ty\|^2$ as a quadratic in $t$ and use non-positivity of its discriminant.
Equality iff $x,y$ are linearly dependent.

\par\noindent\textbullet\quad Deduce the triangle inequality $\|x+y\|\le \|x\|+\|y\|$.

\par\noindent\textbullet\quad Show the reverse triangle inequality $|\|x\|-\|y\||\le \|x-y\|$.

\par\noindent\textbullet\quad Suppose $x=(x^1,\dots,x^n)^t$.

\renewcommand\labelenumii{(\roman{enumii})}
\par\noindent\textbullet\quad $\displaystyle \max_{k}|x^k|\le \|x\|$.
\par\noindent\textbullet\quad $\displaystyle \|x\|\le \sqrt{n}\,\max_{k}|x^k|$.

\textit{Solution.} Immediate from $\|x\|^2=\sum (x^i)^2$.
```

## CP-II-0275

- chapter line: 16350

```tex
\label{prob:cp-ii-0275}
\par\noindent\textbullet\quad Show that if $t \ge s$, then
	\[
	\|f\|_{H^{s}(\mathbb{R}^n)} \le \|f\|_{H^{t}(\mathbb{R}^n)}.
	\]
	Deduce that
	\[
	\|f\|_{L^2(\mathbb{R}^n)}
	\le \frac{1}{(2\pi)^{n/2}}\|f\|_{H^{s}(\mathbb{R}^n)}.
	\]
	\emph{Hint: Use Parseval's formula.}
```

## CP-II-0277

- chapter line: 16418

```tex
\label{prob:cp-ii-0277}
\par\noindent\textbullet\quad Show that \((3)\) admits a unique solution $u$ such that
	\[
	u \in C^0([0,T];H^2(\mathbb{R}^n)) \cap C^1((0,T);L^2(\mathbb{R}^n)),
	\]
	whose spatial Fourier–Plancherel transform is given by
	\[
	\widehat{u}(t,\xi) = \widehat{u_0}(\xi)\, e^{-it|\xi|^2}.
	\]
```

## CP-II-0284

- chapter line: 16553

```tex
\label{prob:cp-ii-0284}
\par\noindent\textbullet\quad If a real polynomial vanishes on an infinite subset of $[0,1]$ with a limit point in $[0,1]$,
	then it is identically zero (identity theorem for polynomials).
```

## CP-II-0285

- chapter line: 16559

```tex
\label{prob:cp-ii-0285}
\par\noindent\textbullet\quad \textbf{Linear rate.}
	For $\delta_n=\frac{1}{n+1}$, one has
	$\gamma_j=\frac{1}{j}-\frac{1}{j+1}=\frac{1}{j(j+1)}$ and
	\[
	f(x)=\sum_{j\ge1}\frac{1}{j(j+1)}\,T_{3j}(x),
	\qquad E_n(f)\ge\frac{1}{n+1}.
	\]
```

## CP-II-0287

- chapter line: 16570

```tex
\label{prob:cp-ii-0287}
\par\noindent\textbullet\quad The Hölder conjugate exponent $q$ of $p$ is defined by
	\[
	\frac{1}{p} + \frac{1}{q} = 1,
	\qquad 1 < p < \infty.
	\]
```

## CP-II-0288

- chapter line: 16579

```tex
\label{prob:cp-ii-0288}
\par\noindent\textbullet\quad \emph{Totally bounded}: for every $\varepsilon>0$, there exist $x_1,\dots,x_N\in X$ such that
	\[
	X \subset \bigcup_{i=1}^N B(x_i,\varepsilon).
	\]
```

## CP-II-0290

- chapter line: 16652

```tex
\label{prob:cp-ii-0290}
\par\noindent\textbullet\quad \textbf{Homogeneity:} $\|\alpha p\|_{I}=\sup_{t\in I}|\alpha||p(t)|=|\alpha|\,\|p\|_{I}$.
```

## CP-II-0292

- chapter line: 16657

```tex
\label{prob:cp-ii-0292}
\par\noindent\textbullet\quad all integrals reduce to finite sums;
```

## CP-II-0294

- chapter line: 16662

```tex
\label{prob:cp-ii-0294}
State whether the sequence $(f_i)_{i=0}^\infty$ of functions converges pointwise and/or uniformly.

\renewcommand\labelenumi{(\alph{enumi})}

\par\noindent\textbullet\quad $f_i:\mathbb{R}\to\mathbb{R}$, \; $f_i(x)=e^{x}+\dfrac{1}{i+1}$.

\textit{Solution.} For each $x$, $f_i(x)\to e^x$. Moreover
\[
\sup_{x\in\mathbb{R}} |f_i(x)-e^x|=\sup_{x\in\mathbb{R}}\frac{1}{i+1}=\frac{1}{i+1}\xrightarrow{i\to\infty}0,
\]
so $f_i\to e^x$ \emph{uniformly} on $\mathbb{R}$.

\par\noindent\textbullet\quad $f_i:\mathbb{R}\to\mathbb{R}$, \; $f_i(x)=x+2^{-i}x^2$.

\textit{Solution.} For fixed $x$, $f_i(x)\to x$. However
\[
\sup_{x\in\mathbb{R}} |f_i(x)-x|=\sup_{x\in\mathbb{R}} 2^{-i}x^2=+\infty \quad \text{for every fixed } i,
\]
hence the convergence is \emph{not} uniform on $\mathbb{R}$.
(Nonetheless, on any bounded interval $[-M,M]$ the convergence is uniform since
$\sup_{|x|\le M} |f_i(x)-x|=2^{-i}M^2\to 0$.)

\par\noindent\textbullet\quad $f_i:[0,1]\to\mathbb{R}$ given by
\[
f_i(x)=
\begin{cases}
2^i x, & 0\le x<2^{-i},\\[2pt]
2-2^i x, & 2^{-i}\le x<2^{-(i-1)},\\[2pt]
0, & x\ge 2^{-(i-1)}.
\end{cases}
\]
\textit{Solution.} For every $x\in[0,1]$, $f_i(x)\to 0$ (as in Exercise 3.1). But
$\sup_{x\in[0,1]} f_i(x)=1$ for all $i$, so the convergence is \emph{not} uniform on $[0,1]$.
(On $[\delta,1]$ with $\delta>0$, the convergence is uniform.)
```

## CP-II-0295

- chapter line: 16700

```tex
\label{prob:cp-ii-0295}
\par\noindent\textbullet\quad $f(x,y)=x+y$ is Lipschitz in both variables and continuous.
```

## CP-II-0296

- chapter line: 16705

```tex
\label{prob:cp-ii-0296}
Quickies on norms

Two norms $\|\cdot\|,\|\cdot\|'$ on $V$ are Lipschitz equivalent iff there exist $r,R>0$ with
	$B_r\subseteq B_1'\subseteq B_R$, where $B_\rho=\{x:\|x\|<\rho\}$, $B'_\rho=\{x:\|x\|'<\rho\}$.
	Indeed, $c\|x\|\le \|x\|'\le C\|x\|$ implies the inclusions with $r=1/C$, $R=1/c$;
	conversely the inclusions give $\|x\|'\le (1/r)\|x\|$ and $\|x\|\le R\|x\|'$.

	The bounds $c\|x\|\le \|x\|'\le C\|x\|$ imply
	$\|x_n-x\|\to0 \Leftrightarrow \|x_n-x\|'\to0$. Conversely, if this fails, one can find
	$\|x_k\|=1$ with $\|x_k\|'\to\infty$; then $y_k=x_k/k$ satisfies $y_k\to0$ in $\|\cdot\|$
	but not in $\|\cdot\|'$.

	It is a norm. If $\varphi$ is not continuous, there are $x_k$ with $\|x_k\|=1$ and
	$|\varphi(x_k)|\to\infty$, hence $\|x_k\|_\varphi\to\infty$, so no inequality
	$\|x\|_\varphi\le C\|x\|$ holds; thus $\|\cdot\|_\varphi$ is not Lipschitz equivalent to $\|\cdot\|$.

	If every norm on $V$ is Lipschitz equivalent to $\|\cdot\|$, then $V$ must be finite-dimensional.
	Otherwise there exists a discontinuous linear functional $\varphi$ on $V$, and by (c) the norm
	$\|x\|+|\varphi(x)|$ would not be equivalent to $\|\cdot\|$.

	\bigskip
```

## CP-II-0302

- chapter line: 16730

```tex
\label{prob:cp-ii-0302}
\par\noindent\textbullet\quad If $(S_n)$ bounded and $x^n$ monotone $\downarrow 0$, then $\sum a_n x^n$ converges (Dirichlet).
```

## CP-II-0306

- chapter line: 16735

```tex
\label{prob:cp-ii-0306}
\par\noindent\textbullet\quad \textbf{Practical diagnostics.}
	Sampling only at $\{x_k\}$ detects the worst-case error and guides adaptive refinement.
```

## CP-II-0307

- chapter line: 16741

```tex
\label{prob:cp-ii-0307}
Which of the following subsets of $\mathbb{R}^n$ is open?

\renewcommand\labelenumi{(\alph{enumi})}
\par\noindent\textbullet\quad $\mathbb{R}^n$: \textbf{Yes}.
\par\noindent\textbullet\quad $\varnothing$: \textbf{Yes}.
\par\noindent\textbullet\quad $\{x\in\mathbb{R}^n:x^1>0\}$: \textbf{Yes}.
\par\noindent\textbullet\quad $\{x\in\mathbb{R}^n:x^i\in[0,1]\}$: \textbf{No}.
\par\noindent\textbullet\quad $\mathbb{Q}^n$: \textbf{No}.
```

## CP-II-0308

- chapter line: 16753

```tex
\label{prob:cp-ii-0308}
Let $(x_i)$ and $(y_i)$ in $\mathbb{R}^n$ satisfy $x_i\to x$, $y_i\to y$.

\renewcommand\labelenumi{(\alph{enumi})}
\par\noindent\textbullet\quad $x_i+y_i\to x+y$. \textit{Proof.} $\|(x_i+y_i)-(x+y)\|\le \|x_i-x\|+\|y_i-y\|\to 0$.
\par\noindent\textbullet\quad $\langle x_i,y_i\rangle\to \langle x,y\rangle$; in particular $\|x_i\|\to \|x\|$.\\
\textit{Proof.} Expand $\langle x_i,y_i\rangle-\langle x,y\rangle$ and use Cauchy--Schwarz.
\par\noindent\textbullet\quad If $a_i\to a$ in $\mathbb{R}$, then $a_i x_i\to ax$.\\
\textit{Proof.} $a_ix_i-ax=(a_i-a)(x_i-x)+(a_i-a)x+a(x_i-x)$.
```

## CP-II-0312

- chapter line: 16765

```tex
\label{prob:cp-ii-0312}
\par\noindent\textbullet\quad \textbf{Oscillations.}
		On $[0,1]$, $f_j(x)=\sin(2\pi j x)$ is bounded in $L^{p}$ for all $1\le p\le\infty$ and
		$f_j\rightharpoonup 0$ in $L^{p}$, since $\int_0^1 f_j\,h\to0$ for all $h\in L^{p'}$
		(Riemann--Lebesgue lemma and density).
```

## CP-II-0314

- chapter line: 16789

```tex
\label{prob:cp-ii-0314}
\par\noindent\textbullet\quad In $L^2(\mathbb R)$ let $f_j=\mathbf1_{(j,j+1)}$. Then $\|f_j\|_2=1$, and for any bounded $E$,
		eventually $\int_E f_j=0$, hence $\int_E f_j\to0=\int_E 0$. Thus $f_j\rightharpoonup 0$ (not strongly).
```

## CP-II-0316

- chapter line: 16795

```tex
\label{prob:cp-ii-0316}
The series
	\[
	L=\sum_{n=1}^{\infty}10^{-n!}
	\]
	defines a Liouville number. Its $N$-th truncation $p_N/10^{N!}$ satisfies
	\[
	\Bigl|L-\frac{p_N}{10^{N!}}\Bigr|
	=\sum_{n\ge N+1}10^{-n!}
	<10^{-(N+1)!}
	\le \frac{1}{(10^{N!})^{\,m}}
	\quad\text{for all }m\le N+1,
	\]
	so $L$ is Liouville and hence transcendental.
```

## CP-II-0318

- chapter line: 16812

```tex
\label{prob:cp-ii-0318}
\par\noindent\textbullet\quad if $d(x,y)<n+1$ then $d(f(x),f(y))<n$;
```

## CP-II-0319

- chapter line: 16817

```tex
\label{prob:cp-ii-0319}
\par\noindent\textbullet\quad Box kernel: $\phi=|B_1|^{-1}\mathbf 1_{B_1(0)}$.

\bigskip\hrule\bigskip

\section*{Exercise 11 — Haar system on $\mathbb{R}$}

Let $\psi=\mathbf 1_{[0,1/2)}-\mathbf 1_{[1/2,1)}$ and $\psi_{n,k}(x)=2^{n/2}\psi(2^n x-k)$, $n,k\in\mathbb{Z}$.
 \par\noindent\textbullet\quad sep2pt
```

## CP-II-0324

- chapter line: 16829

```tex
\label{prob:cp-ii-0324}
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

	We present a collection of classical examples of sequences of functions, with charts illustrating whether convergence is pointwise, uniform, or fails.

	---

	\[
	f_n(x) \to f(x)=
	\begin{cases}
		0, & x\in[0,1), \\
		1, & x=1.
	\end{cases}
	\]
	Pointwise but not uniform, since $\|f_n-f\|_\infty = 1$.

	---

	\[
	f_n(x)\to 0 \quad \text{uniformly, since } \sup_{x\in[0,1]} |f_n(x)|=1/n\to 0.
	\]

	---

	No pointwise limit exists except at some special points.
	Not uniform: $\|f_n-f_m\|_\infty=2$ infinitely often.

	---

	\[
	|f_n(x)| \leq \tfrac{1}{n}, \quad \|f_n\|_\infty=1/n \to 0.
	\]
	Thus convergence is uniform despite oscillations.

	---

	\subsection*{5. $f_n(x)=\tfrac{1}{1+nx}$ on $[0,1]$ (Pointwise not uniform)}
	\[
	f_n(x)\to f(x)=
	\begin{cases}
		0, & x>0, \\
		1, & x=0.
	\end{cases}
	\]
	Not uniform because $\|f_n-f\|_\infty=1$.

	---

	\subsection*{6. $f_n(x)=e^{-nx^2}$ on $\mathbb{R}$ (Gaussian bump)}
	\[
	f_n(x)\to f(x)=
	\begin{cases}
		0, & x\neq 0, \\
		1, & x=0.
	\end{cases}
	\]
	Not uniform, since the peak at $0$ prevents uniform convergence.

	---

	\subsection*{7. $f_n(x)=x^{1/n}$ on $[0,1]$ (Discontinuous limit, not uniform)}
	\[
	f_n(x)\to f(x)=
	\begin{cases}
		1, & x>0, \\
		0, & x=0.
	\end{cases}
	\]
	Limit function is discontinuous, hence convergence not uniform.

	---

	\subsection*{8. $f_n(x)=\tfrac{x^2}{n+1}$ on $[0,1]$ (Uniform)}
	\[
	f_n(x)\to 0 \quad \text{uniformly, since } \|f_n\|_\infty=1/(n+1)\to 0.
	\]

	---

	We present a collection of classical examples of sequences of functions, with charts illustrating whether convergence is pointwise, uniform, or fails.

	---

	\[
	f_n(x) \to f(x)=
	\begin{cases}
		0, & x\in[0,1), \\
		1, & x=1.
	\end{cases}
	\]
	Pointwise but not uniform, since $\|f_n-f\|_\infty = 1$.

	---

	\[
	f_n(x)\to 0 \quad \text{uniformly, since } \sup_{x\in[0,1]} |f_n(x)|=1/n\to 0.
	\]

	---

	No pointwise limit exists except at some special points.
	Not uniform: $\|f_n-f_m\|_\infty=2$ infinitely often.

	---

	\[
	|f_n(x)| \leq \tfrac{1}{n}, \quad \|f_n\|_\infty=1/n \to 0.
	\]
	Thus convergence is uniform despite oscillations.

	---

	\subsection*{5. $f_n(x)=\tfrac{1}{1+nx}$ on $[0,1]$ (Pointwise not uniform)}
	\[
	f_n(x)\to f(x)=
	\begin{cases}
		0, & x>0, \\
		1, & x=0.
	\end{cases}
	\]
	Not uniform because $\|f_n-f\|_\infty=1$.

	---

	\subsection*{6. $f_n(x)=e^{-nx^2}$ on $\mathbb{R}$ (Gaussian bump)}
	\[
	f_n(x)\to f(x)=
	\begin{cases}
		0, & x\neq 0, \\
		1, & x=0.
	\end{cases}
	\]
	Not uniform, since the peak at $0$ prevents uniform convergence.

	---

	\subsection*{7. $f_n(x)=x^{1/n}$ on $[0,1]$ (Discontinuous limit, not uniform)}
	\[
	f_n(x)\to f(x)=
	\begin{cases}
		1, & x>0, \\
		0, & x=0.
	\end{cases}
	\]
	Limit function is discontinuous, hence convergence not uniform.

	---

	\subsection*{8. $f_n(x)=\tfrac{x^2}{n+1}$ on $[0,1]$ (Uniform)}
	\[
	f_n(x)\to 0 \quad \text{uniformly, since } \|f_n\|_\infty=1/(n+1)\to 0.
	\]

	---

	---

	\textbf{Uniform convergence:}
	A sequence of functions $f_n:D\to\mathbb{R}$ converges \emph{uniformly} to $f:D\to\mathbb{R}$ if
	\[
	\sup_{x\in D} |f_n(x)-f(x)| \;\to\; 0 \quad \text{as } n\to\infty.
	\]

	\textbf{Uniform continuity:}
	A function $f:D\to\mathbb{R}$ is \emph{uniformly continuous} on $D$ if
	\[
	\forall \varepsilon>0 \;\; \exists \delta>0 \;\; \text{s.t. } |x-y|<\delta \implies |f(x)-f(y)|<\varepsilon \quad \forall x,y\in D.
	\]

	---

		\par\noindent\textbullet\quad Uniform convergence concerns \emph{a sequence of functions} approaching a limit.
		\par\noindent\textbullet\quad Uniform continuity concerns \emph{a single function} behaving consistently across its domain.

	---

	  $f_n(x)=x/n$ on $[0,1]$.
	Then $f_n\to 0$ uniformly since $\sup_{x\in[0,1]}|f_n(x)|=1/n\to 0$.

	  $f_n(x)=x^n$ on $[0,1]$.
	Pointwise $f(x)=0$ for $x\in[0,1)$ and $f(1)=1$, but not uniform since $\|f_n-f\|_\infty=1$.

	---

	  $f(x)=\sqrt{x}$ on $[0,1]$.
	Continuous on compact set $\Rightarrow$ uniformly continuous (Heine--Cantor theorem).

	  $f(x)=x^2$ on $\mathbb{R}$.
	Continuous but not uniformly continuous: derivative grows without bound, so no global $\delta$ works.
	For example, take $x=n$, $y=n+1/n$, then $|x-y|=1/n\to 0$ but $|x^2-y^2|\approx 2$.

	---

	\renewcommand{\arraystretch}{1.3}
	\begin{tabular}{|c|c|c|}
		\hline
		Concept & Applies to & Key idea \\
		\hline
		Uniform convergence & Sequence $(f_n)$ & $f_n\to f$ uniformly if $\sup |f_n-f|\to 0$ \\
		\hline
		Uniform continuity & Single function $f$ & One $\delta$ works for all $x,y\in D$ \\
		\hline
	\end{tabular}

	---

A sequence $(f_i)_{i=0}^\infty$ with $f_i \in C^0([a,b])$ converges uniformly to some $f \in C^0([a,b])$
if and only if it is Cauchy in the sup norm:
\[
\forall \varepsilon >0 \;\; \exists N \;\; \forall m,n\geq N:\;
\sup_{x\in[a,b]} |f_n(x)-f_m(x)| < \varepsilon.
\]

---
```

## CP-II-0327

- chapter line: 17102

```tex
\label{prob:cp-ii-0327}
\par\noindent\textbullet\quad If $f,g\in\mathcal{S}$ then $f,g\in L^1$ and the convolution
	$f*g$ is well-defined and belongs to $\mathcal{S}(\mathbb{R}^n)$.
```

## CP-II-0329

- chapter line: 17108

```tex
\label{prob:cp-ii-0329}
\par\noindent\textbullet\quad approximation from below by increasing sequences of simple functions;
```

## CP-II-0335

- chapter line: 17113

```tex
\label{prob:cp-ii-0335}
\par\noindent\textbullet\quad For $1\le p<\infty$, the space $L^p(\mathbb{R}^n)$ consists of all
	measurable functions $f$ such that
	\[
	\int_{\mathbb{R}^n} |f(x)|^p \, dx < \infty.
	\]
```

## CP-II-0336

- chapter line: 17122

```tex
\label{prob:cp-ii-0336}
— A Heisenberg-type inequality and uncertainty

Suppose $f\in \mathcal S(\mathbb R^n)$. By observing that
\[
\|f\|_{L^2}^2
=\int_{\mathbb R^n}\frac{1}{n}\,(\operatorname{div}x)\,|f(x)|^2\,dx,
\]
or otherwise, show that
\[
(2\pi)^{\frac n2}\,\|f\|_{L^2}^2
\;\le\; \frac{2}{n}\,\big\|\,|x|\,f(x)\big\|_{L^2}\;\big\|\,|\xi|\,\widehat f(\xi)\big\|_{L^2},
\]
with equality if and only if $f(x)=a\,e^{-\lambda|x|^2}$ for some $a\in\mathbb C$, $\lambda>0$.
Deduce that for any $x_0,\xi_0\in\mathbb R^n$,
\[
(2\pi)^{\frac n2}\,\|f\|_{L^2}^2
\;\le\; \frac{2}{n}\,\big\|\,|x-x_0|\,f(x)\big\|_{L^2}\;\big\|\,|\xi-\xi_0|\,\widehat f(\xi)\big\|_{L^2}.
\]

\medskip

\noindent Explain how this shows that a function $f\in L^2(\mathbb R^n)$ cannot be sharply localised in both physical and Fourier space simultaneously (the \emph{uncertainty principle}).

Let
\[
\widehat f(\xi)=\int_{\mathbb R^n} e^{-i x\cdot \xi} f(x)\,dx,
\qquad \|f\|_{L^2}=(2\pi)^{-n/2}\|\widehat f\|_{L^2}.
\]

\smallskip

Since $\operatorname{div}x=n$ and $f\in\mathcal S(\mathbb R^n)$,
\[
\|f\|_2^2
=\frac1n\int_{\mathbb R^n}(\operatorname{div}x)\,|f|^2
=\frac2n\,\Re\int_{\mathbb R^n} x\cdot f\,\overline{\nabla f}\,dx.
\]

\smallskip

By Cauchy--Schwarz,
\[
\|f\|_2^2 \le \frac2n\,\|\,|x|f\|_2\,\|\nabla f\|_2.
\]
Plancherel with the above normalization gives
\[
\|\nabla f\|_2=(2\pi)^{-n/2}\,\|\,|\xi|\,\widehat f\|_2,
\]
hence
\[
(2\pi)^{\frac n2}\,\|f\|_2^2
\;\le\; \frac2n\,\|\,|x|f\|_2\,\|\,|\xi|\,\widehat f\|_2.
\tag{$\ast$}
\]

\smallskip

Equality in Cauchy--Schwarz requires $\nabla f(x)=-\lambda\,x\,f(x)$ for some $\lambda>0$
(up to a constant phase), whose solutions are precisely
\[
f(x)=a\,e^{-\lambda|x|^2},\qquad a\in\mathbb C,\ \lambda>0.
\]

\smallskip

Applying $(\ast)$ to $g(x)=e^{-i\xi_0\cdot x}f(x-x_0)$ yields
\[
(2\pi)^{\frac n2}\,\|f\|_2^2
\;\le\; \frac2n\,\|\,|x-x_0|\,f\|_2\,\|\,|\xi-\xi_0|\,\widehat f\|_2,
\qquad x_0,\xi_0\in\mathbb R^n.
\]

\smallskip

The product of the $L^2$-spreads in physical and Fourier space controls $\|f\|_2^2$.
One cannot make both $\|\,|x-x_0|f\|_2$ and $\|\,|\xi-\xi_0|\,\widehat f\|_2$ arbitrarily small unless $f\equiv0$.
Gaussians are the unique (up to symmetries) extremizers.
```

## CP-II-0337

- chapter line: 17203

```tex
\label{prob:cp-ii-0337}
For $f(u)=u^2$, $g(x)=e^x$, we have $(f\circ g)(x)=e^{2x}$.
Then
\[
(f\circ g)''(x)=4e^{2x},
\]
and by the formula,
$f''(g(x))(g'(x))^2+f'(g(x))g''(x)=2(e^x)^2+2e^x e^x=4e^{2x}$, confirming the result.
\hfill$\Box$

\bigskip\hrule\bigskip
```

## CP-II-0339

- chapter line: 17217

```tex
\label{prob:cp-ii-0339}
\par\noindent\textbullet\quad \emph{Alternative closedness proof.}
	If $E$ were not closed, pick $p\in\overline E\setminus E$ and consider the continuous
	distance-to-$p$ map $h(x)=\|x-p\|$. Then $h(E)\subset(0,\infty)$ is not closed in $\mathbb R$,
	so $1/h$ is unbounded on $E$—the same contradiction as above.
```

## CP-II-0343

- chapter line: 17289

```tex
\label{prob:cp-ii-0343}
\par\noindent\textbullet\quad The equivalence follows immediately from the definition of the weak topology
		and the Riesz representation theorem:
		$x_i\rightharpoonup x$ means
		$\Lambda(x_i)\to\Lambda(x)$ for every $\Lambda\in H'$,
		but each $\Lambda$ has the form $\Lambda(z)=\langle z,y\rangle$.
```

## CP-II-0344

- chapter line: 17298

```tex
\label{prob:cp-ii-0344}
\textbf{Two quick checks.}
	\hfill

		\par\noindent\textbullet\quad For $f(t)=t$ on $[0,1]$, $a_0=0$, $a_1=1$, and all $a_{m,k}=0$; hence $f=\varphi_1$ exactly.
		\par\noindent\textbullet\quad For $f(t)=t^2$ on $[0,1]$, $a_0=0$, $a_1=1$, and
		\(
		a_{m,k}=\frac{k^2}{4^m}-\tfrac12\frac{(k-1)^2+(k+1)^2}{4^m}=-4^{-m}
		\)
		(independent of $k$), so
		\(
		t^2=\varphi_1-\sum_{m\ge0}\sum_{k\ \mathrm{odd}}4^{-m}\varphi_{m,k}
		\)
		with uniform convergence. Transfer to $[-1,1]$ via $t=\tfrac{x+1}{2}$.
```

## CP-II-0347

- chapter line: 17315

```tex
\label{prob:cp-ii-0347}
Let $f_n:I\to\mathbb{R}$ be given by
	\[
	\begin{array}{ll}
		\text{(a)} & f_n(x)=x e^{-nx},\quad I=[0,+\infty);\\[3pt]
		\text{(b)} & f_n(x)=\dfrac{n^2x}{1+n^4x^2},\quad I=[0,1];\\[10pt]
		\text{(c)} & f_n(x)=(-1)^n\dfrac{x^n}{n},\quad I=[0,1].
	\end{array}
	\]
	Determine for each case whether $\sum_{n=1}^\infty f_n(x)$ converges or diverges on $I$,
	and if it converges, whether the convergence is pointwise, uniform,
	pointwise absolute, or uniform absolute.


	\textbf{Theory.}
	For a series of functions $\sum f_n$,

		\par\noindent\textbullet\quad it converges \emph{pointwise} if for each $x$ the numeric series $\sum f_n(x)$ converges;
		\par\noindent\textbullet\quad it converges \emph{uniformly} if $\sup_{x\in I}|\sum_{k>n}f_k(x)|\to0$;
		\par\noindent\textbullet\quad it is \emph{absolutely convergent} if $\sum|f_n(x)|$ converges;
		\par\noindent\textbullet\quad \emph{uniformly absolute} if $\sum\|f_n\|_\infty<\infty$.


	\textbf{(a)} $f_n(x)=x e^{-nx}$ on $[0,+\infty)$.

	For fixed $x>0$,
	\[
	\sum_{n=1}^\infty f_n(x)
	=x\sum_{n=1}^\infty e^{-nx}
	=x\frac{e^{-x}}{1-e^{-x}},
	\]
	which converges for all $x\ge0$.
	At $x=0$, $f_n(0)=0$.
	Hence the series converges pointwise and absolutely on $[0,+\infty)$.

	Since $\|f_n\|_\infty=\frac{1}{ne}$,
	the convergence is not uniform on the whole interval,
	but it is uniform on each compact $[0,M]$.

	\textit{Conclusion:}
	Pointwise and absolute convergence, uniform on compacts but not on $[0,+\infty)$.

	\medskip

	\textbf{(b)} $f_n(x)=\dfrac{n^2x}{1+n^4x^2}$ on $[0,1]$.

	For each fixed $x>0$,
	$f_n(x)\sim\frac{1}{n^2x}\to0$,
	so the series $\sum f_n(x)$ converges pointwise and absolutely.
	At $x=0$, $f_n(0)=0$.

	However, as $x\to0$, the bound $\frac{1}{n^2x}$ blows up,
	so convergence is not uniform on $[0,1]$.
	It is uniform on every subinterval $[\delta,1]$, $\delta>0$.

	\textit{Conclusion:}
	Pointwise and absolute convergence, uniform on $[\delta,1]$ but not on $[0,1]$.

	\medskip

	\textbf{(c)} $f_n(x)=(-1)^n\dfrac{x^n}{n}$ on $[0,1]$.

	For $x\in[0,1)$,
	\[
	\sum_{n=1}^\infty f_n(x)
	=\sum_{n=1}^\infty (-1)^n\frac{x^n}{n}
	=\ln(1+x)-x,
	\]
	which converges for all $x\in[0,1)$ and also at $x=1$ (to $-\ln2$).
	By the Leibniz criterion, the convergence is uniform on $[0,1]$.

	The absolute series $\sum |f_n(x)|=\sum x^n/n$
	diverges at $x=1$ but converges for $x<1$.
	Thus the convergence is not uniformly absolute.

	\textit{Conclusion:}
	Uniformly convergent on $[0,1]$,
	pointwise absolutely convergent for $x<1$ but not uniformly absolute.


	\textbf{Summary.}
	\[
	\begin{array}{lcccc}
		\toprule
		\text{Case} & \text{Pointwise} & \text{Uniform} & \text{Absolute} & \text{Uniform absolute}\\
		\midrule
		(a)~x e^{-nx} & \checkmark & \text{on compacts} & \checkmark & \times\\
		(b)~\dfrac{n^2x}{1+n^4x^2} & \checkmark & [\delta,1] & \checkmark & \times\\
		(c)~(-1)^n\dfrac{x^n}{n} & \checkmark & \checkmark & \text{for }x<1 & \times\\
		\bottomrule
	\end{array}
	\]

	\par\medskip\noindent\textbf{Sequences vs Series of Functions — Definitions}\par

	\textbf{Sequences of functions.}
	Let $X$ be a set and $Y$ a metric space (e.g.\ $\mathbb{R}$). A sequence of functions is a list
	$(f_n)_{n\ge1}$ with $f_n:X\to Y$.

		\par\noindent\textbullet\quad \emph{Pointwise convergence:} $f_n\to f$ on $X$ if $\lim_{n\to\infty} f_n(x)=f(x)$ for every $x\in X$.
		\par\noindent\textbullet\quad \emph{Uniform convergence:} $f_n\to f$ uniformly on $X$ if
		\[
		\sup_{x\in X}|f_n(x)-f(x)|\xrightarrow[n\to\infty]{}0.
		\]
		\par\noindent\textbullet\quad \emph{Uniform Cauchy:} $(f_n)$ is uniformly Cauchy if
		$\sup_{x\in X}|f_m(x)-f_n(x)|\to0$ as $m,n\to\infty$.
		If $Y$ is complete, this is equivalent to uniform convergence.


	\textbf{Series of functions.}
	Given $(f_n)$, define partial sums $S_N(x)=\sum_{n=1}^N f_n(x)$.
	The series $\sum_{n=1}^\infty f_n$ \emph{converges pointwise} to $S$ if $S_N(x)\to S(x)$ for all $x\in X$.
	It \emph{converges uniformly} if $\sup_{x\in X}|S_N(x)-S(x)|\to0$.

		\par\noindent\textbullet\quad \emph{Pointwise absolute convergence:} $\sum |f_n(x)|$ converges for each $x$.
		\par\noindent\textbullet\quad \emph{Uniform absolute convergence:} $\sum \|f_n\|_\infty<\infty$.
		(By the Weierstrass M-test, this implies uniform convergence of $\sum f_n$.)


	\textbf{Examples.}

		\par\noindent\textbullet\quad \emph{Sequence only.} $f_n(x)=x^n$ on $[0,1]$: $f_n\to \mathbf{1}_{\{1\}}$ pointwise, not uniformly.
		\par\noindent\textbullet\quad \emph{Series.} $f_n(x)=(-1)^n x^n/n$ on $[0,1]$:
		$\sum f_n$ converges uniformly (alternating test),
		but not absolutely at $x=1$ since $\sum |f_n(1)|=\sum 1/n$ diverges.

	\textbf{Remark.} A series of functions $\sum f_n$ converges iff its partial sums
	$(S_N)$ (a \emph{sequence of functions}) converge.
	\par\medskip\noindent\textbf{Problem 15 — The series $\sum_{n=1}^{\infty}(x-n)^{-2}$ on $X=\mathbb{R}\setminus\mathbb{N}$}\par
```

## CP-II-0348

- chapter line: 17447

```tex
\label{prob:cp-ii-0348}
\par\noindent\textbullet\quad \textbf{Dual of the completion.}
		If $\overline{X}$ is the completion of $X$, the restriction
		$J:\overline{X}'\to X'$, $J(\Phi)=\Phi|_X$, is an isometric isomorphism.
		(Hahn--Banach provides an isometric extension $\widetilde\Lambda$ of each $\Lambda\in X'$;
		density of $X$ in $\overline{X}$ yields uniqueness.)

	Consider the set of all pairs $(Z,g)$ where $Y\subset Z\subset X$, $g:Z\to\mathbb K$ is linear,
	$g|_Y=f$, and $\|g\|=\|f\|$, ordered by extension. Zorn's lemma gives a maximal element $(Z_*,g_*)$.
	If $Z_*\neq X$, pick $x_0\in X\setminus Z_*$ and extend $g_*$ to $\operatorname{span}(Z_*\cup\{x_0\})$
	with the same norm (possible by a one-step extension inequality). This contradicts maximality;
	hence $Z_*=X$ and $g_*$ is the desired extension.

	\section*{Exercise 3 — Decomposing a bounded functional on $L^{p}$}

	Let $u:L^{p}(\mathbb{R}^{n};\mathbb{R})\to\mathbb{R}$ be bounded and linear. For $f\ge0$ define
	\[
	\tilde u(f):=\sup\{\,u(g):\ g\in L^{p}(\mathbb{R}^{n}),\ 0\le g\le f\,\}.
	\]

 \vspace{1em}

\noindent\textbf{Bounds.}\quad
Since $g\equiv 0$ is admissible, we have $0 \le \tilde u(f)$.
Moreover, whenever $0 \le g \le f$ one has $\|g\|_{p} \le \|f\|_{p}$, hence
\[
\tilde u(f)
\;=\; \sup_{0 \le g \le f} u(g)
\;\le\; \sup_{0 \le g \le f} \|u\|\,\|g\|_{p}
\;\le\; \|u\|\,\|f\|_{p}.
\]
Also, if $f \ge 0$ then $g=f$ is admissible, and therefore $u(f) \le \tilde u(f)$.

\medskip

\noindent\textbf{Additivity on the positive cone and positive homogeneity.}\quad
If $f,g \ge 0$ and $a>0$, then
\[
\tilde u(f+ a g) \;=\; \tilde u(f) \;+\; a\,\tilde u(g).
\]

\noindent\emph{Proof idea.}\;
Let $0 \le h \le f + a g$ and set
\[
r := h \wedge f, \qquad s := \frac{h - r}{a}.
\]
Then
\[
0 \le r \le f, \qquad 0 \le s \le g, \qquad h = r + a s.
\]
By linearity of $u$,
\[
u(h) \;=\; u(r) + a\,u(s)
\;\le\; \tilde u(f) + a\,\tilde u(g).
\]
Taking the supremum over such $h$ gives
\[
\tilde u(f + a g) \;\le\; \tilde u(f) + a\,\tilde u(g).
\]
For the reverse inequality, fix $\varepsilon>0$ and choose $r,s \ge 0$ with
$r \le f$, $s \le g$ and
\[
u(r) \ge \tilde u(f) - \varepsilon, \qquad
u(s) \ge \tilde u(g) - \varepsilon.
\]
Then $r + a s \le f + a g$ and
\[
u(r + a s) \;=\; u(r) + a\,u(s)
\;\ge\; \tilde u(f) + a\,\tilde u(g) - 2\varepsilon.
\]
Taking the supremum over $h$ and letting $\varepsilon \downarrow 0$ yields the opposite
inequality, hence equality.

\bigskip

 \vspace{1em}

\noindent
Let $f^{+} := \max\{0,f\}$ and $f^{-} := \max\{0,-f\}$. Define
\[
w(f) \;:=\; \tilde u(f^{+}) \;-\; \tilde u(f^{-}).
\]

\medskip

\noindent\textbf{Positivity.}\quad
If $f \ge 0$, then $w(f) = \tilde u(f) \ge 0$.
Also
\[
w(f) - u(f) \;=\; \tilde u(f) - u(f) \;\ge\; 0
\qquad (f \ge 0).
\]
Hence both $w$ and $w-u$ are positive linear functionals.

\medskip

\noindent\textbf{Linearity.}\quad
For arbitrary $f,g$ write $f=f^{+}-f^{-}$ and $g=g^{+}-g^{-}$ and set
\[
A := f^{+}+g^{+} \ge 0, \qquad B := f^{-}+g^{-} \ge 0.
\]
Then $A-B=f+g$, and one can express $A$ and $B$ as
\[
A = (f+g)^{+} + r, \qquad B = (f+g)^{-} + r
\]
for some $r \ge 0$ (take $r := \tfrac12(A+B-|f+g|)$ pointwise).
Using additivity of $\tilde u$ on the positive cone,
\[
\tilde u(A) - \tilde u(B)
= \tilde u\big((f+g)^{+}\big) - \tilde u\big((f+g)^{-}\big)
= w(f+g).
\]
But also
\[
\tilde u(A) - \tilde u(B)
= \big(\tilde u(f^{+}) - \tilde u(f^{-})\big)
+ \big(\tilde u(g^{+}) - \tilde u(g^{-})\big)
= w(f) + w(g).
\]
Hence $w(f+g)=w(f)+w(g)$. Homogeneity follows similarly from the homogeneity of $\tilde u$
on the positive cone.

\medskip

\noindent\textbf{Boundedness.}\quad
From part (a),
\[
|w(f)|
\;\le\; \tilde u(f^{+}) + \tilde u(f^{-})
\;\le\; \|u\|\,\big(\|f^{+}\|_{p} + \|f^{-}\|_{p}\big)
\;\le\; 2\,\|u\|\,\|f\|_{p}.
\]
Thus $w$ is bounded on $L^{p}$.

	From (b), $w$ and $w-u$ are positive bounded linear functionals. Thus
	\[
	u=w-(w-u)=:u_{+}-u_{-},
	\]
	with $u_{\pm}$ positive bounded linear functionals on $L^{p}$.


	\bigskip
```

## CP-II-0351

- chapter line: 17653

```tex
\label{prob:cp-ii-0351}
\par\noindent\textbullet\quad $F$ is \emph{upper semicontinuous (u.s.c.) at $x$} if
		$\displaystyle \limsup_{x'\to x} F(x') \le F(x)$, i.e.\ each superlevel
		$\{F\ge \alpha\}$ is closed (hypograph is closed).
```

## CP-II-0352

- chapter line: 17660

```tex
\label{prob:cp-ii-0352}
\par\noindent\textbullet\quad the Ă˘â‚¬Ĺ›mixedĂ˘â‚¬ĹĄ case cannot occur, because $\lvert x-y\rvert<1$ forbids one point $\ge R+1$
	and the other $<R$.

Thus $f$ is uniformly continuous on $[0,\infty)$.
```

## CP-II-0356

- chapter line: 17711

```tex
\label{prob:cp-ii-0356}
\par\noindent\textbullet\quad Take \(X=(0,1]\subset Y\).
```

## CP-II-0360

- chapter line: 17916

```tex
\label{prob:cp-ii-0360}
Convolution with a regular distribution.

Let $T=T_f$ where $f\in L^1_{\mathrm{loc}}$. Then
\[
(T_f*\phi)(x)
= \int_{\mathbb{R}} f(y)\,\phi(x-y)\,dy,
\]
which is the classical convolution.
```

## CP-II-0361

- chapter line: 17928

```tex
\label{prob:cp-ii-0361}
\par\noindent\textbullet\quad Show that $T_{K_\varepsilon} \to T_{K_t}$ in $\mathscr{S}'$ as $\varepsilon\to0$.
```

## CP-II-0364

- chapter line: 17973

```tex
\label{prob:cp-ii-0364}
\par\noindent\textbullet\quad The norm $x\mapsto\|x\|$ is \emph{weakly l.s.c.}: if $x_n\rightharpoonup x$ in $X$ then
		$\|x\|\le \liminf_n \|x_n\|$. In particular, for Hilbert spaces,
		\[
		\|x\|^2 \le \liminf_{n\to\infty}\|x_n\|^2
		\quad\text{whenever } x_n\rightharpoonup x .
		\]
```

## CP-II-0366

- chapter line: 17983

```tex
\label{prob:cp-ii-0366}
— Gibbs Phenomenon for a Square Wave

Suppose $f:\mathbb{R}\to\mathbb{R}$ is given by
\[
f(x) =
\begin{cases}
	-1, & -\tfrac12 \le x \le 0,\\[0.3em]
	1, & 0 < x \le \tfrac12,
\end{cases}
\qquad\text{and}\qquad
f(x+1) = f(x)\ \text{for all }x\in\mathbb{R}.
\]

Show that
\[
f(x)
= \frac{1}{\pi i}\sum_{n=-\infty}^{\infty}
\frac{2}{2n+1} e^{2\pi i (2n+1)x}
= \frac{4}{\pi}\sum_{n=0}^{\infty}
\frac{1}{2n+1}\,\sin\bigl(2\pi(2n+1)x\bigr),
\]
with convergence in $L^2_{\mathrm{loc}}(\mathbb{R})$.

Define the partial sums
\[
S_N(x)
:= 8 \sum_{n=0}^{N-1} \frac{1}{2\pi(2n+1)}
\sin\bigl(2\pi(2n+1)x\bigr).
\]

Show that
\[
S_N(x)
= 8 \int_0^x \sum_{n=0}^{N-1}
\cos\bigl(2\pi(2n+1)t\bigr)\,dt.
\]

Show that
\[
\cos\bigl(2\pi(2n+1)t\bigr)\,\sin(2\pi t)
= \frac12\Bigl(\sin\bigl(2\pi(2n+2)t\bigr)
- \sin(4\pi n t)\Bigr),
\]
and deduce that
\[
S_N(x)
= 8 \int_0^x
\frac{\sin(4\pi N t)}{2\sin(2\pi t)}\,dt.
\]

Show that the first local maximum of $S_N$ occurs at
$x = \tfrac{1}{4N}$, and that
\[
S_N\!\left(\frac{1}{4N}\right)
\;\ge\;
8\int_0^{1/N} \frac{\sin(4\pi N t)}{4\pi t}\,dt
= \frac{2}{\pi}\int_0^{\pi} \frac{\sin s}{s}\,ds
\simeq 1.179\ldots
\]

Conclude that the Fourier series in part (a) does not converge
uniformly.  This lack of uniform convergence of a Fourier series at a
point of discontinuity is known as the \emph{Gibbs phenomenon}.
```

## CP-II-0369

- chapter line: 18078

```tex
\label{prob:cp-ii-0369}
\par\noindent\textbullet\quad If $|x|>2$, then the supports of $y\mapsto f(x-y)$ and $y\mapsto g(y)$
	do not overlap, so $(f*g)(x)=0$.
```

## CP-II-0370

- chapter line: 18084

```tex
\label{prob:cp-ii-0370}
Geometric series of functions

$f_i(x) = \dfrac{x^i}{2^i}$ on $[0,1]$.
Since $|f_i(x)| \le 1/2^i$ and $\sum 1/2^i < \infty$, the M-test applies.

\[
\sum_{i=0}^\infty f_i(x) = \frac{1}{1-\tfrac{x}{2}}, \quad x\in[0,1].
\]

---
```

## CP-II-0376

- chapter line: 18118

```tex
\label{prob:cp-ii-0376}
(strong separation in $\ell^2$)

\noindent\textbf{Setup.}
	$X=\ell^2$, let $e_1=(1,0,0,\dots)$ and $e_2=(0,1,0,\dots)$.
	\[
	M=\mathrm{span}\{e_1\}=\{t e_1:t\in\mathbb R\},\qquad
	K=B\!\left(e_2,\tfrac12\right)=\{x\in\ell^2:\|x-e_2\|_2<\tfrac12\}.
	\]

	\noindent\textbf{(i) Disjointness.}
	Since $\mathrm{dist}(e_2,M)=\|e_2\|_2=1$, we have $K\cap M=\varnothing$.

	\noindent\textbf{(ii) Functional vanishing on $M$.}
	Define $\Lambda(x)=\langle x,e_2\rangle$ (continuous linear functional via Riesz).
	Then $\Lambda|_M\equiv 0$ because $e_2\perp e_1$.

	\noindent\textbf{(iii) Lower bound on $K$.}
	For $x\in K$, write $x=e_2+(x-e_2)$ and compute
	\[
	\Lambda(x)=\langle x,e_2\rangle
	=\langle e_2,e_2\rangle+\langle x-e_2,e_2\rangle
	=1+\langle x-e_2,e_2\rangle.
	\]
	By Cauchy--Schwarz, $|\langle x-e_2,e_2\rangle|\le \|x-e_2\|_2\|e_2\|_2<\tfrac12$,
	hence $\Lambda(x)>\tfrac12$.
	Therefore $\inf_{x\in K}\Lambda(x)\ge \tfrac12>0$ while $\Lambda(M)=\{0\}$.

	\noindent\textbf{(iv) Separation and hyperplane.}
	With $\alpha=0$ we have $\Re\Lambda(m)\le 0<\inf_{k\in K}\Re\Lambda(k)$.
	Let $N=\ker\Lambda=\{x\in\ell^2:\langle x,e_2\rangle=0\}=e_2^\perp$.
	Then $M\subset N$ and $N\cap K=\varnothing$, so $N$ gives the required codimension-one separation.
```

## CP-II-0379

- chapter line: 18176

```tex
\label{prob:cp-ii-0379}
(strong separation in $\mathbb R^2$)

\noindent\textbf{Setup.}
	$X=\mathbb R^2$,
	\[
	K=B\big((0,1),1\big)=\{(x,y):x^2+(y-1)^2<1\},\qquad
	M=\{(t,0):t\in\mathbb R\}.
	\]

	\noindent\textbf{(i) Assumptions.}
	$K$ is open and convex, $M$ is a closed subspace, and $K\cap M=\varnothing$
	(because $x^2+(0-1)^2=x^2+1<1$ is impossible).

	\noindent\textbf{(ii) Functional.}
	Define $\Lambda:\mathbb R^2\to\mathbb R$ by $\Lambda(x,y)=y$.

	\noindent\textbf{(iii) Values on $M$ and $K$.}
	For $(t,0)\in M$, $\Lambda(t,0)=0$, hence $\Lambda(M)=\{0\}$.
	If $(x,y)\in K$, then $x^2+(y-1)^2<1$, so $|y-1|<1$, i.e.\ $0<y<2$.
	Thus $\Lambda(K)=(0,2)$.

	\noindent\textbf{(iv) Separation and hyperplane.}
	With $\alpha=0$ we have $\Re\Lambda(m)\le 0<\inf_{k\in K}\Re\Lambda(k)$.
	Let $N=\ker\Lambda=\{(x,y):y=0\}=M$.
	Then $M\subset N$ and $N\cap K=\varnothing$, yielding a strict separation by a codimension-one subspace.

	\bigskip
```

## CP-II-0380

- chapter line: 18207

```tex
\label{prob:cp-ii-0380}
(Power cusp on a bounded interval).

Let $f(x)=|x|^\beta \chi_{[-1,1]}(x)$ with $\beta>-1/2$ (so $f\in L^2$). Then
\[
f\in H^s((-1,1)) \quad\Longleftrightarrow\quad s<\beta+\tfrac12.
\]
Indeed, near $0$,
\[
\iint_{(0,1)^2}\frac{|x^\beta-y^\beta|^2}{|x-y|^{1+2s}}\,dx\,dy<\infty
\iff s<\beta+\tfrac12,
\]
and outside a neighbourhood of $0$ the integrand is smooth. A Fourier-tail argument gives the same threshold.

\bigskip

On $\mathbb T$, for $u_m(x)=\sin(2\pi m x)$ one has
\(
\|u_m\|_{H^s(\mathbb T)}\asymp (1+m^2)^{s/2},
\)
which exhibits directly the frequency weight $(1+|m|^2)^{s/2}$.
```

## CP-II-0381

- chapter line: 18231

```tex
\label{prob:cp-ii-0381}
On $(0,1)$, for any $\varepsilon>0$ let
	\[
	f_\varepsilon(x)=x^{-1/p}\,(\log\tfrac{e}{x})^{-1/p-\varepsilon}.
	\]
	Then $f_\varepsilon\in L^p(0,1)$
	(the $x^{-1}$ singularity is softened by the log),
	so $f_\varepsilon\in L^{p,\infty}(0,1)$ as well.
	This shows that $L^p$ can be strictly smaller
	than borderline families living only in $L^{p,\infty}$.
```

## CP-II-0382

- chapter line: 18244

```tex
\label{prob:cp-ii-0382}
\par\noindent\textbullet\quad The inequality
	\[
	ab \le \frac{a^p}{p} + \frac{b^q}{q}
	\]
	is equivalent (since $\log$ is increasing) to the statement
	\[
	\log(ab) \;\le\;
	\log\!\left(\frac{a^p}{p} + \frac{b^q}{q}\right).
	\]
```

## CP-II-0384

- chapter line: 18257

```tex
\label{prob:cp-ii-0384}
{Construct explicit polynomials $p_n\to 1/z$ on the right semicircle}{poly-1-over-z-semicircle}
	Let
	\[
	K:=\{z\in\mathbb C:\ |z|=1,\ \Re z\ge 0\}.
	\]
	Construct polynomials $p_n$ such that $p_n\to 1/z$ uniformly on $K$.
```

## CP-II-0385

- chapter line: 18267

```tex
\label{prob:cp-ii-0385}
\par\noindent (a)\quad Suppose $\phi\in\mathcal{S}$.  Let $\{x_l\}_{l=1}^\infty
	\subset\mathbb{R}^n$ be a sequence with $x_l\to 0$.
	Show that
	\[
	\tau_{x_l}\phi \to \phi, \qquad \text{as } l\to\infty,
	\]
	in $\mathcal{S}$, where $\tau_x$ is the translation
	operator defined in equation~(1.2).

	\par\noindent (b)\quad Suppose $\phi\in\mathcal{S}$, show that
	\[
	\Delta_i^h \phi \to D_i\phi, \qquad \text{as } h\to 0,
	\]
	in $\mathcal{S}$, where $\Delta_i^h$ is the difference
	quotient defined in Example~2.
```

## CP-II-0386

- chapter line: 18286

```tex
\label{prob:cp-ii-0386}
$f_n(x)=x/n$ on $[0,1]$ (Equicontinuous, converges uniformly to 0)

---
```

## CP-II-0387

- chapter line: 18293

```tex
\label{prob:cp-ii-0387}
\par\noindent\textbullet\quad The improper integral
	\[
	\int_1^\infty e^{-u}\,du = [-e^{-u}]_1^\infty = e^{-1}
	\]
	converges.

	\par\noindent\textbullet\quad For $R>1$,
	\[
	\int_1^R e^{-u^2}\,du \leq \int_1^R e^{-u}\,du <\infty,
	\]
	so $\int_1^\infty e^{-u^2}\,du$ converges. By symmetry the whole integral
	\[
	I=\int_{-\infty}^\infty e^{-u^2}\,du
	\]
	converges.

	\par\noindent\textbullet\quad For $f\geq 0$, with $S_R=[-R,R]\times[-R,R]$ and $B_R(0)$ the disk,
	\[
	\int_{B_R(0)} f \leq \int_{S_R} f \leq \int_{B_{\sqrt{2}R}(0)} f,
	\]
	since $B_R(0)\subset S_R \subset B_{\sqrt{2}R}(0)$.

	\par\noindent\textbullet\quad For $f(u,v)=e^{-(u^2+v^2)}$,
	\[
	\iint_{\mathbb{R}^2} e^{-(u^2+v^2)}\,dudv = \left(\int_{-\infty}^\infty e^{-u^2}\,du\right)^2=I^2.
	\]
	In polar coordinates,
	\[
	\iint_{\mathbb{R}^2} e^{-(u^2+v^2)}\,dudv
	= \int_0^{2\pi}\int_0^\infty e^{-r^2}r\,drd\theta
	=2\pi\cdot \tfrac{1}{2}\int_0^\infty e^{-t}\,dt = \pi.
	\]
	So $I^2=\pi$.

	\par\noindent\textbullet\quad Therefore
	\[
	I=\sqrt{\pi}.
	\]
```

## CP-II-0388

- chapter line: 18335

```tex
\label{prob:cp-ii-0388}
\par\noindent\textbullet\quad In $L^p[0,1]$ let $f_j=(-1)^j$. Then $\int_{[0,1]} f_j$ does not converge, so no weak limit exists.

	On a $\sigma$-finite measure space $(\Omega,\mathcal F,\mu)$, the weak topology on $L^{p}(\Omega)$
	is the locally convex topology $\sigma(L^{p},L^{p'})$ generated by the linear functionals
	\[
	T_h(f) := \int_\Omega f\,h\,d\mu \qquad (h\in L^{p'}(\Omega)).
	\]
	Thus $f_j \rightharpoonup f$ in $L^{p}$ iff $\int f_j h \to \int f h$ for every $h\in L^{p'}$.
```

## CP-II-0389

- chapter line: 18347

```tex
\label{prob:cp-ii-0389}
\par\noindent\textbullet\quad $f=\mathbf 1_{[0,1)}=\tfrac12(\mathbf 1_{[0,1/2)}+\mathbf 1_{[1/2,1)})$ has a finite Haar expansion on level $n=0,1$.
```

## CP-II-0390

- chapter line: 18352

```tex
\label{prob:cp-ii-0390}
— A meromorphic function and a Fourier series

Fix $\theta\in[0,2\pi]$ and consider the meromorphic function
\[
F(z) = \frac{1}{1+z^2}\,\frac{\cos\bigl((\pi-\theta)z\bigr)}{2\sin(\pi z)}.
\]
```

## CP-II-0392

- chapter line: 18362

```tex
\label{prob:cp-ii-0392}
Averaging window.

Let
\[
g(t) = \frac{1}{2h}\,1_{[-h,h]}(t).
\]
Then
\[
(f*g)(x)
= \frac{1}{2h} \int_{x-h}^{x+h} f(t)\,dt,
\]
which is just the \emph{average} of $f$ around $x$ over an interval of
length $2h$.

\medskip
\noindent$\Rightarrow$ \emph{Smoothing:} local averaging of the signal.

\bigskip\hrule\bigskip
```

## CP-II-0394

- chapter line: 18384

```tex
\label{prob:cp-ii-0394}
\par\noindent\textbullet\quad $f(x,y)=|x|+|y|$ is separately Lipschitz and globally continuous.

\hfill$\Box$
```

## CP-II-0397

- chapter line: 18391

```tex
\label{prob:cp-ii-0397}
$f_n(x)=x/n$ on $[0,1]$ (Equicontinuous)

---
```

## CP-II-0398

- chapter line: 18398

```tex
\label{prob:cp-ii-0398}
Suppose $A\subset\mathbb{R}^n$ and let $(f_i)_{i=0}^\infty$ with $f_i:A\to\mathbb{R}^m$ be a sequence of functions.
Assume $f_i\to f$ \emph{uniformly} on $A$. Show that if $B\subset A$, then $f_i\to f$ uniformly on $B$.

\textit{Solution.} By uniform convergence on $A$, for every $\varepsilon>0$ there exists $N\in\mathbb{N}$ such that
for all $i\ge N$ and all $x\in A$ we have $\|f_i(x)-f(x)\|<\varepsilon$. Since $B\subset A$, this inequality holds
for all $x\in B$ as well, with the \emph{same} $N$. Hence $f_i\to f$ uniformly on $B$. Equivalently,
\[
\sup_{x\in B}\|f_i(x)-f(x)\|\le \sup_{x\in A}\|f_i(x)-f(x)\|\xrightarrow{i\to\infty} 0.
\]
```

## CP-II-0399

- chapter line: 18411

```tex
\label{prob:cp-ii-0399}
\par\noindent\textbullet\quad Symmetrically, $\mathrm{id}:(X,\rho)\to(X,\tau)$ is continuous iff $\tau\subseteq\rho$.

\bigskip
```

## CP-II-0402

- chapter line: 18480

```tex
\label{prob:cp-ii-0402}
\par\noindent\textbullet\quad Start with \(Y=\mathbb{R}\) equipped with the usual metric \(|\cdot|\).
```

## CP-II-0403

- chapter line: 18485

```tex
\label{prob:cp-ii-0403}
Let $q\geq 2$ and $n\geq 1$. Define
\[
\mathcal{G}(\{x_1,\dots,x_q\}, \{y_1,\dots,y_q\})
= \inf \left\{ \Big(\sum_{j=1}^q |y_j - x_{\sigma(j)}|^2 \Big)^{1/2} : \sigma \text{ a permutation} \right\}.
\]

\subsection*{(i) $\mathcal{G}$ is a metric.}

	\par\noindent\textbullet\quad Non-negativity: sums of squares are nonnegative.
	\par\noindent\textbullet\quad Identity: $\mathcal{G}(X,Y)=0$ iff $X=Y$ as multisets.
	\par\noindent\textbullet\quad Symmetry: follows since $|y_j-x_{\sigma(j)}|=|x_{\sigma(j)}-y_j|$.
	\par\noindent\textbullet\quad Triangle inequality: For $X,Y,Z$, by MinkowskiĂ˘â‚¬â„˘s inequality,
	\[
	\Big(\sum_j |x_{\sigma(j)}-z_j|^2\Big)^{1/2}
	\leq \Big(\sum_j |x_{\sigma(j)}-y_{\tau(j)}|^2\Big)^{1/2} + \Big(\sum_j |y_{\tau(j)}-z_j|^2\Big)^{1/2}.
	\]
	Taking infima over permutations $\sigma,\tau$ proves the inequality.

Hence $\mathcal{G}$ is a metric on $Q$.

If $x_1\leq \dots \leq x_q$ and $y_1\leq \dots \leq y_q$, then by the rearrangement inequality the permutation minimizing
\[
\sum_{j=1}^q (x_{\sigma(j)}-y_j)^2
\]
is the identity permutation. Hence
\[
\mathcal{G}(\{x_1,\dots,x_q\}, \{y_1,\dots,y_q\})
= \Big(\sum_{j=1}^q (x_j-y_j)^2\Big)^{1/2}.
\]

	\par\noindent\textbullet\quad $X=\{0,1\}, Y=\{2,3\}$: $\mathcal{G}(X,Y)=\sqrt{8}$.
	\par\noindent\textbullet\quad $X=\{0,2\}, Y=\{1,3\}$: $\mathcal{G}(X,Y)=\sqrt{2}$.
```

## CP-II-0404

- chapter line: 18523

```tex
\label{prob:cp-ii-0404}
— Gibbs Phenomenon for a Square Wave

Suppose $f:\mathbb{R}\to\mathbb{R}$ is given by
\[
f(x) =
\begin{cases}
	-1, & -\tfrac12 \le x \le 0,\\[0.3em]
	1, & 0 < x \le \tfrac12,
\end{cases}
\qquad\text{and}\qquad
f(x+1) = f(x)\ \text{for all }x\in\mathbb{R}.
\]

\bigskip
\noindent\textbf{Theoretical background.}
The function $f$ is $1$-periodic, odd, and has jump discontinuities at
all half-integers.  For a $1$-periodic integrable function $f$, the
complex Fourier coefficients are
\[
\widehat f(k) = \int_{-1/2}^{1/2} f(x)e^{-2\pi i k x}\,dx,
\qquad k\in\mathbb{Z},
\]
and one formally has
\[
f(x) \sim \sum_{k\in\mathbb{Z}} \widehat f(k)e^{2\pi i k x}.
\]
Because $f$ is odd, only sine terms (and hence only odd harmonics)
appear in the real Fourier series.  Dirichlet's theorem implies that
the Fourier series converges to $f(x)$ at points of continuity, and to
the midpoint of the jump at discontinuities.  However, the convergence
is not uniform near a jump: the partial sums exhibit a persistent
overshoot known as the \emph{Gibbs phenomenon}.  This exercise
quantifies that overshoot for the square wave $f$.

\bigskip

We compute the complex Fourier coefficients
\[
\widehat f(k) = \int_{-1/2}^{1/2} f(x)e^{-2\pi i k x}\,dx.
\]
Since $f$ is odd, $\widehat f(k)=0$ for all even $k$.  For $k=2n+1$ we
have
\[
\widehat f(2n+1)
= \int_{-1/2}^{1/2} f(x)e^{-2\pi i (2n+1)x}\,dx
= \frac{2}{\pi i(2n+1)}.
\]
Therefore
\[
f(x)
= \sum_{n\in\mathbb{Z}} \widehat f(2n+1)e^{2\pi i(2n+1)x}
= \frac{1}{\pi i}\sum_{n=-\infty}^{\infty}
\frac{2}{2n+1}e^{2\pi i(2n+1)x}.
\]
Grouping conjugate terms and passing to the real sine series, we obtain
\[
f(x)
= \frac{4}{\pi}\sum_{n=0}^{\infty}
\frac{1}{2n+1}\,\sin\bigl(2\pi(2n+1)x\bigr),
\]
with convergence in $L^2([-1/2,1/2])$ and hence in
$L^2_{\mathrm{loc}}(\mathbb{R})$.

Define the partial sums
\[
S_N(x)
:= \frac{4}{\pi}\sum_{n=0}^{N-1}\frac{1}{2n+1}
\sin\bigl(2\pi(2n+1)x\bigr)
= 8\sum_{n=0}^{N-1} \frac{1}{2\pi(2n+1)}
\sin\bigl(2\pi(2n+1)x\bigr).
\]

\bigskip

Using
\[
\frac{d}{dt}\sin\bigl(2\pi(2n+1)t\bigr)
= 2\pi(2n+1)\cos\bigl(2\pi(2n+1)t\bigr),
\]
we write
\[
\sin\bigl(2\pi(2n+1)x\bigr)
= \int_0^x 2\pi(2n+1)
\cos\bigl(2\pi(2n+1)t\bigr)\,dt,
\]
and hence
\[
\frac{1}{2\pi(2n+1)}\sin\bigl(2\pi(2n+1)x\bigr)
= \int_0^x \cos\bigl(2\pi(2n+1)t\bigr)\,dt.
\]
Summing over $n$ gives
\[
S_N(x)
= 8\sum_{n=0}^{N-1}\int_0^x
\cos\bigl(2\pi(2n+1)t\bigr)\,dt
= 8\int_0^x \sum_{n=0}^{N-1}
\cos\bigl(2\pi(2n+1)t\bigr)\,dt.
\]

\bigskip

Recall the identity
\[
2\cos A\sin B = \sin(A+B)-\sin(A-B).
\]
Setting $A=2\pi(2n+1)t$, $B=2\pi t$, we find
\[
\cos\bigl(2\pi(2n+1)t\bigr)\sin(2\pi t)
= \frac12\Bigl(\sin\bigl(2\pi(2n+2)t\bigr)
-\sin(4\pi n t)\Bigr).
\]
Thus
\[
\sum_{n=0}^{N-1}\cos\bigl(2\pi(2n+1)t\bigr)
= \frac{1}{2\sin(2\pi t)}
\sum_{n=0}^{N-1}
\Bigl(\sin\bigl(2\pi(2n+2)t\bigr)
-\sin(4\pi n t)\Bigr).
\]
The sum on the right is telescoping and simplifies to $\sin(4\pi N t)$,
whence
\[
\sum_{n=0}^{N-1}\cos\bigl(2\pi(2n+1)t\bigr)
= \frac{\sin(4\pi N t)}{2\sin(2\pi t)}.
\]
Substituting this back into the formula in part~(b) yields
\[
S_N(x)
= 8\int_0^x \frac{\sin(4\pi N t)}{2\sin(2\pi t)}\,dt.
\]

\bigskip

Differentiating $S_N$ gives
\[
S_N'(x)
= 8\sum_{n=0}^{N-1}\cos\bigl(2\pi(2n+1)x\bigr)
= 4\,\frac{\sin(4\pi N x)}{\sin(2\pi x)}.
\]
Critical points occur when $\sin(4\pi N x)=0$ and $x\notin\mathbb{Z}$.
Near $x=0$ the first such zero is at $x=\tfrac{1}{4N}$; inspection of
the sign of $S_N'$ shows this is the first local maximum.

For small $t$ we have $\sin(2\pi t)\le 2\pi t$, hence
$2\sin(2\pi t)\le 4\pi t$ and so
\[
\frac{1}{2\sin(2\pi t)} \ge \frac{1}{4\pi t}.
\]
Thus
\[
S_N(x)
= 8\int_0^x \frac{\sin(4\pi N t)}{2\sin(2\pi t)}\,dt
\;\ge\;
8\int_0^x \frac{\sin(4\pi N t)}{4\pi t}\,dt.
\]
Taking $x=\tfrac{1}{4N}$ and substituting $s=4\pi N t$, so
$dt = \tfrac{ds}{4\pi N}$ and $s$ runs from $0$ to $\pi$, we obtain
\[
S_N\Bigl(\frac{1}{4N}\Bigr)
\ge 8\int_0^{1/(4N)} \frac{\sin(4\pi N t)}{4\pi t}\,dt
= \frac{2}{\pi}\int_0^{\pi} \frac{\sin s}{s}\,ds
\simeq 1.179\ldots
\]
for all $N$.

\bigskip

At the discontinuity $x=0$, Dirichlet's theorem implies that
\[
\lim_{N\to\infty} S_N(0)
= \frac{f(0^-)+f(0^+)}{2}
= 0.
\]
However, for $x_N = \tfrac{1}{4N}$ we have
\[
S_N(x_N) \gtrsim 1.179,
\]
while $f(x_N)\to 1$ as $N\to\infty$.  Hence
\[
\limsup_{N\to\infty}\sup_{x\in[-1/2,1/2]}
|S_N(x)-f(x)|
\ge \limsup_{N\to\infty}|S_N(x_N)-1|
\ge 1.179 - 1 > 0,
\]
so the Fourier series in part~(a) does \emph{not} converge uniformly on
any interval containing $0$.  This persistent overshoot near the jump is
the \emph{Gibbs phenomenon}.

\bigskip

Figure~\ref{fig:ex5-6-square-global} shows the global Fourier partial sums, while Figure~\ref{fig:ex5-6-square-gibbs} zooms in near $x=0$ to show the Gibbs overshoot.

\begin{figure}[htbp]
  \centering
  \includegraphics[width=0.90\linewidth]{figures/part02/ex5_6_square_global.png}
  \caption{Global view of the square-wave Fourier partial sums.}
  \label{fig:ex5-6-square-global}
\end{figure}

\begin{figure}[htbp]
  \centering
  \includegraphics[width=0.88\linewidth]{figures/part02/ex5_6_square_gibbs_zoom.png}
  \caption{Zoom near the jump at $x=0$, showing the persistent Gibbs overshoot.}
  \label{fig:ex5-6-square-gibbs}
\end{figure}

	\clearpage
```

## CP-II-0408

- chapter line: 18734

```tex
\label{prob:cp-ii-0408}
Pointwise but not uniform (Not Cauchy)

$f_n(x)=x^n$ on $[0,1]$.
Pointwise limit discontinuous, not uniform, not Cauchy in sup norm.

---
```

## CP-II-0409

- chapter line: 18744

```tex
\label{prob:cp-ii-0409}
Gaussian.

Let $F(x,y)=e^{-x^2-y^2}$ on $\mathbb{R}$.  Then
\[
\int_{\mathbb{R}}F(x,y)\,dy = \sqrt{\pi}\,e^{-x^2}.
\]
Hence
\[
\int_{\mathbb{R}} \Bigl|\int_{\mathbb{R}}F(x,y)\,dy\Bigr|dx
= \sqrt{\pi}\int_{\mathbb{R}} e^{-x^2}dx
= \pi.
\]
Since $F\ge 0$,
\[
\int_{\mathbb{R}}\int_{\mathbb{R}}|F(x,y)|\,dy\,dx
= \pi.
\]
```

## CP-II-0412

- chapter line: 18765

```tex
\label{prob:cp-ii-0412}
\par\noindent\textbullet\quad On $(\mathbb{R},\mathcal B)$ with $\mu=m$ (Lebesgue) and $\nu=m+\delta_0$, we have
		$\nu_a=m$ and $\nu_s=\delta_0$.
```

## CP-II-0414

- chapter line: 18771

```tex
\label{prob:cp-ii-0414}
\par\noindent\textbullet\quad Surface measure on a smooth embedded manifold $M\subset\mathbb{R}^n$ is a Radon Borel measure on $M$ (subspace topology).
```

## CP-II-0418

- chapter line: 18798

```tex
\label{prob:cp-ii-0418}
\par\noindent\textbullet\quad For every multi-index $\gamma$ and $1\le p<\infty$,
	\[
	x^\gamma D^\alpha f(x)\in L^p(\mathbb{R}^n),
	\]
	since we may take $N$ large enough to dominate the polynomial
	growth of $x^\gamma$.
```

## CP-II-0419

- chapter line: 18808

```tex
\label{prob:cp-ii-0419}
\par\noindent\textbullet\quad Deduce that
		\[
		\widehat{K_\varepsilon^t}(\xi)
		= \left(1+\frac{i4t}{\varepsilon}\right)^{-\tfrac{n}{2}}
		e^{-\, i t|\xi|^2/(1+4it\varepsilon)}.
		\]
```

## CP-II-0420

- chapter line: 18818

```tex
\label{prob:cp-ii-0420}
a step function

Let $H(x)=\mathbf{1}_{[1/2,\,1]}(x)$. Then
\[
B_n[H](x)=\sum_{k=\lceil n/2\rceil}^{n}\binom{n}{k}\,x^k(1-x)^{n-k}.
\]
One has
\[
B_n[H](x)\to
\begin{cases}
	0, & x<\tfrac{1}{2},\\[2pt]
	\tfrac12, & x=\tfrac{1}{2},\\[2pt]
	1, & x>\tfrac{1}{2},
\end{cases}
\qquad (n\to\infty).
\]
Hence $B_n[H]\to H$ pointwise at all continuity points of $H$, but not uniformly.
Moreover, for each $1\le p<\infty$,
\[
\|B_n[H]-H\|_{L^p([0,1])}\longrightarrow 0,
\]
so $H$ is approximable by polynomials in $L^p$.

\bigskip

Dropping uniform convergence allows polynomial approximation of discontinuous functions:
 \setlength{\itemsep}{0.6em}
	\par\noindent\textbullet\quad pointwise convergence at continuity points (e.g.\ Bernstein polynomials),
	\par\noindent\textbullet\quad $L^p$-convergence for every $1\le p<\infty$ (polynomials are dense in $L^p$),
	\par\noindent\textbullet\quad often almost-everywhere convergence for suitable subsequences.

Uniform convergence on the whole interval still fails for discontinuous $f$.

Let $(p_n)$ be polynomials on $[0,1]$ converging to $f$ (pointwise, or in $L^p$, $1\le p<\infty$).
If $f$ is not a polynomial, then necessarily $\deg p_n\to\infty$.

\smallskip

\noindent\textbf{Proof (pointwise case).}
Assume $\deg p_n\le m$ for all $n$. Let $\mathcal P_{\le m}$ be the space of polynomials of degree $\le m$.
Choose distinct nodes $x_0,\dots,x_m\in[0,1]$. The evaluation map
\[
T:\mathcal P_{\le m}\to\mathbb{R}^{m+1}, \qquad T(p)=(p(x_0),\dots,p(x_m))
\]
is a linear isomorphism. Since $p_n(x_j)\to f(x_j)$ for each $j$, we have $T(p_n)\to v:=(f(x_0),\dots,f(x_m))$.
Let $p:=T^{-1}(v)\in\mathcal P_{\le m}$. By Lagrange interpolation, for each $x$ there exists a linear functional
$L_x:\mathbb{R}^{m+1}\to\mathbb{R}$ with $p_n(x)=L_x\!\big(T(p_n)\big)$; hence
$p_n(x)\to L_x(v)=p(x)$. Therefore the pointwise limit $f$ equals $p$, a polynomial of degree $\le m$.
Contradiction. Thus $\deg p_n$ cannot be bounded; hence $\deg p_n\to\infty$.


\smallskip

\noindent\textbf{Remark (normed convergences).}
For convergence in any norm (e.g.\ $L^p$), the same conclusion holds since
$\mathcal P_{\le m}$ is finite-dimensional and therefore closed; a limit of $(p_n)$ with $\deg p_n\le m$
must lie in $\mathcal P_{\le m}$.
```

## CP-II-0422

- chapter line: 18913

```tex
\label{prob:cp-ii-0422}
\begin{lemma}[Mollifiers in $\mathcal{D}'(\mathbb{R}^n)$]
	Let $(\phi_\varepsilon)_{\varepsilon>0}\subset \mathcal{D}(\mathbb{R}^n)$
	be a standard approximate identity as in Theorem~1.13, and let
	$T\in\mathcal{D}'(\mathbb{R}^n)$ be a distribution. Define the
	convolution $\phi_\varepsilon * T$ by
	\[
	\langle \phi_\varepsilon * T, \psi\rangle
	:= \big\langle T, \check{\phi}_\varepsilon * \psi \big\rangle,
	\qquad \psi\in\mathcal{D}(\mathbb{R}^n),
	\]
	where $\check{\phi}_\varepsilon(x):=\phi_\varepsilon(-x)$. Then
	$\phi_\varepsilon * T \in C^\infty(\mathbb{R}^n)$ for every
	$\varepsilon>0$, and
	\[
	\phi_\varepsilon * T \longrightarrow T
	\qquad\text{in }\mathcal{D}'(\mathbb{R}^n)\text{ as }\varepsilon\to0.
	\]
\end{lemma}
```

## CP-II-0423

- chapter line: 18935

```tex
\label{prob:cp-ii-0423}
\hfill

		\par\noindent\textbullet\quad Uniform: $f_n(x)=\dfrac{x}{n+x}$ on $[0,1]$; then
		$\sup_{[0,1]}|f_n|=\frac{1}{n+1}\to0$, so $f_n\to0$ uniformly.
		\par\noindent\textbullet\quad Nonuniform: $f_n(x)=x^n$ on $[0,1]$; then $f_n\to f$ pointwise with
		$f=\mathbf 1_{\{1\}}$, but not uniformly, since
		$\sup_{x\in[0,1)}|x^n-0|=1$ for all $n$.
```

## CP-II-0427

- chapter line: 18964

```tex
\label{prob:cp-ii-0427}
— Fourier Series of the Sawtooth Function

Let
\[
f(x) = x \quad (|x|<\tfrac12),
\qquad f(x+1)=f(x).
\]

\bigskip
\noindent\textbf{Step 1: Complex Fourier coefficients}

For $1$-periodic $f$,
\[
\widehat f(n)
= \int_{-1/2}^{1/2} f(x)e^{-2\pi i n x}\,dx.
\]

For $n=0$:
\[
\widehat f(0)=0.
\]

For $n\neq 0$:
\[
\widehat f(n)
= \int_{-1/2}^{1/2} x e^{-2\pi i n x}\,dx
= \frac{i(-1)^n}{2\pi n}.
\]

Thus
\[
f(x)=\sum_{\substack{n\in\mathbb{Z}\\ n\ne 0}}
\frac{i(-1)^n}{2\pi n} e^{2\pi i n x}
\qquad\text{in } L^2_{\mathrm{loc}}.
\]

\bigskip
\noindent\textbf{Step 2: Real sine series}

Since $f$ is odd, only sine terms appear:
\[
f(x) = \sum_{n=1}^{\infty} b_n \sin(2\pi n x).
\]
Using $\widehat f(n)= -\frac{i}{2}b_n$ for $n>0$ gives
\[
b_n = \frac{2(-1)^{n+1}}{\pi n}.
\]

Therefore:
\[
f(x)
= \sum_{n=1}^{\infty}
\frac{(-1)^{n+1}}{n\pi}\,\sin(2\pi n x),
\qquad
\text{convergent in } L^2_{\mathrm{loc}}(\mathbb{R}).
\]

\clearpage

Figure~\ref{fig:ex5-3-weighted-comb} shows the weighted discrete ``$\delta$--comb'' supported at the points $x=2\pi g$, $g\in\mathbb{Z}$.

\begin{figure}[htbp]
  \centering
  \includegraphics[width=0.82\linewidth]{figures/part02/ex5_3_weighted_comb.png}
  \caption{Weighted discrete $\delta$--comb supported at $x=2\pi g$, $g\in\mathbb{Z}$.}
  \label{fig:ex5-3-weighted-comb}
\end{figure}
```

## CP-II-0431

- chapter line: 19054

```tex
\label{prob:cp-ii-0431}
let $f_n$ be a narrow spike of height $1$ and width $1/n$. Then
	\[
	\|f_n\|_\infty=1 \quad \text{but} \quad \|f_n\|_1=\frac{1}{n}\to 0.
	\]
	Hence convergence in $\|\cdot\|_1$ does not imply convergence in $\|\cdot\|_\infty$.
```

## CP-II-0432

- chapter line: 19063

```tex
\label{prob:cp-ii-0432}
— Quickies (uniform convergence \& regularity)

If $(f_n)$ is a sequence of real functions on $[0,1]$ converging uniformly to a function $f$ on $[0,1]$, and if $f_n$ is continuous at $x_n\in[0,1]$ with $x_n\to x$, does it follow that $f$ is continuous at $x$?

  If $(f_n)$ is a sequence of continuous real functions on $[-1,1]$ converging pointwise to a continuous function $f$ on $[-1,1]$, and if the convergence is uniform on $[-r,r]$ for every $r\in(0,1)$, does it follow that the convergence is uniform on $[-1,1]$?

  If $(f_n)$ is a sequence of real functions on the interval $[0,1]$ converging uniformly to a function $f$ on $[0,1]$, and if each $f_n$ is continuous except at countably many points, does it follow that there exists a point at which $f$ is continuous?

  If $(f_n)$ is a sequence of differentiable functions on $[0,1]$ converging uniformly to a function $f$ on $[0,1]$, does it follow that there exists a point at which $f$ is differentiable?

\bigskip

	\par\noindent\textbullet\quad \textbf{Continuity at a point is preserved by uniform limits:} If $f_n\to f$ uniformly on a set $E$ and each $f_n$ is continuous at $x_0\in E$, then $f$ is continuous at $x_0$.
	\par\noindent\textbullet\quad \textbf{Uniform limit of continuous functions is continuous.}
	\par\noindent\textbullet\quad \textbf{Countable union of countable sets is countable.}
	\par\noindent\textbullet\quad \textbf{Local vs global uniformity:} Uniform convergence on $[-r,r]$ for every $r<1$ need not imply uniform convergence on $[-1,1]$.
	\par\noindent\textbullet\quad \textbf{Weierstrass phenomenon:} There exist continuous nowhere differentiable functions that are uniform limits of differentiable functions (e.g., partial sums of the Weierstrass series).

Let
\[
f(x)=\begin{cases}
	0,& x<\tfrac12,\\
	1,& x\ge \tfrac12,
\end{cases}
\qquad \text{and set } f_n=f \text{ for all } n.
\]
Then $f_n\to f$ uniformly. Define $x_n=\tfrac12+\tfrac1n\to x=\tfrac12$. For each $n$, $f_n$ is continuous at $x_n$ (indeed $f$ is continuous at all $x\ne \tfrac12$), but $f$ is discontinuous at $x=\tfrac12$. Hence the asserted implication fails.

For $n\ge1$, define
\[
f_n(x)=
\begin{cases}
	n(1-x),& x\in[1-\tfrac1n,\,1],\\
	0,& x\in[-1,\,1-\tfrac1n),
\end{cases}
\qquad\text{and let } f\equiv 0.
\]
Each $f_n$ is continuous on $[-1,1]$. For any fixed $x\in[-1,1)$, $f_n(x)=0$ for all large $n$, so $f_n(x)\to 0=f(x)$. Also $f_n(1)=0\to 0=f(1)$, hence $f_n\to f$ pointwise and $f$ is continuous. Given any $r\in(0,1)$, if $n>\frac1{1-r}$ then $[1-\frac1n,1]\subset (r,1]$, so $f_n\equiv 0$ on $[-r,r]$; thus convergence is uniform on $[-r,r]$. However,
\[
\sup_{x\in[-1,1]}|f_n(x)-f(x)|=\max_{x\in[-1,1]} f_n(x)=1 \quad\text{for all }n,
\]
so the convergence is not uniform on $[-1,1]$.

Let $D_n$ be the (countable) set of discontinuities of $f_n$ and $D=\bigcup_{n=1}^\infty D_n$, which is countable. Choose $x_0\in[0,1]\setminus D$. Then each $f_n$ is continuous at $x_0$. Since $f_n\to f$ uniformly, the continuity-at-a-point lemma implies $f$ is continuous at $x_0$. Therefore $f$ is continuous at (at least) one point.

Consider the Weierstrass function
\[
W(x)=\sum_{k=0}^\infty a^k\cos(b^k\pi x),
\]
with $0<a<1$, $b\in\mathbb{N}$ odd, and $ab>1$. Let $S_n(x)=\sum_{k=0}^n a^k\cos(b^k\pi x)$. Then each $S_n$ is differentiable on $[0,1]$, and $S_n\to W$ uniformly on $[0,1]$, while $W$ is continuous everywhere and nowhere differentiable. Thus there need not exist any point where $f$ is differentiable.
```

## CP-II-0439

- chapter line: 19163

```tex
\label{prob:cp-ii-0439}
\par\noindent\textbullet\quad On $\mathbb{R}^n$:
	\[
	\|x\|_1=\sum_{i=1}^n |x_i|,\qquad
	\|x\|_2=\Big(\sum_{i=1}^n x_i^2\Big)^{1/2},\qquad
	\|x\|_\infty=\max_{1\le i\le n}|x_i|.
	\]
	There exist constants $a,b>0$ such that
	\[
	\|x\|_\infty \le \|x\|_2 \le \|x\|_1 \le \sqrt{n}\,\|x\|_2.
	\]
	Thus all norms on $\mathbb{R}^n$ are equivalent.
```

## CP-II-0440

- chapter line: 19178

```tex
\label{prob:cp-ii-0440}
— Discontinuities under uniform limits

Let $(f_n)$ be a sequence of real-valued functions on $[0,1]$ converging uniformly to a function $f$.
For each $n$, let $D_n$ be the set of discontinuities of $f_n$, and let $D$ be the set of discontinuities of $f$.

We show that
\[
D \subseteq \bigcap_{n=1}^{\infty}\ \bigcup_{j=n}^{\infty} D_j
\qquad\text{(the limsup of the sets $D_j$).}
\]
Equivalently, we prove the contrapositive. Suppose $x\notin \limsup D_j$. Then there exists $N$ such that
$x\notin D_j$ for all $j\ge N$. Thus, for all $j\ge N$, the function $f_j$ is continuous at $x$.
Since $f_j \to f$ uniformly on $[0,1]$, the uniform-limit lemma implies that $f$ is continuous at $x$.
Hence $x\notin D$, proving the desired inclusion.

Assume there exists a finite $k$ such that each $f_n$ has at most $k$ discontinuities.
We claim that $f$ has at most $k$ discontinuities.

Suppose, for a contradiction, that $f$ has at least $k+1$ distinct discontinuities $x_1,\dots,x_{k+1}\in[0,1]$.
Let the oscillation of a function $g$ at $x$ be
\[
\omega_g(x)=\lim_{r\downarrow 0}\left(\sup_{|t-x|<r} g(t) - \inf_{|t-x|<r} g(t)\right).
\]
Then $g$ is continuous at $x$ iff $\omega_g(x)=0$. Moreover, if $\|g-h\|_\infty\le \varepsilon$, then
$\omega_g(x)\le\omega_h(x)+2\varepsilon$ and $\omega_h(x)\le\omega_g(x)+2\varepsilon$.

Since $x_i$ is a discontinuity of $f$, we have $\omega_f(x_i)>0$ for each $i$.
Choose $0<\varepsilon<\frac12\min_{1\le i\le k+1}\omega_f(x_i)$.
Because $f_n\to f$ uniformly, there exists $N$ such that $\|f_n-f\|_\infty<\varepsilon$ for all $n\ge N$.
For each $i$ and $n\ge N$,
\[
\omega_{f_n}(x_i)\ \ge\ \omega_f(x_i) - 2\varepsilon\ >\ 0,
\]
so $f_n$ is discontinuous at $x_i$. Hence $f_n$ has at least $k+1$ discontinuities for all $n\ge N$,
contradicting the hypothesis that each $f_n$ has at most $k$ discontinuities.
Therefore $f$ has at most $k$ discontinuities.

(1) From (a) we always have $D \subseteq \limsup D_n$, so if each $D_n$ is finite then $D$ is at most countable.

(2) The conclusion in (b) is stronger: if each $f_n$ has at most $k$ discontinuities for a fixed $k$, then $f$ has at most $k$ discontinuities.

(3) Example (sharpness for $k=1$).

Fix $c\in(0,1)$ and define $f=\mathbf{1}_{[c,1]}$ and $f_n=\mathbf{1}_{[c+1/n,\,1]}$.
Then $f_n\to f$ uniformly, each $f_n$ has exactly one discontinuity, and $f$ has exactly one discontinuity.

Let $k=1$. Fix a point $c\in(0,1)$ and define
\[
f(x) = \mathbf{1}_{[c,1]}(x) =
\begin{cases}
	0, & x < c,\\
	1, & x \ge c,
\end{cases}
\qquad\text{and}\qquad
f_n(x) = \mathbf{1}_{[\,c+1/n,\,1\,]}(x).
\]
Each $f_n$ has exactly one discontinuity (at $x=c+1/n$);
$f_n \to f$ uniformly on $[0,1]$,
and $f$ has exactly one discontinuity (at $x=c$).
This shows that the bound ``$\le k$'' is \emph{sharp}.
```

## CP-II-0442

- chapter line: 19242

```tex
\label{prob:cp-ii-0442}
Uniform convergence with oscillations (Cauchy)

$f_n(x)=\sin(nx)/n$ on $[0,\pi]$.
Uniform convergence to $f(x)=0$ since $\|f_n-0\|_\infty=1/n \to 0$.
```

## CP-II-0444

- chapter line: 19250

```tex
\label{prob:cp-ii-0444}
Let $L=\sum_{n=1}^\infty 10^{-n!}$ and $r_N=\sum_{n=1}^{N}10^{-n!}=p_N/10^{N!}$.
	Then
	\[
	|L-r_N|=\sum_{n\ge N+1}10^{-n!}
	=10^{-(N+1)!}\Bigl(1+\sum_{n\ge N+2}10^{-(n!-(N+1)!)}\Bigr).
	\]
	For $n\ge N+2$ we have $n!-(N+1)!\ge (N+2)!-(N+1)!=(N+1)N!\ge N!$, hence
	\[
	\sum_{n\ge N+2}10^{-(n!-(N+1)!)}\le \sum_{k=1}^\infty (10^{-N!})^{k}
	=\frac{10^{-N!}}{1-10^{-N!}}\le \frac{1}{9}.
	\]
	Therefore
	\[
	\boxed{\ |L-r_N|< \frac{10}{9}\,10^{-(N+1)!}\ }.
	\]
	Fix $m\in\mathbb N$ and choose $N\ge m$. Since $((N+1)-m)N!\ge N!\ge1$,
	\[
	\frac{10}{9}\,10^{-(N+1)!}
	=\frac{10}{9}\,10^{-((N+1)-m)N!}\cdot 10^{-mN!}\le 10^{-mN!}
	=\frac{1}{(10^{N!})^{\,m}}.
	\]
	Thus for $q_N=10^{N!}$ we obtain
	\[
	\Bigl|L-\frac{p_N}{q_N}\Bigr|<\frac{1}{q_N^{\,m}}
	\quad\text{for all }N\ge m.
	\]
	Since this holds for every $m$ and infinitely many $N$, $L$ is a Liouville number and hence transcendental.
```

## CP-II-0447

- chapter line: 19478

```tex
\label{prob:cp-ii-0447}
One may build $p_n$ via Faber polynomials of the arc or via discrete least–squares fits on $K$;
both converge uniformly by Mergelyan.

\noindent\rule{\textwidth}{0.4pt}

\bigskip
```

## CP-II-0448

- chapter line: 19488

```tex
\label{prob:cp-ii-0448}
\par\noindent\textbullet\quad More conceptually: the functions $x \mapsto x^p/p$ and
	$y \mapsto y^q/q$ are Legendre transforms of each other.
	Young's inequality expresses this duality.
```

## CP-II-0450

- chapter line: 19520

```tex
\label{prob:cp-ii-0450}
\par\noindent\textbullet\quad \textbf{Shrinking supports.}
		In $\mathbb R^{n}$, set $f_j := |B_{1/j}|^{-1/p}\,\mathbf 1_{B_{1/j}}$. Then $\|f_j\|_p=1$ and
		$f_j\rightharpoonup 0$ in $L^{p}$; indeed $\int f_j h \to 0$ for $h\in C_c^\infty$, then extend to $L^{p'}$.
```

## CP-II-0451

- chapter line: 19527

```tex
\label{prob:cp-ii-0451}
\par\noindent\textbullet\quad \textbf{Total variation.} If $u_n\to u$ in $L^1(\Omega)$, then
		$\mathrm{TV}(u)\le \liminf_n \mathrm{TV}(u_n)$.

	If $x_n\rightharpoonup x$ in a Hilbert space, then
	$\|x\|\le \liminf_n \|x_n\|$ (weak l.s.c.\ of the norm). Moreover,
	if also $\|x_n\|\to\|x\|$, then
	\[
	\|x_n-x\|^2=\|x_n\|^2+\|x\|^2-2\,\Re\langle x_n,x\rangle \longrightarrow 0,
	\]
	hence $x_n\to x$ in norm.

	\clearpage

\subsection*{A. $L^p$ norms: weak l.s.c.\ $\;\|f\|_{p}\le \liminf_{n}\|f_n\|_{p}$}

\noindent\textbf{1.\ Strict inequality (moving bump).}\par
\noindent
On $\mathbb{R}$ set $f_n=\mathbf 1_{(n,n+1)}$. Then $f_n\rightharpoonup 0$ in $L^p$ for any $1\le p<\infty$
(vanishes on every bounded set), but
\[
\|f_n\|_{p}=1.
\]
Hence
\[
\|0\|_{p}=0 \;<\; \liminf_{n\to\infty}\|f_n\|_{p}=1.
\]

\medskip
\noindent\textbf{2.\ Strict inequality (oscillations).}\par
\noindent
On $[0,1]$, $f_n(x)=\sin(2\pi n x)$ is bounded in $L^2$ and $f_n\rightharpoonup 0$ (Riemann–Lebesgue).
But
\[
\|f_n\|_{2}=\Big(\int_0^1 \sin^2(2\pi n x)\,dx\Big)^{1/2}=\frac{1}{\sqrt{2}},
\]
so
\[
0 \;<\; \liminf_{n\to\infty}\|f_n\|_{2}=\frac{1}{\sqrt{2}}.
\]

\medskip
\noindent\textbf{3.\ Equality case (then strong convergence).}\par
\noindent
Let $f,g\in L^2[0,1]$ with $\langle f,g\rangle=0$ and set $f_n=f+\tfrac{1}{n}g$.
Then $f_n\rightharpoonup f$ and
\[
\|f_n\|_{2}^{2}=\|f\|_{2}^{2}+\frac{1}{n^{2}}\|g\|_{2}^{2}\ \longrightarrow\ \|f\|_{2}^{2}.
\]
Hence $\|f_n\|_{2}\to\|f\|_{2}$, and by the criterion ``weak $+$ norms $\Rightarrow$ strong'' we get
\[
f_n\ \to\ f \quad\text{in }L^2.
\]

\vspace{1em}

\subsection*{B. Dirichlet energy $E(u)=\displaystyle\int_{\Omega} |\nabla u|^{2}$: weak l.s.c.\ and minimizers}

\noindent\textbf{1.\ Weak l.s.c.\ in action (strict inequality possible).}\par
\noindent
Take $\Omega=(0,1)$ and $u_n(x)=\sin(2\pi n x)$. Then $u_n\rightharpoonup 0$ in $H^1_0(0,1)$, but
\[
E(u_n)=\int_0^1 |u_n'(x)|^2\,dx=\int_0^1 (2\pi n)^2\cos^2(2\pi n x)\,dx
=2\pi^{2}n^{2}\ \longrightarrow\ \infty,
\]
so trivially
\[
E(0)=0\ \le\ \liminf_{n\to\infty} E(u_n).
\]

\medskip
\noindent\textbf{2.\ Existence of a minimizer (direct method).}\par
\noindent
Let $\Omega\subset\mathbb{R}^{n}$ be bounded Lipschitz and fix boundary data $g\in H^{1/2}(\partial\Omega)$.
Minimize
\[
\mathcal{A}=\{\,u\in H^{1}(\Omega): u=g \text{ on }\partial\Omega\,\},\qquad
E(u)=\int_{\Omega}|\nabla u|^{2}\,dx.
\]
Let $(u_k)\subset\mathcal{A}$ be such that $E(u_k)\downarrow\inf_{\mathcal{A}}E$. Then $(u_k)$ is bounded in $H^{1}(\Omega)$,
hence (by reflexivity and Rellich–Kondrachov) there is a subsequence $u_{k_j}$ with
\[
u_{k_j}\rightharpoonup u \ \text{ in } H^{1}(\Omega),\qquad u_{k_j}\to u \ \text{ in } L^{2}(\Omega).
\]
The trace is stable under weak $H^1$ convergence, so $u\in\mathcal{A}$. Weak lower semicontinuity yields
\[
E(u)\ \le\ \liminf_{j\to\infty} E(u_{k_j}) \;=\; \inf_{\mathcal{A}}E,
\]
hence $u$ is a minimizer (the weakly harmonic extension of $g$).

\medskip
\noindent\textbf{3.\ Concrete 1D minimizer.}\par
\noindent
On $\Omega=(0,1)$ with boundary data $u(0)=0$, $u(1)=1$, the minimizer is $u(x)=x$, and
\[
E(u)=\int_0^1 |u'(x)|^{2}\,dx=\int_0^1 1\,dx=1.
\]
Any minimizing sequence $(u_k)$ has (up to subsequence) $u_k\rightharpoonup x$ in $H^{1}(0,1)$ and
$E(x)\le\liminf E(u_k)$.

	\subsection*{Why $f_n=\mathbf 1_{(n,n+1)} \rightharpoonup 0$ in $L^p(\mathbb R)$ for $1<p<\infty$}

	Let $p\in(1,\infty)$ and $p'$ be its H\"older conjugate. For any $h\in L^{p'}(\mathbb R)$,
	\[
	\int_{\mathbb R} f_n(x)\,h(x)\,dx=\int_{n}^{n+1} h(x)\,dx.
	\]
	Given $\varepsilon>0$, choose $R>0$ so large that
	\[
	\|h\|_{L^{p'}(\{|x|>R\})}<\varepsilon
	\qquad\text{(possible since $h\in L^{p'}$).}
	\]
	If $n>R$, then $(n,n+1)\subset\{|x|>R\}$ and, by H\"older,
	\[
	\Big|\int_{n}^{n+1} h(x)\,dx\Big|
	\le \|\mathbf 1_{(n,n+1)}\|_{L^p}\,\|h\|_{L^{p'}((n,n+1))}
	\le 1\cdot \|h\|_{L^{p'}(\{|x|>R\})}
	<\varepsilon.
	\]
	Hence $\int f_n h\to 0$ for every $h\in L^{p'}$, i.e.\ $f_n\rightharpoonup 0$ in $L^p$.

	\bigskip
	\noindent\textbf{Important caveat for $p=1$.}
	For $p=1$ the dual is $L^\infty$. The same argument does \emph{not} force
	$\int_{n}^{n+1} h \to 0$ for all $h\in L^\infty$ (one only gets $|\int_{n}^{n+1} h|\le \|h\|_\infty$).
	In fact, taking
	\[
	h(x)=\sum_{k\in\mathbb Z}(-1)^k\,\mathbf 1_{[k,k+1]}(x)\in L^\infty
	\]
	gives
	\[
	\int f_n h = (-1)^n,
	\]
	which does not converge. Therefore $f_n$ does \emph{not} converge weakly to $0$ in $L^1$.

	\bigskip
	\noindent\textbf{Summary.}
	\[
	\begin{aligned}
		&f_n \rightharpoonup 0 \quad \text{in } L^p(\mathbb R)\ \text{for } 1<p<\infty,\\[0.3em]
		&\text{not true in } L^1;\ \text{indeed, } (f_n)\ \text{has no weakly convergent subsequence in } L^1.
	\end{aligned}
	\]
```

## CP-II-0452

- chapter line: 19672

```tex
\label{prob:cp-ii-0452}
— Uniform limits: sums vs products

Let $(f_n)$ and $(g_n)$ be sequences of real-valued functions on a set $E$ converging uniformly to $f$ and $g$, respectively.

By the triangle inequality,
\[
\sup_{x\in E}\big|(f_n+g_n)-(f+g)\big|
\le \sup_{x\in E}|f_n-f|+\sup_{x\in E}|g_n-g|\xrightarrow[n\to\infty]{}0.
\]
Thus $f_n+g_n\to f+g$ uniformly on $E$.

Consider $E=\mathbb{R}$ and define $f_n(x)\equiv \frac1n$, $f(x)\equiv 0$, and $g_n(x)\equiv g(x)=x$. Then
\[
\sup_{x\in\mathbb{R}}|f_n(x)-f(x)|=\frac1n\to0,\qquad
\sup_{x\in\mathbb{R}}|g_n(x)-g(x)|=0,
\]
so $f_n\to f$ and $g_n\to g$ uniformly. However
\[
f_n(x)g_n(x)=\frac{x}{n},\qquad
\sup_{x\in\mathbb{R}}\Big|\frac{x}{n}-0\Big|=\infty,
\]
so $(f_ng_n)$ does not converge uniformly to $fg$ on $\mathbb{R}$ (even though it converges pointwise to $0$).

Suppose $|f|\le M$ and $|g|\le L$ on $E$. Since $g_n\to g$ uniformly, there exists $N_0$ such that for all $n\ge N_0$,
\[
\sup_{x\in E}|g_n(x)-g(x)|<1\quad\Rightarrow\quad
\sup_{x\in E}|g_n(x)|\le L+1.
\]
Then for $n\ge N_0$,
\[
\begin{aligned}
	\sup_{x\in E}|f_n(x)g_n(x)-f(x)g(x)|
	&\le \sup_{x\in E}|f_n(x)-f(x)|\,\sup_{x\in E}|g_n(x)|
	+ \sup_{x\in E}|f(x)|\,\sup_{x\in E}|g_n(x)-g(x)| \\
	&\le (L+1)\sup_{x\in E}|f_n-f| + M\sup_{x\in E}|g_n-g|\xrightarrow[n\to\infty]{}0.
\end{aligned}
\]
Hence $f_ng_n\to fg$ uniformly on $E$.

Uniform convergence of $(f_ng_n)$ to $fg$ need not hold. The example in (2) has bounded $f\equiv 0$, unbounded $g(x)=x$, uniform convergence $f_n\to f$ and $g_n\to g$, yet $(f_ng_n)$ fails to converge uniformly to $fg$.
```

## CP-II-0455

- chapter line: 19716

```tex
\label{prob:cp-ii-0455}
(Trace theorem on a hyperplane)

Assume $s>\tfrac12$ and suppose $u\in\mathcal S(\mathbb R^n)$.
Write $x=(x',x_n)\in\mathbb R^{n-1}\times\mathbb R$ and define the trace
\[
Tu(x') := u(x',0),\qquad x'\in\mathbb R^{n-1}.
\]

Show that for each $\xi'\in\mathbb R^{n-1}$ one has
\[
\widehat{Tu}(\xi') = \frac{1}{2\pi}\int_{\mathbb R}\widehat u(\xi',\xi_n)\,d\xi_n.
\]

Deduce that
\[
\bigl|\widehat{Tu}(\xi')\bigr|^2
\;\le\;
\frac{1}{(2\pi)^2}
\left(\int_{\mathbb R} (1+|\xi|^2)^s\,|\widehat u(\xi',\xi_n)|^2\,d\xi_n\right)
\left(\int_{\mathbb R}\frac{d\xi_n}{(1+|\xi|^2)^s}\right),
\]
where $\xi=(\xi',\xi_n)$.

By changing variables in the second integral above to
$\xi_n = t\sqrt{1+|\xi'|^2}$, show that there exists a constant $C(s)>0$
such that
\[
\|Tu\|_{H^{s-\frac12}(\mathbb R^{n-1})}
\;\le\; C(s)\,\|u\|_{H^s(\mathbb R^n)}.
\]

Conclude that $T$ extends uniquely by density to a bounded linear operator
\[
T:H^s(\mathbb R^n)\longrightarrow H^{s-\frac12}(\mathbb R^{n-1}),
\qquad s>\tfrac12.
\]

Suppose $\nu\in\mathcal S(\mathbb R^{n-1})$ and let $\phi\in C_c^\infty(\mathbb R)$ satisfy
\[
\int_{\mathbb R}\phi(t)\,dt = \sqrt{2\pi}.
\]
Define $u$ through its Fourier transform by
\[
\widehat u(\xi',\xi_n)
:= \frac{\widehat\nu(\xi')}{\sqrt{1+|\xi'|^2}}\,
\phi\!\left(\frac{\xi_n}{\sqrt{1+|\xi'|^2}}\right).
\]
Show that there exists a constant $C>0$ such that
\[
\|u\|_{H^s(\mathbb R^n)} \le C\,\|\nu\|_{H^{s-\frac12}(\mathbb R^{n-1})}.
\]
Compute $Tu$ and verify that $Tu=\nu$. Conclude that
\[
T:H^s(\mathbb R^n)\longrightarrow H^{s-\frac12}(\mathbb R^{n-1})
\]
is surjective and hence an isomorphism onto $H^{s-\frac12}(\mathbb R^{n-1})$.

\bigskip

For $s>\tfrac12$ the trace operator
\[
T:H^s(\mathbb R^n)\to H^{s-\frac12}(\mathbb R^{n-1}),
\qquad Tu(x')=u(x',0),
\]
is well defined, bounded and surjective. The proof above is based on the
Fourier identity in (a), the Cauchy--Schwarz estimate in (b),
and the estimate
\[
\int_{\mathbb R}\frac{d\xi_n}{(1+|\xi'|^2+\xi_n^2)^s}
= c_s\,(1+|\xi'|^2)^{\frac12-s},\qquad s>\tfrac12,
\]
which exactly produces the $H^{s-\frac12}$-weight in $\xi'$.
Part (e) constructs a bounded extension operator
$E:H^{s-\frac12}(\mathbb R^{n-1})\to H^s(\mathbb R^n)$ with $T\circ E=\mathrm{Id}$,
showing that every element of $H^{s-\frac12}(\mathbb R^{n-1})$ arises as a trace.
```

## CP-II-0456

- chapter line: 19795

```tex
\label{prob:cp-ii-0456}
\par\noindent\textbullet\quad \textbf{Tolerance–driven truncation.}
	Given $\varepsilon>0$, choose $n$ so that $S_n\le \varepsilon$. If $\gamma_j$ are unknown,
	estimate $S_n$ via
	\[
	S_n = \max_{0\le k\le 3^{n+1}} |f(x_k)-P_n(x_k)|.
	\]
```

## CP-II-0463

- chapter line: 19866

```tex
\label{prob:cp-ii-0463}
\par\noindent\textbullet\quad \emph{Absolute continuity:} $\nu\ll\mu$ means $\mu(A)=0 \Rightarrow \nu(A)=0$ for all $A\in\mathcal E$.
```

## CP-II-0465

- chapter line: 19871

```tex
\label{prob:cp-ii-0465}
Uniform convergence (Cauchy)

$f_n(x)=x/n$ on $[0,1]$. Limit $f(x)=0$.
Uniform convergence since $\|f_n-0\|_\infty=1/n \to 0$.

---
```

## CP-II-0470

- chapter line: 19881

```tex
\label{prob:cp-ii-0470}
— Separate continuity vs.\ joint continuity; Lipschitz criterion

\textbf{Statement.}\quad

Let $f:U\subset\mathbb{R}^2\to\mathbb{R}$ satisfy:
for each fixed $y$, $f(\cdot,y)$ is continuous; for each fixed $x$, $f(x,\cdot)$ is continuous.
 \setlength{\itemsep}{6pt}
	\par\noindent\textbullet\quad Give an example where $f$ is \emph{not} jointly continuous on $U$.
	\par\noindent\textbullet\quad Suppose there exist $L,M\ge0$ such that
	\[
	|f(x_1,y)-f(x_2,y)|\le L|x_1-x_2|, \qquad
	|f(x,y_1)-f(x,y_2)|\le M|y_1-y_2|
	\]
	for all relevant points in $U$ (constants independent of the other variable).
	Show that $f$ is jointly continuous on $U$.
	\par\noindent\textbullet\quad Deduce: if $D_1 f$ exists and is bounded on $U$, and $f(x,\cdot)$ is continuous for each fixed $x$,
	then $f$ is continuous on $U$.

\bigskip\hrule\bigskip

\textbf{Theory \& Solution.}\quad

\textbf{(1) Counterexample: separate $\not\Rightarrow$ joint).}\;
\[
f(x,y)=
\begin{cases}
	\dfrac{xy}{x^2+y^2}, & (x,y)\neq(0,0),\\[4pt]
	0,&(x,y)=(0,0).
\end{cases}
\]
For fixed $x$ or fixed $y$, $f\to 0$ at the origin; along $y=x$ we have $f(x,x)=\tfrac12$, so $f$ is not continuous at $(0,0)$.

\medskip

\textbf{(2) Uniform one–variable Lipschitz $\Rightarrow$ joint continuity).}\;
For $(x_1,y_1),(x_2,y_2)$,
\[
\begin{aligned}
	|f(x_1,y_1)-f(x_2,y_2)|
	&\le |f(x_1,y_1)-f(x_2,y_1)| + |f(x_2,y_1)-f(x_2,y_2)|\\
	&\le L|x_1-x_2| + M|y_1-y_2|,
\end{aligned}
\]
hence $f$ is globally Lipschitz on $U$ and therefore continuous.

\medskip

\textbf{(3) Bounded $D_1 f$ gives the needed uniform Lipschitz in $x$).}\;
If $|D_1 f|\le L$ on $U$ and $y$ is fixed, the 1D mean value theorem in $x$ yields
$|f(x_1,y)-f(x_2,y)|\le L|x_1-x_2|$ (constant independent of $y$).
Combine with continuity in $y$ and apply (2). \hfill$\square$

\bigskip\hrule\bigskip

\textbf{Examples.}\quad

 \setlength{\itemsep}{6pt}
	\par\noindent\textbullet\quad $f(x,y)=|x|\,\sin y$: here $D_1 f=\operatorname{sgn}(x)\sin y$ is bounded; $f(x,\cdot)$ is continuous. Conclusion: $f$ is continuous on $U$.
	\par\noindent\textbullet\quad The counterexample above shows separate continuity alone is insufficient.
```

## CP-II-0472

- chapter line: 19944

```tex
\label{prob:cp-ii-0472}
\par\noindent\textbullet\quad simple functions are finite linear combinations of indicator sets;
```

## CP-II-0474

- chapter line: 19949

```tex
\label{prob:cp-ii-0474}
\par\noindent\textbullet\quad Show that if $f\in C_c^3(\mathbb{R})$ is an odd function
	(i.e.\ $f(s)=-f(-s)$ for all $s$), then
	\[
	u(x,t) \equiv \frac{f(r+t)+f(r-t)}{2r}
	\]
	extends as a $C^2$ function which solves the wave equation on
	$S_T=(-T,T)\times\mathbb{R}^3$, with
	\[
	u(0,t) = f'(t).
	\]
```

## CP-II-0478

- chapter line: 19963

```tex
\label{prob:cp-ii-0478}
Integrals of vector-valued maps

Let $f:[0,1]\to\mathbb R^n$ be continuous and $\displaystyle \int_0^1 f:=\big(\int_0^1 f_1,\dots,\int_0^1 f_n\big)$.

	With $v=\int_0^1 f$ and the Euclidean dot product,
	\[
	\|v\|_2^2=v\cdot v=v\cdot \int_0^1 f=\int_0^1 v\cdot f(x)\,dx
	\le \int_0^1 \|v\|_2\,\|f(x)\|_2\,dx
	=\|v\|_2\int_0^1 \|f(x)\|_2\,dx,
	\]
	hence $\Big\|\int_0^1 f\Big\|_2 \le \int_0^1 \|f(x)\|_2\,dx$.

Equality
\[
\Bigl\|\!\int_{0}^{1} f \Bigr\| \;=\; \int_{0}^{1} \|f\|
\]
holding for \emph{every} norm on $\mathbb{R}^n$ occurs precisely when there exist
\[
u\in\mathbb{R}^n\setminus\{0\}
\quad\text{and}\quad
\alpha:[0,1]\to\mathbb{R}\ \text{of constant sign}
\]
such that
\[
f(x)=\alpha(x)\,u \qquad (x\in[0,1]).
\]

\noindent\textit{Sufficiency.}
If $f(x)=\alpha(x)u$ and $\alpha$ has constant sign, then for any norm $\|\cdot\|$,
\[
\Bigl\|\!\int_{0}^{1} f \Bigr\|
=\bigl\| (\int_{0}^{1}\alpha)\,u \bigr\|
= \bigl|\!\int_{0}^{1}\alpha \bigr|\,\|u\|
= \int_{0}^{1} |\alpha|\,\|u\|
= \int_{0}^{1} \|f\|.
\]

\noindent\textit{Necessity.}
Fix a strictly convex norm (e.g.\ Euclidean). Equality in the triangle inequality forces
$f(x)$ to be positively colinear a.e.; hence $f(x)=\alpha(x)u$ for some $u$ and scalar $\alpha$.
Requiring equality for \emph{every} norm rules out sign changes of $\alpha$, so $\alpha$ has
constant sign on $[0,1]$.
\medskip
```

## CP-II-0482

- chapter line: 20032

```tex
\label{prob:cp-ii-0482}
\par\noindent\textbullet\quad \textbf{Logarithmic rate.}
	For $\delta_n=\frac{1}{\log(n+2)}$,
	$\gamma_j=\frac{1}{\log(j+1)}-\frac{1}{\log(j+2)}$ and
	$E_n(f)\ge 1/\log(n+2)$.
```

## CP-II-0484

- chapter line: 20077

```tex
\label{prob:cp-ii-0484}
\par\noindent\textbullet\quad \textbf{Triangle inequality:}
	$\|p+q\|_{I}=\sup_{t\in I}|p(t)+q(t)|\le \sup_{t\in I}|p(t)|+\sup_{t\in I}|q(t)|=\|p\|_{I}+\|q\|_{I}$.

Hence $\|\cdot\|_{I}$ is a norm on $\mathcal{P}$.

\bigskip
\par\medskip\noindent\textbf{(b) Same sequence, two norms, two different limits.}\quad
Let
\[
K_1=[0,\tfrac12],\qquad K_2=[\tfrac12,1],
\]
and pick infinite sets $I\subset K_1$, $J\subset K_2$.

By Urysohn on $[0,1]$ choose $f\in C([0,1])$ with $f|_{K_1}\equiv0$ and $f|_{K_2}\equiv1$.
By Weierstrass there exist polynomials $p_n\in\mathcal{P}$ such that
\[
\|p_n-f\|_{[0,1]}:=\sup_{t\in[0,1]}|p_n(t)-f(t)| \xrightarrow[n\to\infty]{} 0.
\]

Then
\[
\|p_n-0\|_{I}=\sup_{t\in I}|p_n(t)|
\ \le\ \sup_{t\in K_1}|p_n(t)-f(t)|
\ \xrightarrow[n\to\infty]{}\ 0,
\]
so $p_n\to 0$ in $(\mathcal{P},\|\cdot\|_{I})$.

Similarly,
\[
\|p_n-1\|_{J}=\sup_{t\in J}|p_n(t)-1|
\ \le\ \sup_{t\in K_2}|p_n(t)-f(t)|
\ \xrightarrow[n\to\infty]{}\ 0,
\]
so $p_n\to 1$ in $(\mathcal{P},\|\cdot\|_{J})$.

\medskip
\noindent
Thus the \emph{same} sequence $(p_n)$ converges to \emph{different} elements (0 and 1) under two different norms on the same vector space $\mathcal{P}$.

\bigskip
\par\medskip\noindent\textbf{(c) Impossibility in $\ell^1,\ell^2$ and in $C([0,1])$ with standard norms.}\quad
No such example exists.
```

## CP-II-0486

- chapter line: 20123

```tex
\label{prob:cp-ii-0486}
\par\noindent\textbullet\quad The pair $(p,q)$ is fundamental: these are exactly the exponents
	for which Young's and Hölder's inequalities hold and for which the
	duality $(L^p)^* \cong L^q$ is valid.

\bigskip
```

## CP-II-0487

- chapter line: 20132

```tex
\label{prob:cp-ii-0487}
\par\noindent (b)\quad Use this to produce a vector space, a single sequence in it, and two different norms on it
	such that the sequence converges to \emph{different} elements of the space with respect to the two norms.
	(Hint: Weierstrass approximation.)
```

## CP-II-0488

- chapter line: 20139

```tex
\label{prob:cp-ii-0488}
{Polynomial step approximations on a half-disk and half-plane}{poly-step}
	(i) Show there exists a sequence of polynomials $(P_n)$ such that
	\[
	P_n(z)\longrightarrow
	\begin{cases}
		1,& |z|\le1,\ \Re z\ge0,\\
		0,& |z|\le1,\ \Re z<0,
	\end{cases}
	\quad\text{as }n\to\infty.
	\]
	(ii) Show there exists a sequence of polynomials $(Q_n)$ such that
	\[
	Q_n(z)\longrightarrow
	\begin{cases}
		1,& \Re z\ge0,\\
		0,& \Re z<0,
	\end{cases}
	\quad\text{as }n\to\infty.
	\]
```

## CP-II-0489

- chapter line: 20162

```tex
\label{prob:cp-ii-0489}
\par\noindent\textbullet\quad For complex-valued $F$, apply the inequality to $|F|$.
```

## CP-II-0490

- chapter line: 20167

```tex
\label{prob:cp-ii-0490}
Suppose $A\subset\mathbb{R}^n$ and $f:A\to\mathbb{R}^m$. Then
\[
\lim_{x\to p}f(x)=F \iff \text{ for every sequence } x_i\in A,\ x_i\neq p,\ x_i\to p,\ \text{we have } f(x_i)\to F.
\]
\textit{Proof.} The forward direction is immediate from the $\varepsilon$--$\delta$ definition; the reverse is proved by contradiction constructing a sequence $x_k\to p$ with $f(x_k)$ staying $\varepsilon_0$ away from $F$.
```

## CP-II-0491

- chapter line: 20176

```tex
\label{prob:cp-ii-0491}
Define
	\[
	L \;=\; \sum_{n=1}^{\infty} 10^{-n!}
	\;=\; 0.110001000000000000000001\ldots,
	\qquad
	r_N \;:=\; \sum_{n=1}^{N} 10^{-n!} \;=\; \frac{p_N}{10^{N!}}.
	\]
	Prove sharp bounds on the tail $|L-r_N|$, deduce the Liouville inequalities
	\(
	\bigl|L-\frac{p_N}{10^{N!}}\bigr| < \frac{1}{(10^{N!})^{\,m}}
	\)
	for arbitrarily large $m$, and conclude that $L$ is transcendental.
```

## CP-II-0497

- chapter line: 20211

```tex
\label{prob:cp-ii-0497}
s.

\par\noindent\textbullet\quad If $F$ is \emph{convex} and \emph{l.s.c.\ in norm}, then $F$ is weakly l.s.c.
		(sublevel sets are convex and weakly closed).
```

## CP-II-0501

- chapter line: 20219

```tex
\label{prob:cp-ii-0501}
Show that if $f:S^1\to\mathbb{R}$ is continuous then there exists $x\in S^1$
	such that $f(-x)=f(x)$.
	Deduce that at any moment there exist two antipodal points on the Earth's equator
	with the same temperature.


	\textbf{Theory.}
	This is the $n=1$ case of the \emph{Borsuk--Ulam theorem:}
	for every continuous $f:S^n\to\mathbb{R}^n$, there exists $x$ with $f(x)=f(-x)$.
	For $S^1=\{(\cos\theta,\sin\theta):\theta\in[0,2\pi)\}$,
	antipodal points correspond to $\theta$ and $\theta+\pi$.
	We will apply the Intermediate Value Theorem (IVT).
```

## CP-II-0503

- chapter line: 20311

```tex
\label{prob:cp-ii-0503}
\par\noindent\textbullet\quad \textbf{$\|\cdot\|_{1}$ is not a norm (only a seminorm).}
	Definiteness fails: let
	\[
	f(x)=\begin{cases}
		1, & x=0,\\
		0, & x\in (0,1],
	\end{cases}
	\]
	which is bounded and Riemann–integrable with $\int_{0}^{1}|f|=0$ but $f\not\equiv 0$.
	Hence $\|f\|_{1}=0\not\Rightarrow f=0$ on $R([0,1])$.
```

## CP-II-0504

- chapter line: 20325

```tex
\label{prob:cp-ii-0504}
{Polynomial step on a half-disk and on a half-plane}{poly-step}
	(i) Show that there exists a sequence of polynomials $(P_n)$ such that
	\[
	P_n(z)\longrightarrow
	\begin{cases}
		1,& |z|\le 1,\ \Re z\ge 0,\\[2pt]
		0,& |z|\le 1,\ \Re z<0,
	\end{cases}
	\quad\text{as }n\to\infty.
	\]
	(ii) Show that there exists a sequence of polynomials $(Q_n)$ such that
	\[
	Q_n(z)\longrightarrow
	\begin{cases}
		1,& \Re z\ge 0,\\[2pt]
		0,& \Re z<0,
	\end{cases}
	\quad\text{as }n\to\infty.
	\]
```

## CP-II-0505

- chapter line: 20348

```tex
\label{prob:cp-ii-0505}
\par\noindent\textbullet\quad For termwise differentiation, restrict to $|x|\le r<1$ and use uniform Dirichlet.
```

## CP-II-0507

- chapter line: 20353

```tex
\label{prob:cp-ii-0507}
If $X$ is a Hilbert space and $(x_i)$ is orthonormal, then $\Lambda(x)=\sum_i a_i\langle x,x_i\rangle$ works and
	$\|\Lambda\|=(\sum |a_i|^2)^{1/2}$.

	\bigskip
```

## CP-II-0509

- chapter line: 20361

```tex
\label{prob:cp-ii-0509}
Polynomial times Gaussian.

Let
\[
F(x,y) = (1+x^2)(1+y^2)e^{-x^2-y^2}.
\]
A direct computation gives
\[
\int_{\mathbb{R}}(1+t^2)e^{-t^2}dt = \frac{3\sqrt{\pi}}{2}.
\]
Thus
\[
\int_{\mathbb{R}}\Bigl|\int_{\mathbb{R}}F(x,y)\,dy\Bigr|dx
= \left(\frac{3\sqrt{\pi}}{2}\right)^2
= \frac{9\pi}{4},
\]
and the same value is obtained on the right--hand side.
```

## CP-II-0511

- chapter line: 20382

```tex
\label{prob:cp-ii-0511}
\par\noindent\textbullet\quad \textbf{Distance to a subspace.}
		For any closed subspace $M\subset X$ and $x\in X$,
		\[
		\operatorname{dist}(x,M)
		=\sup\{\,|\Lambda(x)|:\ \Lambda\in X',\ \|\Lambda\|\le1,\ \Lambda|_M=0\,\}.
		\]
```

## CP-II-0512

- chapter line: 20392

```tex
\label{prob:cp-ii-0512}
\par\noindent\textbullet\quad Using Young's inequality, apply it pointwise to
	$|f(x)|$ and $|g(x)|$:
	\[
	|f(x)g(x)|
	\le
	\frac{|f(x)|^p}{p} + \frac{|g(x)|^q}{q}.
	\]
```

## CP-II-0515

- chapter line: 20418

```tex
\label{prob:cp-ii-0515}
\par\noindent\textbullet\quad They vanish outside the interval $[-1,1]$.
```

## CP-II-0516

- chapter line: 20423

```tex
\label{prob:cp-ii-0516}
Oscillations without convergence (Not Cauchy)

$f_n(x)=\sin(nx)$ on $[0,2\pi]$.
No pointwise limit, not Cauchy.

---
```

## CP-II-0517

- chapter line: 20433

```tex
\label{prob:cp-ii-0517}
\renewcommand\labelenumi{(\alph{enumi})}
\par\noindent\textbullet\quad $f:\mathbb{R}\to\mathbb{R}^n$, $x\mapsto (x,0,\dots,0)^t$ is continuous: $\|f(x)-f(x_0)\|=|x-x_0|$.
\par\noindent\textbullet\quad For $A\subset\mathbb{R}^n$, $f=(f^1,\dots,f^m):A\to\mathbb{R}^m$ is continuous at $p$ iff each $f^k$ is continuous at $p$.
\par\noindent\textbullet\quad Any polynomial map $f:\mathbb{R}^n\to\mathbb{R}$ is continuous (built from projections via sums/products).
```

## CP-II-0518

- chapter line: 20441

```tex
\label{prob:cp-ii-0518}
— From $f(nx)\to0$ to $f(t)\to0$

Let $f:[1,\infty)\to\mathbb R$ be continuous and suppose $f(n x)\to0$ as $n\to\infty$ for each fixed $x\ge1$.
Show $f(t)\to0$ as $t\to\infty$.

Fix $\varepsilon>0$ and set $Q_k=\{x\ge1:\ |f(n x)|\le\varepsilon\ \forall n\ge k\}$.
Each $x\mapsto f(n x)$ is continuous, hence $Q_k=\bigcap_{n\ge k}\{x:\ |f(n x)|\le\varepsilon\}$ is closed.
By the assumption $[1,\infty)=\bigcup_{k\ge1} Q_k$. By Baire, some $Q_{k_0}$ contains an
interval $[a,b]\subset[1,\infty)$. For $t\ge T:=ab/(b-a)$, choose an integer
$n\in[t/b,\,t/a]$ (nonempty). Then $x:=t/n\in[a,b]\subset Q_{k_0}$ and with $n\ge k_0$
we have $|f(t)|=|f(n x)|\le\varepsilon$. Thus $f(t)\to0$ as $t\to\infty$.

\bigskip
```

## CP-II-0519

- chapter line: 20458

```tex
\label{prob:cp-ii-0519}
\par\noindent\textbullet\quad On $\ell^1,\ell^2,\ell^\infty$, for every $z$ we have
	$\|z\|_\infty\ge \|z\|_2\ge \|z\|_1$ (Hölder).
	If $x_n\to x$ in a stronger norm and $x_n\to y$ in a weaker norm,
	then $\|x-y\|\le \limsup_n \|x_n-x\|+\|x_n-y\|=0$, hence $x=y$.
```

## CP-II-0521

- chapter line: 20466

```tex
\label{prob:cp-ii-0521}
(Indicator of an interval; threshold $s<\tfrac12$ in 1D).

Let $f=\mathbf 1_{(0,1)}$ on $\mathbb R$. Then
\[
\widehat f(\xi)=e^{-i\xi/2}\,\frac{2\sin(\xi/2)}{\xi},\qquad
|\widehat f(\xi)|^2\sim \frac{4}{\xi^2}\ \ (|\xi|\to\infty).
\]
Therefore
\[
\|f\|_{H^s(\mathbb R)}^2\sim \int_{\mathbb R}(1+\xi^2)^s\,\frac{1}{\xi^2}\,d\xi<\infty
\iff s<\tfrac12.
\]
Equivalently, for $0<s<1$,
\[
[f]_{H^s(\mathbb R)}^2
=\iint_{\mathbb R^2}\frac{|f(x)-f(y)|^2}{|x-y|^{1+2s}}\,dx\,dy<\infty
\iff s<\tfrac12,
\]
since the only singular contribution comes from pairs $(x,y)$ straddling the endpoints.

\bigskip
```

## CP-II-0522

- chapter line: 20491

```tex
\label{prob:cp-ii-0522}
\par\noindent\textbullet\quad Show that if $\Re(\sigma)>0$, then
		\[
		\int_{\mathbb{R}} e^{-\sigma x^2 - i x \xi}\, dx
		= \sqrt{\frac{\pi}{\sigma}}\, e^{-\xi^2/(4\sigma)}.
		\]
```

## CP-II-0525

- chapter line: 20539

```tex
\label{prob:cp-ii-0525}
\par\noindent\textbullet\quad $\psi_{n,k}$ is supported on $I_{n,k}$ and has zero mean.
```

## CP-II-0526

- chapter line: 20544

```tex
\label{prob:cp-ii-0526}
With $\sqrt7\approx2.64575131$:
	\[
	\begin{array}{c|c|c|c|c|c}
		k & a_k & p_k & q_k & p_k/q_k & |\sqrt7-p_k/q_k| \\ \hline
		0 & 2 & 2   & 1  & 2                 & 6.46\times10^{-1} \\
		1 & 1 & 3   & 1  & 3                 & 3.54\times10^{-1} \\
		2 & 1 & 5   & 2  & 2.5               & 1.46\times10^{-1} \\
		3 & 1 & 8   & 3  & 2.666666\ldots    & 2.09\times10^{-2} \\
		4 & 4 & 37  & 14 & 2.642857\ldots    & 2.89\times10^{-3} \\
		5 & 1 & 45  & 17 & 2.647058\ldots    & 1.31\times10^{-3} \\
		6 & 1 & 82  & 31 & 2.645161\ldots    & 5.90\times10^{-4} \\
		7 & 1 & 127 & 48 & 2.645833\ldots    & 8.20\times10^{-5}
	\end{array}
	\]
	The bound $|\,\sqrt7-p_k/q_k\,|<1/(a_{k+1}q_k^2)$ holds row by row.
```

## CP-II-0527

- chapter line: 20563

```tex
\label{prob:cp-ii-0527}
\par\noindent\textbullet\quad \textbf{$\|\cdot\|_{1}$ is a norm on $C([0,1])$.} For $f,g\in C([0,1])$ and $\alpha\in\mathbb{R}$,
	\[
	\|f\|_{1}=\int_{0}^{1}|f|\ge 0,\qquad
	\|\alpha f\|_{1}=|\alpha|\,\|f\|_{1},\qquad
	\|f+g\|_{1}\le \|f\|_{1}+\|g\|_{1}.
	\]
	If $\|f\|_{1}=0$, then $|f|=0$ a.e.; by continuity, $f\equiv 0$. Hence $\|\cdot\|_{1}$ is a norm.
```

## CP-II-0529

- chapter line: 20574

```tex
\label{prob:cp-ii-0529}
(Gaussian is in all $H^s$).

Let $g(x)=e^{-|x|^2/2}$ on $\mathbb R^n$. Since $\widehat g(\xi)=(2\pi)^{n/2}e^{-|\xi|^2/2}$,
\[
\|g\|_{H^s(\mathbb R^n)}^2=(2\pi)^n\int_{\mathbb R^n}(1+|\xi|^2)^s e^{-|\xi|^2}\,d\xi<\infty
\]
for every $s\in\mathbb R$, hence $g\in H^s(\mathbb R^n)$ for all $s$.

\bigskip
```

## CP-II-0531

- chapter line: 20587

```tex
\label{prob:cp-ii-0531}
For $i\in\mathbb{N}$, define $f_i:[0,1]\to\mathbb{R}$ by
\[
f_i(x)=
\begin{cases}
2^i x, & 0\le x<2^{-i},\\[2pt]
2-2^i x, & 2^{-i}\le x<2^{-(i-1)},\\[2pt]
0, & x\ge 2^{-(i-1)}.
\end{cases}
\]

\renewcommand\labelenumi{(\alph{enumi})}
\par\noindent\textbullet\quad \textit{Sketch.} $f_i$ is a triangular ``spike'' supported on $[0,2^{-(i-1)}]$: it rises linearly
from $0$ at $x=0$ to height $1$ at $x=2^{-i}$, then decreases linearly back to $0$ at $x=2^{-(i-1)}$; afterwards it is identically $0$.
In particular, $\displaystyle \sup_{x\in[0,1]} f_i(x)=1$ for every $i$.

\par\noindent\textbullet\quad \textit{Pointwise limit.} For any fixed $x>0$ choose $I$ such that $2^{-(i-1)}<x$ for all $i\ge I$; then $f_i(x)=0$ for $i\ge I$.
Also $f_i(0)=0$ for all $i$. Hence $f_i(x)\to 0$ for every $x\in[0,1]$.

\par\noindent\textbullet\quad \textit{Interchange of $\lim$ and $\sup$.} We have
\[
\lim_{i\to\infty}\ \sup_{x\in[0,1]} f_i(x)
= \lim_{i\to\infty} 1 = 1,
\qquad\text{while}\qquad
\sup_{x\in[0,1]} \ \lim_{i\to\infty} f_i(x) = \sup_{x\in[0,1]} 0 = 0.
\]
Therefore the equality
\[
\lim_{i\to\infty} \sup_{x\in[0,1]} f_i(x) = \sup_{x\in[0,1]} \lim_{i\to\infty} f_i(x)
\]
is \emph{false} for this family. (This also shows $\{f_i\}$ does not converge uniformly to $0$.)
```

## CP-II-0537

- chapter line: 20718

```tex
\label{prob:cp-ii-0537}
\par\noindent\textbullet\quad The function $\phi(t)=e^t$ is convex and the logarithm is concave.
	The hint in part (b) suggests proving Young's inequality using
	concavity of $\log$.
```

## CP-II-0538

- chapter line: 20725

```tex
\label{prob:cp-ii-0538}
\par\noindent\textbullet\quad $\nu\perp\mu$ (\emph{mutual singularity}) means there exists $S\in\mathcal E$ with $\mu(S)=0$ and $\nu(E\setminus S)=0$.

	\par\medskip\noindent\textbf{$\sigma$-finiteness of Lebesgue measure on $\mathbb{R}^n$.}\quad
	Let $m$ denote Lebesgue measure on $\mathbb{R}^n$. For each $k\in\mathbb{N}$ set
	\[
	Q_k=[-k,k]^n.
	\]
	Then $m(Q_k)=(2k)^n<\infty$ and
	\[
	\mathbb{R}^n=\bigcup_{k=1}^\infty Q_k,
	\]
	so $m$ is $\sigma$-finite. Note that $\sigma$-finite \emph{does not} mean $m(\mathbb{R}^n)<\infty$; indeed $m(\mathbb{R}^n)=\infty$.

	\medskip

	If a disjoint cover is preferred, define
	\[
	A_1=[-1,1]^n,\qquad
	A_k=[-k,k]^n\setminus[-(k-1),k-1]^n\quad (k\ge2).
	\]
	Then $\mathbb{R}^n=\bigsqcup_{k=1}^\infty A_k$ with each $m(A_k)<\infty$, and
	\[
	m(\mathbb{R}^n)=\sum_{k=1}^\infty m(A_k)=\infty.
	\]
	This still exhibits $\sigma$-finiteness: a countable cover by finite-measure sets, even though the total measure is infinite.

	\bigskip

	If $\nu\ll\mu$ and both are finite (or $\sigma$-finite), then there exists $f\in L^1(\mu)$ such that
	\[
	\nu(A)=\int_A f\,d\mu \quad \text{for all }A\in\mathcal E,
	\]
	and we write $f=\frac{d\nu}{d\mu}$.

	\bigskip

	For finite (or $\sigma$-finite) measures $\mu,\nu$ on $(E,\mathcal E)$ there exist unique measures
	$\nu_a,\nu_s$ with
	\[
	\nu=\nu_a+\nu_s,\qquad \nu_a\ll\mu,\qquad \nu_s\perp\mu.
	\]

	\bigskip
```

## CP-II-0541

- chapter line: 20772

```tex
\label{prob:cp-ii-0541}
\par\noindent\textbullet\quad Standard mollifier: $\phi=c_n\,e^{-1/(1-|x|^2)}\mathbf 1_{|x|<1}$, $c_n$ normalizing.
```

## CP-II-0543

- chapter line: 20801

```tex
\label{prob:cp-ii-0543}
Suppose that $f:\mathbb{R}\to\mathbb{R}$ is defined by
\[
f(x) = x \quad\text{for } |x| < \tfrac12,
\qquad
f(x+1) = f(x).
\]
Show that
\[
f(x)
= \sum_{\substack{n\in\mathbb{Z}\\ n\neq 0}}
\frac{i(-1)^n}{2\pi n} e^{2\pi i n x}
= \sum_{n=1}^\infty \frac{(-1)^{n+1}}{n\pi}\sin(2\pi n x),
\]
with convergence in $L^2_{\mathrm{loc}}(\mathbb{R})$.

In Exercise~5.5 the function $f:\mathbb{R}\to\mathbb{R}$ is defined by
\[
f(x) = x \quad\text{for } |x|<\tfrac12,
\qquad f(x+1)=f(x),
\]
so that on each period $(-\tfrac12,\tfrac12)$ the graph of $f$ is a
straight line from $-1/2$ to $1/2$, followed by a jump back to $-1/2$.
The function $f$ is odd and belongs to $L^2([-1/2,1/2])$, hence defines
an element of $L^2(\mathbb{T})$.

For a $1$-periodic $L^2$ function, the complex Fourier coefficients are
given by
\[
\widehat{f}(n) = \int_{-1/2}^{1/2} f(x)\,e^{-2\pi i n x}\,dx,
\qquad n\in\mathbb{Z}.
\]
In this case $\widehat{f}(0)=\int_{-1/2}^{1/2}x\,dx=0$, and for
$n\neq 0$ an integration by parts shows that
\[
\widehat{f}(n)
= \int_{-1/2}^{1/2} x\,e^{-2\pi i n x}\,dx
= \frac{i(-1)^n}{2\pi n}.
\]
Thus the complex Fourier series of $f$ is
\[
f(x) = \sum_{\substack{n\in\mathbb{Z}\\ n\neq 0}}
\frac{i(-1)^n}{2\pi n}\,e^{2\pi i n x}
\]
with convergence in $L^2([-1/2,1/2])$, and hence in
$L^2_{\mathrm{loc}}(\mathbb{R})$.

Since $f$ is an odd function, only sine terms appear in the real Fourier
series
\[
f(x) = \sum_{n=1}^\infty b_n \sin(2\pi n x).
\]
A direct computation (or passage from the complex coefficients) gives
\[
b_n = 2\int_0^{1/2} x\sin(2\pi n x)\,dx
= \frac{2(-1)^{n+1}}{\pi n},
\]
so that
\[
f(x) = \sum_{n=1}^\infty \frac{(-1)^{n+1}}{n\pi}\,\sin(2\pi n x).
\]
Fourier theory on $L^2(\mathbb{T})$ ensures that this series converges
to $f$ in $L^2([-1/2,1/2])$, which is equivalent to convergence in
$L^2_{\mathrm{loc}}(\mathbb{R})$.  Pointwise, the series converges to
$f(x)$ at all continuity points of $f$, and to the midpoint of the jump
at the discontinuities, but the exercise only requires $L^2_{\mathrm{loc}}$
convergence.
```

## CP-II-0546

- chapter line: 20871

```tex
\label{prob:cp-ii-0546}
Let $A=[a_1,b_1]\times[a_2,b_2]$ and $|A|=(b_1-a_1)(b_2-a_2)$.
Suppose $f,g:A\to\mathbb{R}$ are integrable.

For a bounded function $f$ on $A$, let
\[
m=\inf_{x\in A} f(x), \quad M=\sup_{x\in A} f(x).
\]
Then $m\leq f(x)\leq M$ for all $x\in A$. Multiplying by the area $|A|$ and integrating yields inequalities for the integral.
Key facts:

	\par\noindent\textbullet\quad If $f\geq 0$, then $\int_A f\geq 0$.
	\par\noindent\textbullet\quad If $f\leq g$, then $\int_A f\leq \int_A g$.
	\par\noindent\textbullet\quad The triangle inequality: $\left|\int f\right|\leq \int |f|$.

	\par\noindent\textbullet\quad For all $x\in A$, $\inf_A f\leq f(x)\leq \sup_A f$.
	Integrating:
	\[
	|A|\inf_{x\in A} f(x)\;\leq\;\int_A f(x)\,dx\;\leq\;|A|\sup_{x\in A} f(x).
	\]

	\par\noindent\textbullet\quad Applying (a) to both $f$ and $-f$:
	\[
	-|A|\sup_{x\in A}|f(x)|\leq \int_A f(x)\,dx \leq |A|\sup_{x\in A}|f(x)|.
	\]
	Thus
	\[
	\left|\int_A f(x)\,dx\right|\leq |A|\sup_{x\in A}|f(x)|.
	\]

	\par\noindent\textbullet\quad If $f(x)\geq 0$, then $\inf_A f\geq 0$. By (a),
	\[
	0\leq \int_A f(x)\,dx.
	\]

	\par\noindent\textbullet\quad If $f(x)\leq g(x)$, then $0\leq g(x)-f(x)$.
	By (c),
	\[
	0\leq \int_A (g-f)=\int_A g-\int_A f,
	\]
	so
	\[
	\int_A f \leq \int_A g.
	\]

	\par\noindent\textbullet\quad Since $-f(x)\leq |f(x)|$ and $f(x)\leq |f(x)|$, integrating gives
	\[
	-\int_A |f|\leq \int_A f \leq \int_A |f|.
	\]
	Thus
	\[
	\left|\int_A f(x)\,dx\right|\leq \int_A |f(x)|\,dx.
	\]
```

## CP-II-0553

- chapter line: 20927

```tex
\label{prob:cp-ii-0553}
\par\noindent\textbullet\quad if $x,y\ge R$: then
	\[
	\lvert f(x)-f(y)\rvert
	\le \lvert f(x)-L\rvert+\lvert f(y)-L\rvert
	< \tfrac{\varepsilon}{3}+\tfrac{\varepsilon}{3}
	< \varepsilon;
	\]
```

## CP-II-0556

- chapter line: 20985

```tex
\label{prob:cp-ii-0556}
\par\noindent\textbullet\quad Need convergence of $\sum n|a_n|$ only if you want uniform convergence of $f'$ on all of $(-1,1)$.

\begin{tcolorbox}[title=Abel–Dirichlet Cheat-Sheet,colback=white,colframe=black,
	fonttitle=\bfseries,boxsep=4pt,arc=2pt]

	For sequences $(a_n),(b_n)$ and $S_n=\sum_{k=0}^n a_k$ (with $S_{-1}:=0$), for $0\le m\le N$,
	\[
	\sum_{n=m}^N a_n b_n
	= S_N b_N - S_{m-1} b_m - \sum_{n=m}^{N-1} S_n\,(b_{n+1}-b_n).
	\]
	\textit{Power–series form (Abel transform).} For $x\in\mathbb R$,
	\[
	\sum_{n=0}^N a_n x^n=(1-x)\sum_{n=0}^N S_n x^n + S_N x^{N+1}. \tag{A}
	\]

	If $(S_n)$ is bounded and $(b_n)$ is monotone with $b_n\!\to\!0$, then $\sum a_n b_n$ converges.\\
	\textit{One-line proof via Abel:} apply the identity above with $m=0$, $B_N:=b_N\!\to\!0$ and
	$\sum S_n(b_{n+1}-b_n)$ absolutely bounded by $\sup|S_n|\,\sum|b_{n+1}-b_n| \le \sup|S_n|\,(|b_0|+|B_N|)$.

	If $\sup_n|S_n|\le M$ and for each $x\in E$ the sequence $b_n(x)$ is monotone in $n$ with
	$\sup_{x\in E}|b_n(x)|\to0$, then $\sum a_n b_n(x)$ converges \emph{uniformly} on $E$.
	In particular, for any fixed $r\in(0,1)$, $\sum a_n x^n$ converges uniformly on $[0,r]$ and on $[r,1)$.

	If $\sum_{n\ge0} a_n$ converges and $f(x)=\sum_{n\ge0} a_n x^n$ on $[0,1)$, then
	\[
	\lim_{x\to1^-} f(x)=\sum_{n=0}^\infty a_n.
	\]
	\textit{Sketch via (A):} $f(x)=(1-x)\sum S_n x^n$, with bounded $(S_n)$ and the kernel $(1-x)\sum x^n=1$.

	If $\sum a_n$ converges, then for each $r\in(0,1)$ the series
	$\sum a_n x^n$ and $\sum n a_n x^{n-1}$ converge uniformly on $[-r,r]$.
	Hence $f(x)=\sum a_n x^n$ is $C^1$ on $(-1,1)$ with $f'(x)=\sum n a_n x^{n-1}$.

	Use (A) near $x=1$; Dirichlet for $|x|<1$; uniform Dirichlet on compact subintervals; require $\sum n|a_n|<\infty$
	only for \emph{uniform} convergence of $f'$ on all $(-1,1)$.
\end{tcolorbox}
```

## CP-II-0557

- chapter line: 21025

```tex
\label{prob:cp-ii-0557}
\par\noindent\textbullet\quad Scaling $f$ and $g$ yields the general form of Hölder's inequality:
	\[
	\int_{\mathbb{R}^n} |f(x)g(x)|\,dx
	\;\le\;
	\|f\|_{L^p}\,\|g\|_{L^q}.
	\]
```

## CP-II-0558

- chapter line: 21035

```tex
\label{prob:cp-ii-0558}
\par\noindent\textbullet\quad $\nu\ll\mu$ (\emph{absolute continuity}) means $\mu(A)=0\Rightarrow \nu(A)=0$ for all $A\in\mathcal E$.
```

## CP-II-0560

- chapter line: 21040

```tex
\label{prob:cp-ii-0560}
— Uniform Limit of Uniformly Continuous Functions

If $(f_n)$ are uniformly continuous on $\mathbb R$ and $f_n\to f$ uniformly, show $f$ is uniformly continuous.
Give $(f_n)$ uniformly continuous with pointwise $f_n\to f$ where $f$ is continuous but not uniformly continuous.

Fix $\varepsilon>0$. Take $N$ with $\|f_N-f\|_\infty<\varepsilon/3$ and $\delta>0$ for uniform continuity of $f_N$
so that $|x-y|<\delta\Rightarrow |f_N(x)-f_N(y)|<\varepsilon/3$.
Then for $|x-y|<\delta$,
\[
|f(x)-f(y)|\le |f(x)-f_N(x)|+|f_N(x)-f_N(y)|+|f_N(y)-f(x)|<\varepsilon.
\]

Let $\mathrm{clip}_n(x)=\max(-n,\min(x,n))$ and
\[
f_n(x)=\sin\!\big(\mathrm{clip}_n(x)^2\big).
\]
Then $f_n$ is globally Lipschitz (hence uniformly continuous), and for each fixed $x$, if $n>|x|$ then $f_n(x)=\sin(x^2)$.
Thus $f_n\to f$ pointwise with $f(x)=\sin(x^2)$, which is continuous but not uniformly continuous on $\mathbb R$.

\begin{center}

\end{center}
\noindent
\textit{Figure.} The clipped functions $f_n(x)=\sin(\mathrm{clip}_n(x)^2)$.
Each $f_n$ agrees with $\sin(x^2)$ on $[-n,n]$ and becomes constant outside, so $f_n$ are uniformly continuous
yet converge pointwise to the non–uniformly continuous limit $\sin(x^2)$.

\bigskip
```

## CP-II-0561

- chapter line: 21072

```tex
\label{prob:cp-ii-0561}
Metrics and small balls

For each of the following sets $X$, determine whether the given function $d$ defines a metric on $X$.
In each case where the function does define a metric, describe the open ball $B_\varepsilon(x)$
for $x\in X$ and $\varepsilon>0$ small.

	\par\noindent\textbullet\quad $X=\mathbb{R}^n$; \quad $d(x,y)=\min\{|x_1-y_1|,\ |x_2-y_2|,\ \ldots,\ |x_n-y_n|\}$.
	\par\noindent\textbullet\quad $X=\mathbb{Z}$; \quad $d(x,x)=0$, and, for $x\neq y$, $d(x,y)=2^{n}$ where $x-y=2^{n}a$ with
	$n$ a non–negative integer and $a$ an odd integer.
	\par\noindent\textbullet\quad $X$ is the set of functions from $\mathbb{N}$ to $\mathbb{N}$; \quad $d(f,f)=0$, and, for $f\neq g$,
	$d(f,g)=2^{-n}$ for the least $n$ such that $f(n)\neq g(n)$.
	\par\noindent\textbullet\quad $X=\mathbb{C}$; \quad $d(z,w)=|z-w|$ if $z$ and $w$ lie on the same line through the origin,
	and $d(z,w)=|z|+|w|$ otherwise.

\par\medskip\noindent\textbf{(i) $X=\mathbb{R}^n$, $d(x,y)=\min\{|x_1-y_1|,\dots,|x_n-y_n|\}$.}\quad
Not a metric: identity fails since $x\neq y$ may share a coordinate, giving $d(x,y)=0$.

\par\medskip\noindent\textbf{(ii) $X=\mathbb{Z}$, $d(x,x)=0$, and for $x\neq y$, $d(x,y)=2^{n}$ where $x-y=2^{n}a$ with $n\ge0$, $a$ odd.}\quad
Let $\nu_2(k)$ be the exponent of $2$ in $k\neq0$. Then $d(x,y)=2^{\nu_2(x-y)}$.
For all $x,y,z$,
\[
\nu_2(x-z)\ge \min\{\nu_2(x-y),\nu_2(y-z)\}\quad\Rightarrow\quad
d(x,z)\le \max\{d(x,y),d(y,z)\}.
\]
Hence $d$ is an ultrametric. Small balls:
\[
B_\varepsilon(x)=\{y\in\mathbb Z:\ d(x,y)<\varepsilon\}=
\begin{cases}
	\{x\}, & 0<\varepsilon\le 1,\\[2mm]
	\{y:\ x-y\ \text{odd}\}, & 1<\varepsilon\le 2,\\[1mm]
	\{y:\ x-y\not\equiv 0\pmod{4}\}, & 2<\varepsilon\le 4,\\[1mm]
	\vdots\\
	\{y:\ \nu_2(x-y)\le k\}=\mathbb Z\setminus (x+2^{k+1}\mathbb Z), & 2^{k}<\varepsilon\le 2^{k+1}.
\end{cases}
\]

\par\medskip\noindent\textbf{(iii) $X=\mathbb{N}^{\mathbb{N}}$ (functions $\mathbb{N}\to\mathbb{N}$).}\quad
\[
d(f,f)=0,\qquad
\text{and for } f\neq g,\quad d(f,g)=2^{-n},
\quad \text{where } n=\min\{k:\ f(k)\neq g(k)\}.
\]

This is a \emph{metric} (in fact, an ultrametric).

	\par\noindent\textbullet\quad If $n_{fg}$ is the first index where $f$ and $g$ differ, then for any $h$,
	\[
	n_{fh}\ge \min\{n_{fg},n_{gh}\},
	\]
	and hence
	\[
	d(f,h)=2^{-n_{fh}}\le \max\{2^{-n_{fg}},2^{-n_{gh}}\}
	=\max\{d(f,g),d(g,h)\}.
	\]

\noindent\hrulefill

Distances take values $2^{-1},2^{-2},\dots$.
For $\varepsilon\in(2^{-(m+1)},2^{-m}]$ ($m\ge0$),
\[
B_\varepsilon(f)=\{g:\ g(k)=f(k)\ \text{for all } k\le m\}.
\]
Equivalently, with $N=\lfloor\log_2(1/\varepsilon)\rfloor$,
\[
B_\varepsilon(f)=\{g:\ g|_{\{1,\dots,N\}}=f|_{\{1,\dots,N\}}\}.
\]

\[
d(z,w)=
\begin{cases}
	|z-w|, & \text{if $z,w$ lie on the same line through the origin (i.e.\ } w\in \mathbb R z),\\[2mm]
	|z|+|w|, & \text{otherwise.}
\end{cases}
\]

This is a \emph{metric}.

	\par\noindent\textbullet\quad \textbf{Symmetry/positivity.} Clear; and $d(z,w)=0 \Rightarrow z=w$.
	\par\noindent\textbullet\quad \textbf{Triangle inequality.}
	If $z,w$ are not colinear with the origin then $d(z,w)=|z|+|w|$.
	For any $u\in\mathbb C$,
	\[
	d(z,u)\ge |z-u|,\qquad d(u,w)\ge |u-w|
	\]
	(if colinear we have equality with the Euclidean distance; otherwise the value is
	$|\,\cdot\,|+|\,\cdot\,|$, which dominates $|\,\cdot-\cdot\,|$ via
	$|u|+|w|\ge |\,u-w\,|$). Hence
	\[
	d(z,u)+d(u,w)\ \ge\ |z-u|+|u-w|\ \ge\ |z-w|.
	\]
	When $z,w$ are colinear, the rightmost term equals $d(z,w)=|z-w|$, giving the inequality.
	When $z,w$ are non–colinear, $d(z,w)=|z|+|w| \le d(z,u)+d(u,w)$ since in every case
	$d(v,u)\ge \big||v|-|u|\big|$ and at least one summand is $\ge |v|+|u|$.

\noindent\hrulefill

  Fix $z\in\mathbb C$ and $\varepsilon>0$.
\[
B_\varepsilon(z)=
\underbrace{\{\,w\in\mathbb C:\ w\in \mathbb R z\ \text{and}\ |w-z|<\varepsilon\,\}}_{\text{points on the same line as }z}
\ \ \cup\ \
\underbrace{\{\,w\notin \mathbb R z:\ |z|+|w|<\varepsilon\,\}}_{\text{off-line points}}.
\]

Thus:

	\par\noindent\textbullet\quad If $\varepsilon\le |z|$: the second set is empty; $B_\varepsilon(z)$ is the open interval
	of length $2\varepsilon$ on the line $\mathbb R z$ centered at $z$.
	\par\noindent\textbullet\quad If $\varepsilon>|z|$: in addition you get the Euclidean disk
	$\{\,w:\ |w|<\varepsilon-|z|\,\}$ consisting of all off-line points sufficiently
	close to the origin.
```

## CP-II-0563

- chapter line: 21204

```tex
\label{prob:cp-ii-0563}
$^\ast$ — A Nowhere Differentiable Continuous Function

Let $\varphi(x)=|x|$ for $x\in[-1,1]$ and extend to $\mathbb R$ by $\varphi(x+2)=\varphi(x)$.

	\par\noindent\textbullet\quad \textbf{$\varphi$ is 1-Lipschitz.} On each interval between consecutive integers $\varphi$ is linear with slope $\pm1$, hence
	$|\varphi(s)-\varphi(t)|\le|s-t|$ for all $s,t$.
	\par\noindent\textbullet\quad Define $f(x)=\sum_{n=0}^\infty (3/4)^n\varphi(4^n x)$. Since $0\le\varphi\le1$, the Weierstrass M–test shows uniform convergence, so $f$ is continuous.
	\par\noindent\textbullet\quad Fix $x\in\mathbb R$ and $m\in\mathbb N$. Put $\delta_m=\pm \tfrac12 4^{-m}$ with the sign so that no integer lies between $4^m x$ and $4^m(x+\delta_m)$. Then
	\[
	\big|\varphi(4^m(x+\delta_m))-\varphi(4^m x)\big|=|4^m\delta_m|=\tfrac12,
	\]
	while for $n<m$,
	\[
	\big|\varphi(4^n(x+\delta_m))-\varphi(4^n x)\big|\le |4^n\delta_m|=\tfrac12\,4^{\,n-m},
	\]
	and for $n\ge m+1$ we have $4^n\delta_m\in 2\mathbb Z$ so by $2$–periodicity the difference is $0$.
	Therefore,
	\[
	\begin{aligned}
		\big|f(x+\delta_m)-f(x)\big|
		&\ge \Big(\frac{3}{4}\Big)^m\frac12
		- \sum_{n=0}^{m-1}\Big(\frac{3}{4}\Big)^n \frac12\,4^{\,n-m} \\
		&= \frac{1}{2}\,4^{-m}\!\left(3^m-\sum_{n=0}^{m-1}3^n\right)
		= \frac{1}{2}\,4^{-m}\cdot\frac{3^m+1}{2}.
	\end{aligned}
	\]
	Dividing by $|\delta_m|=\tfrac12\,4^{-m}$ yields
	\[
	\left|\frac{f(x+\delta_m)-f(x)}{\delta_m}\right|\ge \frac12\,(3^m+1).
	\]
	Letting $m\to\infty$ shows $f$ is not differentiable at $x$. Since $x$ was arbitrary, $f$ is continuous and nowhere differentiable.

\begin{center}

\end{center}
\noindent
\textit{Figure.} The triangular wave $\varphi(x)=|x|$ periodically extended by
$\varphi(x+2)=\varphi(x)$.  This Lipschitz function forms the building block in the
definition of the Weierstrass–type nowhere differentiable function
$f(x)=\sum_{n=0}^\infty \big(\tfrac34\big)^n \varphi(4^n x)$.
```

## CP-II-0566

- chapter line: 21248

```tex
\label{prob:cp-ii-0566}
Fix $p\in[1,\infty)$ and set $f(x)=x^{-1/p}\mathbf{1}_{(0,1)}(x)$.
	Then for $\lambda\ge 1$,
	\[
	\{|f|>\lambda\}=\{x<\lambda^{-p}\},\qquad
	\mu(\{|f|>\lambda\})=\lambda^{-p}.
	\]
	Hence
	\[
	\|f\|_{p,\infty}
	=\sup_{\lambda>0}\lambda(\lambda^{-p})^{1/p}=1.
	\]
	Thus $f\in L^{p,\infty}(0,1)$, but
	\[
	\int_0^1 |f|^p\,dx
	= \int_0^1 x^{-1}\,dx = \infty,
	\]
	so $f\notin L^p(0,1)$.
```

## CP-II-0018

- chapter line: 21316

```tex
\label{prob:cp-ii-0018}
Take three nodes $z_0=-i$, $z_1=1$, $z_2=i$ on $K$ (angles $-\tfrac\pi2,0,\tfrac\pi2$).
	Then
	\[
	p_2(z)=\sum_{k=0}^{2}\frac{1}{z_k}\,\ell_k(z)
	= i\,\ell_0(z)+1\cdot \ell_1(z)-i\,\ell_2(z)
	\quad\Rightarrow\quad
	\boxed{\,p_2(z)=z^2 - z + 1\,}.
	\]
	Indeed $p_2(1)=1$, $p_2(i)=-i$, $p_2(-i)=i$ (matching $1/z$ at the nodes). On $K$,
	$\big|p_2(e^{it})-e^{-it}\big|
	=\sqrt{\big(\cos2t+1-2\cos t\big)^2+\big(\sin2t\big)^2}$,
	so the uniform error already is modest and will decay rapidly as $n$ grows.
```

## CP-II-0098

- chapter line: 21435

```tex
\label{prob:cp-ii-0098}
the interval $(0,\pi)$

Take $\Omega=(0,\pi)\subset\mathbb{R}$. Then
$H_0^1(0,\pi)$ consists of $L^2$-functions with square-integrable weak
derivative and zero trace at $0$ and $\pi$.

The eigenfunctions of the Dirichlet Laplacian are
\[
w_k(x) = \sqrt{\frac{2}{\pi}}\sin(kx),\qquad k=1,2,\dots,
\]
and they satisfy
\[
-w_k'' = k^2 w_k,\qquad \|w_k\|_{L^2(0,\pi)}=1.
\]
Hence the eigenvalues are $\lambda_k = k^2$. In particular,
$\lambda_1=1$ and Poincar\'e's inequality becomes
\[
\int_0^\pi |u(x)|^2\,dx \le \int_0^\pi |u'(x)|^2\,dx,
\qquad u\in H_0^1(0,\pi),
\]
with equality for multiples of $\sin x$.

On the interval $\Omega=(0,\pi)$ the normalised Dirichlet eigenfunctions and
eigenvalues are
\[
w_k(x) = \sqrt{\frac{2}{\pi}}\sin(kx),
\qquad -w_k'' = \lambda_k w_k,
\qquad \lambda_k = k^2,\quad k=1,2,\dots
\]
The first eigenfunction $w_1$ has a single bump and no interior zero, while
$w_2$ has two bumps and one interior zero at $x=\pi/2$. Both vanish at the
endpoints, corresponding to the Dirichlet boundary conditions. The associated
eigenvalues form a sequence of ``energy levels'' $1,4,9,16,\dots$ which grow
quadratically with $k$.

To visualise this, it is convenient to place a plot of the first two
eigenfunctions next to a simple diagram of the first few eigenvalues. Using
\texttt{pgfplots} one may use the following code.\footnote{Make sure to load
	\texttt{\textbackslash usepackage\{pgfplots\}} and set a compatible version,
	e.g.\ \texttt{\textbackslash pgfplotsset\{compat=1.18\}}.}

On the interval $(0,\pi)$ the Dirichlet Laplacian is the operator
\[
A = -\frac{d^2}{dx^2}, \qquad
D(A) = \{u\in H^2(0,\pi)\cap H_0^1(0,\pi)\}.
\]
Viewed as an operator on $L^2(0,\pi)$ it is self--adjoint and positive. Its
spectrum consists entirely of eigenvalues and is given by
\[
\sigma(A) = \{\lambda_k : k\in\mathbb{N}\},
\qquad \lambda_k = k^2.
\]
There is no continuous spectrum. The associated eigenfunctions $w_k$ form an
orthonormal basis of $L^2(0,\pi)$, so every $u\in L^2(0,\pi)$ admits the
expansion
\[
u(x) = \sum_{k=1}^\infty c_k w_k(x), \qquad
c_k = (u,w_k)_{L^2(0,\pi)}.
\]
For such $u$ in the domain of $A$ one has
\[
Au = -u'' = \sum_{k=1}^\infty \lambda_k c_k w_k
\]
and the Dirichlet energy may be written in spectral form as
\[
E[u] = \int_0^\pi |u'(x)|^2\,dx
= \sum_{k=1}^\infty \lambda_k |c_k|^2.
\]

In the general case of a bounded domain $\Omega\subset\mathbb{R}^n$ with
sufficiently regular boundary, the Dirichlet Laplacian
\[
A = -\Delta, \qquad
D(A) = \{u\in H_0^1(\Omega):\Delta u\in L^2(\Omega)\},
\]
is again self--adjoint and positive on $L^2(\Omega)$. Its spectrum consists of a
discrete sequence of eigenvalues
\[
0 < \lambda_1 \le \lambda_2 \le \cdots, \qquad
\lambda_k \to \infty \text{ as } k\to\infty,
\]
each with finite multiplicity, and an orthonormal basis of $L^2(\Omega)$ made
of smooth eigenfunctions. The first eigenvalue admits the Rayleigh--Ritz
characterisation
\[
\lambda_1
= \inf_{u\in H_0^1(\Omega)\setminus\{0\}}
\frac{\displaystyle\int_\Omega |Du|^2\,dx}
{\displaystyle\int_\Omega |u|^2\,dx},
\]
and the strict inequality $\lambda_1>0$ expresses Poincar\'e's inequality as a
spectral gap between $0$ and the bottom of the spectrum.
```

## CP-II-0112

- chapter line: 21531

```tex
\label{prob:cp-ii-0112}
For
\[
A=
\begin{pmatrix}
	2&1&1\\
	1&2&1\\
	1&1&2
\end{pmatrix},
\quad
F(x)=\frac{Ax}{\mathbf{1}^\top Ax}.
\]
We have $A(1,1,1)^\top=4(1,1,1)^\top$, so the fixed point in $T$ is
$x^\ast=(\tfrac13,\tfrac13,\tfrac13)$ with eigenvalue $\lambda=4$, and all entries are positive.
```

## CP-II-0159

- chapter line: 21586

```tex
\label{prob:cp-ii-0159}
constant right-hand side

If $f(\theta)\equiv 1$, the equation becomes
\[
\psi''(\theta) = -1 + \psi(\theta),
\]
that is $(\psi''-\psi)(\theta)=-1$ with $\psi$ $2\pi$-periodic. Solving
the ordinary differential equation gives
\[
\psi(\theta) = 1 + A e^\theta + B e^{-\theta}.
\]
The $2\pi$-periodicity forces $A=B=0$, so the unique periodic solution is
$\psi(\theta)\equiv 1$, which agrees with the integral representation of
$\psi$ for the constant function $f\equiv1$.

\bigskip
\noindent\rule{\textwidth}{0.4pt}
\medskip
```

## CP-II-0174

- chapter line: 21608

```tex
\label{prob:cp-ii-0174}
Let $K=\{|z|=1,\ \Re z\ge0\}$ and choose nodes $z_0=-i$, $z_1=1$, $z_2=i$.
	The Lagrange interpolant to $f(z)=1/z$ is
	\[
	p_2(z)=\sum_{k=0}^2 \frac{1}{z_k}\prod_{j\ne k}\frac{z-z_j}{z_k-z_j}
	= z^2 - z + 1.
	\]
	Hence $p_2(1)=1$, $p_2(i)=-i$, $p_2(-i)=i$, i.e.\ $p_2$ matches $1/z$ at the
	three orange nodes on the arc. For general $n$, pick $n{+}1$ nodes on $K$,
	form $p_n$ by the same formula; then $p_n\to 1/z$ uniformly on $K$.
```

## CP-II-0238

- chapter line: 21727

```tex
\label{prob:cp-ii-0238}
(Lefschetz map on a compact manifold has finitely many fixed points)

\textbf{Statement.} Let $f:X\to X$ be smooth. Assume that for every fixed point $x$ of $f$,
the linear map $Df_x:T_xX\to T_xX$ does not have $1$ as an eigenvalue.
Prove: if $X$ is compact and $f$ is Lefschetz, then $f$ has only finitely many fixed points.

\medskip
```

## CP-II-0242

- chapter line: 21738

```tex
\label{prob:cp-ii-0242}
If $K$ is a line segment inside $D$ not containing $x$, then $f_x(K)$ is the arc of the circle that subtends the segment with respect to $x$.
If $K=D\setminus \{x\}$, then $f_x(K)=\partial D$.
```

## CP-II-0278

- chapter line: 21744

```tex
\label{prob:cp-ii-0278}
- Weighted sup norm; Picard operator as a contraction

Let $F:[a,b]\times\mathbb{R}^n\to\mathbb{R}^n$ be continuous and Lipschitz in $x$
with constant $L$.
Define $(Tf)(t)=x_0+\int_a^t F(s,f(s))\,ds$ on $C([a,b];\mathbb{R}^n)$.
Under the weighted norm
\[
\|f\|_\alpha=\sup_{t\in[a,b]}e^{-\alpha(t-a)}\|f(t)\|,
\]
we have
\[
\|Tf-Tg\|_\alpha\le \frac{L}{\alpha}\|f-g\|_\alpha.
\]
Thus $T$ is a contraction whenever $\alpha>L$.

If $F(t,x)=x$ on $[0,2]$, then $L=1$.
In the standard sup norm, $L(b-a)=2>1$, so $T$ is not a contraction.
With $\alpha=2$, $\frac{L}{\alpha}=\frac12<1$, so $T$ is a contraction.
\hfill$\Box$

\bigskip\hrule\bigskip
```

## CP-II-0311

- chapter line: 21769

```tex
\label{prob:cp-ii-0311}
Let $q\ge 2$, $n\ge 1$, and $Q$ be the set of unordered $q$-tuples (multisets) of points in $\mathbb{R}^n$.
For $X=\{x_1,\dots,x_q\}$ and $Y=\{y_1,\dots,y_q\}$ define
\[
\mathcal{G}(X,Y)=\inf_{\sigma\in S_q}
\Big(\sum_{j=1}^q \|y_j-x_{\sigma(j)}\|^2\Big)^{1/2}.
\]

\subsection*{(i) $\mathcal{G}$ is a metric on $Q$}
It is permutation-invariant (hence well-defined on multisets), nonnegative and symmetric.
If $\mathcal{G}(X,Y)=0$ there exists $\sigma$ with $\|y_j-x_{\sigma(j)}\|=0$ for all $j$, so $X=Y$ as multisets. Conversely, $X=Y \Rightarrow \mathcal{G}(X,Y)=0$.
For the triangle inequality, for any $\sigma,\pi\in S_q$ and any $X,Y,Z$,
\[
\begin{aligned}
	\Big(\sum_{j}\|x_{\sigma(j)}-z_{\pi(j)}\|^2\Big)^{1/2}
	&=\Big(\sum_{j}\|(x_{\sigma(j)}-y_j)+(y_j-z_{\pi(j)})\|^2\Big)^{1/2}\\
	&\le \Big(\sum_{j}\|x_{\sigma(j)}-y_j\|^2\Big)^{1/2}
	+ \Big(\sum_{j}\|y_j-z_{\pi(j)}\|^2\Big)^{1/2}.
\end{aligned}
\]
Taking infima over $\sigma,\pi$ yields $\mathcal{G}(X,Z)\le \mathcal{G}(X,Y)+\mathcal{G}(Y,Z)$.
Hence $\mathcal{G}$ is a metric.

Assume $x_1\le\cdots\le x_q$ and $y_1\le\cdots\le y_q$. If a permutation $\sigma$ has a crossing (i.e.\ $i<k$ but $\sigma(i)>\sigma(k)$), then
\[
(x_i-y_{\sigma(i)})^2+(x_k-y_{\sigma(k)})^2
-(x_i-y_{\sigma(k)})^2-(x_k-y_{\sigma(i)})^2
=2(x_k-x_i)\big(y_{\sigma(i)}-y_{\sigma(k)}\big)\ge0,
\]
so swapping these two pairs does not increase the cost. Iterating removes all crossings; the minimum is attained at the identity permutation. Thus
\[
\mathcal{G}(\{x_1,\dots,x_q\},\{y_1,\dots,y_q\})
=\Big(\sum_{j=1}^q (x_j-y_j)^2\Big)^{1/2}.
\]
```

## CP-II-0315

- chapter line: 21806

```tex
\label{prob:cp-ii-0315}
— Weak-$^\ast$ limit of difference quotients of distributions

Let $X\in\{\mathcal D(\mathbb R^n),\mathcal S(\mathbb R^n),\mathcal E(\mathbb R^n)\}$.
For $u\in X'$ and $x\in\mathbb R^n$ define $\tau_x u$ by $(\tau_x u)[\phi]=u[\tau_{-x}\phi]$ for all $\phi\in X$.
Let $\Delta_i^{h}u:=h^{-1}(\tau_{h e_i}u-u)$. Show that $\Delta_i^{h}u\to D_i u$ as $h\to0$ in the weak-$^\ast$ topology $\sigma(X',X)$.

For any $\phi\in X$,
\[
(\Delta_i^{h}u)[\phi]
=\frac{u[\tau_{-h e_i}\phi]-u[\phi]}{h}
=u\!\left[\frac{\tau_{-h e_i}\phi-\phi}{h}\right]
=-\,u\!\left[\frac{\tau_{h e_i}\phi-\phi}{h}\right]
=-\,u[\Delta_i^{h}\phi].
\]
By Problem~2(b), $\Delta_i^{h}\phi\to D_i\phi$ in $X$. Since $u\in X'$ is continuous,
\[
(\Delta_i^{h}u)[\phi]=-u[\Delta_i^{h}\phi]\longrightarrow -u[D_i\phi]
= D_i u[\phi],
\]
where $D_i u[\phi]:=-u[D_i\phi]$. Hence $\Delta_i^{h}u\to D_i u$ in $\sigma(X',X)$.

\bigskip

\textbf{Example 1 (regular distributions).}
Let $u=u_f$ be induced by $f\in L^1_{\mathrm{loc}}(\mathbb R^n)$, i.e.
$u_f[\phi]=\int_{\mathbb R^n} f(x)\,\phi(x)\,dx$.
Then
\[
(\Delta_i^{h}u_f)[\phi]
=-\,u_f[\Delta_i^{h}\phi]
=-\int_{\mathbb R^n} f(x)\,\frac{\phi(x-h e_i)-\phi(x)}{h}\,dx.
\]
If $f\in W^{1,1}_{\mathrm{loc}}$ one may integrate by parts:
\[
(\Delta_i^{h}u_f)[\phi]
=\int_{\mathbb R^n} \frac{f(x)-f(x+h e_i)}{h}\,\phi(x)\,dx
\longrightarrow -\int_{\mathbb R^n} (\partial_i f)(x)\,\phi(x)\,dx
= D_i u_f[\phi].
\]
In general (for $f\in L^1_{\mathrm{loc}}$ only), the limit still equals $D_i u_f[\phi]$ because
$\Delta_i^{h}\phi\to D_i\phi$ in $X$ and $u_f$ is continuous on $X$ (here $X=\mathcal D,\mathcal S,\mathcal E$ accordingly).

\medskip

\textbf{Example 2 (Dirac mass).}
For the Dirac distribution,
\[
(\Delta_i^{h}\delta)[\phi]
=\frac{\delta[\tau_{-h e_i}\phi]-\delta[\phi]}{h}
=\frac{\phi(h e_i)-\phi(0)}{h}
\longrightarrow \partial_i\phi(0)
= -\,D_i\delta[\phi].
\]
Hence $\Delta_i^{h}\delta \to D_i\delta$ in $\sigma(X',X)$, as required.

\medskip

\textbf{Example 3 (finite sums of shifted deltas).}
Let $u=\sum_{j=1}^m c_j\,\delta_{a_j}$ with fixed points $a_j\in\mathbb R^n$.
Then
\[
(\Delta_i^{h}u)[\phi]
=\sum_{j=1}^m c_j\frac{\phi(a_j+h e_i)-\phi(a_j)}{h}
\longrightarrow \sum_{j=1}^m c_j\,\partial_i\phi(a_j)
= -\,\sum_{j=1}^m c_j\, D_i\delta_{a_j}[\phi],
\]
so $\Delta_i^{h}u\to \sum_j c_j\,D_i\delta_{a_j}$ weak-$^\ast$.

\bigskip

If $u$ is induced by $f\in L^1_{\mathrm{loc}}$, then
$(\Delta_i^{h}u)[\phi]=-\int \Delta_i^{h}\phi\,f\to -\int D_i\phi\,f=D_i u[\phi]$.
For $u=\delta$, $\Delta_i^{h}\delta=\big(\delta(\cdot-he_i)-\delta\big)/h\to D_i\delta$ weak-$^\ast$.

\bigskip
\bigskip
```

## CP-II-0349

- chapter line: 21974

```tex
\label{prob:cp-ii-0349}
Weighted sup norm; Picard operator as a contraction

Let $I=[0,R]$ be an interval and let $C(I)$ be the space of continuous functions on $I$.
Show that, for any $\alpha\in\mathbb{R}$, we may define a norm by
\[
\|f\|_\alpha=\sup_{x\in I}|f(x)|e^{-\alpha x},
\]
and that the norm $\|\cdot\|_\alpha$ is Lipschitz equivalent to the uniform norm
\[
\|f\|=\sup_{x\in I}|f(x)|.
\]
Now suppose that $\phi:\mathbb{R}^2\to\mathbb{R}$ is continuous and Lipschitz in the second variable.
Consider the map $T$ from $C(I)$ to itself sending $f$ to
\[
(Tf)(x)=y_0+\int_0^x \phi(t,f(t))\,dt.
\]
Give an example to show that $T$ need not be a contraction under the uniform norm.
Show, however, that $T$ is a contraction under the norm $\|\cdot\|_\alpha$ for some $\alpha$, and hence deduce that the differential equation
\[
f'(x)=\phi(x,f(x))
\]
has a unique solution on $I$ satisfying $f(0)=y_0$.

\bigskip
\hrule
\bigskip

\textbf{1. Weighted supremum norm.}
For $\alpha\in\mathbb{R}$ define
\[
\|f\|_\alpha=\sup_{x\in[0,R]}|f(x)|e^{-\alpha x}.
\]
This is a norm on $C(I)$. It is \emph{Lipschitz equivalent} to the usual supremum norm
\(\|f\|_\infty=\sup_{x\in[0,R]}|f(x)|\)
because on $[0,R]$, the weight $e^{-\alpha x}$ satisfies
\[
e^{-|\alpha|R}\le e^{-\alpha x}\le e^{|\alpha|R}.
\]
Hence for all $f\in C(I)$,
\[
e^{-|\alpha|R}\|f\|_\infty \le \|f\|_\alpha \le e^{|\alpha|R}\|f\|_\infty,
\]
showing equivalence of norms.

\bigskip

\textbf{2. The Picard operator.}
Assume $\phi:\mathbb{R}^2\to\mathbb{R}$ is continuous and Lipschitz in its second variable:
there exists $L>0$ such that
\[
|\phi(t,y)-\phi(t,z)|\le L|y-z| \quad \forall\, t,y,z.
\]
Then the operator
\[
(Tf)(x)=y_0+\int_0^x \phi(t,f(t))\,dt
\]
maps $C(I)$ to itself, and a fixed point $f=Tf$ is precisely a solution of the integral form
\[
f(x)=y_0+\int_0^x \phi(t,f(t))\,dt,
\]
equivalent to the differential equation $f'(x)=\phi(x,f(x))$ with $f(0)=y_0$.

\bigskip

\textbf{3. Contraction property.}
For $f,g\in C(I)$,
\[
|(Tf-Tg)(x)|\le \int_0^x |\phi(t,f(t))-\phi(t,g(t))|\,dt
\le L\int_0^x |f(t)-g(t)|\,dt.
\]
Thus
\[
\|Tf-Tg\|_\infty\le LR\,\|f-g\|_\infty.
\]
If $LR\ge1$, $T$ is not a contraction in the uniform norm.

\bigskip

\textbf{4. Weighted norm case.}
For the weighted norm $\|\cdot\|_\alpha$,
\[
e^{-\alpha x}|(Tf-Tg)(x)|
\le L\int_0^x e^{-\alpha(x-t)}|f(t)-g(t)|e^{-\alpha t}\,dt
\le L\|f-g\|_\alpha \int_0^x e^{-\alpha s}\,ds
\le \frac{L}{\alpha}\|f-g\|_\alpha.
\]
Hence $\|Tf-Tg\|_\alpha\le \frac{L}{\alpha}\|f-g\|_\alpha$.
Choosing $\alpha>L$ ensures that $T$ is a contraction in $\|\cdot\|_\alpha$.

\bigskip

\textbf{5. Existence and uniqueness.}
By the Banach Fixed Point Theorem, $T$ admits a unique fixed point $f\in C(I)$.
Thus the differential equation $f'(x)=\phi(x,f(x))$, $f(0)=y_0$, has a unique continuous solution on $I$.


Let $I=[0,R]$ and $C(I)$ be the space of continuous functions on $I$. For $\alpha\in\mathbb R$ set
\[
\|f\|_\alpha=\sup_{x\in I}|f(x)|e^{-\alpha x},\qquad \|f\|_\infty=\sup_{x\in I}|f(x)|.
\]

Since $e^{-\alpha x}\in [e^{-|\alpha|R},e^{|\alpha|R}]$ on $I$, for all $f\in C(I)$,
\[
e^{-|\alpha|R}\,\|f\|_\infty \ \le\ \|f\|_\alpha \ \le\ e^{|\alpha|R}\,\|f\|_\infty.
\]
Hence $\|\cdot\|_\alpha$ is a norm Lipschitz–equivalent to the uniform norm.

Assume $\phi:\mathbb R^2\to\mathbb R$ is continuous and Lipschitz in its second variable:
$|\phi(t,y)-\phi(t,z)|\le L|y-z|$ for all $t,y,z$.
Define $T:C(I)\to C(I)$ by
\[
(Tf)(x)=y_0+\int_0^x \phi(t,f(t))\,dt .
\]

\emph{Not a contraction in $\|\cdot\|_\infty$ in general.}
For $f,g\in C(I)$,
\[
\|Tf-Tg\|_\infty\le L\!\int_0^R |f(t)-g(t)|\,dt \le LR\,\|f-g\|_\infty .
\]
If $LR\ge1$, the Lipschitz factor is not $<1$. Example: $I=[0,2]$, $\phi(t,y)=y$ ($L=1$) gives
$\|Tf-Tg\|_\infty\le 2\,\|f-g\|_\infty$.

\emph{$T$ is a contraction in $\|\cdot\|_\alpha$ for suitable $\alpha>0$.}
For $x\in[0,R]$,
\[
\begin{aligned}
	e^{-\alpha x}\,|(Tf-Tg)(x)|
	&\le L\int_0^x e^{-\alpha(x-t)}\big(|f(t)-g(t)|e^{-\alpha t}\big)\,dt \\
	&\le L\|f-g\|_\alpha \int_0^x e^{-\alpha s}\,ds
	\ \le\ \frac{L}{\alpha}\,\|f-g\|_\alpha .
\end{aligned}
\]
Therefore $\|Tf-Tg\|_\alpha \le \frac{L}{\alpha}\|f-g\|_\alpha$. Choosing $\alpha>L$ makes $T$ a contraction.
By BanachĂ˘â‚¬â„˘s Fixed Point Theorem, $T$ has a unique fixed point $f\in C(I)$, i.e.
\[
f(x)=y_0+\int_0^x \phi(t,f(t))\,dt ,
\]
which is the unique solution on $I$ of the IVP $f'(x)=\phi(x,f(x))$, $f(0)=y_0$.
```

## CP-II-0377

- chapter line: 22117

```tex
\label{prob:cp-ii-0377}
quadrature for $f(x)=\sinh x$ on $[0,1]$

\[
I=\int_{0}^{1}\sinh x\,dx=\cosh(1)-1.
\]

\[
\begin{aligned}
	&\text{Midpoint:} &&Q_{\mathrm{mid}}=(b-a)\,f\!\left(\tfrac{a+b}{2}\right)=1\cdot \sinh\!\left(\tfrac12\right),\\[4pt]
	&\text{Trapezoidal:} &&Q_{\mathrm{trap}}=\tfrac{1}{2}\big(f(0)+f(1)\big)=\tfrac12\sinh(1),\\[4pt]
	&\text{Simpson:} &&Q_{\mathrm{simp}}=\tfrac{1}{6}\Big(f(0)+4f\!\left(\tfrac12\right)+f(1)\Big).
\end{aligned}
\]
Numerically,
\[
\begin{aligned}
	Q_{\mathrm{mid}}&\approx 0.5210953, \\
	Q_{\mathrm{trap}}&\approx 0.5876010, \\
	Q_{\mathrm{simp}}&\approx 0.5430699, \qquad
	I=\cosh(1)-1\approx 0.5430806.
\end{aligned}
\]
Absolute errors:
\(
|Q_{\mathrm{mid}}-I|\approx 1.36\cdot 10^{-3},\
|Q_{\mathrm{trap}}-I|\approx 5.46\cdot 10^{-3},\
|Q_{\mathrm{simp}}-I|\approx 1.09\cdot 10^{-5}.
\)

For $N=16,32$ panels on $[0,1]$:
\[
\begin{aligned}
	&N=16:\quad |Q_{\mathrm{simp},\,N}-I|\approx 4.60\times 10^{-8},\\
	&N=32:\quad |Q_{\mathrm{simp},\,N}-I|\approx 2.88\times 10^{-9}.
\end{aligned}
\]

Mapping the $n$-point Gauss--Legendre rule from $[-1,1]$ to $[0,1]$ gives
\[
Q_n=\sum_{k=1}^{n} w_k\,\sinh(x_k),\quad
x_k=\tfrac{1}{2}(1+\xi_k),\ \ w_k=\tfrac{1}{2}\omega_k,
\]
where $(\xi_k,\omega_k)$ are the standard nodes/weights on $[-1,1]$.
Numerically,
\[
\begin{aligned}
	&n=4:\ |Q_4-I|\approx 3.0\times 10^{-10},\\
	&n=5,6:\ \text{error at machine precision}.
\end{aligned}
\]

For analytic $f$ like $\sinh x$, Gauss--Legendre achieves very high accuracy with few nodes
(degree of exactness $2n-1$), while composite Simpson converges at fourth order as the mesh refines.
```

## CP-II-0462

- chapter line: 22184

```tex
\label{prob:cp-ii-0462}
Let $\gamma:[0,2\pi]\to\mathbb{R}^2$ be given by
\[
\gamma(\theta)=\begin{pmatrix}\theta-\sin\theta\\ 1-\cos\theta\end{pmatrix}.
\]

A \emph{parametrised curve} in $\mathbb{R}^2$ is a map $\gamma:[a,b]\to\mathbb{R}^2$.
We say $\gamma$ is of class $C^1$ if its coordinate functions are continuously differentiable.

For a $C^1$ curve $\gamma:[a,b]\to\mathbb{R}^2$, the \emph{arc length} is
\[
L(\gamma)=\int_a^b \|\gamma'(t)\|\,dt,
\]
where $\|\cdot\|$ is the Euclidean norm in $\mathbb{R}^2$.

The \emph{cycloid} is the path traced by a fixed point on the circumference of a circle of radius $1$ rolling along the $x$-axis without slipping.
Its standard parametrisation is
\[
\gamma(\theta) = (\theta-\sin\theta,\;1-\cos\theta), \quad 0\leq \theta\leq 2\pi.
\]

	\par\noindent\textbullet\quad \emph{Sketch.}

	At $\theta=0$, $\gamma(0)=(0,0)$.
	At $\theta=\pi$, $\gamma(\pi)=(\pi,2)$.
	At $\theta=2\pi$, $\gamma(2\pi)=(2\pi,0)$.

	Hence $\gamma$ describes a single arch of the cycloid: it starts at the origin, rises to height $2$ above $x=\pi$, and returns to the $x$-axis at $(2\pi,0)$.
	It is symmetric about the vertical line $x=\pi$.

	\par\noindent\textbullet\quad \emph{Arc length.}

	Differentiate:
	\[
	\gamma'(\theta)=(1-\cos\theta,\;\sin\theta).
	\]

	Compute norm:
	\[
	\|\gamma'(\theta)\|^2=(1-\cos\theta)^2+\sin^2\theta
	=2-2\cos\theta
	=4\sin^2\!\Bigl(\tfrac{\theta}{2}\Bigr).
	\]

	Thus
	\[
	\|\gamma'(\theta)\|=2\sin\!\Bigl(\tfrac{\theta}{2}\Bigr), \quad 0\le\theta\le 2\pi.
	\]

	Hence
	\[
	L(\gamma)=\int_0^{2\pi}2\sin\!\Bigl(\tfrac{\theta}{2}\Bigr)\,d\theta.
	\]

	Substitute $u=\tfrac{\theta}{2}$, so $d\theta=2du$, limits $0\mapsto 0$, $2\pi\mapsto \pi$:
	\[
	L(\gamma)=4\int_0^\pi \sin u\,du
	=4[-\cos u]_0^\pi
	=4(1-(-1))=8.
	\]

\[
\boxed{L(\gamma)=8}
\]
```

## CP-II-0469

- chapter line: 22301

```tex
\label{prob:cp-ii-0469}
Let $(X,d)$ be a non-empty complete metric space. Suppose $f:X\to X$ is a contraction and
$g:X\to X$ is a function which commutes with $f$, i.e.\ $f(g(x))=g(f(x))$ for all $x\in X$.
Show that $g$ has a fixed point. Must this fixed point be unique?

\bigskip

	\par\noindent\textbullet\quad \textbf{Banach Fixed Point Theorem (Contraction Mapping).}
	If $(X,d)$ is complete and $f:X\to X$ is a contraction, i.e.
	$\exists\,0<L<1$ such that $d(fx,fy)\le L\,d(x,y)$ for all $x,y\in X$, then

		\par\noindent\textbullet\quad $f$ has a \emph{unique} fixed point $p\in X$;
		\par\noindent\textbullet\quad for any $x_0\in X$, the Picard iteration $x_{n+1}=f(x_n)$ converges to $p$ with the a priori bound
		$d(x_n,p)\le \dfrac{L^n}{1-L}\,d(x_1,x_0)$.

	\par\noindent\textbullet\quad \textbf{Commutation and fixed points.}
	If $f\circ g=g\circ f$ and $p$ is a fixed point of $f$ (i.e.\ $f(p)=p$), then
	\[
	f\big(g(p)\big)=g\big(f(p)\big)=g(p),
	\]
	so $g(p)$ is also a fixed point of $f$. Hence $g$ maps the fixed-point set $\mathrm{Fix}(f)$
	into itself.

	\par\noindent\textbullet\quad \textbf{Consequence when $f$ is a contraction.}
	Since $\mathrm{Fix}(f)=\{p\}$ is a singleton by BanachĂ˘â‚¬â„˘s theorem, the previous item forces
	$g(p)=p$. Thus $p$ is a fixed point of $g$.

	\par\noindent\textbullet\quad \textbf{Uniqueness warning.}
	The fixed point of $g$ need not be unique. Example: on $X=\mathbb{R}$, let
	$f(x)=x/2$ (a contraction) and $g(x)=x$ (identity). Then $f\circ g=g\circ f$,
	$g$ has \emph{every} point as a fixed point.

Let $(X,d)$ be complete and let the contraction be the Ă˘â‚¬Ĺ›halvingĂ˘â‚¬ĹĄ map $f=\tfrac12\,\mathrm{Id}$ (so $f(x)=\tfrac12 x$ on linear spaces, or $f(h)=\tfrac12 h$ pointwise on function spaces). In each case below $f\circ g=g\circ f$, and we list the fixed points of $g$.

\par\medskip\noindent\textbf{A. $g$ has \emph{many} fixed points (non-unique).}\quad
\[
X=\mathbb{R},\quad f(x)=\tfrac12 x,\quad g(x)=x.
\]
Then $f\circ g=g\circ f=\tfrac12 x$, and $\mathrm{Fix}(g)=\mathbb{R}$ (every point is fixed).

\par\medskip\noindent\textbf{B. $g$ has a \emph{unique} fixed point but is not a contraction.}\quad
\[
X=\mathbb{R}^2,\quad f(x)=\tfrac12 x,\quad
g(x)=Ax,\ \ A=\begin{pmatrix}2&0\\[2pt]0&\tfrac12\end{pmatrix}.
\]
Clearly $f$ commutes with any linear $A$, so $f\circ g=g\circ f$.
Fixed points solve $Ax=x$, i.e.\ $(2-1)x_1=0$, $(\tfrac12-1)x_2=0$, hence $\mathrm{Fix}(g)=\{(0,0)\}$.
Moreover $\|A\|=2>1$, so $g$ is not a contraction.

\par\medskip\noindent\textbf{C. $g$ has a \emph{finite} fixed-point set.}\quad
\[
X=\mathbb{R},\quad f(x)=\tfrac12 x,\quad g(x)=-x.
\]
Then $f(g(x))=\tfrac12(-x)=-(\tfrac12 x)=g(f(x))$.
Fixed points satisfy $-x=x\Rightarrow x=0$, so $\mathrm{Fix}(g)=\{0\}$.

\par\medskip\noindent\textbf{D. $g$ has \emph{uncountably many} fixed points.}\quad
\[
X=\mathbb{R}^2,\quad f(x)=\tfrac12 x,\quad g=\Pi_L \text{ (orthogonal projection onto a line $L$).}
\]
Since $\tfrac12\Pi_L=\Pi_L\tfrac12$, we have $f\circ g=g\circ f$.
Fixed points of $g$ are precisely the points on $L$, so $\mathrm{Fix}(g)=L$ (uncountable).

\[
X=C([0,1]),\quad \|h\|_\infty\ \text{metric},\quad f(h)=\tfrac12 h,\quad g(h)=h^3\ \text{(pointwise cube)}.
\]
Then $f(g(h))=\tfrac12 h^3=g(f(h))=(\tfrac12 h)^3\cdot 4=\tfrac12 h^3$.
Fixed points satisfy $h^3=h$ pointwise. By continuity, $h$ must be a constant in $\{-1,0,1\}$, so
\[
\mathrm{Fix}(g)=\{-\mathbf{1},\ \mathbf{0},\ \mathbf{1}\}.
\]

\[
X=\mathbb{R},\quad f(x)=\tfrac12 x\ \text{(contraction)},\quad g(x)=x+1.
\]
Here $g$ has no fixed point, and $f\circ g(x)=\tfrac12(x+1)\neq \tfrac12 x+1=g\circ f(x)$, so the
commutation hypothesis fails.
```

## CP-II-0005

- chapter line: 22438

```tex
\label{prob:cp-ii-0005}
— A Dense Set with Super–Polynomial Approximations

Show there is a dense set of reals $x$ such that for each $n\in\mathbb N$ there exist integers $p,q$ with $q\ge2$ and
$
0<\big|x-\frac{p}{q}\big|<\frac{1}{q^{\,n}}.
$

Fix an interval $(\alpha,\beta)$. Choose $r=\frac{u}{10^M}\in(\alpha,\beta)$ and $N$ large with
$\sum_{k\ge N}10^{-k!}<\beta-\alpha$. Define
\[
x=r+\sum_{k=N}^{\infty}10^{-k!}\in(\alpha,\beta).
\]
For any $m\in\mathbb N$, taking $q=10^{K!}$ with $K\ge\max\{N,m\}$ and $p$ the truncation numerator,
\[
0<\Big|x-\frac{p}{q}\Big|<10^{-(K+1)!}<\frac{1}{q^{\,m}}.
\]
Thus every interval contains such $x$; the set is dense.

\begin{definition}[Liouville number]
	A real number $x$ is a \emph{Liouville number} if for every $n\in\mathbb N$ there exist
	infinitely many rationals $p/q$ ($q\ge2$) such that
	\[
	0<\Big|x-\frac{p}{q}\Big|<\frac{1}{q^{\,n}}.
	\]
\end{definition}

\begin{proposition}[Problem 12 $\Rightarrow$ Liouville]
	Let
	\[
	x \;=\; r+\sum_{k=N}^{\infty}10^{-k!}, \qquad r=\frac{u}{10^M}\in\mathbb Q,
	\]
	as constructed in Problem~12. Then $x$ is a Liouville number (hence transcendental).
\end{proposition}

\begin{proof}
	Fix $n\in\mathbb N$ and let $K\ge\max\{N,n\}$. Define the truncation
	\[
	\frac{p_K}{q_K} \;=\; r+\sum_{k=N}^{K}\,10^{-k!}, \qquad q_K=10^{K!}\in\mathbb N.
	\]
	Then
	\[
	0<\Big|x-\frac{p_K}{q_K}\Big|
	=\sum_{j=K+1}^{\infty}10^{-j!}
	<10^{-(K+1)!}
	<\frac{1}{(10^{K!})^{\,n}}
	=\frac{1}{q_K^{\,n}}.
	\]
	Since this holds for every $K\ge\max\{N,n\}$, we obtain \emph{infinitely many} such rationals
	for each fixed $n$. Hence $x$ is a Liouville number.
\end{proof}

\begin{corollary}
	The set $\mathcal L$ of Liouville numbers is dense in $\mathbb R$; in particular,
	the set produced in Problem~12 is a dense subset of $\mathcal L$.
\end{corollary}

\begin{remark}[Topological/measure size of $\mathcal L$]
	One has
	\[
	\mathcal L
	= \bigcap_{n=1}^{\infty}\ \bigcup_{q\ge2}\ \bigcup_{p\in\mathbb Z}
	\Big(\tfrac{p}{q}-q^{-n},\,\tfrac{p}{q}+q^{-n}\Big),
	\]
	so $\mathcal L$ is a dense $G_\delta$ (comeager) subset of $\mathbb R$, but it has Lebesgue measure $0$.
	Moreover, by Liouville's theorem (and Roth's refinement), no irrational algebraic number lies in $\mathcal L$.
\end{remark}
```

## CP-II-0014

- chapter line: 22508

```tex
\label{prob:cp-ii-0014}
— Alternating Continued Fraction with $a,b>0$

Let
\[
x=\cfrac{1}{\displaystyle a+\cfrac{1}{\displaystyle b+\cfrac{1}{\displaystyle a+\cfrac{1}{\displaystyle b+\cdots}}}},
\qquad a,b\in\mathbb N.
\]

	\par\noindent\textbullet\quad Show that $x$ solves $a x^2 + a b x - b=0$.
	\par\noindent\textbullet\quad For $a=b=1$, prove $x=\frac{-1+\sqrt5}{2}$ and that the convergents $p_n/q_n$ satisfy
	$p_n=F_n$, $q_n=F_{n+1}$ where $(F_n)$ are Fibonacci numbers, $F_0=0$, $F_1=1$.
	\par\noindent\textbullet\quad Show CassiniĂ˘â‚¬â„˘s identity $F_{n+1}F_{n-1}-F_n^2=(-1)^{n+1}$.
	\par\noindent\textbullet\quad Prove $F_{2n+1}=F_n^2+F_{n+1}^2$ and $F_{2n}=F_n(F_{n-1}+F_{n+1})$.
	With $x_n=F_{n+1}/F_n$ express $x_{2n}$ as a function of $x_n$ and deduce that
	$y_k=x_{2^k}$ converges very rapidly to $\phi=(1+\sqrt5)/2$.

(a) Since the pattern repeats after the inner $b$, we have $x=\dfrac{1}{a+\dfrac{1}{b+x}}$.
Thus
\[
\frac{1}{x}=a+\frac{1}{b+x}\;\Longrightarrow\;
(b+x)\Big(\frac{1}{x}-a\Big)=1
\;\Longrightarrow\; a x^2 + a b x - b=0.
\]

(b) With $a=b=1$, the quadratic gives $x^2+x-1=0$ and $x=\tfrac{-1+\sqrt5}{2}$.
The SCF is $[0;1,1,1,\ldots]$. Convergent recurrences
$p_{-1}=1,p_0=0,\ p_n=p_{n-1}+p_{n-2}$ and
$q_{-1}=0,q_0=1,\ q_n=q_{n-1}+q_{n-2}$ yield $p_n=F_n$, $q_n=F_{n+1}$.

(c) Cassini: $F_{n+1}F_{n-1}-F_n^2=(-1)^{n+1}$, proved by induction or BinetĂ˘â‚¬â„˘s formula.

(d) Identities (by induction or Binet):
\[
F_{2n+1}=F_n^2+F_{n+1}^2,\qquad F_{2n}=F_n(F_{n-1}+F_{n+1}).
\]
Therefore, with $x_n=F_{n+1}/F_n$,
\[
x_{2n}=\frac{F_{2n+1}}{F_{2n}}
=\frac{F_n^2+F_{n+1}^2}{F_n(F_{n-1}+F_{n+1})}
=\frac{1+x_n^2}{2x_n-1}=:T(x_n).
\]
Since $\phi^2=\phi+1$, we have $T(\phi)=\phi$, and
\[
T'(x)=\frac{2(x^2-x-1)}{(2x-1)^2},\qquad T'(\phi)=0,
\]
so the iteration $y_{k+1}=T(y_k)$ has quadratic convergence to $\phi$.
```

## CP-II-0038

- chapter line: 22558

```tex
\label{prob:cp-ii-0038}
\par\noindent\textbullet\quad \textbf{Exponential rate.}
	For $\delta_n=r^n$ with $0<r<1$, $\gamma_j=r^{j-1}(1-r)$, giving
	\[
	f(x)=\sum_{j\ge1}(1-r)r^{j-1}T_{3j}(x),
	\quad E_n(f)\ge r^n.
	\]

By suitable choice of $\gamma_j$, one can make the polynomial approximation
of $f$ converge to $f$ at any desired (arbitrarily slow) rate.
```

## CP-II-0163

- chapter line: 22706

```tex
\label{prob:cp-ii-0163}
{Uniform polynomial approximation on an annulus forces extension} -{annulus-extension}
	Let $A=\{z\in\mathbb C: \tfrac12\le |z|\le 1\}$ and let $f:A\to\mathbb C$ be continuous on $A$ and
	holomorphic on $\operatorname{int}A$. Suppose polynomials $p_n$ converge uniformly to $f$ on $A$.
	Show there exists $g:\{|z|\le1\}\to\mathbb C$ continuous, holomorphic on $\{|z|<1\}$, with $g=f$ on $A$.
```

## CP-II-0217

- chapter line: 22780

```tex
\label{prob:cp-ii-0217}
For each \(f\in C([-1,1])\), let \(\mathcal P_n\) denote the subspace of polynomials of degree
at most \(n\), and define the best uniform approximation error
\[
E_n(f):=\inf_{p\in \mathcal P_n}\ \sup_{x\in[-1,1]} |f(x)-p(x)|.
\]
By the Weierstrass approximation theorem, \(E_n(f)\to 0\) for every \(f\in C([-1,1])\).
Using the result of Question~3, construct a function \(f\in C([-1,1])\) to show that the
convergence \(E_n(f)\to 0\) can be \emph{arbitrarily slow} in the following sense:

\medskip
\noindent
\textbf{Claim to prove.} For any decreasing sequence \((\delta_n)_{n\ge1}\) of nonnegative numbers with
\(\delta_n\to 0\), there exists \(f\in C([-1,1])\) such that
\[
E_n(f)\ \ge\ \delta_n \qquad\text{for all } n=1,2,\dots.
\]

For \(f\in C([-1,1])\) let
\[
E_n(f):=\inf_{p\in\mathcal P_n}\ \|f-p\|_\infty,\qquad
\mathcal P_n=\{p:\deg p\le n\}.
\]
By Weierstrass, \(E_n(f)\downarrow 0\). We show the convergence can be arbitrarily slow.

If \(\gamma_j\ge0\) with \(\sum_{j=1}^\infty\gamma_j<\infty\) and
\[
f(x)=\sum_{j=1}^\infty \gamma_j\,T_{3j}(x),\qquad
P_n(x)=\sum_{j=1}^{n}\gamma_j\,T_{3j}(x),
\]
then \(f\in C([-1,1])\), \(P_n\) is the best uniform approximant of degree \(\le 3n\), and
\[
E_{3n}(f)=\|f-P_n\|_\infty=\sum_{j=n+1}^\infty \gamma_j.
\]

Given any decreasing sequence \(\delta_n\ge0\) with \(\delta_n\to 0\), there exists
\(f\in C([-1,1])\) such that \(E_n(f)\ge \delta_n\) for all \(n\ge1\).
```

## CP-II-0331

- chapter line: 22820

```tex
\label{prob:cp-ii-0331}
\hfill

		\par\noindent\textbullet\quad \textbf{Quadratic irrationals.} If $x$ is quadratic, then $a_n$ are periodic/bounded,
		so $\mu(x)=2$. E.g.\ $\phi=\frac{1+\sqrt5}{2}=[1;1,1,1,\dots]$ has $\mu(\phi)=2$.
		\par\noindent\textbullet\quad \textbf{$e$.} The continued fraction $[2;1,2,1,1,4,1,1,6,\dots]$ has
		$\log a_{n+1}/\log q_n\to0$, hence $\mu(e)=2$.
		\par\noindent\textbullet\quad \textbf{Liouville constant (base 10).}
		\[
		L=\sum_{n=1}^\infty 10^{-n!}=0.110001000000000000000001\ldots
		\]
		Truncations at $N!$ give rationals $p_N/10^{N!}$ with
		$\bigl|L-\frac{p_N}{10^{N!}}\bigr|<10^{-(N+1)!}\le (10^{N!})^{-m}$ for every $m\le N+1$.
		Thus $\mu(L)=\infty$; $L$ is transcendental.
		\par\noindent\textbullet\quad \textbf{Factorial-base family (from the previous exercise).}
		For any digits $b_n\in\{1,2\}$,
		\[
		x_{\mathbf b}=\sum_{n=0}^\infty \frac{b_n}{10^{\,n!}}
		\]
		is Liouville, hence transcendental; moreover the map $\{1,2\}^{\mathbb N}\to\mathbb R$,
		$\mathbf b\mapsto x_{\mathbf b}$ is injective (no carries at factorial places), so there are
		$2^{\aleph_0}$ distinct such numbers, all with $\mu=\infty$.
		\par\noindent\textbullet\quad \textbf{$\pi$.} It is known that $2\le \mu(\pi)\le 7.6063\ldots$ (Salikhov, 2008);
		the exact value is conjecturally $2$ and remains unknown.
```

## CP-II-0340

- chapter line: 22847

```tex
\label{prob:cp-ii-0340}
— Interpolation remainder and uniform convergence

Let $f:[-1,1]\to\mathbb{R}$ be $(n+1)$-times continuously differentiable and
$J_n=\{x_0,\dots,x_n\}\subset[-1,1]$ distinct.
Let $P_{J_n}\in\Pi_n$ be the unique polynomial with $P_{J_n}(x_j)=f(x_j)$.
Define
\[
\beta_{J_n}(x)=(x-x_0)\cdots(x-x_n).
\]

\bigskip

\noindent\textbf{Remainder formula.}
For every $x\in[-1,1]$ there exists $\zeta\in(-1,1)$ such that
\[
f(x)-P_{J_n}(x)=\frac{f^{(n+1)}(\zeta)}{(n+1)!}\,\beta_{J_n}(x).
\]

\emph{Proof.}
If $x=x_j$ this is trivial. Otherwise choose $\lambda$ so that
$g(y)=f(y)-P_{J_n}(y)-\lambda\,\beta_{J_n}(y)$ satisfies $g(x)=0$.
Since $g(x_j)=0$ for $j=0,\dots,n$, $g$ has $n+2$ distinct zeros.
By repeated Rolle, there exists $\zeta$ with
$g^{(n+1)}(\zeta)=0$. Because $\deg P_{J_n}\le n$,
$g^{(n+1)}(y)=f^{(n+1)}(y)-\lambda (n+1)!$, hence
$\lambda=f^{(n+1)}(\zeta)/(n+1)!$. Evaluating at $x$ yields the formula.

\bigskip

\noindent\textbf{Uniform convergence under factorial control.}
Assume $f\in C^\infty[-1,1]$ and $\sup_{x}|f^{(n)}(x)|\le M^n$ for all $n\ge1$.
From the remainder formula and the bound
\[
|\beta_{J_n}(x)|=\prod_{j=0}^{n}|x-x_j|\le 2^{\,n+1}\qquad(x,x_j\in[-1,1]),
\]
we obtain, uniformly in $x$ and in the choice of nodes $J_n$,
\[
\|f-P_{J_n}\|_{\infty}
\le \frac{\sup_{y}|f^{(n+1)}(y)|}{(n+1)!}\,\sup_{x}|\beta_{J_n}(x)|
\le \frac{M^{n+1}\,2^{\,n+1}}{(n+1)!}\xrightarrow[n\to\infty]{}0.
\]
Hence $P_{J_n}\to f$ uniformly on $[-1,1]$.

\bigskip

The crude bound $\sup|\beta_{J_n}|\le 2^{n+1}$ is node-independent.
Sharper bounds are possible for specific choices, e.g.\ Chebyshev nodes minimize $\|\beta_{J_n}\|_\infty$
among monic polynomials, yielding $\|\beta_{J_n}\|_\infty=2^{-n}$.
Without derivative growth control, poor nodes can cause divergence (Runge phenomenon).

\noindent\textbf{Approximation (by polynomials).}
Let $X\subset\mathbb{R}$ and $f:X\to\mathbb{R}$. A sequence of polynomials $(p_n)$
\emph{approximates} $f$ on $X$ if $p_n\to f$ in a prescribed mode:
 \setlength{\itemsep}{0.4em}
	\par\noindent\textbullet\quad \emph{Uniform approximation:} $\|f-p_n\|_\infty:=\sup_{x\in X}|f(x)-p_n(x)|\to 0$.
	\par\noindent\textbullet\quad \emph{Pointwise approximation:} for every $x\in X$, $p_n(x)\to f(x)$.
	\par\noindent\textbullet\quad \emph{$L^p$ approximation ($1\le p<\infty$):} $\|f-p_n\|_{L^p(X)}\to 0$.

For $m\in\mathbb{N}$, a \emph{best degree-$m$ approximation} is a polynomial
$p_m^*\in\Pi_m$ such that
\[
\|f-p_m^*\|=\inf_{q\in\Pi_m}\|f-q\|,
\]
where $\|\cdot\|$ is the chosen norm (e.g., $\|\cdot\|_\infty$ or $\|\cdot\|_{L^p}$).

\bigskip

\noindent\textbf{Interpolation (by polynomials).}
Given distinct nodes $x_0,\dots,x_n\in X$ and data $y_j=f(x_j)$,
a polynomial $P\in\Pi_n$ \emph{interpolates} $f$ at the nodes if
\[
P(x_j)=f(x_j)\qquad (j=0,\dots,n).
\]
For distinct nodes, such $P$ exists and is unique; it can be written in
\emph{Lagrange form}
\[
P(x)=\sum_{j=0}^n f(x_j)\,\ell_j(x),\qquad
\ell_j(x)=\prod_{\substack{k=0\\ k\ne j}}^n \frac{x-x_k}{x_j-x_k},
\]
or in \emph{Newton form} using divided differences.

\bigskip

\noindent\textbf{Approximation vs.\ interpolation.}
Interpolation enforces exact matching at finitely many points; approximation aims to minimize a global error without necessarily matching at any specific point. An interpolant may approximate well (e.g.\ at Chebyshev nodes), but can also behave poorly (Runge phenomenon with equispaced nodes).
```

## CP-II-0353

- chapter line: 23008

```tex
\label{prob:cp-ii-0353}
(quadrature)

Given a function $f$ on $[a,b]$, approximate the integral
\[
I(f):=\int_a^b f(x)\,dx
\]
by a \emph{quadrature rule}
\[
Q_n(f):=\sum_{k=1}^{n} A_k\, f(x_k),
\]
where the \emph{nodes} $x_k\in[a,b]$ and \emph{weights} $A_k\in\mathbb{R}$ are chosen in advance.

\bigskip

The \emph{degree of exactness} (or precision) of $Q_n$ is the largest integer $m\ge 0$ such that
\[
Q_n(p)=I(p)\qquad\text{for all polynomials $p$ with }\deg p\le m.
\]
Examples:
 \setlength{\itemsep}{0.6em}
	\par\noindent\textbullet\quad \textbf{Midpoint rule} ($n=1$): $Q_1(f)=(b-a)\,f\!\big(\tfrac{a+b}{2}\big)$, exact for $\deg\le1$.
	\par\noindent\textbullet\quad \textbf{Trapezoidal rule} ($n=2$): $Q_2(f)=\tfrac{b-a}{2}\big(f(a)+f(b)\big)$, exact for $\deg\le1$.
	\par\noindent\textbullet\quad \textbf{SimpsonĂ˘â‚¬â„˘s rule} ($n=3$): $Q_3(f)=\tfrac{b-a}{6}\big(f(a)+4f(\tfrac{a+b}{2})+f(b)\big)$, exact for $\deg\le3$.
	\par\noindent\textbullet\quad \textbf{Gauss–Legendre} (optimal): $n$ nodes $\{x_k\}$ are the zeros of $P_n$; with suitable $A_k>0$ the rule is exact for $\deg\le 2n-1$.

\bigskip

If $Q_n$ has degree $m$ and $f\in C^{m+1}[a,b]$, then
\[
I(f)-Q_n(f) \;=\; \frac{f^{(m+1)}(\xi)}{(m+1)!}\,\int_a^b \omega_{m+1}(x)\,dx,
\qquad
\omega_{m+1}(x):=\prod_{k=1}^n (x-x_k),
\]
for some $\xi\in(a,b)$ (exact form depends on the rule; for Newton--Cotes the exponent reflects paneling).

If $Q$ is linear and exact on $\Pi_{r-1}$ (all polynomials of degree $\le r-1$), then for $f\in C^r[a,b]$
\[
\begin{aligned}
K_r(t)
&:= \frac{1}{(r-1)!}
   \Bigg[
      \int_a^b (x-t)_{+}^{\,r-1}\,dx \\
&\hspace{4.5em}
      - \sum_{k=1}^{n}
        A_k (x_k-t)_{+}^{\,r-1}
   \Bigg].
\end{aligned}
\]
Hence
\[
|I(f)-Q(f)|\ \le\ \|f^{(r)}\|_\infty \int_a^b |K_r(t)|\,dt.
\]

\bigskip

 \setlength{\itemsep}{0.6em}
	\par\noindent\textbullet\quad \textbf{Polynomial density + control of weights.}
	Suppose for each polynomial $p$ we have $\varepsilon_n(p):=|I(p)-Q_n(p)|\to0$ as $n\to\infty$,
	the weights $A_k^{(n)}\ge0$, and
	\[
	\sum_{k=1}^n A_k^{(n)} \;=\; I(1)-\varepsilon_n(1)\ \longrightarrow\ b-a .
	\]
	Then for every $f\in C([a,b])$,
	\[
	|I(f)-Q_n(f)| \;\xrightarrow[n\to\infty]{}\; 0.
	\]
	\emph{Idea:} approximate $f$ uniformly by a polynomial $p$ (Weierstrass), split the error, and use positivity to bound $\sum A_k^{(n)}$.
	\par\noindent\textbullet\quad \textbf{Composite Newton--Cotes (refining mesh).}
	On a uniform partition with mesh $h\to0$, the composite midpoint/trapezoidal/Simpson rules converge for $f\in C([a,b])$ (with classical rates if $f$ is smoother).
	\par\noindent\textbullet\quad \textbf{Gaussian sequences.}
	Increasing $n$ in Gauss--Legendre quadrature gives rapidly convergent approximations for analytic $f$ (often near-exponential decay of the error).

\bigskip

If $x_1,\dots,x_n$ are the zeros of $P_n$ on $[-1,1]$, then there are \emph{unique} positive weights
\[
w_k=\frac{2}{\bigl(1-x_k^2\bigr)\,[P_n'(x_k)]^2}
\]
such that
\[
\int_{-1}^{1} p(x)\,dx=\sum_{k=1}^{n} w_k\,p(x_k)\qquad \text{for all } \deg p\le 2n-1.
\]
This degree $2n-1$ is \emph{optimal} for $n$ nodes.

\bigskip

 \setlength{\itemsep}{0.5em}
	\par\noindent\textbullet\quad \textbf{Midpoint / Trapezoidal / Simpson:}
	simple, composite versions easy; exactness $\le 1$ (mid/trap), $3$ (Simpson); global error $O(h^2)$ (trap), $O(h^4)$ (Simpson) for smooth $f$.
	\par\noindent\textbullet\quad \textbf{Newton--Cotes (high order):}
	many nodes, can yield negative weights and instability; not recommended for large $n$.
	\par\noindent\textbullet\quad \textbf{Gauss--Legendre:}
	best degree for a fixed $n$; positive weights; excellent for smooth/analytic $f$.
	\par\noindent\textbullet\quad \textbf{Clenshaw--Curtis:}
	Chebyshev cosine nodes; easy to implement, FFT-accelerated; performance close to Gauss for many $f$.
```

## CP-II-0363

- chapter line: 23180

```tex
\label{prob:cp-ii-0363}
\par\noindent\textbullet\quad \textbf{Equioscillation certificate.}
	The remainder $R_n$ alternates with constant magnitude $S_n$, providing a best-uniform
	(minimax-like) error profile for the truncation under nonnegative coefficients.
```

## CP-II-0476

- chapter line: 23410

```tex
\label{prob:cp-ii-0476}
— Limit of $L^p$ norms

\textbf{Claim.} If $f\in L^{r}(\mathbb{R}^n)\cap L^\infty(\mathbb{R}^n)$ for some $1\le r<\infty$, then
\[
\|f\|_{L^\infty}=\lim_{p\to\infty}\|f\|_{L^p}.
\]

\textbf{Proof.}
For $p\ge r$, Hölder/Lyapunov interpolation gives
\[
\|f\|_{L^p}\le \|f\|_{L^\infty}^{\,1-r/p}\,\|f\|_{L^r}^{\,r/p}
\ \xrightarrow[p\to\infty]{}\ \|f\|_{L^\infty},
\]
so $\limsup_{p\to\infty}\|f\|_{L^p}\le \|f\|_\infty$.
Let $M=\|f\|_\infty$ and fix $\varepsilon>0$; the set
$A_\varepsilon=\{x:\ |f(x)|>M-\varepsilon\}$ satisfies $0<|A_\varepsilon|<\infty$ since
$(M-\varepsilon)^r|A_\varepsilon|\le\int|f|^r<\infty$.
Then for $p\ge r$
\[
\|f\|_{L^p}\ge \biggl(\int_{A_\varepsilon}|f|^p\biggr)^{1/p}
\ge (M-\varepsilon)\,|A_\varepsilon|^{1/p}\ \xrightarrow[p\to\infty]{}\ M-\varepsilon.
\]
Hence $\liminf_{p\to\infty}\|f\|_{L^p}\ge M-\varepsilon$; letting $\varepsilon\downarrow0$ gives the result.


\bigskip\hrule\bigskip
```

## CP-II-0480

- chapter line: 23440

```tex
\label{prob:cp-ii-0480}
— Embeddings, interpolation, and local $L^p$

\tighthrule
\begin{spacy}
	\textbf{Statement.}
	Let $(E,\mathcal E,\mu)$ be a measure space.

		\par\noindent\textbullet\quad If $\mu(E)<\infty$ and $f\in L^{p}(E)$ with $1\le q\le p\le\infty$, then $f\in L^{q}(E)$ and
		\[
		\|f\|_{L^{q}} \;\le\; \mu(E)^{\frac{p-q}{pq}}\;\|f\|_{L^{p}}.
		\]
		\par\noindent\textbullet\quad Suppose $f\in L^{p_{0}}(E)\cap L^{p_{1}}(E)$ with $0<p_{0}<p_{1}\le\infty$.
		For $0\le \theta\le 1$ define $p_{\theta}$ by
		\[
		\frac{1}{p_{\theta}}=\frac{1-\theta}{p_{0}}+\frac{\theta}{p_{1}}.
		\]
		Then $f\in L^{p_{\theta}}(E)$ and
		\[
		\|f\|_{L^{p_{\theta}}} \;\le\; \|f\|_{L^{p_{0}}}^{\,1-\theta}\,\|f\|_{L^{p_{1}}}^{\,\theta}.
		\]
		\par\noindent\textbullet\quad On $\mathbb R^{n}$ show that if $p_{1}\neq p_{2}$ then
		$L^{p_{1}}(\mathbb R^{n})\not\subset L^{p_{2}}(\mathbb R^{n})$.
		Determine for which $p_{1},p_{2}$ we have
		$L^{p_{1}}_{\mathrm{loc}}(\mathbb R^{n}) \subset L^{p_{2}}_{\mathrm{loc}}(\mathbb R^{n})$.

	\tighthrule

	\textbf{Theory (quick toolkit).}

		\par\noindent\textbullet\quad On sets of finite measure: for $1\le q\le p\le\infty$,
		\[
		\|h\|_{L^{q}(E)} \le \mu(E)^{\frac{1}{q}-\frac{1}{p}}\,\|h\|_{L^{p}(E)}.
		\]
		This is Hölder with exponents $\frac{p}{q}$ and $\frac{p}{p-q}$.
		\par\noindent\textbullet\quad Real interpolation for $L^p$:
		If $1\le p_{0}<p_{1}\le\infty$ and $\frac1{p_{\theta}}=\frac{1-\theta}{p_{0}}+\frac{\theta}{p_{1}}$, then
		\[
		L^{p_{0}}\cap L^{p_{1}} \hookrightarrow L^{p_{\theta}},\qquad
		\|f\|_{p_{\theta}}\le \|f\|_{p_{0}}^{1-\theta}\|f\|_{p_{1}}^{\theta}.
		\]
		\par\noindent\textbullet\quad On bounded $K\subset\mathbb R^{n}$: if $p_{1}\ge p_{2}$,
		\[
		\|h\|_{L^{p_{2}}(K)} \le |K|^{\frac1{p_{2}}-\frac1{p_{1}}}\,\|h\|_{L^{p_{1}}(K)}.
		\]
		Hence $L^{p_{1}}_{\mathrm{loc}}\subset L^{p_{2}}_{\mathrm{loc}}$ iff $p_{1}\ge p_{2}$.

	\tighthrule

	\textbf{Proof.}

	\emph{(a) Finite-measure embedding.}
	For $p<\infty$, apply Hölder to $|f|^{q}\cdot 1$ with exponents $\tfrac{p}{q}$ and $\tfrac{p}{p-q}$:
	\[
	\int_E |f|^{q}
	\le \Bigl(\int_E |f|^{p}\Bigr)^{q/p}\,\mu(E)^{1-\frac{q}{p}}.
	\]
	Taking the $q$th root gives
	$\|f\|_{q}\le \mu(E)^{\frac{p-q}{pq}}\|f\|_{p}$.
	For $p=\infty$, $\|f\|_{q}^{q}\le \|f\|_{\infty}^{q}\mu(E)$.

	\medskip

	\emph{(b) Interpolation between $L^{p_{0}}$ and $L^{p_{1}}$.}
	For $p_{1}<\infty$,
	\[
	|f|^{p_{\theta}}
	= \bigl(|f|^{p_{0}}\bigr)^{(1-\theta)\frac{p_{\theta}}{p_{0}}}
	\bigl(|f|^{p_{1}}\bigr)^{\theta\frac{p_{\theta}}{p_{1}}}.
	\]
	With Hölder exponents
	$a=\frac{p_{0}}{(1-\theta)p_{\theta}}$ and $b=\frac{p_{1}}{\theta p_{\theta}}$ (conjugate by the definition of $p_\theta$),
	\[
	\int |f|^{p_{\theta}}
	\le \Bigl(\int |f|^{p_{0}}\Bigr)^{(1-\theta)\frac{p_{\theta}}{p_{0}}}
	\Bigl(\int |f|^{p_{1}}\Bigr)^{\theta\frac{p_{\theta}}{p_{1}}},
	\]
	hence
	$\|f\|_{p_{\theta}}\le \|f\|_{p_{0}}^{1-\theta}\|f\|_{p_{1}}^{\theta}$.
	If $p_{1}=\infty$, replace the second factor by $\|f\|_{\infty}^{\theta p_{\theta}}$.

	\medskip

	\emph{(c) Global non-inclusion and local inclusion.}
	If $p_{1}>p_{2}$, choose $\alpha$ with $\frac{n}{p_{1}}<\alpha\le \frac{n}{p_{2}}$ and set
	$f(x)=(1+|x|)^{-\alpha}$. Then $f\in L^{p_{1}}(\mathbb R^{n})$ but $f\notin L^{p_{2}}(\mathbb R^{n})$.
	If $p_{1}<p_{2}$, choose $\beta$ with $\frac{n}{p_{2}}<\beta\le \frac{n}{p_{1}}$ and let
	$g(x)=|x|^{-\beta}\mathbf 1_{\{|x|\le1\}}$; then $g\in L^{p_{2}}$ but $g\notin L^{p_{1}}$.
	Thus for $p_{1}\ne p_{2}$, neither $L^{p_{1}}(\mathbb R^{n})$ nor $L^{p_{2}}(\mathbb R^{n})$ contains the other.

	For local spaces: on every bounded $K$, the finite-measure embedding yields
	$\|h\|_{L^{p_{2}}(K)}\le |K|^{\frac1{p_{2}}-\frac1{p_{1}}}\|h\|_{L^{p_{1}}(K)}$ when $p_{1}\ge p_{2}$.
	Therefore
	\[
	L^{p_{1}}_{\mathrm{loc}}(\mathbb R^{n}) \subset L^{p_{2}}_{\mathrm{loc}}(\mathbb R^{n})
	\quad\Longleftrightarrow\quad p_{1}\ge p_{2}.
	\]
\end{spacy}

\tighthrule
\begin{spacy}
	\textbf{Monotone Convergence Theorem (Beppo--Levi).}
	Let $(f_n)_{n\ge1}$ be measurable with $0\le f_1\le f_2\le\cdots$ and $f_n\uparrow f$ a.e.
	Then
	\[
	\int_E f\,d\mu \;=\; \lim_{n\to\infty}\int_E f_n\,d\mu \;\in [0,\infty].
	\]
	(No integrability assumption beyond nonnegativity.)

	\medskip

	\textbf{Fatou's Lemma.}
	For nonnegative measurable $f_n$,
	\[
	\int_E \liminf_{n\to\infty} f_n \, d\mu
	\;\le\;
	\liminf_{n\to\infty} \int_E f_n \, d\mu .
	\]

	\medskip

	\textbf{Reverse Fatou (with domination).}
	If $f_n$ are measurable and there exists $g\in L^1(E)$ with $f_n\ge -g$ for all $n$, then
	\[
	\limsup_{n\to\infty} \int_E f_n \, d\mu
	\;\le\;
	\int_E \limsup_{n\to\infty} f_n \, d\mu .
	\]

	\medskip

	\textbf{Dominated Convergence Theorem (Lebesgue).}
	Suppose $f_n \to f$ a.e.\ on $E$ and there exists $g\in L^1(E)$ with $|f_n|\le g$ a.e.\ for all $n$.
	Then $f\in L^1(E)$ and
	\[
	\int_E f_n \, d\mu \;\to\; \int_E f \, d\mu,
	\qquad\text{equivalently}\qquad
	\|f_n-f\|_{L^1}\to 0.
	\]

	\medskip

	\textbf{Bounded Convergence (finite measure case).}
	If $\mu(E)<\infty$, $f_n\to f$ a.e., and $|f_n|\le M$ a.e.\ for some $M<\infty$, then
	\[
	\int_E f_n \, d\mu \;\to\; \int_E f \, d\mu .
	\]
	(Apply DCT with $g\equiv M\mathbf 1_E$.)

	\medskip

	\textbf{Useful corollary (convergence in $L^1$).}
	If $|f_n|\le g\in L^1$ and $f_n\to f$ in measure (or a.e.), then $f\in L^1$ and
	$\|f_n-f\|_{L^1}\to 0$ (by extracting a subsequence a.e.\ and applying DCT).
\end{spacy}

\tighthrule
\begin{spacy}
	\textbf{Markov's inequality (nonnegative case).}
	If $X\ge0$ is measurable and $a>0$, then
	\[
	\mu(\{X\ge a\}) \;\le\; \frac{1}{a}\int_E X\,d\mu.
	\]
	In particular, taking $X=|f|^{p}$ and $a=t^{p}$ gives
	\[
	\mu(\{|f|\ge t\}) \;\le\; \frac{\|f\|_{L^{p}}^{p}}{t^{p}}\qquad (p>0).
	\]

	\medskip

	\textbf{Chebyshev's inequality (general $p$).}
	For $f\in L^{p}(E)$ with $p>0$ and $t>0$,
	\[
	\mu(\{|f|\ge t\}) \;\le\; \frac{\|f\|_{L^{p}}^{p}}{t^{p}}.
	\]
	(Obtained from Markov with $X=|f|^{p}$.)

	\medskip

	\textbf{Egorov's theorem (a.e.\ $\Rightarrow$ almost uniform on finite measure).}
	If $\mu(E)<\infty$ and $f_n\to f$ almost everywhere on $E$, then for every $\varepsilon>0$ there exists
	a measurable $A\subset E$ with $\mu(E\setminus A)<\varepsilon$ such that $f_n\to f$ uniformly on $A$.

	\medskip

	\textbf{Uniform integrability (UI).}
	A family $\mathcal F\subset L^{1}(E)$ is \emph{uniformly integrable} if
	for every $\epsilon>0$ there exists $\delta>0$ such that
	$\mu(A)<\delta \Rightarrow \sup_{f\in\mathcal F}\int_{A}|f|\,d\mu<\epsilon$.
	A sufficient condition is domination: if there exists $g\in L^{1}(E)$ with $|f|\le g$ a.e.\ for all $f\in\mathcal F$,
	then $\mathcal F$ is uniformly integrable.

	\medskip

	\textbf{Vitali convergence theorem.}
	Let $(f_n)\subset L^{1}(E)$ be uniformly integrable and suppose $f_n\to f$ in measure.
	Then $f\in L^{1}(E)$ and
	\[
	\|f_n-f\|_{L^{1}} \;\longrightarrow\; 0 .
	\]
	(With domination $|f_n|\le g\in L^{1}$, Vitali follows from DCT combined with subsequence arguments.)

\end{spacy}

\tighthrule
\begin{spacy}
	\textbf{Setup.}
	Assume $\mu(E)<\infty$, $f_n\to f$ a.e., and $|f_n|\le g\in L^1(E)$.

	\textbf{Step 1 (Egorov).}
	For any $\varepsilon>0$ there is $A\subset E$ with $\mu(E\setminus A)<\varepsilon$ such that
	$f_n\to f$ uniformly on $A$.

	\textbf{Step 2 (convergence on $A$).}
	Uniform convergence and $|f_n|,|f|\le g$ imply
	\[
	\int_{A} |f_n-f|\,d\mu \;\longrightarrow\; 0.
	\]

	\textbf{Step 3 (control on the complement).}
	By domination,
	\[
	\int_{E\setminus A} |f_n-f|\,d\mu
	\;\le\; \int_{E\setminus A} (|f_n|+|f|)\,d\mu
	\;\le\; 2\int_{E\setminus A} g\,d\mu.
	\]
	Choosing $\varepsilon$ so that $\int_{E\setminus A} g<\delta$ gives the desired small tail.

	\textbf{Conclusion.}
	$\displaystyle \int_E |f_n-f|\,d\mu \to 0$; that is, DCT holds via Egorov + small tail.

	\medskip

	\textbf{Remark (infinite measure).}
	If $\mu(E)=\infty$ (e.g.\ $E=\mathbb R^n$), take an increasing sequence of bounded sets $K_R\uparrow E$ with
	$\int_{E\setminus K_R} g$ arbitrarily small. Apply the argument on $K_R$ and then let $R\to\infty$.
\end{spacy}

\tighthrule
\begin{spacy}
	\textbf{Convexity.}
	A function $\varphi:I\to\mathbb R$ is convex if
	\[
	\varphi(\lambda x+(1-\lambda)y)\le \lambda\varphi(x)+(1-\lambda)\varphi(y)
	\quad (x,y\in I,\ 0\le\lambda\le1).
	\]

	\textbf{Jensen's inequality.}
	Let $(E,\mathcal E,\nu)$ be a probability space, $\varphi$ convex on an interval containing the range of $X$.
	If $X$ is integrable, then
	\[
	\varphi\!\Big(\int_E X\,d\nu\Big) \;\le\; \int_E \varphi(X)\,d\nu.
	\]
	For concave $\varphi$ the inequality reverses.

	\textbf{Power means via Jensen.}
	For $p\ge 1$, $\varphi(t)=|t|^{p}$ is convex; hence
	\[
	\Big|\int_E f\,d\nu\Big|^{p}\le \int_E |f|^{p}\,d\nu.
	\]

	\textbf{Young's inequality (via convex duality).}
	For conjugate exponents $p,q>1$ and $a,b\ge0$,
	\[
	ab \;\le\; \frac{a^{p}}{p}+\frac{b^{q}}{q}.
	\]
	(Equivalently, the Legendre transform of $\phi(t)=t^{p}/p$ is $\phi^{\*}(s)=s^{q}/q$.)

	\textbf{Hölder from Young/Jensen.}
	Normalize $f,g$ by $\alpha=\|f\|_{p}$, $\beta=\|g\|_{q}$; write
	\[
	\frac{|fg|}{\alpha\beta}
	\le \frac{|f|^{p}}{p\,\alpha^{p}} + \frac{|g|^{q}}{q\,\beta^{q}}.
	\]
	Integrate to obtain
	$\int |fg|\le \|f\|_{p}\|g\|_{q}$.

	\textbf{AM--GM and log-sum.}
	Since $\log$ is concave,
	\[
	\log\!\Big(\sum_{i} \lambda_i x_i\Big) \;\ge\; \sum_i \lambda_i \log x_i
	\quad\Rightarrow\quad
	\sum_i \lambda_i x_i \;\ge\; \prod_i x_i^{\lambda_i},
	\]
	for $\lambda_i\ge0$, $\sum_i\lambda_i=1$, $x_i>0$.

	\textbf{KL-divergence nonnegativity.}
	For probability densities $p,q$ with $p\ll q$,
	\[
	D_{\mathrm{KL}}(p\|q)=\int p\log\frac{p}{q}\,d\mu \;\ge\; 0,
	\]
	by Jensen with convex $\varphi(t)=t\log t$ (or concavity of $\log$).

\end{spacy}
```

## CP-II-0485

- chapter line: 23737

```tex
\label{prob:cp-ii-0485}
\par\noindent\textbullet\quad \textbf{Closed-form analysis (geometric $\gamma$).}
	For $\gamma_j=r^j$, $0<r<1$,
	\[
	f(x)=\frac{rT_3(x)-r^2}{1-2rT_3(x)+r^2},\quad
	R_n(x)=\frac{r^{n+1}\big(T_{n+1}(T_3(x))-r\,T_n(T_3(x))\big)}{1-2rT_3(x)+r^2}.
	\]

	Given nonnegative coefficients $\gamma_j$, we approximate
	$f(x)=\sum_{j\ge1}\gamma_j T_{3j}(x)$ by the partial sum
	$P_n(x)=\sum_{j=1}^{n}\gamma_j T_{3j}(x)$.
	The points $x_k=\cos\!\big(\frac{k\pi}{3^{n+1}}\big)$ are used to
	\emph{certify the error}:
	\[
	f(x_k)-P_n(x_k)=(-1)^k S_n,\qquad S_n=\sum_{j>n}\gamma_j=\|f-P_n\|_\infty.
	\]
	They are \emph{not} interpolation nodes. Interpolation would require constructing
	a polynomial $Q$ such that $Q(y_i)=f(y_i)$ at prescribed nodes $y_i$.

Write $x=\cos\theta$ and expand
\[
f(x)=\sum_{m=0}^\infty a_m T_m(x),
\quad
a_m=\frac{2}{\pi}\int_{0}^{\pi} f(\cos\theta)\cos(m\theta)\,d\theta\ (m\ge1),\quad
a_0=\frac{1}{\pi}\int_{0}^{\pi} f(\cos\theta)\,d\theta.
\]
Set $\gamma_j:=a_{3j}$ so that
\[
f(x)=\sum_{j\ge1}\gamma_j T_{3j}(x)+a_0 T_0(x)
\quad\text{(with $a_m=0$ for $m\not\equiv 0\!\!\!\pmod 3$ if the expansion is exact).}
\]
Given nonnegative $\gamma_j$, the $n$-term truncation $P_n(x)=\sum_{j=1}^n\gamma_j T_{3j}(x)$
has uniform error
\[
\|f-P_n\|_\infty = S_n:=\sum_{j>n}\gamma_j,
\]
attained at $x_k=\cos\!\big(\frac{k\pi}{3^{n+1}}\big)$, where
$f(x_k)-P_n(x_k)=(-1)^k S_n$.

For example,
\[
f(x)=e^x,\quad f(x)=\sinh x,\quad\text{or any continuous function you can evaluate.}
\]

Use the cosine change of variable $x=\cos\theta$.
The Chebyshev expansion is
\[
f(x)=\sum_{m=0}^{\infty} a_m T_m(x),
\]
where the coefficients are given by
\[
a_0=\frac{1}{\pi}\int_0^{\pi} f(\cos\theta)\,d\theta,
\qquad
a_m=\frac{2}{\pi}\int_0^{\pi} f(\cos\theta)\cos(m\theta)\,d\theta,
\quad (m\ge1).
\]
In practice, these integrals are evaluated efficiently using a
\emph{Discrete Cosine Transform (DCT)}.

\[
\gamma_j := a_{3j}, \qquad j=1,2,\dots
\]
Now you have the nonnegative (if $f$ satisfies the theoremĂ˘â‚¬â„˘s assumption) sequence $\gamma_j$.

\[
P_n(x)=\sum_{j=1}^{n}\gamma_j\,T_{3j}(x).
\]
This $P_n$ is your $n$-term Chebyshev approximation to $f$.

\[
S_n=\sum_{j=n+1}^{\infty}\gamma_j.
\]
In practice, $S_n$ is approximated by summing until $\gamma_j$ become negligible.

\[
x_k=\cos\!\Big(\frac{k\pi}{3^{n+1}}\Big),
\qquad k=0,1,\dots,3^{n+1}.
\]
At these points, the error has the explicit alternating form
\[
f(x_k)-P_n(x_k)=(-1)^k\,S_n,
\]
so that $\|f-P_n\|_\infty=S_n$.

\bigskip

\begin{center}
	\renewcommand{\arraystretch}{1.3}
	\begin{tabular}{>{$}l<{$} | l}
		\hline
		\textbf{Symbol} & \textbf{Meaning} \\ \hline
		f(x) & Given continuous function on $[-1,1]$ \\
		T_m(x) & Chebyshev polynomial of degree $m$ \\
		a_m & Chebyshev coefficients of $f$ \\
		\gamma_j = a_{3j} & Extracted subsequence (used in this theorem) \\
		P_n(x)=\sum_{j=1}^{n}\gamma_j T_{3j}(x) & $n$-term approximation \\
		R_n(x)=f(x)-P_n(x) & Remainder (error) \\
		S_n=\sum_{j>n}\gamma_j & Uniform error magnitude \\
		x_k=\cos\frac{k\pi}{3^{n+1}} & Alternation points of $R_n$ \\
		f(x_k)-P_n(x_k)=(-1)^k S_n & Alternating error pattern \\ \hline
	\end{tabular}
\end{center}
```

## CP-II-0496

- chapter line: 23842

```tex
\label{prob:cp-ii-0496}
{Polynomial approximation of $1/z$ on a semicircle}{poly-1-over-z-semi}
	Construct a sequence of polynomials that converges uniformly to $1/z$ on
	\[
	K=\{\,z\in\mathbb C:\ |z|=1,\ \Re z\ge 0\,\}.
	\]
```

## CP-II-0510

- chapter line: 23851

```tex
\label{prob:cp-ii-0510}
ChebyshevĂ˘â‚¬â„˘s inequality and weak-$L^p$

\textbf{(a)} Prove that for $f\in L^p(\mathbb{R}^n)$ and $\lambda>0$,
\[
\big|\{x\in\mathbb{R}^n:\ |f(x)|>\lambda\}\big|
\;\le\; \frac{\|f\|_{L^p}^p}{\lambda^p}.
\]

\medskip
\textbf{(b)} Define the weak-$L^p$ space $L^{p,\mathrm{w}}(\mathbb{R}^n)$ to be the set of measurable
$f$ for which there exists $C>0$ such that
\[
\big|\{x\in\mathbb{R}^n:\ |f(x)|>\lambda\}\big|
\;\le\; \frac{C}{\lambda^p}\qquad\text{for all }\lambda>0.
\]
Show that $L^p(\mathbb{R}^n)\subset L^{p,\mathrm{w}}(\mathbb{R}^n)$ and that this inclusion is proper by
exhibiting an explicit function in $L^{p,\mathrm{w}}(\mathbb{R}^n)\setminus L^p(\mathbb{R}^n)$.

For $f\in L^p(\mathbb{R}^n)$ and $\lambda>0$,
\[
\big|\{x:\,|f(x)|>\lambda\}\big|
\;\le\; \frac{\|f\|_{L^p}^p}{\lambda^p}.
\]
\emph{Proof.} On $\{|f|>\lambda\}$, $|f|^p\ge \lambda^p$, hence
$\|f\|_p^p \ge \int_{\{|f|>\lambda\}} |f|^p \ge \lambda^p\,|\{|f|>\lambda\}|$.

We say $f\in L^{p,\mathrm{w}}(\mathbb{R}^n)$ if there exists $C$ such that
\[
\big|\{x:\,|f(x)|>\lambda\}\big| \;\le\; \frac{C}{\lambda^p}
\qquad\forall\,\lambda>0.
\]
By Chebyshev, $L^p(\mathbb{R}^n)\subset L^{p,\mathrm{w}}(\mathbb{R}^n)$ with $C=\|f\|_p^p$.

\emph{Properness.} Let $f(x)=|x|^{-n/p}\mathbf 1_{\{|x|\le 1\}}(x)$. Then, for $\lambda>1$,
\[
\{ |f|>\lambda \}=\{ |x|<\lambda^{-p/n}\}, \qquad
\big|\{|f|>\lambda\}\big| = c_n\,\lambda^{-p},
\]
so $f\in L^{p,\mathrm{w}}$. However
$\displaystyle \int_{|x|\le1}|f|^p=\int_{|x|\le1} |x|^{-n}\,dx=\infty$,
hence $f\notin L^p$. Therefore $L^p(\mathbb{R}^n)\subsetneq L^{p,\mathrm{w}}(\mathbb{R}^n)$.

\clearpage

\clearpage
```

## CP-II-0550

- chapter line: 23900

```tex
\label{prob:cp-ii-0550}
(for part (b) \& Minkowski): \boldmath $F(x,y)=f(x)\,h(y)$

Take
\[
f(x)=(1+|x|)^{-\alpha}\quad (\alpha>1,\ \text{so } f\in L^1(\mathbb{R})),
\qquad
h(y)=e^{-|y|}\in L^p(\mathbb{R})\ (1\le p<\infty),
\]
and define $F(x,y)=f(x)\,h(y)$. Then
\[
G(y) \;=\; \int_{\mathbb{R}} F(x,y)\,dx \;=\; \Bigl(\int_{\mathbb{R}} f(x)\,dx\Bigr) h(y) \;=\; \|f\|_{L^1}\,h(y).
\]

\begin{center}
\resizebox{\linewidth}{!}{$\displaystyle
\|f\|_{L^1}
\;=\; \int_{\mathbb{R}}(1+|x|)^{-\alpha}\,dx
\;=\; 2\!\int_{0}^{\infty} (1+x)^{-\alpha}\,dx
\;=\; \boxed{\ \tfrac{2}{\alpha-1}\ },
\qquad
\|h\|_{L^p}
\;=\; \Bigl(\int_{\mathbb{R}} e^{-p|y|}\,dy\Bigr)^{\!1/p}
\;=\; \boxed{\ \bigl(\tfrac{2}{p}\bigr)^{1/p}\ }.
$}
\end{center}

\par\medskip\noindent\textbf{Inequality with a given $g\in L^q$, $\|g\|_{L^q}\le1$.}\quad
\begin{center}
\resizebox{\linewidth}{!}{$\displaystyle
\int_{\mathbb{R}} |G(y)|\,|g(y)|\,dy
\;=\; \|f\|_{L^1} \int_{\mathbb{R}} |h(y)|\,|g(y)|\,dy
\;\le\; \|f\|_{L^1}\,\|h\|_{L^p}\,\|g\|_{L^q}
\;\le\; \|f\|_{L^1}\,\|h\|_{L^p}.
$}
\end{center}

\[
\int_{\mathbb{R}} \Bigl(\int_{\mathbb{R}} |F(x,y)|^p\,dy\Bigr)^{\!1/p} dx
\;=\; \int_{\mathbb{R}} |f(x)|\,\|h\|_{L^p}\,dx
\;=\; \|f\|_{L^1}\,\|h\|_{L^p}.
\]
Hence we obtain equality and MinkowskiĂ˘â‚¬â„˘s integral inequality:
\[
\|G\|_{L_y^p}
\;=\; \|\|f\|_{L^1}\,h\|_{L_y^p}
\;=\; \|f\|_{L^1}\,\|h\|_{L^p}
\;\le\; \int_{\mathbb{R}} \Bigl(\int_{\mathbb{R}} |F(x,y)|^p\,dy\Bigr)^{\!1/p} dx.
\]
Equality occurs for the Hölder extremizer $g(y)=h(y)^{p-1}/\|h\|_{L^p}^{\,p-1}$ (since $h\ge 0$).

\clearpage
```
