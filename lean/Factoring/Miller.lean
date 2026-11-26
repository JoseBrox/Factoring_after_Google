import Factoring.ChainTrial

/-! The scalar order test from the supplied-order splitting proof.
The two primes and their Euler signs are used only in the correctness
argument; the executable scan uses only N, a and the supplied exponent. -/

namespace Factoring.Miller

open Factoring.Quadratic

theorem indexed_euler_stage {p u steps : ℕ} (hp : 1 < p) (hodd : p%2=1)
    (hu : Odd u) (hdiv : p-1 ∣ 2^steps*u) :
    ∃ j k : ℕ, j < steps ∧ j+1=(p-1).factorization 2 ∧ u*2^j=(p/2)*(2*k+1) := by
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
  dsimp only at hf
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
    refine ⟨j,k,by omega,?_,?_⟩
    · rw [hpm,factor_two_odd _ _ hm]
    · rw [hueq,hhalf,hk]
      ring

/-- A scalar gcd scan, using the already verified binary power and
successive-square operations (with zero linear coordinate). -/
def scan (N a u steps : ℕ) : Option ℕ :=
  scanGcd N (a :: (squareChain (0 : ZMod N)
    (power (0 : ZMod N) ((a : ZMod N), 0) u) steps).map
      (fun z => (z.1-1).val))

theorem scan_sound {N a u steps d : ℕ}
    (h : scan N a u steps = some d) : 1<d ∧ d<N ∧ d∣N :=
  scanGcd_sound N _ h

/-- A single stage at which one prime sees 1 and another does not
forces a proper gcd. This remains true for repeated prime powers. -/
theorem discrepancy {N a u steps p q j : ℕ} [NeZero N] [Fact p.Prime]
    (hp : p∣N) (hq : q∣N) (hj : j≤steps)
    (hP : (a : ZMod p)^(u*2^j)=1)
    (hQ : (a : ZMod q)^(u*2^j)≠1) :
    scan N a u steps ≠ none := by
  let z := power (0 : ZMod N) ((a : ZMod N),0) (u*2^j)
  have hz := stage_mem (0 : ZMod N) ((a : ZMod N),0) u j steps hj
  have hfst : z.1 = (a : ZMod N)^(u*2^j) := by
    have hh := eval_power (0 : ZMod N) 0 (by simp)
      ((a : ZMod N),0) (u*2^j)
    simpa [z,eval] using hh
  have ha : p∣(z.1-1).val := by
    apply (reduction_eq_zero_iff hp _).mp
    rw [hfst,map_sub,map_pow,map_natCast,map_one,hP,sub_self]
  have hb : ¬q∣(z.1-1).val := by
    intro h
    have hh := (reduction_eq_zero_iff hq _).mpr h
    rw [hfst,map_sub,map_pow,map_natCast,map_one,sub_eq_zero] at hh
    exact hQ hh
  intro h
  have hs := (scanGcd_none_iff N _).mp h
  apply candidate_exists hp hq ha hb
  apply hs
  exact List.mem_cons_of_mem _ (List.mem_map.mpr ⟨z,hz,rfl⟩)

/-- Euler's criterion transports to every odd multiple of its exponent. -/
theorem odd_sign {R : Type*} [CommRing R] (x : R) (n k : ℕ)
    (h : x^n = -1) : x^(n*(2*k+1)) = -1 := by
  rw [pow_mul,h,pow_add,pow_mul,neg_one_sq,one_pow,_root_.one_mul,pow_one]

/-- Same two-adic valuation and opposite Euler signs imply success. -/
theorem opposite_sign_success {N a u steps p q : ℕ} [NeZero N]
    [Fact p.Prime] [Fact q.Prime]
    (hp : p∣N) (hq : q∣N) (hpodd : p%2=1) (hqodd : q%2=1)
    (hu : Odd u) (hMp : p-1∣2^steps*u) (hMq : q-1∣2^steps*u)
    (heq : (p-1).factorization 2 = (q-1).factorization 2)
    (hP : (a : ZMod p)^(p/2)=1) (hQ : (a : ZMod q)^(q/2) = -1)
    (hq2 : (2 : ZMod q)≠0) :
    scan N a u steps ≠ none := by
  obtain ⟨i,k,hi,hip,hik⟩ := indexed_euler_stage (Fact.out : p.Prime).one_lt hpodd hu hMp
  obtain ⟨j,l,hj,hjq,hjl⟩ := indexed_euler_stage (Fact.out : q.Prime).one_lt hqodd hu hMq
  have hji : j=i := by omega
  subst j
  apply discrepancy hp hq (show i≤steps by omega)
  · rw [hik,pow_mul,hP,one_pow]
  · rw [hjl,odd_sign _ _ _ hQ]
    intro hh
    apply hq2
    linear_combination -hh

/-- Once an Euler stage for a prime has been passed, every later
stage is a multiple of p-1. -/
theorem later_multiple {p u j k i : ℕ} (hp : 1<p) (hodd : p%2=1)
    (he : u*2^j=(p/2)*(2*k+1)) (hji : j < i) :
    p-1∣u*2^i := by
  have hh : 2*(p/2)=p-1 := by omega
  have hj : u*2^(j+1) = (p-1)*(2*k+1) := by
    rw [pow_succ,←Nat.mul_assoc,he,←hh]
    ring
  refine ⟨(2*k+1)*2^(i-(j+1)),?_⟩
  calc
    u*2^i = u*2^((j+1)+(i-(j+1))) := by
      have hi : i = (j+1)+(i-(j+1)) := by omega
      exact congrArg (fun n : ℕ => u*2^n) hi
    _ = (u*2^(j+1))*2^(i-(j+1)) := by rw [pow_add]; ring
    _ = _ := by rw [hj]; ring

/-- When the two-adic valuation is larger at q, a nonsquare Euler sign
at q supplies a witness regardless of the Euler sign at p. -/
theorem unequal_valuation_success {N a u steps p q : ℕ} [NeZero N]
    [Fact p.Prime] [Fact q.Prime]
    (hp : p∣N) (hq : q∣N) (hpodd : p%2=1) (hqodd : q%2=1)
    (hu : Odd u) (hMp : p-1∣2^steps*u) (hMq : q-1∣2^steps*u)
    (hlt : (p-1).factorization 2 < (q-1).factorization 2)
    (ha : (a : ZMod p)≠0) (hQ : (a : ZMod q)^(q/2) = -1)
    (hq2 : (2 : ZMod q)≠0) :
    scan N a u steps ≠ none := by
  obtain ⟨i,k,hi,hip,hik⟩ := indexed_euler_stage (Fact.out : p.Prime).one_lt hpodd hu hMp
  obtain ⟨j,l,hj,hjq,hjl⟩ := indexed_euler_stage (Fact.out : q.Prime).one_lt hqodd hu hMq
  have hij : i < j := by omega
  apply discrepancy hp hq (show j≤steps by omega)
  · obtain ⟨m,hm⟩ := later_multiple (Fact.out : p.Prime).one_lt hpodd hik hij
    rw [hm,pow_mul,ZMod.pow_card_sub_one_eq_one ha,one_pow]
  · rw [hjl,odd_sign _ _ _ hQ]
    intro hh
    apply hq2
    linear_combination -hh

/-- Use the supplied exponent directly; the program does not know p or q. -/
def scanM (N a M : ℕ) : Option ℕ :=
  scan N a (decompose M).2 (decompose M).1

theorem scanM_sound {N a M d : ℕ} (h : scanM N a M=some d) :
    1<d ∧ d<N ∧ d∣N := scan_sound h

/-- If a square at p and a nonsquare at q have equal two-adic orders,
the scalar test finds a factor. The unit hypothesis is local. -/
theorem mixed_equal_success {N a M p q : ℕ} [NeZero N]
    [Fact p.Prime] [Fact q.Prime]
    (hp : p∣N) (hq : q∣N) (hpodd : p%2=1) (hqodd : q%2=1)
    (hM : 0<M) (hMp : p-1∣M) (hMq : q-1∣M)
    (heq : (p-1).factorization 2 = (q-1).factorization 2)
    (ha : (a : ZMod p)≠0) (hP : IsSquare (a : ZMod p))
    (hQ : ¬IsSquare (a : ZMod q)) (hq2 : (2 : ZMod q)≠0) :
    scanM N a M ≠ none := by
  have hdec := decompose_correct hM
  have hq0 : (a : ZMod q)≠0 := by
    intro hh
    apply hQ
    rw [hh]
    exact IsSquare.zero
  have hsign := (ZMod.pow_div_two_eq_neg_one_or_one q hq0).resolve_left
    (fun h => hQ ((ZMod.euler_criterion q hq0).mpr h))
  apply opposite_sign_success hp hq hpodd hqodd hdec.1
    (hdec.2 ▸ hMp) (hdec.2 ▸ hMq) heq
    ((ZMod.euler_criterion p ha).mp hP) hsign hq2

/-- If the two-adic valuations differ, a nonsquare at the larger one
forces the scalar test to succeed. -/
theorem nonsquare_larger_success {N a M p q : ℕ} [NeZero N]
    [Fact p.Prime] [Fact q.Prime]
    (hp : p∣N) (hq : q∣N) (hpodd : p%2=1) (hqodd : q%2=1)
    (hM : 0<M) (hMp : p-1∣M) (hMq : q-1∣M)
    (hlt : (p-1).factorization 2 < (q-1).factorization 2)
    (ha : (a : ZMod p)≠0) (hQ : ¬IsSquare (a : ZMod q))
    (hq2 : (2 : ZMod q)≠0) :
    scanM N a M ≠ none := by
  have hdec := decompose_correct hM
  have hq0 : (a : ZMod q)≠0 := by
    intro hh
    apply hQ
    rw [hh]
    exact IsSquare.zero
  have hsign := (ZMod.pow_div_two_eq_neg_one_or_one q hq0).resolve_left
    (fun h => hQ ((ZMod.euler_criterion q hq0).mpr h))
  exact unequal_valuation_success hp hq hpodd hqodd hdec.1
    (hdec.2 ▸ hMp) (hdec.2 ▸ hMq) hlt ha hsign hq2

end Factoring.Miller
