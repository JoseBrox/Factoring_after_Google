import Mathlib.Data.ZMod.Basic
import Mathlib.Algebra.Field.Basic
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.SplitIfs
import Lean.Elab.Tactic.Omega

/-!
# Quadratic arithmetic and a sound coefficient-chain splitter

Copyright 2026 Jose Brox. Released under CC BY 4.0; see LICENSE.

The pair `(u,v)` represents `u + v α`, where `α² = b`. We prove the
arithmetic identities over arbitrary commutative rings, including compatibility
with the two evaluations in a split quadratic algebra. Binary powering is
proved equal to its elementary power specification.

The executable routine at the end uses actual arithmetic in `ZMod N`. It
tests the norm and, at every squaring stage, both coefficient gcds used by the
quadratic relation method. Every returned value is a proper divisor. The odd
part and number of squarings are explicit inputs; their provenance, the mixed
prime promise, success probability, and running-time bound are not formalized
here. The two local separation lemmas explain a portion of the success
mechanism without asserting that a successful stage always exists.
-/

namespace Factoring.Quadratic

section Arithmetic

variable {R : Type*} [CommRing R]

/-- Multiplication with the relation `α² = b`. -/
def mul (b : R) (x y : R × R) : R × R :=
  (x.1 * y.1 + b * x.2 * y.2, x.1 * y.2 + x.2 * y.1)

/-- The multiplicative identity, represented as a pair. -/
def one : R × R := (1, 0)

/-- Evaluation at a proposed root of `X² - b`. -/
def eval (r : R) (x : R × R) : R := x.1 + r * x.2

/-- Conjugation and its quadratic norm. -/
def conjugate (x : R × R) : R × R := (x.1, -x.2)

def norm (b : R) (x : R × R) : R := x.1 * x.1 - b * x.2 * x.2

theorem mul_assoc (b : R) (x y z : R × R) :
    mul b (mul b x y) z = mul b x (mul b y z) := by
  apply Prod.ext <;> dsimp [mul] <;> ring

theorem mul_comm (b : R) (x y : R × R) : mul b x y = mul b y x := by
  apply Prod.ext <;> dsimp [mul] <;> ring

@[simp] theorem mul_one (b : R) (x : R × R) : mul b x one = x := by
  apply Prod.ext <;> simp [mul, one]

@[simp] theorem one_mul (b : R) (x : R × R) : mul b one x = x := by
  apply Prod.ext <;> simp [mul, one]

@[simp] theorem eval_one (r : R) : eval r (one : R × R) = 1 := by
  simp [eval, one]

theorem eval_mul (b r : R) (hr : r * r = b) (x y : R × R) :
    eval r (mul b x y) = eval r x * eval r y := by
  dsimp [eval, mul]
  rw [← hr]
  ring

theorem norm_mul (b : R) (x y : R × R) :
    norm b (mul b x y) = norm b x * norm b y := by
  dsimp [norm, mul]
  ring

theorem mul_conjugate (b : R) (x : R × R) :
    mul b x (conjugate x) = (norm b x, 0) := by
  apply Prod.ext <;> dsimp [mul, conjugate, norm] <;> ring

theorem split_norm (b r : R) (hr : r * r = b) (x : R × R) :
    norm b x = eval r x * eval (-r) x := by
  dsimp [norm, eval]
  rw [← hr]
  ring

/-- A simple specification of natural-number powering. -/
def powerSpec (b : R) (x : R × R) : ℕ → R × R
  | 0 => one
  | n + 1 => mul b (powerSpec b x n) x

theorem powerSpec_add (b : R) (x : R × R) (m n : ℕ) :
    powerSpec b x (m + n) = mul b (powerSpec b x m) (powerSpec b x n) := by
  induction n with
  | zero => simp [powerSpec]
  | succ n ih =>
    rw [Nat.add_succ, powerSpec, ih, powerSpec, mul_assoc]

theorem eval_powerSpec (b r : R) (hr : r * r = b) (x : R × R) (n : ℕ) :
    eval r (powerSpec b x n) = (eval r x) ^ n := by
  induction n with
  | zero => simp [powerSpec]
  | succ n ih => rw [powerSpec, eval_mul b r hr, ih, pow_succ]

theorem norm_powerSpec (b : R) (x : R × R) (n : ℕ) :
    norm b (powerSpec b x n) = (norm b x) ^ n := by
  induction n with
  | zero => simp [powerSpec, norm, one]
  | succ n ih => rw [powerSpec, norm_mul, ih, pow_succ]

/-- Binary powering, with one recursive call at half the exponent. -/
def power (b : R) (x : R × R) (n : ℕ) : R × R :=
  if hn : n = 0 then one else
    let y := power b x (n / 2)
    let z := mul b y y
    if n % 2 = 0 then z else mul b z x
termination_by n
decreasing_by omega

theorem power_eq_spec (b : R) (x : R × R) (n : ℕ) :
    power b x n = powerSpec b x n := by
  induction n using Nat.strong_induction_on with
  | h n ih =>
    by_cases hn : n = 0
    · subst n
      rw [power]
      simp [powerSpec]
    · rw [power, dif_neg hn, ih (n / 2) (by omega)]
      dsimp only
      by_cases he : n % 2 = 0
      · rw [if_pos he, ← powerSpec_add]
        congr 1
        omega
      · rw [if_neg he, ← powerSpec_add, ← powerSpec]
        congr 1
        omega

theorem eval_power (b r : R) (hr : r * r = b) (x : R × R) (n : ℕ) :
    eval r (power b x n) = (eval r x) ^ n := by
  rw [power_eq_spec, eval_powerSpec b r hr]

theorem norm_power (b : R) (x : R × R) (n : ℕ) :
    norm b (power b x n) = (norm b x) ^ n := by
  rw [power_eq_spec, norm_powerSpec]

/-- The initial element and its successive squares. -/
def squareChain (b : R) (x : R × R) : ℕ → List (R × R)
  | 0 => [x]
  | n + 1 => x :: squareChain b (mul b x x) n

@[simp] theorem squareChain_length (b : R) (x : R × R) (n : ℕ) :
    (squareChain b x n).length = n + 1 := by
  induction n generalizing x with
  | zero => rfl
  | succ n ih => simp [squareChain, ih]

/-- In odd characteristic, opposite evaluations force a nonzero coefficient. -/
theorem linear_ne_zero_of_opposite_evaluations (r : R) (x : R × R)
    (htwo : (2 : R) ≠ 0) (hp : eval r x = 1) (hm : eval (-r) x = -1) :
    x.2 ≠ 0 := by
  intro hx
  have hp' : x.1 = 1 := by simpa [eval, hx] using hp
  have hm' : x.1 = -1 := by simpa [eval, hx] using hm
  apply htwo
  linear_combination hm' - hp'

end Arithmetic

section Transport

variable {R S : Type*} [CommRing R] [CommRing S]

/-- Apply a coefficient-ring homomorphism to both coordinates. -/
def map (f : R →+* S) (x : R × R) : S × S := (f x.1, f x.2)

theorem map_mul (f : R →+* S) (b : R) (x y : R × R) :
    map f (mul b x y) = mul (f b) (map f x) (map f y) := by
  apply Prod.ext <;> simp [map, mul]

theorem map_powerSpec (f : R →+* S) (b : R) (x : R × R) (n : ℕ) :
    map f (powerSpec b x n) = powerSpec (f b) (map f x) n := by
  induction n with
  | zero => simp [powerSpec, map, one]
  | succ n ih => rw [powerSpec, map_mul, ih, powerSpec]

theorem map_power (f : R →+* S) (b : R) (x : R × R) (n : ℕ) :
    map f (power b x n) = power (f b) (map f x) n := by
  simp only [power_eq_spec, map_powerSpec]

end Transport

/-- In a nonsplit quadratic algebra over a field of odd characteristic,
every square root of one has zero linear coefficient. -/
theorem linear_eq_zero_of_nonsquare {K : Type*} [Field K] (b : K)
    (hnonsquare : ∀ r : K, r * r ≠ b) (htwo : (2 : K) ≠ 0)
    (x : K × K) (hsquare : mul b x x = one) : x.2 = 0 := by
  have hs : x.1 * x.1 + b * x.2 * x.2 = 1 := congrArg Prod.fst hsquare
  have ht : x.1 * x.2 + x.2 * x.1 = 0 := congrArg Prod.snd hsquare
  have hprod : x.1 * x.2 = 0 := by
    apply (mul_eq_zero.mp (show (2 : K) * (x.1 * x.2) = 0 by
      linear_combination ht)).resolve_left htwo
  rcases mul_eq_zero.mp hprod with hx | hx
  · by_contra hy
    have hrel : b * (x.2 * x.2) = 1 := by
      simpa [hx, _root_.mul_assoc] using hs
    apply hnonsquare (x.2)⁻¹
    apply mul_right_cancel₀ (mul_ne_zero hy hy)
    calc
      (x.2⁻¹ * x.2⁻¹) * (x.2 * x.2) = 1 := by field_simp [hy]
      _ = b * (x.2 * x.2) := hrel.symm
  · exact hx

/-! ## Executable modular chain and unconditional output soundness -/

/-- Return a gcd only when it lies strictly between one and the modulus. -/
def gcdCandidate (N a : ℕ) : Option ℕ :=
  let d := Nat.gcd a N
  if 1 < d ∧ d < N then some d else none

theorem gcdCandidate_sound {N a d : ℕ} (h : gcdCandidate N a = some d) :
    1 < d ∧ d < N ∧ d ∣ N := by
  unfold gcdCandidate at h
  dsimp only at h
  split_ifs at h with hg
  · cases h
    exact ⟨hg.1, hg.2, Nat.gcd_dvd_right _ _⟩

/-- Inspect coefficients in their given order and return the first proper gcd. -/
def scanGcd (N : ℕ) : List ℕ → Option ℕ
  | [] => none
  | a :: rest =>
      match gcdCandidate N a with
      | some d => some d
      | none => scanGcd N rest

theorem scanGcd_sound (N : ℕ) (values : List ℕ) {d : ℕ}
    (h : scanGcd N values = some d) : 1 < d ∧ d < N ∧ d ∣ N := by
  induction values with
  | nil => simp [scanGcd] at h
  | cons a rest ih =>
    cases hg : gcdCandidate N a with
    | none => exact ih (by simpa [scanGcd, hg] using h)
    | some g =>
      have hd : g = d := by simpa [scanGcd, hg] using h
      subst d
      exact gcdCandidate_sound hg

/-- The scan reports failure exactly when every tested gcd is improper. -/
theorem scanGcd_none_iff (N : ℕ) (values : List ℕ) :
    scanGcd N values = none ↔ ∀ a ∈ values, gcdCandidate N a = none := by
  induction values with
  | nil => simp [scanGcd]
  | cons a rest ih =>
    cases hg : gcdCandidate N a with
    | none => simp [scanGcd, hg, ih]
    | some g => simp [scanGcd, hg]

/-- Test the norm, then the linear coefficient and identity-relation gcd at
each successive square. `oddPart` and `steps` specify `2^steps * oddPart`.
No input promise is needed for output soundness. -/
def split (N b a oddPart steps : ℕ) : Option ℕ :=
  let x : ZMod N × ZMod N := (-(a : ZMod N), 1)
  let denominator := (norm (b : ZMod N) x).val
  let chain := squareChain (b : ZMod N) (power (b : ZMod N) x oddPart) steps
  let coefficients := chain.flatMap fun z =>
    [z.2.val, Nat.gcd (z.1 - 1).val z.2.val]
  if Nat.gcd denominator N = 1 then scanGcd N coefficients
  else gcdCandidate N denominator

theorem split_sound {N b a oddPart steps d : ℕ}
    (h : split N b a oddPart steps = some d) :
    1 < d ∧ d < N ∧ d ∣ N := by
  unfold split at h
  dsimp only at h
  split_ifs at h
  · exact scanGcd_sound N _ h
  · exact gcdCandidate_sound h

/-- Reduction to any divisor of `N` commutes with the actual powering routine. -/
theorem reduce_power {N p : ℕ} (hp : p ∣ N) (b : ZMod N)
    (x : ZMod N × ZMod N) (n : ℕ) :
    map (ZMod.castHom hp (ZMod p)) (power b x n) =
      power ((ZMod.castHom hp (ZMod p)) b)
        (map (ZMod.castHom hp (ZMod p)) x) n := by
  exact map_power _ _ _ _

/-- Small executable checks, proved by Lean's ordinary decision procedure. -/
theorem split_example_factor_five : split 35 2 1 3 4 = some 5 := by
  simp only [split, power_eq_spec]
  decide

theorem split_example_factor_seven : split 35 2 0 3 4 = some 7 := by
  simp only [split, power_eq_spec]
  decide

theorem split_example_prime : split 13 2 1 3 2 = none := by
  simp only [split, power_eq_spec]
  decide

end Factoring.Quadratic
