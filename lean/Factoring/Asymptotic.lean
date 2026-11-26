import Factoring.Deterministic
import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Tactic.Positivity

/-! Exact real-power comparisons used to transfer the deterministic and
randomized budget exponents. Cost estimates for the arithmetic/analytic
algorithms remain hypotheses, not proved by this file. -/
namespace Factoring.Asymptotic

open Factoring.Deterministic

/-- Elementary logarithm absorption, valid already for L ≥ 1. -/
theorem log_absorb {L δ : ℝ} (hL : 1 ≤ L) (hδ : 0 < δ) :
    Real.log L ≤ L^δ/δ := by
  have hpos : 0 < L := by linarith
  have h := Real.log_le_sub_one_of_pos (Real.rpow_pos_of_pos hpos δ)
  rw [Real.log_rpow hpos] at h
  apply (le_div_iff₀ hδ).mpr
  linarith

theorem log_power_absorb {L δ x : ℝ} (hL : 1 ≤ L) (hδ : 0 < δ) :
    L^x * Real.log L ≤ L^(x+δ)/δ := by
  calc
    _ ≤ L^x * (L^δ/δ) := mul_le_mul_of_nonneg_left (log_absorb hL hδ) (by positivity)
    _ = _ := by rw [Real.rpow_add (by linarith : 0<L)]; ring

/-- The output-length exponent of the saturation multiplier is below the
height budget. In particular the log-log factor is absorbed rigorously. -/
theorem saturation_scale {L δ : ℝ} (hL : 1 ≤ L) (hδ : 0 < δ)
    (hδmax : δ ≤ 1/100) :
    L^(1-b δ)*Real.log L ≤ L^(h δ)/δ := by
  apply (log_power_absorb (x := 1-b δ) hL hδ).trans
  apply div_le_div_of_nonneg_right _ hδ.le
  exact Real.rpow_le_rpow_of_exponent_le hL (le_of_lt (schedule_valid hδ hδmax).g_lt_h)

/-- Even the original splitter's sqrt(L) log L factor is below the
new deterministic height budget. -/
theorem original_splitter_scale {L δ : ℝ} (hL : 1 ≤ L) (hδ : 0 < δ) :
    L^(1/2 : ℝ)*Real.log L ≤ 6*L^(h δ) := by
  have ht := log_power_absorb (L := L) (δ := (1:ℝ)/6) (x := 1/2) hL (by norm_num)
  have he : (1:ℝ)/2+1/6=2/3 := by norm_num
  rw [he] at ht
  have hh : (2:ℝ)/3 ≤ h δ := by unfold h; linarith
  have hr := Real.rpow_le_rpow_of_exponent_le hL hh
  linarith

theorem chosen_scale {L ε : ℝ} (hL : 1 ≤ L) (hε : 0 < ε) :
    L^(h (deltaFor ε)) ≤ L^(2/3+ε : ℝ) :=
  Real.rpow_le_rpow_of_exponent_le hL (by
    have h := chosen_height_bound ε
    linarith)

/-- Finite, explicit composition inequality for the three deterministic
cost factors. This is an exponent-budget theorem, not the algorithm. -/
theorem deterministic_cost_transfer {L δ ε C D F : ℝ}
    (hL : 1 ≤ L) (hδ : 0 < δ) (hδmax : δ ≤ 1/100)
    (hheight : h δ ≤ 2/3+ε) (hC : 0 ≤ C) (hD : 0 ≤ D) (hF : 0 ≤ F) :
    Real.exp (C*L^(h δ)) * Real.exp (D*(L^(1-b δ)*Real.log L)) *
      Real.exp (F*(L^(1/2 : ℝ)*Real.log L)) ≤
      Real.exp ((C+D/δ+6*F)*L^(2/3+ε : ℝ)) := by
  rw [← Real.exp_add, ← Real.exp_add]
  apply Real.exp_le_exp.mpr
  have hs := mul_le_mul_of_nonneg_left (saturation_scale hL hδ hδmax) hD
  have hf := mul_le_mul_of_nonneg_left (original_splitter_scale hL hδ) hF
  have hh := Real.rpow_le_rpow_of_exponent_le hL hheight
  have hc : 0 ≤ C+D/δ+6*F := by positivity
  have ht := mul_le_mul_of_nonneg_left hh hc
  have he : D*(L^(h δ)/δ) = D/δ*L^(h δ) := by ring
  rw [he] at hs
  nlinarith

/-- L[1/3] exponent scale, taking L = log N. -/
noncomputable def scale (L : ℝ) : ℝ :=
  L^(1/3 : ℝ) * (Real.log L)^(2/3 : ℝ)

/-- Shrinking log N by a factor d ≤ 1 contracts the L[1/3] scale by at
least d^(1/3), without any asymptotic approximation. -/
theorem scale_contract {L L' d : ℝ} (hL' : 1 ≤ L') (hL : 1 ≤ L)
    (hd0 : 0 ≤ d) (hd1 : d ≤ 1) (hchild : L' ≤ d*L) :
    scale L' ≤ d^(1/3 : ℝ)*scale L := by
  have hle : L' ≤ L := hchild.trans (by nlinarith)
  have hp : L'^(1/3 : ℝ) ≤ (d*L)^(1/3 : ℝ) :=
    Real.rpow_le_rpow (by linarith) hchild (by norm_num)
  have hl : (Real.log L')^(2/3 : ℝ) ≤ (Real.log L)^(2/3 : ℝ) :=
    Real.rpow_le_rpow (Real.log_nonneg hL') (Real.log_le_log (by linarith) hle) (by norm_num)
  unfold scale
  rw [← mul_assoc, ← Real.mul_rpow hd0 (by linarith : 0≤L)]
  exact mul_le_mul hp hl (by positivity) (by positivity)

theorem contraction_cube {d : ℝ} (hd : 0 ≤ d) :
    (d^(1/3 : ℝ))^3 = d := by
  rw [← Real.rpow_natCast, ← Real.rpow_mul hd]
  norm_num

end Factoring.Asymptotic
