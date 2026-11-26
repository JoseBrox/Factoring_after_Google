import Factoring.Quadratic
import Mathlib.NumberTheory.LegendreSymbol.Basic
import Mathlib.Data.Nat.Factorization.Basic

/-! The missing success bridge for the quadratic relation chain.
We do not assume squarefree N. The local prime parameters are used only
in the proof, not in the executable splitter. -/
namespace Factoring.Quadratic

theorem power_add {R : Type*} [CommRing R] (b : R) (x : R × R) (m n : ℕ) :
    power b x (m+n) = mul b (power b x m) (power b x n) := by
  simp only [power_eq_spec, powerSpec_add]

theorem stage_mem {R : Type*} [CommRing R] (b : R) (x : R × R)
    (u j steps : ℕ) (hj : j ≤ steps) :
    power b x (u * 2^j) ∈ squareChain b (power b x u) steps := by
  simp only [power_eq_spec]
  induction steps generalizing j u with
  | zero =>
    have : j = 0 := by omega
    subst j
    simp [squareChain]
  | succ s ih =>
    cases j with
    | zero => simp [squareChain]
    | succ j =>
      rw [squareChain, ← powerSpec_add]
      apply List.mem_cons_of_mem
      have he : u * 2^(j+1) = (u+u) * 2^j := by rw [pow_succ]; ring
      rw [he]
      exact ih (u+u) j (by omega)

theorem reduction_eq_zero_iff {N p : ℕ} [NeZero N] (hp : p ∣ N) (x : ZMod N) :
    ZMod.castHom hp (ZMod p) x = 0 ↔ p ∣ x.val := by
  rw [ZMod.castHom_apply, ZMod.cast_eq_val, ZMod.natCast_zmod_eq_zero_iff_dvd]

theorem candidate_exists {N p q a : ℕ} [NeZero N] [Fact p.Prime]
    (hp : p ∣ N) (hq : q ∣ N) (ha : p ∣ a) (hb : ¬q ∣ a) :
    gcdCandidate N a ≠ none := by
  have hd : p ∣ Nat.gcd a N := Nat.dvd_gcd ha hp
  have hpos : 0 < Nat.gcd a N := Nat.gcd_pos_of_pos_right _ (NeZero.pos N)
  have hgt : 1 < Nat.gcd a N :=
    (Fact.out : p.Prime).one_lt.trans_le (Nat.le_of_dvd hpos hd)
  have hle : Nat.gcd a N ≤ N := Nat.le_of_dvd (NeZero.pos N) (Nat.gcd_dvd_right _ _)
  have hne : Nat.gcd a N ≠ N := by
    intro he
    apply hb
    exact (show q ∣ Nat.gcd a N by rwa [he]).trans (Nat.gcd_dvd_left _ _)
  simp [gcdCandidate, hgt, lt_of_le_of_ne hle hne]

theorem norm_candidate_or_coprime {N q a : ℕ} [NeZero N] (hq : q ∣ N)
    (ha : ¬q ∣ a) :
    Nat.gcd a N = 1 ∨ gcdCandidate N a ≠ none := by
  by_cases h : Nat.gcd a N = 1
  · exact Or.inl h
  right
  have hpos : 0 < Nat.gcd a N := Nat.gcd_pos_of_pos_right _ (NeZero.pos N)
  have hle := Nat.le_of_dvd (NeZero.pos N) (Nat.gcd_dvd_right a N)
  have hne : Nat.gcd a N ≠ N := by
    intro he
    exact ha ((show q ∣ Nat.gcd a N by rwa [he]).trans (Nat.gcd_dvd_left _ _))
  simp [gcdCandidate, show 1 < Nat.gcd a N by omega, lt_of_le_of_ne hle hne]

/-- The actual coefficient scan succeeds if any tested member supplies a proper gcd,
provided the norm does not vanish at the nonsplit prime. -/
theorem split_of_test {N b a u steps q : ℕ} [NeZero N] (hq : q ∣ N)
    (hnorm : ¬q ∣ (norm (b : ZMod N) (-(a : ZMod N), 1)).val)
    (z : ZMod N × ZMod N)
    (hz : z ∈ squareChain (b : ZMod N) (power (b : ZMod N) (-(a : ZMod N), 1) u) steps)
    (htest : gcdCandidate N z.2.val ≠ none ∨
      gcdCandidate N (Nat.gcd (z.1 - 1).val z.2.val) ≠ none) :
    split N b a u steps ≠ none := by
  intro h
  rcases norm_candidate_or_coprime hq hnorm with hg | hg
  · simp only [split, hg, if_pos] at h
    have hs := (scanGcd_none_iff _ _).mp h
    rcases htest with ht | ht
    · exact ht (hs _ (List.mem_flatMap.mpr ⟨z, hz, by simp⟩))
    · exact ht (hs _ (List.mem_flatMap.mpr ⟨z, hz, by simp⟩))
  · by_cases he : Nat.gcd (norm (b : ZMod N) (-(a : ZMod N), 1)).val N = 1
    · exact hg (by simp [gcdCandidate, he])
    · exact hg (by simpa only [split, if_neg he] using h)

theorem map_one_pair {R S : Type*} [CommRing R] [CommRing S] (f : R →+* S) :
    map f (one : R × R) = one := by
  simp [map, one]

theorem map_norm {R S : Type*} [CommRing R] [CommRing S] (f : R →+* S)
    (b : R) (x : R × R) : f (norm b x) = norm (f b) (map f x) := by
  simp [map, norm]

/-- If the two split evaluations are signs with product -1, their linear
coefficient is nonzero and their square is the identity. -/
theorem opposite_stage {F : Type*} [Field F] (b r : F) (hr : r*r=b)
    (hr0 : r ≠ 0) (h2 : (2 : F) ≠ 0) (z : F × F)
    (hp : eval r z ^ 2 = 1) (hm : eval (-r) z ^ 2 = 1)
    (hprod : eval r z * eval (-r) z = -1) :
    z.2 ≠ 0 ∧ mul b z z = one := by
  have hnegroot : (-r)*(-r)=b := by rw [neg_mul_neg, hr]
  constructor
  · intro hz
    simp [eval, hz, pow_two] at hp hprod
    apply h2
    linear_combination hprod - hp
  · have hp' : eval r (mul b z z) = 1 := by rw [eval_mul b r hr, ← pow_two, hp]
    have hm' : eval (-r) (mul b z z) = 1 := by rw [eval_mul b (-r) hnegroot, ← pow_two, hm]
    let w := mul b z z
    change w.1 + r*w.2 = 1 at hp'
    change w.1 + (-r)*w.2 = 1 at hm'
    have hlin : (2:F)*r*w.2 = 0 := by linear_combination hp' - hm'
    have hzero : w.2 = 0 := (mul_eq_zero.mp hlin).resolve_left (mul_ne_zero h2 hr0)
    apply Prod.ext
    · change w.1 = 1
      simpa [hzero] using hp'
    · exact hzero

/-- Local discrepancy at two consecutive stages forces a factor. -/
theorem adjacent_success {N b a u steps p q : ℕ} [NeZero N] [Fact p.Prime] [Fact q.Prime]
    (hp : p ∣ N) (hq : q ∣ N) (hq2 : (2 : ZMod q) ≠ 0)
    (hnonsquare : ∀ r : ZMod q, r*r ≠ (b : ZMod q))
    (hnorm : ¬q ∣ (norm (b : ZMod N) (-(a : ZMod N), 1)).val)
    (z : ZMod N × ZMod N)
    (hz : z ∈ squareChain (b : ZMod N) (power (b : ZMod N) (-(a : ZMod N), 1) u) steps)
    (hw : mul (b : ZMod N) z z ∈
      squareChain (b : ZMod N) (power (b : ZMod N) (-(a : ZMod N), 1) u) steps)
    (hpz : (map (ZMod.castHom hp (ZMod p)) z).2 ≠ 0)
    (hpw : map (ZMod.castHom hp (ZMod p)) (mul (b : ZMod N) z z) = one) :
    split N b a u steps ≠ none := by
  let w := mul (b : ZMod N) z z
  let P := ZMod.castHom hp (ZMod p)
  let Q := ZMod.castHom hq (ZMod q)
  by_cases hqw : map Q w = one
  · have hsquare : mul (b : ZMod q) (map Q z) (map Q z) = one := by
      rw [← map_natCast Q b, ← map_mul]
      exact hqw
    have hqz := linear_eq_zero_of_nonsquare _ hnonsquare hq2 _ hsquare
    apply split_of_test hq hnorm z hz
    left
    exact candidate_exists hq hp
      ((reduction_eq_zero_iff hq z.2).mp hqz)
      (fun h => hpz ((reduction_eq_zero_iff hp z.2).mpr h))
  · apply split_of_test hq hnorm w hw
    right
    have hp1 : P w.1 = 1 := congrArg Prod.fst hpw
    have hp2 : P w.2 = 0 := congrArg Prod.snd hpw
    have hpdiv1 : p ∣ (w.1 - 1).val :=
      (reduction_eq_zero_iff hp _).mp (by change P (w.1-1)=0; rw [map_sub, hp1, map_one, sub_self])
    have hpdiv2 : p ∣ w.2.val := (reduction_eq_zero_iff hp _).mp hp2
    have hqdiv : ¬q ∣ Nat.gcd (w.1-1).val w.2.val := by
      intro hd
      apply hqw
      apply Prod.ext
      · have hh := (reduction_eq_zero_iff hq (w.1-1)).mpr (hd.trans (Nat.gcd_dvd_left _ _))
        change Q (w.1-1)=0 at hh
        rw [map_sub, map_one, sub_eq_zero] at hh
        exact hh
      · exact (reduction_eq_zero_iff hq w.2).mpr (hd.trans (Nat.gcd_dvd_right _ _))
    exact candidate_exists hp hq (Nat.dvd_gcd hpdiv1 hpdiv2) hqdiv

/-- The successful-norm case (the two split roots of X²-b). -/
theorem norm_root_success {N b a u steps p q : ℕ} [NeZero N] [Fact p.Prime]
    (hp : p ∣ N) (hq : q ∣ N)
    (hpnorm : p ∣ (norm (b : ZMod N) (-(a : ZMod N), 1)).val)
    (hqnorm : ¬q ∣ (norm (b : ZMod N) (-(a : ZMod N), 1)).val) :
    split N b a u steps ≠ none := by
  let n := (norm (b : ZMod N) (-(a : ZMod N), 1)).val
  have hc := candidate_exists hp hq hpnorm hqnorm
  have hg : Nat.gcd n N ≠ 1 := by
    intro h
    apply hc
    simp [gcdCandidate, show Nat.gcd (norm (b : ZMod N) (-(a : ZMod N), 1)).val N = 1 from h]
  change Nat.gcd (norm (b : ZMod N) (-(a : ZMod N), 1)).val N ≠ 1 at hg
  simpa only [split, if_neg hg] using hc

/-- For a stage whose exponent is an odd multiple of (p-1)/2, the negative
Euler sign of the norm gives exactly the needed pair of local signs. -/
theorem euler_stage {p : ℕ} [Fact p.Prime] (hpodd : p % 2 = 1)
    (b r a : ZMod p) (hr : r*r=b) (hr0 : r ≠ 0) (h2 : (2 : ZMod p) ≠ 0)
    (E k : ℕ) (hE : E = (p/2)*(2*k+1))
    (hgood : (a*a-b)^(p/2) = -1) :
    (power b (-a,1) E).2 ≠ 0 ∧
    mul b (power b (-a,1) E) (power b (-a,1) E) = one := by
  have hnr : (-r)*(-r)=b := by rw [neg_mul_neg, hr]
  have hn : norm b (-a,1) = a*a-b := by simp [norm]
  have hn0 : a*a-b ≠ 0 := by
    intro he
    have hpos : 0 < p/2 := by have := (Fact.out : p.Prime).one_lt; omega
    simp [he, zero_pow (ne_of_gt hpos)] at hgood
  have hmul : eval r (-a,1) * eval (-r) (-a,1) ≠ 0 := by
    rw [← split_norm b r hr, hn]
    exact hn0
  have hxp := (mul_ne_zero_iff.mp hmul).1
  have hxm := (mul_ne_zero_iff.mp hmul).2
  have hpow (x : ZMod p) (hx : x ≠ 0) : (x^E)^2 = 1 := by
    rw [← pow_mul, hE, show (p/2*(2*k+1))*2 = (p-1)*(2*k+1) by
      have h : p/2*2=p-1 := by omega
      calc
        _ = (p/2*2)*(2*k+1) := by ring
        _ = _ := by rw [h],
      pow_mul, ZMod.pow_card_sub_one_eq_one hx, one_pow]
  apply opposite_stage b r hr hr0 h2
  · rw [eval_power b r hr]; exact hpow _ hxp
  · rw [eval_power b (-r) hnr]; exact hpow _ hxm
  · rw [eval_power b r hr, eval_power b (-r) hnr, ← mul_pow, ← split_norm b r hr,
      hn, hE, pow_mul, hgood, pow_add, pow_mul, neg_one_sq, one_pow]
    simp

/-- The exponent of two in a positive number with a specified odd part. -/
theorem factor_two_odd (s u : ℕ) (hu : Odd u) :
    (2^s*u).factorization 2 = s := by
  have hn : u ≠ 0 := by obtain ⟨k,hk⟩ := hu; omega
  have hd : ¬2 ∣ u := by obtain ⟨k,hk⟩ := hu; omega
  rw [Nat.factorization_mul (pow_ne_zero _ (by decide : (2:ℕ) ≠ 0)) hn,
    Nat.prime_two.factorization_pow]
  simp [Nat.factorization_eq_zero_of_not_dvd hd]

/-- An even supplied multiple of p-1 has a stage with an odd multiple of
(p-1)/2 as its exponent, and the successor stage is inside the scan. -/
theorem exists_euler_stage {p u steps : ℕ} (hp : 1 < p) (hodd : p%2=1)
    (hu : Odd u) (hdiv : p-1 ∣ 2^steps*u) :
    ∃ j k : ℕ, j < steps ∧ u*2^j=(p/2)*(2*k+1) := by
  obtain ⟨e,m,hm,hpm⟩ := Nat.exists_eq_two_pow_mul_odd (show p-1 ≠ 0 by omega)
  obtain ⟨l,hl⟩ := hdiv
  have hu0 : u ≠ 0 := by obtain ⟨k,hk⟩ := hu; omega
  have hl0 : l ≠ 0 := by
    intro h
    rw [h, mul_zero] at hl
    exact (mul_ne_zero (pow_ne_zero _ (by decide : (2:ℕ) ≠ 0)) hu0) hl
  obtain ⟨f,v,hv,hlv⟩ := Nat.exists_eq_two_pow_mul_odd hl0
  have heq : 2^steps*u=2^(e+f)*(m*v) := by
    rw [hl,hpm,hlv,pow_add]
    ring
  have hf := congrArg (fun n : ℕ => n.factorization 2) heq
  rw [factor_two_odd steps u hu, factor_two_odd (e+f) (m*v) (hm.mul hv)] at hf
  have hueq : u=m*v := by
    rw [← hf] at heq
    exact mul_left_cancel₀ (pow_ne_zero _ (by decide : (2:ℕ) ≠ 0)) heq
  cases e with
  | zero =>
    simp at hpm
    obtain ⟨k,hk⟩ := hm
    omega
  | succ j =>
    have hh : 2*(2^j*m)=p-1 := by rw [hpm,pow_succ]; ring
    have hhalf : p/2=2^j*m := by omega
    obtain ⟨k,hk⟩ := hv
    refine ⟨j,k,by omega,?_⟩
    rw [hueq,hhalf,hk]
    ring

/-- The actual program succeeds on every residue with a zero or nonsquare norm
at the split prime. The exponent parameters are the ordinary odd decomposition
of a positive supplied multiple of p-1. No factorization is an input to split. -/
theorem mixed_success {N b a u steps p q : ℕ} [NeZero N] [Fact p.Prime] [Fact q.Prime]
    (hp : p ∣ N) (hq : q ∣ N) (hpodd : p%2=1)
    (hp2 : (2 : ZMod p) ≠ 0) (hq2 : (2 : ZMod q) ≠ 0)
    (r : ZMod p) (hr : r*r=(b : ZMod p)) (hr0 : r ≠ 0)
    (hnonsquare : ∀ x : ZMod q, x*x ≠ (b : ZMod q))
    (hu : Odd u) (hdiv : p-1 ∣ 2^steps*u)
    (hgood : (a : ZMod p)*(a : ZMod p)-(b : ZMod p) = 0 ∨
      ¬IsSquare ((a : ZMod p)*(a : ZMod p)-(b : ZMod p))) :
    ∃ d, split N b a u steps = some d ∧ 1 < d ∧ d < N ∧ d ∣ N := by
  have norm_reduce (s : ℕ) (hs : s ∣ N) :
      ZMod.castHom hs (ZMod s) (norm (b : ZMod N) (-(a : ZMod N),1)) =
        (a : ZMod s)*(a : ZMod s)-(b : ZMod s) := by
    rw [map_norm]
    simp only [map, map_natCast, map_neg, map_one, norm]
    ring
  have hqnorm : ¬q ∣ (norm (b : ZMod N) (-(a : ZMod N),1)).val := by
    intro h
    have hqz := (reduction_eq_zero_iff hq _).mpr h
    rw [norm_reduce q hq] at hqz
    exact hnonsquare (a : ZMod q) (sub_eq_zero.mp hqz)
  have hsuccess : split N b a u steps ≠ none := by
    rcases hgood with hzero | hns
    · exact norm_root_success hp hq ((reduction_eq_zero_iff hp _).mp
        (by rw [norm_reduce p hp]; exact hzero)) hqnorm
    · have hne : (a : ZMod p)*(a : ZMod p)-(b : ZMod p) ≠ 0 := by
        intro h
        apply hns
        rw [h]
        exact IsSquare.zero
      have hsign := (ZMod.pow_div_two_eq_neg_one_or_one hne).resolve_left
        (fun h => hns ((ZMod.euler_criterion p hne).mpr h))
      obtain ⟨j,k,hj,he⟩ := exists_euler_stage (Fact.out : p.Prime).one_lt hpodd hu hdiv
      let z := power (b : ZMod N) (-(a : ZMod N),1) (u*2^j)
      have hz := stage_mem (b : ZMod N) (-(a : ZMod N),1) u j steps (by omega)
      have hw : mul (b : ZMod N) z z ∈
          squareChain (b : ZMod N) (power (b : ZMod N) (-(a : ZMod N),1) u) steps := by
        have h := stage_mem (b : ZMod N) (-(a : ZMod N),1) u (j+1) steps (by omega)
        rw [pow_succ, show u*(2^j*2)=u*2^j+u*2^j by ring, power_add] at h
        exact h
      let P := ZMod.castHom hp (ZMod p)
      have hzmap : map P z = power (b : ZMod p) (-(a : ZMod p),1) (u*2^j) := by
        unfold z
        rw [map_power]
        simp only [map, map_natCast, map_neg, map_one]
      have hloc := euler_stage hpodd (b : ZMod p) r (a : ZMod p) hr hr0 hp2 _ k he hsign
      apply adjacent_success hp hq hq2 hnonsquare hqnorm z hz hw
      · change (map P z).2 ≠ 0
        rw [hzmap]
        exact hloc.1
      · change map P (mul (b : ZMod N) z z)=one
        rw [map_mul, hzmap, map_natCast]
        exact hloc.2
  cases h : split N b a u steps with
  | none => exact (hsuccess h).elim
  | some d => exact ⟨d,rfl,split_sound h⟩

end Factoring.Quadratic
