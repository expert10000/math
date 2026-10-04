# Part II missing-solution batch 19

- problems: **20**
- IDs: CP-II-0527, CP-II-0529, CP-II-0531, CP-II-0537, CP-II-0538, CP-II-0541, CP-II-0543, CP-II-0546, CP-II-0553, CP-II-0556, CP-II-0557, CP-II-0558, CP-II-0560, CP-II-0561, CP-II-0563, CP-II-0566, CP-II-0018, CP-II-0098, CP-II-0112, CP-II-0159

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
