# Comparison sources and scope

Comparison date: 25 November 2026. The README's predecessor column identifies the exact bounds that the new constructions seek to improve. It does not promote a newly posted claim into an independently established literature record.

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

## Established historical reference points

H. W. Lenstra, Jr. and C. Pomerance, *A rigorous time bound for factoring integers*, JAMS 5 (1992), 483–516, proves a randomized $L_N[1/2,1]$ bound. [Primary article](https://cr.yp.to/bib/1992/lenstra.pdf), [DOI](https://doi.org/10.1090/S0894-0347-1992-1137100-0).

The number field sieve literature gives the familiar heuristic general factoring complexity $L_N[1/3,(64/9)^{1/3}]$. See A. K. Lenstra and H. W. Lenstra, Jr., eds., *The Development of the Number Field Sieve*, Springer LNM 1554 (1993), [DOI](https://doi.org/10.1007/BFb0091539). A heuristic constant and a proved worst-case expected constant should be labeled separately.

The new randomized manuscript has not discharged all widened analytic contracts. Its $91.4$ constant therefore does not replace either the rigorous established benchmark or the heuristic GNFS benchmark as an unconditional record.

## A notation discrepancy in the source presentation

The deterministic source README writes the nonresidue expression $\exp(O(\sqrt{\log p}\log\log p))$ and also labels it $L_p[1/2,O(1)]$. Under the standard convention stated in this repository those expressions are not equivalent: the latter has exponent $O(\sqrt{\log p\,\log\log p})$.

The comparison table uses the source's explicit exponential expression. The new sparse construction saves a factor $\sqrt{\log\log p}$ in the exponent. This is a correction to how the source's notation is reported, not a claim that the source proves the stronger expression.

## Citation policy

Cite the theorem actually used, its hypotheses, and a stable version. For recent manuscripts, distinguish a written claim from independent review and from a checked formalization. For an improved parameter choice, check the proof at that choice rather than substituting new constants into a theorem that only states fixed old constants.
