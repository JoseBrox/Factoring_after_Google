# Deterministic squarefree progressions from quasi-RH

**Status:** written alternative proof of the clean squarefree progression
asymptotic and principal windowed-saddle comparison in the deterministic
manuscript, conditional on the exact Dirichlet/zeta seven-eighths
nonvanishing theorem and the already written uniform saddle expansion.
This removes the need for the near-one zero-density theorem, Landau–Page
exceptional-character analysis, and the Gevrey cutoff in this particular
progression argument. It does not itself prove the conditional Gaussian
laws or the positive Gram construction. Full Lean checking is pending.

Use \(L=\log N,\ b_0=\log B,\ u_Y=\log Y/b_0,\ \alpha=\alpha_Y\),
\(\lambda=(1-\alpha)b_0\), \(V=\phi''(\alpha)\). Thus
\(u_Y\asymp L^r,\ \lambda\asymp\log u_Y,\ V\asymp u_Y b_0^2\)
by [the saddle proof](deterministic_saddle_proof.md).
In the manuscript's range \(u_Y\in[u/2,2u]\),
\(R=Y/S\in[K_1^{.8},K_1^{1.7}]\), and
\(q\le Q_{\max}=\exp(3L^{m_0})\), the strict comparisons
\[
 b<r,\quad k<r,\quad m_0-b<r,\quad \eta<r,\quad m_0<h
 \tag{A}
\]
hold. In particular \(\alpha\ge .99\) eventually. All constants below
are uniform in these parameters, including the at-most \(O(L)\)
deleted primes. Put \(T=\exp(L^2)\). Choosing this much larger
height than the original Mellin cutoff is harmless because the fixed
zero-free strip gives a logarithmic dependence on the height.

## 1. Sharp uniform twisted prime sums, including zeta's polar term

The [QRH witness proof](quasi_rh_witnesses.md) supplies the interior
logarithmic derivative bounds on \(15/16\le\Re s\le2\):
\[
 \left|\frac{L'}L(s,\chi)\right|\ll \log(q(|\Im s|+4))
 \quad(\chi\ne1),\qquad
 \left|\frac{\zeta'}\zeta(s)+\frac1{s-1}\right|
 \ll\log(|\Im s|+4).
 \tag{1}
\]
These are uniform in the modulus of an arbitrary (including
imprimitive) nonprincipal character. The second bound is for the
pole-removed log derivative; no uniform bound for the polar part
near the pole is asserted.

Let \([a,b]\subset[X,2X]\), \(X\ge2\), with any endpoint conventions.
Approximate its scaled indicator on \(v=n/X\) by the convolution
of its \(\delta\)-enlargement with a fixed nonnegative compactly
supported smooth mollifier of width \(\delta=X^{-1/64}\).
For large X its support lies in \([1/2,3]\). It differs from the
sharp indicator only within \(2\delta\) of the endpoints, is bounded
by 1, and its second derivative has L1 norm \(O(\delta^{-1})\).
The Mellin transform \(\widehat w(s)=\int w(v)v^{s-1}dv\)
therefore satisfies, by two integrations by parts in log v,
\[
 |\widehat w(\sigma+i v)|\ll
       \delta^{-1}(1+v^2)^{-1},\quad 15/16\le\sigma\le2 .
\]
Mellin inversion on line 2 and the absolutely convergent Euler
product give the weighted \(\Lambda(n)\chi(n)n^{-it}\) sum
as the integral of \(X^s\widehat w(s)(-L'/L)(s+it)\).
Move to the line \(15/16\). For nonprincipal characters there
are no poles. For zeta the crossed simple pole is at \(s=1-it\)
with residue \(X^{1-it}\widehat w(1-it)\), exactly the
continuous weighted integral of \(x^{-it}\).
Along the new line the polar term is bounded absolutely by 16.
Horizontal edges at heights tending to infinity eventually stay
away from the pole and tend to zero, by the \(v^{-2}\) decay.
The new vertical integral is
\[
 O\bigl(X^{61/64}\log(q(|t|+4))\bigr),
\]
since \(15/16+1/64=61/64\) and
\(\int_{\mathbb R}(1+v^2)^{-1}\log(|v|+4)dv<\infty\).
For the zeta case take q=1 in this bound.

The difference between the smoothed and sharp prime-power sum
is \(O((X\delta+1)\log X)\) by counting the integers in the
endpoint intervals. The continuous main term has discrepancy
\(O(X\delta)\), independently of t, since \(|x^{-it}|=1\).
Higher prime powers contribute \(O(\sqrt X\log^2 X)\).
It follows (with deliberately weakened exponents) that, uniformly
for \(\sqrt B/2\le X\le B,\ |t|\le T,\ q\le Q_{\max}\),
\[
 \sum_{a<p\le b}\chi(p)p^{-it}\log p
 = {\bf1}_{\rm all}\int_a^b x^{-it}dx+O(X^{1-1/100}),
 \tag{2}
\]
where the indicator means that all coefficients are 1 (the zeta
case). For nonprincipal characters it is zero. Indeed all log
factors are \(O(L^2)\) and \(\log X\gg L^b\), absorbing the
fixed exponent margin between \(1/64\) and \(1/100\).
The actual principal character modulo q differs from the all-ones
coefficients only on primes dividing q; these will be deleted
below. This proof needs no density theorem for zero counts.

Apply Abel summation with the real weight \(x^{-\alpha}/\log x\)
to (2), on each dyadic subinterval of \([\sqrt B,B]\).
The error is \(O(X^{1-\alpha-1/100}/\log X)\) per interval.
By the sharper saddle location, \(1-\alpha=\lambda/b_0=o(1)\)
and eventually \(1-\alpha<1/200\). Summing over \(O(b_0)\)
intervals gives \(O(B^{-c})\) for an absolute c>0.
Deleting \(O(L)\) primes has cost \(O(LB^{-\alpha/2})\),
also negligible. Consequently for every terminal subinterval
\([Z_1,Z_2]\subset[\sqrt B,B]\),
\[
 \sum_{Z_1<p\le Z_2,\ p\in J'}\chi(p)p^{-\alpha-it}
 =\begin{cases}
 \displaystyle\int_{Z_1}^{Z_2}\frac{x^{-\alpha-it}}{\log x}\,dx
                +O(B^{-c}),&\chi=1,\\
 O(B^{-c}),&\chi\ne1,
 \end{cases}
 \tag{3}
\]
where \(J'\) is \(J\) with all primes dividing q and the prescribed
omissions deleted. The number removed for q is at most
\(\log q/\log2=O(L^{m_0})\), and \(m_0<1\).
The same bound includes a subinterval with an endpoint exactly prime
by the additional single-prime error \(O(B^{-\alpha/2})\).

## 2. Terminal products and the full principal tail

Write \(Z_{\rm sf}=\prod_{p\in J'}(1+p^{-\alpha})\).
The saddle estimate (or (3) at t=0) gives
\(\sum_{p\in J'}p^{-\alpha}\asymp u_Y\) and hence
\(Z_{\rm sf}\ge e^{c u_Y}\).
For every nonprincipal character, uniformly in the terminal
cutoff \(p_b\) and \(|t|\le T\), the exact inequality
\[
 |1+z|^2=1+2\Re z+|z|^2\le\exp(2\Re z+|z|^2)
\]
gives
\[
 \left|\prod_{\substack{p\in J'\\p>p_b}}
             (1+\chi(p)p^{-\alpha-it})\right|
 \le\exp\left(\Re\sum_{p>p_b,\ p\in J'}\chi(p)p^{-\alpha-it}
                  +\tfrac12\sum_{p\in J'}p^{-2\alpha}\right)
 \le e^{O(B^{-c'})}.
 \tag{4}
\]
Here \(\sum p^{-2\alpha}\ll B^{(1-2\alpha)/2}\)
by comparison with the convergent integer series.
In particular the ratio to \(Z_{\rm sf}\) is \(O(e^{-c u_Y})\).
No choice of logarithm of a local Euler factor is needed.
Unlike the old argument, this does not need a case split on
the final prime p_b.

For the principal character put \(v=\log x/b_0\) and \(D=t b_0\).
Equation (3) implies
\[
 \sum_{p\in J'} p^{-\alpha}(1-\cos(t\log p))
 =\int_{1/2}^1\frac{e^{\lambda v}}{v}
                  (1-\cos(Dv))dv+O(B^{-c}).
\]
For \(|D|\ge1\) restrict to \([1-1/\lambda,1]\) (eventually
\(\lambda\ge2\)); the weight is at least \(e^{\lambda-1}\).
On any interval of length \(1/\lambda\), integrating the cosine
explicitly bounds the integral of \(1-\cos(Dv)\) below by
\[
 \frac1\lambda\left(1-
      \left|\frac{\sin(D/(2\lambda))}{D/(2\lambda)}\right|\right)
 \gg \frac1\lambda\min((D/\lambda)^2,1)\gg\lambda^{-3}.
\]
The first lower bound follows from Taylor's formula near zero,
strict \(|\sin z|<|z|\) on compact sets away from zero,
and \(|\sin z|\le1\) for large \(|z|\).
Since \(e^\lambda/\lambda\asymp u_Y\), the loss in the Euler
product is at least a constant times \(u_Y/\lambda^2\).
Using the local squared-norm ratio inequality from the saddle
proof and taking square roots proves
\[
 \frac{|\zeta_{J'}^{\rm sf}(\alpha+it)|}{Z_{\rm sf}}
 \ll \exp(-c u_Y/\lambda^2),
 \quad 1/b_0\le |t|\le T .
 \tag{5}
\]
This holds even at the large height T, because (3) does.

## 3. A fixed smooth cutoff suffices

Take a fixed smooth \(\omega\in[0,1]\) supported in
\([e^{-.31},e^{.31}]\) and equal to one on
\([e^{-.2},e^{.2}]\). Set
\[
 \widetilde W(x)=\omega(x/Y)\,S^{-1}e^{-\pi(x-Y)^2/S^2}.
\]
The discarded original Gaussian sum (even without the smoothness
or residue restriction), multiplied by q, is at most
\(Cq(1+S^{-1})e^{-cR^2}\), by integrating the decreasing
Gaussian tails and including their first integer endpoints.
It is negligible compared with the saddle main term.

In logarithmic coordinates \(v=\log(x/Y)\), the Mellin transform
is \(Y^{it}\) times the Fourier transform with positive sign of
\[
 g(v)= RY^{\alpha-1}\omega(e^v)e^{\alpha v}
                      e^{-\pi R^2(e^v-1)^2}.
\]
On the fixed compact support the substitution \(z=R(e^v-1)\)
has Jacobian bounded by \(C/R\); differentiating at most twice
and using Gaussian polynomial moments yields
\(\|g\|_1\ll Y^{\alpha-1}\) and
\(\|g''\|_1\ll R^2Y^{\alpha-1}\).
For example each differentiated Gaussian is bounded by a constant
times \(R^j(1+|z|^{2j})e^{-\pi z^2}\) for \(j=0,1,2\);
the other factors and their two derivatives are bounded.
Thus by two integrations by parts
\[
 |\widetilde M(\alpha+it)|\ll
 Y^{\alpha-1}\min(1,R^2/t^2),\quad
 \|\widetilde M\|_1\ll RY^{\alpha-1},\quad
 \int_{|t|>T}|\widetilde M|dt\ll R^2Y^{\alpha-1}/T .
 \tag{6}
\]
For \(|t|\le1/b_0\), substitute \(x=Y+Sz\).
On \(|z|\le c_0R\), where the cutoff is identically one,
Taylor's formula for \((1+z/R)^{\alpha+it-1}\) has uniformly
bounded second derivative in z/R. The linear term integrates to
zero by symmetry, and the Gaussian has finite second moment.
The complement is exponentially small. Therefore
\[
 \widetilde M(\alpha+it)=Y^{\alpha+it-1}(1+O(R^{-2})).
 \tag{7}
\]
The error in the central saddle integral relative to its main term
is \(O(R^{-2})\), by the Gaussian central bound from the saddle proof.
For the principal tail up to T, use (5) and (6):
its relative size is \(O(R\sqrt V e^{-c u_Y/\lambda^2})\).
For larger t use the trivial Euler-product bound and (6),
giving \(O(R^2\sqrt V/T)\). By (A) and
\(\log R=O(L^k)\) both are \(o(R^{-2})\).
Hence
\(I(Y,S;S_{\rm tot})=I_{\rm pure}(Y;S_{\rm tot})(1+O(R^{-2}))\).
There is no need for the original Gevrey derivative estimates.

## 4. Exact two-prefix reduction

For q=1 there are no nonprincipal characters. For q>1, the
supported squarefree smooth integer n satisfies
\(n\ge e^{-.31}Y>q^2B^2\), by (A).
Order its primes increasingly. The first shortest prefix m1
strictly exceeding q has \(q<m_1\le qB\) and last prime p_a.
The next shortest prefix m2 strictly exceeding q exists because
\(n/m_1>qB\); it has \(q<m_2\le qB\) and last prime p_b.
The remaining primes are all greater than p_b. Both prefixes
are determined uniquely, including when m1 or m2 has one prime.
Their factors are in disjoint prime ranges, so any choice of
the two allowed prefixes and remaining subset has exactly
this decomposition. Integers outside the cutoff do not
contribute after Mellin inversion.

For fixed p_a,p_b, let \(A_\chi,B_\chi\) denote the two sums
of \(\chi(m)m^{-\alpha-it}\). The quotients \(m_1/p_a\)
and \(m_2/p_b\) are at most q, by shortestness; actually they
are less than q, because they are coprime to q and q>1.
They are distinct integer representatives, so multiplication
by the unit final prime gives distinct residues.
The number of terms in each prefix sum is at most
\(\varphi(q)\). Exact Parseval gives
\[
 \sum_\chi |A_\chi|^2=\varphi(q)\sum_{m_1}m_1^{-2\alpha}
       \le\varphi(q)^2q^{-2\alpha},
\]
and the same for B. By Cauchy–Schwarz,
\[
 \frac q{\varphi(q)}\sum_\chi |A_\chi B_\chi|
       \le q\varphi(q)q^{-2\alpha}\le q^{2(1-\alpha)}.
 \tag{8}
\]
The verified Prefix module already gives the exact Parseval identity.
Notice that one must apply the representative bound to the quotient,
not to the full prefix which can exceed q.

Apply Dirichlet character orthogonality to the windowed sum.
The principal term is \(qI/\varphi(q)\).
On \(|t|\le T\), substitute the unique decomposition for each
nonprincipal character, use (4) and (8), and sum over at most
\(B^2\) pairs of terminal primes. Relative to the saddle main
term \(I\asymp Y^{\alpha-1}Z_{\rm sf}/\sqrt V\), the error is
bounded by
\[
 C B^2 R\sqrt V\exp(2(1-\alpha)\log q-c u_Y).
\]
The logarithm of every positive factor is
\(O(L^b+L^k+L^{m_0-b}\log L+\log L)=o(L^r)\)
by (A). Thus the relative error is \(O(e^{-c' u_Y})\).
There is no extra factor \(\varphi(q)\) lost here: it is precisely
the two-prefix L2 argument that absorbs the number of characters.

One may either use the same decomposition on \(|t|>T\)
with the trivial terminal-product bound \(Z_{\rm sf}\), or bound
the original undecomposed full Euler product there. The first
choice gives relative error \(O(B^2 q^{2(1-\alpha)}
R^2\sqrt V/T)\), by (6) and (8); the second gives
\(O(qR^2\sqrt V/T)\). Both are \(O(e^{-L^2/2})\).
Since all terms are finite Dirichlet polynomials, there is no
interchange-of-infinite-sums issue. Mellin inversion is justified
by (6). The initial replacement of W by its cutoff has the
negligible error already bounded in Section 3.

We obtain, for **every** modulus in the specified range,
\[
 \Sigma(Y,S;q,a_0,S_{\rm om})=
 \frac q{\varphi(q)} I(Y,S;S_{\rm tot})
       (1+O(e^{-c_\delta L^\eta})).
\]
The error exponent follows from \(r>\eta\), and
\(I=I_{\rm pure}(1+O(R^{-2}))\) was separately proved above.
This is the deterministic clean progression proposition with
the cleanliness condition removed, conditional on QRH.

## 5. What is and is not discharged

The actual medium and high exceptional zero-location sets in the
deterministic manuscript are empty for large N under QRH since
\(1-\nu_0>7/8\); the possible Landau–Page real zero in its much
narrower near-one strip is also absent. In particular there is no
exceptional generator-prime deletion. Equations (2)–(8) replace
the entire quantitative character-sum argument without assuming
a new smooth-progression oracle. The fixed-strip log derivative,
sharp Mellin estimate, cutoff integration by parts, and saddle
asymptotic still require Lean certification. The next deterministic
analytic step is to transfer the progression theorem into the
actual one-point and two-point Gaussian laws, and then audit
the Gram matrix with its exceptional-conductor deletions removed.
No new general factoring exponent is claimed merely from this note.
