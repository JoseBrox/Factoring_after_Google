import Factoring.ChainCount
import Mathlib.NumberTheory.LegendreSymbol.QuadraticChar.Basic
import Mathlib.Tactic.Linarith

/-! The bridge from a quadratic character sum to the affine curve count.
A projective model and its Weil point-count theorem are not yet supplied. -/
namespace Factoring.Curve
open scoped BigOperators

/-- This identity works for an arbitrary right-hand side, including
repeated roots and zeros; it uses the actual field character. -/
theorem quadratic_sum_affine_count {F : Type*} [Field F] [Fintype F] [DecidableEq F]
    (hchar : ringChar F ≠ 2) (f : F→F) :
    (Nat.card {z:F×F // z.2^2=f z.1}:ℤ) =
      (Fintype.card F:ℤ)+∑ a:F,quadraticChar F (f a) := by
  classical
  let e : (Σ a:F,{y:F // y^2=f a}) ≃ {z:F×F // z.2^2=f z.1} :=
    {toFun := fun z => ⟨(z.1,z.2.1),z.2.2⟩
     invFun := fun z => ⟨z.1.1,⟨z.1.2,z.2⟩⟩
     left_inv := by rintro ⟨a,y,hy⟩; rfl
     right_inv := by rintro ⟨⟨a,y⟩,hy⟩; rfl}
  rw [←Nat.card_congr e,Nat.card_eq_fintype_card,Fintype.card_sigma,Nat.cast_sum]
  have h (a:F) : (Fintype.card {y:F // y^2=f a}:ℤ)=quadraticChar F (f a)+1 := by
    rw [Fintype.card_subtype]
    simpa only [Set.toFinset_setOf] using quadraticChar_card_sqrts hchar (f a)
  simp_rw [h]
  rw [Finset.sum_add_distrib]
  simp [add_comm]

/-- If the projective curve has the stated count bound and the affine
chart has t missing points, the character sum has the corresponding
absolute bound. This is only the numerical endgame of the Weil argument. -/
theorem sum_bound_from_projective_count {F : Type*} [Field F] [Fintype F] [DecidableEq F]
    (hchar : ringChar F ≠ 2) (f : F→F) (P t : ℕ) (C : ℝ)
    (hpoints : P=Nat.card {z:F×F // z.2^2=f z.1}+t)
    (hweil : |(P:ℝ)-(Fintype.card F:ℝ)-1|≤C) :
    |(↑(∑ a:F,quadraticChar F (f a)) : ℝ)|≤C+|1-(t:ℝ)| := by
  have h := quadratic_sum_affine_count hchar f
  have hreal : (Nat.card {z:F×F // z.2^2=f z.1}:ℝ) =
      (Fintype.card F:ℝ)+(↑(∑ a:F,quadraticChar F (f a)):ℝ) := by exact_mod_cast h
  have hp : (P:ℝ)=(Nat.card {z:F×F // z.2^2=f z.1}:ℝ)+(t:ℝ) := by exact_mod_cast hpoints
  have he : (↑(∑ a:F,quadraticChar F (f a)):ℝ) =
      ((P:ℝ)-(Fintype.card F:ℝ)-1)+(1-(t:ℝ)) := by linarith
  rw [he]
  exact (abs_add_le _ _).trans (add_le_add_right hweil _)

end Factoring.Curve
