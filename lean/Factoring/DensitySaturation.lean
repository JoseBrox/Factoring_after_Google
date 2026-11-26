import Factoring.MultisetSaturation
import Mathlib.Analysis.SpecialFunctions.Pow.Real

/-! Explicit density-to-order-multiple theorem. These are precisely the
finite numerical guards used in the deterministic saturation proof.
No prime distribution result is used or asserted in this module. -/
namespace Factoring.Saturation

/-- The real-valued density and cutoff inequalities imply the integer
subgroup-index cap. All rounding in the product degree is handled by Nat.log. -/
theorem density_index_guard {N p B K s : ℕ}
    (hB : 1<B) (hpB : B<p) (hpN : p≤N) (hL : 1≤Real.log N)
    (hs : (B:ℝ)/(6*Real.log B) ≤ s)
    (hK : (B:ℝ)*Real.exp (Real.log N / Real.log B * Real.log (6*Real.log N)) ≤ K) :
    B^(Nat.log B (p-1))<p ∧
      p-1 ≤ K*(s+Nat.log B (p-1)-1).choose (Nat.log B (p-1)) := by
  let k := Nat.log B (p-1)
  have hk : 0<k := Nat.log_pos hB (by omega)
  have hB' : (1:ℝ)<B := by exact_mod_cast hB
  have hlogB := Real.log_pos hB'
  have hB0 : (0:ℝ)<B := by linarith
  have hk' : (0:ℝ)<k := by exact_mod_cast hk
  have h6L : 0<6*Real.log N := by linarith
  have h6L' : 1≤6*Real.log N := by linarith
  have hpow : B^k≤p-1 := Nat.pow_log_le_self B (by omega)
  refine ⟨lt_of_le_of_lt hpow (by omega),?_⟩
  have hlog : (k:ℝ)*Real.log B≤Real.log N := by
    have hh : (B:ℝ)^k≤(N:ℝ) := by
      exact_mod_cast (hpow.trans (show p-1≤N by omega))
    simpa only [Real.log_pow] using Real.log_le_log (pow_pos hB0 k) hh
  have hkL : (k:ℝ)≤Real.log N / Real.log B := (le_div_iff₀ hlogB).mpr hlog
  have hspos : 0<s := by
    have hpos : 0<(B:ℝ)/(6*Real.log B) := div_pos hB0 (by positivity)
    exact_mod_cast (hpos.trans_le hs)
  have hratio : (B:ℝ)/(6*Real.log N)≤(s:ℝ)/k := by
    apply (div_le_div_iff₀ h6L hk').mpr
    have hb := (div_le_iff₀ (show 0<6*Real.log B by positivity)).mp hs
    calc
      (B:ℝ)*k ≤ ((s:ℝ)*(6*Real.log B))*k :=
        mul_le_mul_of_nonneg_right hb hk'.le
      _ = (6*(s:ℝ))*((k:ℝ)*Real.log B) := by ring
      _ ≤ (6*(s:ℝ))*Real.log N := mul_le_mul_of_nonneg_left hlog (by positivity)
      _ = (s:ℝ)*(6*Real.log N) := by ring
  have hcount : ((B:ℝ)/(6*Real.log N))^k ≤ ((s+k-1).choose k:ℝ) :=
    (pow_le_pow_left₀ (by positivity) hratio k).trans (multichoose_lower hspos hk)
  rw [div_pow] at hcount
  have hmul := (div_le_iff₀ (pow_pos h6L k)).mp hcount
  have hExp : (6*Real.log N)^k ≤
      Real.exp (Real.log N / Real.log B * Real.log (6*Real.log N)) := by
    calc
      _ = Real.exp ((k:ℝ)*Real.log (6*Real.log N)) := by
        rw [mul_comm (k:ℝ), Real.exp_mul, Real.exp_log h6L, Real.rpow_natCast]
      _ ≤ _ := Real.exp_le_exp.mpr
        (mul_le_mul_of_nonneg_right hkL (Real.log_nonneg h6L'))
  have hcap : (B:ℝ)*(6*Real.log N)^k≤K :=
    (mul_le_mul_of_nonneg_left hExp hB0.le).trans hK
  have hlt : ((p-1:ℕ):ℝ) < (B:ℝ)^(k+1) := by
    exact_mod_cast Nat.lt_pow_succ_log_self hB (p-1)
  have hh : ((p-1:ℕ):ℝ)≤(K:ℝ)*((s+k-1).choose k:ℝ) := by
    calc
      _ ≤ (B:ℝ)^(k+1) := hlt.le
      _ = (B:ℝ)*(B:ℝ)^k := by rw [pow_succ,mul_comm]
      _ ≤ (B:ℝ)*(((s+k-1).choose k:ℝ)*(6*Real.log N)^k) :=
        mul_le_mul_of_nonneg_left hmul hB0.le
      _ = ((B:ℝ)*(6*Real.log N)^k)*((s+k-1).choose k:ℝ) := by ring
      _ ≤ _ := mul_le_mul_of_nonneg_right hcap (by positivity)
  exact_mod_cast hh

/-- The manuscript's density hypothesis, a verified certificate for each
successful prime, and its cutoff ensure one common p-1 multiple for every
prime p|N, even for N with repeated prime factors. -/
theorem density_order_multiple {N B K : ℕ} (S : Finset ℕ) (e : ℕ→ℕ)
    (hB : 1<B) (hBK : B≤K) (hN : 0<N) (hL : 1≤Real.log N)
    (hprime : ∀ n ∈ S, n.Prime) (hsmall : ∀ n ∈ S, n≤B)
    (hcert : ∀ n ∈ S, (n : ZMod N)^(e n)=1)
    (hdensity : (B:ℝ)/(6*Real.log B)≤S.card)
    (hK : (B:ℝ)*Real.exp (Real.log N / Real.log B * Real.log (6*Real.log N))≤K)
    (hnoSmall : ∀ p : ℕ, p.Prime → p∣N → K<p) :
    ∀ p : ℕ, p.Prime → p∣N → p-1 ∣ S.lcm e*indexMultiple K := by
  have hB' : (1:ℝ)<B := by exact_mod_cast hB
  have hspos : 0<S.card := by
    have hp : 0<(B:ℝ)/(6*Real.log B) :=
      div_pos (by linarith) (mul_pos (by norm_num) (Real.log_pos hB'))
    exact_mod_cast (hp.trans_le hdensity)
  apply all_prime_order_multiple S e (Finset.card_pos.mp hspos) hprime hsmall hcert
  intro p hp hdiv
  exact density_index_guard hB (hBK.trans_lt (hnoSmall p hp hdiv))
    (Nat.le_of_dvd hN hdiv) hL hdensity hK

/-- Positivity of the actual common-exponent construction follows from
positive individual certificates. -/
theorem common_exponent_pos {S : Finset ℕ} {e : ℕ→ℕ} (K : ℕ)
    (he : ∀ n ∈ S, 0<e n) : 0<S.lcm e*indexMultiple K := by
  apply Nat.mul_pos _ (indexMultiple_pos K)
  by_contra h
  have hz : S.lcm e=0 := by omega
  obtain ⟨a,ha,hea⟩ := (Set.mem_image e (S : Set ℕ) 0).mp (Finset.lcm_eq_zero_iff.mp hz)
  exact (ne_of_gt (he a ha)) hea

end Factoring.Saturation
