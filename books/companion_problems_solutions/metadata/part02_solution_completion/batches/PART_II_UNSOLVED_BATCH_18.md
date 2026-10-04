# Part II missing-solution batch 18

- problems: **20**
- IDs: CP-II-0490, CP-II-0491, CP-II-0497, CP-II-0501, CP-II-0503, CP-II-0504, CP-II-0505, CP-II-0507, CP-II-0509, CP-II-0511, CP-II-0512, CP-II-0515, CP-II-0516, CP-II-0517, CP-II-0518, CP-II-0519, CP-II-0521, CP-II-0522, CP-II-0525, CP-II-0526

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
