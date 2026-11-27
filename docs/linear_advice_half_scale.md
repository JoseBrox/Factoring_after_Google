# Linear total advice for deterministic half-scale factoring

**Status (27 November 2026): proved conditional transfer from the existing common-anchor coverage theorem.** The advice is nonuniform. This strengthens the previous polynomial-advice result, not the uniform deterministic factoring exponent. No new Lean milestone is asserted.

We use the [common-anchor theorem](common_anchor_derandomization.md), with its already stated uniform prime-character input, itself derived in writing from the project's fixed Dirichlet/zeta zero-free theorem. The finite-group and advice argument below is elementary and independent of that analytic proof. The motivation is catalogue N48 (deterministic covering), N46 (arithmetic Fourier methods), and O50 (spectral methods).

## 1. An explicit small-bias graph on raw input strings

Let \(n\ge2\) and let \(q=2^k>n\). Work in \(\mathbb F_q\), with a fixed nonzero \(\mathbb F_2\)-linear functional \(\ell:\mathbb F_q\to\mathbb F_2\). For \(a,z\in\mathbb F_q\), define the \(n\)-bit string
\[
v(a,z)=(\ell(z),\ell(za),\ldots,\ell(za^{n-1})).
\]
Use the uniform distribution over all \(q^2\) ordered choices \((a,z)\), including multiplicity. A walk on \(\mathbb F_2^n\) adds one independently sampled string \(v(a,z)\) at each step (addition is XOR).

For any nonzero \(w\in\mathbb F_2^n\), put \(P_w(X)=\sum_{i=0}^{n-1}w_i X^i\). This is a nonzero polynomial of degree at most \(n-1\). Its character eigenvalue for the transition operator \(T\) is
\[
\begin{aligned}
\widehat T(w)
 &=\mathbb E_{a,z}(-1)^{\ell(zP_w(a))}\\
 &=q^{-1}\#\{a:P_w(a)=0\}
 \ \in[0,(n-1)/q].
\end{aligned}
\tag{1}
\]
For a fixed nonroot \(a\), multiplication by \(P_w(a)\ne0\) permutes the field, and the nonzero functional takes each bit equally often. This proves (1). All additive characters of the string group have this form, so in the normalized real \(L^2\) space \(T=J+E\), where \(J\) projects to constants and
\(\|E\|_{2\to2}\le\lambda=(n-1)/q\). This includes loops and multiple edges and needs no simplicity of the graph.

A field of degree \(k\) can be constructed deterministically in \(2^k\operatorname{poly}(k)\) bit operations by enumerating monic binary degree-\(k\) polynomials and testing irreducibility (Frobenius powers and polynomial gcds). Existence of such a polynomial is the standard finite-field theorem. Use the first irreducible in a fixed order and the coefficient-of-1 functional. Given \(a,z\), all \(n\) coordinates of the edge are computed in \(\operatorname{poly}(n,k)\) bit operations by iterated field multiplication. Thus the field is public and need not be advice.

## 2. Walks avoid an arbitrary small bad set

Let \(D\subseteq\mathbb F_2^n\) have density \(\beta\). Write \(M_D\) for multiplication by \(1_D\). The rank-one operator \(M_D J M_D\) has norm \(\beta\), since it maps a function \(f\) to \(1_D\langle1_D,f\rangle\). Hence
\[
\|M_D T M_D\|\le\beta+\lambda.
\]
Starting at a uniform vertex and taking fresh uniform edges, the probability that all \(r\ge1\) visited vertices are in \(D\) is
\[
\langle1_D,(M_D T M_D)^{r-1}1_D\rangle
\le \beta(\beta+\lambda)^{r-1}.
\tag{2}
\]
No property of \(D\) beyond its density is needed. This is a spectral small-set survival bound, not an independence assertion.

## 3. One linear-length advice string works for all subinputs

For a bit length \(m\), the previous common-anchor result takes
\[
b_m=\left\lceil\sqrt{m\lceil\log_2(m+2)\rceil}\right\rceil,\qquad B_m=2^{b_m}.
\]
After its deterministic sieve and primality/perfect-power preprocessing, it tests a raw \(m\)-bit candidate reduced modulo the surviving modulus. The exact deterministic test either produces a proper factor (including a coordinate gcd exit) or fails. Its failure probability on a uniform \(m\)-bit candidate is at most \(B_m^{-2}\) for sufficiently large \(m\), uniformly in the surviving modulus. A successful common anchor gives all the order relations needed to split. This is precisely the input theorem from the linked note, not a new density assumption.

Fix a maximum input length \(n\). Put \(m_0=b_n\); small \(n\) are handled by finite base cases. All subinputs of length below \(m_0\) can be completely factored by trial division in \(2^{O(b_n)}\) bit time. For large enough \(n\), all bit lengths \(m\ge m_0\) satisfy the asymptotic coverage threshold.

For a surviving modulus \(M\) of any bit length \(m_0\le m\le n\), use an \(n\)-bit raw candidate, still reducing modulo \(M\) and running the test with its own \(m\)-parameters. Let \(D_M\) be the bad set of these \(n\)-bit strings. Every canonical residue has at least one preimage among the \(m\)-bit strings, so the fraction of bad residues under the uniform canonical law is at most \(2 B_m^{-2}\). A uniform \(n\)-bit string reduced modulo \(M\) assigns each residue probability at most \(2/M\), since \(2^n\ge M\). Therefore
\[
|D_M|/2^n\le4 B_m^{-2}.
\tag{3}
\]
The same proof allows any exact test whose outcome depends only on the canonical residue; this holds for the common-anchor test. Preprocessed inputs need no successful raw candidate.

Set
\[
s=\left\lfloor\sqrt{m_0\lceil\log_2(m_0+2)\rceil}\right\rfloor,\quad
k=s+\lceil\log_2 n\rceil+2,\quad
r=1+\left\lceil\frac{n+2}{s-1}\right\rceil .
\]
For sufficiently large \(n\), \(s\ge2\), \(s/\log n\to\infty\), \(k=O(s)=O(b_n)\), and (3) is at most \(2^{-s}\), as \(b_m\ge s\). Equation (1) gives \(\lambda\le2^{-s}/4\). By (2), the probability that a random \(r\)-vertex walk misses the successful set for any fixed surviving \(M\le2^n-1\) is at most
\[
2^{-s}(2^{1-s})^{r-1}<2^{-n-2}.
\]
A union bound over fewer than \(2^n\) possible moduli shows that there is a single walk with at least one successful candidate for **every** surviving modulus of bit length between \(m_0\) and \(n\).

Encode the walk by its initial \(n\)-bit string and its \(r-1\) pairs \((a,z)\) of \(k\)-bit field elements. Its total advice length is
\[
n+2k(r-1)=O(n).
\tag{4}
\]
Indeed \(r-1=O(n/s)\) and \(k=O(s)\). This one advice string works for every input of length at most \(n\), including all recursively encountered factors, not just for length exactly \(n\). There is no need to supply a separate advice list for each smaller bit length. The walk contains a polynomial number of candidate anchors.

## 4. Result and complexity audit

**Theorem.** Under the analytic input of the existing common-anchor theorem, complete factoring of all positive integers of bit length at most \(n\) is possible by a deterministic algorithm with \(O(n)\) bits of advice and worst-case bit time \(2^{O(b_n)}=L_N[1/2,O(1)]\) when the original input has bit length \(n\). The one advice string is universal over this entire input-length range.

The algorithm constructs the public field, decodes the walk, and reuses the list at each recursive splitting call. Test candidates in their deterministic order until a verified proper factor is found. The theorem above guarantees success whenever needed. Each candidate test costs \(2^{O(b_m)}\operatorname{poly}(m)\le2^{O(b_n)}\); the field construction, the polynomial list length, trial division for short subinputs, and polynomially many splitting/prime-power recursive nodes fit the same time scale. Prime verification and factor multiplication checks are unchanged from the existing method. The bound is relative to the original maximum input size; if an advice string for a larger \(n\) is used on a much smaller input, no sharper running time in that smaller size is asserted.

The prior common-anchor note gave \(O(n^2/b_n)\) bits for a single input length by independent anchors, and required advice for smaller lengths for recursive factoring. Equation (4) improves this to a single \(O(n)\)-bit advice string for the whole recursion. We do not assert that linear advice is optimal.

**Unresolved:** the proof selects the walk by a union bound. Constructing a suitable walk or a successful anchor uniformly in \(2^{O(b_n)}\) time is still open. Enumerating all \(O(n)\)-bit advice strings costs \(2^{O(n)}\), which would lose the claimed scale. The small-bias graph is explicit, but its initial vertex and edge sequence are not certified to be universally good by a uniform efficient procedure. Neither a generic expander walk nor the known failure density alone closes this gap.

The nonuniform transfer supplies a more compact object for subsequent uniform derandomization research: one short walk described by linear advice, with the same candidate list reusable throughout recursion.
