# Shared-subfield packet reduction and relative-norm compression

27 November 2026. **Status:** constructive joint ideal/modular-image transitions with strict *measurable* rank savings for shared full-extension packets, and a relative-norm projection for partial packets. They require explicit compatible field presentations and actual correlated incidences. Neither their uniform supply nor a quarter-scale factoring theorem is established. This note complements [correlated ideal-image transport](joint_ideal_image_transport.md) and [terminal ideal reduction](terminal_ideal_reduction_and_support.md).

## 1. Compatible shared base

Let F be an odd-degree number field, including F=Q. Let \(K_j/F\), \(1\le j\le J\), have odd relative degrees \(d_j\). Write \(\iota_j\) for the inclusion of F. Suppose explicit orders \(A\subset F,\ A_j\subset K_j\) and compatible modular evaluation maps are supplied:
\[
 \psi_j\circ\iota_j=\psi_0\quad\text{on the shared evaluable localization of } A .
\]
The necessary localized inclusions are part of the input. All elements used must have checked unit images. We can work with \(A_j=A[T]/(g_j)\) for monic irreducible \(g_j\) over F with a verified modular root and explicit relative power basis. In that case the relative norm of an integral atom is the determinant of its relative multiplication matrix and belongs to A. Norms of compact fractions are formed multiplicatively, without expanding large exponent products.

Whenever a relative norm will be *evaluated*, require its image under \(\psi_0\) to be a unit and its representation to lie in the evaluable localization. This does not follow merely from the element having a unit image at one selected root; its other local components could be nonunits. The stronger guard of a unit absolute norm modulo N suffices for integral atoms. In an implementation test the actual required elements and norms; return a proper gcd if one occurs, otherwise reject a failed guard. This note does not prove that the guard is frequent in a new sampling law.

We use the standard prime-ideal extension and norm identities in the full rings of integers. Invertible ideals in explicit orders can also be used for reductions; their verified products are extended to the full rings for the rank analysis. At a prime \(\mathfrak p\) of F, write \(e_{j,\mathfrak P}, f_{j,\mathfrak P}\) for the ramification index and residue degree of the primes \(\mathfrak P\) of \(K_j\) above it. Then
\[
 \sum_{\mathfrak P\mid\mathfrak p}e_{j,\mathfrak P}f_{j,\mathfrak P}=d_j,\qquad
 \operatorname{Norm}_{K_j/F}(\mathfrak P)=\mathfrak p^{f_{j,\mathfrak P}}.
\]
Relative ideal norms take principal ideals to the ideals of the relative element norms. These facts apply without assuming the extensions are Galois or all primes unramified. For a standard reference see A. V. Sutherland, MIT 18.785 (2021), *Ideal Norms and the Dedekind–Kummer Theorem*, [Lecture 6](https://ocw.mit.edu/courses/18-785-number-theory-i-fall-2021/mit18_785f21_lec6.pdf). No computation of an unspecified Galois closure is required.

## 2. Simultaneous reduction of a full extension packet

Let \(\mathfrak a\subset A\) be a supplied nonzero integral invertible ideal. It need not be principal. Its full extension packet in \(A_j\) is \(\mathfrak a A_j\). Choose any verified reductions
\[
 (\alpha_0)=\mathfrak a\mathfrak b_0,\qquad
 (\alpha_j)=(\mathfrak a A_j)\mathfrak b_j
\]
with integral invertible residual ideals and unit-evaluable nonzero elements. The base reduction can use exact trace-Gram LLL when F is totally real. The separate extension reductions may use any justified lattice or norm-controlled search. They need not be conjugates, equal, independent, or chosen from a random law.

Put \(t_0=\psi_0(\alpha_0),\ t_j=\psi_j(\alpha_j)\). Define
\[
 \delta_j=\alpha_j/\iota_j(\alpha_0).
\]
The following identities are exact:
\[
 \boxed{
 (\delta_j)=\mathfrak b_j/(\mathfrak b_0 A_j),
 \qquad t_j=t_0\,\psi_j(\delta_j).
 }\tag{1}
\]
The large parent ideal cancels before any factorization of a residual norm. In particular for signed packet multiplicities \(n_j\) we have
\[
 \prod_j t_j^{n_j}=t_0^{\sum_j n_j}\prod_j\psi_j(\delta_j)^{n_j}.
 \tag{2}
\]
Only one shared base image label remains, instead of J separate labels for the packet. For balanced multiplicities \(\sum_j n_j=0\) it disappears completely. This is a joint modular-image transition for the supplied correlated requests, not a claim that independently chosen lattice-reduction outputs have the same residues.

The total absolute ideal norm of numerator times denominator in the reduced fractional ideal of \(\delta_j\) is at most
\[
 \operatorname{Norm}_{K_j/\mathbb Q}\mathfrak b_j\,
       (\operatorname{Norm}_{F/\mathbb Q}\mathfrak b_0)^{d_j}.
\]
It may be smaller by cancellation. If these norms are at most \(\exp(O(\Lambda_{1/4}))\), with \(\Lambda_{1/4}=L^{1/4}(\log L)^{3/4}\), \(L=\log N\), their entire prime supports can be included in a quarter-scale factor base with polynomial degree overhead. If the base norm bound is larger, it must be charged; it cannot be ignored because the original ideal was common.

There is also a base-only reduction choice \(\alpha_j=\iota_j(\alpha_0)\), for which \(\delta_j=1\) and no field-specific modular label is introduced. Its actual residual norm is \((\operatorname{Norm}\mathfrak b_0)^{d_j}\), so using it in a high-degree field can increase height substantially. The relative norm decomposition below is useful precisely because it accounts for this shared base residual only once instead of paying a separate ideal support for every copy.

## 3. Odd relative-norm split of the local move

When a relative norm \(\nu_j=\operatorname{Norm}_{K_j/F}(\alpha_j)\) has verified unit evaluation, define
\[
 \eta_j=\alpha_j^{d_j}/\iota_j(\nu_j),\qquad
 \zeta_j=\nu_j/\alpha_0^{d_j}.
\]
Then \(\operatorname{Norm}_{K_j/F}(\eta_j)=1\) and
\[
 \begin{split}
 (\nu_j)&=\mathfrak a^{d_j}\operatorname{Norm}_{K_j/F}\mathfrak b_j,\\
 (\eta_j)&=\mathfrak b_j^{d_j}/
                    \bigl(\operatorname{Norm}_{K_j/F}\mathfrak b_j\bigr)A_j,\\
 (\zeta_j)&=\operatorname{Norm}_{K_j/F}\mathfrak b_j/\mathfrak b_0^{d_j},\\
 t_j^{d_j}&=t_0^{d_j}\,\psi_0(\zeta_j)\,\psi_j(\eta_j).
 \end{split} \tag{3}
\]
These ideal identities are read in the full rings of integers if a relative norm of an order ideal is not explicitly represented. They follow from the extension/norm formula and hold for nonprincipal \(\mathfrak a\). The parent ideal is absent from both new residuals. The only modular discrepancy is represented by explicit small-ideal field elements, not by an unrelated rational integer obtained by reducing \(t_j/t_0\) to a least residue.

The crucial separation is between one base request, which can be processed in F, and norm-one relative directions in the extension. The exponent \(d_j\) is odd, so it is compatible with sealed-root parity. A norm map is not assumed to commute with evaluation; the last identity in (3) follows from the actual field equality \(\alpha_j^{d_j}=\iota_j(\alpha_0^{d_j}\zeta_j)\eta_j\). It would be false in general to replace a relative norm by a power of its evaluation without the \(\eta_j\) factor.

For a degree-one parent prime in the base, (3) yields the usual small residual norm of base reduction when it exists. In a high-degree extension it yields a norm-one residual whose ideal support is only over primes below \(\mathfrak b_j\), regardless of the original request norm. The unit-log rank of norm-one units is at most
\[
 u(K_j)-u(F),\qquad u(K)=r_1(K)+r_2(K)-1 .
\]
Indeed the norm map on unit lattices has image of full real rank \(u(F)\), since a base unit has norm equal to its \(d_j\)-th power. This removes the redundant base-unit directions. It does not bound the number of distinct residual prime supports of different reductions.

## 4. Global relative-norm projection, even for partial packets

Consider a public row of the form
\[
 s_i=\psi_0(\gamma_{0i})\prod_{j=1}^J\psi_j(\gamma_{ji})
\]
with base rational factors incorporated into \(\gamma_{0i}\). Compute the relative norms \(n_{ji}=\operatorname{Norm}_{K_j/F}(\gamma_{ji})\), requiring all needed evaluations to be well defined and units as in §1. Set \(D=\operatorname{lcm}_j d_j\), which is odd, and define
\[
 b_i=\gamma_{0i}^{D}\prod_j n_{ji}^{D/d_j},\qquad
 u_{ji}=\gamma_{ji}^{d_j}/\iota_j(n_{ji}).
\]
Then
\[
 \boxed{s_i^D=\psi_0(b_i)\prod_j\psi_j(u_{ji})^{D/d_j},
 \qquad \operatorname{Norm}_{K_j/F}(u_{ji})=1.}\tag{4}
\]
All exponents and norms can be kept as compact products of the input atoms and their relative norms. Computing each atom norm by its relative multiplication matrix has polynomial bit cost in the explicit degree and field data. No expansion of a product with exponentially large numerical exponent is needed. The least common multiple of polynomially many explicitly supplied degrees has bit length at most their sum of logarithms.

Here is the precise finite-rank calculation. Fix a base prime \(\mathfrak p\). Write \(x_0\) for its valuation in \(\gamma_0\), \(v_j\) for the vector of valuations in \(K_j\) at all primes over \(\mathfrak p\), and \(e_j,f_j\) for the vectors of ramification indices and residue degrees. Thus \(f_j^Te_j=d_j\). Over Q and ignoring nonzero scale factors D, \(d_j\), the effect of (4) is the linear map
\[
 {\cal P}_{\mathfrak p}:(x_0,(v_j))\longmapsto
 \left(
 x_0+\sum_j f_j^Tv_j/d_j,\
 \left(v_j-e_j f_j^Tv_j/d_j\right)_j
 \right).\tag{5}
\]
The relative component is in \(\ker f_j^T\). The map has kernel exactly
\[
 v_j=e_j a_j,\qquad x_0=-\sum_j a_j,\qquad a_j\in\mathbb Q.
 \tag{6}
\]
Its rank is \(1+\sum_j(m_j-1)\) on the full valuation space, where \(m_j\) is the number of primes of \(K_j\) above \(\mathfrak p\). It saves J dimensions there, or J-1 on the subspace \(x_0=0\) with all \(v_j\) free. When a prime has only one prime above it, its relative component is identically zero, including ramification.

For an actual row span W across all relevant prime fibres, the exact finite rank saved is
\[
 \boxed{\dim W-\dim{\cal P}(W)=\dim(W\cap\ker{\cal P}),}\tag{7}
\]
where \({\cal P}\) is the direct sum of (5). In particular one may not count a saving at a fibre that contains only one of several possible extension primes and for which the full-packet direction is absent from W. The projected representation may introduce the other primes over the same base prime; their valuations are linear in the original coordinates and do not increase the rank in (7).

The kernel description is at the level of ideal valuations. It does not assert that every rational diagonal ideal combination is generated by a base element. Formula (4) is valid on the actual field elements regardless of principality, and the remaining relative norm-one units still have to be canceled in the final certificate. That is why this is stronger than a formal cancellation of rational prime labels while not charging the unit rank.

## 5. Exact rank saving for correlated full packets; residuals need not be factored

A particularly useful input regime is a block of rows in which all nonterminal field valuations over certain base primes are full-extension packets:
\[
 v_{j,i}(\mathfrak p)=e_j n_{j,i}(\mathfrak p).
\]
Let \(x_{0,i}(\mathfrak p)\) record any actual base contribution. The nonterminal relative valuations in (5) vanish identically, and the base incidence is just
\[
 a_i(\mathfrak p)=x_{0,i}(\mathfrak p)+\sum_j n_{j,i}(\mathfrak p).
 \tag{8}
\]
Let E be the complete original nonterminal incidence matrix and \(E_0\) the matrix of the sums (8). Then the exact savings on this block are
\[
 \operatorname{rank}_{\mathbb Q} E-
                     \operatorname{rank}_{\mathbb Q} E_0 .
 \tag{9}
\]
In the absence of base components, J independently used copies of k full packets have ambient dimension Jk, but their projected dimension is k. This bound is attained if the actual incidence span contains the full packet space. For partial correlations use the actual ranks rather than the ambient count.

Now apply one base ideal reduction per base label in (8) to the elements \(b_i\) of (4), reusing it for every field and every row. The temporary residual ideals in that reduction are slaved to the same exponent matrix \(D E_0\). For any combination of rows canceling the projected base incidence, both the base image labels and **all** temporary base residual ideals cancel exactly by [the coupled transport identity](joint_ideal_image_transport.md), (5). They need not even be individually factored. Thus the savings (9) are not paid back by introducing one independent residual copy per field. The relative norm-one components already have only their designated terminal valuations. This is a genuine simultaneous transition on the supplied block even when the base ideals were nonprincipal.

For an ordinary unsealed anchor whose base incidence does not vanish, one can further apply the Smith-aware block elimination theorem of the companion note. Full base packet correlations automatically make the field-specific anchor directions vanish from (5). Actual new anchors can also be produced as follows. For a base ideal \(\mathfrak a\), its single base reduction \(\alpha_0\) gives the identity
\(\psi_i(\iota_i(\alpha_0))/\psi_j(\iota_j(\alpha_0))=1\).
The full-extension packets occur with opposite signs in the two fields; the remaining ideals are two copies of \(\mathfrak b_0\). If the latter are terminal, this is a literal anchor with that active vector. If not, they are a *coupled* new packet, not two arbitrary modular ports; (4) cancels both copies. More generally one can construct these anchors between the base and any extension. This works for nonprincipal base ideals as well as rational primes. The arithmetic cost of the base reduction is that of F, rather than a new independent search in each extension. Such anchors only count as new rank gain if they intersect the actual target span (7); they do not prove useful new correlations from nothing.

## 6. Certificate bound and implementation scope

The projected finite rank is computable without factoring unknown norm residuals: apply the exact ideal-refinement theorem to the explicit field atoms and their relative norm images, then compute the integer kernel on the compact exponents. A simpler implementation for supplied complete prime-ideal lists uses (5) directly. After exact finite cancellation, the base field products are units, and the relative components are norm-one units. The remaining logarithmic rank is at most
\[
 T_{\log}=u(F)+\sum_j(u(K_j)-u(F)).
 \tag{10}
\]
All fields have odd degree, so torsion in any of them is a sign. Apply the saturated kernel and sign-selection argument of [the exact unit certificate](exact_descent_unit_certificate.md). In particular with k sealed rows, projected nonterminal rank r, and a bound T on the remaining terminal finite rank, the inequality
\[
 k>r+T+T_{\log}+1
\]
is sufficient for the odd-coefficient certificate when there are no additional unsealed anchors. With additional anchors use (8)–(10) of [correlated transport](joint_ideal_image_transport.md) to account for their integral projection defect. Verify the resulting public congruence before exposing private roots. The original common exponent D in (4) is odd and does not change the sign-fibre success probability. In comparison with treating the base and extensions as unrelated fields, (10) saves \(J u(F)\) archimedean dimensions; the actual finite rank saving is given by (7).

This supplies a specific mathematical answer to the earlier modular-image gap: compatible shared-base packets can be processed jointly, with one base incidence vector and explicitly bounded relative directions. No assumption of equal image distributions or independent residuals is involved. It does not assert that all local searches yield such packets, or that a norm bound on a high-degree order automatically fits the quarter-scale budget.

The still-missing part of a complete quarter-scale algorithm is a relation-generation law supplying enough **genuine** full-packet or other anchor correlations in a bounded shared family. A row obtained merely by copying a known base element into many extensions has no new quotient information; (4) returns the original base contribution. Similarly, extending every row to its own field without controlling the new relative rank cannot close the ledger. The existing ordinary KeyBreak root labels usually pick a single prime ideal, not a full extension packet. We therefore cannot substitute (9) for its active rank without a new incidence theorem. Promising next steps are constructing common-base extension families with controllable relative norms of nonlinear marks, and generating new anchors whose joint old-target intersection is positive in (11) of the companion note. No new asymptotic bound or certified record is asserted.
