import Mathlib.NumberTheory.DiophantineApproximation.ContinuedFractions
import Mathlib.Data.Rat.Cast.Order
import Mathlib.Tactic

/-! Certified uniqueness and existence of the bounded-denominator
continued-fraction reconstruction used in TryPair. Bit bounds for
root isolation and formation of the rational approximation are separate. -/
namespace Factoring.RationalRecovery

theorem separation (p q : ℚ) (hne : p≠q) :
    (1:ℝ)≤ |(p:ℝ)-(q:ℝ)| * (p.den:ℝ)*(q.den:ℝ) := by
  have hp : (0:ℝ)<p.den := by exact_mod_cast p.den_pos
  have hq : (0:ℝ)<q.den := by exact_mod_cast q.den_pos
  let t : ℤ := p.num*q.den-q.num*p.den
  have he : ((p:ℝ)-(q:ℝ))*(p.den:ℝ)*(q.den:ℝ)=(t:ℝ) := by
    rw [Rat.cast_def p,Rat.cast_def q]
    dsimp [t]
    push_cast
    field_simp
    ring
  have ht : t≠0 := by
    intro hz
    rw [hz,Int.cast_zero] at he
    have hh : (p:ℝ)-(q:ℝ)=0 := (mul_eq_zero.mp ((mul_eq_zero.mp he).resolve_right hq.ne')).resolve_right hp.ne'
    exact hne (by exact_mod_cast sub_eq_zero.mp hh)
  have h1 : (1:ℤ)≤|t| := by
    have hpos : (0 : ℤ) < |t| := abs_pos.mpr ht
    omega
  have hh : (1:ℝ)≤|(t:ℝ)| := by exact_mod_cast h1
  rw [←he,abs_mul,abs_mul,abs_of_pos hp,abs_of_pos hq] at hh
  exact hh

/-- At most one rational with denominator ≤ D lies strictly within
1/(2D²) of a certified approximation. -/
theorem unique_near {x : ℝ} {D : ℕ} (hD : 0<D) (p q : ℚ)
    (hp : p.den≤D) (hq : q.den≤D)
    (h₁ : |x-(p:ℝ)| < 1/(2*(D:ℝ)^2))
    (h₂ : |x-(q:ℝ)| < 1/(2*(D:ℝ)^2)) :
    p=q := by
  by_contra h
  have hd : (0:ℝ)<D := by exact_mod_cast hD
  have hp' : (p.den:ℝ)≤D := by exact_mod_cast hp
  have hq' : (q.den:ℝ)≤D := by exact_mod_cast hq
  have hs := separation p q h
  have hmul : (p.den:ℝ)*(q.den:ℝ)≤(D:ℝ)^2 := by
    rw [pow_two]
    exact mul_le_mul hp' hq' (by positivity) hd.le
  have ht : |(p:ℝ)-(q:ℝ)| < 1/(D:ℝ)^2 := by
    have htri := abs_sub_le (p:ℝ) x (q:ℝ)
    rw [abs_sub_comm (p:ℝ) x] at htri
    have he : 1/(2*(D:ℝ)^2)+1/(2*(D:ℝ)^2)=1/(D:ℝ)^2 := by ring
    linarith
  have hs' : (1:ℝ)≤|(p:ℝ)-(q:ℝ)| * (D:ℝ)^2 := by
    exact hs.trans (by rw [mul_assoc]; exact mul_le_mul_of_nonneg_left hmul (abs_nonneg _))
  have ht' := (lt_div_iff₀ (show (0:ℝ)<(D:ℝ)^2 by positivity)).mp ht
  linarith

/-- The true rational occurs as an actual mathlib continued-fraction
convergent, not merely a member of an abstract candidate set. -/
theorem occurs_as_convergent {x : ℝ} {D : ℕ} (q : ℚ)
    (hq : q.den≤D) (h : |x-(q:ℝ)| < 1/(2*(D:ℝ)^2)) :
    ∃ n, (GenContFract.of x).convs n=(q:ℝ) := by
  have hd : (0:ℝ)<q.den := by exact_mod_cast q.den_pos
  have hh : (q.den:ℝ)≤D := by exact_mod_cast hq
  apply Real.exists_convs_eq_rat (q:=q)
  apply h.trans_le
  apply div_le_div_of_nonneg_left (by norm_num) (by positivity)
  nlinarith

end Factoring.RationalRecovery

