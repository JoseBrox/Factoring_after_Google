# Notation and cost conventions

| Symbol | Meaning |
|---|---|
| $N$ | Integer to be factored, represented in binary |
| $p,q$ | Prime divisors or prime inputs, as specified locally |
| $L$ | $\log N$, with natural logarithms unless stated otherwise |
| $L_2$ | $\log\log N$ |
| $\operatorname{len}(x)$ | Binary length, taken to be at least one |
| $L_N[\alpha,c]$ | $\exp((c+o(1))(\log N)^\alpha(\log\log N)^{1-\alpha})$ |
| $M$ | Supplied exponent; its exact divisibility promise is part of each theorem |
| $O_\varepsilon(\cdot)$ | The hidden constant may depend on a fixed positive $\varepsilon$ |
| $\chi$, $(b/p)$ | Dirichlet character, Legendre symbol |
| $\Psi(x,y)$ | Count of positive integers at most $x$ whose prime divisors are at most $y$ |
| PSD | Positive semidefinite, in the sense of quadratic forms |

The manuscripts specify bit complexity on a classical multitape Turing machine. A bound in ring operations is explicitly labeled as such and must be multiplied by the bit cost of the ring operations before comparing it to a bit bound.

Two expressions that look similar have different $L$-behavior:

$$\exp(O(\sqrt{\log N\,\log\log N}))=L_N[1/2,O(1)],$$

whereas $\exp(O(\sqrt{\log N}\,\log\log N))$ has an extra factor $\sqrt{\log\log N}$ in its exponent. The latter is not a fixed-constant $L_N[1/2,c]$ estimate under this convention.

Likewise, having a bound $\exp(O_\varepsilon((\log N)^{2/3+\varepsilon}))$ for every fixed positive $\varepsilon$ does not justify setting $\varepsilon=0$, or allowing it to vary with $N$ without controlling the constants and thresholds.
