# Uniform squarefree saddle-point proof

**Status:** detailed written analytic proof of the deterministic manuscript's
Lemma "Uniform saddle expansion", including the covariance formula. The
classical strong PNT used below has already been separately kernel-checked;
the full argument here is not yet Lean-certified. All constants in the
bounds are uniform in the ranges specified in the manuscript. This does not
prove the subsequent conditional Gaussian laws or uniform positive Gram.

Write \(b_0=\log B\), \(u_x=x/b_0\), \(x=\log Z\), and
\(J\subset(\sqrt B,B]\) for the full set of primes in that interval
with at most \(O(L)\) primes removed, where \(L=\log N\).
We have \(b_0\asymp L^b\), \(u_x\asymp L^r\) with fixed positive
\(b,r\). In particular \(u_x\to\infty\), \(\log u_x=O(\log L)\),
and \(B^{-\epsilon}\) is smaller than any power of \(L^{-1}\).
All arguments apply also after removing a further \(O(L)\) primes.
Define
\[
 \phi(s)=\sum_{p\in J}\log(1+p^{-s}),
 \quad
 \phi_S(s)=\sum_{p\in J\setminus S}\log(1+p^{-s}),
\]
using the absolutely convergent Taylor logarithm for \(\Re s>0\).
There is no branch choice along any of the contours used here.

## 1. Saddle and uniform cumulants

For every fixed integer \(j\ge1\), differentiating the absolutely
convergent local logarithm series gives
\[
 \phi^{(j)}(s)=(-1)^j
 \sum_{p\in J}(\log p)^j\sum_{k\ge1}(-1)^{k-1}k^{j-1}p^{-ks}.
\]
For \(4/5\le\Re s\le1\), the terms with \(k\ge2\) are bounded
absolutely by \(C_j\sum_{p\in J}(\log p)^j p^{-2\Re s}\).
Indeed the power series \(\sum_{k\ge2}k^{j-1}v^{k-2}\) is
bounded on \(0\le v\le1/2\). Since \(p>\sqrt B\),
this error is \(O_j(B^{-2/5})\) times the sum of absolute first
terms. This bound holds for *every* imaginary part.

Put \(\lambda=(1-\alpha)b_0\) for \(\alpha\in[4/5,1]\).
Strong PNT and Abel summation, uniformly in this interval, give
\[
 T_j(\alpha):=\sum_{\sqrt B<p\le B}(\log p)^j p^{-\alpha}
 = (1+O_j(e^{-c'\sqrt{b_0}})) b_0^j
       \int_{1/2}^1 v^{j-1}e^{\lambda v}\,dv.
 \tag{1}
\]
Here the weight against \(d\vartheta(t)\) is
\(t^{-\alpha}(\log t)^{j-1}\). Its derivative has absolute
value at most \(C_j t^{-1-\alpha}(\log t)^{j-1}\) for large B.
The PNT error in the partial summation formula is therefore at most
\(C_j e^{-c'\sqrt{b_0}}\) times the integral plus the two endpoint
terms. At the upper endpoint the ratio of the endpoint term to the
integral is \(O_j((1+\lambda)/b_0)=O_j(1)\), using
\[
 \int_{1/2}^1 v^{j-1} e^{\lambda v}dv\asymp_j e^\lambda/(1+\lambda)
 \quad(\lambda\ge0).
\]
This also controls the lower endpoint. Removing \(O(L)\) primes
changes \(T_j\) by \(O(L B^{-2/5}b_0^j)\), negligible relative
to its main term uniformly.

On the real line,
\(-\phi'(\alpha)=\sum_p\log p/(1+p^\alpha)\)
is continuous and strictly decreasing because
\[
 \phi''(\alpha)=\sum_p (\log p)^2\,p^{-\alpha}/(1+p^{-\alpha})^2>0.
\]
At \(\alpha=1\), \(-\phi'\asymp b_0\); at \(\alpha=4/5\) it
is \(\asymp B^{1/5}\). The intermediate value theorem thus
gives a unique \(\alpha=\alpha_x\in(4/5,1)\) with
\(-\phi'(\alpha_x)=x\). It is a smooth function of \(x\) by the
inverse function theorem, with
\(\alpha_x'=-1/V_x\), \(V_x=\phi''(\alpha_x)\).
Equation (1) yields \(e^\lambda/(1+\lambda)\asymp u_x\).
Taking logs first gives \(\lambda\to\infty\) and
\(\lambda\asymp\log u_x\) (since \(\log(1+\lambda)=o(\lambda)\)),
then gives
\[
 \lambda=\log u_x+\log\log u_x+O(1),\qquad
 (-1)^j\phi^{(j)}(\alpha_x)\asymp_j u_x b_0^j .
 \tag{2}
\]
In particular \(V_x\asymp u_x b_0^2\). The complex derivative bounds
above and (1) give the same upper bounds on
\(|\phi^{(j)}(\alpha_x+it)|\) for all real t.
The omitted-prime logarithm difference and its j-th derivative are
\(O_j(LB^{-2/5}b_0^j)\), also for \(j=0\).

## 2. Central tail and Edgeworth expansion

Let
\[
 F_x(t)=\exp(itx+\phi(\alpha_x+it)-\phi(\alpha_x)),
 \qquad
 F_{x,S}(t)=\exp(itx+\phi_S(\alpha_x+it)-\phi_S(\alpha_x)).
\]
For \(a=p^{-\alpha_x}\) one has the exact identity
\[
 \frac{|1+ae^{-it\log p}|^2}{(1+a)^2}
 = 1-\frac{2a(1-\cos(t\log p))}{(1+a)^2}.
\]
If \(|t|\le 1/b_0\), then \(1-\cos(t\log p)\ge
c(t\log p)^2\). Apply \(1-z\le e^{-z}\), multiply over p,
and use (1) for \(j=2\). This yields
\[
 |F_{x,S}(t)|\le e^{-c V_x t^2},
 \tag{3}
\]
uniformly including the removed primes. We may replace
\(F_{x,S}\) by \(F_x\) inside the central integral with an
absolute error \(O(LB^{-2/5})\) times its Gaussian majorant:
the exponent difference is \(O(LB^{-2/5})\) uniformly and
\(|e^w-1|\le |w|e^{|w|}\). After scaling by \(\sqrt{V_x}\)
this is \(o(u_x^{-K})\) for every fixed K.

Write \(z=t\sqrt{V_x}\) and \(u=u_x\).
For \(|z|\le\log u\) Taylor's formula along the vertical
line, through degree five, gives
\[
 \log F_x(t)=-z^2/2+A(z)+D(z)+E(z)+R(z),
\]
where
\[
 A=\frac{(iz)^3\phi'''(\alpha_x)}{6V_x^{3/2}},\quad
 D=\frac{(iz)^4\phi^{(4)}(\alpha_x)}{24V_x^2},\quad
 E=\frac{(iz)^5\phi^{(5)}(\alpha_x)}{120V_x^{5/2}},\quad
 |R|\le C u^{-2}|z|^6 .
\]
The last bound uses the uniform sixth derivative estimate and the
integral Taylor remainder; the linear term vanishes by the saddle
equation. On this region
\(|A|\le C u^{-1/2}|z|^3\),
\(|D|\le C u^{-1}|z|^4\),
\(|E|\le C u^{-3/2}|z|^5\).
Thus \(|A+D+E+R|\le1\) for sufficiently large u. Expanding
the exponential through degree three and collecting terms of
order less than \(u^{-2}\) yields
\[
 e^{A+D+E+R}=1+A+D+A^2/2+E+AD+A^3/6
                   +O(u^{-2}(1+|z|^{24})).
 \tag{4}
\]
For example the fourth-order remainder is at most \(e|A+D+E+R|^4/24\);
each omitted monomial has at least two powers of \(u^{-1}\), and
degree at most 24 in z. This establishes the error without differentiating
any asymptotic estimate. The four terms \(A,E,AD,A^3\) are odd in z
and integrate to zero on the symmetric interval.

By (3) the part \(\log u<|z|\le\sqrt{V_x}/b_0\) has integral
\(O(e^{-c'(\log u)^2})\); the same estimate, allowing a polynomial
in \(\log u\), holds for the Gaussian polynomial terms integrated
over \(|z|>\log u\). The normalized Gaussian even moments of degrees
4 and 6 are 3 and 15, respectively, by integration by parts.
Consequently (4) gives
\[
 \frac{1}{2\pi}\int_{-1/b_0}^{1/b_0}F_{x,S}(t)\,dt
 =\frac1{\sqrt{2\pi V_x}}\left(
  1+\frac{\phi^{(4)}(\alpha_x)}{8V_x^2}
  -\frac{5\phi'''(\alpha_x)^2}{24V_x^3}
  +O(u_x^{-2})\right).
\]
The integral is real by conjugation symmetry. Both displayed
corrections are \(O(u_x^{-1})\), so it is strictly positive eventually.
Multiplication by \(e^{(\alpha_x-1)x+\phi_S(\alpha_x)}\)
proves the stated uniform expansion for \(I_{\rm pure}(e^x;S)\).

## 3. Derivative and one-sided ratio

Differentiate the finite central integral with respect to x, with
fixed B,J,S (the endpoints \(\pm1/b_0\) are fixed).
The differentiated integrand is the original integrand times
\[
 \alpha_x-1+it+\alpha_x'(x+\phi_S'(\alpha_x+it)).
\]
The modulus of the last bracket \(x+\phi_S'\) is at most
\(C |t| V_x+O(LB^{-2/5}b_0)\) by the saddle equation, the
complex second derivative bound, and the removed-prime bound.
Since \(|\alpha_x'|=1/V_x\), (3) bounds the derivative integral by
\[
 C\,e^{(\alpha_x-1)x+\phi_S(\alpha_x)}
       V_x^{-1/2}\bigl(|1-\alpha_x|+V_x^{-1/2}+o(1)\bigr).
\]
Division by the positive asymptotic above gives the claimed
\(O(I_{\rm pure})\) derivative bound. Differentiation is justified
by continuous differentiability on each compact x interval and
the finite t interval.

For the sharper one-sided comparison let
\[
 G(x)=(\alpha_x-1)x+\phi(\alpha_x)
      -\tfrac12\log(2\pi V_x)+\log(1+\kappa_1(\alpha_x)),
\]
with the two explicit correction terms making up \(\kappa_1\).
All derivatives of the displayed finite functions are legitimate.
The cumulant bounds imply
\[
 |\partial_\alpha^j\kappa_1|\ll_j b_0^j/u_x,\quad j=0,1,2.
\]
Indeed differentiating the two rational expressions uses at most
sixth derivatives, and each differentiation adds at most a factor
\(O(b_0)\) by (2). Also \(V_x'=\phi'''(\alpha_x)\alpha_x'\),
so \(|V_x'/V_x|\ll1/(u_xb_0)\).
It follows that
\[
 G'(x)=\alpha_x-1+O(1/(u_xb_0)).
\]
If \(x'\le x\) in the stated comparable u range,
\(\alpha_t\ge\alpha_x\) for \(t\in[x',x]\).
Thus
\(G(x')-G(x)\le (1-\alpha_x)(x-x')
 +O((x-x')/(u_xb_0))\).
The removed-prime logarithm difference is \(O(LB^{-2/5})\)
and the logarithm of the asymptotic ratio error is \(O(u_x^{-2})\).
Exponentiating proves the ratio bound, with an absolute bounded
prefactor absorbing the endpoint errors.

## 4. Covariance: exact second difference, not derivative of a remainder

The first derivative of the Legendre term is \(\alpha_x-1\);
its second derivative is \(-1/V_x\). Differentiating
\(V_x=\phi''(\alpha_x)\) twice gives
\[
 V_x'=\phi'''\alpha_x',\qquad
 V_x''=\phi^{(4)}(\alpha_x')^2+\phi'''\alpha_x'',\quad
 \alpha_x''=V_x'/V_x^2.
\]
By (2), \(V_x'/V_x=O((u_xb_0)^{-1})\) and
\(V_x''/V_x=O((u_xb_0)^{-2})\).
The chain rule and the bounds on \(\kappa_1\) show that the
second derivative of its logarithmic correction is
\(O((u_x^3 b_0^2)^{-1})\).
Therefore
\[
 G''(x)=-V_x^{-1}+O((u_x^2 b_0^2)^{-1}).
\]
Throughout \([x-2b_0,x]\), \(V_t/V_x=1+O(u_x^{-1})\),
by integration of its logarithmic derivative. For \(h_1,h_2\in[0,b_0]\),
the fundamental theorem of calculus twice gives exactly
\[
 G(x-h_1-h_2)-G(x-h_1)-G(x-h_2)+G(x)
 =\int_0^{h_1}\int_0^{h_2}G''(x-v-w)\,dw\,dv
 =-h_1h_2/V_x+O(u_x^{-2}).
\]
Each of the four actual log-integral values differs from G by
\(O(u_x^{-2})\), including their omitted-prime terms. This gives the
same second difference for the log integrals, with no differentiation
of the unspecified remainder. Exponentiating (the leading term is
\(O(u_x^{-1})\)) gives \(1-h_1h_2/V_x+O(u_x^{-2})\) for their
cross ratio. With \(h_1=\log p,h_2=\log p'\) and the manuscript's
weights, this is exactly
\[
 U^{\rm ex}_{\mathfrak q,\mathfrak q'}
 =m_{\mathfrak q}m_{\mathfrak q'}-
   \frac{m_{\mathfrak q}m_{\mathfrak q'}\log p\log p'}{V_x}
   +O((pp')^{-\alpha_s/2}u_x^{-2}).
\]
The first-moment estimate follows by integrating \(G'\) over a
distance at most \(b_0\), using
\(\alpha_t=\alpha_x+O((u_xb_0)^{-1})\) there:
\(I(x-\log p;\{p\})/I(x;\varnothing)
 =p^{1-\alpha_x}(1+O(u_x^{-1}))\).
For the evaluation-point shift \(|x-\log X_{\rm sc}|=O(L^t)\)
with \(t<b\), the saddle derivative gives
\(|\alpha_x-\alpha_s|b_0=O(L^t/(u_xb_0))=o(u_x^{-1})\).
This completes the covariance and first-moment calculations.

## Formalization boundary

The exact local product-decay inequality and prime-product counting
are in the verified core. To kernel-certify the above, construct
the finite complex logarithm sums and their differentiated series,
the uniform Abel summation estimate from the pinned PNT, the inverse
saddle with derivative, the Gaussian integral/explicit expansion
remainder, and the integral second-difference transfer. The written
proof is not itself a passing Lean endpoint, and no milestone is
marked checked solely from this note.
