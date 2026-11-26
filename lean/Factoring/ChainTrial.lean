import Factoring.ChainCount
import Factoring.ChainCost
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity

/-! The supplied-M quadratic chain: explicit exponent decomposition, exact
uniform-trial success fraction, and abstract arithmetic-operation bounds.
The executable routine uses no hidden-prime data. -/
namespace Factoring.Quadratic

/-- Repeated halving computes the two-adic exponent and odd part, not a
factorization of the supplied exponent. The zero input is handled separately. -/
def decompose (M : ℕ) : ℕ×ℕ :=
  if h : 0<M ∧ M%2=0 then
    let z := decompose (M/2)
    (z.1+1,z.2)
  else (0,M)
termination_by M
decreasing_by omega

theorem decompose_correct {M : ℕ} (hM : 0<M) :
    Odd (decompose M).2 ∧ M=2^(decompose M).1*(decompose M).2 := by
  induction M using Nat.strong_induction_on with
  | h M ih =>
    rw [decompose]
    split_ifs with he
    · have hi := ih (M/2) (by omega) (by omega)
      change Odd (decompose (M/2)).2 ∧
        M=2^((decompose (M/2)).1+1)*(decompose (M/2)).2
      refine ⟨hi.1,?_⟩
      calc
        M = 2*(M/2) := by omega
        _ = 2*(2^(decompose (M/2)).1*(decompose (M/2)).2) :=
          congrArg (fun n:ℕ => 2*n) hi.2
        _ = _ := by rw [pow_succ]; ring
    · constructor
      · exact ⟨M/2,by omega⟩
      · simp

/-- The factoring trial from the manuscript, using only N,b,a,M. -/
def splitM (N b a M : ℕ) : Option ℕ :=
  let z := decompose M
  split N b a z.2 z.1

theorem splitM_sound {N b a M d : ℕ} (h : splitM N b a M=some d) :
    1<d ∧ d<N ∧ d∣N :=
  split_sound h

/-- Main finite success theorem, exactly under the manuscript's promises.
The inequality is the success count divided by N ≥ (p+3)/(2p), cleared
of denominators. p and q occur only in the proof, not the algorithm. -/
theorem splitM_count {N b M p q : ℕ} [Fact p.Prime] [Fact q.Prime]
    (hN : N%2=1) (hM : 0<M) (hp : p∣N) (hq : q∣N)
    (hcop : Nat.Coprime b N) (hsquare : IsSquare (b : ZMod p))
    (hnonsquare : ¬IsSquare (b : ZMod q)) (hdiv : p-1∣M) :
    2*p*Nat.card {a : Fin N // splitM N b a.val M ≠ none} ≥ (p+3)*N := by
  letI : NeZero N := ⟨by omega⟩
  have hpne : p ≠ 2 := by intro he; rw [he] at hp; omega
  have hqne : q ≠ 2 := by intro he; rw [he] at hq; omega
  have hpodd := (Fact.out : p.Prime).eq_two_or_odd.resolve_left hpne
  have hp2 : (2 : ZMod p) ≠ 0 := by
    intro he
    have hd := (ZMod.natCast_zmod_eq_zero_iff_dvd 2 p).mp he
    have hl := Nat.le_of_dvd (by decide : 0<2) hd
    have hh := (Fact.out : p.Prime).one_lt
    omega
  have hq2 : (2 : ZMod q) ≠ 0 := by
    intro he
    have hd := (ZMod.natCast_zmod_eq_zero_iff_dvd 2 q).mp he
    have hl := Nat.le_of_dvd (by decide : 0<2) hd
    have hh := (Fact.out : q.Prime).one_lt
    omega
  obtain ⟨r,hr⟩ := hsquare
  have hr0 : r ≠ 0 := by
    intro hz
    have hb : (b : ZMod p)=0 := by simpa [hz] using hr
    have hbdiv := (ZMod.natCast_zmod_eq_zero_iff_dvd b p).mp hb
    have hd := Nat.dvd_gcd hbdiv hp
    change Nat.gcd b N=1 at hcop
    rw [hcop] at hd
    exact (Fact.out : p.Prime).not_dvd_one hd
  have hdec := decompose_correct hM
  have hdiv' : p-1 ∣ 2^(decompose M).1*(decompose M).2 := by
    rw [← hdec.2]
    exact hdiv
  exact mixed_success_count hp hq hpodd hp2 hq2 r hr.symm hr0
    (fun x hx => hnonsquare ⟨x,hx.symm⟩) hdec.1 hdiv'

/-- Exact finite-uniform probability statement, including its strict
one-half bound. Rational arithmetic avoids floating-point estimates. -/
theorem splitM_probability {N b M p q : ℕ} [Fact p.Prime] [Fact q.Prime]
    (hN : N%2=1) (hM : 0<M) (hp : p∣N) (hq : q∣N)
    (hcop : Nat.Coprime b N) (hsquare : IsSquare (b : ZMod p))
    (hnonsquare : ¬IsSquare (b : ZMod q)) (hdiv : p-1∣M) :
    (Nat.card {a : Fin N // splitM N b a.val M ≠ none} : ℚ)/(N:ℚ) ≥
      ((p:ℚ)+3)/(2*p) ∧ (1:ℚ)/2 < ((p:ℚ)+3)/(2*p) := by
  have h := splitM_count hN hM hp hq hcop hsquare hnonsquare hdiv
  have hN0 : (0:ℚ)<N := by exact_mod_cast (show 0<N by omega)
  have hp0 : (0:ℚ)<p := by exact_mod_cast (Fact.out : p.Prime).pos
  constructor
  · apply (div_le_div_iff₀ (by positivity) hN0).mpr
    rw [_root_.mul_comm (Nat.card {a : Fin N // splitM N b a.val M ≠ none} : ℚ) (2*(p:ℚ))]
    exact_mod_cast h
  · apply (lt_div_iff₀ (by positivity)).mpr
    linarith

/-- The abstract counts of quadratic-ring multiplications and gcd tests
for positive M. Per-operation bit complexity and the cost of sampling are
not included in this theorem. -/
theorem splitM_arithmetic_budget {M : ℕ} (hM : 0<M) :
    powerCost (decompose M).2+(decompose M).1 ≤ 2*(Nat.log 2 M+1) ∧
    2+3*((decompose M).1+1) ≤ 3*(Nat.log 2 M+1)+2 := by
  have hd := decompose_correct hM
  have hu0 : (decompose M).2 ≠ 0 := by
    obtain ⟨k,hk⟩ := hd.1
    omega
  have h1 := chain_cost_le (decompose M).2 (decompose M).1 hu0
  have h2 := chain_gcd_budget (decompose M).2 (decompose M).1 hu0
  rw [← hd.2] at h1 h2
  exact ⟨h1,h2⟩

end Factoring.Quadratic
