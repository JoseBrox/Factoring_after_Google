# Deterministic supplied-exponent splitting: independent core audit

25 November 2026. This audit checks Lemma 3.1, Lemma 5.1, Lemma 6.4, and the synthesis of Theorem 1.2(a) in the pinned deterministic Cogentic manuscript. There is no separate Lemma 5.2 in this version. The input is the hash-verified extraction `audit/sources/deterministic-paper.txt`; the relevant source pages are 13–15, 20–22, and 27–29.

Source: <https://github.com/google-research/google-research/blob/4a7bc8ab0bc770e71a259b7966c500496b99010a/cogentic_research_papers/deterministic_factoring_l34/paper.pdf>, Git blob `973002e0eb92acf3964fc020ca52ba6f1ac384ac`.

## 1. Result and exact boundary

The checked core, combined with the two auxiliary results established in `enumeration-burgess-audit.md` and restated in Section 2 below, proves that there is a deterministic algorithm that, on an odd composite integer N with at least two distinct prime divisors and an even supplied integer M satisfying p−1 | M for every prime p | N, returns a verified nontrivial factor in

\[
\exp\bigl(O(\sqrt{\log N}\,\log\log(N+16))\bigr)
\, (\log M)(\log N)^2
\]

bit operations, with effective absolute constants. No factorization of M is required. Even N is handled immediately, and perfect powers can be removed by the general factorer's preprocessing.

The Miller tests, active-character argument, compatible roots, ideal-character extension, Walsh positivity, dyadic scale selection, and effective fallback are all checked below. The source's small class-representative norm is **sqrt(D)**, where D is the absolute discriminant; the PDF-to-text extraction sometimes obscures this square root.

One literal correction is needed: the particular construction in Lemma 3.1(3) provides `m_ell | P_K^K`, rather than its stated stronger `m_ell | P_K`. The proof itself already gives the correct formula. All subsequent uses need only that the prime factors of m_ell divide P_K, so this correction has no effect on the proof or complexity.

The companion investigation supplies a replacement for source Lemma 4.2 and a detailed proof audit of Lemma 6.3(1). A further independent read corroborated its parity-normalized weighted-lattice construction and the full Burgess shift, collision, moment, and Hölder arguments; Section 9 records the decisive checks. These auxiliary results are proved components of the combined audit. They are treated as modular inputs here to avoid duplicating that full file.

## 2. The two auxiliary contracts

### 2.1 Enumeration contract

For a quadratic field F with absolute discriminant D, a compatible modular embedding into Z/NZ, and a norm cutoff Z below N, in time polynomial in the **numerical values** D and Z and in log N, produce either a factor of N or modular images of:

- a generating set for the full unit group of F;
- at least one generator of every principal integral ideal of norm at most Z and norm coprime to N.

The analogous contract for a biquadratic field E uses time polynomial in the numerical discriminant |Delta_E|, cutoff Z, and log N. The source assumes N > 64|Delta_E| in this case. Only constant degree 2 or 4 occurs. It is enough to establish this contract by any effective algorithm; reproducing the source's particular infrastructure routine is unnecessary.

If every returned image passes the order test without splitting N, the active character is +1 on all unit generators. It is then +1 on every unit, including inverse powers. Any other generator of a listed principal ideal differs by a unit, so it too has active character +1. This explains why finite lists certify the infinitely many unit and generator assertions required later.

### 2.2 Uniform character-sum contract

Let q be an odd prime or a product of two distinct odd primes, chi the associated Legendre or Jacobi character, F a quadratic field of discriminant D, and phi a modular embedding. Suppose

\[
P^-(q)>D,\qquad D\le q^{1/200},\qquad
\chi(\phi(u))=1\quad(u\in O_F^\times).
\]

For every integral ideal b of norm at most sqrt(D) and every
`q^(3/10) <= W <= q^(2/5)`, require

\[
\left|\sum_{\substack{\gamma\in(b\setminus\{0\})/O_F^\times\\
1\le |N_{F/\mathbf Q}(\gamma)|\le N(b)W}}
\chi(\phi(\gamma))\right|
\le C_B D^2 Wq^{-1/4000}
\]

for an effective absolute constant C_B. The companion audit treats source Lemma 6.3(1), including its complete finite-field character-sum input. The source's formulation of that finite-field input needs the standard count of distinct roots over an algebraic closure; the actual polynomials used in the application are products of linear factors, so this correction preserves the application.

## 3. The order test works with only a multiple of every p−1

Write `M=2^t u` with u odd. For a unit z modulo N, set `b_k=z^(u 2^k) mod N`, and at each k test `gcd(b_k−1,N)`. Return a proper nontrivial gcd if one appears; otherwise stop at the first b_r=1.

Although M need not annihilate the entire unit group modulo a repeated prime power p^a, it does annihilate modulo p. Therefore `b_t−1` is divisible by every distinct prime factor of N. Its gcd with N is greater than 1. If that gcd is not proper, it equals N, so b_t=1 modulo N. Thus the procedure really reaches an order certificate whenever it does not split.

If r>0, the preceding gcd is 1. Since

\[
p^a\mid b_{r-1}^2-1=(b_{r-1}-1)(b_{r-1}+1)
\]

and p does not divide the first factor, p^a divides the second. Hence `b_(r−1)=−1 mod N`, and b_0 has exact order 2^r modulo every p and every p^a. This is the needed synchronization of local 2-parts. The r=0 case gives order 1 everywhere. Modular exponentiation and the gcd chain cost `O((log M)(log N)^2)` with the stated elementary arithmetic model.

Now write `p_i−1=2^(e_i)m_i` with m_i odd. If the e_i are not all equal, choose a prime p_* of maximum e_i and take chi to be its Legendre character. A value with chi(z)=−1 forces local 2-order exponent at least e_*, whereas a prime with smaller e_i forces it at most that smaller value. This contradicts synchronization. If all e_i agree, take chi to be the product of the Legendre characters at any two distinct prime factors. A chi-value of −1 gives opposite local Legendre signs, again incompatible with a synchronized 2-order.

Consequently any integer with active chi-value −1 splits N. If that integer was not a unit modulo N, its initial gcd is already proper: its active chi-value ensures it is coprime to the active modulus q.

The active modulus q is used only in the proof. The algorithm never needs to find the primes defining it.

## 4. Compatible square roots and the corrected m_ell statement

Test `q_0=−1,q_1=2,...,q_K`, under `P^-(N)>q_K`. If no test splits N, let z_j=q_j^u have synchronized order 2^(r_j), select a maximum-order pivot z_*, and denote it by zeta. Since q_0=−1, its order is 2, so zeta has positive order exponent r_*.

A bit-by-bit discrete logarithm in this 2-group either expresses every z_j as zeta^(m_j), or produces a nontrivial square root of 1 whose gcd splits N. The invariant at step nu is

\[
(z_j\zeta^{-m})^{2^{r_*-\nu}}=1\pmod N.
\]

Its half-power is ±1 on each prime-power component. Mixed signs split N; equal signs determine the next bit. Thus the routine needs only polynomially many modular operations, rather than enumerating 2^(r_*) values.

For each nonpivot index i_r, let `delta_r=m_(i_r) mod 2` and

\[
d^{(r)}=q_*^{\delta_r}q_{i_r},\qquad
s^{(r)}=(d^{(r)})^{(u+1)/2}\zeta^{-(m_{i_r}+\delta_r)/2}.
\]

Then `(s^(r))^2=d^(r) mod N`. For a subset ell, write
`sum ell_r delta_r=2 k(ell)+epsilon(ell)` and define

\[
d_\ell=q_*^{\epsilon(\ell)}\prod_{r:\ell_r=1}q_{i_r},\qquad
s_\ell=q_*^{-k(\ell)}\prod_{r:\ell_r=1}s^{(r)}.
\]

The d_ell are distinct nontrivial squarefree signed divisors of P_K. They satisfy

\[
\prod_{r:\ell_r=1}d^{(r)}=d_\ell m_\ell^2,
\qquad m_\ell=|q_*|^{k(\ell)}\mid P_K^K.
\]

A repeated positive pivot can give k(ell)>=2, so divisibility by the squarefree P_K itself is not guaranteed. The weaker displayed conclusion gives exactly the prime support needed in the Legendre-symbol argument.

For distinct ell_1,ell_2, put ell_3=ell_1+ell_2. Cancelling the common subset factors gives

\[
s_{\ell_1}s_{\ell_2}=\eta_{12}s_{\ell_3}\pmod N,
\]

where `|eta_12|=gcd(|d_ell1|,|d_ell2|)` and eta_12 is negative precisely when both radicands are negative. This is the exact sign dictated by the canonical complex square roots. It certifies a compatible modular embedding of each biquadratic compositum, including the cases of negative radicands.

## 5. Why the ideal-character extension is multiplicative

For each quadratic or biquadratic field F choose, in every inverse ideal class c^−1, an integral representative a_c of norm at most `M_F=sqrt(|Delta_F|)`, with a_1=O_F. All these ideals are coprime to q because the smallest prime factor of q exceeds their norms.

For an ideal c coprime to the selected prime ideals above q, choose a generator gamma of a_[c] c and define chi_F^*(c)=chi(phi(gamma)); set it to zero on the excluded ideals. Triviality on units makes this definition independent of the generator.

To check multiplicativity for integral ideals mathfrak c_1, mathfrak c_2, let c_i=[mathfrak c_i] be their ideal classes and put `e=a_((c_1 c_2)^−1)`. The two auxiliary ideals

\[
a_{c_1c_2}e,\qquad a_{c_1}a_{c_2}e
\]

are principal, of norms at most M_F^2 and M_F^3. Their character values are +1 by the small-principal-generator hypotheses. Applying the principal character to the identity

\[
(a_{c_1}\mathfrak c_1)(a_{c_2}\mathfrak c_2)
(a_{c_1c_2}e)
=(a_{c_1c_2}\mathfrak c_1\mathfrak c_2)
(a_{c_1}a_{c_2}e)
\]

proves multiplicativity. The convention of zero on ideals divisible by selected primes extends multiplicativity to all integral ideals.

The source bounds are enough: in a quadratic field, `M_F^3=D M_F<=4P_K M_F<=Y M_F`; in a biquadratic field, `M_E^3<=4096 P_K^(9/2)`. A prime ideal over an unramified rational prime r<=Y therefore has value +1: its norm is r in the split case, while the inert ideal is rO_F and has value chi(r)=1.

For a quadratic subfield F of E, let b=a_[c]. Extending `bc=(gamma)` to E and using multiplicativity gives

\[
\chi_E^*(bO_E)\chi_E^*(cO_E)=\chi_F^*(c).
\]

The correcting principal generator used to define `chi_E^*(bO_E)` has norm at most

\[
M_E\,N_F(b)^2\le M_E D_F\le64P_K^{5/2},
\]

within the biquadratic cutoff. Thus its value is +1 and restriction compatibility follows. This is a genuine cancellation of the ideal-class cocycle, with all correcting norms charged.

## 6. Walsh positivity: all local cases

For a rational prime r not dividing P_K q, let g(r) encode the Legendre symbols of the K basis radicands. A quadratic field indexed by ell splits at r exactly when `ell·g(r)=0`. Write V for this splitting subspace.

When chi(r)=1, the two split prime ideals have the same sign. The three pairwise quadratic subfields of a biquadratic extension give a product of three signs equal to chi(r)=1: each of its four prime-ideal signs appears once, and the common prime-ideal sign appears twice extra. Hence the signs on V form a linear character, represented by a vector v.

Let b_ell(r^e) be the sum of ideal-character values over ideals of norm r^e. Its elementary values are:

| Case | Split field | Inert field |
|---|---:|---:|
| chi(r)=1 | `(e+1) alpha^e` | `0` if e odd; `1` if e even |
| chi(r)=−1, e odd | `0` | `0` |
| chi(r)=−1, e=2m | `1` | `(−1)^m` |

Each row is a nonnegative integral combination of the Fourier functions `(-1)^(ell·w)`:

- At r<=Y, all split signs are +1. The coefficients at w=0 and w=g are respectively `ceil((e+1)/2)` and `floor((e+1)/2)`.
- At r>Y with chi(r)=1 and e even, use the same coefficients.
- At r>Y with chi(r)=1 and e odd, put coefficient `(e+1)/2` at both v and v+g.
- For chi(r)=−1 and e odd, all coefficients are zero.
- For chi(r)=−1 and e=2m, use the single coefficient 1 at 0 if m is even, and at g if m is odd.

Colliding indices simply add their coefficients, including when g=0. The total local coefficient mass is at most e+1. Multiplication over prime powers corresponds to convolution of these nonnegative coefficients. Therefore there is an artificial coefficient `0<=b_0(n)<=tau(n)` with

\[
b_0(n)+\sum_{\ell\ne0}b_\ell(n)
\ge2^K\mathbf1_{P^+(n)\le Y}
\qquad((n,P_Kq)=1).
\]

For a smooth n the Fourier coefficient at zero is at least 1, since every prime-power factor already has a coefficient at least 1 there. Summing n<=X and bounding `sum tau(n)<=X(1+log X)` proves the lower bound used by Lemma 6.4.

## 7. The contradiction and deterministic scale search

For a dyadic scale `L_m=2^m`, use `u_m=floor(floor(sqrt(L_m))/(6m))` and `K_m=u_m(m+5)+m+2`. The source's explicit cutoffs satisfy, for m>=40,

\[
\log P_{K_m}<\tfrac38\sqrt{L_m}\log L_m,
\qquad
\log B_{\rm guard}(m)<8\sqrt{L_m}\log L_m.
\]

Suppose `0.99L_m<=log q<2.01L_m`, `P^-(q)>B_guard(m)`, and all tests fail to find a negative active character. Put `X=q^(1/3)` and `Y=floor(X^(1/u_m))`. Then the integer tests and field enumerations imply precisely the small-integer, unit, and principal-generator hypotheses of the Walsh lemma. Their cutoffs dominate `sqrt(4P_K)Y` and `4096 ceil(P_K^(9/2))`.

The elementary construction of smooth numbers as products of u_m distinct primes from `(Y/2,Y]` yields

\[
\Psi_{P_Kq}(X,Y)>X(25\log X)^{-u_m}.
\]

Here no excluded prime lies in `(Y/2,Y]`: primes dividing P_K are below Y/2 and primes dividing q are above Y. The chosen K makes the diagonal error in the Walsh lower bound smaller than half this quantity, and hence

\[
\max_{\ell\ne0}S_\ell^{\rm cop}(X)
>\tfrac12 X\exp(-\sqrt{L_m}).
\]

The character-sum contract, summed over at most D ideal classes, and inclusion–exclusion over at most 2K prime ideals above P_K give

\[
|S_\ell^{\rm cop}(X)|\le C'_B4^KD^3Xq^{-1/4000}.
\]

Removing rational divisibility by q needs only one further correction if q=p_1p_2. The larger prime exceeds X. At the smaller prime, the selected prime ideal already has character zero, while divisibility by the other prime ideal contributes a single term at X/p_1. If `p_1<=q^(1/50)`, the shifted norm range remains within the character-sum contract; otherwise the divisor bound is already smaller than the required saving. This justifies the stated uniform prime-or-semiprime bound.

The resulting upper bound is at most

\[
C'_BX\exp(2\sqrt{L_m}\log L_m-L_m/4100),
\]

which contradicts the lower bound for every sufficiently large effectively specified m. The source gives an explicit threshold in terms of C'_B.

Finally, the algorithm first trial-divides up to an explicitly rounded value T with

\[
\exp(12\sqrt L\log L)<T<\exp(55\sqrt L\log L),
\qquad L=\log N,
\]

for all sufficiently large N. If this fails, all prime factors of N exceed T. It then tries all dyadic m up to `floor(log_2(floor(log_2 N)+1))`, executing an iteration only when `B_guard(m)<T`.

For the proof's unknown active modulus q, the index `m_*=floor(log_2 log q)` is in this loop, eventually exceeds the contradiction threshold, and satisfies

\[
B_{\rm guard}(m_*)<\exp(8\sqrt L\log L)<T<P^-(q).
\]

Thus that iteration either returns a factor or produces the forbidden simultaneous positivity assertions. Every enumerated family, discriminant, and norm cutoff is polynomially bounded in T, so the whole search costs a fixed polynomial in T and log N, times the per-test dependence on log M. The number of dyadic iterations is only O(log log N).

A final trial-division fallback guarantees termination for every input, including the finitely many inputs below the analytic threshold. The program does not need that threshold as input. The constants are effective as soon as the two contracts are effective.

## 8. Consequence for the 2/3+epsilon transfer

This older supplied-exponent splitter is already fast enough. If the annihilator construction outputs an exponent with

\[
\log M\le\exp(O(L^h)),\qquad h=2/3+8\delta,
\]

and costs `exp(O(L^h))`, then the additional splitting cost is still `exp(O(L^h))`, because `sqrt(L) log L=o(L^h)`. One may therefore close the general-factoring exponent transfer using this original splitter and the two audited auxiliary contracts, without relying on any new sparse-family optimization. The optional sparse and ramification-tolerant improvements are separate claims.

## 9. Independent corroboration of the two auxiliary proofs

The replacement enumeration proof uses exact quadratic fundamental units and exact ideal arithmetic, whose polynomial dependence on the numerical discriminant is within the required budget. For a principal biquadratic ideal B=(beta), relative norms into the real quadratic subfields determine their unit exponents modulo two. Multiplication by suitable subfield units reduces these exponents to at most eight parity tuples. For the correct tuple, explicitly determined archimedean weights make all four embedding absolute values of a generator beta' equal to `N(B)^(1/4)`.

Every nonzero x in B has absolute norm at least N(B), so the arithmetic-geometric mean inequality certifies that this beta' is an exact shortest vector in the weighted Minkowski lattice. A rational approximation with relative operator error at most 1/1000 preserves the requisite comparison with the first reduced basis vector. The dimension-four LLL inequalities put a true shortest vector in the fixed integer coordinate box `[-8,8]^4`: with a 1.01 length comparison, backward bounds on the four integer coefficients are at most 2, 3, 3, and 5. Exact norm testing among these candidates recovers a generator. For the unit ideal, retaining every norm-one candidate, together with the subfield units, covers every unit after reversing the parity reduction. This includes torsion. The required precision is polynomial in the numerical discriminant and log of the norm cutoff. Thus no uncharged search over an enormous real-unit interval remains.

In the Burgess proof the scaling of the real embeddings is consistent: gamma and omega use the strip-dependent scaling, while the multiplier beta uses the original embeddings. This gives both the small product shift and the norm estimate for a ratio collision. The collision difference `delta=gamma_1 beta_2−gamma_2 beta_1` lies in an ideal of norm N(b)q but has absolute norm at most `N(b) q^(.7365)`, hence is zero. Counting ideal divisors and unit multiples then gives the claimed second-moment factor `O(q^(3/500))`.

For the sixteenth moment, the larger prime of a semiprime has injective reduction on the shift set. Tuples with all individual elements occurring evenly contribute `O(q^(3/2))`; tuples with an odd residue multiplicity at the smaller prime have square-root cancellation at both primes and give the same bound. The remaining tuples pair only modulo the smaller prime p_1: their number is `O(q p_1^(-8))`, and their character sums are `O(q^(1/2)p_1^(1/2))`, again sufficient. The complete finite-field polynomials all split into linear factors, so the corrected standard Weil estimate applies.

Hölder's exact exponent calculation is

\[
\frac1{3200}+\frac1{16000}-\frac3{80}
+\frac1{32000}-\frac{15}{256}+\frac3{32}+\frac3{8000}
=-\frac1{640}< -\frac1{4000}.
\]

Boundary squares and the at most D^2 real-unit strips give the stated `D^2 W q^(-1/4000)` bound. The constants from divisor bounds can be enormous, but they are effective and absolute; the finite-input fallback absorbs them.
