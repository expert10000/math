# Part II missing-solution batch 07

- problems: **20**
- IDs: CP-II-0477, CP-II-0499, CP-II-0559, CP-II-0565, CP-II-0003, CP-II-0004, CP-II-0009, CP-II-0011, CP-II-0015, CP-II-0024, CP-II-0025, CP-II-0026, CP-II-0027, CP-II-0031, CP-II-0033, CP-II-0034, CP-II-0036, CP-II-0037, CP-II-0039, CP-II-0040

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
