import Mathlib.NumberTheory.DirichletCharacter.Orthogonality
import Mathlib.NumberTheory.MulChar.Lemmas
import Mathlib.Analysis.Complex.Polynomial.Basic
import Mathlib.Algebra.Star.BigOperators
import Mathlib.Tactic.Ring

/-! Exact orthogonality for injective prefix residues, the diagonal
mechanism in the two-prefix argument. The analytic tail and
zero-density estimates are separate obligations. -/
namespace Factoring.Prefix
open scoped BigOperators

theorem prefix_bilinear {q : ℕ} [NeZero q] {I : Type*}
    (s : Finset I) (r : I→ZMod q)
    (hu : ∀ i∈s, IsUnit (r i)) (hinj : Set.InjOn r (s:Set I))
    (w v : I→ℂ) :
    (∑ χ : DirichletCharacter ℂ q,
      (∑ i∈s, w i*χ (r i)⁻¹)*(∑ j∈s, v j*χ (r j))) =
      (q.totient:ℂ)*(∑ i∈s,w i*v i) := by
  classical
  calc
    _ = ∑ i∈s, ∑ j∈s, ∑ χ : DirichletCharacter ℂ q,
          (w i*χ (r i)⁻¹)*(v j*χ (r j)) := by
      simp_rw [Finset.sum_mul,Finset.mul_sum]
      rw [Finset.sum_comm]
      apply Finset.sum_congr rfl
      intro i _
      rw [Finset.sum_comm]
    _ = ∑ i∈s, ∑ j∈s, w i*v j*(if r i=r j then (q.totient:ℂ) else 0) := by
      apply Finset.sum_congr rfl
      intro i hi
      apply Finset.sum_congr rfl
      intro j _
      calc
        _ = ∑ χ : DirichletCharacter ℂ q, (w i*v j)*(χ (r i)⁻¹*χ (r j)) := by
          apply Finset.sum_congr rfl
          intro χ _
          ring
        _ = _ := by
          rw [←Finset.mul_sum,DirichletCharacter.sum_char_inv_mul_char_eq ℂ (hu i hi)]
    _ = _ := by
      rw [Finset.mul_sum]
      apply Finset.sum_congr rfl
      intro i hi
      rw [Finset.sum_eq_single i]
      · simp
        ring
      · intro j hj hji
        have hne : r i≠r j := fun h => hji (hinj hi hj h).symm
        simp [hne]
      · simp [hi]

/-- For a unit residue, inverse evaluation is the conjugate character value. -/
theorem star_eval {q : ℕ} [NeZero q] (χ : DirichletCharacter ℂ q)
    (a : ZMod q) (ha : IsUnit a) : star (χ a)=χ a⁻¹ := by
  rw [MulChar.star_apply',MulChar.inv_apply_eq_inv']
  have h : χ a⁻¹ * χ a=1 := by
    rw [← map_mul,(ZMod.inv_mul_eq_one_of_isUnit ha a).mpr rfl,map_one]
  have hne : χ a ≠ 0 := by intro hh; rw [hh,mul_zero] at h; exact zero_ne_one h
  apply (mul_right_cancel₀ hne)
  rw [inv_mul_cancel₀ hne,h]

/-- The actual L² identity for a weighted character prefix. -/
theorem prefix_parseval {q : ℕ} [NeZero q] {I : Type*}
    (s : Finset I) (r : I→ZMod q)
    (hu : ∀ i∈s, IsUnit (r i)) (hinj : Set.InjOn r (s:Set I))
    (w : I→ℂ) :
    (∑ χ : DirichletCharacter ℂ q, ‖∑ i∈s,w i*χ (r i)‖^2) =
      (q.totient:ℝ)*(∑ i∈s,‖w i‖^2) := by
  classical
  have h := prefix_bilinear s r hu hinj (fun i => star (w i)) w
  have hc : ∀ χ : DirichletCharacter ℂ q,
      (∑ i∈s, star (w i)*χ (r i)⁻¹)=star (∑ i∈s,w i*χ (r i)) := by
    intro χ
    rw [star_sum]
    apply Finset.sum_congr rfl
    intro i hi
    rw [star_mul,star_eval χ _ (hu i hi),mul_comm]
  simp_rw [hc] at h
  have hz : ∀ z:ℂ, star z*z=(‖z‖^2:ℝ) := fun z => by simpa only [Complex.ofReal_pow] using Complex.conj_mul' z
  simp_rw [hz] at h
  exact_mod_cast h

/-- Consecutive integer representatives below q are injective on reduction.
In the actual shortest-prefix argument this is applied after removing the
last prime, not to arbitrary prefixes of size qB. -/
theorem nat_prefix_injective {q : ℕ} (s : Finset ℕ) (h : ∀ n∈s,n<q) :
    Set.InjOn (fun n:ℕ => (n:ZMod q)) (s:Set ℕ) := by
  intro a ha b hb he
  have hv := congrArg ZMod.val he
  simpa only [ZMod.val_natCast_of_lt (h a ha),ZMod.val_natCast_of_lt (h b hb)] using hv

end Factoring.Prefix
