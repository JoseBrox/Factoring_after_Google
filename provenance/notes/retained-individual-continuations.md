# Individual continuations of retained construction methods

2026-11-25. These are concrete investigations of five retained catalogue entries. They do not promote all retained ideas, claim that a general readout constructs its input, or count thematic resemblance as reuse of a proved theorem. The principal new construction is the quadratic exponent chain; the other entries are tested against their exact promised interfaces.

## 1. N1101: a short relation in a supplied root algebra

### A proved construction with a supplied-exponent promise

Let \(N\) be odd and let distinct primes \(p,q\mid N\) satisfy

\[
\left(\frac bp\right)=1,
\qquad \left(\frac bq\right)=-1,
\qquad \gcd(b,N)=1.
\]

Other prime factors and arbitrary multiplicities are allowed. Let an even \(M=2^tu\), with \(u\) odd, satisfy \(p-1\mid M\). Work in

\[
A=(\mathbb Z/N\mathbb Z)[X]/(X^2-b).
\]

For uniformly random \(a\bmod N\), first compute \(\gcd(a^2-b,N)\). Otherwise form

\[
z_0=(X-a)^u,
\qquad z_{j+1}=z_j^2,
\qquad z_j=c_j+d_jX.
\]

At every level test \(\gcd(N,d_j)\) and \(\gcd(N,c_j-1,d_j)\). This takes \(O(\log M)\) quadratic-algebra operations and has success probability at least

\[
\frac{p+3}{2p}>\frac12.
\]

The proof is in `splitting-provenance-audit.md`. The decisive point is that for every \(a\) with \(\left(\frac{a^2-b}{p}\right)=-1\), the split coordinates at level \(v_2(p-1)-1\) have opposite signs, and at the next level both equal one. In the nonsplit field modulo \(q\), either the later element is not one, or its preceding square root is a scalar \(\pm1\). One of the two displayed coefficient gcds therefore contains one of \(p,q\) and excludes the other.

This is a genuine instance of the retained local-relation constructor: the reduced relation has only two coefficients and a short power circuit, and the local discrepancy is proved. It also handles the case where \(M\) annihilates both quadratic unit groups; the one-shot relation may vanish everywhere, but the chain still succeeds.

For a distinct-prime semiprime \(N=pq\), a supplied unit with Jacobi symbol \(-1\) gives the mixed splitting promise after relabeling. For general odd \(N\), that Jacobi condition alone is insufficient; the mixed-prime promise is the correct statement.

**Remaining constructor task:** produce an appropriate exponent and useful local type, or produce a deterministic short list containing a successful \(a\), within the desired general-factoring budget. The theorem does not reduce those costs by itself. Classical randomized factoring from a supplied order multiple already has polynomial overhead, so this formulation is not advertised as a new randomized complexity class.

## 2. N1505: construct the actual selected bundle section

### Exact prior interface checked

The catalogue asks for a nonzero selected value of a section of the particular bundle \(\mathcal V_N(-m)\), not an arbitrary useful scalar. I retrieved the actual manuscript proof, rather than only its catalogue description. For \(N=pq\) with \(p<q\), it sets

\[
t=\lfloor\sqrt N\rfloor,
\qquad m=\lfloor t/2\rfloor+1,
\qquad G(X)=(1+X)^N-1,
\]

and uses transition

\[
T_N(X)=
\begin{pmatrix}X^{-m}&X^{-m}G(X)\\0&X^m\end{pmatrix}.
\]

The third summand produces the rank-three bundle. The selected second-coordinate ideal is exactly \(pR\), where \(R=\mathbb Z/N\mathbb Z\). Its calculation uses the annihilator of the coefficient ideal of the prefix \(\sum_{j=1}^{2m-1}\binom NjX^j\). This is a torsion section created by reduction modulo \(N\), not a characteristic-zero section.

### Supplied-order transfer all the way to a section

Under the N1101 supplied inputs, run the quadratic chain until it gives a factor \(h\). In the semiprime case set

\[
p_0=\min(h,N/h),\qquad q_0=N/p_0,
\qquad c=p_0\pmod N.
\]

Then \(c\) is a nonzero element of the **actual required** ideal \(p_0R\). The earlier proved section-reconstruction proposition supplies the complete division-free circuit

\[
s_\infty=\binom0c,
\qquad
s_0=\binom{cX^{q_0-2m}S_{p_0}(1+X^{q_0})}{c},
\qquad
S_k(U)=1+U+\cdots+U^{k-1}.
\]

The exponent \(q_0-2m\) is nonnegative because \(2m-1<q_0\). Modulo \(p_0\) both sides of the gluing equation vanish; modulo \(q_0\), Frobenius gives

\[
c((1+X)^N-1)=cX^{q_0}S_{p_0}(1+X^{q_0}).
\]

Joint binary recursion for \(U^k,S_k(U)\) uses \(O(\log k)\) gates. Thus the new chain plus the **specific previously proved reconstruction theorem** gives the actual selected section in expected polynomial time in \(\log N+\log M\), under its additional supplied-input promise.

This is an explicit use of an earlier result. It does not give a section constructor from the succinct transition alone: the cost of constructing \(M,b\), or the deterministic successful-parameter search, remains. The reduction is not evidence that the bundle route has been exhausted, and it is not an independent general-factorization speedup.

**Checked prior source:** manuscript source part 03, Git blob `1578d434022855fc62019deef8ef5522eca24db5`, Theorem `repo-rank-three`, Corollary `repo-one-section`, and Proposition `rw-section-circuit`. [Existing manuscript part](https://github.com/JoseBrox/factoring-algorithms/blob/main/manuscripts/current/source_parts/part-03.tex.txt).

## 3. N1124: an explicit local rank witness, and a precise readout limitation

### A two-dimensional witness from the chain

Multiplication by \(z_j=c_j+d_jX\) in the basis \(1,X\) is

\[
U_j=\begin{pmatrix}c_j&bd_j\\d_j&c_j\end{pmatrix}.
\]

Only its first two characteristic coefficients are needed. Put

\[
\tau_j=\operatorname{tr}(U_j)=2c_j,
\quad\delta_j=\det(U_j)=c_j^2-bd_j^2,
\]

\[
D_j=1-\tau_j+\delta_j=\det(U_j-I),
\qquad
E_j=\tau_j^2-4\delta_j=4bd_j^2.
\]

Testing \(\gcd(N,D_j)\) and \(\gcd(N,E_j)\) gives the same success guarantee as the coefficient chain. Indeed at the decisive later level, \(U_j-I\) is zero modulo the split prime \(p\). If \(z_j\ne1\) in the nonsplit field modulo \(q\), multiplication by \(z_j-1\) is invertible there, so \(D_j\) contains \(p\) and excludes \(q\). Otherwise at the preceding level, \(d_{j-1}\ne0\pmod p\) and \(d_{j-1}=0\pmod q\), so \(E_{j-1}\) contains \(q\) and excludes \(p\).

This explicitly constructs the local rank discrepancy that a joint-orbit proposal seeks, on the supplied-exponent input. It has constant dimension, and the corresponding invariants are already computed by the power circuit in \(O(\log M)\) operations. The high-dimensional band-matrix evaluator from N1124 is not needed to compute them; it must not be cited as the source of this speedup.

### Why trace access alone does not solve the randomized sparse-kernel stage

The retained N1124 theorem evaluates selected traces and an initial characteristic segment for particular polynomial or fixed-frequency band matrices. It does not provide the kernel of an arbitrary sparse relation matrix. There is even an exact obstruction to trying to reconstruct generic characteristic-two kernel dimensions solely from all those invariants:

\[
A=\begin{pmatrix}1&1\\1&1\end{pmatrix}
\quad\text{over }\mathbb F_2.
\]

This symmetric matrix has rank one and \(A^2=0\), whereas the zero matrix has rank zero. Both have characteristic polynomial \(T^2\), and \(\operatorname{tr}(A^k)=0\) for every positive \(k\). Thus even a complete characteristic polynomial and all power traces do not determine the generic kernel dimension in this characteristic. This does not exclude the special structured classes or a richer kernel oracle; it identifies exactly why their trace interface cannot simply be substituted for the kernel solver.

**Remaining task:** construct a factor-sensitive operator in the proven structured access class, or furnish a richer efficient kernel/Smith readout for the actual operator. Its existence as a large sparse matrix is insufficient.

## 4. N1002: which selected coefficient has actually become inexpensive?

### A fixed quotient coefficient is now supplied

The chain computes the exact reduced coefficients

\[
(X-a)^E\bmod(X^2-b)=c_E+d_EX,
\]

with

\[
d_E=\sum_{\substack{0\leq k\leq E\\k\text{ odd}}}
\binom Ek(-a)^{E-k}b^{(k-1)/2}.
\]

This selected sum is inexpensive because it is a coefficient in a **fixed-degree quotient**. The recurrences

\[
c_{2E}=c_E^2+bd_E^2,
\qquad d_{2E}=2c_Ed_E,
\]

and ordinary binary powering give \(O(\log E)\) ring operations. Exact gcds of \(d_E\) or the joint coefficients \((c_E-1,d_E)\) are therefore available. N1101's local theorem supplies the missing usefulness proof for the consecutive exponents; the coefficient readout alone would not.

This is a concrete efficient selected-coefficient constructor under the exponent/local-type promise. It is not the arbitrary arithmetic-product unit bit or the binomial-prefix coefficient ideal requested by the general N1002 entry.

### A precise obstruction to silently transferring it to the prefix

Reduction modulo \(X^2-b\) does not determine truncation at a large degree. For every \(h\geq0\),

\[
F(X)=X^h(X^2-b)
\]

has zero image in the quadratic quotient, while its truncation through degree \(h\) is \(-bX^h\), with unit coefficient when \(b\) is a unit. Thus no function of that quotient value alone can recover the desired prefix coefficient ideal for all polynomial inputs. The chain succeeds because a separately proved local exponent property makes its particular quotient relation useful. It does not construct the N1505 obstruction prefix or a general factorial endpoint from an arbitrary short input circuit.

There is also a limited cost observation about encoding an exponent: in a plain multiplication circuit starting from a formal indeterminate \(x\) and constants, after \(s\) multiplications the degree is at most \(2^s\). Computing the formal monomial \(x^M\) therefore needs at least \(\lceil\log_2M\rceil\) multiplications. A compact product/LCM specification of \(M\) alone does not remove that cost in this model. This statement does not rule out modular order information, a different circuit model, or a new selected-product algorithm.

## 5. N1131: a concrete exponent-pair lattice and what its short vector means

Assume the initial norm check found a unit, and write

\[
y=X-a,
\qquad \overline y=-X-a,
\qquad y\overline y=a^2-b\in R^*.
\]

The two multiplication actions commute. Modulo a prime \(\ell\mid N\), consider the projective relation lattice

\[
\Lambda_\ell=
\{(r,s)\in\mathbb Z^2:
y^r\overline y^{s}\in\mathbb F_\ell^*\}.
\]

Since \(\overline y=(a^2-b)y^{-1}\), if \(h_\ell\) is the order of the class of \(y\) in \(A_\ell^*/\mathbb F_\ell^*\), then

\[
\Lambda_\ell=\{(r,s):r-s\equiv0\pmod{h_\ell}\}.
\]

For a split prime, \(h_\ell\mid\ell-1\); for a nonsplit prime, \(h_\ell\mid\ell+1\). These statements follow directly from the split product algebra or from \(\mathbb F_{\ell^2}^*/\mathbb F_\ell^*\).

The vector \((1,1)\) is a public short relation in **every** component. If \(h_\ell\geq3\), the shortest nonzero lattice vectors are exactly \(\pm(1,1)\): every vector outside the diagonal has \(|r-s|\geq h_\ell\), and hence Euclidean norm at least \(h_\ell/\sqrt2>\sqrt2\). For several components replace \(h_\ell\) by their least common multiple. Thus ordinary short-vector minimization on this exact two-action lattice can return only the common norm relation, even when the hidden local orders differ. Small dimension and a short vector are not themselves a separating certificate.

The supplied exponent adds the specific candidate \((M,0)\) to the split-prime relation lattice because \(h_p\mid p-1\mid M\). It need not belong to the nonsplit lattice. When its endpoint already separates, a coefficient gcd extracts the factor; when the exponent is saturated in both components, the 2-adic chain supplies the finer adjacent-level sign separation proved above. This identifies exactly what the order promise contributes to this particular retained construction.

**Remaining task:** construct a useful off-diagonal exponent relation without first being given the required annihilator, or exploit structure beyond this universal norm relation. The shortest-vector statement is a proved screen for this two-action family; it is not a lower bound for all exponent-pair lattices or for factoring.

## 6. What is genuinely reused, and what is still new work

| Entry | Concrete result in this continuation | Earlier theorem actually invoked | Remaining limitation |
|---|---|---|---|
| N1101 | Short quadratic quotient relations with uniform success above one half, including saturated exponents and arbitrary additional prime powers | Existing coefficient-content extraction is the same interface; the displayed local success proof is new in this continuation | Supplied exponent and mixed splitting; deterministic successful-parameter construction |
| N1505 | The actual selected value and a complete division-free section circuit on the supplied inputs | The checked earlier `rw-section-circuit` reconstruction theorem and exact selected ideal | Does not construct the section from the succinct transition alone |
| N1124 | Explicit 2-by-2 local rank witness; two characteristic coefficients suffice for this witness | No high-dimensional trace theorem is needed; its exact scope is respected | Generic characteristic-two trace data do not supply a kernel, and the required structured constructor is absent |
| N1002 | Exact cheap coefficient/gcd in a fixed quadratic quotient | Binary powering and existing coefficient/gcd readout | A quotient value cannot recover a general prefix; general selected-product compression remains open |
| N1131 | Exact projective exponent-pair lattice; proof that its shortest vectors can be universal nonseparating relations | Elementary commuting-action/norm identities | Useful off-diagonal relation construction remains charged |

These are individually specified advances or screens. They neither certify all 232 retained catalogue entries nor establish a general factoring algorithm with first L-parameter below one third.
