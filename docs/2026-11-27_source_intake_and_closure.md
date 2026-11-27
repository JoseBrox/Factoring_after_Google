# 27 November 2026: closure of the short-ratio checkpoint and Shanghai source intake

## Status and provenance

This note audits the latest committed research checkpoint, not an unavailable
interrupted chat transcript. The audited head is
[be094b266bdba4d37ff32bb696b13271ef65b26f](https://github.com/JoseBrox/Factoring_after_Google/commit/be094b266bdba4d37ff32bb696b13271ef65b26f).
The preceding private catalogue/archive repository is distinct from this public
manuscript repository. Its latest family routing and stable identifiers are
retained, not rewritten.

### Closure of the preceding continuation

The [depth-free character rigidity note](depth_free_character_rigidity.md)
has a sound finite-group argument, conditional on its stated uniform
prime-character estimates. The following are the key checks.

* Approximate character identification is unique: for distinct characters
  the distance after scalar rotations is at least
  \(\sqrt{2(1-\delta)}\ge1\). The good-power difference construction has
  error at most \(1/4\); the multiplication comparison has error at most
  \(3/4\). These strict inequalities prove the homomorphism, including
  reduction of indices modulo the finite label order.
* For the balanced word distribution, comparison of two \(k\)-prime
  products uses \(B^k<N\). Unique factorization identifies their multisets,
  and hence cancels the label phases even for arbitrary labels. The
  \(B^4\) moment bound is valid with the specified \(b,k\).
* The large-spectrum estimate follows from almost orthogonality. If \(x^2
  \ge4\delta\), its cardinality is at most \(2/x^2\); integration from
  \(x_0=2\sqrt\delta\) to \(\theta\) bounds the \(2L\)-moment of the large
  coefficients by \(6\theta^{2L-2}\) for \(L\ge2\). The small part is
  bounded separately by the \(2k\)-moment. No independence of labels
  is needed.
* In Case B the order of the image of the cyclic label group divides
  both \(D=2^{n+1}\) and the group order, and is a power of two strictly
  less than \(D/2\). Thus \(\chi_{D/2}\) is trivial. The sign function has
  \(|\mathbb E u|\ge31/32\), and the balanced even word count makes the
  principal Fourier coefficient nonnegative. Parseval bounds the negative
  fibres exactly as claimed.
* Primitive annihilators exist by rational elimination, denominator
  clearing and dividing by the gcd. A label disagreement modulo \(D\)
  implies a nonzero integer pairing, and hence a strict rational rank
  gain. The two primitive-lattice queries have area \(H^2\le NB^{2001}\);
  the enumeration and arithmetic costs remain half-scale.
* The rank driver is randomized. The recursion has deterministic
  control, with randomized splitting calls; the phrase "deterministic
  recursion" is not a claim of deterministic factoring. When the label
  modulus is \(2^{e+1}\), it is **the value \(e+1\)** (the maximum bit length of
  a canonical label), not the bit length of the integer \(e\), that must fit
  the stated resource budget.

The analytic dependency is the exact externally comparator-accepted
Dirichlet/zeta strip described in [quasi-RH witnesses](quasi_rh_witnesses.md)
and its written contour transfer. This audit does not independently rebuild
that external artifact, the full analytic transfer, or the previous finite
test harness. The pinned tests and their recorded receipts remain prior
evidence. No new deterministic uniform hitter or Lean milestone follows
from the rank argument.

The remaining half-scale problem is selecting an anchor for the exact
two-fibre disagreement predicate, not proving rank increase after a
disagreement. The independent residual-pooling route still lacks a
uniform bound on the cumulative residual dimension. The polynomial-advice
result is nonuniform, and an exact read-many random-tape predicate is not a
fresh-randomness BPL computation.

## Shanghai manuscript: source and evidence levels

**Update (27 November, after PDF upload).** The primary manuscript is now available, and the historical access limitation below is superseded by the [pinned-source audit](keybreak_source_audit.md). Page 1 names **The KeyBreak Cryptanalysis Agent** as author; Nielsen is credited through reference [33], not as a coauthor. Page 3 gives the unconditional constant **10^13**, not 1013. The earlier preliminary report misread the superscript; the displayed table has been corrected.

**Primary source (now obtained):** The KeyBreak
Cryptanalysis Agent (Shanghai Jiao Tong University et al.), *Provable Integer
Factorization via Multilevel Descent: Approaching Heuristic Bounds* (2026),
[manuscript URL](https://crypto.sjtu.edu.cn/factoring.pdf).
The author attribution and title here are provisional metadata derived
from the public announcement and leaderboard, not a transcription of
the unavailable title page. The leaderboard attributes the agent harness
and prompt to Qi Wang, Zhian Qian, Changhao Yuan, Juanru Li, Xiaogang Zhou,
Shi Bai and Yu Yu, and credits Nielsen's precursor constructions.

On 27 November the direct HTTPS URL, HTTP variant, query-string variant,
and the leaderboard's source link failed in the browsing environment
(timeouts or access error). Direct container retrieval was also unavailable
(DNS failure). No immutable copy or SHA-256 of the Shanghai manuscript
was obtained. In particular **no page, lemma, proof or numerical
optimization from that PDF has been verified**. This is a source-intake
checkpoint, not a theorem-level audit, and no defect is attributed to the
unread manuscript.

Reported claims (not independent validation):

| Reported statement | Time | Evidence |
|---|---:|---|
| Theorem 1.1 | \(L_N[1/3,10^{13}]\) | Unconditional claimed Las Vegas bound |
| Theorem 1.2 | \(L_N[1/3,2.97]\) | Uses Dirichlet GRH; claimed written proof |

Source: [Big O Speedrun randomized factoring board](https://bigospeedrun.com/integer-factoring-randomized),
retrieved 27 November 2026, which labels both as claimed and reports no
checked Lean artifact for this manuscript. See also the
[27 November announcement/republication](https://cn-sec.com/archives/5619552.html)
for the title and description of the growing descent. The board's treatment
of its accepted GRH artifact is not by itself a proof of the factoring
paper. Do not confuse exponent \(1/3\), leading constant \(2.97\), and
practical performance; nor do our conditional constant \(91.4\) and the
Google claimed constant \(105\) establish an improvement on Theorem 1.2.

### Accessible predecessor (distinct from the Shanghai manuscript)

Kasper Nielsen / factoring-connection, *Theorem U-MF: a Las Vegas factoring
algorithm in expected time L_N[2/5]*, 28 October 2026,
[pinned text](https://github.com/kasper0406/factoring-connection/blob/351e8eeee142b2b13790cf67c3e8e2e35aaf1f0d/notes/mfU_theorem.md).
Its overview explicitly distinguishes the rigorous-square-congruence
result of Lee–Venkatesan from fruitfulness and describes its own
Dixon descent, independent algebraic polynomial pools, integer multiplier
randomization, shared norm-parity columns, and recursive shape test.
It is an AI-reviewed draft claiming exponent 2/5, not the Shanghai
proof of exponent 1/3.

Nielsen's [multidescent results](https://github.com/kasper0406/factoring-connection/blob/main/notes/multidescent_results.md)
(inspected Git blob 3c95d28228cc59f71de529b1ec8e268841537a54, dated 23 October)
explicitly leave conditional three-point incidence/covariance and mixed
smoothness estimates open in their 3/8 route. The corresponding
[genus-two RH note](https://github.com/kasper0406/factoring-connection/blob/main/notes/genus2rh_results.md)
(inspected blob b553739cf674013824dd1483e624112dfb412ef5)
is an RH-dependent small-factor test and is not a general one-third
factorer. These sources identify concrete audit questions for the new
paper, not evidence that its newer method has the same gaps.

### Proof-level intake checklist when the primary PDF is available

1. Pin the exact bytes, title page, theorem statements and bibliography.
   Distinguish RH for zeta, Dirichlet GRH, and zero-free strips, including
   their actual formal theorem statements and assumptions.
2. Verify the distribution of requests generated by the selected
   relations, conditional on all previous data and retries. Unweighted
   density in a universe of possible labels does not alone bound failure
   on the selected child incidences.
3. Check the multilevel branching/weight normalization, tail bounds,
   abort/restart law, uniform thresholds, and the entire sum of charged
   costs, including unsuccessful requests and cofactors.
4. Check square-class certification in each actual field, exceptional
   classes, units and ideal-prime labels, existence and complexity of
   extracting square roots, and transcript symmetry of the final
   nontrivial-root probability.
5. Check shrinking recursive inputs, bit cost of modular and number-field
   arithmetic, linear-algebra complexity and all constant optimization
   on the same model as the theorem. Only then transfer any theorem to
   our comparison table or improve its parameters.

No claim here settles or refutes the reported Shanghai bound. The primary
PDF is needed to complete the requested audit. The research goal must
not be selected on the assumption that the announcement has already
been proved or that a rumored polynomial-time method exists.
