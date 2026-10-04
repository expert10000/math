# Part II missing-solution batch 14

- problems: **20**
- IDs: CP-II-0312, CP-II-0314, CP-II-0316, CP-II-0318, CP-II-0319, CP-II-0324, CP-II-0327, CP-II-0329, CP-II-0335, CP-II-0336, CP-II-0337, CP-II-0339, CP-II-0343, CP-II-0344, CP-II-0347, CP-II-0348, CP-II-0351, CP-II-0352, CP-II-0356, CP-II-0360

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
