# Explicit paired units with surplus-degree monic fields

**Status:** proved written construction of many shared, independently
generated unit relations. This is a possible supplement to the
polynomial-mark algorithm, not an order-extraction or factoring theorem.
In particular it does not establish the covariance hypothesis in
monic_polynomial_mark_factorer.md.

## 1. Construction

Let n be the binary length of an odd composite N. For sufficiently
large n let d be the least power of 2 at least 8 sqrt(n), let
k=ceil(d/sqrt(log_2 n)), J=ceil(20d/sqrt(log_2 n)), and
r=d-k-J. These integer choices can be made by replacing sqrt(log_2 n)
with the integer square root of floor(log_2 n), with no change to the
following estimates. Use m=2^ceil(n/k).

Choose a prime ell of polynomial size in n with
\[
 \ell\equiv1\pmod {2d},\qquad \ell\equiv2\pmod3,
 \qquad \gcd(6\ell,N)=1.
\]
For example, existence in a sufficiently large polynomial dyadic
interval follows from the smoothed character estimate in the
polynomial-mark note: the fixed residue class modulo 6d has density
1/phi(6d), and the uniform error with exponent 15/16 is negligible
for X=n^128. One can also impose desired Legendre signs at two hidden
prime factors greater than X, by the same character orthogonality
argument with modulus 6dpq. The principal coefficient is then
1/(4 phi(6d)). The character expansion has absolute coefficient sum
at most 1. The algorithm simply enumerates the publicly specified
class and tests gcds; the signs are used only for the existence proof.

Set
\[
 R_j=3\ell(2j+1),\quad P(X)=\prod_{j=1}^d(X-R_j),
 \qquad Q(X)=\prod_{j=1}^r(X-R_j).
\]
The marks R_j are odd multiples of 3ell. Check gcd(m-R_j,N).
Since m grows faster than every polynomial in n but is smaller
than N, any nontrivial gcd is proper eventually. If none occurs,
Q(m) is invertible modulo N.

For i=1,2 put c_1=1,c_2=3. Choose a scalar h_i,0 modulo 4ell
satisfying
\[
 h_{i,0}\equiv0\pmod\ell,\qquad
 P(0)+c_i+Q(0)h_{i,0}\equiv2\pmod4.
\]
This is possible with h_i,0 even because P(0),Q(0),c_i are odd
and Q(0) is invertible modulo 4. Take the least nonnegative
representative. Form the base-m digit polynomial T_i of
\[
 -\big(P(m)+c_i+Q(m)h_{i,0}\big)
                   (4\ell Q(m))^{-1}\pmod N .
\]
It has degree <k since m^k>=2^n>N. Put
\[
 f_i(X)=P(X)+c_i+Q(X)(h_{i,0}+4\ell T_i(X)).
\]
Then f_i is monic of degree d, and f_i(m)=0 modulo N. The
correction has degree at most r+k-1=d-J-1, apart from the
constant c_i. These formulas are all computable in polynomial
bit time.

Modulo 2, P(X)=(X+1)^d=X^d+1, the odd constant adds 1, and
the Q correction vanishes. The constant coefficient is 2
modulo 4. Hence both f_i are Eisenstein at 2 and irreducible
over Q. Modulo ell their reductions are X^d+1 and X^d+3.
The first splits completely with distinct roots since 2d
divides ell-1. For the second, quadratic reciprocity gives
(-3/ell)=-1: for ell=1 modulo 4, (3/ell)=-1 when ell=2 modulo 3.
If beta is a root of X^d+3, its order has 2-adic valuation
v_2(ell-1)+log_2 d, since beta^d=-3 has order with full
2-part v_2(ell-1). If beta is in F_(ell^a), then
v_2(ell^a-1)=v_2(ell-1)+v_2(a), by lifting the exponent and
ell=1 modulo 4. Thus d divides a. Since the root has degree
at most d, it has degree exactly d; f_2 is irreducible modulo ell.

## 2. All roots are real and close to the centers

Use eta=1/[4(ell d)^floor(J/4)]. The log of |P| at either
endpoint of each sign bracket is at least
\[
 (d-J/4)\log(\ell d)-O(d+\log(\ell d)).
\]
This follows from the factorial bound on the product of
distances to the other centers, just as in Proposition 1 of
the polynomial-mark note. The log of an upper bound for
the correction is at most
\[
 (d-J)\log(\ell d)+O(d+\log m+\log(\ell d)).
\]
Indeed Q is a product of r linear factors, each bounded by
O(ell d) near all the centers, and h_i has degree <k,
coefficients bounded by O(ell m). The gap tends to infinity:
J log(ell d) is at least (10+o(1))d sqrt(log_2 n)
times an absolute positive logarithm-conversion constant,
whereas log m is at most O((n/d)sqrt(log_2 n)).
With d>=8 sqrt(n), the constant 20 in J gives ample strict
margin. More explicitly log(ell d)>=log d>=
(log 2)(log_2 n)/2, so (3/4)J log(ell d) is at least
(7.5 log 2+o(1))d sqrt(log_2 n), while
log m <= (log 2/64+o(1))d sqrt(log_2 n).
All d disjoint brackets therefore contain a simple real root
of each polynomial. Denote the roots by theta_i,j.
The brackets, signs, and coefficient heights can be checked
by exact integer arithmetic in polynomial bit time.

## 3. Many explicit paired units

For every 1<=j<=r the evaluations are exact:
\[
 f_1(R_j)=1,\qquad f_2(R_j)=3.
\]
Because d is even, the field norms of theta_1-R_j and
theta_2-R_j are respectively 1 and 3. Thus the first is a
unit, and the second generates a prime ideal of norm 3 in
the full ring of integers (no power-order index condition
at 3 is required). All of these latter ideals are identical:
their generators differ by multiples of 3, which belong to
the prime ideal of norm 3, and equal norms force equality.

Consequently for j=2,...,r the elements
\[
 u_{i,j}=\frac{\theta_i-R_j}{\theta_i-R_1}
\]
are units in both fields. Their expressions have the same
modular image in the localized polynomial orders, namely
(m-R_j)/(m-R_1) modulo N. This assertion uses the exact
unit/gcd guards; it does not assert that the evaluation
map is defined on the entire ring of integers.

These paired units are multiplicatively independent modulo
torsion. It suffices to check field 1. Use R=10ell d and
consider the r by r matrix of entries
log(|theta_1,i-R_j|/R) for i,j<=r. For i != j the absolute
distance is comparable to ell |i-j|, with uniform constants.
Hence the sum of absolute off-diagonal entries in each row
is O(d), by the factorial estimate for
sum_(a=1)^d log(d/a). The norm-one identity at mark R_i
gives for the diagonal
\[
 \log(|\theta_{1,i}-R_i|/R)
            =-d\log R+O(d).
\]
The same factorial estimate uses all d embeddings here,
including those not in the displayed matrix. The matrix is
strictly diagonally dominant and invertible for large d.
A relation among the ratios gives a log relation among
these r columns with coefficient sum zero; subtracting
log R from every entry has no effect on such a relation.
Invertibility forces all coefficients zero.

Thus the product log-unit lattice has an explicitly constructible
subgroup of rank
\[
 r-1=d-O(d/\sqrt{\log n}).
\]
The full product rank is 2d-2. These relations are available
without finding a single smooth resultant. They do not yet
span the full product lattice, and their common modular images
do not by themselves give a useful order multiple. The similar
root centers of the two fields can also make independent joint
log directions hard to find. It would be incorrect to count
these paired units as twice their rank, or to infer factoring
from their existence alone.

## 4. Implication for the research program

The construction shows that exact paired-unit supply is not
inherently tied to exponential perturbation searches. It suggests
trying to replace only the missing unit directions with polynomial
marks, rather than demanding a full basis from smooth values.
This is a second route to investigate, alongside the one-mark
covariance contract. It does not eliminate the need for nontrivial
ideal relations involving the target prime ell.
