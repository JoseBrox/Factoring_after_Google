# Adversarial field parameters for the bounded rank-one search

**Status (26 November 2026): proved negative result for uniformity
over the choice of the field parameter C.** This does not refute
coverage for the canonical least-C construction, nor the existence
of a good C in a suitable enumerated family. It identifies an actual
obstruction that the desired uniform success proof must avoid.

This continues [the 2-adic quadratic extraction](padic_rank_one_extraction.md).
The key improvement over merely choosing C divisible by all primes
below a bound is to use the finite list's **pairwise resultants**.
Neither the resultants nor the mark norms need to be factored.

## 1. The theorem

Fix odd N>=3, an odd prime ell coprime to N, a=(ell-1)/2,
and a finite list of nonzero integer polynomials g_j with g_j(0)=1.
Assume the list is selected independently of C and that
\[
 \gcd(g_j(2(\ell+1)),N)=1
 \qquad\text{for every }j.                                \tag{1}
\]
Adjoin the special mark h_*=1+aX, which also satisfies (1)
because h_*(2(ell+1))=ell^2.

There is a deterministically constructible positive integer C
with all the original quadratic field guards
\[
 C\equiv-4\bmod N,\quad v_2(C)=1,\quad
 \ell^2\mid C,\quad C\ge(16(1+\ell))^{20},
\]
for which the following holds. In the real quadratic field
\[
 f_C(X)=(X-2)^2+C(1+aX),\qquad f_C(\theta)=0,
\]
**every product of the listed marks with integral exponents
whose ideal valuations vanish is exactly 1.**

Thus the entire mark list fails the rank-one transverse-unit
criterion for this admissible field. The construction of C has
polynomial bit complexity in the total description length of
the mark list, log N and log ell. In particular, if the list
is an explicitly enumerated half-scale family of bounded-degree
polynomials, this adverse parameter can also be constructed
within the half-scale budget (although its individual bit
length need not be polynomial in log N).

## 2. Gcd-free polynomial basis

Refine the list, including h_*, into pairwise coprime
nonconstant polynomials h_i in Z[X], each of constant
coefficient 1, with exact nonnegative exponent vectors
expressing all original marks as their products.

This needs no integer polynomial factorization. Whenever two
active factors have a nonconstant gcd, split them by that gcd,
using Gauss's lemma and normalizing its constant to 1. Merge
equal factors and add their exponent rows; discard factors
equal to 1. All divisors have constant coefficient ±1, so this
normalization is integral. The sum of degrees of the active
factors strictly decreases at a nontrivial split: replacing
h,p by h/g,g,p/g decreases the sum by deg g. The number of
operations is at most the total original degree. Every new
factor divides an original polynomial, so the standard Mahler
measure coefficient bound gives polynomial bit heights.
Polynomial gcd and exact division have polynomial bit
complexity in the input sizes.

The final list contains h_* itself, since it is linear.
Every other h_i is coprime to h_*. Every h_i satisfies (1)
because its evaluation divides an original mark evaluation.
Also h_i(2) is odd and nonzero, because h_i(0)=1.

## 3. Choose C using the pairwise resultants

Form the positive integer
\[
 R=\ell\prod_{i<j}|\operatorname{Res}(h_i,h_j)|.
\]
Every resultant is nonzero by the gcd-free property. Remove
all prime-power factors supported on 2N by repeatedly
dividing R by gcd(R,2N) until the gcd is one. Denote the
result by R_0. It is odd, coprime to N, and still divisible
by ell. This stripping uses only gcd and exact division,
not the unknown factorization of N.

Choose an integer K with
\[
 2^K>\max_i |h_i(2)|^2.
\]
Use CRT to take C a multiple of \(2\ell^2 R_0^K\), with
C/2 odd and C≡-4 mod N. An odd multiplier in the required
residue class exists since N is odd and the base multiple
is coprime to N. Increasing it by 2N lets us meet any
specified lower bound on C.

For each nonexceptional h_i, consider the integer polynomial
\[
 P_i(Z)=\operatorname{Res}_X((X-2)^2+Z h_*(X),h_i(X)).
\]
It has degree deg h_i with nonzero leading coefficient:
over a splitting field each root beta of h_i contributes
(beta-2)^2+Z h_*(beta), and h_*(beta)!=0 by coprimality.
Moreover P_i(0)=h_i(2)^2.

We can compute P_i by evaluating at deg h_i+1 distinct
integer values of Z and interpolating exactly. Its coefficients
have polynomial bit lengths in the given data (also directly
from the Sylvester determinant). If P_i has coefficients
A_0,...,A_s with A_s nonzero, then
\[
 |P_i(C)|\ge C^s-C^{s-1}\sum_{j<s}|A_j|
 \quad(C\ge1).
\]
Thus a computable lower bound on C ensures
\[
 |P_i(C)|>|h_i(2)|^2
 \qquad\text{for all }h_i\ne h_* .                        \tag{2}
\]
Use the maximum of these lower bounds and the earlier
explicit real-root bound. This completes the field
construction. The original proofs of monicity, real roots,
Eisenstein irreducibility and integral norm-one unit
\(u=h_*(\theta)/\ell\) apply.

The bit length of R is polynomial in the total list
description: there are quadratically many pairs, each
resultant has polynomial bit length. The exponent K is
polynomial in the individual polynomial sizes. The chosen
C, obtained from the least suitable CRT multiple above the
lower bound, also has polynomial bit length in the total
list size. Every operation has the stated cost. No claim
is made that this deliberately adverse C is the smallest
permitted C in the original construction.

## 4. Every nonexceptional factor has a private ideal

Write \(A_i=|\operatorname{Norm}h_i(\theta)|=|P_i(C)|\)
for the absolute norms.

For every prime p|R_0,
\[
 P_i(C)\equiv h_i(2)^2\bmod p^K .
\]
Since \(v_p(h_i(2)^2)<K\), it follows exactly that
\[
 v_p(A_i)=2v_p(h_i(2)).
\]
The part of A_i supported on the primes dividing R_0 is
therefore at most |h_i(2)|^2. By (2), for every
nonexceptional h_i there is a rational prime p|A_i
not dividing R_0.

Also A_i is odd: f_C mod 2 is X^2 and h_i(0)=1.
Modulo N the defining polynomial is
\[
 f_C(X)\equiv X(X-2(\ell+1))\pmod N .
\]
The resultant identity with this product shows
\[
 \operatorname{Norm}h_i(\theta)
        \equiv h_i(0)h_i(2(\ell+1))
        =h_i(2(\ell+1))\pmod N .
\]
This is a polynomial resultant identity over Z/NZ and
does not require the two roots to be distinct there.
By (1) the norm is coprime to N. Thus the chosen prime
p does not divide 2N and, because p does not divide R_0,
it does not divide R either.

There is at least one actual prime ideal over p
dividing h_i(theta), because p divides its norm.
If that prime ideal also divided another h_j(theta),
the residue of theta would be a common root of h_i,h_j
in its residue field, forcing
\(p\mid\operatorname{Res}(h_i,h_j)\), a contradiction.
This proof is valid also at ramified primes and primes
dividing the power-order index. We do not infer private
prime *ideals* just from rational gcds of the norms.

So every nonexceptional h_i has an isolated prime-ideal
valuation row in the refined mark basis. In any product
with all valuations zero, its coefficient must be zero.
Only h_* remains; its norm is ell^2, so its coefficient
must also be zero. The product is exactly 1.

This proves the theorem, including possible polynomial
factor dependencies in the original mark list. The
refinement is essential: singleton-row elimination on
the original list alone could miss this obstruction.

## 5. Consequences for the original uniform coverage question

For balanced semiprimes N=pq of bit length n, both p,q
have logarithms Omega(n). Suppose ell is polynomially
bounded and we use the usual marks with g(0)=1, degree
at most s and coefficients bounded by H, where
\[
 s\log(2H+1)=O(\sqrt{n\log n}).
\]
Each g(2(ell+1)) is odd and nonzero, and its absolute
logarithm is at most
\[
 O(\log(s+1)+\log H+s\log(2(\ell+1)))=o(n).
\]
Thus (1) holds for all sufficiently large balanced
inputs. The same is true of any finite subset and of
the gcd-free factors, since their evaluations divide
those of the original polynomials.

It follows that for every such N and every polynomially
bounded odd target ell, **there exists an admissible C**
on which this whole predetermined half-scale family
has no transverse unit. This includes separating
targets. The construction is uniform in the mark list
and uses at most polynomial overhead in its explicit
size.

This disproves a positive coverage statement quantified
over *every* C satisfying the algebraic construction
guards. It does **not** disprove the desired theorem
for a specific canonical, polynomial-bit-height C,
a carefully selected parameter distribution, or a
search that generates new marks depending on C.
For polynomial-sized lists the adverse C also has
polynomial bit height; for the full subexponential
list its bit height can be much larger than that of
the canonical choice.

In particular, a proof of uniform success at the
half scale must use meaningful information about
how C is chosen or must generate a C-dependent
descent. The prescribed explicit unit and the
field's real-root/irreducibility conditions alone
cannot imply coverage. Merely using the larger
factor-refinement relation space does not fix this
obstruction.

## 6. Finite exact check

The [adverse-field fixture](../verification/research/adversarial_field.py)
uses N=1000036000099, ell=5, and 21 mark polynomials,
including reducible products. It performs the
gcd-free refinement, computes pairwise resultants,
constructs an admissible C, and certifies the
private support of every nonexceptional factor
by gcd stripping and resultant coprimality.
No norm or resultant is prime-factored.

Exact checked source: Git blob
7cb6c579b2ab195fd999b3bd55d170b1fed9dcf5,
SHA-256
2144500e6ca9f512bf239de8a28bd7909fc45a442e69d3ca779e15ebb875033f.

Observed output:

    mark polynomials 21 gcd-free factors 18 refinements 3
    C bit length 3455 private-support certificates 17 of 17
    all nonexceptional factor exponents forced to zero; remaining norm ell^2 forces trivial unit

This finite check exercises the actual deterministic
construction and its integer certificates. It is not
a test of failure of the canonical C.

The general half-scale success theorem remains open.
The obstruction directs further work towards proving
coverage for a specifically chosen small C or towards
an adaptive, C-dependent mark constructor rather than
assuming that the prescribed algebraic identities
already ensure a nonzero integer kernel image.
