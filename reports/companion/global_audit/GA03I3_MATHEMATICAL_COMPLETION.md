# GA-03i.3 — Mathematical completion of four editorial gaps

The arguments below are mathematical audit notes, not yet modifications to canonical problems.
All four issues require a separate editorial decision before insertion into Part V.

### Connecting-map naturality
Consider a commutative morphism from a short exact sequence
\(0\to C'\xrightarrow{\alpha}C\xrightarrow{\beta}C''\to0\)
to \(0\to D'\xrightarrow{\alpha'}D\xrightarrow{\beta'}D''\to0\),
with chain maps \(a,b,c\) in the three columns. For a homology class
\([z'']\in H_n(C'')\), choose \(z\in C_n\) with \(\beta(z)=z''\).
The top connecting class is represented by \(z'\) such that
\(\alpha(z')=d_Cz\). Commutativity yields
\[
\alpha'(a(z'))=b(\alpha(z'))=b(d_Cz)=d_D(b(z)),
\qquad \beta'(b(z))=c(z'').
\]
Thus the bottom connecting map applied to \([c(z'')]\) is represented
by \(a(z')\), proving
\[
\boxed{H_{n-1}(a)\circ\partial_n
=\widetilde{\partial}_n\circ H_n(c).}
\]
The statement is independent of choices because both connecting
homomorphisms are well defined.

### Ext variance and connecting maps
For fixed \(M\), the covariant cohomological functor
\(\operatorname{Ext}_R^i(M,-)\) sends
\(0\to A'\to A\to A''\to0\) to a long exact sequence with
\[
\operatorname{Ext}_R^i(M,A)\to
\operatorname{Ext}_R^i(M,A'')\xrightarrow{\delta^i}
\operatorname{Ext}_R^{i+1}(M,A')\to
\operatorname{Ext}_R^{i+1}(M,A).
\]
For fixed \(N\), the contravariant functor
\(\operatorname{Ext}_R^i(-,N)\) yields, for the same short exact
sequence of modules,
\[
\operatorname{Ext}_R^i(A,N)\to
\operatorname{Ext}_R^i(A',N)\xrightarrow{\delta^i}
\operatorname{Ext}_R^{i+1}(A'',N)\to
\operatorname{Ext}_R^{i+1}(A,N).
\]
Both long exact sequences are natural in morphisms of short exact
sequences. For commutative rings these constructions are valid in the
usual module category (and with appropriate left/right module
conventions more generally).

### Chain homotopy versus naturality
A chain homotopy \(f-g=d_Dh+hd_C\) implies that for every cycle
\(z\), \((f-g)(z)=d_Dh(z)\), so \(H_n(f)=H_n(g)\).
This fact does not, by itself, prove the commuting identity for
connecting homomorphisms. Connecting-map naturality requires a
commutative diagram of *short exact sequences of complexes* and the
lift-and-boundary argument above. The two facts serve different
functorial purposes.

### Inverse limits and completion
For a short exact sequence of inverse systems
\(0\to A_n\to B_n\to C_n\to0\), taking inverse limits gives
\[
0\to\varprojlim A_n\to\varprojlim B_n\to\varprojlim C_n,
\]
but the final map need not be surjective. For ordinary countable
towers the derived-limit exact sequence continues
\[
\varprojlim B_n\to\varprojlim C_n\to
\varprojlim{}^1 A_n\to\varprojlim{}^1 B_n\to\cdots.
\]
A Mittag--Leffler condition on \((A_n)\), such as surjective
transition maps, ensures \(\varprojlim{}^1 A_n=0\) and hence
surjectivity of \(\varprojlim B_n\to\varprojlim C_n\).
For completion of finitely generated modules over a Noetherian ring,
Artin--Rees gives the cofinality needed to compare induced and
intrinsic filtrations; this is distinct from asserting that inverse
limits are always exact.

