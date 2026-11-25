import Mathlib.Data.Complex.Exponential
import Mathlib.Tactic.IntervalCases
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.Ring

/-!
# Exact budgets for the repaired randomized recursion

Copyright 2026 Jose Brox. Released under CC BY 4.0; see LICENSE.

The path bounds hold for every natural-number depth, not just a finite test
range.  The real theorems then bound any three-term exponential recurrence
that satisfies the displayed hypotheses.  A separate two-term estimate
handles the sequential-workspace budget.

This file does not formalize a factoring algorithm, smoothness estimates,
probability estimates, or the analytic contract in the manuscript.  In
particular, it does not identify the algorithm with the abstract recurrence.
The constants 91.4 and 19 are certified conditional budgets, not an
unconditional factoring theorem.
-/

open scoped BigOperators

namespace Factoring.Recursion

def decay : ℚ := 9 / 16
def tau : ℚ := 19 / 16
def g : ℚ := 43 / 8
def trials : ℚ := 18 + 1 / tau
def timeBudget : ℚ := 457 / 5
def descentCost : ℚ := 41 / 20
def spaceBudget : ℚ := 19

def m1 (r : ℕ) : ℚ :=
  ((∑ j ∈ Finset.range r, decay ^ j) + (r : ℚ) * decay ^ r) / 2

def m2 (r : ℕ) : ℚ := m1 r + decay ^ r

def fibre (r : ℕ) : ℚ :=
  ((∑ j ∈ Finset.range r, decay ^ j) + 2 * decay ^ r) / 2

theorem geometric_sum (r : ℕ) :
    (∑ j ∈ Finset.range r, decay ^ j) = (16 / 7 : ℚ) * (1 - decay ^ r) := by
  induction r with
  | zero => norm_num
  | succ r ih =>
    rw [Finset.sum_range_succ, ih, pow_succ]
    dsimp [decay]
    ring

theorem m1_difference (r : ℕ) :
    m1 (r + 1) - m1 r = decay ^ r * (25 - 7 * (r : ℚ)) / 32 := by
  dsimp [m1]
  simp only [Finset.sum_range_succ, pow_succ, Nat.cast_add, Nat.cast_one]
  dsimp [decay]
  ring

theorem m2_difference (r : ℕ) :
    m2 (r + 1) - m2 r = decay ^ r * (11 - 7 * (r : ℚ)) / 32 := by
  calc
    _ = (m1 (r + 1) - m1 r) + (decay ^ (r + 1) - decay ^ r) := by
      dsimp [m2]
      ring
    _ = _ := by
      rw [m1_difference, pow_succ]
      dsimp [decay]
      ring

theorem m1_decreases {r : ℕ} (hr : 4 ≤ r) : m1 (r + 1) ≤ m1 r := by
  have hr' : (4 : ℚ) ≤ r := by exact_mod_cast hr
  have hp : 0 ≤ decay ^ r := pow_nonneg (by norm_num [decay]) r
  have hc : 25 - 7 * (r : ℚ) ≤ 0 := by linarith
  have hd := m1_difference r
  have hm := mul_nonpos_of_nonneg_of_nonpos hp hc
  linarith

theorem m2_decreases {r : ℕ} (hr : 2 ≤ r) : m2 (r + 1) ≤ m2 r := by
  have hr' : (2 : ℚ) ≤ r := by exact_mod_cast hr
  have hp : 0 ≤ decay ^ r := pow_nonneg (by norm_num [decay]) r
  have hc : 11 - 7 * (r : ℚ) ≤ 0 := by linarith
  have hd := m2_difference r
  have hm := mul_nonpos_of_nonneg_of_nonpos hp hc
  linarith

/-- A universal maximum, proved by induction and the negative tail difference. -/
theorem m1_upper (r : ℕ) : m1 r ≤ (40261 / 32768 : ℚ) := by
  induction r with
  | zero => norm_num [m1]
  | succ r ih =>
    by_cases hr : r < 4
    · interval_cases r <;> norm_num [m1, decay, Finset.sum_range_succ]
    · exact le_trans (m1_decreases (by omega)) ih

theorem m1_attains : m1 4 = (40261 / 32768 : ℚ) := by
  norm_num [m1, decay, Finset.sum_range_succ]

theorem m2_upper (r : ℕ) : m2 r ≤ (181 / 128 : ℚ) := by
  induction r with
  | zero => norm_num [m2, m1]
  | succ r ih =>
    by_cases hr : r < 2
    · interval_cases r <;> norm_num [m2, m1, decay, Finset.sum_range_succ]
    · exact le_trans (m2_decreases (by omega)) ih

theorem m2_attains : m2 2 = (181 / 128 : ℚ) := by
  norm_num [m2, m1, decay, Finset.sum_range_succ]

theorem fibre_formula (r : ℕ) : fibre r = (8 / 7 : ℚ) - decay ^ r / 7 := by
  rw [fibre, geometric_sum]
  ring

theorem fibre_upper (r : ℕ) : fibre r ≤ (8 / 7 : ℚ) := by
  rw [fibre_formula]
  have hp : 0 ≤ decay ^ r := pow_nonneg (by norm_num [decay]) r
  linarith

/-- The old choice g = 3 fails the root conductor inequality. -/
theorem old_root_margin :
    ((3 : ℚ) - tau / 2) / 8 - tau / 2 = -75 / 256 := by
  norm_num [tau]

theorem repaired_root_margin :
    (g - tau / 2) / 8 - tau / 2 = (1 / 256 : ℚ) := by
  norm_num [g, tau]

/-- The algebraic AP margin holds uniformly over all path depths. -/
theorem algebraic_ap_margin (r : ℕ) :
    tau * m2 r + (17 / 2048 : ℚ) ≤ 27 / 16 := by
  have h := m2_upper r
  dsimp [tau]
  linarith

theorem rough_prefix_margin (r : ℕ) : tau * m1 r < (147 / 100 : ℚ) := by
  have h := m1_upper r
  dsimp [tau]
  linarith

theorem fibre_margin (r : ℕ) :
    g + tau + tau * fibre r + (9 / 112 : ℚ) ≤ 8 := by
  have h := fibre_upper r
  dsimp [g, tau]
  linarith

/-- Exact rational guards; these identities do not prove the analytic estimates. -/
theorem remaining_margins :
    (g - tau / 2) / 18 = (17 / 64 : ℚ) ∧
    (g - tau / 2) / 18 - 2 / 15 = (127 / 960 : ℚ) ∧
    4 - (2 / 3) * ((g - tau / 2) / 18) - 382 / 100 = (7 / 2400 : ℚ) ∧
    19 / 100 - (2 / 3) * ((g - tau / 2) / 18) - 1 / 100 = (7 / 2400 : ℚ) ∧
    7 - g = (13 / 8 : ℚ) ∧ 8 - g = (21 / 8 : ℚ) ∧
    83 / 1000 - (147 / 100) / (891 / 50) > (0 : ℚ) := by
  norm_num [g, tau]

theorem trial_coefficient : trials = (358 / 19 : ℚ) := by
  norm_num [trials, tau]

theorem root_cubic_certificate :
    2 * (timeBudget - trials) ^ 3 - timeBudget ^ 3 =
      (370059927 / 857375 : ℚ) := by
  norm_num [timeBudget, trials, tau]

theorem descent_cubic_certificate :
    64 * (timeBudget - trials - descentCost) ^ 3 - 19 * timeBudget ^ 3 =
      (6795396287504 / 857375 : ℚ) := by
  norm_num [timeBudget, trials, tau, descentCost]

section RealBounds

/-- Elementary cubic comparison; no numerical approximation to a cube root. -/
theorem lt_of_cube_lt {x y : ℝ} (hx : 0 ≤ x) (hy : 0 ≤ y)
    (hcube : x ^ 3 < y ^ 3) : x < y := by
  by_contra h
  have hxy : 0 ≤ x - y := sub_nonneg.mpr (le_of_not_gt h)
  have hp : 0 ≤ (x - y) * (x ^ 2 + x * y + y ^ 2) := by positivity
  nlinarith

/-- A generic strict contraction certificate in cubed form. -/
theorem cubic_budget {A C d r : ℝ} (hC : 0 < C) (hAC : A < C)
    (hr : 0 ≤ r) (hr3 : r ^ 3 ≤ d)
    (hbudget : C ^ 3 * d < (C - A) ^ 3) : A + C * r < C := by
  have hcube : (C * r) ^ 3 < (C - A) ^ 3 := by
    calc
      _ = C ^ 3 * r ^ 3 := by ring
      _ ≤ C ^ 3 * d := mul_le_mul_of_nonneg_left hr3 (by positivity)
      _ < _ := hbudget
  have h := lt_of_cube_lt (by positivity) (by linarith) hcube
  linarith

/-- The root branch leaves at least 0.01 of the exponent coefficient free. -/
theorem root_budget {r : ℝ} (hr : 0 ≤ r) (hr3 : r ^ 3 ≤ (1 / 2 : ℝ)) :
    (trials : ℝ) + (timeBudget : ℝ) * r + 1 / 100 < timeBudget := by
  have h := cubic_budget (A := (trials : ℝ) + 1 / 100)
    (C := (timeBudget : ℝ)) (d := (1 / 2 : ℝ))
    (by norm_num [timeBudget])
    (by norm_num [trials, tau, timeBudget]) hr hr3
    (by norm_num [trials, tau, timeBudget])
  linarith

theorem descent_budget {r : ℝ} (hr : 0 ≤ r) (hr3 : r ^ 3 ≤ (19 / 64 : ℝ)) :
    (trials : ℝ) + descentCost + (timeBudget : ℝ) * r + 1 / 100 < timeBudget := by
  have h := cubic_budget (A := (trials : ℝ) + descentCost + 1 / 100)
    (C := (timeBudget : ℝ)) (d := (19 / 64 : ℝ))
    (by norm_num [timeBudget])
    (by norm_num [trials, tau, descentCost, timeBudget]) hr hr3
    (by norm_num [trials, tau, descentCost, timeBudget])
  linarith

/-- Strong induction for an actual sum of three exponential cost terms.
The guard `3 ≤ exp (ε * w n)` absorbs addition of the terms.  The theorem
makes no assertion that a particular factoring algorithm meets its hypotheses.
The recurrence is required only above an arbitrary natural threshold.  The
desired bound on the finite initial range is a separate explicit hypothesis;
no asymptotic-to-exact transfer or automatic initial-range absorption is claimed. -/
theorem exponential_recurrence_bound
    (T w : ℕ → ℝ) (left right : ℕ → ℕ) (n₀ : ℕ) (A K linear C r s ε : ℝ)
    (hC : 0 ≤ C) (hw : ∀ n, 0 ≤ w n)
    (hleft : ∀ n, n₀ < n → left n < n)
    (hright : ∀ n, n₀ < n → right n < n)
    (hleftScale : ∀ n, n₀ < n → w (left n) ≤ r * w n)
    (hrightScale : ∀ n, n₀ < n → w (right n) ≤ s * w n)
    (hrootBudget : A + C * r + ε ≤ C)
    (hdescentBudget : A + K + C * s + ε ≤ C)
    (hlinearBudget : linear + ε ≤ C)
    (hadd : ∀ n, n₀ < n → 3 ≤ Real.exp (ε * w n))
    (hbase : ∀ n, n ≤ n₀ → T n ≤ Real.exp (C * w n))
    (hstep : ∀ n, n₀ < n →
      T n ≤ Real.exp (linear * w n) + Real.exp (A * w n) * T (left n) +
        Real.exp ((A + K) * w n) * T (right n)) :
    ∀ n, T n ≤ Real.exp (C * w n) := by
  intro n
  induction n using Nat.strong_induction_on with
  | h n ih =>
    by_cases hn : n ≤ n₀
    · exact hbase n hn
    have hnpos : n₀ < n := by omega
    have hl : Real.exp (A * w n) * T (left n) ≤ Real.exp ((C - ε) * w n) := by
      calc
        _ ≤ Real.exp (A * w n) * Real.exp (C * w (left n)) :=
          mul_le_mul_of_nonneg_left (ih _ (hleft n hnpos)) (Real.exp_nonneg _)
        _ = Real.exp (A * w n + C * w (left n)) := (Real.exp_add _ _).symm
        _ ≤ _ := by
          apply Real.exp_le_exp.mpr
          have hs := mul_le_mul_of_nonneg_left (hleftScale n hnpos) hC
          have hb := mul_le_mul_of_nonneg_right hrootBudget (hw n)
          nlinarith
    have hr : Real.exp ((A + K) * w n) * T (right n) ≤
        Real.exp ((C - ε) * w n) := by
      calc
        _ ≤ Real.exp ((A + K) * w n) * Real.exp (C * w (right n)) :=
          mul_le_mul_of_nonneg_left (ih _ (hright n hnpos)) (Real.exp_nonneg _)
        _ = Real.exp ((A + K) * w n + C * w (right n)) := (Real.exp_add _ _).symm
        _ ≤ _ := by
          apply Real.exp_le_exp.mpr
          have hs := mul_le_mul_of_nonneg_left (hrightScale n hnpos) hC
          have hb := mul_le_mul_of_nonneg_right hdescentBudget (hw n)
          nlinarith
    have hb : Real.exp (linear * w n) ≤ Real.exp ((C - ε) * w n) := by
      apply Real.exp_le_exp.mpr
      exact mul_le_mul_of_nonneg_right (by linarith) (hw n)
    calc
      T n ≤ 3 * Real.exp ((C - ε) * w n) := by
        linarith [hstep n hnpos]
      _ ≤ Real.exp (ε * w n) * Real.exp ((C - ε) * w n) :=
        mul_le_mul_of_nonneg_right (hadd n hnpos) (Real.exp_nonneg _)
      _ = Real.exp (C * w n) := by
        rw [← Real.exp_add]
        congr 1
        ring

/-- The repaired time coefficient, specialized to the manuscript's two
recursive size powers.  All scale and cost assumptions remain explicit. -/
theorem repaired_time_bound
    (T w : ℕ → ℝ) (left right : ℕ → ℕ) (n₀ : ℕ) (r s : ℝ)
    (hr : 0 ≤ r) (hr3 : r ^ 3 ≤ (1 / 2 : ℝ))
    (hs : 0 ≤ s) (hs3 : s ^ 3 ≤ (19 / 64 : ℝ))
    (hw : ∀ n, 0 ≤ w n)
    (hleft : ∀ n, n₀ < n → left n < n)
    (hright : ∀ n, n₀ < n → right n < n)
    (hleftScale : ∀ n, n₀ < n → w (left n) ≤ r * w n)
    (hrightScale : ∀ n, n₀ < n → w (right n) ≤ s * w n)
    (hadd : ∀ n, n₀ < n → 3 ≤ Real.exp ((1 / 100 : ℝ) * w n))
    (hbase : ∀ n, n ≤ n₀ → T n ≤ Real.exp ((timeBudget : ℝ) * w n))
    (hstep : ∀ n, n₀ < n →
      T n ≤ Real.exp (38 * w n) + Real.exp ((trials : ℝ) * w n) * T (left n) +
        Real.exp (((trials : ℝ) + descentCost) * w n) * T (right n)) :
    ∀ n, T n ≤ Real.exp ((timeBudget : ℝ) * w n) := by
  exact exponential_recurrence_bound T w left right n₀ trials descentCost 38 timeBudget r s
    (1 / 100) (by norm_num [timeBudget]) hw hleft hright hleftScale hrightScale
    (le_of_lt (root_budget hr hr3)) (le_of_lt (descent_budget hs hs3))
    (by norm_num [timeBudget]) hadd hbase hstep

/-- One step of the sequential-workspace estimate: the local allocation has
coefficient 18.5, the child has coefficient 19, and the input scale shrinks. -/
theorem workspace_step {x r : ℝ} (hx : 0 ≤ x) (hr : 0 ≤ r)
    (hr3 : r ^ 3 ≤ (1 / 2 : ℝ)) (hadd : 2 ≤ Real.exp (x / 4)) :
    Real.exp ((37 / 2 : ℝ) * x) + Real.exp ((spaceBudget : ℝ) * r * x) ≤
      Real.exp ((spaceBudget : ℝ) * x) := by
  have hc : (spaceBudget : ℝ) * r < 75 / 4 := by
    have h := cubic_budget (A := (1 / 4 : ℝ)) (C := (spaceBudget : ℝ))
      (d := (1 / 2 : ℝ)) (by norm_num [spaceBudget])
      (by norm_num [spaceBudget]) hr hr3 (by norm_num [spaceBudget])
    norm_num [spaceBudget] at h ⊢
    linarith
  have hlocal : Real.exp ((37 / 2 : ℝ) * x) ≤ Real.exp ((75 / 4 : ℝ) * x) := by
    apply Real.exp_le_exp.mpr
    exact mul_le_mul_of_nonneg_right (by norm_num) hx
  have hchild : Real.exp ((spaceBudget : ℝ) * r * x) ≤
      Real.exp ((75 / 4 : ℝ) * x) :=
    Real.exp_le_exp.mpr (mul_le_mul_of_nonneg_right (le_of_lt hc) hx)
  calc
    _ ≤ 2 * Real.exp ((75 / 4 : ℝ) * x) := by linarith
    _ ≤ Real.exp (x / 4) * Real.exp ((75 / 4 : ℝ) * x) :=
      mul_le_mul_of_nonneg_right hadd (Real.exp_nonneg _)
    _ = _ := by
      rw [← Real.exp_add]
      congr 1
      norm_num [spaceBudget]
      ring

/-- Sequential stack allocation under an explicit shrinking-child bound. -/
theorem workspace_bound
    (S w : ℕ → ℝ) (child : ℕ → ℕ) (n₀ : ℕ) (r : ℝ)
    (hr : 0 ≤ r) (hr3 : r ^ 3 ≤ (1 / 2 : ℝ))
    (hw : ∀ n, 0 ≤ w n)
    (hchild : ∀ n, n₀ < n → child n < n)
    (hscale : ∀ n, n₀ < n → w (child n) ≤ r * w n)
    (hadd : ∀ n, n₀ < n → 2 ≤ Real.exp (w n / 4))
    (hbase : ∀ n, n ≤ n₀ → S n ≤ Real.exp ((spaceBudget : ℝ) * w n))
    (hstep : ∀ n, n₀ < n → S n ≤ Real.exp ((37 / 2 : ℝ) * w n) + S (child n)) :
    ∀ n, S n ≤ Real.exp ((spaceBudget : ℝ) * w n) := by
  intro n
  induction n using Nat.strong_induction_on with
  | h n ih =>
    by_cases hn : n ≤ n₀
    · exact hbase n hn
    have hnpos : n₀ < n := by omega
    have hc : S (child n) ≤ Real.exp ((spaceBudget : ℝ) * r * w n) := by
      calc
        _ ≤ Real.exp ((spaceBudget : ℝ) * w (child n)) := ih _ (hchild n hnpos)
        _ ≤ _ := by
          apply Real.exp_le_exp.mpr
          have hs := mul_le_mul_of_nonneg_left (hscale n hnpos)
            (show (0 : ℝ) ≤ spaceBudget by norm_num [spaceBudget])
          nlinarith
    calc
      S n ≤ Real.exp ((37 / 2 : ℝ) * w n) + S (child n) := hstep n hnpos
      _ ≤ Real.exp ((37 / 2 : ℝ) * w n) +
          Real.exp ((spaceBudget : ℝ) * r * w n) := add_le_add_left hc _
      _ ≤ Real.exp ((spaceBudget : ℝ) * w n) :=
        workspace_step (hw n) hr hr3 (hadd n hnpos)

end RealBounds

end Factoring.Recursion
