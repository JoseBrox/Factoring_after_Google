import Factoring.Quadratic
import Mathlib.Data.Nat.Log
import Mathlib.Data.Nat.Factorization.Basic

/-! Exact arithmetic-operation budgets for the binary-power / squaring-chain
construction, not a machine-code bit-complexity model. -/
namespace Factoring.Quadratic

/-- Number of multiplications in the recursive binary powering algorithm:
one square per nonzero exponent, one extra product for an odd exponent. -/
def powerCost (n : ℕ) : ℕ :=
  if hn : n = 0 then 0 else powerCost (n/2) + 1 + n%2
termination_by n
decreasing_by omega

theorem powerCost_le (n : ℕ) : powerCost n ≤ 2*(Nat.log 2 n+1) := by
  induction n using Nat.strong_induction_on with
  | h n ih =>
    by_cases hn : n = 0
    · subst n
      rw [powerCost]
      simp
    rw [powerCost, dif_neg hn]
    have hi := ih (n/2) (by omega)
    by_cases h : n < 2
    · have hn1 : n=1 := by omega
      subst n
      rw [show (1:ℕ)/2=0 by decide, powerCost]
      simp
    · have hlog := Nat.log_pos (by decide : 1<2) (by omega : 2≤n)
      rw [Nat.log_div_base] at hi
      omega

theorem log_two_mul_power (u steps : ℕ) (hu : u ≠ 0) :
    Nat.log 2 (2^steps*u) = Nat.log 2 u + steps := by
  induction steps with
  | zero => simp
  | succ s ih =>
    rw [pow_succ, show (2^s*2)*u=(2^s*u)*2 by ring]
    rw [Nat.log_mul_base (by decide : 1<2) (mul_ne_zero (pow_ne_zero _ (by decide)) hu), ih]
    omega

/-- The explicit upper bound for multiplication count, including the norm
evaluation's three scalar products only as a separate constant allowance. -/
theorem chain_cost_le (u steps : ℕ) (hu : u ≠ 0) :
    powerCost u + steps ≤ 2*(Nat.log 2 (2^steps*u)+1) := by
  rw [log_two_mul_power u steps hu]
  have h := powerCost_le u
  omega

/-- Two coefficient tests per stage use at most three gcds, plus two for
the norm branch (a conservative bound, including the repeated norm gcd). -/
theorem chain_gcd_budget (u steps : ℕ) (hu : u ≠ 0) :
    2+3*(steps+1) ≤ 3*(Nat.log 2 (2^steps*u)+1)+2 := by
  rw [log_two_mul_power u steps hu]
  omega

end Factoring.Quadratic
