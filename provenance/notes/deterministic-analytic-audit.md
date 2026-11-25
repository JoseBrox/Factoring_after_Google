# Deterministic analytic transfer: saddle estimates, clean progressions, and the large-modulus obstruction

25 November 2026. Independent audit of the proposed power schedule in `deterministic-parameter-compression.md`, against pp. 44–48 of the hash-verified deterministic Cogentic paper. This note establishes the analytic parameter transfer through the conditional Gaussian moments, centered Gram estimates, stopping-time peeling, and final spectral guard, using the classical prime number theorem, Landau–Page theorem, and Montgomery zero-density estimate as mathematical inputs. The combined proof incorporates the separately audited base-polynomial/preconditioning construction, exact unit-relation extractor, and supplied-order splitter; the precise dependencies and their completed audit status are listed in Section 10. It does not certify the source's full formalization.

## 1. Main audit conclusions

1. The earlier concern about differentiating an unspecified Edgeworth error does not apply to the actual covariance argument. The source writes the logarithm of the saddle integral as an explicit smooth main term `G(x)` plus a uniformly `O(u^-2)` remainder. It differentiates `G`, then bounds the four remainder values in a second finite difference. This is legitimate.
2. The two shortest-prime-prefix character argument in Proposition 9.3 is sound at the displayed scale. In particular, its removal of a factor comparable to the number of characters follows from a genuine injectivity statement and character orthogonality, not an assumption of equidistribution.
3. A small repair is needed in the presentation of Lemma 9.2(1): its Perron proof retains a horizontal-contour error containing `mathcal L/nu`, whereas the final displayed bound omits that factor. Retaining the factor suffices for the application and does not change any power of `log N`.
4. The proposed powers satisfy the actual quantitative inequalities for Lemma 9.2, Proposition 9.3, Lemmas 9.4–9.5, and Proposition 10.1. Sections 3–5 and 9 check their analytic, conditioning, cancellation, adaptive deletion, and spectral arguments. The base construction, exact algebraic extractor, and supplied-order splitter have also been checked in the combined audit, as recorded in Section 10.
5. Smoothing alone does not remove the double-prefix obstruction. A shorter-prefix Cauchy–Schwarz estimate retains a loss exponential in `log q`, while the available Euler-product saving is exponential in `u = log Y/log B`. A structural average or a new character estimate is required.

## 2. Parameters and independent hypotheses

Write `L = log N`, `L2 = log L`. The candidate schedule fixes rational `0 < delta <= 1/100` and uses

```
a = 1/3,
t = 1/3 + delta,
k = 1/3 + 2 delta,
v = 1/3 + 5 delta/2,
b = 1/3 + 3 delta,
eta = 1/3 + 4 delta,
r = 1/3 + 5 delta,
c = 1/3 + 6 delta,
h = 2/3 + 8 delta.
```

Thus `log B = (log 2 + o(1)) L^b`, `log K1 = (log 2 + o(1)) L^k`, `log Y = Theta(L^h)`, `uY = log Y/log B = Theta(L^r)`, and `q <= Qmax = exp(3 L^(2/3))`. Window ratios satisfy `K1^.8 <= R = Y/S <= K1^1.7`. At most a fixed polynomial in `L` primes are deleted from `(sqrt(B), B]`.

The standard inputs needed here are:

- effective PNT error `theta(x) = x + O(x exp(-c sqrt(log x)))`;
- the usual effective Landau–Page zero-free region, with at most one exceptional primitive real character;
- for `4/5 <= sigma <= 1`, Montgomery's bound

```
sum_{d <= Q} sum_{primitive chi mod d} N(sigma,T,chi)
  << (Q^2 T)^(2(1-sigma)/sigma) (log(QT+2))^14.
```

The displayed near-one zero-density exponent is corroborated in the primary research paper by Ren and Tsang, *On Roth's theorem concerning a cube and three cubes of primes*, Lemma 5.2 and its proof, which identifies the underlying result as Montgomery Theorem 12.2. Primary author-hosted paper: <https://hub.hku.hk/bitstream/10722/75437/1/content.pdf>. The Cogentic reference labels it Theorem 12.1. The original Montgomery book has not been independently inspected in this audit; do not claim that its precise numbering or all bibliographic details have been verified. The displayed bound is used explicitly as a classical input.

## 3. Corrected prime-sum estimate

Let `chi` be primitive of conductor `d`, suppose `L(s,chi)` is zero-free in the rectangle `Re s >= 1-nu`, `|Im s-t| <= 2H`, and take `1-nu/2 <= sigma <= 1`, `0<nu<=1/8`, `H>=8`. For the trivial conductor require `|t|>=3H`. Put

```
mathcal L = log(d (|t|+H+4)/nu).
```

The Borel–Caratheodory argument in the source gives

```
|L'/L(s,chi)| << mathcal L/nu
```

on the inner rectangle. Truncated Perron, applied to the difference of two interval endpoints, shifts the contour to `Re z = 1-nu/2-sigma`. The apparent `1/z` singularity at zero is removable because `(x2^z-x1^z)/z` is analytic there. The resulting valid estimate is

```
|sum_{x1<p<=x2} chi(p) p^(-sigma-it) log p|
 << (mathcal L/nu) x1^(1-nu/2-sigma) log(H log B)
    + x2^(1-sigma) ((log B)^2 + mathcal L/nu)/H
    + B^(-1/10),
```

uniformly for `sqrt(B)<=x1<x2<=B` (harmless absolute constants absorb half-integer endpoints). The extra horizontal-contour term is retained explicitly.

For the new schedule set `H=L^12`; the source's `L^10` is also sufficient. With `nu0=L^-v`, the new saddle has `1-alpha = O(L2/L^b)=o(nu0)`. For large conductors, `mathcal L/nu0 <= L^(2/3+v+o(1)) < L^1.1`. The factor `B^(1-alpha)` is `O(u log u) <= L^.4` for sufficiently large `L`. Consequently the horizontal error is much smaller than `L^-8`; the vertical error contains

```
exp(-c nu0 log B) = exp(-c L^(b-v))
                   = exp(-c L^(delta/2)),
```

which is smaller than every fixed negative power of `L`. For small conductors, use `nu1=400 L2/log B` and `Dsmall=exp(cLP log B/(800 L2))`. The same estimate applies, with the Landau–Page exceptional character treated separately. Abel summation yields the uniform partial-prime-sum estimate `O(L^-4)` used by Proposition 9.3.

The factor omitted by the printed prime-sum statement is not asymptotically bounded by `(log B)^2` in the high-conductor application. At the original powers its size can be `L^(1.055+o(1))`, versus `L^(.72+o(1))`. Thus simply asserting the printed statement from the displayed proof would be incorrect; retaining it resolves the application.

## 4. Uniform saddle expansion and covariance

Let `J` be `(sqrt(B),B]` with at most `L^C` primes deleted, for fixed `C`, and

```
phi(s) = sum_{p in J} log(1+p^-s),
-phi'(alpha) = log Z,
uZ = log Z/log B,
lambda = (1-alpha) log B.
```

Uniformly for `uZ=Theta(L^r)`, PNT and partial summation give

```
lambda = log uZ + log log uZ + O(1),
(-1)^j phi^(j)(alpha) = Theta_j(uZ (log B)^j),
V = phi''(alpha) = Theta(uZ (log B)^2).
```

Deleting a further `O(L)` primes changes the `j`th derivative by at most `O(L^C B^(-alpha/2) (log B)^j)`, which is negligible compared with any fixed negative power of `L` times the saddle scale.

In the integral over `|t|<=1/log B`, set `z=t sqrt(V)`. On `|z|<=log uZ`, the cubic standardized cumulant is `O(uZ^-1/2)`, the fourth is `O(uZ^-1)`, and generally the `j`th is `O_j(uZ^(1-j/2))`. Expand the exponential through the fourth-order term and the square of the cubic term. Odd contributions integrate to zero on the symmetric interval. Gaussian moments of the sixth-order Taylor remainder and the unretained products are `O(uZ^-2)`. The tail `|z|>log uZ` is `O(exp(-c(log uZ)^2))`, after using the elementary cosine bound in the Euler product. This gives

```
Ipure(Z;S)
 = Z^(alpha-1) zeta^sf_{J\S}(alpha)/sqrt(2 pi V)
   * (1 + phi^(4)(alpha)/(8 V^2)
          - 5 phi'''(alpha)^2/(24 V^3) + O(uZ^-2)).
```

The implied constants are uniform over the deleted sets and over the stated `Z` range. This proof does not require differentiating an unspecified asymptotic remainder.

For the two-prime covariance, write `x=log Z`, `alpha'= -1/V`, and

```
G(x) = (alpha(x)-1)x + phi(alpha(x))
       - (1/2) log(2 pi phi''(alpha(x)))
       + log(1+kappa1(alpha(x))).
```

Derivative estimates through order six give

```
G''(x) = -V^-1 (1+O(u^-1)).
```

For `h1=log p`, `h2=log p'`, the exact double-integral identity for second differences yields

```
G(x-h1-h2)-G(x-h1)-G(x-h2)+G(x)
   = -h1 h2/V + O(u^-2).
```

The four Edgeworth remainder values contribute only `O(u^-2)`. This proves the rank-one covariance correction in the generalized Lemma 9.2. To compare its reference saddle `alpha_s` with root-centered means, use `|log |P_i^*(a/A)||=O(L^t+d log d)`. Since `t<b`, the corresponding saddle displacement times `log B` is `o(u^-1)`. Therefore the source's `1+O(u^-1)` normalizations remain valid.

## 5. Euler-product repulsion and clean progression theorem

For the principal character at `|t|>=1/log B`, and for the exceptional real character at all `t`, the source's elementary sine/cosine integration on the terminal prime interval yields

```
|L_J^sf(alpha+it,chi)|/zeta_J^sf(alpha)
    <= C exp(-c u/(log u)^2)
```

at low frequencies `|t|<=L^50/log B`. At higher frequencies up to `R^2`, the corrected prime-sum estimate gives the stronger `C exp(-c u)` bound. All deleted-prime costs are exponentially small in `log B`.

For the chosen power schedule, `u/(log u)^2 >> L^eta >> log R`, so both bounds give the source's required `exp(-c' L^eta)` relative error after Mellin integration. In an endpoint logarithmic optimization it is preferable to keep the frequency ranges separate: the low-frequency interval has only polynomial length in `L`, so its contribution does not need a full `R` loss. This observation improves bookkeeping but does not itself cross the large-modulus barrier.

### Exact two-prefix calculation

Assume `q^2 B^2 < exp(-.31)Y`. Every squarefree `J`-smooth integer in the compact cutoff support has a unique decomposition

```
n = m1 m2 m3,
q < m1,m2 <= qB,
```

where `m1` and `m2` are the first and second shortest prime prefixes exceeding `q`. Fix their terminal primes `pa<pb`. In the first prefix `m1=pa m1'`, the condition of shortestness implies `1<=m1'<=q`, and `gcd(m1',q)=1`. Thus the distinct allowed `m1'` inject into the reduced residue classes modulo `q`. The same holds for `m2/pb`. Define their Dirichlet polynomials `A_pa` and `B_pa,pb`. Orthogonality gives

```
sum_{chi mod q} |A_pa(alpha+it,chi)|^2
  = phi(q) sum_{m1} m1^(-2alpha)
  <= phi(q)^2 q^(-2alpha),
```

and the identical bound for `B`. Hence

```
(q/phi(q)) sum_chi |A_pa B_pa,pb|
  <= phi(q) q^(1-2alpha)
  <= q^(2(1-alpha)).
```

There is no square root of `q` left in this inequality.

For every nonprincipal, nonexceptional character whose primitive conductor avoids the excluded zero sets, the remaining Euler-product tail contributes `exp(-c u) zeta_J^sf(alpha)`. If `pb` is below `B^(1-1/(4lambda))`, the surviving terminal interval supplies the saving via prime-sum cancellation. If `pb` is above that threshold, the omitted lower primes already remove a fixed positive fraction of the saddle's prime mass. Both cases are uniform.

There are at most `B^2` terminal-prime pairs. The Mellin transform has `L1` norm `O(R Y^(alpha-1))`, while the main saddle has size `Theta(Y^(alpha-1) zeta_J^sf(alpha)/sqrt(V))`. Therefore the nonexceptional relative error is bounded by

```
C B^2 R sqrt(V) exp(2(1-alpha) log q - c u).
```

The exceptional-character contribution has relative bound

```
C R sqrt(V) exp(-c u/(log u)^2).
```

The cutoff's high-frequency error is at most a polynomial/exponential-in-`log q+u` factor times `exp(-c R^.6)`; it is negligible here.

With `q<=exp(3L^(2/3))`, the positive exponents in the first error are

```
O(L^b + L^k + L^(2/3-b) L2 + log L),
```

all `o(u)` because `r>b`, `r>k`, and `r>2/3-b`. For the exceptional error, `u/(log u)^2` dominates both `L^eta` and `L^k`. Also

```
2 log q + 2 log B = O(L^(2/3)) = o(log Y)
```

because `h>2/3`. Thus generalized Proposition 9.3(2) follows with relative error `O(exp(-c_delta L^eta))`.

### Exceptional-set counts

At `sigma=1-nu0`, `nu0=L^-v`, and `T*=2 K1^3.5`, Montgomery's estimate gives

```
log |E_med| = O(L^(b-v)) = O(L^(delta/2)),
log |E_hi|  = O(L^(2/3-v)) = O(L^(1/3-5delta/2)).
```

Each medium conductor has at most an absolute constant number of prime factors in `(B/2,B]`, so deleting all those primes still leaves `(1/2-o(1))B/log B` generator primes. This establishes the new schedule's version of Proposition 9.3(1).

## 6. Why shorter prefixes and smoothing do not by themselves cross the barrier

Suppose the two prefix thresholds are reduced to `Z1,Z2<=q`. For a fixed terminal prime, orthogonality now gives only

```
sum_chi |A_i|^2 <= phi(q) Zi^(1-2alpha)
```

up to constants. Cauchy–Schwarz therefore leaves

```
(q/phi(q)) sum_chi |A_1 A_2|
   <= q (Z1 Z2)^(1/2-alpha).
```

When `alpha=1-o(1)`, suppressing the exponential-in-`log q` loss requires `Z1 Z2 >= q^(2-o(1))`. If the whole smooth integer has size at most a constant times `Y` and `q>=Y^(1/2+epsilon0)` for fixed `epsilon0>0`, then even the largest possible product `Z1Z2=O(Y)` leaves at least `exp((epsilon0+o(1))log Y)` in this upper-bound mechanism. Its Euler-product saving is only `exp(-O(u))`, with `u=log Y/log B=o(log Y)`. Changing a Gaussian cutoff into another smooth cutoff cannot alter this arithmetic size comparison.

This is a limitation of this specific orthogonality/Cauchy–Schwarz proof. It is **not** a lower bound on smoothness equidistribution or on factoring. A proof using special residues, averaging over structured moduli, a stronger multilinear character estimate, or a different relation constructor remains possible.

## 7. Exact obstruction to simply moving all roots close to the evaluation point

Consider a degree-`d` integer polynomial `f`, leading coefficient `cd`, with `f(m)=kN` for a nonzero integer `k`. Suppose all real roots satisfy `|m-theta_j|<=C A`, and a sampled integer `a` lies in a root interval for which one factor has distance at least `wA`, while every other factor has distance at least `A/(C' d)`. Then the exact product formula gives

```
|f(a)|/|f(m)|
 = product_j |a-theta_j|/|m-theta_j|
 >= w C^(-d) (C' d)^(-(d-1)).
```

Consequently

```
log |f(a)| >= log N - log(1/w) - O(d log d).
```

For the intended regime `log(1/w),d log d=o(log N)`, these are values of size `N^(1-o(1))`, not the desired subexponential norm size. The same computation is valid without knowing the roots explicitly, provided the stated interval bounds are certified. It rules out obtaining the intended saving by a simple translation of the existing separated-root construction toward `m`; it leaves open differently shaped polynomials, very narrow special-value sampling, and genuinely new short-relation constructors.

## 8. Scope of the completed analytic transfer

The following section checks the conditioned Gaussian, Gram, and stopping-time arguments. Together with Sections 3–5, it completes the parameter transfer for Sections 9–10 of the source. The endpoint is a certified positive Gram with the same conservative `L^-3` guard used by the algebraic extractor. Section 10 records the algorithmic inputs incorporated by the combined proof.

## 9. Gaussian, Gram, and peeling transfer

### 9.1 Greedy–Rankin bound at the actual lattice widths

For a Gaussian progression of width `S`, modulus `q`, and center `Y`, assume `S>exp(.62)qB`. Set `M1=exp(.31)Yq/S`. Every supported squarefree smooth integer `n` near `Y` has a shortest prime prefix `d1>=M1`, with `d1<M1 B`. The remaining factor satisfies

```
exp(-.62)S/(qB) < d2 <= S/q.
```

For fixed `d2`, the admissible `d1` occupy one reduced class modulo `q`; their normalized Gaussian mass is at most `3/d2`. For `0<alpha<=1`, summing

```
d2^-1 <= (exp(-.62)S/(qB))^(alpha-1) d2^-alpha
```

gives the claimed Rankin bound, plus the exponentially small Gaussian tail. The complete upper expression can also be written `O((qB/S)^(1-alpha) zeta_J^sf(alpha))`; its apparent `Y` factors cancel. This matters when a forced gcd is divided from a conditional progression: the basic rough bound does not acquire an unaccounted factor `G^(1-alpha)`.

In the one-point application, the progression width divided by its modulus is `S(a)/Qhit >= UA/B^2`. In the two-point application the ratio is at least `U/(sqrt(2)B^2)`. Both exceed `exp(.62)B` because `U>=4B^4`. These conditions remain true with enormous slack in the proposed schedule. The large center-to-width assumptions follow from `K1^(1-o(1))>>L^3`.

### 9.2 Exact conditioning and coprimality in Lemmas 9.4–9.5

Write `L_a(u)=u0+a u1`. Conditioned on at most two prescribed simple modular roots at distinct primes, each root condition is a linear congruence

```
u0+r u1 = c_q (mod q).
```

It is a genuine single congruence because `q` is coprime to `P0 ell(r-m)`. The change of variables `(u0,u1) -> (L_a(u),u1)` is unimodular. Completing the Gaussian square and applying Poisson summation on the remaining coset gives exactly the one-dimensional conditional Gaussian used in the source. The errors are `O(exp(-cU))`, uniformly over all classes, because every residual width is at least `U/(sqrt(2)B^2)`.

For two evaluation points, `(u0,u1) -> (L_a,L_a')` identifies the integer lattice with the pairs satisfying `L_a'=L_a mod |a'-a|`. After the root conditions are imposed, the conditional step is

```
M2 = (Delta/gcd(Delta,Qhit(a'))) Qhit(a') Qfree,
Delta=|a'-a|.
```

This is verified prime by prime, including the case where a prescribed prime divides both hits and a positive power of `Delta`. No assertion of independence of the values at `a,a'` is being made.

For a clean first point the normalized value runs in a coprime class modulo

```
q1 = P0 ell^(1-epsilon_ell(a)) |a-m|.
```

Indeed `f(a)=f(m) mod(a-m)`, `f(m)=k0 N`, and both `gcd(a-m,N)=1` and `gcd(a-m,k0)=1` are imposed by the algorithm/preconditioning. The prescribed factors divided from `f(a)` are coprime to `a-m` because their roots are different from `m` modulo those primes. The possible `ell` factor is handled by the explicit `epsilon_ell` case split.

At the second point the modulus is

```
q2 = P0 ell^(1-epsilon_ell(a')) |a'-m|
       (Delta/Qboth) Qfree*.
```

It divides the integer product used in the definition of two-cleanliness and is at most `exp((1+o(1))L^(2/3))`, so the generalized clean progression theorem applies. Integer rounding of `d` causes only `O(L^(1/3))` in `log m`, safely inside the `3L^(2/3)` conductor cap.

When a second-point residue has a gcd `G` with its modulus, the rough bound divides `G` out. On a squarefree smooth event, `G` itself must be squarefree and factor-base smooth; otherwise the event is empty. The preceding Rankin observation controls the divided progression. The more precise saddle comparison can cost

```
exp(O((log G)^2/(u (log B)^2))).
```

Here `G<=AB^3`, and `2c<h+b`, so this factor is bounded and tends to 1. The inequality is explicit for the proposed powers: `2c-(h+b)=-1/3+delta<0`.

For two-clean pairs, the source's remaining exceptional residue classes are legitimate small errors:

- primes of `P0` and `|a'-m|` never divide the normalized residue;
- the prescribed `ell` can create one additional bad class when both sample points meet its root class; excluding `ell^2|Delta` makes the first and second squarefreeness exclusions distinct;
- primes in `(z0,sqrt(B)]` dividing `Delta` contribute the exact local multiplier `p/(p-1)`;
- factor-base primes dividing `Delta` remove only `O(p^-alpha)` of the first-point smooth mass;
- at most two remaining prescribed primes each remove `O(p^-alpha)`, whether the extra congruence gives a zero or a nonzero value at the first point. The zero case is counted after dividing `p`, and the nonzero case in the enlarged modulus.

All enlarged moduli still divide the product appearing in two-cleanliness. The total relative residue-exclusion error is bounded by

```
poly(L) exp(O(L^(2/3-b) log L)) B^(-alpha/2),
```

which is smaller than `K1^(-.90)` because `b>2/3-b` and `b>k`. Perturbed centers differ by `O(K1^(-.94))` relatively; the directly differentiated saddle-integral bound makes this error smaller than `K1^(-.90)` as well. Thus Lemma 9.5 transfers with the same stated clean relative error and rough factor

```
exp(O(L^(2/3-b) log L)).
```

### 9.3 Centered moments and exceptional conductors

For a fixed pair of feature indices, condition only on those indices being actual modular roots. The universal root set makes this conditioning precise even though the realized factor base depends on the random polynomial. There are at most two prescribed roots in each field, so the preceding Gaussian estimates apply. Partition sample points according to which prescribed primes and which `ell` root class they hit. This gives only polynomially many cells; a cell modulus `Mc` is at most `B^3`. The conditional feature weight obeys

```
|g(a)| Pi_R(a) <= poly(L) Mc M_{alpha,beta},
sum_a pi0(a)|g(a)|Pi_R(a) <= poly(L)M_{alpha,beta}.
```

The diagonal contribution is exponentially small in `L^c`, since `log((Z1 Z2)^-1)=O(u log u)`, `log A=Theta(L^c)`, and `c>r,b,k,t`. Close pairs give `K1^(-1/2+o(1))` because `t<k`; repeated prescribed primes give `B^(-1/2+o(1))`.

For the exceptional-conductor contributions, the exact logarithmic costs are:

```
medium:
  O(L^(b-v) + L^(b/2) + L^(2/3-b) log L),
  versus a saving c L^b/log L;

high:
  O(L^(2/3-v) + L^(1/3) + L^(2/3-b) log L),
  versus a saving c L^b.
```

Every comparison is strict at the chosen powers. The divisor weight estimate used here is `sum_{h|d0}h^-1/2 <= exp(C sqrt(log d0))`; it does not introduce a hidden full divisor-count factor. For bounded-prefix divisors as large as `B^10` or `B^20`, plain arithmetic progression counting suffices: `Aw` dominates every fixed power of `B`, so all additive endpoint errors are negligible. An extension of the Brun lemma beyond its written `hMq<=B^4` range is unnecessary.

On the two-clean pairs, expand the exact local factor `gamma(a,a')^2` over squarefree divisors supported on `(z0,sqrt(B)]`. For each small divisor `h`, the mean term cancels because

```
f(a) Pi_R^circ(a)
   = 1_{a=rpair mod Qpair} Qpair U_ex(a).
```

The corresponding average of `Pi_R^circ` is 1, to the Brun error. This identity is checked for scalar, archimedean, diagonal-prime, same-field distinct-prime, and different-field prime indices; it is not a heuristic independence assertion. The sum of divisor weights is bounded. The residual square moment is `poly(L) EBr^2`, with

```
EBr = exp(-(delta/2)L^delta log L),
Erel = exp(-(3delta/4)L^delta log L),
```

so it is `o(M_{alpha,beta}^2 Erel)`.

The derivatives of `U_ex(a)` needed for Brun summation can carry a polynomial factor in `d`; this is harmless because the Brun hypothesis allows `L^40/(Aw)`. One should not silently infer derivative bounds by differentiating an unspecified remainder. They follow directly by differentiating the saddle integrals and applying the chain rule to the explicit means. The previously obtained bounds suffice, with a fixed polynomial loss far below `L^40`.

### 9.4 Stopping-time peeling with dimension-independent inequalities

Put `E=Erel` and choose

```
tau_diag = E^(1/4),
delta_peel = E^(1/8),
mu_* = E^(7/15).
```

The moment bounds and Markov's inequality give, with probability `1-o(1)`, the source's good event with the squared Frobenius and weighted diagonal errors bounded by `E^(74/75)`. All expectation-to-threshold ratios are a fixed positive power of `E` times a polynomial in `L`, hence tend to zero. The total number of feature indices is not inserted as a multiplicative loss: conditioning on the prescribed root events gives the weighted sums `O(u)` for a field and `O(du ell^-alpha)` for the protected rows.

At a peeling stage with deleted mass at most `mu_*`, each protected `ell` row loses at most

```
B^(-c) + 2mu_* + sqrt(mu_*) E^(37/75)
   = o(delta_peel).
```

For all newly deleted rows, the exact weighted Cauchy–Schwarz inequality gives

```
mu(new rows) <= 4 delta_peel^-1 B^(-c)
                 + 4 delta_peel^-2 mu_* E^(74/75)
              < mu_*/2.
```

The exponent in the second relative factor is `74/75-1/4=221/300>0`, so the invariant closes at every stage without a union bound over the number of stages. This proves retention of the protected rows and bounded total deleted mass even though the deletion rule is adaptive.

The removed Gram mass has operator norm at most

```
poly(L) mu_* + poly(L) delta_peel,
```

because each retained relation has at most `5u` nonzero prime features. Together with the retained diagonal and Frobenius errors, the operator error is `O(E^(1/10))`, which is smaller than every fixed inverse power of `L`.

### 9.5 Spectral lower bound: preserve the block structure

The prime-feature covariance approximation error is `O(1/u)` in operator norm and is supported **only** on the prime-feature block. Applying a global Weyl estimate against the final small eigenvalue would be invalid. The proof instead absorbs this error into the order-one coefficient of `||y_F||^2` before deriving the smaller archimedean gap.

Let `w_i=(q^(-alpha_s/2) log q)` on the retained roots in field `i`. Then `||w_i||^2=Theta(u(log B)^2)`. For a unit input vector, subtract the two exact norm identities to obtain a vector `w'` whose field components are orthogonal to `w_i`. The source's case split is purely deterministic and gives

```
||w'||^2 >= c min(1,
                    d/max_i ||w_i||^2,
                    d/(log Xsc)^2)
           >= c L^(a-2h).
```

The potentially negative covariance direction is now negligible on this complement: the difference between its vector and `w_i/sqrt(V)` has norm `O(1/u)`, so its square contributes only `O(u^-2)||y_Fi||^2`. The remaining covariance error and diagonal error likewise affect only `||y_F||^2` and can be absorbed there. The prime means have squared norm `O(u)`, so the elementary inequality used in the source yields

```
y^T U_ex y >= (1/2)||y_F||^2
              + c/u sum_a pi0(a)(y0+ell(a/A)^T y_arch)^2.
```

For the archimedean means, the diagonal differences between the root-centered intervals and the reference interval have size `Theta(L^t)`; the off-diagonal Frobenius norm is `O(d log d)`. Since `t>a`, the minimum singular value is `Theta(L^t)`. The reference interval has mean-log squared norm `O(d)`. Combining these facts and averaging over the `2d+1` intervals gives

```
sum_a pi0(a)(y0+ell(a/A)^T y_arch)^2
  >= c/d (y0^2+||y_arch||^2).
```

Consequently the quadratic form on the normalized transformed vector is at least `c/(du)`. Replacing the reference roots by the true isolated roots loses only `poly(L)K1^-1.8`, and the peeling error is superpolynomially small. The actual reduced Gram therefore satisfies

```
lambda_min(H_true) >= c L^(a-2h)/(du)
                   = c L^(-2h-r).
```

At the proposed schedule `2h+r=5/3+21delta<3`. Thus the source's conservative `L^-3` output guard remains valid. No hidden dependence on the exponentially large factor-base dimension occurs in this step.

## 10. Revised theorem boundary after the additional checks

The analytic parameter-transfer obligations in Lemma 9.2, Proposition 9.3, Lemmas 9.4–9.5, and Proposition 10.1 are checked at the proposed powers, including the actual conditioning and adaptive deletion arguments. The previous `2/3+epsilon` checkpoint is therefore a proved analytic parameter transfer. Its full algorithmic assembly uses the generalized base-polynomial and preconditioning statements from Lemmas 8.1–8.2, the elementary cutoff estimates in Lemmas 8.3–8.4, the exact order extraction and bit bounds in Lemmas 7.4–7.5, and a supplied-order splitter. Lemma 7.3 supplies the valuation identity for the extractor.

The combined audit has checked the finite/algebraic transfer in Lemmas 7.3–7.5 and the generalized base construction and guards in Lemmas 8.1–8.2: localization, valuation offsets, unit-lattice covolume and denominator bounds, exact pivot selection, Gram determinant conditioning, rational reconstruction, and polynomial runtime in `(A,B,d,Drow,Pbit)`.

The supplied-order package is now also established by `enumeration-burgess-audit.md` and `deterministic-splitting-core-audit.md`. The former provides an independent replacement for biquadratic enumeration and checks the uniform quadratic-field Burgess argument. The latter checks the original Miller tests, compatible square roots, ideal-class cocycle cancellation, Walsh positivity, and dyadic search. This assembly uses the original `exp(O(sqrt(L) log L))` splitter, which is already absorbed by `exp(O(L^(2/3+epsilon)))`; the newer sparse construction is not required. The literal squarefactor-divisibility and finite-field-root-count corrections are stated in those files and preserve all applications.

Thus the audit boundary is no longer an unresolved parameter transfer or an unexamined supplied-order lemma. The assembled argument is an ordinary mathematical proof using the stated classical analytic and lattice inputs. It is not a verification of the source's full Lean formalization. No sub-`L[1/3]` algorithm is proved.


## 11. Constructive finite-input coverage and effectivity

Fix a rational `delta` in the stated range. Every power appearing in the changed algorithm can be implemented by integer arithmetic and the source's rational-power rounding. The algorithm performs finitely many guards, finitely many prime/gcd tests, and a finite enumeration of all generator primes and perturbation pairs. Every purported order multiple is checked by modular powering, and the same explicit cardinality and bit-length guards decide whether to return the annihilator or enter deterministic trial division.

The exceptional-character and exceptional-conductor sets occur only in the analysis. The algorithm neither computes zeros of Dirichlet L-functions nor attempts to identify a possible Siegel zero. In particular, the analytic proof uses the exceptional real character with its permitted sign and Euler-product repulsion, and never invokes an ineffective lower bound for `1-beta`.

All positive comparisons in this note use explicit strict gaps between powers, or fixed positive powers of `Erel`. Given effective versions of the stated classical inputs, these comparisons yield an effective finite threshold `N0(delta)`. For every admissible `N>N0(delta)`, all construction guards hold, enough generator primes succeed, the output bit-length guard holds, and fallback trial division is not used. For `N<=N0(delta)`, trial division is finite and its maximum cost is absorbed in an effective constant depending on `delta` and on the imported effective constants.

The program does not need to know `N0(delta)` in order to run. It follows its finite guards and certificate checks on every input. Thus there is no hidden noncomputable threshold in the proposed uniform algorithm for each fixed rational `delta`. For a requested fixed `epsilon>0`, selecting a fixed rational `delta<epsilon/8` yields the stated `exp(O((log N)^(2/3+epsilon)))` family of bounds, with constants allowed to depend on `epsilon`.

## 12. An exact refinement for future logarithmic optimization

The source's specified roots, within either field, are equally spaced by `1/(2d)`. Their exact derivative product is

```
|P_i'(rho_{i,s})| = (s-1)! (d-s)!/(2d)^(d-1)
                  >= (8e)^(-(d-1)).
```

Indeed the numerator is `(d-1)!/binom(d-1,s-1)`, the binomial is at most `2^(d-1)`, and `n!>=(n/e)^n`. For `0<eta<=1/(8d)`, each factor other than the nearest root is at least `3/4` of its value at the root, so

```
|P_i(rho_{i,s} +/- eta)|
  >= eta (3/(32e))^(d-1)
  > eta 32^(-(d-1)).
```

Thus isolating a perturbation whose uniform error is at most `K1^-1` inside radius `K1^(-.95)` requires only `log K1 > 20(d-1)log 32` (and the elementary radius/separation condition). The coarse product estimate `(8d)^-d` unnecessarily spends a factor `log d` in this comparison.

There is a corresponding improvement in the mean-log matrix. Its off-diagonal entries are bounded by a constant plus `|log(|j-k|/(4d))|`; grouping by the difference and comparing with the convergent integral `integral_0^1 log(x)^2 dx=2` gives a squared Frobenius norm `O(d^2)`, hence norm `O(d)`. The source's `O(d log d)` upper bound is sufficient but not sharp.

These elementary refinements affect logarithmic factors at the boundary of the `2/3` schedule. They do not by themselves reduce its fixed power, remove the large-modulus progression obstacle, or establish a new endpoint `L[2/3,c]` theorem. Such a claim would require retracing the Landau–Page height, exceptional-conductor, Gaussian, and peeling error budgets with an explicit logarithmic schedule.
