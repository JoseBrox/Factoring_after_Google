# Corrections and rejected shortcuts

These items record why several attractive shortcuts were not used as originally stated. The current manuscript statements incorporate the corrections.

1. **Perron horizontal contribution.** The deterministic progression estimate must retain the horizontal-contour prefactor. Dropping it obscures the large-modulus obstruction. The general factoring manuscript includes the corrected bound and checks it against the replacement schedule.
2. **Weil root count.** A multiplicative-character bound counts distinct roots in a splitting field, not only roots in the ground field. The polynomial $X^3+2X$ over $\mathbb F_5$ gives an explicit counterexample to the ground-field-root version: it has one ground-field root and character sum $-4$. The actual Burgess moment polynomials split into linear factors, so the correctly stated theorem applies there.
3. **Exponent saturation.** The relevant divisibility statement is $m_\ell\mid P_K^K$, not $m_\ell\mid P_K$. The exact extractor and saturation argument preserve the powers.
4. **Biquadratic enumeration.** The shared appendix replaces an inadequately specified enumeration step with quadratic-unit reduction, at most eight parity targets, weighted four-dimensional LLL, and a fixed coordinate box. Its cost is polynomial in the numeric discriminant and search bounds, not automatically polynomial in their bit lengths.
5. **Ramified Gram factors.** Local Euler factors at ramified primes need their own PSD decomposition. Treating them as unramified signs would omit cases.
6. **Randomized recursion choice.** The tentative choice $g=3$ fails the root-volume inequality by $75/256$. The retained choice $g=43/8$ has positive root margin $1/256$; all downstream margins and the recursion cap are rechecked exactly.
7. **Endpoint relation saturation.** Looking only at $(X-a)^M-1$ can lose a factor when $M$ saturates both local groups. At $N=35$, $b=2$, $M=48$, the one-shot routine succeeds on only 10 of 35 parameters, whereas the full chain succeeds on all 35. This is a finite example supporting the necessity of the chain, alongside the general proof.
8. **Trace does not determine rank.** Over $\mathbb F_2$, the all-ones $2\times2$ matrix is nonzero, rank one, and nilpotent. It has the same characteristic polynomial and all power traces as the zero matrix. N1124's trace-only rank shortcut is therefore insufficient.
9. **Fixed quotient data is not a full coefficient prefix.** The N1002 reduction does not establish the needed bound for every prefix coefficient. The archived note gives the polynomial obstruction.
10. **A common lattice relation need not separate factors.** In $r-s\equiv0\pmod h$, shortest vectors such as $(1,1)$ can encode a common relation. N1131 needs an additional separation argument.
11. **Source nonresidue L-notation.** The source's displayed explicit exponential bound and its fixed-constant $L[1/2,O(1)]$ label differ under the standard convention. The README preserves the explicit source bound; see [comparison sources](comparison_sources.md).

Items 2, 5–8 and the parameter margins have exact executable checks in [verification](../verification/README.md). Other corrections are mathematical arguments in the manuscripts and historical audit notes; the presence of a test suite is not presented as proof of those arguments.
