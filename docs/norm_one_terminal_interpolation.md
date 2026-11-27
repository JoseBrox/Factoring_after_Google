# Shared norm-one terminal units and interpolation rigidity

27 November 2026. **Status:** unconditional construction of shared exact-norm-one marks for arbitrary modular unit targets, and a stronger proved rank obstruction for linear-mark interpolation. This is a new terminal-relation building block, not a sub-one-third factoring algorithm. It follows the [projective discriminant diameter bound](projective_discriminant_barrier.md) and [probe-free unit certificate](exact_descent_unit_certificate.md). It controls *actual* norms, even when coefficient height envelopes are large.

## 1. Arbitrary modular targets in a single odd-degree field

Let \(N\ge3\), and let \(s_1,\dots,s_k\in(\mathbb Z/N)^\times\) be any explicitly supplied list, with repetitions allowed. Check unit gcds first in an algorithm. Choose odd \(d\ge3\) with \(d-1\ge k\) and \(d\le k+3\). Pad the list to \(d-1\) by units 1, and set
\[
 s_d=(s_1\cdots s_{d-1})^{-1}\pmod N.
\]
Use representatives \(0\le \widetilde s_i<N\), and distinct integer marks \(r_i=4iN-\widetilde s_i\). Define the monic polynomial
\[
 f(X)=\prod_{i=1}^{d}(X-r_i)-1.
\]
Then \(f(0)\equiv0\pmod N\), because \( -r_i\equiv s_i\) and their product is 1. The construction has polynomial bit cost in \(k,\log N\); all coefficient bit lengths are \(O(d\log(dN))\).

**Irreducibility.** If the monic f were reducible over \(\mathbb Q\), Gauss's lemma supplies a nonconstant integer factor g of degree at most \((d-1)/2\). Since \(f(r_i)=-1\), each \(g(r_i)=\pm1\). Thus \(g^2-1\) has at least d distinct roots and degree at most \(d-1\), impossible for nonconstant g. No probabilistic irreducibility assertion is used.

**Real embeddings.** At \(r_i\pm1/2\) the product of linear factors has opposite signs and absolute value at least \(\tfrac12(3N-1/2)^{d-1}>1\). Consequently f has a root in each of these d disjoint intervals. They are simple and exhaust its roots. All this may be verified by exact rational sign tests.

**Norms and images.** In \(K=\mathbb Q(\theta)\), \(f(\theta)=0\), define \(u_i=\theta-r_i\). These are algebraic integers with
\[
 \prod_{i=1}^d u_i=1,\qquad
 N_{K/\mathbb Q}(u_i)=(-1)^d f(r_i)=1 .
\]
They are units in \(\mathbb Z[\theta]\) itself (the explicit inverse is the product of the other u's). The evaluation map \(\psi:\mathbb Z[\theta]\to\mathbb Z/N,\ \theta\mapsto0\), sends \(u_i\) to \(s_i\). This gives a common field, explicit norm-one terminal elements, and a verified modular evaluation, with no smoothness search, factorization of N, or character probes.

The rank, however, must be charged. Let \(\theta_j\) be the real root in the j-th interval and \(M_{ji}=\log|\theta_j-r_i|\). Every row sums to zero by the product identity, and every off-diagonal entry is strictly positive by the separation of the marks. Thus the real kernel of M consists exactly of constant vectors: in a maximum coordinate of a vector c with \(Mc=0\), use \(0=\sum_{i\ne j}M_{ji}(c_i-c_j)\) to conclude that all coordinates equal that maximum. Hence the only integral multiplicative relations among the u's are multiples of \(\prod u_i=1\). In particular the first k prescribed unit images have **k independent unit-log directions**. Replacing k rational labels by these k units is rank-neutral, even though it removes their finite ideal support completely.

This theorem applies to a whole shared batch of arbitrary rational prime requests, without having to represent those primes by short linear forms at the same rational height. The field coefficients need not meet the old quarter-scale uniform envelope; the norm of every mark is exactly one, and their binary data are polynomial in the actual batch data. But it gives no rank saving by itself.

## 2. A more flexible interpolation route and its rigidity theorem

One might try to eliminate the balancing unit and reduce the unit rank by choosing a polynomial with many prescribed norm-one linear marks but a predominantly complex signature. The following theorem screens this approach under explicit, broad separation guards. It is not confined to polynomials with all real roots.

Let \(r_1,\dots,r_k\) be distinct integer marks, \(k\ge2\), with
\[
 S=\min_{i\ne j}|r_i-r_j|,\qquad H=\max_i|r_i| .
\]
Put \(P(X)=\prod_{i=1}^k(X-r_i)\). Let \(Q(X)\) be any monic integer polynomial of degree \(m\), \(1\le m<k\), and set
\[
 f(X)=P(X)Q(X)-1,\qquad d=k+m .
\]
Assume f irreducible over \(\mathbb Q\). The theorem only needs separability and the full d-embedding log matrix for its analytic part; irreducibility gives the stated field/unit interpretation. The arbitrary integer coefficients of Q need not satisfy any height bound.

Require the following explicit guards, where \(C=\max(8,(2H+2)/(S-4))\):
\[
 \begin{gathered}
 S-4\ge64,\qquad (S-2)^{k-1}>[4(m+1)]^m,\\
 \frac{4d\log(2H+2)}{(S-2)\log(S-2)}\le\tfrac12,\qquad
 (S-4)^{k-m}>C^{2m}. \tag{1}
 \end{gathered}
\]
They hold, for example, for the lifted marks \(4iN-\widetilde s_i\) of §1 with \(k=O((\log N)^{1/2})\), uniformly for all \(1\le m<k\), for sufficiently large N. Indeed \(S\ge3N,\ H=O(kN)\), \(\log C=O(\log k)\); the last guard follows from \(\log N\gg k\log k\), even if \(k-m=1\).

**Rigidity theorem.** Under (1), the elements \(u_i=\theta-r_i\) are units, and their full embedding-log columns are real-linearly independent unless
\[
 Q(X)=\prod_{i=1}^k(X-r_i)^{a_i},
 \qquad a_i\in\mathbb Z_{\ge0},\quad\sum_i a_i=m. \tag{2}
\]
In the latter case the kernel is exactly the line spanned by \((1+a_i)_i\), and the corresponding relation is already explicit:
\[
 \prod_{i=1}^k u_i^{1+a_i}=1 .
\]
Thus the free correction polynomial cannot supply an unexpected rank compression in this regime. This includes arbitrary repeated roots of Q, and allows Q roots to be nonreal before the argument.

### Proof: cluster the embeddings

Let \(z_1,\dots,z_d\) be the complex roots of f, with all embeddings counted. For each i choose a circle about \(r_i\) of radius \(\rho_i\in(1,2)\) such that its radius is at distance at least \(1/[4(m+1)]\) from the radial distances \(|w-r_i|\) of all m complex roots w of Q. This is possible: the forbidden intervals have total length at most \(m/(2(m+1))<1\). On that circle,
\[
 |P(z)Q(z)|\ge(S-2)^{k-1}[4(m+1)]^{-m}>1 .
\]
Rouché's theorem implies that f and P Q have the same number \(d_i\ge1\) of roots inside the i-th circle, counted with multiplicity. The circles bound disjoint disks. Each disk contains precisely one mark and \(d_i-1\) roots of Q. There can also be roots of f and Q outside all disks.

For each cluster i form the row
\[
 M_{ij}=\sum_{z_h\ {\rm in\ cluster}\ i}\log |z_h-r_j| .
\]
For \(i\ne j\), \(M_{ij}>0\), since every distance is at least \(S-2>1\). For each j, the sum of all logs over all d roots is \(\log|f(r_j)|=0\). If there is any root outside the disks, its distance to every mark is greater than 1. Thus each column of the k by k cluster matrix has strictly negative diagonal whose absolute value exceeds the sum of its off-diagonal entries. The transpose is strictly diagonally dominant and invertible, so there is no log dependence.

It remains to consider a log dependence. Then all f roots belong to the clusters, \(\sum_i d_i=d\), and the matrix M has zero column sums and strictly positive off-diagonal entries. Its transpose has zero row sums and kernel exactly the constants by the maximum-coordinate argument in §1. So M has rank k-1. Every nonzero vector c in its kernel has coordinates all of the same strict sign: if the positive index set is nonempty and proper, sum \((Mc)_i=0\) over it. The contributions from positive columns are strictly negative (use the zero column sums and a positive off-diagonal outside that index set), and contributions from nonpositive columns are nonpositive. This is impossible. Apply also to -c. Hence choose c strictly positive. In particular any dependence of the individual embedding-log columns has a vector c of this kind.

Set \(C_0=\sum_j c_j\), \(R_0=\log(2H+2)/\log(S-2)\). The cluster equation in row i gives the lower bound
\[
 c_i(d-d_i)\log(2H+2)\ \ge\
 c_i(-M_{ii})=\sum_{j\ne i}c_j M_{ij}
 \ \ge\ d_i\log(S-2)(C_0-c_i).
\]
Consequently \(c_i/C_0\ge d_i/(R_0d)\).

### Proof: a genuine dependence forces all roots in a cluster to have comparable radii

For any two roots z,z' in the i-th cluster the individual log equations give
\[
 c_i\log\frac{|z-r_i|}{|z'-r_i|}
 =-\sum_{j\ne i}c_j\log\frac{|z-r_j|}{|z'-r_j|}.
\]
The absolute log difference for \(j\ne i\) is at most \(4/(S-2)\), since \(|z-z'|\le4\) and both distances to \(r_j\) are at least \(S-2\). By the bound for c_i and (1), the absolute left log ratio after division by c_i is at most
\[
 4R_0 d/(d_i(S-2))\le1/2<\log2.
\]
The radii of all f roots in this cluster therefore vary by a factor at most 2. The norm-one identity at the mark says \(\prod_{h=1}^d|z_h-r_i|=1\). Its off-cluster factors are all at least \(S-2\). It follows that every root in the i-th cluster satisfies
\[
 |z-r_i|\le2(S-2)^{-(d-d_i)/d_i}. \tag{3}
\]
No assumption about separation of two different f roots within a cluster is made.

### Proof: turn small radii into exact integer linear factors of Q

Since \(1\le d_i\le m+1\le k\), we have \((d-d_i)/d_i\ge(k-1)/k\ge1/2\). Define \(R_i=8(S-4)^{-(d-d_i)/d_i}\le1\). All f roots of cluster i lie in radius \(R_i/4\) by (3). On the circle of radius \(R_i\) around \(r_i\), each such factor of f has absolute value at least \(R_i/2\), and every off-cluster factor is at least \(S-3\). Monicity gives
\[
 |f(z)|\ge(R_i/2)^{d_i}(S-4)^{d-d_i}>1.
\]
Rouché, this time for f and f+1=P Q, proves that all \(m_i=d_i-1\) roots of Q assigned to cluster i are inside radius \(R_i\); there are no other Q roots.

Now iteratively divide Q by the integer linear mark factors found so far. Let \(Q'\) be any resulting monic integer quotient of positive degree \(m'\le m\), and let \(b_i\le m_i\) be its remaining root counts in the smaller disks. The number of occupied clusters is at most \(m'\), and \(\sum_{b_i>0}d_i\le m+m'\). Hence there exists an occupied cluster i with
\[
 b_i/d_i\ge m'/(m+m').
\]
At its integer mark, use the bounds for the Q roots in that disk, and the bound \(2H+2\) for distances to any other disk:
\[
 \begin{split}
 |Q'(r_i)|&\le R_i^{b_i}(2H+2)^{m'-b_i}\\
 &\le C^{m'}(S-4)^{\,m'-d b_i/d_i}\\
 &\le C^{m'}(S-4)^{-m'(k-m')/(m+m')}\\
 &\le \big[C(S-4)^{-(k-m)/(2m)}\big]^{m'}<1 .
 \end{split}
\]
The last strict inequality is exactly (1). Thus the integer \(Q'(r_i)\) is zero. Monic division by \(X-r_i\) produces another monic integer polynomial. Repeat until constant. This proves (2), including all multiplicities. Conversely (2) gives the displayed product identity, so the nontrivial kernel is exactly its line by the cluster matrix rank k-1. The unit assertion follows from \(|f(r_i)|=1\). This completes the proof.

## 3. Consequence for sealed-row initialization

Suppose now that \(d=k+m\) is odd, \(\psi(\theta)=t\bmod N\) is the common evaluation root, and the k public images \(s_i=t-r_i\bmod N\) are independent sealed uniform unit squares (e.g. from independent private roots). If an algorithm produces a rank-saving field with the hypotheses of §2, equation (2) implies the already-known-type modular relation
\[
 \prod_i s_i^{1+a_i}=1\bmod N,\qquad\sum_i(1+a_i)=d<2k.
\]
Because f is irreducible, \(\gcd_i(1+a_i)=1\) (a common divisor greater than one would make \(P Q-1\) a difference of powers), so at least one exponent is odd. This would indeed be fruitful given the private roots. The difficulty is precisely generating such a relation, not recovering the unit logs.

For an odd balanced semiprime \(N=p_1p_2\) with distinct primes, the unit-square group has order \((p_1-1)(p_2-1)/4\asymp N\). For any fixed exponent vector with all positive entries at most d, conditioning on all but one square and using the CRT cyclic square groups, the probability of its modular product relation is at most \(O(d^2/N)\): a power map of exponent e has kernel size at most \(e^2\). There are at most \(\binom{d-1}{k-1}\le2^{d}\) possible positive exponent vectors of sum d. Therefore even if the marks, common evaluation root and Q are selected adaptively from the public squares, the probability that a rank-saving construction of this kind exists is at most \(O(2^d d^2/N)\). Union over polynomially many permitted degrees d=o(log N) or over \(\exp((\log N)^\alpha)\) fresh batches, \(\alpha<1\), remains negligible when d=o(log N) uniformly.

This probabilistic corollary is only for independent uniform sealed squares on balanced semiprimes. It is not a law for adaptively selected rational child primes or an algorithm-independent factoring lower bound. The deterministic rigidity theorem remains valid for any list of targets at the stated separation guards.

## 4. Where the quarter-scale research should move

The arbitrary-image construction solves norm-one **existence**, not rank compression. The rigidity theorem is stronger than merely counting the degree or assuming real-root stability: even complex roots and arbitrary correction coefficient heights do not help in the specified \(m<k\) separated-linear-mark architecture. Combined with the projective diameter theorem, it eliminates the two most direct ways of obtaining many shared low-height terminal relations by reparametrizing binary forms or adding a low-degree interpolation correction.

A promising surviving approach must use, for example, genuinely nonlinear norm-controlled marks in a common field (several independent polynomial divisibility prescriptions rather than the factors of one product minus one), actual norm reduction in ideal lattices rather than projective charts, or a two-sided incidence scheme where independent rational and algebraic requests are compressed by new arithmetic rather than transferred one-for-one into the unit rank. The [exact unit certificate](exact_descent_unit_certificate.md) can test any such proposed rank saving. We have not proved such a supply theorem, and the first L-parameter remains 1/3.
