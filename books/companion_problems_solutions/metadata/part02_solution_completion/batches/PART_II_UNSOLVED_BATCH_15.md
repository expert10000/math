# Part II missing-solution batch 15

- problems: **20**
- IDs: CP-II-0361, CP-II-0364, CP-II-0366, CP-II-0369, CP-II-0370, CP-II-0376, CP-II-0379, CP-II-0380, CP-II-0381, CP-II-0382, CP-II-0384, CP-II-0385, CP-II-0386, CP-II-0387, CP-II-0388, CP-II-0389, CP-II-0390, CP-II-0392, CP-II-0394, CP-II-0397

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
