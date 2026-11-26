import Mathlib.Analysis.SpecialFunctions.ExpDeriv
import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Analysis.Calculus.Deriv.MeanValue
import Mathlib.Analysis.Calculus.Deriv.Inv
import Mathlib.Topology.Order.IntermediateValue
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Positivity

/-! Exact finite squarefree saddle calculus. No asymptotic assertion is
included without proving the actual uniform analytic estimates. -/
namespace Factoring.Saddle
open scoped BigOperators
open Set

noncomputable def mass (J : Finset ℕ) (α : ℝ) : ℝ :=
  ∑ p∈J, Real.log p / (1+Real.exp (α*Real.log p))

noncomputable def variance (J : Finset ℕ) (α : ℝ) : ℝ :=
  ∑ p∈J, (Real.log p)^2*Real.exp (α*Real.log p)/(1+Real.exp (α*Real.log p))^2

theorem mass_deriv (J : Finset ℕ) (α : ℝ) :
    HasDerivAt (mass J) (-variance J α) α := by
  unfold mass variance
  rw [← Finset.sum_neg_distrib]
  apply HasDerivAt.sum
  intro p _
  have he : HasDerivAt (fun x : ℝ => Real.exp (x*Real.log p))
      (Real.exp (α*Real.log p)*Real.log p) α := by
    simpa using ((hasDerivAt_id α).mul_const (Real.log p)).exp
  have hd := (hasDerivAt_const α (1:ℝ)).add he
  have h := (hasDerivAt_const α (Real.log p)).div hd
    (by positivity : 1+Real.exp (α*Real.log p)≠0)
  convert h using 1
  · simp only [zero_mul,zero_add,sub_eq_add_neg,zero_add]
    ring

theorem variance_pos (J : Finset ℕ) (hJ : J.Nonempty)
    (hp : ∀ p∈J,1<p) (α : ℝ) : 0<variance J α := by
  unfold variance
  obtain ⟨p,hpJ⟩ := hJ
  apply Finset.sum_pos' (fun i _ => by positivity)
  refine ⟨p,hpJ,?_⟩
  have h := Real.log_pos (show (1:ℝ)<p by exact_mod_cast hp p hpJ)
  positivity

theorem mass_strictAnti (J : Finset ℕ) (hJ : J.Nonempty)
    (hp : ∀ p∈J,1<p) : StrictAnti (mass J) := by
  apply strictAnti_of_deriv_neg
  intro α
  rw [(mass_deriv J α).deriv]
  exact neg_neg_of_pos (variance_pos J hJ hp α)

theorem saddle_exists_unique (J : Finset ℕ) (hJ : J.Nonempty)
    (hp : ∀ p∈J,1<p) {a b x : ℝ} (hab : a≤b)
    (ha : x≤mass J a) (hb : mass J b≤x) :
    ∃! α : ℝ, α∈Icc a b ∧ mass J α=x := by
  have hcont : Continuous (mass J) :=
    continuous_iff_continuousAt.mpr (fun α => (mass_deriv J α).continuousAt)
  obtain ⟨α,hα,he⟩ := intermediate_value_Icc' hab hcont.continuousOn
    (show x∈Icc (mass J b) (mass J a) from ⟨hb,ha⟩)
  refine ⟨α,⟨hα,he⟩,?_⟩
  intro β hβ
  exact (mass_strictAnti J hJ hp).injective (hβ.2.trans he.symm)

/-- An exact second difference from two ordinary mean-value theorems.
The derivative is taken only of G, never of an unspecified remainder. -/
theorem second_difference {G G' G'' : ℝ→ℝ}
    (hG : ∀ x, HasDerivAt G (G' x) x)
    (hG' : ∀ x, HasDerivAt G' (G'' x) x)
    {x h k : ℝ} (hh : 0<h) (hk : 0<k) :
    ∃ z∈Ioo (x-h-k) x,
      G (x-h-k)-G (x-h)-G (x-k)+G x = h*k*G'' z := by
  let F := fun t : ℝ => G t-G (t-h)
  have hF (t : ℝ) : HasDerivAt F (G' t-G' (t-h)) t := by
    have h := (hG (t-h)).comp t ((hasDerivAt_id t).sub_const h)
    simpa [F] using (hG t).sub h
  have hFc : Continuous F := continuous_iff_continuousAt.mpr fun t => (hF t).continuousAt
  have hGc : Continuous G' := continuous_iff_continuousAt.mpr fun t => (hG' t).continuousAt
  obtain ⟨c,hc,he⟩ := exists_deriv_eq_slope F (show x-k<x by linarith)
    hFc.continuousOn (fun t _ => (hF t).differentiableAt.differentiableWithinAt)
  rw [(hF c).deriv] at he
  obtain ⟨z,hz,he'⟩ := exists_deriv_eq_slope G' (show c-h<c by linarith)
    hGc.continuousOn (fun t _ => (hG' t).differentiableAt.differentiableWithinAt)
  rw [(hG' z).deriv] at he'
  have hc1 := hc.1
  have hc2 := hc.2
  have hz1 := hz.1
  have hz2 := hz.2
  refine ⟨z,⟨by linarith,by linarith⟩,?_⟩
  have he1 := (eq_div_iff (by linarith : x-(x-k)≠0)).mp he
  have he2 := (eq_div_iff (by linarith : c-(c-h)≠0)).mp he'
  change (G' c-G' (c-h))*(x-(x-k)) = (G x-G (x-h))-(G (x-k)-G (x-k-h)) at he1
  rw [show x-(x-k)=k by ring] at he1
  rw [show c-(c-h)=h by ring] at he2
  rw [←he2] at he1
  rw [show x-h-k=x-k-h by ring]
  linarith [show G'' z*h*k=h*k*G'' z by ring]

end Factoring.Saddle

#print axioms Factoring.Saddle.mass_deriv
#print axioms Factoring.Saddle.variance_pos
#print axioms Factoring.Saddle.mass_strictAnti
#print axioms Factoring.Saddle.saddle_exists_unique
#print axioms Factoring.Saddle.second_difference
