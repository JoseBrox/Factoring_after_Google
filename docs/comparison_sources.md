# Comparison sources and scope

Comparison date: 27 November 2026 (pinned Google baseline dated 25 November). The README's predecessor column identifies the exact bounds that the new constructions seek to improve. It does not promote a newly posted claim into an independently established literature record.

## Pinned recent predecessors

Both source manuscripts come from Google Research commit `4a7bc8ab0bc770e71a259b7966c500496b99010a`. All page and theorem references below are to those immutable PDFs, not to a moving default branch.

| Problem | Source location | Bound as stated in the source | How it is used here |
|---|---|---|---|
| Deterministic general factoring | Deterministic paper, Theorem 1.1; abstract on page 1 | $O(\exp(3(\log N)^{3/4}))$ | Baseline architecture for the replacement parameter schedule |
| Supplied-order splitting | Deterministic paper, Theorem 1.2 and abstract | $O(\exp(C_{\rm split}\sqrt{\log N}\log\log(N+16))\,(\log M)(\log N)^2)$ | Like-for-like promised-input predecessor |
| Quadratic nonresidue | Deterministic paper, Theorem 1.2 and abstract | $\exp(O(\sqrt{\log p}\log\log p))$ | Like-for-like prime-input predecessor; retain the explicit expression |
| Randomized factoring | Randomized paper, Theorem 1.1, page 2 | Expected time $L_N[1/3,105]$, deterministic workspace $L_N[1/3,40]$ | The source's headline theorem |
| Randomized tighter bookkeeping | Randomized proof, Step 2 on page 47; Step 4 on pages 48–49 | Workspace constant 38 and time constant 104 appear in the concluding analysis | Also reported, so the comparison does not hide the tighter source accounting |

Source PDFs and READMEs: [deterministic](https://github.com/google-research/google-research/tree/4a7bc8ab0bc770e71a259b7966c500496b99010a/cogentic_research_papers/deterministic_factoring_l34), [randomized](https://github.com/google-research/google-research/tree/4a7bc8ab0bc770e71a259b7966c500496b99010a/cogentic_research_papers/integer_factorization). The source READMEs attribute the papers to Cogentic using Gemini 4 and promise a companion release of formal proofs. Their announcement is not a verification performed by this repository.

The deterministic source's general-factor theorem is stated for finding a proper factor of a composite input. Recursive completion preserves the exponent in the comparison; extra polynomial factors should not be suppressed when discussing its exact displayed constant. The randomized source theorem is explicitly for complete prime factorization. The new deterministic manuscript explains the corresponding reduction, while the randomized manuscript keeps the complete-factorization output specification throughout.

## Established historical reference points

H. W. Lenstra, Jr. and C. Pomerance, *A rigorous time bound for factoring integers*, JAMS 5 (1992), 483–516, proves a randomized $L_N[1/2,1]$ bound. [Primary article](https://cr.yp.to/bib/1992/lenstra.pdf), [DOI](https://doi.org/10.1090/S0894-0347-1992-1137100-0).

The number field sieve literature gives the familiar heuristic general factoring complexity $L_N[1/3,(64/9)^{1/3}]$. See A. K. Lenstra and H. W. Lenstra, Jr., eds., *The Development of the Number Field Sieve*, Springer LNM 1554 (1993), [DOI](https://doi.org/10.1007/BFb0091539). A heuristic constant and a proved worst-case expected constant should be labeled separately.

The new randomized manuscript has not discharged all widened analytic contracts. Its $91.4$ constant therefore does not replace either the rigorous established benchmark or the heuristic GNFS benchmark as an unconditional record.

## A notation discrepancy in the source presentation

The deterministic source README writes the nonresidue expression $\exp(O(\sqrt{\log p}\log\log p))$ and also labels it $L_p[1/2,O(1)]$. Under the standard convention stated in this repository those expressions are not equivalent: the latter has exponent $O(\sqrt{\log p\,\log\log p})$.

The comparison table uses the source's explicit exponential expression. The new sparse construction saves a factor $\sqrt{\log\log p}$ in the exponent. This is a correction to how the source's notation is reported, not a claim that the source proves the stronger expression.

## Citation policy

Cite the theorem actually used, its hypotheses, and a stable version. For recent manuscripts, distinguish a written claim from independent review and from a checked formalization. For an improved parameter choice, check the proof at that choice rather than substituting new constants into a theorem that only states fixed old constants.

## Additional reported November 2026 result: growing descent

The KeyBreak Cryptanalysis Agent, *Provable Integer Factorization via Multilevel Descent: Approaching Heuristic Bounds* (26 November 2026; title and author verified from the uploaded PDF), [manuscript](https://crypto.sjtu.edu.cn/factoring.pdf). The [Big O Speedrun board](https://bigospeedrun.com/integer-factoring-randomized) reports:

| Reported theorem | Expected time | Hypothesis/evidence |
|---|---|---|
| 1.1 | \(L_N[1/3,10^{13}]\) | Claimed unconditional written proof |
| 1.2 | \(L_N[1/3,2.97]\) | Claimed proof using Dirichlet GRH |

Retrieved the board and [announcement/republication](https://cn-sec.com/archives/5619552.html) on 27 November. The primary PDF was subsequently supplied by the user. SHA-256: `2b534eaf77fb2b9712018879059d8d4667c40c0a4adf2fff90efc22fb356cfc9`. See [the pinned-source audit](keybreak_source_audit.md). The originally reported constant 1013 was a superscript transcription error: the PDF states 10^13. The full analytic proof has not been independently certified. The board's reported verification of an external GRH result is not a checked formalization of either factoring theorem. The claimed \(2.97\) is smaller than the source's \(105\) and our conditional \(91.4\), but no unconditional record or direct improvement is inferred from unverified claims.

The accessible precursor, Kasper Nielsen, *Theorem U-MF: a Las Vegas factoring algorithm in expected time L_N[2/5]* (28 October 2026), [pinned manuscript](https://github.com/kasper0406/factoring-connection/blob/351e8eeee142b2b13790cf67c3e8e2e35aaf1f0d/notes/mfU_theorem.md), is the source for the generalized accounting arguments in [this note](multilevel_descent_accounting.md). It is a distinct manuscript. See the [source-intake audit](2026-11-27_source_intake_and_closure.md) for the missing evidence and the proof-level checklist. The README's pinned baseline column remains unchanged.


The [compressed unconditional-route continuation](keybreak_unconditional_compression.md) gives a new proposed expected-time transfer \(L_N[1/3,40]\) conditional on the explicitly stated ordinary and semismooth covariance transfer and source certificate/computation bounds. The arithmetic route is intended to be unconditional (no GRH); the independent proof audit is incomplete. This does not supersede the source's claimed GRH constant or establish a new unconditional record.


The [U100 intermediate target](keybreak_unconditional_fallback.md) uses the source's original exceptional-mass transfer and sharpened ordinary moment parameters; it is conditional on the changed-range source estimates, without GRH in the proposed arithmetic route. The [G2.96/2.95 cost transfer](keybreak_grh_constants.md) retains Dirichlet GRH. The former uses the original source geometry and changes only caps; the latter also requires a changed-range analytic audit. They are separate from the U40 target and do not establish unconditional records.


**Written-proof continuation:** [U100](keybreak_u100_proof.md) and [U40](keybreak_u40_proof.md) supply the changed-range arguments that the above historical conditional ledgers isolated, including the weighted semismooth covariance and linear exceptional-mass transfer for 40. Their stated expected-time bounds are \(L_N[1/3,100]\) and \(L_N[1/3,40]\), using the pinned source's finite lemmas and classical unconditional analytic imports. They have not received independent review or complete formal verification. The source's claimed GRH 2.97 is a different result, and no new workspace bound or independently established record is claimed.


**Optimized written continuation:** [U14.1](keybreak_u142_proof.md#8-tighten-the-same-schedule-to-141) derives changed-range ordinary/semismooth concentration and revised exact coefficient-window, sieve and recursive cost ledgers using [the U40 critical audit](keybreak_u40_critical_audit.md). It uses the pinned manuscript's finite results and classical unconditional analytic inputs; no explicit GRH or extra covariance conjecture is used. It is not independently refereed or formally certified. The separate [probe-free unit certificate](exact_descent_unit_certificate.md) uses Ge (1994), Props. 6.2–6.3, and polynomial-precision unit lattice recovery; no new numerical constant is inferred from that replacement. [The beyond-one-third research](beyond_one_third_research.md) proves architecture-specific obstructions and isolates the next target, not a general complexity lower bound.
