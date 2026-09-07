# Volume III — dependency and notation repair

This professional-review pass makes the logical order of III/01--III/28 explicit.

## Logical spine

```text
III/01 -> III/02 -> III/03 -> III/04 -> III/05
       -> III/06 -> III/07 -> III/08
       -> III/09 -> III/10 -> III/11 -> III/12 -> III/13 -> III/14
       -> III/15 -> III/16 -> III/17 -> III/18 -> III/19
       -> III/20 -> III/21 -> III/22 -> III/23
       -> III/24 -> III/25 -> III/26 -> III/27 -> III/28
```

The graph is not merely linear: each row of `VOL03_PREREQUISITE_GRAPH.tsv`
records the actual earlier chapters used by that chapter.

## Source-level dependency repairs

### III/09 -> III/10

The Dirichlet-kernel discussion previously used approximate-identity terminology
before the formal approximate-identity chapter. The terminology is now explicitly
marked as a preview; the III/09 argument is stated to depend only on its local
kernel representation and oscillatory analysis.

### III/11 -> III/14

Fourier inversion uses Schwartz functions before the dedicated Schwartz-space
chapter. III/11 now contains the local rapid-decay definition needed for that
result and explicitly defers the full seminorm topology to III/14.

### III/13 -> III/14

The Plancherel extension uses Schwartz functions as a dense core. III/13 now
states that convention locally and identifies density as the standard
cutoff-and-mollification core lemma, rather than silently importing III/14.

## Cross-part prerequisite policy

- Fubini/Tonelli precede convolution and transform interchange.
- Lp structure precedes Holder/Minkowski and all subsequent norm estimates.
- Convolution/approximate identities precede the general Fourier-transform calculus.
- The transform normalization is fixed in III/11 and inherited thereafter.
- Schwartz space is formalized before tempered distributions.
- Test-function topology precedes distributions.
- Distributions precede weak derivatives and fundamental solutions.
- Weak derivatives and Lp spaces precede Sobolev spaces.
- Sobolev and density machinery precede weak boundary-value problems.
- Fundamental solutions precede Green-function constructions.
- Spectral/transform PDE methods are the terminal synthesis chapter.

## External theorem policy

External standard machinery is named rather than hidden. In particular the graph
records Riesz/Hilbert-space input for Lax--Milgram, ODE and regular
Sturm--Liouville background, domain extension machinery, and the Hilbert spectral
theorem where those results are used rather than developed from first principles.

## Result

Audit status: **PASS**.
