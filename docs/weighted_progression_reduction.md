# Exact reduction of the enlarged weighted progression contract

This is a new written finite identity for the weight in the randomized
manuscript (Section "The weighted progression obligation"). It does not
prove the asymptotic estimate or the enlarged conditional laws.

Write \(h=4u-1\), \(F=(4u)!\), and let \(P(\mathbf p)=\prod_{i=1}^h p_i\)
for ordered tuples from \(\mathcal P(y)^h\), repetitions allowed. Use \(m\)
for the progression modulus and \(k\) for the free integer factor. Put
\(A=z_0-mR\), \(B'=z_0+mR\) and define the integer endpoints
\[
 a_P=\max(\lfloor y/2\rfloor+1,\lceil A/P\rceil),\qquad
 b_P=\min(\lfloor y\rfloor,\lfloor B'/P\rfloor).
\]
When \(a_P>b_P\), the contribution is zero. For other tuples put
\(g=\gcd(P,m)\). If \(g\nmid z_0\) their contribution is again zero.
Otherwise the congruence \(Pk\equiv z_0\bmod m\) is equivalent to
\(k\equiv r_P\bmod (m/g)\), where \(r_P\) is the product of \(z_0/g\) and
the inverse of \(P/g\) modulo \(m/g\). For \(m/g=1\), choose \(r_P=0\).

Consequently the unnormalized sum of weights is exactly
\[
 \sum_{t=-R}^R\widetilde w_{y,u}(z_0+mt)
 = \frac1F\sum_{\substack{\mathbf p\\a_P\le b_P\\g\mid z_0}}
 \left(
 \left\lfloor\frac{b_P-r_P}{m/g}\right\rfloor
 -\left\lfloor\frac{a_P-1-r_P}{m/g}\right\rfloor
 \right).
\]
Proof: expand the definition of the weight, interchange the two finite
sums, and observe that the free factor uniquely determines \(t\) when
\(Pk\) lies in \([A,B']\) and has residue \(z_0\bmod m\). The floor
difference counts all possible \(k\), including the endpoints.

## Simplification in the stated range

For \(y\ge2^{100}\) and \(\gcd(z_0,m)\le y^{3/10}\), any contributing tuple
must have \(\gcd(P,m)=1\). Indeed a prime dividing both \(P\) and \(m\)
would divide \(z_0\) as well, but is larger than \(y/2>y^{3/10}\).
Thus all the contributing progression moduli for the free factor are
exactly \(m\), not a divisor of it.

Writing \(\ell_P=\max(0,b_P-a_P+1)\), the floor difference differs from
\(\ell_P/m\) by strictly less than one. Let \(C\) count ordered tuples
with \(\gcd(P,m)=1\) and \(\ell_P>0\). Then
\[
 \left|\frac{\sum_{t=-R}^R\widetilde w_{y,u}(z_0+mt)}{2R+1}
 - \frac{\sum_{\mathbf p:\gcd(P,m)=1}\ell_P}{F m(2R+1)}\right|
 \le \frac{C}{F(2R+1)}.
\]
The weak inequality covers the empty case as well.

## What is still needed

This identity isolates, rather than disposes of, the genuinely analytic
error: termwise rounding can be much larger than the required relative
error \(e^{-27\ell^2}\nu(z_0;y,u)\) in the large-modulus regime. The
remaining task is to control the aggregate discrepancy uniformly in the
actual tuned range, with nontrivial cancellation or a different counting
argument, and to compare the main term with the density \(\nu\), including
boundary intervals and removal of primes dividing \(m\). A fixed zero-free
half-plane for Dirichlet L-functions is helpful but is not itself a proof of
any of these uniform estimates. In particular it cannot by itself certify
that all exceptional sets in the weighted large-sieve argument are empty.

The conditional polynomial-slice coupling, local moments, all-history
readiness, and square-certification requirements remain independent proof
obligations. No substitution of axioms for these missing results is made.
