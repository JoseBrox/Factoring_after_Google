# Uniform paired norm lifts with a fixed affine squareclass offset

27 November 2026. **Status:** new unconditional constructive square-aware norm representation for arbitrary public units, and a stronger shared-polynomial/constant-offset specialization. It solves the previously unproved *existence of a paired cofactor representation without supplied norm/image square compatibility*. It does not solve low-rank norm supply. Exact finite tests of both constructions give essentially full remaining squareclass rank, including negative smooth-squareclass results. No smaller factoring exponent is established.

This continues [square-resultant norm transport](square_resultant_norm_transport.md), [affine-core collision supply](affine_core_collision_supply.md), and [correlated conic sampling](conic_masked_incidence_supply.md). We use only monic polynomial resultants and explicit coefficient constructions, not a number-field class-group, unit or square-root oracle. A polynomial need not be irreducible or squarefree for the resultant identities used here; they concern the determinant of multiplication in a finite free algebra. This broader interface is deliberate. When prime-ideal language is used elsewhere, the necessary number-field hypotheses must still be checked.

## 1. Mark-local square pairing instead of a globally square cofactor

Let \(R=\mathbb Z/N\), let \(f\in\mathbb Z[X]\) be monic with a public root \(t\) modulo N, and let \(g\) be its monic modular quotient:
\[
 \bar f=(X-t)\bar g.
\]
For an explicit monic polynomial mark P, suppose
\(\bar g\equiv\bar Q^2\bmod\bar P\), with Q supplied. Then multiplicativity and monic remainder invariance of resultants give
\[
 (-1)^{\deg P}\operatorname{Res}(P,f)
       \equiv P(t)\operatorname{Res}(P,Q)^2\pmod N.
 \tag{1}
\]
For a monic f of odd degree, the signed resultant on the left is simply \(\operatorname{Res}(f,P)\); for general degrees keep the displayed sign. All needed evaluated factors must be units; a proper gcd is success. This is a known-square correction, not an assertion that a cofactor norm is abstractly a square.

For instance P can be any monic integer factor of an integer lift of \(g-Q^2\), with the quotient congruence checked. The identity requires square structure only at the chosen marks, rather than a global factorization \(\bar g=\bar h^2\). Thus the discriminant obstruction to the latter does not automatically apply. But merely generating such P by polynomial factorization does not bound \(|\operatorname{Res}(P,f)|\) or its squareclass support.

There is an alternative useful pair identity: if explicit marks \(L_+,L_-\) have opposite remainders modulo \(\bar g\), their cofactor resultant contributions have the same squareclass, up to the known sign \((-1)^{\deg g}\). It suffices that \(\bar g\mid L_++L_-\); no monicity of the marks is necessary because the quotient and f are monic. We exploit precisely this fact below.

## 2. A uniform constructive lift for every ordinary unit

**Theorem.** For odd N, every supplied unit \(u\bmod N\), a public integer \(2\le m<N\) coprime to N, and \(k\ge2\) with \(m^k>N\), one can construct, or obtain a proper gcd factor during the guards below, a monic f of degree \(2k+1\), two explicit marks \(L_+,L_-\), and a known unit c such that
\[
 f(m)\equiv0\bmod N,\qquad
 \boxed{ -\operatorname{Res}(f,L_+)\operatorname{Res}(f,L_-)
                       \equiv u c^2\bmod N. }\tag{2}
\]
The two resultants are verified units. This construction is uniform in u, uses no private root, and requires no prescribed norm/image compatibility as in the earlier interpolation theorem. Its bit cost is polynomial in \(k,\log N,\log m\) and the actual coefficient bit lengths, for the polynomial-size choices below. It is not a small **norm** theorem.

Preprocess primes at most \(4(k+1)(1+\operatorname{bitlength}N)\). This costs polynomial time for polynomial k (if a proper divisor is found, stop). We prove the construction for the remaining B-rough inputs; alternatively each guard may produce a proper gcd. Set \(n=\operatorname{bitlength}N\).

### Difference of squares and base polynomial

Choose a small positive integer \(a\le2n+1\), a unit, such that \(u\not\equiv a^2\pmod p\) for every \(p\mid N\). For each prime at most two values of a in this interval are forbidden, because the interval is shorter than p and all a are units. There are fewer than n distinct primes dividing N, so one such a exists. Test the gcds directly, not the factors p. Put, modulo N,
\[
 w=(u/a-a)/2,\qquad z=(u/a+a)/2 .
\]
Then w is a unit and \(z^2-w^2=u\). The value z need not be a unit. This is a public ordinary-unit parametrization; it does not purport to give a root of u. It also permits correlated conic input by taking \(w=1\) and the supplied public z when \(u=z^2-1\).

Write the nonnegative integer \(m^k-N<m^k\) in base m, with digit polynomial E of degree less than k, and set
\[
 F=X^k-E,\qquad D=(F-N)/(X-m).
\]
Here F and D are monic integral polynomials of degrees k and k-1, and \(F(m)=N\). Choose a monic degree-k polynomial \(R_0=X^k+E_w\) with \(E_w(m)\) the representative of \(w-m^k\bmod N\) in \([0,N-1]\), again using base-m digits. Thus \(R_0(m)\equiv w\).

For \(j=0,\ldots,kn\) try \(R=R_0+j(X-m)\) until \(\operatorname{Res}(D,R)\) is a unit modulo N. For each prime p and each distinct algebraic root \(\alpha\) of D mod p, if \(\alpha\ne m\), at most one scalar j can make \(R(\alpha)=0\); if \(\alpha=m\), R has the nonzero value w. Hence at most k-1 bad j residues per p, and at most that many integers in the scan, since p exceeds its length. A good j therefore exists. All tests are public resultants and gcds. Monicity is preserved since k≥2.

Define
\[
 f=F^2+(X-m)R^2,\qquad
 g=(f-N^2)/(X-m),\qquad A=R^2+FD .
 \tag{3}
\]
Then f is monic of degree \(d=2k+1\), \(f(m)=N^2\), and
\[
 g=R^2+(F+N)D=A+ND .
\]
In particular \(\bar f=(X-m)\bar g,\ \bar g(m)=w^2,\ \bar A=\bar g\). Over every residue field of a prime divisor of N, g and R are coprime: a common root would be a root of \((X-m)D^2\), but R(m) and its resultant with D are units. No discriminant factorization or squarefreeness of g is assumed.

Choose a monic degree-k digit polynomial \(Q_0\) with \(Q_0(m)\equiv z\bmod N\), and try \(Q=Q_0+j(X-m)\) for \(0\le j\le2kn\) until \(\operatorname{Res}(g,Q)\) is a unit. The same root count gives at most \(2k\) forbidden j per p, since g(m) is a unit. The strict preprocessing guard and \(\omega(N)<n\) guarantee a choice. Again this is a deterministic polynomial scan, not an assumed distribution of algebraic norms.

### Exact transport

Set
\[
 L_\pm=A\pm RQ,\quad
 n_\pm=\operatorname{Res}(f,L_\pm),\quad B=\operatorname{Res}(g,RQ).
\]
Modulo N the two cofactor remainders are \(\pm RQ\), and \(g\) has even degree \(2k\). The universal monic resultant product gives
\[
 n_\pm\equiv w(w\pm z)B \pmod N,\qquad
 -n_+ n_-\equiv u(wB)^2\bmod N .
\]
Here \(B\) is a verified unit by both guards, and \(w^2-z^2=-u\) implies \(w\pm z\) are units. This proves (2) with \(c=wB\bmod N\). The actual public representation is \(u=(-n_+n_-)c^{-2}\bmod N\). In the binary generator interface a common squareclass basis of these signed integer products suffices. No field-unit-log coordinates enter the certificate.

The coefficient heights of F,R,Q and f are bounded by polynomials in \(m,k,n\); in particular \(\log H_f=O(\log m+\log(kn))\). There is **no** imposed globally squared cofactor for f. The high coefficients occur in D and A. If k is the least integer ≥2 with \(m^k>N\), then the division recurrence gives \(\log H_D=O(L+\log m+\log k)\), \(L=\log N\). Hence the elementary Sylvester determinant bound yields \(\log|n_+n_-|=O(kL)\) for \(2\le m<N\). This estimate is much too large to imply quarter-scale smooth-squareclass supply at the degree \(k\asymp L^{1/2}/(\log L)^{1/2}\). It is only an upper envelope, not a claim that every actual norm must be that large.

## 3. Exact projector cost and low-height obstruction

The high coefficients just identified are not a removable detail of the construction. In the monic quotient \(\mathbb Z[X]/(f)\),
\[
 FA=NR^2 .
\]
This follows from \(F-N=(X-m)D\) and \(F^2=-(X-m)R^2\) modulo f. Use the resultant identities
\[
 \operatorname{Res}(f,F)=N\operatorname{Res}(F,R)^2,\quad
 \operatorname{Res}(f,R)=(-1)^k\operatorname{Res}(F,R)^2 .
\]
They follow by evaluating f at roots of the respective monic F and R and using the resultant sign. The guards make \(\operatorname{Res}(F,R)\) nonzero and a unit modulo N because \(\bar F=(X-m)\bar D\). Multiplication determinants in the monic quotient therefore give the exact formula
\[
 \boxed{\operatorname{Res}(f,A)
                =N^{2k}\operatorname{Res}(F,R)^2.}\tag{4}
\]
In particular A has large norm, although its image at m is the unit \(w^2\). Also
\[
 N n_\pm=(-1)^k\operatorname{Res}(f,NR\pm FQ)
\]
by multiplying \(L_\pm\) by F in the quotient. Division by N here is an exact integer resultant identity, not modular inversion of N.

The general obstruction is independent of this example. If a monic degree-d f has monic modular factor g of degree h and an explicit integer polynomial P is divisible by g modulo N, then
\[
 N^h\mid\operatorname{Res}(f,P).
 \tag{5}
\]
Indeed in \(\mathbb Z[X]/(f)\) take the integral unimodular basis consisting of the first \(d-h\) powers of X followed by a monic lift of \(\bar f/g\) times the first h powers of X. Multiplication by P kills these last h vectors modulo N. Its determinant is divisible by \(N^h\). This is valid for repeated prime powers of N as well as primes. If the resultant is zero, the divisibility assertion is trivial and does not yield a height obstruction; for coprime f,P over Q it is nonzero.

For paired marks \(L_++L_-\equiv0\bmod g\), apply (5) to their sum. If they have degree ≤m_0, coefficient bound H_P, and f has coefficient bound H_f, the nonzero-resultant case requires
\[
 hL\le m_0\log(\sqrt{d+1}H_f)
                +d\log(2\sqrt{m_0+1}H_P).
 \tag{6}
\]
This is Sylvester Hadamard, bounding the actual sum's height by \(2H_P\) and using monotonicity in m_0. In particular at the proposed half-log-height, degree-\(\asymp L^{1/2}\) scales, one cannot arrange equality/opposition of *whole* polynomial cofactor remainders at \(h=d-1\) using only uniformly small coefficients. A large known scalar in place of the sign would have to be charged in the same bound. The obstruction is not a lower bound on both individual norms \(\operatorname{Res}(f,L_\pm)\); a pair of very differently oriented, compact high-height elements could have small norms despite their large sum. This is a surviving possible mechanism.

## 4. Constant-offset specialization and one fixed norm environment

There is a stronger construction that genuinely produces the **same rational norm squareclass in one component for every target u**. It also reduces the other norm to one fixed monic polynomial. This addresses the affine offset issue in the previous collision-supply theorem. It trades more coefficient height for exact common structure, not for a proved low-rank remaining component.

Choose a fixed integer \(a\ge2\) coprime to N, \(m=a^2<N\). Take a monic integer polynomial F such that
\[
 F(0)=0,\quad F(m)=M=mN,\quad F'(m)\equiv1\bmod N.
\]
There is an explicit base-m construction: take k minimal with \(m^k>N\), a monic degree-\(k+1\) polynomial G with \(G(m)=N\) from negative base-m digits, and \(F_0=XG\). Choose T of degree less than k with \(T(m)\equiv(1-F_0'(m))/m\bmod N\) by base-m digits. Set \(F=F_0+X(X-m)T\); it retains its leading coefficient and degree \(k_F=k+2\). Put \(D=(F-M)/(X-m)\). Then
\[
 D(0)=N,\qquad D(m)\equiv1\bmod N.
\]
The polynomial D is fixed, monic of degree \(k_F-1\).

Given a public unit u, let \(w=(u/a-a)/2\bmod N\). If its gcd with N is proper, return that factor; if \(w=0\bmod N\), then \(u=a^2\bmod N\) already has a known root. Otherwise w is a unit. Choose monic S of fixed degree \(k+1\), with \(S(0)=0\) and \(S(m)\equiv w-1\bmod N\): take \(S=X(X^k+E)\) with digit \(E(m)\equiv (w-1-m^{k+1})/m\bmod N\). Set
\[
 R=1+DS,\qquad Q=R+aD,\qquad
 f=F^2+(X-m)R^2,\quad g=(f-M^2)/(X-m),\quad A=R^2+FD .
\]
Then R is monic of degree \(r=k_F-1+k+1=2k+2>k_F\) for k≥1, \(R(0)=1,\ R(m)\equiv w\), and \(R\bmod D=1\). (If k is small, increase the fixed degree of S by one to retain \(r>k_F\); all formulas below use only this guard.) We have \(Q(m)\equiv w+a\) and \((w+a)^2-w^2=u\), so the paired identity still holds:
\[
 -n_+ n_-\equiv u(wB)^2\bmod N,\qquad
 L_\pm=A\pm RQ,\ B=\operatorname{Res}(g,RQ).
\]
The norm-unit guards now hold without a search over j: modulo each prime divisor of N, g and R cannot have a common root since \(R\bmod D=1\) and R(m) is a unit. A common root of g and Q would, using \(R=-aD\) and \(m=a^2\), satisfy \(0=g=X D^2\). It cannot be a root of D, so it must be zero; but \(Q(0)=1+aN\equiv1\). Thus B is a unit.

Define the **fixed** integer
\[
 K=(-1)^{\deg D}\operatorname{Res}(D,M^2+X-m).
\]
Because R≡1 and F≡M modulo D, monic resultant invariance shows \(\operatorname{Res}(f,D)=K\), independently of u. Moreover \(K\equiv D(m)\equiv1\bmod N\), so K is nonzero and a unit.

We have \(L_-=D(F-aR)\). Since \(m=a^2\),
\[
 f=(F-aR)(F+aR)+X R^2 .
\]
Both f and \(X R^2\) have degree \(2r+1\), and \(F-aR\) has degree r and leading coefficient \(-a\). Replacement of f in the second argument of its resultant with \(F-aR\) by the same-degree polynomial \(XR^2\) therefore introduces no leading-coefficient factor. Resultant symmetry, multiplicativity, and \(F(0)-aR(0)=-a\) give
\[
 \operatorname{Res}(f,F-aR)=-a\,\operatorname{Res}(F-aR,R)^2 .
\]
Consequently
\[
 \boxed{n_-=-aK\,\operatorname{Res}(F-aR,R)^2.}\tag{7}
\]
This is an exact, public squareclass identity over the rationals. The first norm contributes a fixed rational squareclass for **all** u, even across the distinct f's. Its entire unknown prime support cancels from every affine difference. No norm factorization is required to obtain this saving.

The remaining norm also has a fixed presentation. Set
\[
 H=4MF+X(X-m)D^2,\qquad C=2F-XD-2aR .
\]
The monic H is fixed of degree \(2k_F\), and C has degree r, leading coefficient \(-2a\). In the monic quotient by f,
\[
 L_+(F-aR)=R^2 C .
\]
Indeed \(L_+=D(F+aR)+2R^2\), and multiplication by \(F-aR\) followed by \(f=0\) gives the displayed identity. Further,
\[
 4m f\equiv X H\pmod C ,
\]
by substituting \(2aR=2F-XD\) and \(F-(X-m)D=M\). The difference of the two polynomial degrees here is \(2(r-k_F)\), an even number. Taking resultants with nonmonic C introduces the leading-coefficient factor \((-2a)^{2(r-k_F)}\), which is a square. Also \(C(0)=-2a\). Using these equalities in multiplication determinants gives the exact identity
\[
 \boxed{
 n_+=2\operatorname{Res}(H,C)
        \left(\frac{\operatorname{Res}(R,F)}{(2a)^{k_F}}\right)^2 .
 }\tag{8}
\]
For detail, \((4m)^r\operatorname{Res}(f,C)=(-2a)^{2(r-k_F)}(-2a)\operatorname{Res}(H,C)\); the signs from switching f,C and extracting X cancel because f has odd degree and H has even degree. Divide the determinant identity for \(L_+(F-aR)=R^2C\) by the nonzero square factor in the norm of \(F-aR\). Since \(\operatorname{Res}(f,R)=(-1)^r\operatorname{Res}(R,F)^2\) and \(\operatorname{Res}(F-aR,R)=(-1)^r\operatorname{Res}(R,F)\), the quotient simplifies to (8). All denominators of the displayed rational correction are units modulo N: \(N\) is odd, \(a\) is a unit, and F,R have unit resultant from \(\bar F=(X-m)\bar D\) and the earlier guards. No inversion of an unknown factor is used.

Equivalently the final square-aware norm presentation has the particularly simple verification
\[
 \bar H=X(X-m)\bar D^2,\quad C(0)=-2a,\quad
 C(m)\equiv-u\bmod N,\qquad
 \boxed{\operatorname{Res}(H,C)
           \equiv 2a u\,\operatorname{Res}(D,C)^2\bmod N.}\tag{9}
\]
In fact (9) holds directly by multiplicativity for any C with those values and the unit guard; the derivation (7)–(8) establishes how it removes the varying-field paired norm terms. Thus the new affine sampler can use the single rational norm squareclass \(2a\operatorname{Res}(H,C)\) instead of both original norm products, with explicit known root correction. Its two field-dependent norm labels have been replaced by a fixed offset and a norm in one fixed monic algebra. H is allowed to be reducible; (9) is a determinant statement, not an asserted irreducible field with small discriminant. The construction of H has large coefficients involving M; it does not contradict the global square-cofactor height obstruction.

## 5. What these constructions do and do not supply

The new theorems produce a square-aware representation *uniformly* for arbitrary ordinary public units (and hence for the square-only ratio/mask sampler). They do not presuppose a square root of the input, including in the varying-field construction (2). The specialization has a provably fixed high-norm squareclass offset (7), not merely equality of ideal classes. It achieves a nontrivial exact compression of the original pair of algebraic norm expressions. But (8)–(9) leave a generally new large integer squareclass \(\operatorname{Res}(H,C)\) for each row. Neither the common environment H nor the known square corrections imply dependencies among those remaining integers. In fact (9) is equivalent to the direct norm problem for the fixed square-cofactor algebra, and it would be circular to assert that this norm automatically has a small squarefree part.

The following experiment checks this unresolved part without factoring huge norms or inferring anything from modular correctness alone.

Use exact gcd-free refinement of all signed integer norm products in a batch: recursively split any two positive different bases with a nontrivial gcd into their gcd and two quotients, deduplicating the basis. Every split decreases the sum of logarithms of the distinct factors by at least \(\log2\), so this terminates with pairwise coprime bases. Exact repeated division recovers every input exponent vector. Delete bases which are integer squares, include a sign axis, and take the other exponents modulo 2. These remaining disjoint-support nonsquare bases are independent in rational squareclasses, since each has some odd prime valuation. Thus the computed binary rank is **exact** for the given list without any prime factorization. Independently, the test for a squareclass supported at primes ≤B divides out all powers of those small primes and tests whether the remaining positive integer is a perfect square; it is also exact without factoring the large part. The sign is separately retained, not treated as an automatic square modulo N.

Tested script: [verify_projected_norm_supply.py](../verification/research/verify_projected_norm_supply.py), Python 3.13.5, SymPy 1.14.0. Local execution matched committed Git blob `ee01ccbd26b0a74f57b0aabe5c7518fda6644ad2`; SHA-256 `09d2630d978d676775c494cdd0fb7dce8fc57e12f455632ddb6a39d37b080896`. For the first sampler choose \(m=\lfloor\sqrt N\rfloor+1\) (increment to be a unit), \(k=2\), all units when fewer than 80, otherwise 80 seeded samples. Small fixtures deliberately skip gcd exits to isolate the transport. Every resultant identity, including (4), was checked exactly.

| N | verified rows | norm product bit sizes | exact rational squareclass rank |
|---:|---:|---:|---:|
| 77 | 60 | 56–93 | 60 |
| 899 | 80 | 89–114 | 80 |
| 1189 | 80 | 77–120 | 80 |
| 10403 | 80 | 121–155 | 80 |
| 1022117 | 80 | 197–234 | 80 |

All 380 lifts passed the guards and identities. Every one of these five batches has full squareclass rank; none of the rows has its absolute squareclass supported below or at 101 (nor 13 or 31). These are negative supply results for the tested choices, not statistical independence claims.

For the constant-offset version choose \(a=\lfloor N^{1/4}\rfloor+1\) (increment to be a unit), 24 seeded ordinary-unit trials per fixture, with exactly constructed F,D,H,R,C. In each accepted trial the original paired norms, (7), (8), and (9) were checked, including the fixed K and the exact squared factor of (8).

| N | accepted | rank after fixed-offset projection | projected norm bit sizes |
|---:|---:|---:|---:|
| 77 | 15 | 14 | 124–134 |
| 899 | 21 | 20 | 193–206 |
| 1189 | 24 | 23 | 197–207 |
| 10403 | 24 | 24 | 259–272 |
| 1022117 | 24 | 24 | 376–394 |

There were 108 verified lifts and 12 nonunit-w guard cases (the mathematical algorithm handles them by a gcd or direct known-square exit). Samples in this version were with replacement; the rank deficits must not be interpreted as nontrivial fresh random relations. No accepted projected norm had squareclass supported at primes ≤101. This tests the literal fixed-offset family, not a search over all admissible C or higher-degree compact norm-controlled representations.

The companion [projected norm parity obstruction](projected_norm_parity_barrier.md) shows that the previous determinant-scale collision barrier persists even after passing to rational norm parity in a fixed bounded-height field tuple. It does not exclude the large actual norm budgets here. The concrete problem left is therefore to exploit additional arithmetic structure of the **remaining fixed norm values**, or construct small actual squareclass norms with large compact logarithmic heights; simple whole-cofactor pairing of small marks is not enough. No quarter-scale collision mass or complete factoring theorem is claimed. No full repository, PDF or Lean rebuild was performed.


## 6. Subsequent homogeneous and normalized transport

The [normalized norm lattice theorem](normalized_norm_lattice_supply.md) replaces the fixed-offset endpoint prescriptions by one homogeneous ratio condition, using a new simple-endpoint environment. It proves exact Hensel normalization of arbitrarily prescribed finite powers of N and the lattice index \(N^{e+1}\). The original H of §4 has a repeated endpoint at zero and is not assumed to meet the new guards. Exact principal/localized depth equivalence identifies the redundant square-mask shifts and their fixed denominator corrections. Multiplication-matrix LLL reduces selected norm sizes on the new fixtures, but selected ranks remain full. Pooled multiple representations produce useful parity directions only on the smallest tested modulus. No quarter-scale arithmetic supply result follows. The [multiway norm parity obstruction](multiway_norm_parity_barrier.md) rules out replacing this missing supply merely by many more distinct-input samples under the bounded actual norm hypotheses.
