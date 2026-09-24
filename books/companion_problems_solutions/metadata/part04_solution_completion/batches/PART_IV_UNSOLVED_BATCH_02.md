# Part IV Unsolved Solution Authoring Batch 02

- problems in batch: 20
- IDs: CP-IV-0129, CP-IV-0134, CP-IV-0024, CP-IV-0025, CP-IV-0048, CP-IV-0053, CP-IV-0062, CP-IV-0070, CP-IV-0076, CP-IV-0079, CP-IV-0098, CP-IV-0099, CP-IV-0110, CP-IV-0137, CP-IV-0004, CP-IV-0007, CP-IV-0008, CP-IV-0016, CP-IV-0019, CP-IV-0023

Author canonical worked solutions for these problems. Do not alter the problem statements.

## CP-IV-0129


- chapter line: 2904
- atlas source solution flag: `unknown`
- linked source-solution candidates: `none`
- embedded solution marker in problem body: `NO`

```tex
\par\noindent\textbullet\quad \textbf{Pole:} $|f(z)|\to\infty$ as $z\to a$; equivalently, $(z-a)^m f(z)$ extends holomorphically with nonzero value at $a$ for some $m\in\mathbb N$.
```

## CP-IV-0134


- chapter line: 2931
- atlas source solution flag: `unknown`
- linked source-solution candidates: `none`
- embedded solution marker in problem body: `NO`

```tex
\par\noindent\textbullet\quad \textbf{Isotropic:} conformality is equivalent to
	\[
	\phi_z\cdot \phi_z = 0
	\qquad\text{(complex bilinear dot product).}
	\]

\smallskip
\textbf{The holomorphic $\mathbb C^3$-valued $1$-form.}
Now set
\[
\Phi := 2\phi_z \in \mathbb C^3.
\]
Then $\Phi$ is a holomorphic map into $\mathbb C^3$ satisfying $\Phi\cdot \Phi=0$.
The $1$-form $\Phi\,dz$ is the holomorphic $\mathbb C^3$-valued form that one integrates to recover $\phi$:
\[
\Psi(z)=\int^z \Phi(\zeta)\,d\zeta \in \mathbb C^3,
\qquad
\phi(z)=\Re \Psi(z)\in \mathbb R^3.
\]

\smallskip
\textbf{Geometric meaning.}
The function $g$ is (up to stereographic projection) the Gauss map: it encodes the unit normal direction
$N\in\mathbb S^2$. Concretely,
\[
N
=
\frac{1}{1+|g|^2}\,\bigl(2\Re g,\ 2\Im g,\ |g|^2-1\bigr),
\]
which is inverse stereographic projection from $g\in\mathbb C$ to $N\in\mathbb S^2$.
The holomorphic $1$-form $f\,dz$ controls the conformal scale; the induced metric is
\[
ds^2
=
\frac{|f|^2(1+|g|^2)^2}{4}\,|dz|^2.
\]
Thus $|f|$ (together with $|g|$) determines local lengths; multiplying $f$ by $e^{-i\theta}$ rotates the differential but
does not change the metric.

\smallskip
\textbf{Clarifying the target spaces ($\mathbb C^3$ vs.\ $\mathbb R^3$ vs.\ $\mathbb C^2$).}
```

## CP-IV-0024


- chapter line: 2980
- atlas source solution flag: `unknown`
- linked source-solution candidates: `none`
- embedded solution marker in problem body: `NO`

```tex
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
```

## CP-IV-0025


- chapter line: 3043
- atlas source solution flag: `unknown`
- linked source-solution candidates: `none`
- embedded solution marker in problem body: `NO`

```tex
Classify the singularities of
\[
\frac{z}{\sin z},\qquad
\sin\!\Big(\frac{\pi}{z^{2}}\Big),\qquad
\frac{1}{z^{2}}+\frac{1}{z^{2}+1},\qquad
\frac{1}{z^{2}}\cos\!\Big(\frac{\pi z}{z+1}\Big).
\]

At an isolated singularity $a$, if the Laurent expansion
$f(z)=\sum_{k=-m}^{\infty} c_k (z-a)^k$ has
(i) $m=0$ $\Rightarrow$ removable;
(ii) finitely many negative terms with highest $(z-a)^{-m}$ $\Rightarrow$ pole of order $m$;
(iii) infinitely many negative terms $\Rightarrow$ essential.

\medskip
\emph{(1) $\boldsymbol{z/\sin z}$.}
Near $0$, $\sin z=z-\frac{z^{3}}{6}+O(z^{5})$, so
\[
\frac{z}{\sin z}=1+\frac{z^{2}}{6}+O(z^{4}),
\]
hence $z=0$ is \textbf{removable} (define value $1$). At $z=n\pi$, $n\in\mathbb Z\setminus\{0\}$,
$\sin z$ has simple zeros and the numerator is nonzero, so each $n\pi$ is a \textbf{simple pole}.

\medskip
\emph{(2) $\boldsymbol{\sin(\pi/z^{2})}$.}
Using $\sin w=\sum_{k\ge0}\frac{(-1)^k w^{2k+1}}{(2k+1)!}$ with $w=\pi/z^{2}$,
\[
\sin\!\Big(\frac{\pi}{z^{2}}\Big)=\sum_{k=0}^{\infty}\frac{(-1)^k \pi^{2k+1}}{(2k+1)!}\,z^{-4k-2},
\]
which contains infinitely many negative powers. Thus $z=0$ is an \textbf{essential singularity}.
There are no other singularities.

\medskip
\emph{(3) $\boldsymbol{1/z^{2} + 1/(z^{2}+1)}$.}
At $z=0$ one has a \textbf{pole of order $2$}. At $z=\pm i$ (simple zeros of $z^{2}+1$) there are
\textbf{simple poles}. No other singularities occur.

\medskip
\emph{(4) $\boldsymbol{z^{-2}\cos\!\big(\pi z/(z+1)\big)}$.}
Let $h(z)=\dfrac{\pi z}{z+1}$.
Near $z=0$, $h(z)=\pi(z-z^{2}+z^{3}-\cdots)$, hence
\[
\cos h(z)=1-\tfrac12 h(z)^{2}+O(z^{3})=1-\tfrac{\pi^{2}}{2}z^{2}+O(z^{3}),
\]
and
\[
\frac{1}{z^{2}}\cos h(z)=\frac{1}{z^{2}}-\frac{\pi^{2}}{2}+O(z),
\]
so $z=0$ is a \textbf{pole of order $2$}. At $z=-1$, $h$ has a simple pole; since
$\cos w=\tfrac12(e^{iw}+e^{-iw})$, composition with a pole yields an \textbf{essential singularity}
at $z=-1$. There are no other singularities.
```

## CP-IV-0048


- chapter line: 3146
- atlas source solution flag: `unknown`
- linked source-solution candidates: `none`
- embedded solution marker in problem body: `NO`

```tex
â€” area from a $1$-form (what $\tfrac12(x\,dy-y\,dx)$ measures)

Set
\[
\alpha \;=\; \frac12\,(x\,dy - y\,dx).
\]
Then
\[
d\alpha
=
\frac12\,(dx\wedge dy + dy\wedge dx)
=
dx\wedge dy.
\]
Hence, by Stokes/Green,
\[
\oint_{C} \alpha
=
\iint_{D} dx\wedge dy
=
\operatorname{Area}(D)
=
\pi R^2.
\]
Therefore,
\[
\boxed{\ \frac12 \oint_{C} (x\,dy - y\,dx)\;=\;\operatorname{Area}(D)\;=\;\pi R^2\ }.
\]

	\par\noindent\textbullet\quad Pick $\mathbf F=(L,M)$ $\Rightarrow$ $1$-form $L\,dx+M\,dy$.
	\par\noindent\textbullet\quad Circulation (line integral on $C$) equals total curl over $D$.
	\par\noindent\textbullet\quad If $\;M_x-L_y\equiv 0$ on $D$, then $\displaystyle \oint_{C}(L\,dx+M\,dy)=0$ (path-independence on simply connected $D$).
	\par\noindent\textbullet\quad The special $1$-form $\tfrac12(x\,dy - y\,dx)$ integrates to the enclosed area.
```

## CP-IV-0053


- chapter line: 3183
- atlas source solution flag: `unknown`
- linked source-solution candidates: `none`
- embedded solution marker in problem body: `NO`

```tex
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
```

## CP-IV-0062


- chapter line: 3246
- atlas source solution flag: `unknown`
- linked source-solution candidates: `none`
- embedded solution marker in problem body: `NO`

```tex
\par\noindent\textbullet\quad Define
	\[
	g(z):=f(z)-z .
	\]
	Then $g$ is entire and $g(1/n)=0$ for all $n$. Since $1/n\to 0$ (an interior point),
	the identity theorem gives $g\equiv 0$, hence $f(z)\equiv z$.

	\medskip
```

## CP-IV-0070


- chapter line: 3258
- atlas source solution flag: `unknown`
- linked source-solution candidates: `none`
- embedded solution marker in problem body: `NO`

```tex
\par\noindent\textbullet\quad Show that $F$ has poles at $z=\pm i$ and at each integer $z=n$, $n\in\mathbb{Z}$. Compute the residues at these poles and verify that
	\[
	\operatorname{Res}(F,\pm i)
	= -\frac{\cosh(\pi-\theta)}{4\sinh\pi},
	\qquad
	\operatorname{Res}(F,n)
	= \frac{\cos(n\theta)}{2\pi\,(1+n^2)}.
	\]

	\par\noindent\textbullet\quad For each $N\in\mathbb{N}$ define four curves $\Gamma^{(N)}_j$ on $[-1,1]$ by
	\[
	\Gamma^{(N)}_1(t) = \Bigl(N+\tfrac12\Bigr)(1+it),\qquad
	\Gamma^{(N)}_2(t) = \Bigl(N+\tfrac12\Bigr)(-t+i),
	\]
	\[
	\Gamma^{(N)}_3(t) = \Bigl(N+\tfrac12\Bigr)(-1-it),\qquad
	\Gamma^{(N)}_4(t) = \Bigl(N+\tfrac12\Bigr)(t-i),
	\]
	and let $\Gamma^{(N)}$ be the closed contour obtained by following
	$\Gamma^{(N)}_1,\Gamma^{(N)}_2,\Gamma^{(N)}_3,\Gamma^{(N)}_4$ in turn.
	Sketch $\Gamma^{(N)}$ in the complex plane and indicate the locations of the poles of $F$ relative to this rectangle.

	\par\noindent\textbullet\quad Show that there exists a constant $C>0$, independent of $N$, such that for all integers $N\ge 1$ and all $\theta\in[0,2\pi]$,
	\[
	\left| \int_{\Gamma^{(N)}} F(z)\,dz \right|
	\le \frac{C}{N}.
	\]

	\par\noindent\textbullet\quad Using Cauchyâ€™s residue theorem applied to $\Gamma^{(N)}$, show that for $0\le\theta\le 2\pi$,
	\[
	\left|
	\frac{\cosh(\pi-\theta)}{2\sinh\pi}
	- \sum_{n=-N}^N \frac{e^{in\theta}}{1+n^2}
	\right|
	\le \frac{C}{N},
	\]
	and deduce that
	\[
	\frac{\cosh(\pi-\theta)}{2\sinh\pi}
	= \sum_{n=-\infty}^{\infty} \frac{e^{in\theta}}{1+n^2},
	\]
	with the series converging uniformly in $\theta\in[0,2\pi]$.

The function $F$ is meromorphic on $\mathbb{C}$, being the product of the entire function
$\cos\bigl((\pi-\theta)z\bigr)$ with the factors $(1+z^2)^{-1}$ and $(\sin\pi z)^{-1}$.
The only singularities of $F$ are poles arising from zeros of $1+z^2$ and $\sin(\pi z)$.

The equation $1+z^2=0$ has solutions $z=\pm i$, which give simple poles of $F$.
The function $\sin(\pi z)$ vanishes simply at each integer $z=n\in\mathbb{Z}$, so
$(\sin\pi z)^{-1}$ has simple poles there. Since $1+z^2$ does not vanish at any integer,
$F$ also has simple poles at all $z=n\in\mathbb{Z}$.

For a simple pole at $a\in\mathbb{C}$, the residue is given by
\[
\operatorname{Res}(F,a) = \lim_{z\to a} (z-a)\,F(z).
\]
At an integer $n$ one uses the local behaviour
$\sin(\pi z) = \pi(-1)^n(z-n) + O\bigl((z-n)^2\bigr)$ and evaluates the remaining factors at $z=n$.
At $z=\pm i$ one factors $1+z^2=(z-i)(z+i)$ and again evaluates the remaining analytic part at the pole.

The contour $\Gamma^{(N)}$ is a rectangle with vertices
\[
\pm\Bigl(N+\tfrac12\Bigr)\pm i,
\]
with horizontal sides at $\Im z=\pm1$ and vertical sides at $\Re z=\pm(N+\tfrac12)$.
For each fixed $N$, the contour encloses the poles at $z=\pm i$ and at the integers $n$ with $|n|\le N$.

Cauchyâ€™s residue theorem states that for such a closed contour,
\[
\int_{\Gamma^{(N)}} F(z)\,dz
= 2\pi i \sum_{a\in\mathcal{P}_N} \operatorname{Res}(F,a),
\]
where $\mathcal{P}_N$ is the finite set of poles of $F$ inside $\Gamma^{(N)}$.
Here $\mathcal{P}_N=\{-i,+i\}\cup\{n\in\mathbb{Z}:|n|\le N\}$.

To estimate the integral along $\Gamma^{(N)}$ one uses the estimation lemma
\[
\left|\int_{\Gamma^{(N)}} F(z)\,dz\right|
\le \sup_{z\in\Gamma^{(N)}} |F(z)|\cdot \operatorname{length}(\Gamma^{(N)}).
\]
On the vertical segments, $z = \pm\bigl(N+\tfrac12\bigr) + it$ with $-1\le t\le 1$, the factor
$1/(1+z^2)$ is of order $1/N^2$, whereas $\cos\bigl((\pi-\theta)z\bigr)$ and
$1/\sin(\pi z)$ are uniformly bounded in $N$, since $\Im z$ stays in a compact set.
On the horizontal segments, $\Re z$ is bounded and $\Im z=\pm1$, so $F$ remains uniformly bounded.
Combining these facts gives a bound of the form
\[
\left|\int_{\Gamma^{(N)}} F(z)\,dz\right|
\le \frac{C}{N}
\]
for some constant $C$ independent of $N$ and $\theta$.

Substituting the residue computations into the residue theorem gives an identity of the form
\[
\frac{\cosh(\pi-\theta)}{2\sinh\pi}
- \sum_{n=-N}^N \frac{e^{in\theta}}{1+n^2}
= \frac{1}{2\pi i}\int_{\Gamma^{(N)}} F(z)\,dz,
\]
so that the absolute value of the difference is bounded by $C/N$.
Letting $N\to\infty$ shows that the Fourier series
\[
\sum_{n=-\infty}^{\infty} \frac{e^{in\theta}}{1+n^2}
\]
converges uniformly in $\theta\in[0,2\pi]$ and represents $\cosh(\pi-\theta)/(2\sinh\pi)$.
```

## CP-IV-0076


- chapter line: 3367
- atlas source solution flag: `unknown`
- linked source-solution candidates: `none`
- embedded solution marker in problem body: `NO`

```tex
Find the Laurent expansion (in powers of $z$, i.e.\ about $0$) of
\[
\frac{1}{z^{2}-3z+2}=\frac{1}{(z-1)(z-2)}
\]
in the regions $\{|z|<1\}$, $\{1<|z|<2\}$, and $\{|z|\ge 2\}$.

Partial fractions:
\[
\frac{1}{(z-1)(z-2)}=-\frac{1}{z-1}+\frac{1}{z-2}.
\]
Geometric expansions:
\[
\frac{1}{1-w}=\sum_{n=0}^{\infty}w^{n}\quad(|w|<1),\qquad
\frac{1}{z-a}=\frac{1}{z}\cdot\frac{1}{1-\frac{a}{z}}
=\sum_{n=0}^{\infty}\frac{a^{n}}{z^{n+1}}\quad(|z|>|a|).
\]

\emph{(A) For $|z|<1$.}
\[
-\frac{1}{z-1}=\frac{1}{1-z}=\sum_{n=0}^{\infty}z^{n},\qquad
\frac{1}{z-2}=-\frac{1}{2}\frac{1}{1-\frac{z}{2}}
=-\sum_{n=0}^{\infty}\frac{z^{n}}{2^{\,n+1}}.
\]
Hence
\[
\boxed{\ \frac{1}{z^{2}-3z+2}=\sum_{n=0}^{\infty}\Big(1-2^{-(n+1)}\Big)z^{n},\quad |z|<1.\ }
\]

\medskip
\emph{(B) For $1<|z|<2$.}
\[
-\frac{1}{z-1}=-\frac{1}{z}\frac{1}{1-\frac{1}{z}}
=-\sum_{n=1}^{\infty} z^{-n},\qquad
\frac{1}{z-2}=-\sum_{n=0}^{\infty}\frac{z^{n}}{2^{\,n+1}}.
\]
Thus
\[
\boxed{\ \frac{1}{z^{2}-3z+2}
	=-\sum_{n=1}^{\infty} z^{-n}-\sum_{n=0}^{\infty}\frac{z^{n}}{2^{\,n+1}},
	\quad 1<|z|<2.\ }
\]

\medskip
\emph{(C) For $|z|>2$.}
\[
-\frac{1}{z-1}=-\sum_{m=1}^{\infty} z^{-m},\qquad
\frac{1}{z-2}=\frac{1}{z}\frac{1}{1-\frac{2}{z}}
=\sum_{m=1}^{\infty}\frac{2^{\,m-1}}{z^{m}}.
\]
Therefore
\[
\boxed{\ \frac{1}{z^{2}-3z+2}
	=\sum_{m=1}^{\infty}\big(2^{\,m-1}-1\big)z^{-m},\quad |z|>2.\ }
\]
```

## CP-IV-0079


- chapter line: 3426
- atlas source solution flag: `unknown`
- linked source-solution candidates: `none`
- embedded solution marker in problem body: `NO`

```tex
(restated).

Let $p(z)=z^{n}+a_{n-1}z^{n-1}+\cdots+a_1 z+a_0$ be a polynomial of degree $n$ and set
$A=\max\{|a_0|,\dots,|a_{n-1}|\}$. Prove that $p$ has $n$ zeros
(counting multiplicity) in the disk $\{|z|<A+1\}$.

Let $p(z)=z^{n}+a_{n-1}z^{n-1}+\cdots+a_0$ and $A=\max_{k}|a_k|$. For $|z|\ge A+1$,
\[
|p(z)|\ge |z|^{n}-\sum_{k=0}^{n-1}|a_k||z|^{k}
\ge |z|^{n}-A\,\frac{|z|^{n}-1}{|z|-1}>0.
\]
Hence $p$ has no zeros for $|z|\ge A+1$, so all (exactly $n$) zeros lie in $|z|<A+1$.

\medskip
```

## CP-IV-0098


- chapter line: 3444
- atlas source solution flag: `unknown`
- linked source-solution candidates: `none`
- embedded solution marker in problem body: `NO`

```tex
â€” Solution

We consider, for fixed $\theta\in[0,2\pi]$, the meromorphic function
\[
F(z) = \frac{1}{1+z^2}\,\frac{\cos\bigl((\pi-\theta)z\bigr)}{2\sin(\pi z)}.
\]

The factor $\cos\bigl((\pi-\theta)z\bigr)$ is entire, so the singularities of $F$
arise from the denominators $1+z^2$ and $\sin(\pi z)$.

	\par\noindent\textbullet\quad The zeros of $1+z^2$ are $z=\pm i$, and these are simple.
	\par\noindent\textbullet\quad The zeros of $\sin(\pi z)$ are the integers $z=n\in\mathbb{Z}$,
	and each zero is simple, so $(\sin\pi z)^{-1}$ has simple poles at all integers.

Thus $F$ has simple poles at $z=\pm i$ and at each $z=n\in\mathbb{Z}$.

For a simple pole at $a$, we have
\[
\operatorname{Res}(F,a) = \lim_{z\to a}(z-a)F(z).
\]

We factor
\[
1+z^2=(z-i)(z+i).
\]
Hence the residue of $(1+z^2)^{-1}$ at $z=i$ is
\[
\operatorname{Res}\Bigl(\frac{1}{1+z^2},i\Bigr)
=\frac{1}{2i}, \qquad
\operatorname{Res}\Bigl(\frac{1}{1+z^2},-i\Bigr)
=-\frac{1}{2i}.
\]
Using $\cos(ix)=\cosh x$ and $\sin(ix)=i\sinh x$ we have
\[
\cos\bigl((\pi-\theta)i\bigr)=\cosh(\pi-\theta),
\qquad
\sin(\pi i)=i\sinh\pi,
\qquad
\sin(-\pi i)=-i\sinh\pi.
\]
Therefore
\[
\operatorname{Res}(F,i)
=\frac{1}{2i}\cdot\frac{\cosh(\pi-\theta)}{2\sin(\pi i)}
=\frac{1}{2i}\cdot\frac{\cosh(\pi-\theta)}{2i\sinh\pi}
=-\frac{\cosh(\pi-\theta)}{4\sinh\pi},
\]
and
\[
\operatorname{Res}(F,-i)
=-\frac{1}{2i}\cdot\frac{\cosh(\pi-\theta)}{2\sin(-\pi i)}
=-\frac{1}{2i}\cdot\frac{\cosh(\pi-\theta)}{-2i\sinh\pi}
=-\frac{\cosh(\pi-\theta)}{4\sinh\pi}.
\]
Thus
\[
\operatorname{Res}(F,\pm i)=-\frac{\cosh(\pi-\theta)}{4\sinh\pi}.
\]

Let $n\in\mathbb{Z}$. Near $z=n$ we have
\[
\sin(\pi z)
=\sin\bigl(\pi n + \pi(z-n)\bigr)
=\sin(\pi n)\cos(\pi(z-n))
+\cos(\pi n)\sin(\pi(z-n)).
\]
Since $\sin(\pi n)=0$ and $\cos(\pi n)=(-1)^n$, it follows that
\[
\sin(\pi z)
=(-1)^n\pi(z-n) + O\bigl((z-n)^2\bigr),
\]
and therefore
\[
\frac{1}{\sin(\pi z)}
=\frac{(-1)^n}{\pi}\frac{1}{z-n}+O(1).
\]
The other factors are analytic at $z=n$, so
\[
\operatorname{Res}(F,n)
=\frac{1}{1+n^2}\cdot\frac{\cos\bigl((\pi-\theta)n\bigr)}{2}
\cdot\frac{(-1)^n}{\pi}.
\]
Using
\[
\cos\bigl((\pi-\theta)n\bigr)
=\cos(\pi n-n\theta)
=\cos(\pi n)\cos(n\theta)+\sin(\pi n)\sin(n\theta)
=(-1)^n\cos(n\theta),
\]
we obtain
\[
\operatorname{Res}(F,n)
=\frac{(-1)^n}{2\pi(1+n^2)}\cdot (-1)^n\cos(n\theta)
=\frac{\cos(n\theta)}{2\pi(1+n^2)}.
\]

\subsection*{(b) The contour $\Gamma^{(N)}$}

For $N\in\mathbb{N}$, the four curves
\[
\Gamma^{(N)}_1(t)=\Bigl(N+\tfrac12\Bigr)(1+it),\quad
\Gamma^{(N)}_2(t)=\Bigl(N+\tfrac12\Bigr)(-t+i),
\]
\[
\Gamma^{(N)}_3(t)=\Bigl(N+\tfrac12\Bigr)(-1-it),\quad
\Gamma^{(N)}_4(t)=\Bigl(N+\tfrac12\Bigr)(t-i),
\qquad -1\le t\le 1,
\]
form the sides of the rectangle whose vertices are
\[
\pm\Bigl(N+\tfrac12\Bigr)\pm i.
\]
We denote by $\Gamma^{(N)}$ the closed contour obtained by successively
traversing $\Gamma^{(N)}_1,\dots,\Gamma^{(N)}_4$.

This rectangle encloses the poles at $z=\pm i$ and at $z=n$ for all integers
$n$ with $|n|\le N$.

A schematic picture is shown in Figure~\ref{fig:contour-poles}.
\input{figures/part04/tikz/cp_iv_0098_source_figure_01.tex}


We claim that there exists a constant $C>0$, independent of $N$ and $\theta$,
such that
\[
\left|\int_{\Gamma^{(N)}} F(z)\,dz\right|\le \frac{C}{N}
\qquad\text{for all } N\ge1.
\]

A standard way to see this is to decompose $\Gamma^{(N)}$ into its four sides
and apply the estimation lemma.

On the vertical sides we have $z=\pm\bigl(N+\tfrac12\bigr)+it$ with $|t|\le1$.
Then $|z|^2\asymp N^2$ and hence
\[
\left|\frac{1}{1+z^2}\right|\le \frac{C_1}{N^2}.
\]
Moreover, for such $z$ the imaginary part is bounded, so both
$\cos\bigl((\pi-\theta)z\bigr)$ and $1/\sin(\pi z)$ are uniformly bounded in
$N$. The length of each vertical side is $2$, so the total contribution of the
vertical sides is $O(N^{-2})$.

On the horizontal sides we have $z=x\pm i$ with
$-(N+\tfrac12)\le x\le N+\tfrac12$. Using explicit expressions for
$\cos\bigl((\pi-\theta)(x\pm i)\bigr)$ and $\sin\bigl(\pi(x\pm i)\bigr)$, one
checks that
\[
|F(x+i)-F(x-i)| \le \frac{C_2}{1+|x|^3}
\qquad\text{for all }x\in\mathbb{R},
\]
and that $|F(x\pm i)|\le C_3/(1+x^2)$ for large $|x|$. Writing the integral
over the two horizontal sides as
\[
\int_{-(N+1/2)}^{N+1/2} \bigl(F(x+i)-F(x-i)\bigr)\,dx,
\]
one sees that the tail for $|x|\ge N$ is $O(N^{-2})$, while the integral over
$|x|\le N$ remains bounded independently of $N$. Altogether this yields a
bound of the form
\[
\left|\int_{\Gamma^{(N)}} F(z)\,dz\right|
\le \frac{C}{N}
\]
for some constant $C$ independent of $N$.

By Cauchyâ€™s residue theorem,
\[
\int_{\Gamma^{(N)}} F(z)\,dz
=2\pi i\sum_{a\in\mathcal{P}_N}\operatorname{Res}(F,a),
\]
where $\mathcal{P}_N=\{-i,+i\}\cup\{n\in\mathbb{Z}:|n|\le N\}$ is the set of
poles inside the rectangle. Using the residues computed in part (a),
\[
\sum_{a\in\mathcal{P}_N}\operatorname{Res}(F,a)
= \operatorname{Res}(F,i)+\operatorname{Res}(F,-i)
+\sum_{n=-N}^N \operatorname{Res}(F,n)
= -\frac{\cosh(\pi-\theta)}{2\sinh\pi}
+\sum_{n=-N}^N \frac{\cos(n\theta)}{2\pi(1+n^2)}.
\]
Therefore
\[
\int_{\Gamma^{(N)}} F(z)\,dz
= 2\pi i\left(
-\frac{\cosh(\pi-\theta)}{2\sinh\pi}
+\sum_{n=-N}^N \frac{\cos(n\theta)}{2\pi(1+n^2)}
\right),
\]
or equivalently
\[
\frac{\cosh(\pi-\theta)}{2\sinh\pi}
-\sum_{n=-N}^N \frac{\cos(n\theta)}{2\pi(1+n^2)}
= -\frac{1}{2\pi i}\int_{\Gamma^{(N)}} F(z)\,dz.
\]

Using the estimate from part (c) we obtain
\[
\left|
\frac{\cosh(\pi-\theta)}{2\sinh\pi}
-\sum_{n=-N}^N \frac{\cos(n\theta)}{2\pi(1+n^2)}
\right|
\le \frac{1}{2\pi}
\left|\int_{\Gamma^{(N)}} F(z)\,dz\right|
\le \frac{C}{N}.
\]
Since
\[
\frac{1}{2\pi}\sum_{n=-N}^N \frac{\cos(n\theta)}{1+n^2}
= \Re\left(\sum_{n=-N}^N \frac{e^{in\theta}}{1+n^2}\right),
\]
we can rewrite this in the complex exponential form
\[
\left|
\frac{\cosh(\pi-\theta)}{2\sinh\pi}
-\sum_{n=-N}^N \frac{e^{in\theta}}{1+n^2}
\right|
\le \frac{C}{N}.
\]
Letting $N\to\infty$ gives, uniformly in $\theta\in[0,2\pi]$,
\[
\frac{\cosh(\pi-\theta)}{2\sinh\pi}
=\sum_{n=-\infty}^{\infty} \frac{e^{in\theta}}{1+n^2},
\]
which is the desired Fourier series representation.


\bigskip
\noindent\rule{\textwidth}{0.4pt}
\medskip

We first recall the residues already computed:
\begin{align*}
	\operatorname{Res}(F,\pm i) &= -\,\frac{\cosh(\pi-\theta)}{4\sinh\pi},\\[4pt]
	\operatorname{Res}(F,n) &= \frac{\cos(n\theta)}{2\pi(1+n^2)}, \qquad n\in\mathbb{Z}.
\end{align*}

The set of poles inside $\Gamma^{(N)}$ is
\[
\mathcal{P}_N = \{-i,+i\}\cup\{n\in\mathbb{Z}:|n|\le N\},
\]
so
\begin{equation*}
	\sum_{a\in\mathcal{P}_N} \operatorname{Res}(F,a)
	= \operatorname{Res}(F,i)+\operatorname{Res}(F,-i)+\sum_{n=-N}^{N}\operatorname{Res}(F,n).
\end{equation*}

Now substitute the explicit formulas and simplify **step by step**:
\begin{align*}
	\sum_{a\in\mathcal{P}_N} \operatorname{Res}(F,a)
	&= \left(-\frac{\cosh(\pi-\theta)}{4\sinh\pi}\right)
	+\left(-\frac{\cosh(\pi-\theta)}{4\sinh\pi}\right)
	+\sum_{n=-N}^{N}\frac{\cos(n\theta)}{2\pi(1+n^2)}\\[6pt]
	&= -\frac{\cosh(\pi-\theta)}{4\sinh\pi}
	-\frac{\cosh(\pi-\theta)}{4\sinh\pi}
	+\sum_{n=-N}^{N}\frac{\cos(n\theta)}{2\pi(1+n^2)}\\[6pt]
	&= -\left(
	\frac{\cosh(\pi-\theta)}{4\sinh\pi}
	+\frac{\cosh(\pi-\theta)}{4\sinh\pi}
	\right)
	+\sum_{n=-N}^{N}\frac{\cos(n\theta)}{2\pi(1+n^2)}\\[6pt]
	&= -\frac{2\cosh(\pi-\theta)}{4\sinh\pi}
	+\sum_{n=-N}^{N}\frac{\cos(n\theta)}{2\pi(1+n^2)}\\[6pt]
	&= -\frac{\cosh(\pi-\theta)}{2\sinh\pi}
	+\sum_{n=-N}^{N}\frac{\cos(n\theta)}{2\pi(1+n^2)}.
\end{align*}

Hence
\[
\boxed{
	\sum_{a\in\mathcal{P}_N} \operatorname{Res}(F,a)
	= -\frac{\cosh(\pi-\theta)}{2\sinh\pi}
	+\sum_{n=-N}^{N}\frac{\cos(n\theta)}{2\pi(1+n^2)}.
}\]

\bigskip
\noindent\rule{\textwidth}{0.4pt}
\medskip

\clearpage

\bigskip
\noindent\rule{\textwidth}{0.4pt}
\medskip

\clearpage

\[
\frac{\cosh\pi}{2\sinh\pi}
= \sum_{n=-\infty}^{\infty}\frac{1}{1+n^2}.
\]

\[
1 + 2\sum_{n=1}^{\infty}\frac{1}{1+n^2}
= \frac{\cosh\pi}{2\sinh\pi},
\qquad
\sum_{n=1}^{\infty}\frac{1}{1+n^2}
= \frac{1}{2}\Bigl(\frac{\cosh\pi}{2\sinh\pi}-1\Bigr).
\]
```

## CP-IV-0099


- chapter line: 3744
- atlas source solution flag: `unknown`
- linked source-solution candidates: `none`
- embedded solution marker in problem body: `NO`

```tex
Fourier transforms and inverse verification

We use the convention \(\displaystyle \widehat f(\xi)=\int_{-\infty}^{\infty} f(x)\,e^{-i\xi x}\,dx\) and
	\(\displaystyle f(x)=\frac{1}{2\pi}\int_{-\infty}^{\infty}\widehat f(\xi)\,e^{i\xi x}\,d\xi\).

	\subsection*{(a) \(f(x)=e^{-|x|}\) â€” Transform and step-by-step inverse}
	\textit{Transform:}
	\[
	\widehat f(\xi)
	=\int_{0}^{\infty}e^{-(1+i\xi)x}\,dx+\int_{-\infty}^{0}e^{(1-i\xi)x}\,dx
	=\frac{1}{1+i\xi}+\frac{1}{1-i\xi}
	=\boxed{\frac{2}{1+\xi^{2}}}.
	\]

	\textit{Inverse by residues (two cases):}
	\begin{align*}
		f(x)
		&=\frac{1}{2\pi}\int_{\mathbb R}\frac{2\,e^{i\xi x}}{1+\xi^{2}}\,d\xi
		=\frac{1}{2\pi}\int_{\mathbb R}\frac{2\,e^{i\xi x}}{(\xi-i)(\xi+i)}\,d\xi.
		\\[0.25em]
		\textbf{Case }x>0:\quad
		f(x)
		&=\frac{1}{2\pi}\oint_{\Gamma^+}\frac{2\,e^{i\xi x}}{(\xi-i)(\xi+i)}\,d\xi
		&&\text{(close upward; Jordanâ€™s lemma)}\\
		&=\frac{1}{2\pi}(2\pi i)\,\operatorname{Res}_{\xi=i}\!\left(\frac{2\,e^{i\xi x}}{(\xi-i)(\xi+i)}\right)
		=\frac{i\,2\,e^{ix}}{2i( i+i)}=\;e^{-x}.
		\\[0.35em]
		\textbf{Case }x<0:\quad
		f(x)
		&=\frac{1}{2\pi}\oint_{\Gamma^-}\frac{2\,e^{i\xi x}}{(\xi-i)(\xi+i)}\,d\xi
		&&\text{(close downward)}\\
		&=\frac{1}{2\pi}(2\pi i)\,\operatorname{Res}_{\xi=-i}\!\left(\frac{2\,e^{i\xi x}}{(\xi-i)(\xi+i)}\right)
		=\;e^{\,x}.
	\end{align*}
	Therefore \(\boxed{\,f(x)=e^{-|x|}\,}\).

	\subsection*{(b) \(f(x)=e^{-a^{2}x^{2}}\) (\(a>0\)) â€” Transform and step-by-step inverse}
	\textit{Transform:}
	\begin{align*}
		\widehat f(\xi)
		&=\int_{\mathbb R}e^{-a^{2}x^{2}-i\xi x}\,dx
		= e^{-\xi^{2}/(4a^{2})}\int_{\mathbb R}e^{-a^{2}\left(x+i\frac{\xi}{2a^{2}}\right)^{2}}dx\\
		&\phantom{=} \qquad \Rightarrow\qquad
		\boxed{\,\widehat f(\xi)=\frac{\sqrt{\pi}}{a}\,e^{-\xi^{2}/(4a^{2})}\, }.
	\end{align*}
	(Justify by integrating over a large rectangle whose vertical sides are the real line and
	the line shifted up by \(i\,\xi/(2a^{2})\); the horizontal sides vanish by Gaussian decay.)

	\textit{Inverse by a rectangular shift (explicit steps):}
	\begin{align*}
		f(x)
		&=\frac{1}{2\pi}\int_{\mathbb R}\frac{\sqrt{\pi}}{a}\,e^{-\xi^{2}/(4a^{2})}\,e^{i\xi x}\,d\xi\\
		&=\frac{1}{2\pi}\cdot\frac{\sqrt{\pi}}{a}\,
		\int_{\mathbb R} \exp\!\left(-\frac{1}{4a^{2}}(\xi-2ia^{2}x)^{2}\right)\,
		\exp\!\left(-a^{2}x^{2}\right)\,d\xi
		&&\text{(complete the square)}\\
		&=\frac{1}{2\pi}\cdot\frac{\sqrt{\pi}}{a}\,e^{-a^{2}x^{2}}
		\int_{\mathbb R+2ia^{2}x} \exp\!\left(-\frac{u^{2}}{4a^{2}}\right)\,du
		&&\text{(shift contour vertically)}\\
		&=\frac{1}{2\pi}\cdot\frac{\sqrt{\pi}}{a}\,e^{-a^{2}x^{2}}
		\int_{\mathbb R} \exp\!\left(-\frac{u^{2}}{4a^{2}}\right)\,du
		&&\text{(no poles; horizontal sides vanish)}\\
		&=\frac{1}{2\pi}\cdot\frac{\sqrt{\pi}}{a}\,e^{-a^{2}x^{2}}\cdot 2a\sqrt{\pi}
		\;=\;e^{-a^{2}x^{2}}.
	\end{align*}

	\bigskip\hrule\bigskip
```

## CP-IV-0110


- chapter line: 3817
- atlas source solution flag: `unknown`
- linked source-solution candidates: `none`
- embedded solution marker in problem body: `NO`

```tex
Consider the meromorphic function
\[
F(z) = \frac{1}{1+z^2} \frac{\cos[(\pi-\theta)z]}{2\sin(\pi z)}.
\]

The poles occur at $z=\pm i$ and $z=n$, $n\in\mathbb{Z}$.
...

\begin{center}

\end{center}

\textit{Legend.} Red dots = poles at integers, Blue dots = poles at $\pm i$, dashed square = contour $\Gamma^{(N)}$.

---

...

\begin{center}

\end{center}

\textit{Legend.} Blue curve = exact hyperbolic expression, red dashed = Fourier sum with $N=1$, green dashed = Fourier sum with $N=5$.

	To recall the behavior of basic meromorphic functions near poles,
	we show plots of $f(z) = 1/z$ and $f(z) = 1/z^2$ on the real line.
	Both have a pole at $z=0$, with $1/z$ being of order $1$ and
	$1/z^2$ being of order $2$. Clearly, $(1/z)^2 = 1/z^2$.

	\subsection*{Chart: $f(x)=1/x$ on $\mathbb{R}\setminus\{0\}$}
	\begin{center}

		\hspace{1cm}

	\end{center}

	\textit{Legend.} Function $1/x$ has a simple pole at $x=0$. The left and right limits
	blow up to $\mp\infty$.

	---

	\begin{center}

		\hspace{1cm}

	\end{center}

	\textit{Legend.} Function $1/x^2$ has a pole of order 2 at $x=0$.
	It diverges to $+\infty$ on both sides of the pole.
	Clearly, $(1/x)^2 = 1/x^2$.

	\subsection*{Example 1: $f(z) = \tfrac{1}{z}$}

	\textbf{Description.}
	For $z = re^{i\theta}$ we have
	\[
	\frac{1}{z} = \frac{1}{r} e^{-i\theta}.
	\]
	Thus $f(z)$ inverts the magnitude ($r \mapsto 1/r$) and reflects the angle
	($\theta \mapsto -\theta$). The unit circle maps to itself with reversed orientation.
	Lines through the origin are mapped to lines through the origin, reflected in the real axis.

	\begin{center}

		\hspace{1cm}

	\end{center}

	\textit{Legend.} Left: domain ($z$-plane). Right: image ($w=1/z$).
	The unit circle is preserved, rays reflect across the real axis.

	---

\subsection*{Example: $f(z)=\tfrac{1}{z}$}

\textbf{Description.}
For $z = re^{i\theta}$ we have
\[
\frac{1}{z} = \frac{1}{r} e^{-i\theta}.
\]
Thus the mapping $f(z)=1/z$ has the following geometric effects:

	\par\noindent\textbullet\quad \textbf{Inversion of radii:} $r \mapsto 1/r$.
	\par\noindent\textbullet\quad \textbf{Reflection of angles:} $\theta \mapsto -\theta$.
	\par\noindent\textbullet\quad The unit circle $|z|=1$ is invariant, but orientation is reversed.
	\par\noindent\textbullet\quad The interior of the unit disk $|z|<1$ maps to the exterior $|w|>1$, and vice versa.
	\par\noindent\textbullet\quad Rays through the origin map to reflected rays across the real axis.
	\par\noindent\textbullet\quad More generally, lines not through the origin map to circles, and circles not through the origin map to circles (inversion geometry).

\begin{center}

	\hspace{1.5cm}

\end{center}

\textit{Legend.}
Blue: unit circle (invariant).
Red: ray at $\theta=\pi/4$ mapping to $\theta=-\pi/4$.
Green dashed: vertical line $\Re z=1$ maps to a circle through the origin.

\subsection*{Example: $f(z)=\tfrac{1}{z+1}$}

\textbf{Description.}
This mapping is a shifted inversion. Let $w=z+1$. Then
\[
f(z) = \frac{1}{z+1} = \frac{1}{w}.
\]
Thus the inversion is centered at $z=-1$ instead of $z=0$.
The function has a simple pole at $z=-1$.
As $|z|\to\infty$, $f(z)\to 0$.
Key geometric effects:

	\par\noindent\textbullet\quad Pole at $z=-1$ corresponds to $w=0$ under translation.
	\par\noindent\textbullet\quad The unit circle $|z|=1$ no longer maps to itself, but to another circle in the $w$-plane.
	\par\noindent\textbullet\quad Lines and circles not passing through $z=-1$ map to circles.
	\par\noindent\textbullet\quad Rays and bands relative to $z=-1$ are inverted accordingly.

\begin{center}

	\hspace{1.5cm}

\end{center}

\textit{Legend.}
Left: domain ($z$-plane) with unit circle (blue), pole at $z=-1$ (red), and imaginary axis (green dashed).
Right: schematic image under $f(z)=1/(z+1)$: unit circle maps to another circle, imaginary axis maps to a circle through the origin, and $z=-1$ maps to infinity.

\subsection*{Example: $f(z)=\tfrac{1}{z^2}$}

\textbf{Description.}
For $z = re^{i\theta}$ we have
\[
f(z) = \frac{1}{z^2} = \frac{1}{r^2} e^{-2i\theta}.
\]
Thus the mapping $f(z)=1/z^2$ has the following geometric effects:

	\par\noindent\textbullet\quad \textbf{Inversion of radii (squared):} $r \mapsto 1/r^2$.
	\par\noindent\textbullet\quad \textbf{Angle doubling and reflection:} $\theta \mapsto -2\theta$.
	\par\noindent\textbullet\quad The unit circle $|z|=1$ is invariant (maps to itself).
	\par\noindent\textbullet\quad The interior of the unit disk $|z|<1$ maps to the exterior $|w|>1$, and vice versa.
	\par\noindent\textbullet\quad Rays at angle $\theta$ map to rays at angle $-2\theta$.
	\par\noindent\textbullet\quad There is a pole of order 2 at $z=0$.

\begin{center}

	\hspace{1.5cm}

\end{center}

\textit{Legend.}
Blue: unit circle (invariant).
Red: sample rays mapped under $\theta \mapsto -2\theta$.
Black dot: pole of order 2 at $z=0$.
```

## CP-IV-0137


- chapter line: 4064
- atlas source solution flag: `unknown`
- linked source-solution candidates: `none`
- embedded solution marker in problem body: `NO`

```tex
(cotangent trick and square contour).

Let $N\in\mathbb N$ and let $\gamma_N$ be the square contour with vertices
$(\pm1\pm i)\bigl(N+\tfrac12\bigr)$, oriented positively.

	\par\noindent\textbullet\quad Show that there exists a constant $C>0$, independent of $N$, such that
	\[
	|\cot(\pi z)|<C \qquad \text{for all } z\in\gamma_N .
	\]
	\par\noindent\textbullet\quad By integrating $\displaystyle \frac{\pi\cot(\pi z)}{z^{2}+1}$ around $\gamma_N$,
	prove that
	\[
	\sum_{n=0}^{\infty}\frac{1}{n^{2}+1}\;=\;\frac{1+\pi\coth\pi}{2}\, .
	\]
	\par\noindent\textbullet\quad Evaluate the alternating series
	\[
	\sum_{n=0}^{\infty}\frac{(-1)^{n}}{n^{2}+1}\, .
	\]

With $z=x+iy$ one has
\[
|\sin(\pi z)|^{2}=\sin^{2}(\pi x)+\sinh^{2}(\pi y),\qquad
|\cos(\pi z)|^{2}=\cos^{2}(\pi x)+\sinh^{2}(\pi y).
\]
On the \emph{vertical} sides $x=\pm(N+\tfrac12)$ we get
$\sin(\pi x)=\pm1$, $\cos(\pi x)=0$, hence
\[
\cot(\pi z)=-i\,\tanh(\pi y),\qquad |\cot(\pi z)|\le 1.
\]
On the \emph{horizontal} sides $y=\pm(N+\tfrac12)$,
\[
|\cot(\pi z)|^{2}
=\frac{\cos^{2}(\pi x)+\sinh^{2}(\pi y)}{\sin^{2}(\pi x)+\sinh^{2}(\pi y)}
\le 1+\frac{1}{\sinh^{2}(\pi|y|)}
\le 1+\frac{1}{\sinh^{2}(\pi/2)}.
\]
Thus there is a constant
$C=\max\!\big\{1,\sqrt{1+\sinh^{-2}(\pi/2)}\big\}$, independent of $N$, such that
$|\cot \pi z|<C$ on $\gamma_N$.

\medskip
\paragraph{(ii) $\displaystyle \sum_{n=0}^{\infty}\frac{1}{n^{2}+1}$.}
Let $F(z)=\dfrac{\pi\cot(\pi z)}{z^{2}+1}$. Then on $\gamma_N$,
$|F(z)|\lesssim C/|z|^{2}$, so $\int_{\gamma_N}F(z)\,dz\to0$ as $N\to\infty$.
Residues:
\[
\operatorname{Res}(F;n)=\frac{1}{n^{2}+1}\quad(n\in\mathbb Z),
\qquad
\operatorname{Res}(F;i)=\operatorname{Res}(F;-i)=\frac{\pi\cot(\pi i)}{2i}.
\]
Since $\cot(\pi i)=-i\,\coth\pi$, we have
$\operatorname{Res}(F;i)+\operatorname{Res}(F;-i)=-\pi\coth\pi$.
Hence, letting $N\to\infty$,
\[
0=\int_{\gamma_N}F
=2\pi i\!\left(\sum_{n\in\mathbb Z}\frac{1}{n^{2}+1}-\pi\coth\pi\right)
\ \Rightarrow\
\sum_{n\in\mathbb Z}\frac{1}{n^{2}+1}=\pi\coth\pi.
\]
By symmetry,
\[
\boxed{\ \sum_{n=0}^{\infty}\frac{1}{n^{2}+1}=\frac{1+\pi\coth\pi}{2}\ }.
\]

\medskip
\paragraph{(iii) $\displaystyle \sum_{n=0}^{\infty}\frac{(-1)^{n}}{n^{2}+1}$.}
Set $G(z)=\dfrac{\pi\csc(\pi z)}{z^{2}+1}$.
Again $\int_{\gamma_N}G\to0$ and
\[
\operatorname{Res}(G;n)=\frac{(-1)^{n}}{n^{2}+1}\quad(n\in\mathbb Z),
\qquad
\csc(\pi i)=\frac{1}{\sin(\pi i)}=\frac{1}{i\sinh\pi}=-i\,\mathrm{csch}\,\pi.
\]
Therefore
\[
\operatorname{Res}(G;i)+\operatorname{Res}(G;-i)
=\frac{\pi\csc(\pi i)}{2i}+\frac{\pi\csc(-\pi i)}{-2i}
=-\pi\,\mathrm{csch}\,\pi.
\]
Thus
\[
\sum_{n\in\mathbb Z}\frac{(-1)^{n}}{n^{2}+1}
=\pi\,\mathrm{csch}\,\pi,
\qquad
\boxed{\ \sum_{n=0}^{\infty}\frac{(-1)^{n}}{n^{2}+1}
	=\frac{1+\pi\,\mathrm{csch}\,\pi}{2}\ }.
\]


\emph{Core identities.} For $z=x+iy$,
\[
\sin(\pi z)=\sin(\pi x)\cosh(\pi y)+i\cos(\pi x)\sinh(\pi y),\quad
\cos(\pi z)=\cos(\pi x)\cosh(\pi y)-i\sin(\pi x)\sinh(\pi y),
\]
hence
\[
|\sin(\pi z)|^2=\sin^2(\pi x)+\sinh^2(\pi y),\qquad
|\cos(\pi z)|^2=\cos^2(\pi x)+\sinh^2(\pi y).
\]
Also
\[
\cot z=i\,\coth(iz)=i\,\frac{e^{2iz}+1}{e^{2iz}-1}.
\]

\emph{Poles, residues, partial fractions.}
$\cot$ has simple poles at $k\pi$ with residue $1$; $\pi\cot(\pi z)$ has simple poles at integers with residue $1$.
\[
\pi\cot(\pi z)=\sum_{n\in\mathbb Z}\frac{1}{z-n}.
\]

\medskip
\paragraph{Images of horizontal lines $y=\text{const}$.}
Write
\[
\cot(x+iy)=\frac{\sin 2x - i\,\sinh 2y}{\cosh 2y - \cos 2x}=u(x)+iv(x).
\]
Eliminating $x$ yields the circle
\[
\boxed{\ u^2+\big(v+\coth 2y\big)^2=\csch^2 2y\ },
\]
i.e.\ for fixed $y$ the image is a circle centered at $-i\,\coth 2y$ with radius $\csch 2y$ (orthogonal to the imaginary axis). As $y\to\pm\infty$ this circle collapses to the point $\mp i$; as $y\to0$ it expands and approaches the real axis.

\medskip
\paragraph{Images of vertical lines $x=\text{const}$.}
For fixed $x$, as $y$ varies,
\[
\cot(x+iy)\to -\,i\ (y\to+\infty),\qquad \cot(x+iy)\to +\,i\ (y\to-\infty),
\]
and $\cot(x+0i)=\cot x\in\mathbb R$. Thus the image is a circular arc joining $\pm i$ and crossing the real axis at $\cot x$ (orthogonal to the family in the previous paragraph).

\medskip

Because $\cot z=\tan(\tfrac{\pi}{2}-z)$, the vertical strip $\{0<\Re z<\pi\}$ is mapped bijectively onto $\mathbb C$, and periodicity $\cot(z+\pi)=\cot z$ tiles the plane by such strips.
Via $e^{2iz}=e^{-2y}e^{2ix}$ a horizontal strip $y\in(y_1,y_2)$ maps to an annulus; the MĂ¶bius map $w\mapsto i\frac{w+1}{w-1}$ then sends annuli to circular bands bounded by the circles $u^2+(v+\coth 2y)^2=\csch^2 2y$.

\medskip

On the square with vertices $(\pm1\pm i)(N+\tfrac12)$,
\[
|\cot(\pi z)|\le 1 \ \text{on vertical edges},\qquad
|\cot(\pi z)|^2\le 1+\frac{1}{\sinh^2(\pi/2)} \ \text{on horizontal edges},
\]
so there is a constant $C$ independent of $N$ with $|\cot(\pi z)|<C$ on the boundary.

\medskip
\emph{Asymptotics and symmetries.}
$\cot(-z)=-\cot z$, $\overline{\cot(\bar z)}=\cot z$, and $\cot(x+iy)\to\mp i$ as $y\to\pm\infty$.
These give quick qualitative sketches of level sets and images.

Let $z=x+iy$ and set
\[
\cot z=\frac{\sin 2x-i\,\sinh 2y}{\cosh 2y-\cos 2x}=u+iv,\qquad
D:=\cosh 2y-\cos 2x,\ S:=\sinh 2y,\ C:=\cosh 2y.
\]
Then
\[
u=\frac{\sin 2x}{D},\qquad v=-\frac{S}{D}\ \Longrightarrow\ D=-\frac{S}{v}.
\]
Hence
\[
\sin 2x=uD=-\frac{uS}{v},\qquad \cos 2x = C - D = C+\frac{S}{v}.
\]
Now
\[
u^{2}+\Bigl(v+\frac{C}{S}\Bigr)^{2}
=\frac{1}{D^{2}}\!\left[\sin^{2}2x+\frac{(1-C\cos 2x)^{2}}{S^{2}}\right].
\]
Using $D=C-\cos 2x$ and $\cosh^{2}2y-\sinh^{2}2y=1$ we get
\[
S^{2}\sin^{2}2x+(1-C\cos 2x)^{2}=(C-\cos 2x)^{2}=D^{2}.
\]
Therefore
\[
\boxed{\,u^{2}+\bigl(v+\coth 2y\bigr)^{2}=\csch^{2}2y\,},
\]
i.e.\ for fixed $y$ the image is a circle centered at $-i\,\coth(2y)$ with radius $\csch(2y)$.

\[
\csch x=\frac{1}{\sinh x}=\frac{2}{e^{x}-e^{-x}},\qquad
\sech x=\frac{1}{\cosh x},\quad
\coth x=\frac{\cosh x}{\sinh x}.
\]
Parity and derivatives:
\[
\csch(-x)=-\csch x,\qquad
\frac{d}{dx}\csch x=-\csch x\,\coth x,\qquad
\frac{d}{dx}\coth x=-\csch^{2}x.
\]
Identity and asymptotics:
\[
\coth^{2}x-\csch^{2}x=1,\qquad
\csch x\sim 2e^{-|x|}\quad (|x|\to\infty).
\]

\emph{Core identities.} For $z=x+iy$,
\[
\sin z=\sin x\,\cosh y+i\,\cos x\,\sinh y,\qquad
|\sin z|^{2}=\sin^{2}x+\sinh^{2}y.
\]
Symmetries: $\overline{\sin\bar z}=\sin z$, $\sin(-z)=-\sin z$, $\sin(z+2\pi)=\sin z$.
Zeros are simple at $z=n\pi$ ($n\in\mathbb Z$) since $\sin'(n\pi)=\cos(n\pi)\neq0$.

\medskip
\paragraph{Images of horizontal lines $y=\text{const}$.}
Let $w=\sin z=u+iv$. For fixed $y$,
\[
u=\sin x\,\cosh y,\qquad v=\cos x\,\sinh y.
\]
Eliminating $x$ gives the ellipse
\[
\boxed{\ \Big(\tfrac{u}{\cosh y}\Big)^{2}+\Big(\tfrac{v}{\sinh y}\Big)^{2}=1\ }.
\]
Thus the image is an ellipse centered at $0$ with semiaxes $\cosh y$ (real axis) and $\sinh y$ (imaginary axis).
Since $\cosh^{2}y-\sinh^{2}y=1$, the foci lie at $\pm1$, and
\[
|w-1|+|w+1|=2\cosh y.
\]

\medskip
\paragraph{Images of vertical lines $x=\text{const}$.}
For fixed $x$,
\[
u=\sin x\,\cosh y,\qquad v=\cos x\,\sinh y
\]
and eliminating $y$ using $\cosh^{2}y-\sinh^{2}y=1$ yields
\[
\boxed{\ \Big(\tfrac{u}{\sin x}\Big)^{2}-\Big(\tfrac{v}{\cos x}\Big)^{2}=1\ } \quad
(\sin x\,\cos x\ne0).
\]
Hence the image is a hyperbola with the same foci $\pm1$.
Degenerate cases:
$x=n\pi$ gives $u=0$ (imaginary axis) and $x=\frac{\pi}{2}+n\pi$ gives $v=0$ (real axis).

\medskip

One may take the fundamental strip $S=\{\,0<\Re z<\pi\,\}$. On $x=0$ or $x=\pi$
the image is purely imaginary; in the interior the images of horizontal/vertical lines
form the orthogonal confocal families of ellipses and hyperbolas with foci $\pm1$.
(Branches of $\arcsin$ use the slits $(-\infty,-1]\cup[1,\infty)$.)

\emph{Core identities.} For $z=x+iy$,
\[
\cos z=\cos x\,\cosh y - i\,\sin x\,\sinh y,\qquad
|\cos z|^{2}=\cos^{2}x+\sinh^{2}y.
\]
Symmetries: $\overline{\cos\bar z}=\cos z$, $\cos(-z)=\cos z$, $\cos(z+2\pi)=\cos z$.
Zeros are simple at $z=\tfrac{\pi}{2}+n\pi$ since $\cos'(z)=-\sin z$.

\medskip
\paragraph{Images of horizontal lines $y=\text{const}$.}
Let $w=\cos z=u+iv$. For fixed $y$,
\[
u=\cos x\,\cosh y,\qquad v=-\,\sin x\,\sinh y.
\]
Eliminating $x$ gives the ellipse
\[
\boxed{\ \Big(\tfrac{u}{\cosh y}\Big)^{2}+\Big(\tfrac{v}{\sinh y}\Big)^{2}=1\ }.
\]
Thus the image is an ellipse centered at $0$ with semiaxes $\cosh y$ (real axis) and $\sinh y$ (imaginary axis); since $\cosh^{2}y-\sinh^{2}y=1$, the foci are $\pm1$ and
\[
|w-1|+|w+1|=2\cosh y.
\]

\medskip
\paragraph{Images of vertical lines $x=\text{const}$.}
For fixed $x$,
\[
u=\cos x\,\cosh y,\qquad v=-\,\sin x\,\sinh y.
\]
Eliminating $y$ using $\cosh^{2}y-\sinh^{2}y=1$ yields
\[
\boxed{\ \Big(\tfrac{u}{\cos x}\Big)^{2}-\Big(\tfrac{v}{\sin x}\Big)^{2}=1\ } \quad
(\sin x\,\cos x\ne0),
\]
a hyperbola with the same foci $\pm1$.
Degenerate cases:
$x=n\pi$ gives $v=0$ (real axis) and $x=\tfrac{\pi}{2}+n\pi$ gives $u=0$ (imaginary axis).

\medskip

A fundamental strip is $S=\{\,0<\Re z<\pi\,\}$. On $x=0$ or $x=\pi$ the image is real; inside $S$ the images of horizontal/vertical lines form orthogonal confocal ellipses and hyperbolas with foci $\pm1$.
(Branches of $\arccos$ use the slits $(-\infty,-1]\cup[1,\infty)$.)

\emph{Core identities.} For $z=x+iy$,
\[
\tan z=\frac{\sin z}{\cos z}
=\frac{\sin 2x + i\,\sinh 2y}{\cos 2x+\cosh 2y}.
\]
Thus, writing $w=\tan z=u+iv$,
\[
u=\frac{\sin 2x}{\cos 2x+\cosh 2y},\qquad
v=\frac{\sinh 2y}{\cos 2x+\cosh 2y}.
\]

\emph{Zeros, poles, residues.}
$\tan z$ has simple zeros at $z=n\pi$ and simple poles at $z=\tfrac{\pi}{2}+n\pi$ ($n\in\mathbb Z$).
At each pole, $\mathrm{Res}(\tan;z_0)=1$. The partial fraction expansion is
\[
\pi\,\tan(\pi z)=\sum_{n\in\mathbb Z}\frac{1}{\,z-(n+\tfrac12)\,}.
\]
Symmetries: $\tan(-z)=-\tan z$, $\overline{\tan\bar z}=\tan z$, and $\tan(z+\pi)=\tan z$.
As $|y|\to\infty$, $\tan(x+iy)\to i\,\mathrm{sgn}(y)$.

\medskip
\paragraph{Images of horizontal lines $y=\text{const}$.}
Fix $y$ and set $C=\cosh(2y)$, $S=\sinh(2y)$, $D=\cos(2x)+C$. Then
\[
u=\frac{\sin 2x}{D},\qquad v=\frac{S}{D}.
\]
Eliminating $x$ (using $D=S/v$) yields the circle
\[
\boxed{\ u^{2}+\Bigl(v-\frac{\cosh(2y)}{\sinh(2y)}\Bigr)^{2}=\frac{1}{\sinh^{2}(2y)}\ }.
\]
Hence the image is a circle centered at $-i\,\dfrac{\cosh(2y)}{\sinh(2y)}$ on the imaginary axis (note the sign in $u+iv$) with radius $\dfrac{1}{|\sinh(2y)|}$.
As $y\to\pm\infty$ the circle shrinks to $\pm i$; as $y\to0$ it expands toward the real axis.

\medskip
\paragraph{Images of vertical lines $x=\text{const}$.}
For fixed $x$, as $y$ varies,
\[
\tan(x+iy)\to i \ (y\to+\infty),\qquad \tan(x+iy)\to -i \ (y\to-\infty),
\]
and $\tan(x+0i)=\tan x\in\mathbb R$. Thus the image is a circular arc joining $\pm i$ and crossing the real axis at $\tan x$ (orthogonal to the family above).

\medskip

The vertical strip $S=\{\, -\tfrac{\pi}{2}<\Re z<\tfrac{\pi}{2}\,\}$ is mapped bijectively onto $\mathbb C$ by $\tan$; its boundary lines map to $\infty$ (simple poles). Periodicity $\tan(z+\pi)=\tan z$ tiles the plane by translates of $S$.
```

## CP-IV-0004


- chapter line: 4440
- atlas source solution flag: `unknown`
- linked source-solution candidates: `none`
- embedded solution marker in problem body: `NO`

```tex
\par\noindent\textbullet\quad \textbf{(c)}\;
	Consider instead the branch
	\[
	f(z) \;=\; (r_{1}r_{2})^{1/2} \, e^{\,i(\theta_{1}+\theta_{2})/2},
	\qquad -\tfrac{3\pi}{2}<\theta_{1}\le \tfrac{\pi}{2},\quad
	-\tfrac{\pi}{2}<\theta_{2}\le \tfrac{3\pi}{2}.
	\]
	State the values of \((\theta_{1}+\theta_{2})/2\) on either side of the imaginary axis,
	and hence compute \(f(\pm0+iy)\) in terms of \(y\) for \(y\in\mathbb{R}\).
	Deduce that the branch cut is along the imaginary axis
	from \(z=-i\infty\) to \(z=-i\) and from \(z=i\) to \(z=i\infty\).
	Compute \(f(x)\) in terms of \(x\) for \(x\in\mathbb{R}\).
	Show that
	\[
	f(z)\sim
	\begin{cases}
		z,  & \text{as } |z|\to\infty \text{ with } \Re(z)>0,\\[2pt]
		-z,  & \text{as } |z|\to\infty \text{ with } \Re(z)<0.
	\end{cases}
	\]
	Sketch the images of the half-planes \(\Re(z)>0\) and \(\Re(z)<0\) under the map \(\zeta=f(z)\).

	\bigskip\hrule\bigskip
```

## CP-IV-0007


- chapter line: 4469
- atlas source solution flag: `unknown`
- linked source-solution candidates: `none`
- embedded solution marker in problem body: `NO`

```tex
Temperature in a right halfâ€“plane with a removed disk

The domain $D$ consists of the right-hand half plane $x>0$ with the circle $|z-a|=b$, $0<b<a$, and its interior removed.
	Find the temperature $u(x,y)$ in steady heat flow if $u=0$ on the $y$ axis, $u=1$ on $|z-a|=b$, and $u\to0$ at infinity.

	\medskip
	\noindent\textit{Hint:} Show that the mapping $\displaystyle \zeta=\frac{z-\alpha}{z+\alpha}$, with $\alpha$ real and positive,
	takes $D$ onto an annular region with the imaginary axis mapping to $|\zeta|=1$ and show that, if $\alpha^{2}=a^{2}-b^{2}$, then the image of $D$ is a concentric circular annulus.

	\bigskip\hrule\bigskip

	Consider the real-parameter MĂ¶bius map
	\[
	\zeta=\zeta(z)=\frac{z-\alpha}{z+\alpha}, \qquad \alpha>0.
	\]

	For $z=iy$ we have
	\[
	\left|\frac{iy-\alpha}{iy+\alpha}\right|=1 \quad\text{(numerator and denominator are conjugates),}
	\]
	so the $y$â€“axis maps to the unit circle $|\zeta|=1$.

	\paragraph{Image of the circle $\boldsymbol{|z-a|=b}$.}
	Write $z=a+be^{i\theta}$ and compute
	\[
	|\zeta|^{2}
	=\frac{|a-\alpha+be^{i\theta}|^{2}}{|a+\alpha+be^{i\theta}|^{2}}
	=\frac{A+B\cos\theta}{C+D\cos\theta},
	\]
	where
	\[
	A=(a-\alpha)^{2}+b^{2}, \qquad B=2b(a-\alpha), \qquad
	C=(a+\alpha)^{2}+b^{2}, \qquad D=2b(a+\alpha).
	\]
	For $|\zeta|$ to be constant on the circle (i.e. the image is a circle \emph{centered at the origin}),
	the $\cos\theta$â€“dependence must drop out:
	\[
	\frac{A+B\cos\theta}{\,C+D\cos\theta\,}\equiv\frac{A}{C}
	\quad\Longleftrightarrow\quad AD=BC.
	\]
	We now verify that
	\[
	AD-BC
	=2b\Big[(a+\alpha)((a-\alpha)^{2}+b^{2})-(a-\alpha)((a+\alpha)^{2}+b^{2})\Big]
	=4b\alpha\,(\alpha^{2}+b^{2}-a^{2}).
	\]
	Thus $AD=BC$ is equivalent to
	\[
	\boxed{\ \alpha^{2}=a^{2}-b^{2}\ }.
	\]
	With this choice (note $a>b>0\Rightarrow \alpha>0$), the ratio becomes \emph{constant}:
	\[
	|\zeta|^{2}=\frac{A}{C}
	=\frac{(a-\alpha)^{2}+b^{2}}{(a+\alpha)^{2}+b^{2}}
	=\frac{2a(a-\alpha)}{2a(a+\alpha)}
	=\frac{a-\alpha}{a+\alpha}.
	\]
	Hence the circle $|z-a|=b$ maps to the circle $|\zeta|=\rho$ with
	\[
	\boxed{\ \rho=\sqrt{\frac{a-\alpha}{a+\alpha}}\in(0,1). \ }
	\]

	Therefore, for $\alpha=\sqrt{a^{2}-b^{2}}$, the map $z\mapsto\zeta$ sends the domain $D$
	(right halfâ€“plane with the closed disk $\{|z-a|\le b\}$ removed) onto the concentric circular \emph{annulus}
	\[
	\mathcal A=\{\ \rho<|\zeta|<1\ \}.
	\]
	The boundary pieces correspond as follows:
	\[
	\{x=0\}\ \longmapsto\ |\zeta|=1,
	\qquad
	\{|z-a|=b\}\ \longmapsto\ |\zeta|=\rho.
	\]

	\bigskip\hrule\bigskip

	Let $U(\zeta)$ denote the temperature in the $\zeta$â€“plane. Harmonicity is preserved by conformal maps, so
	$U$ is harmonic on $\mathcal A$ and the boundary data become
	\[
	U=0 \ \ \text{on}\ \ |\zeta|=1,
	\qquad
	U=1 \ \ \text{on}\ \ |\zeta|=\rho.
	\]
	By rotational symmetry, $U$ depends only on $r=|\zeta|$. The general radial harmonic function on an annulus is
	$A\log r + B$. Imposing the boundary values gives
	\[
	U(r)=\frac{\log(1/r)}{\log(1/\rho)}
	=\frac{-\log r}{-\log \rho}
	=\frac{\log r}{\log \rho}
	\quad\text{for}\quad \rho<r<1.
	\]
	(Any of the three displayed forms is correct; we will use the first one momentarily.)

	\bigskip\hrule\bigskip

	The physical temperature is $u(z)=U(\zeta(z))$ with $r=|\zeta(z)|=\left|\frac{z-\alpha}{z+\alpha}\right|$.
	Hence
	\[
	u(z)
	=U\!\left(\left|\frac{z-\alpha}{z+\alpha}\right|\right)
	=\frac{\displaystyle \log\!\left(\frac{1}{\left|\frac{z-\alpha}{z+\alpha}\right|}\right)}
	{\displaystyle \log\!\left(\frac{1}{\rho}\right)}
	=\frac{\displaystyle \log\left|\frac{z+\alpha}{z-\alpha}\right|}
	{\displaystyle \log\!\left(\frac{1}{\rho}\right)}.
	\]
	Since $\displaystyle \rho=\sqrt{\frac{a-\alpha}{a+\alpha}}$ we have
	\[
	\log\!\left(\frac{1}{\rho}\right)
	=\frac{1}{2}\,\log\!\left(\frac{a+\alpha}{a-\alpha}\right).
	\]
	Therefore a convenient explicit form is
	\[
	\boxed{\quad
		u(z)
		=\frac{2\,\log\!\left|\dfrac{z+\alpha}{z-\alpha}\right|}
		{\log\!\left(\dfrac{a+\alpha}{a-\alpha}\right)},
		\qquad
		\alpha=\sqrt{a^{2}-b^{2}}.
		\quad}
	\]

	\bigskip

		\par\noindent\textbullet\quad \textbf{On the $y$--axis $x=0$:} for $z=iy$ we have $\left|\dfrac{z-\alpha}{z+\alpha}\right|=1$,
		so the numerator $\log\left|\dfrac{z+\alpha}{z-\alpha}\right|=0$ and hence $u=0$.
		\par\noindent\textbullet\quad \textbf{On the circle $|z-a|=b$:} by construction $|\zeta|=\rho$, i.e.
		$\left|\dfrac{z-\alpha}{z+\alpha}\right|=\rho$, so
		$\log\left|\dfrac{z+\alpha}{z-\alpha}\right|=\log\!\left(\dfrac{1}{\rho}\right)$
		and the fraction evaluates to $u=1$.
		\par\noindent\textbullet\quad \textbf{At infinity:} as $|z|\to\infty$, $\left|\dfrac{z+\alpha}{z-\alpha}\right|\to 1$,
		so the numerator $\to 0$ and $u(z)\to 0$.

	\bigskip\hrule\bigskip

	With $\alpha=\sqrt{a^{2}-b^{2}}$ and $\displaystyle \rho=\sqrt{\frac{a-\alpha}{a+\alpha}}$,
	the MĂ¶bius map $\displaystyle \zeta=\frac{z-\alpha}{z+\alpha}$ carries
	$D$ onto the annulus $\{\rho<|\zeta|<1\}$.
	The unique harmonic function with $U=1$ on $|\zeta|=\rho$ and $U=0$ on $|\zeta|=1$
	is $U(r)=\log(1/r)/\log(1/\rho)$, and hence
	\[
	u(z)=\frac{2\,\log\!\left|\dfrac{z+\alpha}{z-\alpha}\right|}
	{\log\!\left(\dfrac{a+\alpha}{a-\alpha}\right)}.
	\]
	This $u$ satisfies all the prescribed boundary conditions and $u(z)\to 0$ as $|z|\to\infty$.

\textbf{Background:} entire, odd; period $2\pi i$. \quad
\textbf{Zeros:} $z=i\pi k$; \textbf{poles:} none.\\
\textbf{Decomposition: } $w=u+iv=\sinh x\cos y + i\,\cosh x\sin y$.\\
\textbf{Vertical lines } $x=\text{const}$: $\left(\frac{u}{\sinh x}\right)^2+\left(\frac{v}{\cosh x}\right)^2=1$ (ellipses, foci $\pm i$).\\
\textbf{Horizontal lines } $y=\text{const}$: $\left(\frac{u}{\cos y}\right)^2-\left(\frac{v}{\sin y}\right)^2=-1$ (hyperbolas, foci $\pm i$).\\
\textbf{Strip mapping:}
\[
\boxed{\,\sinh:\ \{|\Im z|<\tfrac{\pi}{2}\}\ \xrightarrow{\ 1\text{--}1\ }\ \mathbb C\setminus i\big((-\infty,-1]\cup[1,\infty)\big)\,}
\]
Boundaries $y=\pm\frac{\pi}{2}$ map to imaginary rays $\pm i[1,\infty)$.

\bigskip\hrule\bigskip

\textbf{Background:} entire, even; period $2\pi i$. \quad
\textbf{Zeros:} $z=i\pi(k+\frac12)$; \textbf{poles:} none.\\
\textbf{Decomposition: } $w=u+iv=\cosh x\cos y + i\,\sinh x\sin y$.\\
\textbf{Vertical lines } $x=\text{const}$: $\left(\frac{u}{\cosh x}\right)^2+\left(\frac{v}{\sinh x}\right)^2=1$ (ellipses, foci $\pm1$).\\
\textbf{Horizontal lines } $y=\text{const}$: $\left(\frac{u}{\cos y}\right)^2-\left(\frac{v}{\sin y}\right)^2=1$ (hyperbolas, foci $\pm1$).\\
\textbf{Strip mapping:}
\[
\boxed{\,\cosh:\ \{|\Im z|<\pi\}\ \xrightarrow{\ 2\text{--}1\ }\ \mathbb C\setminus\big((-\infty,-1]\cup[1,\infty)\big)\,}
\]
On the half-strip $0<|\Im z|<\pi$, the map is 1--1 onto the slit plane.

\bigskip\hrule\bigskip

\textbf{Background:} meromorphic, odd; period $i\pi$. \quad
\textbf{Zeros:} $z=i\pi k$; \textbf{poles:} $z=i\pi(k+\tfrac12)$.\\
\textbf{Strip $\to$ disk:}
\[
\boxed{\,\tanh:\ \{|\Im z|<\tfrac{\pi}{2}\}\ \xrightarrow{\ 1\text{--}1\ }\ \mathbb D\,}
\]
Real line maps to $(-1,1)$; as $|\Im z|\to\pi/2$, $|\tanh z|\to1$.

\bigskip\hrule\bigskip

\textbf{Background:} meromorphic, odd; period $i\pi$. \quad
\textbf{Zeros:} $z=i\pi(k+\tfrac12)$; \textbf{poles:} $z=i\pi k$.\\
\textbf{Strip $\to$ exterior disk:}
\[
\boxed{\,\coth:\ \{|\Im z|<\tfrac{\pi}{2}\}\setminus\{0\}\ \xrightarrow{\ 1\text{--}1\ }\ \{\,|w|>1\,\}\,}
\]
Real line maps to $(-\infty,-1)\cup(1,\infty)$; $|\Im z|\to\pi/2$ gives $|w|\to1^+$.

Throughout, write $z=x+iy$, $x,y\in\mathbb R$, and $w=u+iv$ for the image.
Recall the basic identities
\[
\cosh z=\frac{e^{z}+e^{-z}}{2},\qquad
\sinh z=\frac{e^{z}-e^{-z}}{2},\qquad
\tanh z=\frac{\sinh z}{\cosh z},\qquad
\coth z=\frac{\cosh z}{\sinh z}.
\]
We use the principal branch of the logarithm $\log$ on $\mathbb C\setminus(-\infty,0]$, and principal square roots $\sqrt{\cdot}$ with branch cut on $(-\infty,0]$ unless stated otherwise.

\bigskip\hrule\bigskip

 \mbox{}\\[2pt]
$\sinh$ is an \emph{entire}, \emph{odd} function, with imaginary-periodicity:
\[
\sinh(-z)=-\sinh z,\qquad \sinh(z+2\pi i)=\sinh z.
\]
Zeros occur at $z_k=i\pi k$ for $k\in\mathbb Z$ (all simple). No poles.

\medskip

 \mbox{}\\[2pt]
With $z=x+iy$,
\[
\sinh z=\sinh x\cos y\ +\ i\,\cosh x\sin y \quad\Rightarrow\quad
u=\sinh x\cos y,\ \ v=\cosh x\sin y.
\]
From this, one obtains orthogonal families of confocal conics:
\begin{align*}
	x=\text{const}&:\quad \left(\frac{u}{\sinh x}\right)^{2}+\left(\frac{v}{\cosh x}\right)^{2}=1
	&&\text{(ellipses, foci at $\pm i$)},\\[2pt]
	y=\text{const}&:\quad \left(\frac{u}{\cos y}\right)^{2}-\left(\frac{v}{\sin y}\right)^{2}=-1
	&&\text{(hyperbolas, foci at $\pm i$)}.
\end{align*}
Real and imaginary axes map as:
\[
y=0:\ w=\sinh x\in\mathbb R\ \text{(onto $\mathbb R$)},\qquad
x=0:\ w=i\sin y\ \text{(onto the segment $i[-1,1]$)}.
\]

\medskip

 \mbox{}\\[2pt]
$\sinh'(z)=\cosh z$, and $\cosh z\neq 0$ on the strip $|\Im z|<\tfrac{\pi}{2}$; hence $\sinh$ is conformal there.

\medskip

 \mbox{}\\[2pt]
\[
\boxed{\
	\sinh:\ \{\,|\Im z|<\tfrac{\pi}{2}\,\}\ \xrightarrow[\ \text{biholomorphism}\ ]{}\
	\mathbb C\setminus i\big((-\infty,-1]\cup[1,\infty)\big)\ .
}\]
\emph{Explanation.} The boundary lines $y=\pm\frac{\pi}{2}$ map to the imaginary rays $\pm i[1,\infty)$
(via $v=\cosh x\,\sin y$ with $\sin(\pm\pi/2)=\pm1$ and $u=\sinh x\cos(\pm\pi/2)=0$), while the interior maps injectively since $\cosh z\neq0$ and periodicity in the imaginary direction has period $2\pi$, not $\pi$.

\medskip

 \mbox{}\\[2pt]
A principal inverse on the slit domain is
\[
\operatorname{arsinh} w=\log\!\big(w+\sqrt{w^{2}+1}\big),
\]
with branch cuts along $i(-\infty,-1]\cup i[1,\infty)$ so that $\Im(\operatorname{arsinh} w)\in(-\tfrac{\pi}{2},\tfrac{\pi}{2})$.

\medskip

 \mbox{}\\[2pt]
\[
\cosh^{2}z-\sinh^{2}z=1,\qquad
\sinh(z+\zeta)=\sinh z\,\cosh\zeta+\cosh z\,\sinh\zeta.
\]

\bigskip\hrule\bigskip

 \mbox{}\\[2pt]
$\cosh$ is \emph{entire}, \emph{even}, and $2\pi i$-periodic:
\[
\cosh(-z)=\cosh z,\qquad \cosh(z+2\pi i)=\cosh z.
\]
Zeros at $z=i\pi\big(k+\tfrac12\big)$, all simple. No poles.

\medskip

 \mbox{}\\[2pt]
With $z=x+iy$,
\[
\cosh z=\cosh x\cos y\ +\ i\,\sinh x\sin y \quad\Rightarrow\quad
u=\cosh x\cos y,\ \ v=\sinh x\sin y.
\]
Again one gets confocal conics:
\begin{align*}
	x=\text{const}&:\quad \left(\frac{u}{\cosh x}\right)^{2}+\left(\frac{v}{\sinh x}\right)^{2}=1
	&&\text{(ellipses, foci at $\pm1$)},\\[2pt]
	y=\text{const}&:\quad \left(\frac{u}{\cos y}\right)^{2}-\left(\frac{v}{\sin y}\right)^{2}=1
	&&\text{(hyperbolas, foci at $\pm1$)}.
\end{align*}
On the axes,
\[
y=0:\ w=\cosh x\in[1,\infty),\qquad
x=0:\ w=\cos y\in[-1,1].
\]

\medskip

 \mbox{}\\[2pt]
$\cosh'(z)=\sinh z$, which vanishes at $z=i\pi k$. Thus $\cosh$ fails to be injective across lines $y=k\pi$, but is injective on any strip avoiding these lines (e.g.\ $0<\Im z<\pi$).

\medskip

 \mbox{}\\[2pt]
\[
\boxed{\
	\cosh:\ \{\,0<\Im z<\pi\,\}\ \xrightarrow[\ \text{biholomorphism}\ ]{}\
	\mathbb C\setminus\big((-\infty,-1]\cup[1,\infty)\big)\ .
}\]
\emph{Explanation.} The midline $y=0$ maps to $[1,\infty)$; the top boundary $y=\pi$ maps to $(-\infty,-1]$; injectivity holds on $0<\Im z<\pi$ since there $\sinh z\neq0$.

\medskip

 \mbox{}\\[2pt]
\[
\operatorname{arcosh} w=\log\!\Big(w+\sqrt{w-1}\,\sqrt{w+1}\Big),
\]
with branch cuts along $(-\infty,-1]\cup[1,\infty)$ so that $\Re(\operatorname{arcosh} w)\ge0$ and $0<\Im(\operatorname{arcosh} w)<\pi$ on the principal sheet.

\medskip

 \mbox{}\\[2pt]
\[
\cosh(z+\zeta)=\cosh z\,\cosh\zeta+\sinh z\,\sinh\zeta,\qquad
\cosh z=1+2\sinh^{2}\!\frac{z}{2}.
\]

\bigskip\hrule\bigskip

 \mbox{}\\[2pt]
$\tanh$ is \emph{meromorphic}, \emph{odd}, and $i\pi$-periodic:
\[
\tanh(-z)=-\tanh z,\qquad \tanh(z+i\pi)=\tanh z.
\]
Zeros at $z=i\pi k$; poles (simple) at $z=i\pi\big(k+\tfrac12\big)$.

\medskip

 \mbox{}\\[2pt]
\[
\boxed{\
	\tanh:\ \{\,|\Im z|<\tfrac{\pi}{2}\,\}\ \xrightarrow[\ \text{biholomorphism}\ ]{}\ \mathbb D\ .
}\]
\emph{Boundary correspondence.} The real axis $y=0$ maps bijectively onto $(-1,1)$ (strictly increasing).
As $y\to\pm\frac{\pi}{2}$, $|\tanh(x+iy)|\to1$ uniformly in $x$; hence the horizontal boundaries map to $\partial\mathbb D$.

\medskip

 \mbox{}\\[2pt]
\[
\operatorname{artanh} w=\frac{1}{2}\log\!\left(\frac{1+w}{1-w}\right),
\qquad |w|<1,
\]
which maps $\mathbb D$ conformally onto $\{|\Im z|<\tfrac{\pi}{2}\}$.

\medskip

 \mbox{}\\[2pt]
\[
(\tanh z)'=\operatorname{sech}^{2}\!z,\qquad
\left|\tanh'(z)\right|=\frac{1}{|\cosh z|^{2}}
\]
and conjugating by a disk automorphism shows $\tanh$ is extremal for the disk-strip version of Schwarz--Pick.

\medskip

 \mbox{}\\[2pt]
Lines $x=\text{const}$ and $y=\text{const}$ in the strip map to orthogonal circle arcs inside $\mathbb D$ meeting $\partial\mathbb D$ orthogonally (images of preimages under the conformal equivalence with the half-plane followed by a Cayley map).

\bigskip\hrule\bigskip

 \mbox{}\\[2pt]
$\coth$ is \emph{meromorphic}, \emph{odd}, and $i\pi$-periodic:
\[
\coth(-z)=-\coth z,\qquad \coth(z+i\pi)=\coth z.
\]
Poles (simple) at $z=i\pi k$; zeros (simple) at $z=i\pi\big(k+\tfrac12\big)$.

\medskip

 \mbox{}\\[2pt]
\[
\boxed{\
	\coth:\ \{\,|\Im z|<\tfrac{\pi}{2}\,\}\setminus\{0\}\ \xrightarrow[\ \text{biholomorphism}\ ]{}\ \{\,|w|>1\,\}\ .
}\]
\emph{Boundary correspondence.} The real axis (excluding $0$) maps to the rays $(-\infty,-1)\cup(1,\infty)$.
As $y\to\pm\frac{\pi}{2}$, $|\coth(x+iy)|\to1^{+}$; thus horizontal boundaries map to the unit circle from the \emph{exterior} side.

\medskip

 \mbox{}\\[2pt]
\[
\operatorname{arcoth} w=\frac{1}{2}\log\!\left(\frac{w+1}{w-1}\right),\qquad |w|>1,
\]
with the standard logarithm branch so that $\Im(\operatorname{arcoth} w)\in(-\tfrac{\pi}{2},\tfrac{\pi}{2})$.

\medskip

 \mbox{}\\[2pt]
\[
\coth z=\tanh\!\left(z+\tfrac{i\pi}{2}\right),
\]
so the exterior-disk picture is just the disk picture shifted vertically by $i\pi/2$ and inverted via $w\mapsto 1/w$.

\bigskip\hrule\bigskip

 \mbox{}\\[2pt]
\[
\operatorname{arsinh} w=\log\!\big(w+\sqrt{w^{2}+1}\big),\qquad
\operatorname{arcosh} w=\log\!\big(w+\sqrt{w-1}\,\sqrt{w+1}\big),
\]
\[
\operatorname{artanh} w=\frac12\log\!\left(\frac{1+w}{1-w}\right),\qquad
\operatorname{arcoth} w=\frac12\log\!\left(\frac{w+1}{w-1}\right).
\]
Branch cuts are chosen to match the canonical target domains described above.

\medskip

 \mbox{}\\[2pt]
Using the Cayley map $C(\zeta)=\frac{1+\zeta}{1-\zeta}$ and its inverse $C^{-1}(w)=\frac{w-1}{w+1}$,
\[
\tanh z=\ C^{-1}\!\left(e^{2z}\right),\qquad
\coth z=\ C^{-1}\!\left(e^{2z}\right)^{-1},\qquad
\sinh z=\frac{e^{z}-e^{-z}}{2},\quad \cosh z=\frac{e^{z}+e^{-z}}{2}.
\]
Thus strip $\leftrightarrow$ disk/exterior-disk mappings for $\tanh$ and $\coth$ are just the exponentialâ€™s strip-to-sector equivalences composed with a Cayley map.

\medskip

 \mbox{}\\[2pt]
As $x\to\pm\infty$ with $y$ fixed, $\sinh z\sim \frac12 e^{x}e^{iy}$ and $\cosh z\sim \frac12 e^{x}e^{iy}$; hence horizontal lines map to asymptotically radial curves. For $\tanh$ and $\coth$, $|\tanh(x+iy)|\to 1$ and $|\coth(x+iy)|\to 1$ exponentially in $|x|$ (uniform in $y$ within the strip height).

\medskip

 \mbox{}\\[2pt]
$\sinh'(z)=\cosh z$ vanishes along $y=\frac{\pi}{2}+\pi\mathbb Z$; $\cosh'(z)=\sinh z$ vanishes along $y=\pi\mathbb Z$.
Therefore, the natural injectivity strips are $|\Im z|<\tfrac{\pi}{2}$ for $\sinh$ and $0<\Im z<\pi$ for $\cosh$.
For $\tanh$ and $\coth$, poles on the horizontal boundaries determine the natural strip height $\pi$.

\bigskip\hrule\bigskip

\[
\boxed{\
	\sinh:\ \{\,|\Im z|<\tfrac{\pi}{2}\,\}\ \longrightarrow\
	\mathbb C\setminus i\big((-\infty,-1]\cup[1,\infty)\big)\ \ \text{(biholomorphism)}\ .
}\]
\[
\boxed{\
	\cosh:\ \{\,0<\Im z<\pi\,\}\ \longrightarrow\
	\mathbb C\setminus\big((-\infty,-1]\cup[1,\infty)\big)\ \ \text{(biholomorphism)}\ .
}\]
\[
\boxed{\
	\tanh:\ \{\,|\Im z|<\tfrac{\pi}{2}\,\}\ \longrightarrow\ \mathbb D\ \ \text{(biholomorphism)}\ .
}\]
\[
\boxed{\
	\coth:\ \{\,|\Im z|<\tfrac{\pi}{2}\,\}\setminus\{0\}\ \longrightarrow\ \{\,|w|>1\,\}\ \ \text{(biholomorphism)}\ .
}\]

\medskip

If $\sinh z_{1}=\sinh z_{2}$ then $e^{z_{1}}-e^{-z_{1}}=e^{z_{2}}-e^{-z_{2}}$.
Rearranging gives $\{e^{z_{1}},e^{-z_{1}}\}=\{e^{z_{2}},e^{-z_{2}}\}$.
Taking logs in the horizontal strip $|\Im z|<\pi/2$ (where the exponential is injective modulo $2\pi i$) forces $z_{1}=z_{2}$.

Set $z=x\pm i\pi/2$. Then $\sinh z=\sinh x\cdot 0 \ \pm i\,\cosh x$, so the boundaries map to $\pm i[1,\infty)$; the interior cannot reach those rays by the open mapping theorem and the maximum modulus principle applied to $1/(\sinh z\mp i)$.

  apply to $\cosh$ (use $\sinh$ zeros to avoid critical lines) and to $\tanh,\coth$ using the representation via exponentials and the Cayley transform.

We use principal branches of $\log$ and $\sqrt{\cdot}$ with branch cut $(-\infty,0]$ unless stated otherwise.
For each inverse, the principal domain is obtained by slitting the $w$â€“plane along the images of the multiple values.

\bigskip\hrule\bigskip

 \mbox{}\\[2pt]
\BoxEq{ \arcsin w = -\,i\,\log\!\Big(i\,w+\sqrt{\,1-w^{2}\,}\Big) }

 \mbox{}\\[2pt]
Branch points at $w=\pm1$; principal cuts along $(-\infty,-1]\cup[1,\infty)$.

 \mbox{}\\[2pt]
\BoxEq{ \arcsin:\ \mathbb C\setminus\big((-\infty,-1]\cup[1,\infty)\big)\ \longrightarrow\ \{\,|\Re z|<\tfrac{\pi}{2}\,\} }
For $w\in(-1,1)$, $\arcsin w\in(-\tfrac{\pi}{2},\tfrac{\pi}{2})\subset\mathbb R$.
For $w>1$,
$\arcsin w=\tfrac{\pi}{2}-i\,\operatorname{arcosh} w$ (hence $\Re=\tfrac{\pi}{2}$);
for $w<-1$,
$\arcsin w=-\tfrac{\pi}{2}+i\,\operatorname{arcosh}(-w)$ (hence $\Re=-\tfrac{\pi}{2}$).

 \mbox{}\\[2pt]
Approaching the cuts $[1,\infty)$ or $(-\infty,-1]$ forces $\Re \arcsin w\to \pm\tfrac{\pi}{2}$ and $|\Im \arcsin w|\to\infty$.
The real axis segment $(-1,1)$ maps to the real segment $(-\tfrac{\pi}{2},\tfrac{\pi}{2})$.

\bigskip\hrule\bigskip

 \mbox{}\\[2pt]
\BoxEq{ \arccos w = \frac{\pi}{2}-\arcsin w }
\BoxEq{ \arccos w = \frac{1}{i}\,\log\!\Big(w+\sqrt{w-1}\,\sqrt{w+1}\Big) }

 \mbox{}\\[2pt]
Same as $\arcsin$: branch points $\pm1$; cuts $(-\infty,-1]\cup[1,\infty)$.

 \mbox{}\\[2pt]
\BoxEq{ \arccos:\ \mathbb C\setminus\big((-\infty,-1]\cup[1,\infty)\big)\ \longrightarrow\ \{\,0<\Re z<\pi\,\} }
For $w\in(-1,1)$, $\arccos w\in(0,\pi)\subset\mathbb R$.
For $w>1$, $\arccos w=i\,\operatorname{arcosh} w$ (so $\Re=0$);
for $w<-1$, $\arccos w=\pi - i\,\operatorname{arcosh}(-w)$ (so $\Re=\pi$).

 \mbox{}\\[2pt]
The two slits map to the vertical strip boundaries $\Re z=0$ and $\Re z=\pi$.
The central interval $(-1,1)$ maps to the real segment $(0,\pi)$.

\bigskip\hrule\bigskip

 \mbox{}\\[2pt]
\BoxEq{ \arctan w = \frac{1}{2i}\,\log\!\left(\frac{1+i\,w}{\,1-i\,w\,}\right) }

 \mbox{}\\[2pt]
Branch points at $w=\pm i$; principal cuts $i(-\infty,-1]\cup i[1,\infty)$ along the imaginary axis beyond $\pm i$.

 \mbox{}\\[2pt]
\BoxEq{ \arctan:\ \mathbb C\setminus i\big((-\infty,-1]\cup[1,\infty)\big)\ \longrightarrow\ \{\,|\Re z|<\tfrac{\pi}{2}\,\} }
On $\mathbb R$, $\arctan \mathbb R=(-\tfrac{\pi}{2},\tfrac{\pi}{2})$.
Approaching $w=\pm i\,t$ ($t\ge1$) drives $\Re \arctan w\to \pm\tfrac{\pi}{2}$ and $|\Im|\to\infty$.

 \mbox{}\\[2pt]
$\arctan(-w)=-\arctan w$; conjugation across the real axis preserves values away from cuts.

\bigskip\hrule\bigskip

 \mbox{}\\[2pt]
\BoxEq{ \arccot w = \frac{1}{2i}\,\log\!\left(\frac{w+i}{\,w-i\,}\right) }
\BoxEq{ \arccot w = \frac{\pi}{2}-\arctan w }

 \mbox{}\\[2pt]
As for $\arctan$: branch points at $w=\pm i$; cuts $i(-\infty,-1]\cup i[1,\infty)$.

 \mbox{}\\[2pt]
\BoxEq{ \arccot:\ \mathbb C\setminus i\big((-\infty,-1]\cup[1,\infty)\big)\ \longrightarrow\ \{\,0<\Re z<\pi\,\} }
On $\mathbb R$, $\arccot \mathbb R=(0,\pi)$.
Approaching the cuts pins the image to $\Re z=0$ or $\Re z=\pi$ with $|\Im|\to\infty$.

\bigskip\hrule\bigskip

\[
\arcsin w + \arccos w = \frac{\pi}{2},\qquad
\arctan w + \arccot w = \frac{\pi}{2}.
\]
\[
\arcsin w = -\,i\,\operatorname{arsinh}(i w),\qquad
\arccos w = \operatorname{arcosh} w \cdot \frac{1}{i}\ \ (\text{on }[1,\infty)).
\]
\[
\arctan w = \frac{1}{2i}\big(\log(1+i w)-\log(1-i w)\big),\quad
\arccot w = \frac{1}{2i}\big(\log(w+i)-\log(w-i)\big).
\]

\medskip

	\par\noindent\textbullet\quad $\arcsin$: real on $(-1,1)$; the cuts map to $\Re z=\pm\tfrac{\pi}{2}$.
	\par\noindent\textbullet\quad $\arccos$: real on $(-1,1)$; the cuts map to $\Re z=0,\ \pi$.
	\par\noindent\textbullet\quad $\arctan$: real on $\mathbb R$; the imaginary-axis cuts beyond $\pm i$ map to $\Re z=\pm\tfrac{\pi}{2}$.
	\par\noindent\textbullet\quad $\arccot$: real on $\mathbb R$; the same cuts map to $\Re z=0,\ \pi$.

	\par\noindent\textbullet\quad \textbf{Cayley (disk $\leftrightarrow$ right half-plane).}\\[2pt]
	\[
	\boxed{\,w=\frac{1+z}{1-z}\,}\qquad\text{inverse:}\quad z=\frac{w-1}{w+1}.
	\]

	\par\noindent\textbullet\quad \textbf{Half-plane $\to$ half-plane (three-point normalization).}\\[2pt]
	\[
	\boxed{\,w=\frac{(z-a)(c-b)}{(z-b)(c-a)}\,}.
	\]

	\par\noindent\textbullet\quad \textbf{Disk automorphisms.}\\[2pt]
	\[
	\boxed{\,\phi_{a,\theta}(z)=e^{i\theta}\frac{z-a}{1-\bar a z}\,},\qquad |a|<1.
	\]

	\par\noindent\textbullet\quad \textbf{Strip $|\Im z|<h/2$ $\to$ right half-plane.}\\[2pt]
	\[
	\boxed{\,w=\exp\!\left(\frac{\pi z}{h}\right)\,}.
	\]

	\par\noindent\textbullet\quad \textbf{Strip $|\Im z|<h/2$ $\to$ unit disk.}\\[2pt]
	\[
	\boxed{\,\zeta=\frac{e^{\pi z/h}-1}{\,e^{\pi z/h}+1\,}\,}.
	\]

	\par\noindent\textbullet\quad \textbf{Strip $\to$ strip (height scaling).}\\[2pt]
	\[
	\boxed{\,z\mapsto \frac{h_2}{h_1}\,z\,}.
	\]

	\par\noindent\textbullet\quad \textbf{Band $a<\Im z<b$ $\to$ centered strip.}\\[2pt]
	\[
	\boxed{\,z\mapsto \frac{\pi}{b-a}\!\left(z-i\frac{a+b}{2}\right)\,}.
	\]

	\par\noindent\textbullet\quad \textbf{Sector $\{0<\arg z<\alpha\}$ $\to$ upper half-plane.}\\[2pt]
	\[
	\boxed{\,w=z^{\pi/\alpha}\,}\ \ \text{(principal branch)}.
	\]

	\par\noindent\textbullet\quad \textbf{Wedge $\to$ disk.}\\[2pt]
	Compose item (8) with Cayley (item 1).

	\par\noindent\textbullet\quad \textbf{Upper half-plane $\to$ disk (prescribed triple).}\\[2pt]
	\[
	\boxed{\,\Phi(z)=\frac{(z-a)}{(z-\bar a)}\cdot \frac{(b-\bar a)}{(b-a)}\,}.
	\]

	\par\noindent\textbullet\quad \textbf{Annulus $r<|z|<1$ $\leftrightarrow$ strip.}\\[2pt]
	\[
	\boxed{\,w=\log z\,}\quad\text{maps to }\ \log r<\Re w<0.
	\]

	\par\noindent\textbullet\quad \textbf{Annulus $\to$ disk.}\\[2pt]
	Use $w=\log z$ then item (5).

	\par\noindent\textbullet\quad \textbf{Half-plane minus disk $\to$ annulus.}\\[2pt]
	\[
	\boxed{\,\zeta=\frac{z-\alpha}{z+\alpha}\,},\qquad \alpha^{2}=a^{2}-b^{2}.
	\]

	\par\noindent\textbullet\quad \textbf{Disk with off-center hole $\to$ annulus.}\\[2pt]
	Center via $\phi_a$ (item 3), then items (11)â€“(12).

	\par\noindent\textbullet\quad \textbf{Punctured plane $\leftrightarrow$ cylinder.}\\[2pt]
	\[
	\boxed{\,w=\log z\,}\quad(\text{period }2\pi i).
	\]

	\par\noindent\textbullet\quad \textbf{Strip $\to$ punctured plane.}\\[2pt]
	\[
	\boxed{\,z\mapsto e^{z}\,}.
	\]

	\par\noindent\textbullet\quad \textbf{Ray-slit plane $\mathbb C\setminus[0,\infty)$ $\to$ half-plane.}\\[2pt]
	\[
	\boxed{\,w=\sqrt{z}\,}\ \ \text{(choose branch)}.
	\]

	\par\noindent\textbullet\quad \textbf{Segment-slit plane $\mathbb C\setminus[a,b]$ $\to$ half-plane.}\\[2pt]
	\[
	\boxed{\,w=\sqrt{\frac{z-a}{\,z-b\,}}\,}.
	\]

	\par\noindent\textbullet\quad \textbf{Exterior of $[-1,1]$ $\leftrightarrow$ exterior unit circle (Joukowski).}\\[2pt]
	\[
	\boxed{\,w=z+\frac{1}{z}\,},\qquad
	z=\frac{w\pm\sqrt{w^{2}-4}}{2}.
	\]

	\par\noindent\textbullet\quad \textbf{Exterior of ellipse $\leftrightarrow$ exterior unit circle.}\\[2pt]
	\[
	\boxed{\,w=\tfrac12\!\left(c z+\frac{1}{c z}\right)\,}\quad(\text{$c$ from axes}).
	\]

	\par\noindent\textbullet\quad \textbf{Right half-plane $\to$ vertical strip.}\\[2pt]
	\[
	\boxed{\,z\mapsto \frac{1}{\pi}\log\frac{z-1}{\,z+1\,}\,}.
	\]

	\par\noindent\textbullet\quad \textbf{Upper half-plane $\to$ rectangle (SC/elliptic).}\\[2pt]
	\[
	\boxed{\,\zeta=\int^z \frac{dt}{\sqrt{(t-a)(t-b)(t-c)(t-d)}}\,}.
	\]

	\par\noindent\textbullet\quad \textbf{Rectangle $\to$ disk (Jacobi sn).}\\[2pt]
	\[
	\boxed{\,\zeta=\operatorname{sn}\!\left(\frac{K(k)}{L}\,z;\,k\right)\,}.
	\]

	\par\noindent\textbullet\quad \textbf{Half-disk $\leftrightarrow$ half-plane.}\\[2pt]
	Restriction of Cayley (item 1) and inverse.

	\par\noindent\textbullet\quad \textbf{Lens (intersection of two disks) $\to$ disk.}\\[2pt]
	MĂ¶bius normalizes the circles; then a power map; then Cayley.

	\par\noindent\textbullet\quad \textbf{Half-strip $\{x>0,\ 0<\Im z<h\}$ $\to$ half-disk.}\\[2pt]
	\[
	\boxed{\,\exp(\pi z/h)\,}\ \ \text{then power, then Cayley}.
	\]

	\par\noindent\textbullet\quad \textbf{Polygon $\to$ half-plane (Schwarz--Christoffel).}\\[2pt]
	\[
	\boxed{\,\Phi'(z)=C\prod_k (z-z_k)^{\alpha_k-1}\,},\qquad \sum\alpha_k=2.
	\]

	\par\noindent\textbullet\quad \textbf{Upper half-plane $\to$ slit half-plane.}\\[2pt]
	\[
	\boxed{\,w=z+\frac{1}{z}\,}\ \ \text{then a real MĂ¶bius adjustment}.
	\]

	\par\noindent\textbullet\quad \textbf{Disk $\to$ disk with boundary arc removed.}\\[2pt]
	Automorphism to put endpoints at $\pm1$, then boundary power $z^\lambda$.

	\par\noindent\textbullet\quad \textbf{Finite Blaschke product (disk $\to$ disk, degree $n$).}\\[2pt]
	\[
	\boxed{\,B(z)=e^{i\theta}\prod_{k=1}^n \frac{z-a_k}{\,1-\bar a_k z\,}\,}.
	\]

 \mbox{}\\[2pt]
\[
w=\frac{1+z}{\,1-z\,}
\quad\text{maps}\quad
\mathbb D=\{|z|<1\}\ \text{onto}\ \{\,\Re w>0\,\},
\qquad
z=\frac{w-1}{\,w+1\,}
\]
is the inverse.

\medskip

 \mbox{}\\[2pt]
Compute
\[
\Re\!\left(\frac{1+z}{\,1-z\,}\right)
=\frac{\,1-|z|^{2}\,}{\,|1-z|^{2}\,}.
\]
Thus $\Re w>0$ for $|z|<1$, and $\Re w=0$ for $|z|=1$ (except $z=1$, which maps to $w=\infty$).
Therefore
\[
|z|<1\ \Longleftrightarrow\ \Re w>0,
\qquad
|z|=1\ \Longleftrightarrow\ \Re w=0 .
\]

\medskip

 \mbox{}\\[2pt]
$z=0\mapsto w=1$,
\quad
$z\to1^{-}\mapsto w\to+\infty$,
\quad
and $\partial\mathbb D\setminus\{1\}$ maps to the line $\Re w=0$.\\[2pt]
Circles/lines orthogonal to $\partial\mathbb D$ map to \emph{vertical} lines in the $w$â€“plane.

\bigskip\hrule\bigskip

 \mbox{}\\[2pt]
Let $L$ be a line or circle, and choose three distinct points $a,b,c\in L$. Define
\[
\Phi(z)=\frac{(z-a)(c-b)}{(z-b)(c-a)}.
\]
Then $\Phi(L)\subset\mathbb R\cup\{\infty\}$, with
\[
\Phi(a)=0,\qquad \Phi(b)=\infty,\qquad \Phi(c)=1,
\]
and the two sides of $L$ map to the half-planes $\Im\Phi(z)\gtrless 0$.

\medskip

 \mbox{}\\[2pt]
Given half-planes $H_1,H_2$ with boundary arcs $L_1,L_2$,
pick ordered boundary triples $a,b,c\in L_1$ and $A,B,C\in L_2$ (same cyclic order).
Then
\[
T(z)=\frac{(z-a)(c-b)}{(z-b)(c-a)}\cdot\frac{(C-A)}{(C-B)}
\]
is a MĂ¶bius map sending $L_1\!\to L_2$ with
\[
a\mapsto A,\qquad b\mapsto B,\qquad c\mapsto C,
\]
and taking the chosen side of $H_1$ onto the chosen side of $H_2$.

\medskip

 \mbox{}\\[2pt]
To send $L$ to $\mathbb R$, use $\Phi$ above; then pre/postcompose with an \emph{affine real} map
\[
\xi\longmapsto \alpha\,\xi+\beta,\qquad \alpha>0,
\]
to obtain any target half-plane, e.g.\ $\Re w>0$ or $\Im w>0$.
```

## CP-IV-0008


- chapter line: 5247
- atlas source solution flag: `unknown`
- linked source-solution candidates: `none`
- embedded solution marker in problem body: `NO`

```tex
(Gaussian curvature formula and isolated zeros)

Let a minimal surface be given by Weierstrass data $(f,g)$ as in Problem 8:
	\[
	X(z)=\Re\int^z \Big(\tfrac12 f(1-g^2),\ \tfrac{i}{2}f(1+g^2),\ fg\Big)\,dz.
	\]

	\medskip
	\textbf{Step 1: induced metric.}
	In the parameter $z=u+iv$ the parametrization is conformal and one has
	\[
	ds^2=\lambda^2|dz|^2,\qquad
	\lambda=\frac{|f|(1+|g|^2)}{2},
	\]
	equivalently
	\[
	E=G=\lambda^2=\frac{|f|^2(1+|g|^2)^2}{4},\qquad F=0.
	\]

	\medskip
	\textbf{Step 2: Gauss map and stereographic projection.}
	For a minimal surface, the Gauss map $N:S\to S^2$ is conformal in conformal coordinates, and its stereographic
	coordinate is precisely $g$. The round metric on $S^2$ written in the stereographic coordinate $g$ is
	\[
	ds^2_{S^2}=\frac{4}{(1+|g|^2)^2}|dg|^2,
	\]
	so the pullback satisfies
	\[
	|N_u|^2+|N_v|^2=\frac{4}{(1+|g|^2)^2}\bigl(|g_u|^2+|g_v|^2\bigr).
	\]
	Since $g$ is holomorphic (meromorphic), $g_u=g'(z)$ and $g_v=i g'(z)$, hence
	\[
	|g_u|^2+|g_v|^2=2|g'(z)|^2,
	\]
	and therefore
	\[
	|N_u|^2+|N_v|^2=\frac{8|g'|^2}{(1+|g|^2)^2}.
	\]

	\medskip
	\textbf{Step 3: relate $K$ to $dN$ for minimal surfaces.}
	In an orthonormal basis of $T_pS$, the eigenvalues of $dN_p$ are $-k_1,-k_2$.
	For a minimal surface $k_2=-k_1$, so $K=k_1k_2=-k_1^2\le 0$ and
	\[
	\|dN\|^2=k_1^2+k_2^2=2k_1^2=-2K,
	\qquad\text{hence}\qquad
	K=-\frac12\|dN\|^2.
	\]
	In conformal coordinates, an orthonormal basis is $e_1=X_u/\lambda$, $e_2=X_v/\lambda$, so
	\[
	\|dN\|^2=\frac{|N_u|^2+|N_v|^2}{\lambda^2}.
	\]
	Thus
	\[
	K=-\frac12\frac{|N_u|^2+|N_v|^2}{\lambda^2}
	=-\frac12\frac{\frac{8|g'|^2}{(1+|g|^2)^2}}{\frac{|f|^2(1+|g|^2)^2}{4}}
	=-\frac{16|g'|^2}{|f|^2(1+|g|^2)^4}.
	\]
	Equivalently,
	\[
	K=-\left(\frac{4|g'|}{|f|(1+|g|^2)^2}\right)^2.
	\]

	\medskip
	\textbf{Zeros of $K$.}
	Assume the surface is regular (no branch points), so $f\neq 0$.
	Then $K(p)=0$ iff $g'(p)=0$.
	But $g'$ is holomorphic wherever $g$ is holomorphic, hence either $g'\equiv 0$ or its zeros are isolated.
	If $g'\equiv 0$, then $g$ is constant, the Gauss map is constant, and the surface is a plane, so $K\equiv 0$.
	Otherwise, the zeros of $g'$ (hence of $K$) are isolated.
```

## CP-IV-0016


- chapter line: 5323
- atlas source solution flag: `unknown`
- linked source-solution candidates: `none`
- embedded solution marker in problem body: `NO`

```tex
â€” Conformal mappings

\noindent
	(a)\; $D$ is the region exterior to the two circles $|z-1|=1$ and $|z+1|=1$.
	Find a conformal mapping from $D$ to the exterior of the unit circle.\\
	\emph{Hint:} First apply an inversion with respect to the origin $(z\mapsto 1/z)$,
	then rotate and scale so as to use the exponential function to get to a half plane,
	from where use MĂ¶bius.

	\medskip
	\noindent
	(b)\; Find a conformal map from the unit disc $|z|<1$ onto the strip $-\pi/2<\eta<\pi/2$,
	taking the origin to the origin, $1$ to $\xi=+\infty$, $-1$ to $\xi=-\infty$.
	(Thus, the upper half of the unit circle maps to $\eta=\pi/2$ and the lower half to $\eta=-\pi/2$.)

	\medskip
	\noindent
	(c)\; Find a conformal map of the quarter-disc $0<|z|<1,\ 0<\arg z<\pi/2$
	to the upper half-plane $\eta>0$, taking $0$ to $0$, $1$ to $1$, and $i$ to $\infty$.

	\bigskip\hrule\bigskip

		\setlength{\itemsep}{0.4em}
		\par\noindent\textbullet\quad \textbf{Invert.} Let $w=1/z$. Then the circles through $0$ become lines:
		\[
		|z-1|=1 \Rightarrow \Re w=\tfrac12,\qquad
		|z+1|=1 \Rightarrow \Re w=-\tfrac12.
		\]
		Hence $D$ maps to the vertical strip $S=\{-\tfrac12<\Re w<\tfrac12\}$.
		\par\noindent\textbullet\quad \textbf{Rotate/scale to a horizontal strip.} Put $s=i\pi w$.
		Then $|\Im s|<\pi/2$.
		\par\noindent\textbullet\quad \textbf{Exponential to a half-plane.} Let $u=e^{\,s}$.
		Then $|\Im s|<\pi/2 \;\Longrightarrow\; \Re u>0$.
		\par\noindent\textbullet\quad \textbf{MĂ¶bius to exterior unit disk.} Use

	\[
	\Phi(u)=\frac{u+1}{u-1},\qquad \operatorname{Re} u>0 \longmapsto |\zeta|>1.
	\]

	Therefore a concrete map is
	\[
	\boxed{\ \zeta=\Phi\!\big(e^{\,i\pi/z}\big)=\dfrac{e^{\,i\pi/z}+1}{e^{\,i\pi/z}-1}\ }.
	\]

	\bigskip

		\setlength{\itemsep}{0.4em}
		\par\noindent\textbullet\quad \textbf{Disk to right half-plane (Cayley).}
		\[
		w=\frac{1+z}{1-z},\qquad |z|<1 \mapsto \Re w>0,
		\]
		and $z=0\mapsto w=1$, $z=1\mapsto w=\infty$, $z=-1\mapsto w=0$.
		\par\noindent\textbullet\quad \textbf{Log to a horizontal strip.}
		\[
		\zeta=\log w \quad (\text{principal branch}),\qquad \Im\zeta\in\big(-\tfrac{\pi}{2},\tfrac{\pi}{2}\big).
		\]
		Then $\zeta(0)=0$, $\zeta(1)=+\infty$, $\zeta(-1)=-\infty$.

	Hence
	\[
	\boxed{\ \zeta=\log\!\left(\frac{1+z}{1-z}\right)\ }.
	\]

	\bigskip

		\setlength{\itemsep}{0.4em}
		\par\noindent\textbullet\quad \textbf{Square to upper semicircle.}
		\[
		t=z^{2}:\quad \{0<|z|<1,\ 0<\arg z<\tfrac{\pi}{2}\}
		\longmapsto \{|t|<1,\ \Im t>0\}.
		\]
		Moreover $0\mapsto0$, $1\mapsto1$, $i\mapsto-1$.
		\par\noindent\textbullet\quad \textbf{Real MĂ¶bius to upper half-plane.}
		Find $M(t)$ with $M(-1)=\infty$, $M(0)=0$, $M(1)=1$.
		A suitable choice is
		\[
		M(t)=\frac{2t}{t+1}.
		\]

	Therefore
	\[
	\boxed{\ \zeta=M(z^{2})=\frac{2z^{2}}{z^{2}+1}\ }.
	\]
	It maps the quarter-disk conformally onto $\Im\zeta>0$ and has
	$\zeta(0)=0$, $\zeta(1)=1$, $\zeta(i)=\infty$.

	\section*{6(c)\quad Quarter-disk $0<|z|<1,\ 0<\arg z<\tfrac{\pi}{2}$
		$\longrightarrow$ upper half-plane $\Im\zeta>0$,
		with $0\mapsto0$, $1\mapsto1$, $i\mapsto\infty$}

	Construct an explicit conformal map $\zeta=\zeta(z)$ that maps the open quarter-disk
	\[
	Q=\{\,z:\ 0<|z|<1,\ 0<\arg z<\tfrac{\pi}{2}\,\}
	\]
	onto the upper half-plane $\mathbb H=\{\zeta:\ \Im\zeta>0\}$, sending the three marked boundary
	points
	\[
	z=0 \longmapsto \zeta=0,\qquad
	z=1 \longmapsto \zeta=1,\qquad
	z=i \longmapsto \zeta=\infty .
	\]

	Let
	\[
	t=z^{2}.
	\]
	Write $z=re^{i\theta}$ with $0<r<1$ and $0<\theta<\frac{\pi}{2}$. Then
	\[
	t=r^{2}e^{i(2\theta)}\quad\Rightarrow\quad |t|<1,\ \ 0<\arg t<\pi \iff \Im t>0.
	\]
	Therefore the squaring map $z\mapsto t=z^{2}$ sends $Q$ \emph{bijectively and conformally}
	onto the \emph{open upper semicircle}
	\[
	S=\{\,t:\ |t|<1,\ \Im t>0\,\}.
	\]
	On the boundary rays/arcs we have
	\[
	0\mapsto 0,\qquad 1\mapsto 1,\qquad i\mapsto -1.
	\]
	(Conformality is immediate, since $(z^{2})'=2z\neq 0$ on $Q$.)

	Seek a real-coefficient MĂ¶bius transformation
	\[
	M(t)=\frac{a t+b}{c t+d},\qquad a,b,c,d\in\mathbb R,\ \ ad-bc\neq0,
	\]
	such that
	\[
	M(-1)=\infty,\qquad M(0)=0,\qquad M(1)=1.
	\]
	Imposing the conditions:

		\par\noindent\textbullet\quad $M(-1)=\infty \ \Rightarrow\ c(-1)+d=0 \ \Rightarrow\ d=c$.
		\par\noindent\textbullet\quad $M(0)=0 \ \Rightarrow\ b/d=0 \ \Rightarrow\ b=0$.
		\par\noindent\textbullet\quad $M(1)=1 \ \Rightarrow\ a/(c+d)=1 \ \Rightarrow\ a=c+d=2c$.

	Up to an overall nonzero constant (which does not change the map), we can take $c=1$ and obtain
	\[
	\boxed{\,M(t)=\frac{2t}{t+1}\,}.
	\]

	Let $t=x+iy$ with $y>0$. Then
	\[
	M(t)=\frac{2t}{1+t},\qquad
	\Im M(t)=\frac{2\,\Im\big(t(1+\overline{t})\big)}{|1+t|^{2}}
	=\frac{2\,\Im t}{|1+t|^{2}}
	=\frac{2y}{|1+t|^{2}}
	>0.
	\]
	Hence $M$ maps $\{\,\Im t>0\,\}$ into itself; in particular it maps the upper semicircle $S$
	(which lies in $\Im t>0$) into the upper half-plane. Moreover
	\[
	M'(t)=\frac{2}{(1+t)^{2}}\neq0\quad\text{on}\ S,
	\]
	so $M$ is conformal (locally injective) there. The three-point normalization guarantees that it
	sends the three distinguished boundary points as prescribed:
	\[
	M(-1)=\infty,\qquad M(0)=0,\qquad M(1)=1.
	\]

	Define the desired map
	\[
	\boxed{\ \zeta(z)=M\big(z^{2}\big)=\frac{2z^{2}}{z^{2}+1}\ }.
	\]
	Then the normalization follows immediately:
	\[
	\zeta(0)=0,\qquad \zeta(1)=1,\qquad \zeta(i)=\infty .
	\]
	Because $t=z^{2}$ has $\Im t>0$ on $Q$ and $\Im M(t)>0$ for $\Im t>0$, we have
	\[
	\Im \zeta(z)=\Im\big(M(z^{2})\big)>0\quad\text{for all }z\in Q.
	\]
	Also $\zeta'(z)=M'(z^{2})\cdot 2z=\dfrac{4z}{(1+z^{2})^{2}}\neq0$ on $Q$, hence the map is conformal
	throughout the domain.

		\par\noindent\textbullet\quad The \emph{real radius} segment $\{\,0<z<1\,\}$ maps by $t=z^{2}$ to $(0,1)$ and then by $M$
		to $(0,1)\subset\mathbb R$; thus that edge lands on the real axis between $0$ and $1$.
		\par\noindent\textbullet\quad The \emph{imaginary radius} segment $\{\,0<iz<i\,\}$ maps by $t=z^{2}$ to $(0,-1)$ and then by $M$
		to $(0,\infty)$ on $\mathbb R$; thus the edge $0\to i$ lands on the ray $[0,\infty)$.
		\par\noindent\textbullet\quad The \emph{circular arc} $\{\,e^{i\theta}: 0<\theta<\tfrac{\pi}{2}\,\}$ maps by $t=z^{2}$ to the unit
		semicircle $\{\,e^{i\phi}: 0<\phi<\pi\,\}$ and then by $M$ to the real line as a boundary set.

	The interior of the quarter-disk maps onto $\Im\zeta>0$ by the positivity computation for $\Im M(t)$.

	The composition
	\[
	\boxed{\ \zeta(z)=\frac{2z^{2}}{z^{2}+1}\ }
	\]
	is a conformal bijection from the open quarter-disk $Q$ onto the upper half-plane $\mathbb H$,
	satisfying the three mapping conditions $0\mapsto0$, $1\mapsto1$, $i\mapsto\infty$.

	\subsection*{(b) Unit disk $\to$ strip $-\dfrac{\pi}{2}<\Im\zeta<\dfrac{\pi}{2}$}

	\textbf{Disk to right half-plane (Cayley).}
	\[
	w=\frac{1+z}{1-z},\qquad |z|<1 \;\Longrightarrow\; \operatorname{Re} w>0,
	\]
	and on the marked points
	\[
	z=0 \mapsto w=1,\qquad z=1 \mapsto w=\infty,\qquad z=-1 \mapsto w=0.
	\]
	Moreover, the unit circle $|z|=1\setminus\{1\}$ maps to the imaginary axis $\operatorname{Re} w=0$.

	\medskip
	\textbf{Log to a horizontal strip.}
	Use the principal logarithm on the right half-plane:
	\[
	\zeta=\log w=\ln|w|+i\,\arg(w),\qquad \arg(w)\in\big(-\tfrac{\pi}{2},\tfrac{\pi}{2}\big),
	\]
	so
	\[
	-\frac{\pi}{2} < \Im \zeta < \frac{\pi}{2}.
	\]
	At the marked points:
	\[
	\zeta(0)=\log 1=0,\qquad
	\zeta(1)=\log(\infty)=+\infty,\qquad
	\zeta(-1)=\log(0)=-\infty.
	\]

	\medskip
	\textbf{Which boundary goes where.}
	For $z=e^{i\theta}$,
	\[
	w=\frac{1+e^{i\theta}}{1-e^{i\theta}}
	= -\,i\,\cot\!\left(\frac{\theta}{2}\right)\in i\mathbb{R}.
	\]
	Hence
	\[
	0<\theta<\pi\ (\text{upper semicircle}) \Rightarrow \Im w<0 \Rightarrow \Im \zeta=-\frac{\pi}{2},
	\]
	\[
	\pi<\theta<2\pi\ (\text{lower semicircle}) \Rightarrow \Im w>0 \Rightarrow \Im \zeta=+\frac{\pi}{2}.
	\]
	(If one wants the upper semicircle to land on $\Im\zeta=+\pi/2$, use $\zeta=-\log\!\left(\frac{1+z}{1-z}\right)$.)

	\medskip
	\textbf{Hence}
	\[
	\boxed{\ \zeta=\log\!\left(\frac{1+z}{1-z}\right)\ }
	\]
	is a conformal bijection from $|z|<1$ onto the strip $-\pi/2<\Im\zeta<\pi/2$ with
	$0\mapsto 0$, $1\mapsto +\infty$, $-1\mapsto -\infty$.

	\subsection*{(a) Exterior of the two circles $\boldsymbol{|z-1|=1}$ and $\boldsymbol{|z+1|=1}$
		$\;\longrightarrow\;$ exterior of $\boldsymbol{|\zeta|=1}$}

	Let
	\[
	D=\big\{z\in\mathbb C:\ |z-1|\ge 1,\ |z+1|\ge 1\big\}\setminus\big(\{|z-1|=1\}\cup\{|z+1|=1\}\big),
	\]
	the region \emph{exterior to both} unit circles centered at $\pm1$.
	Construct an explicit conformal bijection $F:D\to\{\zeta:\ |\zeta|>1\}$.

	Let $w=\dfrac{1}{z}$.
	For any $a\in\mathbb C$, the circle $\{|z-a|=|a|\}$ (which passes through $0$) satisfies
	\[
	|z-a|=|a|
	\iff \left|\frac{1}{w}-a\right|=|a|
	\iff |1-aw|=|a||w|
	\iff 1=2\,\Re(aw).
	\]
	Hence circles through $0$ invert to \emph{lines}.
	For $a=1$ and $a=-1$ we obtain
	\[
	|z-1|=1 \iff \Re w=\frac{1}{2},
	\qquad
	|z+1|=1 \iff \Re w=-\frac{1}{2}.
	\]

	\emph{Which side is the exterior?}  Using $|1-aw|^{2}=(1-2\Re(aw)+|a|^{2}|w|^{2})$ we compute
	\[
	|z-1|>1
	\iff |1-w|>|w|
	\iff 1-2\Re w>0
	\iff \Re w<\frac{1}{2},
	\]
	\[
	|z+1|>1
	\iff |1+ w|>|w|
	\iff 1+2\Re w>0
	\iff \Re w>-\frac{1}{2}.
	\]
	Therefore the inversion $w=1/z$ sends $D$ bijectively onto the \emph{vertical strip}
	\[
	S=\Big\{\,w\in\mathbb C:\ -\tfrac12<\Re w<\tfrac12\,\Big\}.
	\]
	(Since $z\neq 0$ on $D$, the inversion is analytic and injective there.)

	Define
	\[
	s=i\pi w.
	\]
	Write $w=u+iv$ with $-\tfrac12<u<\tfrac12$. Then $s=i\pi(u+iv)=-\pi v+i\pi u$, so
	\[
	|\Im s|=|\pi u|<\frac{\pi}{2}.
	\]
	Consequently $S$ is mapped conformally onto the horizontal strip
	\[
	T=\Big\{\,s\in\mathbb C:\ |\Im s|<\frac{\pi}{2}\,\Big\}.
	\]

	Set
	\[
	u=e^{\,s}.
	\]
	If $s=\sigma+i\tau$ with $|\tau|<\pi/2$, then
	\[
	\Re u = \Re\big(e^{\sigma}(\cos\tau+i\sin\tau)\big)=e^{\sigma}\cos\tau>0,
	\]
	because $\cos\tau>0$ on $(-\pi/2,\pi/2)$.
	Hence $e^{(\cdot)}$ maps $T$ conformally and bijectively onto the \emph{right half-plane}
	\[
	H=\{\,u\in\mathbb C:\ \Re u>0\,\},
	\]
	and the boundary lines $\Im s=\pm\pi/2$ go to the imaginary axis $\Re u=0$.

	Consider
	\[
	\Phi(u)=\frac{u+1}{u-1}.
	\]
	For $u\in H$ we have the equivalence
	\[
	|\Phi(u)|>1
	\iff |u+1|>|u-1|
	\iff (u+1)(\bar u+1)>(u-1)(\bar u-1)
	\iff 4\,\Re u>0,
	\]
	which holds precisely on $H$. Thus $\Phi$ maps $H$ conformally onto $\{\zeta:\ |\zeta|>1\}$ and
	sends the imaginary axis to the unit circle $|\zeta|=1$.

	The composition of the four conformal bijections yields
	\[
	F:D \xrightarrow{\,z\mapsto w=1/z\,} S
	\xrightarrow{\,w\mapsto s=i\pi w\,} T
	\xrightarrow{\,s\mapsto u=e^{\,s}\,} H
	\xrightarrow{\,u\mapsto \Phi(u)\,} \{|\zeta|>1\}.
	\]
	Therefore an explicit mapping is
	\[
	\boxed{\quad \zeta = F(z) = \Phi\!\big(e^{\,i\pi/z}\big)
		= \frac{e^{\,i\pi/z}+1}{\,e^{\,i\pi/z}-1\,}\quad }.
	\]
	Every factor is analytic and injective on the relevant domain; hence $F$ is conformal and bijective from $D$ onto $\{|\zeta|>1\}$.

	As $z\to\infty$ we have $e^{\,i\pi/z}=1+\dfrac{i\pi}{z}+O(z^{-2})$, so
	\[
	\zeta
	=\frac{2+\dfrac{i\pi}{z}+O(z^{-2})}{\dfrac{i\pi}{z}+O(z^{-2})}
	= \frac{2}{i\pi}\,z\,\Big(1+O(z^{-1})\Big)
	= -\,\frac{2i}{\pi}\,z\Big(1+O(z^{-1})\Big),
	\]
	which confirms that far out in $D$ the map behaves like an affine scaling of $z$, as expected.

		\par\noindent\textbullet\quad The line $\Re w=\tfrac12$ (image of $|z-1|=1$) becomes $\Im s=\tfrac{\pi}{2}$,
		then the imaginary axis, and finally the unit circle $|\zeta|=1$.
		\par\noindent\textbullet\quad The line $\Re w=-\tfrac12$ (image of $|z+1|=1$) becomes $\Im s=-\tfrac{\pi}{2}$,
		then the same imaginary axis, and again $|\zeta|=1$.
		\par\noindent\textbullet\quad The interior $-\tfrac12<\Re w<\tfrac12$ maps to $|\Im s|<\tfrac{\pi}{2}$,
		then to $\Re u>0$, and finally to $|\zeta|>1$.

	This completes the construction and detailed verification.
```

## CP-IV-0019


- chapter line: 5690
- atlas source solution flag: `unknown`
- linked source-solution candidates: `none`
- embedded solution marker in problem body: `NO`

```tex
\par\noindent\textbullet\quad Inversion in a circle is \emph{anti-conformal} (it involves complex conjugation), and the composition of two inversions is conformal; in particular, any composition of an \emph{even} number of inversions is holomorphic (hence MĂ¶bius on $\widehat{\mathbb C}$).
```

## CP-IV-0023


- chapter line: 5697
- atlas source solution flag: `unknown`
- linked source-solution candidates: `none`
- embedded solution marker in problem body: `NO`

```tex
\par\noindent\textbullet\quad \textbf{(b)}\;
	Consider the branch defined by
	\[
	f(z) \;=\; (r_{1}r_{2})^{1/2} \, e^{\,i(\theta_{1}+\theta_{2})/2},
	\qquad -\tfrac{\pi}{2}<\theta_{1},\ \theta_{2}\le \tfrac{3\pi}{2}.
	\]
	State the values of \((\theta_{1}+\theta_{2})/2\) on either side of the imaginary axis,
	and hence compute \(f(\pm0+iy)\) in terms of \(y\) for \(y\in\mathbb{R}\).
	Deduce that the branch cut is
	\[
	S \;=\; \{\,x+iy:\ x=0,\ |y|\le 1\,\}.
	\]
	Show that \(f(z)\sim z\) as \(|z|\to\infty\)
	(i.e.\ \(f(z)/z\to 1\) as \(|z|\to\infty\)).
	Sketch the image of the cut \(z\)-plane \(\mathbb{C}\setminus S\) under the map \(\zeta=f(z)\).

	\medskip
```

