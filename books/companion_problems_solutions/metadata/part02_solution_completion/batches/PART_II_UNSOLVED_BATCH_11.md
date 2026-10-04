# Part II missing-solution batch 11

- problems: **20**
- IDs: CP-II-0189, CP-II-0192, CP-II-0194, CP-II-0195, CP-II-0196, CP-II-0199, CP-II-0201, CP-II-0204, CP-II-0205, CP-II-0207, CP-II-0208, CP-II-0209, CP-II-0210, CP-II-0211, CP-II-0213, CP-II-0214, CP-II-0219, CP-II-0221, CP-II-0224, CP-II-0226

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
