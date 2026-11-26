# Quasi-RH route to polylogarithmic witnesses

**Status:** written proof conditional on the externally comparator-accepted
Dirichlet/zeta seven-eighths theorem. The analytic estimates and algorithmic
bit-cost transfer below are not yet Lean-verified in this repository.
This is a new alternative to the sparse Gram witness search, not a change
to the published manuscript theorem or an unconditional general factorer.

## 1. A uniform interior log-derivative estimate

Fix \(7/8<\sigma_0<1\). Assume that for every positive modulus \(q\) and
nonprincipal character \(\chi\bmod q\), \(L(s,\chi)\ne0\) for
\(\Re s>7/8\), and the corresponding zeta statement. Then, uniformly in
\(q,\chi,t\) and \(\sigma_0\le\sigma\le2\),
\[
 |L'/L(\sigma+it,\chi)|\ll_{\sigma_0}\log(q(|t|+4)).
 \tag{1}
\]
Here no primitivity assumption or restriction on the size of \(q\) is
needed. This estimate is not an immediate logical consequence of abstract
nonvanishing alone: the growth bounds and Euler product used below matter.

For a nonprincipal character, its sum over a period is zero. Its partial
sum \(A(u)=\sum_{n\le u}\chi(n)\) has absolute value at most \(q\).
For \(\Re s>0\), partial summation gives the analytic continuation
\[
 L(s,\chi)=s\int_1^\infty A(u)u^{-s-1}\,du,\qquad
 |L(s,\chi)|\le q|s|/\Re s .
\]
The integral converges locally uniformly in this half-plane and agrees
with the usual Dirichlet series where \(\Re s>1\).

Choose fixed radii \(2-\sigma_0<r<R<2-7/8\).
The disc about \(2+it\) of radius \(R\) is zero-free. There is a holomorphic
logarithm \(g\) of \(L\) on that disc, normalized at the centre by the
absolutely convergent Euler-product logarithm
\[
 g(2+it)=\sum_p\sum_{k\ge1}\chi(p)^k/(k p^{k(2+it)}).
\]
Thus \(|g(2+it)|\le\log\zeta(2)\); everywhere on the disc
\(\Re g=\log|L|\ll\log(q(|t|+4))\), by the previous integral bound.
Borel–Carathéodory on the radii \(r,R\), followed by Cauchy's derivative
estimate on discs of radius smaller than \(r-(2-\sigma_0)\), proves (1).
All implied constants are independent of the character and its modulus.

For zeta apply the same argument to \(F(s)=(s-1)\zeta(s)\), analytic and
nonzero throughout \(\Re s>7/8\), including \(s=1\) by the residue-one
pole. The formula
\[
 F(s)=s-s(s-1)\int_1^\infty\{u\}u^{-s-1}\,du
\]
bounds \(|F(s)|\) polynomially in \(|t|+4\) on those discs.
The logarithm at the centre is the Euler-product logarithm of zeta plus
the principal logarithm of \(1+it\), of magnitude \(O(\log(|t|+4))\).
Hence
\[
 \left|\zeta'/\zeta(s)+1/(s-1)\right|
 \ll_{\sigma_0}\log(|t|+4),\qquad
 \sigma_0\le\Re s\le2,\ s\ne1.
 \tag{2}
\]
These arguments need only standard complex analysis, the partial-sum
integrals, and the canonical Dirichlet Euler products. They also give the
uniform log-derivative input to a corrected truncated Perron proof of
the deterministic manuscript's Lemma 9.2-type estimate, without an
exceptional-zero classification. In a rectangle including the principal
pole one must explicitly separate its polar contribution.

## 2. A smoothed prime-power sum, with no exceptional conductor

Let \(x\ge2\), and
\[
 S_\chi(x)=\sum_{n\le x}\Lambda(n)\chi(n)(1-n/x).
\]
For a nonprincipal character of modulus \(q\), absolute convergence on
the line \(\Re s=2\) gives
\[
 S_\chi(x)=\frac1{2\pi i}\int_{2-i\infty}^{2+i\infty}
          -\frac{L'}{L}(s,\chi)\frac{x^s}{s(s+1)}\,ds .
 \tag{3}
\]
Indeed the Mellin kernel \(1/(s(s+1))\) inverts to
\((1-y)_+\) at \(y=n/x>0\), including its continuous value zero at \(y=1\).
This follows directly by moving the contour to the left for \(y<1\)
(residues at 0 and -1) and to the right for \(y>1\), or by Mellin
transforming the compactly supported weight. The integral and series on
the line 2 can be interchanged by the absolutely summable majorant
\(\sum_n\Lambda(n)n^{-2}\int_{\mathbb R}|(2+it)(3+it)|^{-1}dt\).

Shift (3) to \(\Re s=\sigma_0\). There are no poles in the strip.
At heights \(\pm T\), (1) bounds the horizontal integrals by
\(O_{\sigma_0}(x^2\log(q(T+4))/T^2)\), which tends to zero for fixed
\(x,q\). The vertical integral is bounded absolutely, because
\(\int_{\mathbb R}\log(|t|+4)/(1+t^2)\,dt<\infty\).
Consequently
\[
 |S_\chi(x)|\ll_{\sigma_0}x^{\sigma_0}\log(q+2).
 \tag{4}
\]
For the sum with every character coefficient replaced by 1, use (2)
and the zeta logarithmic derivative. Shifting crosses precisely the
pole at 1 with residue \(x/2\), giving
\[
 S_{\rm all}(x)=x/2+O_{\sigma_0}(x^{\sigma_0}).
 \tag{5}
\]
In (4) the character may be imprimitive: both the partial-sum argument
and the zero-free theorem are for the actual modulus \(q\). This avoids
any missing Euler-factor correction.

## 3. Least character-detecting prime

Suppose every prime \(p\le x\) coprime to \(q\) has \(\chi(p)=1\).
Multiplicativity shows that the difference between (5) and (4) arises
only from prime powers of primes dividing \(q\). Since the weight is
between zero and one,
\[
 |S_{\rm all}(x)-S_\chi(x)|
 \le \sum_{p\mid q,\ p\le x}
   \log p\left\lfloor\frac{\log x}{\log p}\right\rfloor
 \le \frac{\log q\,\log x}{\log2}.
\]
Together (4) and (5) would imply
\[
 x/2\ll_{\sigma_0}x^{\sigma_0}\log(q+2)+\log q\log x.
 \tag{6}
\]
For any fixed \(\varepsilon>0\) choose \(\sigma_0>7/8\) so close to
\(7/8\) that \((8+\varepsilon)(1-\sigma_0)>1\).
Set \(x=(\log(q+2))^{8+\varepsilon}\). Dividing the right side of
(6) by \(x\) gives \(o(1)\) as \(q\to\infty\), a contradiction.
For the finitely many small moduli, the existence of a detecting prime
follows already from nonprincipality: take a positive integer representative
of a unit at which the character is not 1 and factor it, so some prime
factor is coprime to \(q\) and has value not 1. Absorb those moduli into
the constant. Therefore
\[
 \boxed{\min\{p\ {\rm prime}:p\nmid q,\ \chi(p)\ne1\}
      \ll_\varepsilon(\log(q+2))^{8+\varepsilon}}
 \tag{7}
\]
uniformly over nonprincipal characters. For quadratic characters the
witness has value -1. The proof is effective in principle, but the
algorithm below does not need a computed cutoff.

## 4. Consequences for two promised-input algorithms

* Prime nonresidue: on odd prime input \(p\), enumerate the positive
  integers and evaluate Euler's criterion modulo \(p\) by binary
  exponentiation. By (7) a nonresidue occurs within
  \(O_\varepsilon((\log p)^{8+\varepsilon})\) trials. Each trial uses
  \(O(\log p)\) modular multiplications of \(O(\log p)\)-bit residues.
  The resulting polynomial bit-complexity replaces the earlier
  subexponential bound, conditional on the QRH theorem. Handle \(p=2\)
  separately according to the nonresidue problem's usual odd-prime
  promise.

* Supplied-order splitting: use the existing exact scalar scan
  (Factoring.Miller.scanM); no factorization or character is supplied to
  the algorithm. Remove even inputs and perfect powers by the standard
  preliminary operations. Let \(p,q\) be two distinct hidden odd prime
  divisors of the remaining composite \(N\); assume the supplied positive
  exponent \(M\) is divisible by \(p-1,q-1\) (the manuscript's stronger
  universal promise suffices). Enumerate positive integers \(a<N\),
  computing \(\gcd(a,N)\) first, then the scalar scan with the supplied
  exponent. If the two 2-adic valuations of \(p-1,q-1\) agree, use the
  nonprincipal quadratic character \((\cdot/p)(\cdot/q)\) modulo \(pq\)
  in (7). A detecting prime is a unit at both and gives opposite Euler
  signs; swap their names if needed. The verified mixed_equal_success
  theorem gives a factor. If the valuations differ, call the larger one
  \(q\); use the nonprincipal quadratic character modulo \(q\). Its
  detecting prime either immediately gives a proper gcd or is a unit
  at \(p\), so nonsquare_larger_success gives a factor. A prime
  detecting a character modulo \(pq\) or \(q\) can always be chosen
  below \(N\) by the representative argument above, even for small
  inputs. All detecting-character moduli are at most \(N\).
  Thus the scan needs at most
  \(O_\varepsilon((\log N)^{8+\varepsilon})\) trials, with polynomial
  bit cost per trial in \(\log N,\operatorname{len}(M)\). It never
  computes the character on the hidden primes.

These arguments prove polynomial-time *promised-input* constructions
once the fixed QRH result and the indicated arithmetic facts are
accepted. They do not construct the common exponent \(M\) for arbitrary
\(N\) and therefore do not give a general polynomial-time factorer.
The full randomized descent still requires its other distribution and
square-certification contracts.

## Formalization tasks

The source-level QRH adapters are in lean-qrh. To make (1)–(7) a
certified improvement, formalize the partial-sum continuation/growth,
holomorphic logarithm with Euler normalization, interior derivative
bound, weighted Mellin inversion, absolutely convergent contour shift,
and the elementary prime-power contradiction. Then link the latter to
the actual mathlib Dirichlet characters from Legendre symbols and to the
already verified scalar supplied-exponent scan, and give a concrete
bit-cost model for modular exponentiation, gcd and the sequential
enumeration. A separate modern toolchain is currently used for QRH,
so this final linkage is not yet a kernel-checked theorem.
