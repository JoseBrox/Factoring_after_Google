import OAI.NumberTheory.DirichletL.Nonvanishing

/-! Exact mathlib endpoints and the zero-location consequence used in
the near-one conductor deletion. No new L-function definition, no
comparator challenge import, no extra analytic axiom. -/
namespace Factoring.QRH

open scoped DirichletCharacter

theorem dirichlet_nonzero {q : ℕ} [NeZero q]
    (χ : DirichletCharacter ℂ q) {s : ℂ}
    (hs : (7 / 8 : ℝ) < s.re) (hpole : ¬ (χ = 1 ∧ s = 1)) :
    DirichletCharacter.LFunction χ s ≠ 0 :=
  OAI.DirichletCharacter.LFunction_ne_zero_of_seven_eighths_lt_re χ hs hpole

theorem zeta_nonzero {s : ℂ} (hs : (7 / 8 : ℝ) < s.re) :
    riemannZeta s ≠ 0 :=
  OAI.riemannZeta_ne_zero_of_seven_eighths_lt_re hs

theorem zero_re_le {q : ℕ} [NeZero q]
    (χ : DirichletCharacter ℂ q) {s : ℂ} (hpole : ¬ (χ = 1 ∧ s = 1))
    (hz : DirichletCharacter.LFunction χ s = 0) : s.re ≤ (7 / 8 : ℝ) :=
  le_of_not_gt (fun hs => dirichlet_nonzero χ hs hpole hz)

/-- The uniform real-zero gap for every nonprincipal character, without
a conductor threshold, parity assumption or primitivity assumption. -/
theorem real_zero_gap {q : ℕ} [NeZero q]
    (χ : DirichletCharacter ℂ q) (hχ : χ ≠ 1) {β : ℝ}
    (hz : DirichletCharacter.LFunction χ (β : ℂ) = 0) :
    (1 / 8 : ℝ) ≤ 1 - β := by
  have h := zero_re_le χ (s := (β : ℂ)) (fun hp => hχ hp.1) hz
  rw [Complex.ofReal_re] at h
  linarith

/-- The bad-conductor predicate requiring a nonprincipal zero in a
near-one rectangle is impossible as soon as its left edge is > 7/8.
The height restriction can be arbitrary and need not enter the proof. -/
theorem no_bad_character {q : ℕ} [NeZero q]
    (χ : DirichletCharacter ℂ q) (hχ : χ ≠ 1) {σ : ℝ}
    (hσ : (7 / 8 : ℝ) < σ) (T : ℝ) :
    ¬ ∃ s : ℂ, σ ≤ s.re ∧ |s.im| ≤ T ∧
      DirichletCharacter.LFunction χ s = 0 := by
  rintro ⟨s, hs, _, hz⟩
  exact (dirichlet_nonzero χ (lt_of_lt_of_le hσ hs) (fun hp => hχ hp.1)) hz

end Factoring.QRH

#print axioms OAI.DirichletCharacter.LFunction_ne_zero_of_seven_eighths_lt_re
#print axioms OAI.riemannZeta_ne_zero_of_seven_eighths_lt_re
#print axioms Factoring.QRH.dirichlet_nonzero
#print axioms Factoring.QRH.zeta_nonzero
#print axioms Factoring.QRH.zero_re_le
#print axioms Factoring.QRH.real_zero_gap
#print axioms Factoring.QRH.no_bad_character
