import Factoring.Prefix
import Mathlib.Analysis.SpecialFunctions.Exp
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity

/-! Finite squared-norm Euler-product decay. This is the algebraic part
of the deterministic squarefree progression proof: the prime-sum and
Mellin hypotheses are not asserted here. -/
namespace Factoring.EulerDecay
open scoped BigOperators

theorem local_decay (z : ℂ) (r : ℝ) (hr : 0 ≤ r) (hr1 : r ≤ 1)
    (hs : Complex.normSq z ≤ r^2) (hre : z.re ≤ r) :
    Complex.normSq (z+1) ≤ (1+r)^2 * Real.exp (-(r-z.re)/2) := by
  have heq : Complex.normSq (z+1) = Complex.normSq z + 1 + 2*z.re := by
    rw [Complex.normSq_add]
    simp [Complex.normSq_one]
  have hA : 0 ≤ r-z.re := sub_nonneg.mpr hre
  have hB : (1+r)^2 ≤ 4 := by nlinarith
  have hmul := mul_le_mul_of_nonneg_right hB hA
  have hE := Real.add_one_le_exp (-(r-z.re)/2)
  calc
    _ ≤ (1+r)^2 * (1-(r-z.re)/2) := by rw [heq]; nlinarith
    _ ≤ _ := mul_le_mul_of_nonneg_left (by linarith) (sq_nonneg _)

/-- Product decay with a nonnegative mass deficit at each prime. No
logarithm of a possibly zero local factor or branch choice is needed. -/
theorem product_decay {I : Type*} (s : Finset I) (z : I → ℂ) (r : I → ℝ)
    (h : ∀ i ∈ s, 0 ≤ r i ∧ r i ≤ 1 ∧
      Complex.normSq (z i) ≤ (r i)^2 ∧ (z i).re ≤ r i) :
    Complex.normSq (∏ i ∈ s, (z i+1)) ≤
      (∏ i ∈ s, (1+r i)^2) * Real.exp (∑ i ∈ s, -(r i-(z i).re)/2) := by
  classical
  rw [map_prod, Real.exp_sum, ← Finset.prod_mul_distrib]
  apply Finset.prod_le_prod
  · intro i _
    exact Complex.normSq_nonneg _
  · intro i hi
    obtain ⟨h0,h1,h2,h3⟩ := h i hi
    exact local_decay (z i) (r i) h0 h1 h2 h3

end Factoring.EulerDecay

#print axioms Factoring.EulerDecay.local_decay
#print axioms Factoring.EulerDecay.product_decay
