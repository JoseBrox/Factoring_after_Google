# U100: ordinary concentration and completion of the parameter transfer

27 November 2026. **Written mathematical proof checkpoint.** This note discharges the ordinary-concentration and changed-range arithmetic obligations in [the U100 schedule](keybreak_unconditional_fallback.md), using the explicit constructions and finite lemmas of the pinned KeyBreak manuscript and the classical analytic inputs specified below. It is not a Lean proof, independently refereed theorem, or implementation benchmark. The proof is structured as a replacement argument for the range-dependent source lemmas, not an invocation of Theorem 1.1 at parameters for which it was not stated. The source's finite algebraic certification, bit-operation implementations and elementary lattice-window lemmas are reused with their hypotheses checked here.

Source: The KeyBreak Cryptanalysis Agent, *Provable Integer Factorization via Multilevel Descent: Approaching Heuristic Bounds*, 26 November 2026, 144 pp., [PDF](https://crypto.sjtu.edu.cn/factoring.pdf), SHA-256 2b534eaf77fb2b9712018879059d8d4667c40c0a4adf2fff90efc22fb356cfc9. Equation numbers B.1–H.19 below identify that exact source. The earlier conditional ledger is preserved as the historical development. No hypothesis about the zeros of Dirichlet L-functions, no heuristic polynomial smoothness law and no assumed factoring oracle are used in this argument.

## 1. Notation, analytic imports and common ranges

Put \(D=\log N/\log\log N,\lambda=\log\log N,\Lambda=D^{1/3}\lambda\). Write \(n=\operatorname{bitlength}N,\ m_b=\operatorname{bitlength}n,\ d\) the least odd integer at least 3 satisfying \(d^3m_b\ge n,\ t=dm_b,\ \Lambda_b=t\log2\sim\Lambda\). In this note let
\[
 b=1,\quad \kappa=24,\quad Q_*=161/10,\quad e_B=t,\quad
 e_0=\lfloor(n-5)/(2\kappa d)\rfloor-1,\qquad
 e_{i+1}=\max(e_B,\lceil(e_i+2t)/Q_*\rceil).
\]
Here \(Q_*\) is the descent ratio, distinct from the sampled rational prime \(Q\). Set \(Y_i=2^{e_i},V_i=Y_i^6,B=2^{e_B}\), and stop at \(e_j=e_B\). Use the exact source coefficient law (B.4),(B.6), with \(M=\lfloor N^{1/d}\rfloor,E=2^{d^2m_b}, W=M^2V_0^2E^4,H=2^{d+20}d^{10}WE^4,h_0=2H+1\). Let \(y=Y_{i+1},Y=Y_i\) at level i. The fixed point of the unclamped recursion is below \(e_B\), so
\[
 j=\frac{\log D}{3\log Q_*}+O(1).
\]
All bounds below are for sufficiently large N and are uniform across levels, admitted labels and environments. A bound \(D^C\) may have a fixed large exponent depending on the fixed parameters, not on i. Floors and ceilings contribute \(o(\Lambda)\) to the leading cost.

We use the following published results, with the classical large sieve, prime number theorem, linear sieve, Mertens estimates and ordinary number-field arithmetic. These analytic results are imports; their original proofs are not reproved here.

* Hildebrand–Tenenbaum, *Integers without large prime factors*, JTNB 5 (1993), 411–484, [DOI](https://doi.org/10.5802/jtnb.101), Thm. 1.1, Thm. 5.1 (p.447), Cor. 2.3. For \(u=\log x/\log y\) in the range \(1\le u\le\exp((\log y)^{1/2})\), the global smooth count and the direct interval count for \(xy^{-5/12}\le L\le x\) have relative error \(O(\log(u+1)/\log y)\) against \(x\rho_D(u)\) and \(L\rho_D(u)\), respectively. Also \(-\log\rho_D(u)=(1+o(1))u\log u\). Here \(\rho_D\) denotes Dickman's function; use \(\rho(x,y)=\Psi(x,y)/x\) below. The short interval theorem is used directly, not by subtracting global asymptotics.
* Hildebrand–Tenenbaum, *On integers free of large prime factors*, Trans. AMS 296 (1986), 265–290, [author's PDF](https://tenenb.perso.math.cnrs.fr/PPP/Psi%2B.pdf), Thm. 2(i) and Thm. 3, pp.268–269. With \(\beta=\beta(x,y)\) the saddle, \(\Psi(cx,y)/\Psi(x,y)=c^\beta(1+O(1/u+\log y/y))\) for \(1\le c\le y\); \(\phi_2(\beta,y)\asymp\log x\log y\) in our ranges. Implicit differentiation gives \(d\beta/d\log x=-1/\phi_2\). The saddle bound \(1-\beta=O(\log(u+1)/\log y)\) follows from Thm.2 (or the explicit estimate (2.1) in Harper below). Positivity \(1-\beta>0\) holds here since \(u\to\infty\).
* Drappeau, *Théorèmes de type Fouvry–Iwaniec pour les entiers friables*, Compos. Math. 151 (2015), [arXiv:1307.7554v3, Lemma 1(i), p.7](https://arxiv.org/abs/1307.7554v3), gives \(\Psi(x/a,y)\ll a^{-\beta(x,y)}\Psi(x,y)\) for every \(1\le a\le x\), \(x\ge y\ge2\). For \(a>x\) the count is zero. This also handles divisors that are not smooth, though their corresponding original smooth indicators are zero.
* Drappeau, *Sommes friables d'exponentielles et applications*, Canad. J. Math. 67 (2015), 597–638, [DOI](https://doi.org/10.4153/CJM-2014-036-5), Prop. 2.9 p.618 and Prop. 2.13 p.626, plus the zero-free alternative (1.2) and the definition of W p.619. See §5.1 for the precise small-conductor consequence.
* Harper, *Minor arcs, mean values, and restriction theory for exponential sums over smooth numbers*, Compos. Math. 152 (2016), 1121–1158, [accepted manuscript, Prop. 2 (4.1), p.23](https://wrap.warwick.ac.uk/id/eprint/107457/). The large-value estimate is for one bounded coefficient sequence and separated frequencies, with the lower threshold \(x^{-1/1000}\). We handle smaller values by the additive large sieve, as proved in §5.2.

The number-field certificate uses Lagarias–Odlyzko, *Effective versions of the Chebotarev density theorem*, 1977, Thm. 1.3, and Stark, *Some effective cases of the Brauer-Siegel theorem*, Invent. Math. 23 (1974), 135–152, [DOI](https://doi.org/10.1007/BF01405166), Lemma 8, p.145. Their ranges and factorial degree dependence are discussed in §8. The statements of the smooth interval, saddle ratio, dilation, large-value and exceptional-character estimates and Stark/Chebotarev statements were checked against the accessible source texts, not just against the KeyBreak bibliography.

For the rational smooth counts the endpoint log-size is between fixed positive multiples of \(d\Lambda_b\). For the algebraic counts (ordinary or semismooth, even after any of the fixed root/parent/modulus divisions below) it is between fixed positive multiples of \(d\log Y\). This follows from
\[
 \log(HM)=(11+6/\kappa+o(1))d\Lambda_b,\qquad
 \log(2X_i)<12d\Lambda_b+6d\log Y,
 \quad X_i=16(d+2)h_0 M V_i^d .
\]
The ratio \(\log Y/\log y\) is bounded by a fixed constant. Hence \(u\asymp d\), \(0<\gamma:=1-\beta=O(1/d)\), \(\gamma\log Y=O(\log D)\), and \(\rho(x,y)\ge e^{-C\Lambda}\) for all these algebraic endpoints. The corresponding bounds hold on the rational side with cutoff B; there \(\gamma\log Y\) need not be small at the highest levels, and is not used as such. In both cases \(\rho=x^{-o(1)}\). These comparisons imply the global and direct interval source ranges whenever the relative interval length is at least \(y^{-5/12}\) (respectively \(B^{-5/12}\)). The smallest interval grids used below have relative length \(e^{-o(\log y)}\).

## 2. Rational environment, window laws and uniform means

We first check the hypotheses of the source's finite lemmas B.1–B.10 in the changed experiment; the following is also a concise derivation of the range-dependent estimates.

### 2.1 Rational side

At the top, \(\log Y_0/\log M\to1/48\), \(\log V_0/\log M\to1/8\), and \(\log Y_1/\log M\to1/(48Q_*)\). In particular \(V_0^2/M\to0\) on the \(\log M\) scale. Use \(K_{\rm cell}=\lceil\exp(D^{1/6}\lambda^2)\rceil\). For a whole or cell numerator interval the sharp smooth-density lower bound is \(e^{-(3/8+o(1))\Lambda}\) for the whole interval at every level; the upper cell bound is \(O(\rho x/K_{\rm cell})\) by the direct interval estimate. The same lower bound applies to each top cofactor, and the complete-band aggregate loses only a factor comparable to \(1/\log Y_0\).

For each denominator interval of length \(L\asymp V/K_{\rm cell}\) and each unit class mod \(\ell>B\), the elementary lower/upper linear sieve at fixed s=3 gives \(\asymp L/(\ell\log B)\) B-rough integers: the individual inclusion-exclusion remainder is \(O(1)\), and the weighted remainder is \(O(B^3)\). The ratio of this remainder to the main term tends to zero because
\[
 K_{\rm cell}YB^3\log B/V \le K_{\rm cell}\log B/Y^2=o(1).
\]
Deleting the (single) excluded root and the primes of N has exactly the source's interpretation. In the convolution of the smooth numerator and rough denominator, the multiplicity is one by uniqueness of the full smooth part. The primitive-Q multiplicative large sieve with sequence length \(O(MV^2)\), followed by injective averaging over the r interval, gives B.20. Chebyshev and the union over roots and cell pairs give the B.8 failure upper bound
\[
 D^C K_{\rm cell}^4 \rho^{-1}(Y^{-8}+Y^4/M).
\]
All such bounds are \(o(1)\), uniformly even at the bottom, and remain \(o(1)\) after the polynomial union over the levels. The whole-box count is comparable to \(T_i/\ell\), where \(T_i=V^2\rho/\log B\); every cell contains at most \(C T_i/(\ell K_{\rm cell}^2)\). The determinant strip through one point meets \(O(K_{\rm cell})\) cell pairs in the (numerator,denominator) coordinates, hence the number of ordered distinct rationally eligible pairs with \(0<|\det(P,P')|\le cV^2/K_{\rm cell}\) is \(O((T_i/\ell)^2/K_{\rm cell})\).

For the top, use the complete bands of H.18 rather than one band beyond \(Y_0\). Their primes lie between \(Y_0^{127/128+o(1)}\) and \(Y_0\), above \(Y_1\). In B.12–B.16 replace the top-parent band lower scale by its actual lower endpoint P, while keeping the box \(V_0=Y_0^6\). The product convolution for the aggregate can have multiplicity at most \(\lfloor\log(xV_0)/\log P\rfloor=O(\kappa)\), since the smooth part determines the smooth cofactor and the possible parent primes divide the product. For an individual parent p the restriction \(p\nmid b\) gives multiplicity one after division by p. For the aggregate child lattice the nonprimitive points, where \(p\mid b\), are removed by the deterministic count in B.21. Relative to the main term this costs
\[
 O((\log B)/\rho_*\,[P^{-1}+Y_1/V_0+Y_1P/V_0^2])=o(1).
\]
The B.14–B.15 errors have positive fixed margins on the \(\log M\) scale; explicitly the ratios \(P^2/V_0^2,P/M,Y_1^4/V_0^2,Y_1^4/M\) do. The number of bands is polynomial in n. Thus there is a single environment event G of probability \(1-o(1)\) supplying all these counts, including the auxiliary child-root counts in each larger parent box. It depends only on g, not F or accepted searches. All remaining arguments average over the reference law \(\bar\mu=\mu(\cdot\mid G,Q\nmid N)\). A gcd discovery is immediate success, not conditioning on an event with unknown probability.

### 2.2 Finite evaluation laws

For the points above, \(P=(a,b')\) is primitive with \(0<a<b'\), \(b'\asymp V\), \(|G(P)|\asymp MV\) and \(\gcd(G(P),N)=1\). The two evaluation maps in B.3–B.4 have image \(\mathbb Z\) and, for two distinct primitive points, the index-\(\Delta=|\det(P,P')|\) lattice described in B.4. The integral kernels are generated by the primitive vanishing linear forms (or their product) times the remaining monomials, by Gauss's lemma. The rounding lifts therefore have coefficient size \(O(V)\) and \(O(V^2)\), respectively. Adding an independent uniform lift of a residue changes the box law in TV by at most \(O(d(1+V^2)/h_0)\). This yields the actual mixture of uniform windows on the selected evaluation columns. The w residue modulo \(|G(P)|\), or \(|G(P)G(P')|\), is uniformizable since evaluation at \((r,Q)\) maps the quotient to that cyclic group and sends \(\widehat F\) to N, a unit. The shift of selected columns is \(O(Wd^32^d)\) by the divided-difference identity in B.4; it does not contain \(1/\Delta\). The error from this reanchoring is \(O((Wd^32^d+1)/h_0+M^2 V^2/W)\). Substituting B.4's coefficient sizes bounds total error by \(O(E^{-4})\).

Condition on an admissible root modulo q for one or two points on its lattice. The unit coefficient in the root equation gives \(\Pr(R_{q,s})=1/q+O(h_0^{-1})\), so the conditional TV cost is at most \(O(qE^{-4})\). In the pair image, \(\Delta=q t'\), and the actual support after division is the odd ratio lattice
\[
 \mathcal L=\{(u,v)\text{ odd}:u\equiv\iota v\pmod{K}\},\qquad K=2t',\quad(\iota,K)=1.
\]
The lift of the multiplier modulo \(2\Delta\) uses the odd \(F_0\) coset; division by q retains every remaining power of q. This is exactly the B.4 construction, not a coprime or independence simplification. At the top the unconditioned version uses \(q=1\) and \(K=2\Delta\). The proof before conditioning is identical. In every case \(K\le4Y^{12}\) for the appropriate box.

For the comparison pair windows, set \(X_P=8(d+2)h_0|G(P)|b'^{d-1}/q\), \(s_P=X_P/[8(d+2)]\), \(\vartheta=b'_1 b'_2/\Delta\). The projection widths are comparable to \(s_P\), area to \(s_1s_2/\vartheta\), and vertical chord maximum \(L_2\asymp s_2/\vartheta\). In particular \(K/L_2\ll 2^d V^{2-d}/(HM)\); the determinant cancels. Row counting on this lattice gives the actual denominator \(\#(W\cap\mathcal L)=\operatorname{area}(W)/(2K)+O(L_2/K+w_1+1)\), by the total variation bound on the chord length function. The relative error is exponentially small, and a coordinate central strip of width \(2T\) has mass \(O(d(T+1)/X_P)\). Thus B.8's hypotheses hold for all determinants and window translates. The one-point mixture has uniform odd intervals of length comparable to \(X_P/d\). Every endpoint height above has logarithm \(\asymp d\log Y\); conditioning and all finite-law errors are \(e^{-\Omega(d\Lambda)}\).

### 2.3 Mean and upper-moment bounds

Use HT's interval theorem and ratio theorem for B.5. Every comparison one-point interval contains an outer subinterval of length comparable to its width with lower endpoint \(\gg X_P/d\) and relative length \(\gg1/d\). Smooth counts at odd integers are the difference of the counts at all integers and those divided by 2. This gives probability comparable to \(c_o(X_P,y)=2(1-2^{-\beta(X_P,y)})\rho(X_P,y)\), including intervals crossing zero (for the upper bound use an enclosing interval centered at zero). Dividing by an odd parent prime in a complete band gives the corresponding \(1/\ell\) times the density at \(X_P/\ell\). The root-divided scales \(X_P\) and \(X_i/q\) differ by at most \(e^{O(d)}\), so the saddle shift changes densities only by a fixed factor. Division by q or by a parent changes \(u\) by \(O(1)\). The TV cost divided by even the one-parent main term is \(o(1)\), because \(q,\ell\le Y_0\le E^{1/(2\kappa)}\) and \(\rho\ge e^{-C\Lambda}\). This proves the B.6 point and relation mean comparisons at the new parameters.

For clarity the B.9–B.10 upper pair moment does not use a distribution theorem for small smooth residues. In a progression \(a\bmod m\), set \(g=(a,m),W_1=L/m\) for an interval of length L. If \(g\) is not smooth no smooth value is possible. Otherwise a smooth \(n/g\ge W_1\) has a divisor \(e\in(W_1/y,W_1]\) coprime to \(m/g\); fixing e leaves at most \(W_1/e+1\) quotients. The dyadic sum and global dilation bound give
\[
 O\big(W_1\log(2y)\rho(X,y)(CXy/W_1)^{1-\beta(X,y)}\big).
\]
For \(f_J=\sum_{\ell\in J}w_\ell 1_{\{|u|\in\ell S_y\}}\) with a complete parent band and fixed bounded weight ratio, divide by \(\ell\) if \(\ell\nmid K\). When \(\ell\mid K\), a nonzero pair term requires the unique parent above y in the other coordinate to equal this \(\ell\); after division the modulus is \(K/\ell\). This exceptional term is bounded by the band sum times \(O(\log(2P))\), since a complete band has \(\asymp P/\log P\) primes. This is the only exceptional-parent cost. In the first coordinate use modulus two. Pad the positive/reflected fibre pieces (all outside \(T_j=X_j y^{-C_X}\)) to lengths at least \(\lambda_1=T_1/(Cd)\) and \(\lambda_2=T_2/(Cd(1+\vartheta))\). Both \(\lambda_1/(4Y),\lambda_2/(2YK)\ge2y\) eventually because their logs are \(\gg d\log Y\); all lower endpoint conditions follow by taking pieces of length at most their lower endpoint. The padding costs relative \(o(1)\) to the original area by the chord layer-cake argument in B.9: total padded length at most \(O(\lambda_j\log(2X_j))\) per fibre or projection. The powers arising from progression counts are bounded by \(D^C\) since \(K,\vartheta\le CY^{12}\) and \(\gamma\log Y=O(\log D)\) at the algebraic endpoints. Strip and TV errors normalized by the two densities are negligible by choosing \(C_X\) sufficiently large once. This proves B.10's pointwise product bound, both for ordinary smoothness and for any one complete parent band, including the top unconditioned ordinary test. The diagonal is bounded by \(v_{\max}\) times the mean. It remains to check that the means are large enough, as below.

Let \(\xi=\log Y/\Lambda_b\ge1\). The sharp Dickman estimate and the cutoff give, uniformly in i,
\[
 -\log \rho_{\rm alg}/\Lambda_b
 \le \min(2Q_*,(12+6\xi)/3)+o(1)
\]
where the global cap \(2Q_*\) makes the error uniform even at growing \(\xi\). The rational loss is at most \(3/8+o(1)\). Consequently the normalized band and ordinary own-level means have
\[
 \log\mu_{\rm norm}/\Lambda_b
 \ge 11\xi-(12+6\xi)/3-3/8-o(1)\ge37/8-o(1)>4.
\]
For the semismooth mean divide weights by their maximum, so a complete band costs only \(O(\log P)\) in density, not \(P\). The top ordinary mean uses \(p\le Y_0\) in the same bound. These estimates give the uniform exponential lower means and the required density \(p_{\rm den}=2^{-\lceil3259t/100\rceil}\), since \(2Q_*+3/8<32.59\). They absorb diagonal terms in B.10. All root-condition probabilities are comparable to \(1/q\). B.11 and B.13 now follow by the single child-root reordering of the actual incidences: the unmasked complete semismooth sum bounds the masked one above, and the lower comparison loses \(O(\log V/P)\) from parents dividing the denominator. The saddle ratio for a division by \(q\le y\) is comparable to \(q^{\gamma_e}\), uniformly over the parent band, because the variation of the saddle multiplied by \(\log q\) is \(O(1/d)\). In particular the normalized incoming second moments are polynomial in D times the fourth power of the profile comparison loss. No semismooth *concentration* is used in this note.

## 3. Local-density lemma with explicit finite errors

Here we prove the local part of C.4–C.9 at the enlarged moment parameters. Put
\[
 A=2^{j+10}m_b^3,\quad m=100000A,\quad
 a=\log2/(3\log Q_*)<1/12,\quad A=D^{a+o(1)},\quad
 z=R=D^{8A},\quad K_p=\lceil\log R/\log p\rceil .
\]
The following argument also works for \(A=(j+10)^3\), \(m=1000A\), with \(a=0\) (used later). Define \(Q_o=\prod_{3\le p\le z}p^{K_p}\), where p ranges over primes. This modulus is only an analysis device. Let \(\Theta=e^{D^{1/6}\lambda^2}\) and choose a deterministic positive/negative multiplicative grid of relative mesh \(\eta=D^{-10A}/(C_gd\Theta)\). For a reflected retained cell \(I=(x,x+L]\), \(L\asymp\eta x\). Put \(S=(u,Q_o)\), \(T=(u,K_o)\), \(K=2^vK_o\) even. The probability law P is uniform on the actual odd integers of I; the ideal law of S,T is the product of capped geometric valuation laws, with shared coordinates at overlapping primes. Fix
\[
 \log U=C_U\log(2z)(\Lambda+A\log D),\quad
 \log E_c=C_c\log(2z)(\Lambda+A\log D),
 \qquad
 \nu=\lceil(Ad+\log Y/\lambda)(\log D)^2\rceil .
\]
Constants \(C_U,C_c,C_X\) are chosen sufficiently large after the fixed density lower bound. Let
\[
 E_\nu=(\sum_{3\le p\le z}1/p)^\nu/\nu!,\qquad B_\nu=(1+z)^{\nu+1}.
\]

**Finite pattern comparison.** For a retained compatible pattern \(S=s\le U,T=\delta\), write \(u=s v'\). Oddness and all local constraints at primes of K can be imposed by a nonempty union of classes for \(v'\) modulo \(2K\). The other constraints are avoidances of primes \(\le z\) coprime to \(2K\). Bonferroni upper/lower sums truncated at two adjacent orders have absolute omitted density at most \(E_\nu\), and at most \(B_\nu\) individual endpoint errors. In each class the count with \(e\mid v'\) is \(L/(2Kse)+O(1)\); the number of classes cancels from the relative error, and the signed avoidance product is at least \(c/\log(2z)\). Including the normalization by the actual odd count gives the uniform relative error
\[
 \epsilon_{\rm ar}\ll z(E_\nu+UK^2B_\nu/L).
 \tag{1}
\]
For the full gcd T alone, counting classes modulo K gives relative error \(O(K/L)\) even for a rare content. In particular no inverse of the rare-pattern probability is used. The tail of S satisfies
\[
 \Pr_P(S>U)\ll z^C U^{-1/\log z}+Uz/L.
 \tag{2}
\]
Indeed any z-smooth divisor exceeding U has a divisor in \((U,Uz]\); summing divisibility counts gives this by Rankin with exponent \(1/\log z\) and the finite Euler product at \(1-1/\log z\). The endpoint errors are at most \(Uz\) in number. This works also for intervals of length comparable to \(X_P/d\) and for the full support interval, rather than a grid cell.

**Smooth numerator.** For either a prescribed small-prime pattern or a full content, its forced divisor s is at most \(S_0=U\) or K. If it has a nonsmooth prime the numerator is zero. Otherwise the inclusion-exclusion avoidance primes above y are automatically absent from the numerator. For \(e\le E_c\) in the avoidance sum use the HT direct interval theorem after division by \(se\) (also by 2 for oddness). Iterating the saddle ratio theorem through at most \(1+\log(S_0E_c)/\log y\) shifts of log-size at most \(\log y\), and integrating the saddle derivative, yields
\[
 \#(S_y\cap I/(se))=L\rho(x,y)(se)^{-\beta(x,y)}(1+O(\epsilon_{\rm an}))
\]
with
\[
 \epsilon_{\rm an}\ll \frac{\log(u+1)}{\log y}
 +\frac{1+\log(S_0E_c)/\log y}{u}
 +\frac{(\log(S_0E_c)+2\log y)^2}{\log x\log y}
 +(1+\log(S_0E_c)/\log y)\frac{\log y}{y}.
 \tag{3}
\]
All endpoints remain in the interval theorem range: \(\log(S_0 E_c)=o(\log x)\), \(L/x\ge y^{-5/12}\), even after the divisions; \(u\asymp d\) uniformly. The ratio of the absolute Euler sum to its signed product is \(\ll\log^2(2z)\). For small primes use \(\gamma\log z=o(1)\) and Mertens, comparing the logarithms of the products at \(\beta\) and 1 by \(O(\gamma\sum_{p\le z}\log p/p)\). The primes of K above z add a bounded product since \(\omega(K)z^{-\beta+1/\log z}=o(1)\). The tail \(e>E_c\) of the actual count is bounded by global dilation at \(x+L\), relative to the signed interval main term, by
\[
 O\big((x/L)\log^2(2z)E_c^{-1/\log z}\big).
\]
The same bound controls the omitted signed main tail. This follows by the Rankin factor \(E_c^{-1/\log z}\) inside the absolute Euler sum; the extra \(x/L\) is essential for a global-count upper bound. Thus the relative local density error is
\[
 \epsilon_{\rm loc}\ll
 \log^2(2z)\epsilon_{\rm an}+
 (x/L)\log^2(2z)E_c^{-1/\log z}+\epsilon_{\rm ar}+K/L .
 \tag{4}
\]
For the full gcd alone \(\epsilon_{\rm ar}\) can be omitted. This proves the product formula with the local factors
\[
 t_{p,k}(v;\gamma)=
 \begin{cases}
 p^{\gamma v}(1-p^{-\beta})/(1-1/p),&v<k,\ p\le y,\\
 p^{\gamma k},&v=k,\ p\le y,\\
 (1-1/p)^{-1},&v=0,\ p>y,\\
 0,&v>0,\ p>y .
 \end{cases}
\]
The common density is \(c_I=2(1-2^{-\beta})\rho(x,y)\). These expressions follow by exact divisibility and avoidance, so the capped (not exact) top valuation has no avoidance factor.

**High moment on small-prime patterns.** Under the ideal independent caps \(J_p\), the logarithmic derivative at zero of the p-factor is \((J_p-1/(p-1))\log p\) if \(J_p<K_p\), and \(K_p\log p\) otherwise. Its mean is zero, using \(E J_p=(1-p^{-K_p})/(p-1)\). For sufficiently small absolute \(c>0\), summing the geometric distribution gives \(E[(J_p+1/(p-1))^2e^{c(J_p+1/(p-1))}]\ll1/p\), independently of the cap. Taylor's inequality for the exponential, independence and \(\sum_{p\le z}(\log p)^2/p\ll\log^2(2z)\) give a bounded exponential moment for the centered sum divided by \(\log(2z)\). Taylor expansion of each log local factor has total remainder \(O(\gamma^2\log^2(2z))\), since its second derivative is \(O((\log p)^2/p^{1-\gamma})\). Thus the log product is \(\gamma\log(2z)W+O(\gamma^2\log^2(2z))\) with \(E e^{c'|W|}=O(1)\). From \(|e^v-1|\le |v|e^{|v|}\) and Hölder,
\[
 \left\|\prod_{p\le z,\ p\text{ odd}}t_{p,K_p}(J_p;\gamma)-1\right\|_m
 \ll m\gamma_{\max}\log(2z)
\]
when \(m\gamma_{\max}\log(2z)=o(1)\). This is uniform even for an outcome-dependent \(0\le\gamma\le\gamma_{\max}\), by the pointwise log-product bound. Its positive and negative fixed moments are bounded as well.

**Fourth moment on full content.** For a fixed integer r, geometric summation at a smooth prime gives
\[
 E[t_{p,k}^r]=a_p(1-p^{(-1+r\gamma)k})+p^{(-1+r\gamma)k},
 \quad a_p=\frac{(1-1/p)((1-p^{-\beta})/(1-1/p))^r}{1-p^{-1+r\gamma}}.
\]
Both the value and first derivative of \(\log a_p\) at zero give zero deviation from one. For \(r\gamma\le1/2\), the logarithm of the moment is \(O_r(\gamma^2(\log p)^2 p^{-1+r\gamma})\) and also \(O_r(p^{-1+r\gamma})\), uniformly in k. Split at \((1+\log(3K))^8\); below, \(\gamma\log\log(3K)=o(1)\), and above the sum is \(O_r(\omega(K)(1+\log(3K))^{-4})\). The nonsmooth-prime factors have moment \((1-1/p)^{1-r}\), whose product is bounded. The full-gcd marginal formula and (4) consequently give
\[
 E_{\pi_K}\big(E_P[f_y\mid T]/c_I\big)^4=O(1),\qquad f_y=1_{\{0<|u|\in S_y\}}.
 \tag{5}
\]
This is a fixed moment, not a bound on the fourth moment of the indicator normalized by its density.

**Explicit uniform errors.** Since \(a<1/12\), the chosen nu gives
\[
 -\log E_\nu\gg (Ad+\log Y/\lambda)(\log D)^3,\quad
 \log B_\nu=O((A^2d+A\log Y/\lambda)(\log D)^3)=o(d\log Y).
\]
The latter uses \(\log Y\gg d\lambda\) and \(2a<1/3\). The first dominates both \(m C\Lambda\) and \(\log K\) for every fixed C. The smallest retained cell length has logarithm \(\gg d\log Y\), since the near-zero strip cutoff is \(X_P y^{-C_X}\) and \(\log\eta^{-1}=O(D^{1/6}\lambda^2+A\log D)=o(\log y)\). Therefore (1) is exponentially negligible after any fixed density normalization and the needed m-th roots; the tail (2) divided by a fixed power of the minimum density is \(e^{-\Omega(\Lambda)}\) by choice of \(C_U\). In (3), \(\log(S_0E_c)/\log y\le D^{a+o(1)}\), the squared saddle term is \(D^{-1/3+2a+o(1)}\); the sharp factor \(\log^2(2z)\) in (4) yields
\[
 \epsilon_{\rm loc}\le D^{-1/3+4a+o(1)},\quad
 m\gamma_{\max}\log(2z)\le D^{-1/3+2a+o(1)} .
 \tag{6}
\]
These inequalities are the reason for the revised nu and \(Q_*>16\). The global-count tail in (4) is negligible since its exponent \(-C_c(\Lambda+A\log D)\) dominates \(\log(x/L)\), and the finite endpoint budgets are exponentially smaller. The source's weaker \(\log^4 z\) alternative would not suffice in U100.

## 4. A single fixed proxy and its principal residual

Let \(D_P^U(u)\) be the conditional mean of \(f_y\) on the complete cell and small-prime pattern of u, set to zero for \(S>U\) and the rounded near-zero strip \(|u|<X_P y^{-C_X}\). This is defined for each point before any pairing. Let \(a_P=E[f_y(F(P)/q)\mid g,R_{q,s}]\). On each one-point comparison window, the law is dominated by \(Cd\) times uniform odd counting on the full support. The random variable \(T_x=\log(X_P/|u|)\ge0\) has tail \(\ll\min(1,de^{-t'})\) and satisfies \(\|T_x\|_r\ll\log(2d)+r\). On retained cells \(T_x\le C_X\log y+O(\eta)\); the saddle shift from \(X_P\) to the cell location is \(\gamma T_x\) with log-error \(O_{C_X}(1/d)\) by (3) or the ratio theorem. Combining (1), (4), the score estimate and Hölder (at orders up to \(4m\)) shows that
\[
 \|D_P^U/c_o(X_P,y)-1\|_m
 \ll (Cd)^{1/(4m)}m\gamma_{\max}\log(2z)
 +O(\gamma_{\max}\log(2d)+d^{-1}+\epsilon_{\rm loc})+e^{-\Omega(\Lambda/m)} .
\]
In this expression the bound for discarded values uses (2) and the strip probability, since the normalized deviation of the *zero proxy* there is exactly -1. The TV transfer adds at most \(2c_{\min}^{-1}(CqE^{-4})^{1/m}\), negligible because \(m=o(d)\). There is no assumption of independence between size and valuations. Exact conditional averaging cancels the residual on complete cells separately on each retained pattern. The two partial endpoint cells have absolute residual sum at most twice their full smooth count. Their total relative window length is \(O(d\eta)\), their density at most \(D^C c_o(X_P,y)\) in the retained range. The discarded mass and TV error, normalized by \(c_{\min}\), are exponentially small. This gives \( |E D_P^U-a_P|\le c_o(X_P,y)(D^{-9A}+e^{-c\Lambda})\). Jensen/triangle inequality now centers the high moment at a_P:
\[
 \|D_P^U-a_P\|_m/a_P\le D^{-1/3000}
 \tag{7}
\]
eventually for U100. Indeed \(1/3-4a=\log(Q_*/16)/(3\log Q_*)>1/1449\). The proof also gives \(D^{-1/4}\) for \(A=D^{o(1)}\). In particular the true mean comparison follows without identifying \(c_o(X_P,y)\) with \(a_P\) exactly.

For the principal character in a pair of cells we need a small conditional residual against T, not simply the high-moment bound. Under the ideal valuation law, \(S,T\) are conditionally independent given \(V_*=(u,\gcd(Q_o,K_o))\), including overlapping nested caps. For any bounded test \(f\), \(E[E(f|S)|T]=E(f|V_*)\). Conditional on \(V_*\), the distinguished value of T has no extra valuation at primes above z or beyond the small-prime caps. Its conditional probability is at least \(c/\log(2z)\) (product of \(1-1/p\)); the total probability of the exceptional alternative is
\[
 \epsilon_0\ll \log K/(z\log z)+\log\log(3z)/R.
 \tag{8}
\]
The latter uses the union bound on \(p\mid K,p>z\) and on the next valuation beyond \(K_p\), whose probability is at most \(1/(pR)\). For a variable \(D_T=E(f|T)\), compare its within-\(V_*\) variance to its mean squared distance from its distinguished value. Cauchy–Schwarz bounds the two exceptional terms by
\[
 E[(D_T-E(f|V_*))^2]\ll
 (E D_T^4)^{1/2}\sqrt{\epsilon_0}\log(2z).
\]
This uses \(q(V_*)D_{\rm dist}^4\le E[D_T^4|V_*]\) and the lower bound on \(q(V_*)\). The conditional fourth moment must be normalized as in (5).

To transfer to actual P, extend the ideal joint law on S,T by attaching the actual conditional law of \(f_U=f1_{S\le U}\) on each retained joint pattern, and zero otherwise. Call it P'. By (1),(2) its TV distance from the actual joint law is \(O(\epsilon_{\rm ar}+\Pr(S>U))\). For the fourth moment on T, first compare the retained joint numerators *relatively* using (1) and the full-gcd marginal error \(O(K/L)\): \(E_{P'}[f_U|T]\le (1+o(1))E_P[f|T]\). Thus (5) transfers without inverse density powers. For bounded h and finite X, direct summation on fibres gives \(E_P|E_P[h|X]-E_{P'}[h|X]|^2\le4\,\mathrm{TV}(P,P')\); this follows by bounding the absolute difference of each conditional numerator and marginal. Apply it and contraction of conditional expectation to \(E_T(h-E_S h)\), writing its difference as three conditional-expectation terms. Replacing \(f_U\) by f costs its discarded mass in squared norm. Hence
\[
 E_{\pi_K}|E_P[f_y-D_I^U|T]|^2/c_I^2
 \ll \log(2z)\sqrt{\epsilon_0}
       +(\epsilon_{\rm ar}+\Pr_P(S>U)+K/L)/c_I^2 .
 \tag{9}
\]
On a retained rectangle this bounds the principal residual covariance by the product of the square roots of (9) at the two cells, after normalizing by their densities. The lattice modulus is K even and the content law is exactly \(\pi_K(\delta)=2\phi(K/\delta)/K\) for \(\delta\mid K_o\). In the actual rectangle the principal weights differ from these by \(1+O(K/L_{\min})\). Thus the relative principal error is \(D^{-4A+O(1)}\).

## 5. Nonprincipal residual: detailed conductor summation

### 5.1 Small conductors, including exceptional real characters

Take fixed endpoint envelopes
\[
 x_{-,r}=M/(64Y^7),\quad x_{+,r}=2MV,\qquad
 x_{-,F}=\frac{h_0M2^{-2d}Y^{6d-14}y^{-C_X}}{100(d+2)},\
 x_{+,F}=16(d+2)h_0 M Y^{6d}.
\]
They include every rational/algebraic prefix endpoint after root/content/induction division and parity halving, since combined content/induction divisors divide the relevant modulus \(\le4Y^{12}\). They are independent of g,F and the point pair. The algebraic log heights differ by \(O(d+\log Y+C_X\log y)=o(d\log Y)\), so \(x_{-,F}\ge x_{+,F}^{1/3}\) and \((\log y)^2/\log x_{+,F}\gg\lambda\). Here no use is made of the original source's numerical \(\log(HM)\le d\log Y\), which is false at the new bottom. The actual bound \(O(d\log Y)\) suffices.

For a primitive nonprincipal character of conductor at most \(\exp(u_X^{3/4})\), \(u_X=\log X/\log y\asymp d\), apply Drappeau with \(X=x_{+,F}\) and each endpoint \(x\in[X^{1/3},X]\). Write \(v=\log x/\log y\), \(h=\min(a_0\log y/\log_3 x,\sqrt{\log x})\), and choose height \(\mathcal T=e^h\), with \(a_0\) fixed sufficiently small as in his Prop. 2.13. The conductor bound has log \(O(v^{3/4})=o(h)\) since \(h\gg v/\log_3 x\). For a character not exceptional at height \(2\mathcal T\), the classical zero-free alternative gives the strip at gap \(\epsilon\asymp1/h\) up to height \(\mathcal T\); \(\log(q\mathcal T)=o(\log y)\), \(\epsilon\log y\to\infty\), and \(\log y/h^2=o(1)\), \(\log\log x/h=o(1)\). Thus all the range conditions used in the proof of Prop. 2.9 hold. Apply it with its x and z both equal to the endpoint x, twist zero. The smooth saddle count gives \(x^\beta\zeta(\beta,y)/\Psi(x,y)\ll(\log x)^2\); the relative error is \(O((\log x)^2(he^{-c\log x/h}+e^{-ch}))\), at most \(\exp(-u_X^{3/4})\) eventually.

For the possible exceptional primitive character, it is also exceptional at the smaller height \(\mathcal T\) by uniqueness. At its own conductor the exceptional W sum equals its smooth character sum times \(\tau(\chi)/\phi(q)\); the Gauss prefactor in Prop. 2.13 cancels. Its remaining relative upper bound is
\[
 O(e^{-cv/\log^2(v+1)}+e^{-a_0\log y/\log_3 x}
       +e^{-a_0\sqrt{\log x}}+(\log x)^{3/2}e^{-a_0\log x/\log Q_c}),
\]
where \(Q_c=\lfloor e^{u_X^{3/4}}\rfloor\). The factor \(x^{\beta_{\rm exc}-1}\le1\) was dropped. This estimate uses \(Q_c\le y^{a_0/\log_3 x}\) and \(v\gg(\log\log x)^5\), which follow from \(v\asymp d\) and \((\log y)^2\gg\log x\). Every exponential on the right beats \(e^{-u_X^{3/4}}\). Thus C.10 holds uniformly in the new algebraic envelope, without any Siegel-zero lower bound and without assuming a fixed exceptional character across all endpoints.

### 5.2 Large conductors and moving endpoints

For \(1/x\)-separated fractions the weighted additive large-value theorem (Harper Prop. 2) gives normalized p-energy \(O((\log x)^4)\) for values above \(x^{-1/1000}\), with \(p=12/5\): its distribution exponent \(2+20(1-\beta)+1/100\) is below p eventually. For the smaller values the additive large sieve bounds their p-energy by \(O(x^{-(p-2)/1000}/\rho(x,y))=o(1)\), because \(\rho=x^{-o(1)}\). This is the strengthening in [U40 §1](keybreak_unconditional_compression.md). Primitive Gauss sums give
\[
 \sum_{R'<r\le2R'}\frac1{\phi(r)}\sum_{\chi\bmod r}^{*}
 |S_x(\chi)/\Psi(x,y)|^2\ll (R')^{-2/3}(\log x)^4 .
\]
Indeed the Gauss orthogonality costs at most \(1/r\) times additive squared energy at the reduced fractions; Hölder over \(O((R')^2)\) fractions gives the exponent. The needed separation is \(4K_{\max}^2\le x_-\), \(K_{\max}=4Y^{12}\). On the rational side use the internal level bound \(31\log Y/\log M\le31/(48Q_*)+o(1)<1\); on the algebraic side \(\log K_{\max}=O(\log Y)=o(\log x_-)\). Both have \((\log x)^{21}\le y\le x^{1/100}\) (use B for the rational cutoff).

For maxima over prefixes in a dyadic range \(X/2\le x\le X\), decompose each prefix into at most one binary block at each scale. Cauchy–Schwarz costs \(O(\log X)\); the sum of squared block sums at one scale is exactly the expected squared sum with independent signs on those disjoint blocks. Each sign realization is one common bounded coefficient sequence, so the above bound applies, with denominator \(\Psi(X,y)\asymp\Psi(X/2,y)\). Sum over scales and then endpoint dyadic ranges to obtain, writing \(a(r),b(s)\) for the source C.51 primitive energies with endpoint suprema,
\[
 \sum_{r\ge R'}a(r),\ \sum_{s\ge R'}b(s)\ll D^C(R')^{-2/3}.
\]
Partial summation gives \(\sum\sqrt r\,a(r)\ll D^C\). On the algebraic side use §5.1 up to \(R_0=e^{cD^{1/4}}\) with c sufficiently small. Summing the bounded individual energies below \(R_0\), and the tail above \(R_0\), gives
\[
 \sum_{s\ge2}\sqrt s\,b(s)\ll D^C e^{-c'D^{1/4}} .
 \tag{10}
\]
The exact constant in the exponential is irrelevant.

### 5.3 Imprimitive characters and the common determinant

For a fixed content h and character modulo k induced from a primitive nonprincipal character mod r, the tested smooth sum after h division is
\(\sum_{e\mid\operatorname{rad}k,(e,r)=1}\mu(e)\chi^*(e)U_{he}(r,\chi^*)\).
In the odd algebraic test use only odd e and odd prefixes; subtract the even prefixes by \(\chi^*(2)S(x/2)\). Unsupported h,e (nonsmooth on the corresponding side) contribute zero. By global dilation and the primitive endpoint suprema, divide by \(\Psi(x,y)h^{-\beta_*}\) where \(\beta_*\) is the minimum saddle over the envelope. Weighted Cauchy–Schwarz with weights \(1/e\), followed by \(\phi(r)/\phi(k)\le(r/k)(k/\phi(k))\), gives the deterministic energy upper bounds
\[
 A_h(k)\ll L_K\sum_{er\mid k}\frac r k e^{1-2\beta_r}a(r),\quad
 B_\delta(k)\ll L_K\sum_{fs\mid k,\ f\ {\rm odd}}\frac s k f^{1-2\beta_F}b(s),
 \quad L_K\ll\log^2(2K_{\max}).
 \tag{11}
\]
In the first sum preserve \(q\nmid he\) when the query q>B. Here \(\beta_r,\beta_F\) denote the two minimum saddles, not conductor-dependent parameters. The \(r/k,s/k\) factors are essential.

For a pair of primitive points with \(\Delta=q t'\), the rational modulus is \(\Delta\), the algebraic one is \(2t'\). The exact lattice identity grouped by content and unit character gives the absolute rational pair-test upper bound
\[
 E_g[R_PR_{P'}]\ll
 \log M\,\rho_r^2 V^2
 \sum_{h\mid t',\,q\nmid h}h^{-2\beta_r}
   \big(\phi(qt'/h)^{-1}+ A_h(qt'/h)\big).
 \tag{12}
\]
To see this directly, map (r,Q) to the two rational numerator values by the determinant-\(\Delta\) linear map. This is injective with image a unit-ratio congruence lattice (use primitivity and a unimodular change of the two coordinates). Enlarge the prime-Q set to all integers in the rectangle and then its image to the full product numerator interval. Group the counts by common gcd h with \(\Delta\), expand multiplicative characters; the principal term and nonprincipal terms are bounded by (11) and dilation. Each numerator endpoint is of order \(MV\), the environment count is \(\asymp M^2/\log M\). This proves (12) with the actual factor \(\rho_r^2 V^2\). All discarded conditions, including roughness, can only decrease this nonnegative count.

For the algebraic f-f term on a retained grid rectangle, the normalized nonprincipal upper bound is
\[
 D^C\eta^{-2}c_1c_2\,t'
          \sum_{\delta\mid t',\,\delta\ {\rm odd}}\delta^{-2\beta_F}B_\delta(2t'/\delta).
 \tag{13}
\]
This follows from the same exact content identity modulo \(2t'\), with two different cell intervals. Cauchy–Schwarz bounds the product of the two character sums by their energy. The normalization is by the actual rectangle count \(L_1 L_2/(2K)(1+O(K/L_{\min}))\); each cell has \(L_j\asymp\eta x_j\) and \(\Psi(x_j,y)\asymp x_j c_o(x_j,y)\). The retained cell density is at most \(D^C c_j\), \(c_j=c_o(X_{P_j},y)\). This gives (13) with \(c_j\) the point references. To sum the rectangles inside or covering a comparison window, weight by their actual lattice counts; their total normalized weight is bounded for nonthin pairs by the geometry in §6 below. No count of grid cells is multiplied into (13).

Before averaging (12), cancel \(c_1c_2/\tau^2\ll(\log B)^2/(\rho_r^2 n_0^2)\), \(n_0=V^2/q\), using the pointwise mean on G. Removing the conditioning G then costs only \(1+o(1)\) on a nonnegative integrand. For each numerical s mod q and fixed signed determinant \(qt'\) there are \(O(n_0)\) primitive ordered point pairs: first choose one point in its root lattice, then the second solution differs by an integer multiple of the first primitive vector, whose denominator step exceeds the permitted interval width. Averaging the root with factor at most \(2/q\) (excluded root has zero rational count) and multiplying the factor \(V^2/n_0\) gives exactly \(q t'\), including the t' in (13). Consequently the band average of the nonprincipal term, divided by \(\tau^2\), is bounded by \(D^C\eta^{-2}\) times the sum over q in its complete dyadic band J and \(t'\le V^2/q\) of
\[
 \frac1{|J|}qt'\sum_{h\mid t',q\nmid h;\ \delta\mid t',\delta\ {\rm odd}}
 h^{-2\beta_r}\delta^{-2\beta_F}
 \big(\phi(qt'/h)^{-1}+A_h(qt'/h)\big)B_\delta(2t'/\delta).
 \tag{14}
\]

Here is the complete summation of (14). Enlarge \(t'\le V^2/\inf J=:T_0\). For the term with both nonprincipal energies put \(H_1=he,H_2=\delta f,r'=r/(r,q),s'=s/(s,2)\). The constraints in (11) give \(H_1r'\mid t'\), \(H_2s'\mid t'\), since \(q\nmid he\) and H2 is odd. The coefficient after expansion, excluding \(L_K^2\), is
\[
 \frac{rs}{2t'}H_1^{1-2\beta_r}H_2^{1-2\beta_F} a(r)b(s).
\]
Writing \(L_*=\operatorname{lcm}(H_1r',H_2s')\), we have \(rs/(2L_*)\le \sqrt{rs(r,q)/(H_1H_2)}\). The sum of \(1/t'\) over these multiples is at most \((1+\log T_0)/L_*\). The number of factorizations of H into the content and induction factors is at most \(\tau(H)\); \(\sum_H\tau(H)H^{1/2-2\beta}\) converges uniformly for \(\beta\ge\beta_0>3/4\). Average the extra factor \(\sqrt{(r,q)}\) over the complete q-band: if \(r\) is fixed, at most \(\omega_J(r)\le\log K_{\max}/\log\inf J\) primes q in the band divide it; the added contribution is bounded by \(D^C\) times the ordinary \(\sqrt r\) energy since \(|J|\gg\inf J/\log(\inf J)\). This proves that this part of (14) is \(D^C\sum\sqrt r a(r)\sum\sqrt s b(s)\).

For the rational-principal term, \(qt'/\phi(qt'/h)\ll h\log(2K_{\max})\). Expand the algebraic energy only. Bound \(\sum_{h\mid t'} h^{1-2\beta_r}\) by a fixed power of \(\log(3T_0)\): use its Euler product split at \((\log(3T_0))^2\), and \((1-\beta_r)\log\log(3T_0)=o(1)\). Then sum the coefficient \(H_2^{1-2\beta_F}s/(2t')\) over \(H_2s'\mid t'\); it is at most \((1+\log T_0)H_2^{-2\beta_F}\) since \(s/(2s')\le1\). The divisor function sum converges, giving \(D^C\sum b(s)\). These derivations retain all repeated powers of q and two and do not assume independence of the rational and algebraic modulus.

Combining with (10), (14) is \(D^Ce^{-cD^{1/4}}\). The \(\eta^{-2}\) factor in front is harmless by the scale hierarchy. This is the normalized, jointly averaged nonprincipal error, including the rational principal companion.

### 5.4 Proxy character sums

For a complete cell I and content \(\delta\), let \(k=K/\delta\). Fix a compatible \(S=s\le U\); after factoring out \(s_0=(\delta,Q_o)\) the additional forced factor \(a=s/s_0\) is coprime to k. The remaining small-prime avoidances outside k are handled by the same adjacent Bonferroni sums, since primes of k are already excluded by the character. Every main term is a nonprincipal character sum over a consecutive interval after a divisor has been removed; full periods cancel and the endpoint sum is \(O(k)\). The error is bounded by the positive difference of the adjacent Bonferroni sums, even for complex characters, because their absolute values are at most one. Since the proxy is constant on this pattern and cell and has values in [0,1], summing the at most U patterns and using \(\sum_{a\le U}1/a\le1+\log U\) gives
\[
 |\widehat D_{I,\delta}(\chi)|\ll U(k+1)B_\nu+
 (L/\delta)(1+\log U)E_\nu\quad(\chi\ne1).
\]
For mixed fD and DD terms use \(|\widehat f_{I,\delta}|\le O(L/\delta)\) and sum over characters (their number cancels \(1/\phi(k)\)). Then \(\sum_{\delta\mid K_o}\delta^{-2}\le\sum_{\delta\ge1}\delta^{-2}\). Dividing by the actual rectangle size and the two minimum smooth densities yields an upper error \(O(K\epsilon_D/c_{\min}^2)\), where
\[
 \epsilon_D=O(UK^2B_\nu/L_{\min}+(1+\log U)E_\nu).
\]
By §3's exponent checks it is exponentially negligible. This estimate uses neither an analytic character theorem for the proxy nor a bound on the number of its complete CRT patterns.

## 6. Assemble ordinary covariance, including discarded sets

For fixed g,q,s put \(Z=\sum_P R_P f_y(F(P)/q)\), \(\widetilde Z=\sum_PR_P D_P^U(F(P)/q)\), and \(\tau=EZ\). Minkowski and (7) give \(\|\widetilde Z-\tau\|_m/\tau\le D^{-1/3000}\), uniformly at fixed g and label.

For distinct points, first use the TV comparison in §2.2 with bounded residual test. Normalize the resulting absolute error by \(c_{\min}^2\), not by an additional rational-density factor, since the sum has at most \(O(\tau/c_{\min})^2\) rationally eligible pairs. The diagonal costs \(O(1/\tau)\) by \(f^2=f\), (7) and \(a_P\le1\). The near-zero coordinate strips have total pair mass \(O(d(y^{-C_X}+X_{\min}^{-1}))\), normalized by the same density squared. All these terms are \(e^{-\Omega(\Lambda)}\) by the fixed choices and §2.3.

Call a determinant thin if \(\Delta\le cV^2/\Theta\), choosing fixed c large enough for the subsequent rectangular covers. Its ordered-pair proportion among eligible pairs is \(O(\Theta^{-1})\) by §2.1. On every such pair, \(E f_1f_2\ll D^C c_1c_2\) by §2.3. The supremum of the normalized retained proxy is at most \(e^{C A(\log D)^2}\): its forced product is at most U, giving \(\gamma\log U=O(A(\log D)^2)\) and the remaining local factors and archimedean shifts give no larger contribution. Thus mixed and DD products are bounded by \(c_1c_2 e^{C A(\log D)^2}\), using the actual first moment for f. The normalized thin error is \(D^C e^{C A(\log D)^2}/\Theta\), which is \(o(D^{-4A})\).

For nonthin pairs, scale coordinates by \(s_1,s_2\); the window has bounded widths and area comparable to \(1/\vartheta\), with \(\vartheta=O(\Theta)\). The largest retained grid mesh is \(O(d\eta)\) in these coordinates. The boundary rectangles intersecting the window boundary thus have relative area \(O(d\eta\vartheta)=O(D^{-10A})\). Every rectangle has relative lattice count error \(O(K/L_{\min})\); the finite window denominator in §2.2 has exponentially small relative error. Therefore the sum of their lattice weights is \(O(D^{-10A}+e^{-c d\Lambda})\), and all interior/cover weights sum to \(O(1)\). We do not bound the error by an unweighted count of rectangles. On complete interior rectangles apply (9) to the principal residual, and §5.3–5.4 to the nonprincipal parts. On boundary rectangles bound a partial sum in absolute value by the full sum of \(f_1 f_2+f_1D_2+D_1f_2+D_1D_2\). Each principal product is at most \(C c_{I_1}c_{I_2}\) after rectangle normalization, by (5), the analogous fixed moment for D (from the score/finite count) and conditional Jensen. The nonprincipal parts of this positive majorant are bounded by the same absolute energies. Since \(c_I\le D^C c_P\) on all retained cells, the normalized boundary principal error is \(D^C(D^{-10A}+e^{-c d\Lambda})\). This is density-normalized; a bare absolute boundary error \(D^{-10A}\) divided by \(c_{\min}^2\) would not be sufficient.

Summing all pieces gives
\[
 E_{\rm base}\frac{(Z-\widetilde Z)^2}{\tau^2}
 \ll e^{-c\Lambda}+
 D^C\log(2z)\sqrt{\epsilon_0}
 +D^C D^{-10A}
 + O(c_{\min}^{-2}(K\epsilon_D+\epsilon_{\rm ar}+\Pr(S>U)+K/L_{\min}))
 +D^C\eta^{-2}e^{-cD^{1/4}}
 +D^C e^{C A(\log D)^2}/\Theta .
\]
Every constant is fixed independently of the complete query band. The leading term in (8) after square root and \(\log(2z)\) is \(D^{-4A+O(1)}\); the TV, tail and finite pattern terms were checked in §3. Also \(D^{1/4}\gg D^{1/6}\lambda^2\gg A(\log D)^2\). Hence the right side is at most \(D^{-4A+O(1)}\). Here the expectation is precisely over \(\bar\mu\), a uniform prime in the complete query band with primes of N deleted, a uniform admissible root and its raw root-conditioned F. Deterministic band mixtures preserve the bound. The ordinary proxy Markov estimate from (7), with \(m=100000A\), is \(o(D^{-10A})\) at threshold \(\tau/4\). Chebyshev for the residual yields
\[
 \Pr_{\rm base}(|Z-\tau|>\tau/2)\le D^{-3A}.
 \tag{15}
\]
This proves the changed-range ordinary C.3, rather than assuming it. The single-value truncation, rare-content projection, boundary control and common-determinant convolution are all essential. The proof does not give a pointwise concentration probability for each g or for a root drawn adaptively during Search.

## 7. From ordinary concentration to usable trees (U100)

Use the actual conditional-mean incidence weights (B.47),(B.62), including terminal and even-valuation incidences with zero bad indicator. At each complete parent band B.11 holds by §2.3. Positive band sums and pass-through edges retain the second-moment bound without independence, since \((\sum H_e)^2/(\sum a_e)\le\sum H_e^2/a_e\). The profile recursion (B.68) is a positive sum of powers \(q^{\gamma-1}\), \(0\le\gamma<1\), so it has within-band ratio at most two and compares to actual means with loss \(L_i\le D^{C(i+1)}\). This also verifies the change-of-measure B.64: root-event mass times the number of admissible roots is bounded above/below by constants, so deterministic band weights give \(d\sigma_i/d\beta_i\le C L_i^2\). The incoming density second moment is \(K_i^2\le D^C L_i^4\). The source's exact finite deletion argument (4.1)–(4.4) therefore uses \(\epsilon_i\le D^{-2A}\) by (15), \(T=D^{O(j+1)}\) and \(M_i\le n+1\). It yields
\[
 \delta_1\le 4T^2 D^{-\Omega(A/2^j)}
             =e^{-\Omega(m_b^3\log D)}.
\]
Apply this for each top private band with its own initial normalized weights. The good-state sets are independent of the weight choice, since they are defined by the exact pointwise ordinary means and deletions. The top B.13 identity and its upper second moment now give top normalized expected discarded mass \(e^{-\Omega(m_b^3\log D)}\), uniformly in the band. Pass-through contributes its identity edge; zero-mass layers are omitted.

The top unconditional ordinary second moment from §2.3 is \(D^C\) after normalization by each actual mean; no top covariance is needed. With \(J=2^{m_b^2}\) independent raw fields at fixed g, the empirical normalized count has variance at most \(D^C/J\); its rejected-field loss is at most \(D^{C/2}\sqrt{\rho_{\rm rej}}\) by Cauchy–Schwarz. The derivative rejection bound is \(O(H^{-1})\) (A.2, checked coefficient and unit-slope guards), exponentially small. The Chebyshev/Markov pool argument in D.2 therefore gives at least three quarters of every private band's parents with pooled usable count at least \(J\tau/2\) and total count at most \(5J\tau/4\), simultaneously with probability \(1-o(1)\) after the polynomial band union. This event is fixed before sampling any private root. All actual proposals choose a uniform slot, including rejected slots, and then a uniform legal geometric point with the source rejection sampler. Internal searches remain in that slot's field. No analytic rejection-conditioned law is substituted.

The source's H.5 broad-band shape count is entirely elementary; at \(k_0=\kappa d\) its lower bound has inverse exponent \(2\kappa/3=16\) in \(\Lambda\) units. Its guards are verified by \(k/k_0\to1\), \(J_b+1\asymp e_0/m_k\), \(e_{\min}>e_1\), and \(\omega(N)\log2=o(\log Y_{\min})\) from B-roughness. It does not assert smoothness equidistribution for an arbitrary set of good primes. The unique primitive shortest vector count cancels the square-class multiplicity with the number of private roots, even for nonsquarefree inputs. The source D.3 stopped search proof uses the fixed candidate density \(p_{\rm den}\) and the usable fraction at least 1/8, not independence of a candidate's children. Only verified candidates start child searches; the caps count every failed tree. The child multiplier \((q_s M_c+1)^{O(j)}=e^{O((\log D)^2)}\) is subleading. Thus the capped shape/search procedure obtains the source's constant success mass for \(C+1\) verified rows or an immediate factor.

## 8. Certificate and cost closure

The finite algebraic lemmas E.1–E.6 and row construction E.6 are unchanged by this parameter substitution. All field height and modular unit checks are retained. For completeness the following verifies the main inputs and why no extra algebraic oracle is introduced.

An accepted primitive odd-degree field polynomial is irreducible because the raw form is odd at primitive points and has fixed irreducible reduction mod 2. If its leading coefficient, content or derivative at the specified modular root has a proper gcd with N, return that verified divisor; the all-N derivative rejection has probability \(O(1/H)\) by the unit coefficient slope. For sufficiently large parameters \(8MH<N,2H+1<N\) and the raw height ceilings follow from the windows. The atom norms and their good-ideal valuations are obtained from the full verified raw factor lists, subtracting content factors; no factoring the leading coefficient or discriminant is required. In each field impose occurrence parity, small good-ideal parity, rational correction parity, shared norm parity, and quadratic character columns (E.27). Large good-ideal parities already vanish by completed descents; late bad-prime columns are zero-extended because earlier good large parities were even and earlier bad occurrences would have registered the prime. Every internal atom's rational correction \(Q/G(P)\) is included in the row identity, verified modulo N.

For \(H_D=\{\gamma:v_{\mathfrak p}(\gamma)\text{ even outside }D\}/K^{\times2}\), the source's S-unit/class-group and discriminant bounds (E.9) follow from the S-unit rank, 2-torsion in the S-class group, Minkowski and the local quadratic discriminant bound. The logs of the group-size and discriminant upper bounds are polynomial in n, even with the new field and pool heights. If an odd-degree K and a nonrational class \(\gamma\) yield \(L=K(\sqrt\gamma)\), then L has no quadratic subfield over \(\mathbb Q\): otherwise oddness gives \(L=KF\) for a quadratic F, making \(\gamma\)'s class rational. Stark's exact Lemma 8 applies also to nonnormal fields, with the \(4(2d)!\log|\Delta_L|\) denominator in the zero gap. Lagarias–Odlyzko Thm. 1.3 applies to the normal quadratic extension L/K, not to an unspecified Galois closure; its range is \(x\ge\exp(10[ L:\mathbb Q](\log|\Delta_L|)^2)\), with an exceptional \(\mathrm{Li}(x^\beta)\) term and absolute error \(O(xe^{-c\sqrt{\log x/[L:\mathbb Q]}})\). Use \(S=(2d)!T^4,x=2^S\) of E.12. Here T bounds the log discriminant and log group size, so the range and the exceptional suppression \((1-\beta)\log x\gg T^3\) hold uniformly; the other error also beats \(x/\log x\). The degree at least two primes have total count \(O(d\sqrt x)\). The same Chebotarev argument for K/K gives the degree-one supply. Consequently the probe success and separation probabilities E.3 hold at the new parameters, including all possible later row/dependency choices. A bounded ideal prime sampler uses checked rational primality and full linear-root enumeration; a slot is chosen with probability proportional to the number of roots so the degree-one ideals are uniform. The original capped coupling/union bounds apply with subleading J.

After parity selection a surviving field product has rational square class. Because d is odd the signed squarefree norm representative identifies that rational class; hence multiplying by it produces a field square. Clearing denominators and multiplying by the derivative places its integral square root in the monogenic order, by the trace-dual formula. Reconstruct by enumerating the at most \(2^d\) component root choices modulo a sampled prime, Hensel lifting above the coefficient bound and checking the square exactly. The modular evaluation uses only verified units. This is E.4, and no ideal/class group or integer factorization of a new large norm is used. The source E.5 invariance under the independent CRT sign actions on sealed private blocks holds verbatim. It gives proper-factor probability at least 1/2 on the public success event, for odd non-prime-power inputs; every other exit is a verified factor or a failed epoch.

The original bit-operation implementation in F.3–F.9 is applicable to these unchanged algebraic operations, with the new finite parameters and the value-size guard below. In particular all loops, including direct arithmetic and integer sampling, are capped except the recursive exact factorizations; the latter strictly shrink. Finding the fixed irreducible reduction mod two can be done by enumerating all monic degree-d binary polynomials and testing irreducibility, in \(2^{O(d)}\operatorname{poly}(n)\) work, absorbed by the direct budget. No cost is assigned to computing analytic means, profiles, grids or good-state tests: the program uses only the explicit numerical predicates. The ordinary rational smoothness predicate uses division by the base primes, not an auxiliary factoring oracle. Rejected samples and failed trees count. Storing/restoring the local frame at numerical calls is included in the source F.9 copy charges.

Use the actual raw-value sufficient guard \(500(12d^2m_b+6de_0)\le63(n-1)\); it holds eventually since \(3/\kappa=1/8<63/500\). Every called value is at most \(\lceil N^{63/500}\rceil\); coordinates at most \(\lceil\sqrt{2N}\rceil\). The finite invalid parameter cases and all failed epochs advance the persistent trial-divisor counter, ensuring every-tape termination by induction on the input. All prime factors and products are verified.

The logarithmic coefficient ledger, in units of \(\Lambda\), is: columns, retained data and precision 1; shape and search caps 17; raw trials and value calls 49.59; \(\log S^*/\Lambda=2/3+o(1)\) by Stirling; the direct probe cost \(64Q_\chi^2P\) has coefficient at most 28 since \(J\) and all field/degree/count factors apart from \(S^*\) are subleading. The F.9 direct terms have coefficients at most \(3,3,49.59+1,49.59+2,28,12\), all less than 53. The actual recursive coordinate and value call counts have coefficients 17 and 49.59 respectively. No claim is made that the total workspace has the earlier 19 coefficient.

Each epoch succeeds with probability bounded below by an absolute positive constant, conditional on its entry history; conditional expected costs of calls are taken with fresh coins at their actual input. For \(C_*=100\),
\[
 17+2^{-1/3}C_*<C_*,\qquad
 49.59+(63/500)^{1/3}C_*<C_*.
\]
These strict inequalities follow from the positive rational cubes \((83/100)^3>1/2\) and \((5041/10000)^3>63/500\). Together with \(53<100\), the strong induction in Section 6 (or the repository's [heterogeneous recurrence theorem](multilevel_descent_accounting.md)) gives the expected bit complexity of the complete verified output algorithm
\[
 \boxed{L_N[1/3,100]} .
\]
This is a written unconditional-route proof by reuse of the source's finite lemmas and the verified published analytic inputs, with the changed-range estimates derived explicitly in §§2–7. It is a fixed-input upper bound in the limsup convention. It is not a formal or independent peer-review certificate. In particular it does not rely on the proposed new semismooth concentration theorem for U40. We keep the original R manuscript and source comparisons distinct until the new proof receives independent review.

## 9. Remaining review tasks

The proof above is an inspectable source-based derivation, not a claim that the entire 144-page source has been mechanically checked. The exact numerical schedule checks in the [U100 receipt](keybreak_unconditional_fallback.md#6-exact-finite-check-receipt) are supporting evidence only. Independent review should focus on the finite pattern and covariance estimates (especially the boundary normalization, (9), and the shared determinant sum (14)), and on source E/F's bit-cost implementations. No new Lean build is claimed. The next step is to prove the extra semismooth full-content and character-sum estimates for linear exceptional-mass transfer at the U40 parameters.

Exact additional regression checks: [verification receipt](../verification/research/README.md#keybreak-ordinary-and-semismooth-proof-checks). The earlier U100 parameter checker was rerun on the same 18 symbolic schedules. The local covariance checker verifies exact content, projection, induction and determinant inequalities against direct finite arithmetic; its committed blob matches the locally executed version. No full repository, PDF or Lean rebuild was performed in this continuation.
