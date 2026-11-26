import Factoring.EulerDecay
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Bounds

/-! Actual finite Gaussian central-tail bound, with the Euler factors
written in real and imaginary coordinates. The PNT estimate for the
second moment is not assumed to follow from this finite inequality. -/
namespace Factoring.SaddleDecay
open scoped BigOperators

noncomputable def phase (r x : ℝ) : ℂ :=
  ⟨r*Real.cos x,r*Real.sin x⟩

theorem phase_normSq (r x : ℝ) : Complex.normSq (phase r x)=r^2 := by
  rw [phase,Complex.normSq_mk]
  nlinarith [congrArg (fun z : ℝ => r^2*z) (Real.sin_sq_add_cos_sq x)]

theorem phase_re_le (r x : ℝ) (hr : 0≤r) : (phase r x).re≤r := by
  change r*Real.cos x≤r
  exact mul_le_of_le_one_right hr (Real.cos_le_one x)

/-- On the central interval, the loss of each Euler factor is
quantitatively quadratic in its angle. -/
theorem central_product {I : Type*} (s : Finset I) (r x : I→ℝ)
    (h : ∀ i∈s,0≤r i ∧ r i≤1 ∧ |x i|≤Real.pi) :
    Complex.normSq (∏ i∈s, (phase (r i) (x i)+1)) ≤
      (∏ i∈s, (1+r i)^2) *
        Real.exp (-(∑ i∈s,r i*(x i)^2)/Real.pi^2) := by
  have hdec := Factoring.EulerDecay.product_decay s (fun i=>phase (r i) (x i)) r (by
    intro i hi
    obtain ⟨h0,h1,_⟩ := h i hi
    exact ⟨h0,h1,(phase_normSq _ _).le,phase_re_le _ _ h0⟩)
  apply hdec.trans
  apply mul_le_mul_of_nonneg_left _ (Finset.prod_nonneg fun i _=>sq_nonneg _)
  apply Real.exp_le_exp.mpr
  have he : -(∑ i∈s,r i*(x i)^2)/Real.pi^2 =
      ∑ i∈s, -(r i*(x i)^2)/Real.pi^2 := by
    rw [←Finset.sum_neg_distrib,Finset.sum_div]
  rw [he]
  apply Finset.sum_le_sum
  intro i hi
  obtain ⟨hr,_,hx⟩ := h i hi
  have hc := mul_le_mul_of_nonneg_left (Real.cos_le_one_sub_mul_cos_sq hx) hr
  change -(r i-r i*Real.cos (x i))/2≤-(r i*(x i)^2)/Real.pi^2
  have hpi : Real.pi^2≠0 := by positivity
  field_simp [hpi] at hc ⊢
  nlinarith [Real.pi_pos]

/-- The actual dyadic-prime logarithmic variance weight. The hypothesis
on t is the central angle bound, as used in the saddle integral. -/
theorem central_log_product (J : Finset ℕ) (r : ℕ→ℝ) (t : ℝ)
    (hr : ∀ p∈J,0≤r p ∧ r p≤1)
    (ht : ∀ p∈J, |t*Real.log p|≤Real.pi) :
    Complex.normSq (∏ p∈J,(phase (r p) (t*Real.log p)+1))≤
      (∏ p∈J,(1+r p)^2) *
        Real.exp (-(t^2*(∑ p∈J,r p*(Real.log p)^2))/Real.pi^2) := by
  have h := central_product J r (fun p=>t*Real.log p)
    (fun p hp=>⟨(hr p hp).1,(hr p hp).2,ht p hp⟩)
  convert h using 2
  rw [Finset.mul_sum]
  apply Finset.sum_congr rfl
  intro p _
  ring

end Factoring.SaddleDecay

#print axioms Factoring.SaddleDecay.phase_normSq
#print axioms Factoring.SaddleDecay.phase_re_le
#print axioms Factoring.SaddleDecay.central_product
#print axioms Factoring.SaddleDecay.central_log_product
