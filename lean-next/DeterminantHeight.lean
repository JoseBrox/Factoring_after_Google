import Mathlib.LinearAlgebra.Matrix.Adjugate
import Mathlib.Data.Fintype.Perm
import Mathlib.Algebra.Order.BigOperators.Group.Finset
import Mathlib.Tactic.Positivity

/-! Explicit determinant heights. Leibniz rather than Hadamard is
sufficient for the manuscript's logarithmic height scale. -/
namespace Factoring.DeterminantHeight
open scoped BigOperators
open Matrix

theorem det_bound {ι : Type*} [Fintype ι] [DecidableEq ι]
    (A : Matrix ι ι ℝ) (B : ℝ) (hB : 0≤B)
    (h : ∀ i j, |A i j|≤B) :
    |A.det| ≤ (Fintype.card ι).factorial * B^(Fintype.card ι) := by
  classical
  rw [Matrix.det_apply']
  calc
    _ ≤ ∑ σ : Equiv.Perm ι, |(↑(Equiv.Perm.sign σ) : ℝ)*∏ i,A (σ i) i| := by
      exact Finset.abs_sum_le_sum_abs _ _
    _ ≤ ∑ _σ : Equiv.Perm ι, B^(Fintype.card ι) := by
      apply Finset.sum_le_sum
      intro σ _
      rw [abs_mul,Finset.abs_prod]
      have hsign : |(↑(Equiv.Perm.sign σ) : ℝ)|=1 := by
        have ht := Equiv.Perm.sign σ
        rcases Int.units_eq_one_or ht with he | he <;> simp [he]
      rw [hsign,one_mul]
      calc
        _ ≤ ∏ _i:ι, B := Finset.prod_le_prod (fun _ _ => abs_nonneg _) (fun i _ => h _ _)
        _ = _ := by simp
    _ = _ := by simp [Fintype.card_perm]

/-- This bounds all Cramer numerators by replacing a column by a vector
whose entries have the same height bound. -/
theorem cramer_bound {ι : Type*} [Fintype ι] [DecidableEq ι]
    (A : Matrix ι ι ℝ) (v : ι→ℝ) (B : ℝ) (hB : 0≤B)
    (hA : ∀ i j, |A i j|≤B) (hv : ∀ i, |v i|≤B) (j : ι) :
    |Matrix.cramer A v j| ≤ (Fintype.card ι).factorial * B^(Fintype.card ι) := by
  rw [Matrix.cramer_apply]
  apply det_bound _ B hB
  intro i k
  by_cases hk : k=j
  · subst k
    simpa using hv i
  · simpa [Matrix.updateCol, hk] using hA i k

end Factoring.DeterminantHeight

#print axioms Factoring.DeterminantHeight.det_bound
#print axioms Factoring.DeterminantHeight.cramer_bound
