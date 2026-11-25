import Mathlib.Data.Real.Archimedean
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring

/-!
# Exact exponents for the deterministic factoring schedule

This file formalizes the affine arithmetic in
verification/verify_deterministic_parameters.py and the parameter section of
manuscripts/deterministic_factoring/body.tex.

The variables are real, so the results also apply to the manuscript's rational
choices.  ScheduleValid lists exactly the 19 strict inequalities checked by
the Python program.  The four additional manuscript comparisons are proved
separately.  An explicit real choice handles every positive epsilon, and
rational density supplies the manuscript's admissible rational parameter.

These are parameter theorems, not a formalization of the factoring algorithm,
its analytic inputs, its running time, or an asymptotic transfer principle.
The final height-budget lemma is a limitation of the stated affine constraints,
not a lower bound for integer factoring.
-/

noncomputable section

namespace Factoring.Deterministic

def a : ℝ := 1 / 3
def t (δ : ℝ) : ℝ := 1 / 3 + δ
def k (δ : ℝ) : ℝ := 1 / 3 + 2 * δ
def v (δ : ℝ) : ℝ := 1 / 3 + (5 / 2) * δ
def b (δ : ℝ) : ℝ := 1 / 3 + 3 * δ
def eta (δ : ℝ) : ℝ := 1 / 3 + 4 * δ
def r (δ : ℝ) : ℝ := 1 / 3 + 5 * δ
def c (δ : ℝ) : ℝ := 1 / 3 + 6 * δ
def h (δ : ℝ) : ℝ := 2 / 3 + 8 * δ
def m0 : ℝ := 2 / 3
def g (δ : ℝ) : ℝ := 1 - b δ + δ

/-- The 19 inequalities, in the order used by the exact Python checker.
The checker calls the exponent eta by the letter j. -/
structure ScheduleValid (δ : ℝ) : Prop where
  a_lt_t : a < t δ
  t_lt_k : t δ < k δ
  k_lt_v : k δ < v δ
  v_lt_b : v δ < b δ
  b_lt_eta : b δ < eta δ
  eta_lt_r : eta δ < r δ
  r_lt_c : r δ < c δ
  one_sub_a_lt_h : 1 - a < h δ
  a_add_c_lt_h : a + c δ < h δ
  m0_sub_b_lt_r : m0 - b δ < r δ
  m0_sub_v_lt_b : m0 - v δ < b δ
  m0_sub_b_lt_b : m0 - b δ < b δ
  two_c_lt_h_add_b : 2 * c δ < h δ + b δ
  two_h_add_r_lt_three : 2 * h δ + r δ < 3
  g_lt_h : g δ < h δ
  eta_add_delta_lt_c : eta δ + δ < c δ
  h_lt_one : h δ < 1
  r_lt_one : r δ < 1
  b_lt_one_sub_b : b δ < 1 - b δ

/-- Universal interval certification, rather than a finite sample of deltas. -/
theorem schedule_valid {δ : ℝ} (hδ : 0 < δ) (hδmax : δ ≤ 1 / 100) :
    ScheduleValid δ := by
  constructor <;>
    dsimp [a, t, k, v, b, eta, r, c, h, m0, g] <;>
    linarith

theorem m0_eq_one_sub_a : m0 = 1 - a := by
  norm_num [m0, a]

/-- The smoothness exponent is exactly the difference of the height and
smoothness-bound exponents. -/
theorem h_sub_b_eq_r (δ : ℝ) : h δ - b δ = r δ := by
  dsimp [h, b, r]
  ring

theorem spectral_guard_identity (δ : ℝ) :
    2 * h δ + r δ = 5 / 3 + 21 * δ := by
  dsimp [h, r]
  ring

theorem g_explicit (δ : ℝ) : g δ = 2 / 3 - 2 * δ := by
  dsimp [g, b]
  ring

/-- Comparisons printed in the manuscript but not listed separately among
the Python checker's 19 gates.  The remaining printed comparisons follow
directly from ScheduleValid and m0_eq_one_sub_a. -/
theorem manuscript_auxiliary_gates {δ : ℝ}
    (hδ : 0 < δ) (hδmax : δ ≤ 1 / 100) :
    c δ < m0 ∧ h δ < 3 / 4 ∧ m0 - b δ < k δ ∧ 1 - b δ < g δ := by
  refine ⟨?_, ?_, ?_, ?_⟩ <;>
    dsimp [c, m0, h, b, k, g] <;>
    linarith

/-- A fixed positive epsilon gets a fixed admissible delta, with room to
spare in the height exponent. -/
def deltaFor (ε : ℝ) : ℝ := min (1 / 100) (ε / 16)

theorem deltaFor_pos {ε : ℝ} (hε : 0 < ε) : 0 < deltaFor ε := by
  unfold deltaFor
  exact lt_min (by norm_num) (by linarith)

theorem deltaFor_le (ε : ℝ) : deltaFor ε ≤ 1 / 100 := by
  exact min_le_left _ _

theorem chosen_height_bound (ε : ℝ) :
    h (deltaFor ε) ≤ 2 / 3 + ε / 2 := by
  have hmin := min_le_right (1 / 100 : ℝ) (ε / 16)
  dsimp [h, deltaFor]
  linarith

theorem epsilon_schedule {ε : ℝ} (hε : 0 < ε) :
    0 < deltaFor ε ∧
      deltaFor ε ≤ 1 / 100 ∧
      ScheduleValid (deltaFor ε) ∧
      h (deltaFor ε) < 2 / 3 + ε := by
  have hpos := deltaFor_pos hε
  have hcap := deltaFor_le ε
  refine ⟨hpos, hcap, schedule_valid hpos hcap, ?_⟩
  have hheight := chosen_height_bound ε
  linarith

/-- The weak inequality requested when choosing the schedule is a direct
consequence of the stronger strict bound. -/
theorem exists_epsilon_schedule {ε : ℝ} (hε : 0 < ε) :
    ∃ δ : ℝ, 0 < δ ∧ δ ≤ 1 / 100 ∧ ScheduleValid δ ∧ h δ ≤ 2 / 3 + ε := by
  obtain ⟨hpos, hcap, hvalid, hheight⟩ := epsilon_schedule hε
  exact ⟨deltaFor ε, hpos, hcap, hvalid, le_of_lt hheight⟩

/-- The manuscript requires a fixed rational parameter.  Rational density
supplies one even when epsilon itself is real.  This is an existence result,
not an algorithm for accessing an arbitrary real input. -/
theorem exists_rational_epsilon_schedule {ε : ℝ} (hε : 0 < ε) :
    ∃ δ : ℚ, 0 < (δ : ℝ) ∧ (δ : ℝ) ≤ 1 / 100 ∧
      ScheduleValid (δ : ℝ) ∧ h (δ : ℝ) < 2 / 3 + ε := by
  obtain ⟨δ, hpos, hlt⟩ := exists_rat_btwn (deltaFor_pos hε)
  have hcap : (δ : ℝ) ≤ 1 / 100 :=
    le_trans (le_of_lt hlt) (deltaFor_le ε)
  refine ⟨δ, hpos, hcap, schedule_valid hpos hcap, ?_⟩
  have hheight := chosen_height_bound ε
  dsimp [h] at hheight ⊢
  linarith

/-- The elementary minimax balance used in the discussion of this
construction's barrier.  No analytic or algorithmic conclusion is imported. -/
theorem power_budget_minimax (degree : ℝ) :
    (2 : ℝ) / 3 ≤ max (1 - degree) (2 * degree) := by
  have hbase := le_max_left (1 - degree) (2 * degree)
  have hcoeff := le_max_right (1 - degree) (2 * degree)
  linarith

theorem power_budget_minimax_attained :
    max (1 - a) (2 * a) = (2 : ℝ) / 3 := by
  norm_num [a]

/-- A positive separation between evaluation and degree exponents forces
a strict height excess.  The hypotheses are explicit affine constraints. -/
theorem height_budget_strict {degree evaluation height : ℝ}
    (hsep : degree < evaluation)
    (hbase : 1 - degree ≤ height)
    (hcoeff : degree + evaluation ≤ height) :
    (2 : ℝ) / 3 < height := by
  linarith

/-- The same argument gives an exact margin for any imposed separation. -/
theorem height_budget_margin {degree evaluation height gap : ℝ}
    (hsep : degree + gap ≤ evaluation)
    (hbase : 1 - degree ≤ height)
    (hcoeff : degree + evaluation ≤ height) :
    (2 + gap) / 3 ≤ height := by
  linarith

end Factoring.Deterministic
