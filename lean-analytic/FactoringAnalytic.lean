import PrimeNumberTheoremAnd.StrongPNT

/-! Reuse of the pinned PNT+ theorem and mathlib's prime-power correction.
These are mathematical asymptotic statements, not effective algorithms
for computing the unspecified constants. -/
open Filter Asymptotics Topology
open scoped BigOperators

namespace Factoring.Analytic

theorem sqrt_error_scale {c : ℝ} (hc : 0 < c) :
    Real.sqrt =O[atTop] (fun x : ℝ =>
      x * Real.exp (-c * (Real.log x) ^ ((1 : ℝ) / 2))) := by
  apply IsBigO.of_bound 1
  filter_upwards [eventually_ge_atTop (Real.exp ((2*c)^2))] with x hx
  have hx0 : 0 < x := (Real.exp_pos _).trans_le hx
  have hl := Real.log_le_log (Real.exp_pos _) hx
  rw [Real.log_exp] at hl
  have hl0 : 0 ≤ Real.log x := (sq_nonneg (2*c)).trans hl
  have hs0 := Real.sqrt_nonneg (Real.log x)
  have hs2 := Real.sq_sqrt hl0
  have hs : 2*c ≤ Real.sqrt (Real.log x) := by
    by_contra! hh
    have h := mul_pos (sub_pos.mpr hh)
      (show 0 < 2*c + Real.sqrt (Real.log x) by positivity)
    nlinarith
  have he : c * Real.sqrt (Real.log x) ≤ Real.log x / 2 := by
    have h := mul_le_mul_of_nonneg_right hs hs0
    nlinarith
  rw [← Real.sqrt_eq_rpow, one_mul, Real.norm_of_nonneg (Real.sqrt_nonneg x),
    Real.norm_of_nonneg (mul_nonneg hx0.le (Real.exp_pos _).le)]
  calc
    Real.sqrt x = Real.exp (Real.log x/2) := by
      rw [Real.sqrt_eq_rpow, Real.rpow_def_of_pos hx0]
      congr 1
      ring
    _ ≤ Real.exp (Real.log x - c * Real.sqrt (Real.log x)) :=
      Real.exp_le_exp.mpr (by linarith)
    _ = _ := by
      rw [sub_eq_add_neg, Real.exp_add, Real.exp_log hx0, neg_mul]

/-- The precise classical PNT input for the prime sums in the deterministic
manuscript: the Chebyshev theta function, not the prime-power psi sum. -/
theorem theta_strongPNT : ∃ c > (0 : ℝ),
    (Chebyshev.theta - id) =O[atTop] (fun x : ℝ =>
      x * Real.exp (-c * (Real.log x) ^ ((1 : ℝ) / 2))) := by
  obtain ⟨c,hc,hp⟩ := StrongPNT
  refine ⟨c,hc,?_⟩
  have hd := Chebyshev.isBigO_psi_sub_theta_sqrt.trans (sqrt_error_scale hc)
  convert hp.sub hd using 1
  ext x
  simp only [Pi.sub_apply, id_eq, ChebyshevPsi]
  ring

/-- The strong PNT implies an eventual relative error bound of any given
positive size. The constants here are existential, as in the upstream PNT. -/
theorem theta_relative_error (ε : ℝ) (hε : 0 < ε) :
    ∀ᶠ x : ℝ in atTop, |Chebyshev.theta x - x| ≤ ε*x := by
  obtain ⟨c,hc,hp⟩ := theta_strongPNT
  obtain ⟨C,hC⟩ := isBigO_iff.mp hp
  let t := max 1 (Real.log ((|C|+1)/ε)/c)
  have ht : 0 < t := (show (0:ℝ)<1 by norm_num).trans_le (le_max_left _ _)
  filter_upwards [hC, eventually_ge_atTop (Real.exp (t^2))] with x hx hxt
  have hx0 : 0 < x := (Real.exp_pos _).trans_le hxt
  have hl := Real.log_le_log (Real.exp_pos _) hxt
  rw [Real.log_exp] at hl
  have hnonneg := (sq_nonneg t).trans hl
  have hs : t ≤ Real.sqrt (Real.log x) := by
    by_contra! hh
    have h := mul_pos (sub_pos.mpr hh) (add_pos_of_pos_of_nonneg ht (Real.sqrt_nonneg _))
    nlinarith [Real.sq_sqrt hnonneg]
  have hlog : Real.log ((|C|+1)/ε) ≤ c*Real.sqrt (Real.log x) :=
    ((div_le_iff₀ hc).mp (le_max_right 1 (Real.log ((|C|+1)/ε)/c))).trans
      (by have hh := mul_le_mul_of_nonneg_left hs hc.le; linarith)
  have hratio : 0 < (|C|+1)/ε := by positivity
  have hdecay : Real.exp (-c * Real.sqrt (Real.log x)) ≤ ε/(|C|+1) := by
    calc
      _ ≤ Real.exp (-Real.log ((|C|+1)/ε)) := Real.exp_le_exp.mpr (by linarith)
      _ = _ := by rw [Real.exp_neg, Real.exp_log hratio, inv_div]
  simp only [Pi.sub_apply, id_eq, Real.norm_eq_abs] at hx
  rw [← Real.sqrt_eq_rpow, abs_of_nonneg (mul_nonneg hx0.le (Real.exp_pos _).le)] at hx
  have he : |C|*Real.exp (-c*Real.sqrt (Real.log x)) ≤ ε := by
    have hb := mul_le_mul_of_nonneg_left hdecay (abs_nonneg C)
    have hf : |C|*(ε/(|C|+1)) ≤ ε := by
      rw [mul_comm, ← div_mul_eq_mul_div]
      apply (div_le_iff₀ (by positivity : 0 < |C|+1)).mpr
      nlinarith
    exact hb.trans hf
  calc
    _ ≤ C*(x*Real.exp (-c*Real.sqrt (Real.log x))) := hx
    _ ≤ |C|*(x*Real.exp (-c*Real.sqrt (Real.log x))) :=
      mul_le_mul_of_nonneg_right (le_abs_self C) (by positivity)
    _ = (|C|*Real.exp (-c*Real.sqrt (Real.log x)))*x := by ring
    _ ≤ ε*x := mul_le_mul_of_nonneg_right he hx0.le

end Factoring.Analytic

#print axioms StrongPNT
#print axioms Factoring.Analytic.sqrt_error_scale
#print axioms Factoring.Analytic.theta_strongPNT
#print axioms Factoring.Analytic.theta_relative_error
