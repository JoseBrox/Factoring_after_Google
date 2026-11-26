import Factoring.Gram
import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Linarith

/-! Finite stopping-time peeling. The analytic moment calculation supplies
the nonnegative base/error arrays and the weighted row-loss bound.
Here the cumulative deletion bound is proved for arbitrary finite
label sets, without a union bound over the adaptive stages. -/
namespace Factoring.Peeling
open scoped BigOperators
open Finset
variable {I : Type*} [Fintype I] [DecidableEq I]

def mass (w : I→ℝ) (D : Finset I) : ℝ := ∑ i ∈ D, w i

noncomputable def step (loss : Finset I→I→ℝ) (ζ : ℝ) (D : Finset I) : Finset I := by
  classical
  exact D ∪ univ.filter (fun i => ζ < loss D i)

noncomputable def stages (loss : Finset I→I→ℝ) (ζ : ℝ) (D₀ : Finset I) : ℕ→Finset I
  | 0 => D₀
  | n+1 => step loss ζ (stages loss ζ D₀ n)

theorem mem_step {loss : Finset I→I→ℝ} {ζ : ℝ} {D : Finset I} {i : I} :
    i ∈ step loss ζ D ↔ i ∈ D ∨ ζ < loss D i := by
  classical
  simp [step]

theorem initial_subset (loss : Finset I→I→ℝ) (ζ : ℝ) (D₀ : Finset I) (n : ℕ) :
    D₀ ⊆ stages loss ζ D₀ n := by
  induction n with
  | zero => exact Subset.rfl
  | succ n ih =>
    intro i hi
    exact mem_step.mpr (Or.inl (ih hi))

theorem young_bound {w m e ζ : ℝ}
    (hw : 0≤w) (hm : 0≤m) (he : 0≤e) (hz : 0<ζ) :
    Real.sqrt w * Real.sqrt (m*e) ≤ ζ*w/4+(m/ζ)*e := by
  have hh := sq_nonneg (ζ/2*Real.sqrt w-Real.sqrt (m*e))
  have hf : (ζ/2*Real.sqrt w-Real.sqrt (m*e))^2 =
      ζ^2*w/4-ζ*(Real.sqrt w*Real.sqrt (m*e))+m*e := by
    rw [sub_sq, mul_pow, Real.sq_sqrt hw, Real.sq_sqrt (mul_nonneg hm he)]
    ring
  rw [hf] at hh
  have h : Real.sqrt w*Real.sqrt (m*e) ≤ (ζ^2*w/4+m*e)/ζ :=
    (le_div_iff₀ hz).mpr (by nlinarith)
  have hform : (ζ^2*w/4+m*e)/ζ=ζ*w/4+(m/ζ)*e := by
    field_simp [ne_of_gt hz]
    ring
  rwa [hform] at h

theorem weighted_row_bound {w b e m ζ : ℝ} (hw : 0≤w) (hm : 0≤m) (he : 0≤e)
    (hz : 0<ζ) (hmean : 2*m≤ζ/4)
    (h : ζ*w ≤ w*b+2*m*w+Real.sqrt w*Real.sqrt (m*e)) :
    ζ/2*w≤w*b+(m/ζ)*e := by
  have hy := young_bound hw hm he hz
  have hx := mul_le_mul_of_nonneg_right hmean hw
  linarith

/-- The sum of all cumulative new-row charges is bounded by the full
base and Frobenius-error budgets, regardless of the stage of deletion. -/
theorem cumulative_bound (w b e : I→ℝ) (D D₀ : Finset I) (m ζ : ℝ)
    (hw : ∀ i, 0≤w i) (hb : ∀ i, 0≤b i) (he : ∀ i, 0≤e i)
    (hm : 0≤m) (hz : 0<ζ)
    (h₀ : D₀⊆D) (hm₀ : mass w D₀≤m/2)
    (hbudget : (∑ i, w i*b i)+(m/ζ)*(∑ i, e i)≤ζ*m/4)
    (hrows : ∀ i ∈ D\D₀, ζ/2*w i≤w i*b i+(m/ζ)*e i) :
    mass w D≤m := by
  classical
  have hsum : ζ/2*mass w (D\D₀) ≤
      (∑ i ∈ D\D₀, w i*b i)+(m/ζ)*(∑ i ∈ D\D₀, e i) := by
    unfold mass
    rw [Finset.mul_sum, Finset.mul_sum, ← Finset.sum_add_distrib]
    exact Finset.sum_le_sum hrows
  have hb' : (∑ i ∈ D\D₀, w i*b i) ≤ ∑ i, w i*b i :=
    Finset.sum_le_sum_of_subset_of_nonneg (Finset.subset_univ _) fun i _ _ =>
      mul_nonneg (hw i) (hb i)
  have he' : (∑ i ∈ D\D₀, e i) ≤ ∑ i, e i :=
    Finset.sum_le_sum_of_subset_of_nonneg (Finset.subset_univ _) fun i _ _ => he i
  have hmul := mul_le_mul_of_nonneg_left he' (div_nonneg hm hz.le)
  have hnew : mass w (D\D₀)≤m/2 := by
    apply (mul_le_mul_left (show 0<ζ/2 by linarith)).mp
    linarith
  have hsplit : mass w (D\D₀)+mass w D₀=mass w D := by
    unfold mass
    exact Finset.sum_sdiff h₀
  linarith

/-- All stages satisfy the mass cap and preserve every kept label.
The row hypothesis is the weighted mean/error estimate for a new deletion;
the global moment bounds occur only once in the cumulative charge.
This is the finite stopping-time invariant, not a proof of those analytic
row estimates. -/
theorem invariant (loss : Finset I→I→ℝ) (w b e : I→ℝ)
    (D₀ kept : Finset I) (m ζ : ℝ)
    (hw : ∀ i, 0≤w i) (hb : ∀ i, 0≤b i) (he : ∀ i, 0≤e i)
    (hm : 0≤m) (hz : 0<ζ) (hmean : 2*m≤ζ/4)
    (hm₀ : mass w D₀≤m/2)
    (hp₀ : ∀ i ∈ kept, i∉D₀)
    (hbudget : (∑ i, w i*b i)+(m/ζ)*(∑ i, e i)≤ζ*m/4)
    (hprotected : ∀ D, mass w D≤m → ∀ i ∈ kept, loss D i≤ζ)
    (hrow : ∀ D, mass w D≤m → ∀ i, i∉D → ζ<loss D i →
      ζ*w i≤w i*b i+2*m*w i+Real.sqrt (w i)*Real.sqrt (m*e i)) :
    ∀ n, mass w (stages loss ζ D₀ n)≤m ∧
      (∀ i ∈ kept, i∉stages loss ζ D₀ n) ∧
      (∀ i ∈ stages loss ζ D₀ n \ D₀, ζ/2*w i≤w i*b i+(m/ζ)*e i) := by
  intro n
  induction n with
  | zero =>
    change mass w D₀≤m ∧ (∀ i ∈ kept, i∉D₀) ∧
      (∀ i ∈ D₀\D₀, ζ/2*w i≤w i*b i+(m/ζ)*e i)
    exact ⟨by linarith,hp₀,by simp⟩
  | succ n ih =>
    let D := stages loss ζ D₀ n
    let D' := stages loss ζ D₀ (n+1)
    have hrows : ∀ i ∈ D'\D₀, ζ/2*w i≤w i*b i+(m/ζ)*e i := by
      intro i hi
      have hmem := Finset.mem_sdiff.mp hi
      by_cases h : i∈D
      · exact ih.2.2 i (Finset.mem_sdiff.mpr ⟨h,hmem.2⟩)
      · have ht : ζ<loss D i := (mem_step.mp hmem.1).resolve_left h
        exact weighted_row_bound (hw i) hm (he i) hz hmean (hrow D ih.1 i h ht)
    refine ⟨cumulative_bound w b e D' D₀ m ζ hw hb he hm hz
      (initial_subset loss ζ D₀ (n+1)) hm₀ hbudget hrows,?_,hrows⟩
    intro i hi hmem
    rcases mem_step.mp hmem with h | h
    · exact ih.2.1 i hi h
    · exact (not_lt_of_ge (hprotected D ih.1 i hi)) h

/-- The increasing sequence stabilizes after at most the total number
of labels. -/
theorem stabilizes (loss : Finset I→I→ℝ) (ζ : ℝ) (D₀ : Finset I) :
    ∃ n≤Fintype.card I, stages loss ζ D₀ (n+1)=stages loss ζ D₀ n := by
  classical
  by_contra h
  push_neg at h
  have hc : ∀ n≤Fintype.card I+1, n≤(stages loss ζ D₀ n).card := by
    intro n hn
    induction n with
    | zero => omega
    | succ n ih =>
      have hne := h n (by omega)
      have hsub : stages loss ζ D₀ n ⊆ stages loss ζ D₀ (n+1) := by
        intro i hi
        exact mem_step.mpr (Or.inl hi)
      have hlt := Finset.card_lt_card (ssubset_of_subset_of_ne hsub (Ne.symm hne))
      have hp := ih (by omega)
      omega
  have hh := hc (Fintype.card I+1) (by omega)
  have hu := Finset.card_le_univ (stages loss ζ D₀ (Fintype.card I+1))
  omega

end Factoring.Peeling
