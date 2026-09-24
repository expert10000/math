# Part IV Unsolved Solution Authoring Batch 05

- problems in batch: 20
- IDs: CP-IV-0088, CP-IV-0091, CP-IV-0093, CP-IV-0094, CP-IV-0095, CP-IV-0100, CP-IV-0101, CP-IV-0103, CP-IV-0105, CP-IV-0108, CP-IV-0115, CP-IV-0119, CP-IV-0120, CP-IV-0121, CP-IV-0122, CP-IV-0127, CP-IV-0130, CP-IV-0132, CP-IV-0136, CP-IV-0060

Author canonical worked solutions for these problems. Do not alter the problem statements.

## CP-IV-0088


- chapter line: 8187
- atlas source solution flag: `unknown`
- linked source-solution candidates: `none`
- embedded solution marker in problem body: `NO`

```tex
\par\noindent (i)\quad Show that $X$ is totally bounded.
```

## CP-IV-0091


- chapter line: 8192
- atlas source solution flag: `unknown`
- linked source-solution candidates: `none`
- embedded solution marker in problem body: `NO`

```tex
â€” constant curl, easy numbers

Take $\mathbf F=(-y,x)$. Then $L=-y$, $M=x$ and
\[
M_x - L_y \;=\; \partial_x(x) - \partial_y(-y) \;=\; 1 - (-1) \;=\; 2 \quad(\text{constant}).
\]
Area integral:
\[
\iint_{D} (M_x-L_y)\,dA
\;=\;
\iint_{D} 2\,dA
\;=\; 2\,\pi R^2.
\]
Line integral (check by parametrizing $C$):
\[
dx=-R\sin t\,dt,\qquad dy=R\cos t\,dt,
\]
\[
L\,dx+M\,dy
=
(-y)\,dx + (x)\,dy
=
(-R\sin t)(-R\sin t)\,dt + (R\cos t)(R\cos t)\,dt
=
R^2\,dt,
\]
\[
\oint_{C} (L\,dx+M\,dy)
=
\int_{0}^{2\pi} R^2\,dt
=
2\pi R^2.
\]
Both sides match: $2\pi R^2$.
```

## CP-IV-0093


- chapter line: 8230
- atlas source solution flag: `unknown`
- linked source-solution candidates: `none`
- embedded solution marker in problem body: `YES`

```tex
\par\noindent\textbullet\quad (\textbf{Operator norm and singular values})
	Show the maximal and minimal stretch factors (singular values) of $T$ are
	\[
	\sigma_{\max}=|A|+|B|,\qquad \sigma_{\min}=\bigl||A|-|B|\bigr|.
	\]
	\emph{Solution (sketch).} Write $T(z)=A\bigl(z+\tfrac{B}{A}\bar z\bigr)$ if $A\neq0$; by rotating/scaling the domain and range one reduces to $A\ge0$, $B\ge0$ real. Then $T$ acts by stretching along two orthogonal directions with factors $A\pm B$, giving the claim. General case follows by unitary conjugation.
```

## CP-IV-0094


- chapter line: 8240
- atlas source solution flag: `unknown`
- linked source-solution candidates: `none`
- embedded solution marker in problem body: `NO`

```tex
\par\noindent\textbullet\quad \textbf{Derivative not continuous from $(C^1,\|\cdot\|_\infty)$ to $(C,\|\cdot\|_\infty)$.}

	Take $f_n(x)=\tfrac{1}{n}\sin(n^2 x)$ on $[0,1]$.
	We have
	\[
	\|f_n\|_\infty=\frac{1}{n}\longrightarrow 0,
	\qquad
	\|f_n'\|_\infty = n \longrightarrow \infty .
	\]
	Hence $D$ is discontinuous with these norms.

	\medskip
```

## CP-IV-0095


- chapter line: 8256
- atlas source solution flag: `unknown`
- linked source-solution candidates: `none`
- embedded solution marker in problem body: `NO`

```tex
$|x|^3$ is $C^2$ with
$f'(x)=3x^2$ for $x>0$ and $f'(x)=-3x^2$ for $x<0$,
$f''(x)=6x$ for $x>0$ and $f''(x)=-6x$ for $x<0$, both extending continuously at $0$ by $0$,
while $f^{(3)}(x)=6$ for $x>0$ and $f^{(3)}(x)=-6$ for $x<0$, so $f^{(3)}$ has a jump at $0$.
```

## CP-IV-0100


- chapter line: 8264
- atlas source solution flag: `unknown`
- linked source-solution candidates: `none`
- embedded solution marker in problem body: `NO`

```tex
\par\noindent\textbullet\quad \textbf{Integration map is Lipschitz $C^k\!\to C^{k+1}$.}

	For $f,g\in C^k$ put $F=T(f)$ and $G=T(g)$ with
	\[
	F(x)=\int_a^x f(y)\,dy, \qquad G(x)=\int_a^x g(y)\,dy .
	\]
	Then
	\[
	\|F-G\|_\infty \;\le\; (b-a)\,\|f-g\|_\infty,
	\]
	and for $1\le j\le k+1$,
	\[
	\|F^{(j)}-G^{(j)}\|_\infty \;=\; \|f^{(j-1)}-g^{(j-1)}\|_\infty .
	\]
	Consequently,
	\[
	d_{C^{k+1}}(T(f),T(g))
	\;\le\; \max\{1,b-a\}\; d_{C^k}(f,g).
	\]

	\medskip
```

## CP-IV-0101


- chapter line: 8289
- atlas source solution flag: `unknown`
- linked source-solution candidates: `none`
- embedded solution marker in problem body: `YES`

```tex
\par\noindent\textbullet\quad (\textbf{Wirtinger derivatives})
	For $T(z)=Az+B\bar z$, compute $\partial T/\partial z$ and $\partial T/\partial\bar z$.
	\emph{Solution.} $\displaystyle \frac{\partial T}{\partial z}=A,\qquad \frac{\partial T}{\partial\bar z}=B$.
```

## CP-IV-0103


- chapter line: 8296
- atlas source solution flag: `unknown`
- linked source-solution candidates: `none`
- embedded solution marker in problem body: `YES`

```tex
\par\noindent\textbullet\quad (\textbf{Matrix from $A,B$})
	Given $T(z)=Az+B\bar z$ with $A=\alpha+i\beta$, $B=\gamma+i\delta$ ($\alpha,\beta,\gamma,\delta\in\mathbb{R}$), show the real matrix is
	\[
	\begin{pmatrix}
		\alpha+\gamma & -\beta+\delta\\
		\beta+\delta & \alpha-\gamma
	\end{pmatrix}.
	\]
	\emph{Solution.} Expand $Az+B\bar z$ with $z=x+iy$ and collect $(x,y)$ coefficients.
```

## CP-IV-0105


- chapter line: 8336
- atlas source solution flag: `unknown`
- linked source-solution candidates: `none`
- embedded solution marker in problem body: `NO`

```tex
Show that the following functions do not have antiderivatives on the indicated domains:
\[
\text{(a)}\; f(z)=\frac{1}{z}-\frac{1}{z-1}\quad\text{on } \{\,0<|z|<1\,\},\qquad
\text{(b)}\; g(z)=\frac{z}{1+z^{2}}\quad\text{on } \{\,1<|z|<\infty\,\}.
\]
```

## CP-IV-0108


- chapter line: 8345
- atlas source solution flag: `unknown`
- linked source-solution candidates: `none`
- embedded solution marker in problem body: `NO`

```tex
Let $T:\mathbb{R}^2\to\mathbb{R}^2$ be a real-linear map. Regard $T$ as a map $\mathbb{C}\to\mathbb{C}$ via $(x,y)\leftrightarrow x+iy$.
	Show that there exist unique $A,B\in\mathbb{C}$ such that
	\[
	T(z)=Az+B\overline{z}\qquad(\forall\,z\in\mathbb{C}),
	\]
	and that $T$ is complex differentiable (i.e.\ $\mathbb{C}$-linear) iff $B=0$.
```

## CP-IV-0115


- chapter line: 8470
- atlas source solution flag: `unknown`
- linked source-solution candidates: `none`
- embedded solution marker in problem body: `NO`

```tex
Take
	\[
	a = 0.5 + 0.2i, \qquad \theta = \frac{\pi}{4},
	\]
	and define
	\[
	\phi(z) = \phi_{a,\theta}(z)
	= e^{i\pi/4}\,\frac{z-a}{1-\overline{a}\,z}.
	\]
	Then $\phi(a)=0$, and $\phi$ maps $\mathbb D$ onto itself while
	distorting the radial/circular grid in a non-trivial way.

	Figures~\ref{fig:disk-auto-z} and \ref{fig:disk-auto-w} show the unit
	disk and its image under $\phi$.
```

## CP-IV-0119


- chapter line: 8502
- atlas source solution flag: `unknown`
- linked source-solution candidates: `none`
- embedded solution marker in problem body: `NO`

```tex
(Conjugation).

Let $T(z)=\bar z$. Then $A=0$, $B=1$.
The unit circle is fixed as a set, but orientation is reversed. $T$ is not complex-differentiable since $B\neq0$.
```

## CP-IV-0120


- chapter line: 8510
- atlas source solution flag: `unknown`
- linked source-solution candidates: `none`
- embedded solution marker in problem body: `NO`

```tex
\par\noindent\textbullet\quad \textbf{Total boundedness still fails (infinite dimension).}

	Closed balls in $(C^k,d_{C^k})$ are complete but not totally bounded.
	For instance, translate a fixed bump function to disjoint locations;
	the resulting family lies in the unit ball and remains pairwise well separated.
```

## CP-IV-0121


- chapter line: 8519
- atlas source solution flag: `unknown`
- linked source-solution candidates: `none`
- embedded solution marker in problem body: `NO`

```tex
Compute $\displaystyle \int_{0}^{2\pi} e^{\,e^{it}}\,dt$.

Let $z=e^{it}$ so that $|z|=1$ and $dt=\frac{dz}{iz}$. Then
\[
\int_{0}^{2\pi} e^{e^{it}}\,dt
=\frac1i\oint_{|z|=1}\frac{e^{z}}{z}\,dz.
\]
By Cauchyâ€™s integral formula for $f(z)=e^{z}$,
\[
\oint_{|z|=1}\frac{e^{z}}{z}\,dz=2\pi i\,f(0)=2\pi i.
\]
Hence
\[
\boxed{\displaystyle \int_{0}^{2\pi} e^{\,e^{it}}\,dt=2\pi }.
\]

Since $e^{e^{it}}=\sum_{n=0}^\infty \frac{e^{int}}{n!}$, the integral over $[0,2\pi]$
kills all terms with $n\neq0$ and equals $2\pi$.
```

## CP-IV-0122


- chapter line: 8541
- atlas source solution flag: `unknown`
- linked source-solution candidates: `none`
- embedded solution marker in problem body: `NO`

```tex
\par\noindent\textbullet\quad $U=(0,1)\cup(2,3)$.
```

## CP-IV-0127


- chapter line: 8575
- atlas source solution flag: `unknown`
- linked source-solution candidates: `none`
- embedded solution marker in problem body: `NO`

```tex
\par\noindent\textbullet\quad \textbf{Concrete identity.}

	With $f(x)=\sin x$ on $[0,1]$,
	\[
	T(f)(x)=\int_0^x\sin y\,dy = 1-\cos x,
	\]
	so $D(T(f))=f$, while $D(f)=\cos x$ and
	\[
	T(D(f))(x)=\int_0^x \cos y\,dy=\sin x=f(x).
	\]
```

## CP-IV-0130


- chapter line: 8614
- atlas source solution flag: `unknown`
- linked source-solution candidates: `none`
- embedded solution marker in problem body: `NO`

```tex
\par\noindent\textbullet\quad \textbf{Derivative map is $1$-Lipschitz $C^{k+1}\!\to C^{k}$.}

	For $f,g\in C^{k+1}$ we have
	\[
	d_{C^{k}}(f',g')
	=\sum_{j=0}^{k} \|f^{(j+1)}-g^{(j+1)}\|_\infty
	\;\le\;
	\sum_{j=0}^{k+1} \|f^{(j)}-g^{(j)}\|_\infty
	= d_{C^{k+1}}(f,g).
	\]

	\medskip
```

## CP-IV-0132


- chapter line: 8663
- atlas source solution flag: `unknown`
- linked source-solution candidates: `none`
- embedded solution marker in problem body: `NO`

```tex
$f_n(x)=\arctan(nx)$ (each UC) $\to$ a step function, which is not UC.
```

## CP-IV-0136


- chapter line: 8668
- atlas source solution flag: `unknown`
- linked source-solution candidates: `none`
- embedded solution marker in problem body: `NO`

```tex
â€” gradient field (curl $=0$), circulation $=0$

Let $\phi(x,y)=x^2+y^3$ and $\mathbf F=\nabla\phi=(2x,\,3y^2)$.
Then
\[
M_x - L_y
=
\partial_x(3y^2)-\partial_y(2x)
=
0-0
=
0,
\]
so
\[
\oint_{C} (2x\,dx+3y^2\,dy)
=
\iint_{D} 0\,dA
=
0.
\]
\emph{Interpretation:} exact/gradient fields do no net work around closed curves.
```

## CP-IV-0060


- chapter line: 8733
- atlas source solution flag: `unknown`
- linked source-solution candidates: `none`
- embedded solution marker in problem body: `NO`

```tex
(Weierstrass data for catenoid and helicoid)

We use the Weierstrass representation in the $(f,g)$-form:
	\[
	X(z)=\Re\int^z \Big(\tfrac12 f(1-g^2),\ \tfrac{i}{2}f(1+g^2),\ fg\Big)\,dz,
	\]
	where $g$ is meromorphic, $f$ is holomorphic, and the resulting parametrization is conformal and minimal.

	\medskip
	\textbf{Choice of complex parameter.}
	For the given real parameters $(u,v)$, the catenoid/helicoid are conformal in $(u,v)$, and it is convenient to set
	\[
	z=v+iu.
	\]
	Thus a suitable domain is the strip
	\[
	D=\{z=v+iu\in\mathbb{C}:\ v\in\mathbb{R},\ 0<u<2\pi\}.
	\]

	\medskip
	\textbf{Catenoid.}
	Take
	\[
	g(z)=e^{z},\qquad f(z)=a e^{-z}.
	\]
	Then
	\[
	\tfrac12 f(1-g^2)=\frac{a}{2}(e^{-z}-e^{z})=-a\sinh z,\qquad
	\tfrac{i}{2}f(1+g^2)=\frac{ia}{2}(e^{-z}+e^{z})=i a\cosh z,
	\]
	and $fg=a$. Hence
	\[
	X(z)=\Re\bigl(-a\cosh z,\ i a\sinh z,\ a z\bigr).
	\]
	With $z=v+iu$ this becomes (up to a rigid motion in the $xy$-plane)
	\[
	X(u,v)=\bigl(a\cosh v\cos u,\ a\cosh v\sin u,\ a v\bigr),
	\]
	which is exactly the given catenoid parametrization (possibly after rotating by $\pi$ about the $z$-axis).

	\medskip
	\textbf{Helicoid.}
	Keep the same $g(z)=e^{z}$ but replace $f$ by $if$:
	\[
	g(z)=e^{z},\qquad f(z)= i a e^{-z}.
	\]
	This is the classical associate surface construction. Substituting yields a parametrization which, after a rigid motion
	and a harmless shift of $u$, is the given helicoid
	\[
	\phi(u,v)=\bigl(a\sinh v\cos u,\ a\sinh v\sin u,\ a u\bigr).
	\]
	(Geometrically: multiplying $f$ by $i$ rotates the Weierstrass integrand by $90^\circ$ in the associate family.)

	\bigskip
```

