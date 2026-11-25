# Deterministic exponent extraction and the revised end-to-end schedule

25 November 2026. This note records the algebraic and finite-algorithm part of the audit of the deterministic paper at Google Research commit `4a7bc8ab0bc770e71a259b7966c500496b99010a`, PDF blob `973002e0eb92acf3964fc020ca52ba6f1ac384ac`. It is read together with `deterministic-analytic-audit.md` and the separate supplied-order splitting audit. The source is cited by lemma and page; no formal proof assistant certification is claimed.

## 1. Exact statement of the exponent-construction result

Fix a rational `0<delta<=1/100`. Put `L=log N` and use

| Quantity | Power of L |
|---|---:|
| Degree d and small-prime cutoff z0 | a=1/3 |
| log(1/w) | t=1/3+delta |
| log K1 | k=1/3+2delta |
| Reciprocal zero-free width nu0^(-1) | v=1/3+5delta/2 |
| log B | b=1/3+3delta |
| log zBr and the clean-error power | j=1/3+4delta |
| Smoothness quotient u | r=1/3+5delta |
| log A | c=1/3+6delta |
| log U and log Xsc | h=2/3+8delta |

Use exact dyadic/integer-root rounding as in Section 8.2 of the source. In particular, `d=floor(L^(1/3))+O(1)`, `m=ceil(N^(1/d))`, and `log m=(1+o(1))L^(2/3)`. All integer data are computable without a real-number oracle.

The generalized analytic estimates in `deterministic-analytic-audit.md`, combined with the finite construction below, prove this statement: on every sufficiently large odd composite non-perfect-power N, the deterministic search either finds a proper divisor or constructs an even integer M such that

\[
(p-1)\mid M\quad\hbox{for every prime }p\mid N,
\]

in `exp(O_delta(L^h))` bit operations, with

\[
\operatorname{bitlen}(M)
\le \exp\bigl(O_\delta(L^{1-b}\log L)\bigr).
\]

For all finite inputs the same algorithm remains correct by explicit guards and trial-division fallback. The fallback is absent above an effective threshold. Combining this result with an independently justified supplied-order splitter completes a general-factoring complexity theorem; the analytic exponent transfer alone is not a substitute for that last input.

## 2. The base polynomial construction is unchanged

For each generator prime ell in `(B/2,B]`, choose a leading coefficient `cd` supported on the odd primes at most d, as in the source, so that

\[
X_{\rm sc}=c_dA^d\asymp K_1BP_0m\,L^{20}UA.
\]

The leading logarithmic scale is L^h because `h>2/3` and `h>a+c`. Consequently cd is positive and has polynomially many bits; its numerical size is never a loop bound.

Lemma 8.1 constructs two integer polynomials of degree d with the same leading coefficient. Their values at m are nonzero integer multiples of N. One polynomial is split with simple roots modulo ell, and the other has no root there. Modulo 2 both are irreducible. Modulo the odd primorial they equal 1; since all prime factors of cd belong to that primorial, this also proves that their contents are 1. The perturbations

\[
f_{1,u}=f_1^{(0)}+P_0\ell(X-m)(u_0+u_1X),
\qquad
f_{2,v}=f_2^{(0)}+P_0\ell(X-m)(v_0+v_1X)
\]

preserve these exact conditions.

The CRT construction and base-m correction cost `poly(2^d,B,log cd,d log(mA))`. The inequalities `a<b`, `h<1`, and `a+c<h` place this below the total search budget. The base-m correction is not being assumed inexpensive in its numerical modulus: its bit length is what is charged.

Root targeting also transfers. The target roots are equally spaced, and the coefficient perturbation has normalized size at most K1^(-1). Since `k>t>a`, root errors of size K1^(-.95) are much smaller than w, and the product lower bounds at the target endpoints dominate the perturbation. Thus each polynomial has d isolated real roots. Its smooth values have at most `2.1u` prime factors, so the sparse-column cap `1+omega(f1(a))+omega(f2(a))<L0` still holds, with `L0=ceil(log N)`.

The estimate for the factors of `k0 k0'` in the Brun preconditioning remains uniform. These integers have logarithm `O(L^h)` and no prime factor at most d. For delta<=.01 one can retain the original coarse prime cutoff L^.80, giving reciprocal-prime sum `log(.80/(1/3))+o(1)<1.1`. The product of `(1-1/p)` is therefore larger than 1/4. The finer Brun truncation uses `rBr=ceil(L^delta)`, `log zBr=L^j`, and the strict inequality `j+delta<c`.

## 3. Why the unit relation produces a genuine modular exponent

This verifies the role of source Lemma 7.4, including the localization issue.

For the two totally real degree-d fields, let H project the d real logarithms isometrically onto their sum-zero hyperplane. The direct sum of the two unit-log lattices has rank `DU=2d-2`.

A nontrivial totally real unit gamma satisfies

\[
1\le |N(\gamma^2-1)|=\prod_s|\sigma_s(\gamma)^2-1|.
\]

Hence some squared embedding is at least 2, and its logarithmic vector has Euclidean norm greater than 1/3. Minkowski's theorem then gives the explicit lower covolume bound

\[
\det\Lambda_U>(9d)^{-d}.
\]

Collect the common smooth values into a valuation matrix V, with an additional top row of ones. Simple roots modulo factor-base primes identify the relevant degree-one prime ideals exactly. The top row cancels the fixed denominators coming from a nonmonic defining polynomial.

Suppose an integer vector c0 has valuation `-E0` at every prime of the first field above ell and zero elsewhere, including in the second field. Suppose c1,...,cDU have zero valuations and their archimedean images form an invertible matrix MU. Then all these images lie in the same unit lattice. Its sublattice index is the integer

\[
E_1=|\det M_U|/\det\Lambda_U.
\]

For `x=-MU^(-1)u(c0)`, each reduced coordinate denominator divides E1. Let Q be their least common multiple. The resulting integral combination has zero valuations and zero unit logarithms. In each totally real field its associated unit is therefore either +1 or -1.

The modular evaluation is well defined on the localized order

\[
\mathbf Z[c_d^{-1}][\theta_i][(a-\theta_i)^{-1}:a\text{ retained}],
\]

because cd and every a-m are units modulo N. It does not require coprimality between N and the index of the polynomial order in the full ring of integers. Both fields send a-theta_i to the same residue a-m. Dividing their images and squaring therefore yields

\[
\ell^{2E_0Q}\equiv1\pmod N.
\]

This is the exact algebraic reason the two-field construction supplies a useful exponent. A positive Gram matrix is used only to guarantee the required rational valuation solve and the full unit-log span.

## 4. Exact extraction has adequate bit complexity

Source Lemma 7.5 works on finite data and does not assume the unknown factorization of N. Fraction-free pivoting gives a rational nullspace basis with sparse integer columns. Hadamard bounds control their heights. Certified bisection and logarithm approximation compute archimedean vectors with

\[
P_{\rm bit}=64d^3D_{\rm row}L_0
\]

bits of precision. The unit-lattice covolume bound prevents every prospective full-rank minor from being arbitrarily tiny. Greedy Gram-minor selection thus succeeds at the stated precision whenever the full span exists.

Solving in the selected basis approximates x with error less than `1/(2 E1max^2)`. Continued fractions recover its exact coordinate denominators, and their least common multiple divides E1. The algorithm checks both the output-size bound and `ell^Eell=1 mod N` by exact modular arithmetic before accepting an exponent.

Every call costs `poly(A,B,d,Drow,Pbit)`. Since `Drow<=1+2dB`, its logarithmic cost is `O(L^c+L^b)`, which is `o(L^h)`. No exact symbolic logarithm or uncharged algebraic-unit computation occurs in this extractor.

The new Gram audit supplies `lambda_min(Htrue)>>L^(-2h-r)`. Since

\[
2h+r=5/3+21\delta<3,
\]

the existing conservative L^(-3) guard is adequate. The prime-feature covariance error must be absorbed within that block, as detailed in the analytic note; applying a global eigenvalue perturbation estimate would lose this conclusion.

## 5. Generator saturation and total complexity

The clean-prime theorem supplies at least `B/(6 log B)` successful generator primes. Take the least common multiple Mstar of their verified exponents. For any hidden prime p dividing N, let G be the subgroup of Fp* generated by those small rational primes. Products of k such generators, where `k=floor(log(p-1)/log B)`, are distinct integers below p and hence distinct group elements. Consequently

\[
|G|\ge(B/(6L))^k,
\qquad
[\mathbf F_p^*:G]\le B\exp\{(L/\log B)\log(6L)\}.
\]

Let Kidx be the explicit dyadic upper bound on the latter expression. Multiplying Mstar by `lcm(1,...,Kidx)` produces M with every p-1 dividing M. This saturation argument only uses unique factorization of ordinary positive integers and cyclicity of Fp*.

The exponent bit length is dominated by

\[
K_{\rm idx}=\exp\bigl(O(L^{1-b}\log L)\bigr),
\]

since b<1/2. A finite integer output cap with bit-length exponent `1-b+delta` is sufficient. It is smaller than the main search exponent because `1-b+delta<h`.

There are at most

\[
16B L^{80}U^4A^2
=\exp\bigl((4\log2+o(1))L^h\bigr)
\]

polynomial-pair trials. All other work, including trial division up to Kidx, is below `exp(O_delta(L^h))`. If the supplied-order splitter costs

\[
\exp(O(\sqrt L\log L))\operatorname{bitlen}(M)\,\operatorname{poly}(L),
\]

as in the original deterministic paper, its total cost is also below this budget. The stronger sparse splitter is not required to obtain the 2/3+epsilon general bound.

For any fixed epsilon>0 choose rational `0<delta<=.01` with `8delta<epsilon`. The resulting composition has deterministic worst-case bit complexity

\[
\exp\bigl(O_\varepsilon((\log N)^{2/3+\varepsilon})\bigr).
\]

This conclusion uses the supplied-order splitting theorem as an actual proved input, not just its informal description. The separate `enumeration-burgess-audit.md` and `deterministic-splitting-core-audit.md` supply its fixed-degree enumeration replacement, uniform character bound, and character-assembly synthesis. Those dependencies have now been incorporated; no unproved splitter hypothesis remains in this deterministic composition.

The elementary smoothing inputs in source Lemmas 8.3–8.4 have also been checked: Cauchy's estimate on a disk of radius one quarter of the boundary distance gives the Gevrey derivative bound, and integration by parts with order proportional to `(abs(t)/Rwin)^(2/3)` gives the required Mellin tail. Their absolute constants are fixed and effective, so the changed schedule only needs Rwin to tend to infinity. They impose no extra power constraint.

## 6. What this conclusion does not establish

It does not lower general deterministic factoring to a first L-power of 1/2, and it does not give a first L-power below 1/3. The large-modulus obstruction is substantive: the current two-prefix proof needs two smooth prefixes of length approximately q, hence a smooth value of size at least q^(2-o(1)). A new argument for the much larger moduli in a near-1/2 schedule is still required.

The finite verifier `verify_deterministic_parameters.py` checks the rational power inequalities and the stated elementary counterexample to the literal printed Proposition 6.2. It does not certify analytic estimates, infinite asymptotics, or a Lean theorem.
