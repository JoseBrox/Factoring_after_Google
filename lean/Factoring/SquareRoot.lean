import Mathlib.Data.Int.GCD
import Mathlib.Data.Int.ModEq
import Mathlib.Tactic.Ring

/-!
# A nontrivial square congruence produces a proper factor

The result is valid for every natural modulus N > 1, including even moduli
and repeated prime factors.  The roots may be arbitrary integers: neither
invertibility nor a prescribed representative range is needed.

The hypotheses exclude both trivial signs.  The conclusion certifies that
the computed gcd divides N and lies strictly between 1 and N.  Producing
the square congruence and estimating its success probability are separate
problems and are not claimed here.
-/

namespace Factoring.SquareRoot

/-- Euclid's lemma turns a nontrivial product congruence into a proper gcd
factor.  This core statement also applies outside square-root extraction. -/
theorem proper_factor_of_product {N : ℕ} {u v : ℤ}
    (hN : 1 < N)
    (hprod : (N : ℤ) ∣ u * v)
    (hu : ¬ (N : ℤ) ∣ u)
    (hv : ¬ (N : ℤ) ∣ v) :
    1 < Int.gcd (N : ℤ) u ∧
      Int.gcd (N : ℤ) u < N ∧
      Int.gcd (N : ℤ) u ∣ N := by
  have hdvd : Int.gcd (N : ℤ) u ∣ N :=
    Int.natCast_dvd_natCast.mp Int.gcd_dvd_left
  have hpos : 0 < Int.gcd (N : ℤ) u := by
    change 0 < Nat.gcd N u.natAbs
    exact Nat.gcd_pos_of_pos_left _ (by omega)
  have hne_one : Int.gcd (N : ℤ) u ≠ 1 := by
    intro heq
    exact hv (Int.dvd_of_dvd_mul_right_of_gcd_one hprod heq)
  have hle : Int.gcd (N : ℤ) u ≤ N :=
    Nat.le_of_dvd (by omega) hdvd
  have hne_N : Int.gcd (N : ℤ) u ≠ N := by
    intro heq
    have hright := Int.gcd_dvd_right (a := (N : ℤ)) (b := u)
    rw [heq] at hright
    exact hu hright
  exact ⟨by omega, by omega, hdvd⟩

/-- The actual gcd returned by the square-root extraction routine. -/
def factorFromRoots (N : ℕ) (x y : ℤ) : ℕ :=
  Int.gcd (N : ℤ) (x - y)

/-- A square congruence with neither trivial sign certifies a proper factor. -/
theorem proper_factor_of_square_congruence {N : ℕ} {x y : ℤ}
    (hN : 1 < N)
    (hsq : x ^ 2 ≡ y ^ 2 [ZMOD (N : ℤ)])
    (hneq : ¬ (x ≡ y [ZMOD (N : ℤ)]))
    (hneg : ¬ (x ≡ -y [ZMOD (N : ℤ)])) :
    1 < factorFromRoots N x y ∧
      factorFromRoots N x y < N ∧
      factorFromRoots N x y ∣ N := by
  have hprod : (N : ℤ) ∣ (x - y) * (x + y) := by
    have hid : (x - y) * (x + y) = x ^ 2 - y ^ 2 := by ring
    rw [hid]
    exact hsq.symm.dvd
  have hminus : ¬ (N : ℤ) ∣ x - y := by
    intro hx
    exact hneq (Int.modEq_of_dvd hx).symm
  have hplus : ¬ (N : ℤ) ∣ x + y := by
    intro hx
    have hx' : (N : ℤ) ∣ x - (-y) := by simpa using hx
    exact hneg (Int.modEq_of_dvd hx').symm
  exact proper_factor_of_product hN hprod hminus hplus

theorem roots_example_odd : factorFromRoots 15 4 1 = 3 := by decide

/-- An even modulus and noninvertible roots are permitted. -/
theorem roots_example_even_nonunits : factorFromRoots 12 4 2 = 2 := by decide

end Factoring.SquareRoot
