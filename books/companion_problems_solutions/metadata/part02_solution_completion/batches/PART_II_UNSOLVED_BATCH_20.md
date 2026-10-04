# Part II missing-solution batch 20

- problems: **20**
- IDs: CP-II-0174, CP-II-0238, CP-II-0242, CP-II-0278, CP-II-0311, CP-II-0315, CP-II-0349, CP-II-0377, CP-II-0462, CP-II-0469, CP-II-0005, CP-II-0014, CP-II-0038, CP-II-0163, CP-II-0217, CP-II-0331, CP-II-0340, CP-II-0353, CP-II-0363, CP-II-0476

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
