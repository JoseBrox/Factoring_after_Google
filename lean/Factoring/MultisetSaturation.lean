import Factoring.PrimeProducts
import Mathlib.Data.Sym.Card
import Mathlib.Data.Nat.Choose.Bounds
import Mathlib.Data.Nat.Log
import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity

/-! The exact multiset count in the deterministic manuscript's subgroup
saturation lemma, followed by the log-scale index inequality and the
common-exponent certificate. The successful-prime density remains a hypothesis. -/
namespace Factoring.Saturation
open scoped BigOperators

theorem prime_prod_pos (s : Multiset ℕ) (hs : ∀ a ∈ s, a.Prime) : 0 < s.prod := by
  induction s using Multiset.induction_on with
  | empty => simp
  | cons a s ih =>
    rw [Multiset.prod_cons]
    exact Nat.mul_pos (hs a (by simp)).pos (ih fun x hx => hs x (by simp [hx]))

theorem prime_prod_factorization (s : Multiset ℕ) (hs : ∀ a ∈ s, a.Prime) (q : ℕ) :
    s.prod.factorization q = s.count q := by
  induction s using Multiset.induction_on with
  | empty => simp [Nat.factorization_one]
  | cons a s ih =>
    have ha := hs a (by simp)
    have htail : ∀ x ∈ s, x.Prime := fun x hx => hs x (by simp [hx])
    rw [Multiset.prod_cons, Nat.factorization_mul ha.ne_zero
      (ne_of_gt (prime_prod_pos s htail)), Finsupp.add_apply, ha.factorization,
      ih htail, Multiset.count_cons]
    simp [Finsupp.single_apply, eq_comm, add_comm]

theorem multiset_product_bound (s : Multiset ℕ) (B : ℕ)
    (hs : ∀ a ∈ s, a ≤ B) : s.prod ≤ B^s.card := by
  induction s using Multiset.induction_on with
  | empty => simp
  | cons a s ih =>
    rw [Multiset.prod_cons, Multiset.card_cons, pow_succ, mul_comm (B^s.card) B]
    exact Nat.mul_le_mul (hs a (by simp)) (ih fun x hx => hs x (by simp [hx]))

theorem multiset_product_annihilated {p E : ℕ} (s : Multiset ℕ)
    (hs : ∀ a ∈ s, (a : ZMod p)^E=1) : (s.prod : ZMod p)^E=1 := by
  induction s using Multiset.induction_on with
  | empty => simp
  | cons a s ih =>
    rw [Multiset.prod_cons, Nat.cast_mul, mul_pow, hs a (by simp),
      ih (fun x hx => hs x (by simp [hx])), one_mul]

/-- Products of multisets (not ordered tuples) give exactly the stars-and-bars
lower bound, even if a prime appears more than once in a product. -/
theorem multiset_saturation {p E K B k : ℕ} [Fact p.Prime] (S : Finset ℕ)
    (hS : S.Nonempty) (hp : ∀ n ∈ S, n.Prime) (hB : ∀ n ∈ S, n≤B)
    (hpow : B^k<p) (hE : ∀ n ∈ S, (n : ZMod p)^E=1)
    (hcap : p-1 ≤ K*(S.card+k-1).choose k) :
    p-1 ∣ E*indexMultiple K := by
  classical
  let f (x : Sym S k) : ℕ := ((x : Multiset S).map Subtype.val).prod
  have hpr (x : Sym S k) : ∀ n ∈ (x : Multiset S).map Subtype.val, n.Prime := by
    intro n hn
    obtain ⟨a,_,rfl⟩ := Multiset.mem_map.mp hn
    exact hp a.val a.property
  have hf : Function.Injective f := by
    intro x y he
    apply Sym.ext
    apply Multiset.map_injective (f := (Subtype.val : S→ℕ)) Subtype.val_injective
    apply Multiset.ext'
    intro q
    rw [← prime_prod_factorization _ (hpr x), ← prime_prod_factorization _ (hpr y)]
    exact congrArg (fun n : ℕ => n.factorization q) he
  let T := Finset.univ.image f
  have hcard : T.card = (S.card+k-1).choose k := by
    unfold T
    rw [Finset.card_image_of_injective _ hf, Finset.card_univ, Sym.card_sym_eq_choose]
    simp
  have hT : T.Nonempty := by
    obtain ⟨a,ha⟩ := hS
    exact ⟨f (Sym.replicate k ⟨a,ha⟩), Finset.mem_image.mpr ⟨_,by simp,rfl⟩⟩
  apply small_products_saturation p E K T hT
  · intro n hn
    obtain ⟨x,_,rfl⟩ := Finset.mem_image.mp hn
    refine ⟨prime_prod_pos _ (hpr x), ?_⟩
    apply lt_of_le_of_lt _ hpow
    unfold f
    have hh := multiset_product_bound ((x : Multiset S).map Subtype.val) B (by
      intro n hn
      obtain ⟨a,_,rfl⟩ := Multiset.mem_map.mp hn
      exact hB a.val a.property)
    simpa only [Multiset.card_map, Sym.card_coe] using hh
  · intro n hn
    obtain ⟨x,_,rfl⟩ := Finset.mem_image.mp hn
    apply multiset_product_annihilated
    intro n hn
    obtain ⟨a,_,rfl⟩ := Multiset.mem_map.mp hn
    exact hE a.val a.property
  · rwa [hcard]

/-- The binomial estimate in the manuscript, with no flooring loss. -/
theorem multichoose_lower {s k : ℕ} (hs : 0<s) (hk : 0<k) :
    ((s:ℝ)/k)^k ≤ ((s+k-1).choose k : ℝ) := by
  have h := Nat.pow_le_choose (α := ℝ) k (s+k-1)
  rw [show s+k-1+1-k=s by omega] at h
  have hf : (k.factorial : ℝ) ≤ (k:ℝ)^k := by exact_mod_cast Nat.factorial_le_pow k
  have hk' : 0 < (k:ℝ)^k := by positivity
  rw [div_pow]
  exact (div_le_div_of_nonneg_left (by positivity) (by positivity) hf).trans h

/-- LCM(1,...,K) is bounded by K!, which suffices for the same
asymptotic exponent as the manuscript's sharper Chebyshev estimate. -/
theorem indexMultiple_dvd_factorial (K : ℕ) : indexMultiple K ∣ K.factorial := by
  unfold indexMultiple
  apply Finset.lcm_dvd
  intro i hi
  simp at hi
  exact Nat.dvd_factorial (by omega) (by omega)

theorem indexMultiple_pos (K : ℕ) : 0 < indexMultiple K := by
  by_contra h
  have he : indexMultiple K = 0 := by omega
  have hd := indexMultiple_dvd_factorial K
  rw [he, zero_dvd_iff] at hd
  exact (Nat.factorial_ne_zero K) hd

theorem indexMultiple_log_bound (K : ℕ) (hK : 0<K) :
    Real.log (indexMultiple K : ℝ) ≤ (K:ℝ)*Real.log K := by
  have h : indexMultiple K ≤ K^K :=
    (Nat.le_of_dvd (Nat.factorial_pos K) (indexMultiple_dvd_factorial K)).trans
      (Nat.factorial_le_pow K)
  have hh := Real.log_le_log (show (0:ℝ)<indexMultiple K by exact_mod_cast indexMultiple_pos K)
      (show (indexMultiple K:ℝ) ≤ (K:ℝ)^K by exact_mod_cast h)
  rwa [Real.log_pow] at hh

/-- Verified individual modular powers yield their common least multiple. -/
theorem lcm_certificate {N : ℕ} (S : Finset ℕ) (e : ℕ→ℕ)
    (h : ∀ a ∈ S, (a : ZMod N)^(e a)=1) :
    ∀ a ∈ S, (a : ZMod N)^(S.lcm e)=1 := by
  intro a ha
  obtain ⟨k,hk⟩ := (Finset.dvd_lcm (f := e) ha : e a ∣ S.lcm e)
  rw [hk,pow_mul,h a ha,one_pow]

/-- All unknown prime factors are covered by a single computed order
multiple. The size and exponent guards are visible, rather than
requiring the program to know the hidden primes. -/
theorem all_prime_order_multiple {N B K : ℕ} (S : Finset ℕ) (e : ℕ→ℕ)
    (hS : S.Nonempty) (hp : ∀ n ∈ S, n.Prime) (hB : ∀ n ∈ S, n≤B)
    (hcert : ∀ n ∈ S, (n : ZMod N)^(e n)=1)
    (hguard : ∀ p : ℕ, p.Prime → p∣N →
      B^(Nat.log B (p-1))<p ∧
      p-1 ≤ K*(S.card+Nat.log B (p-1)-1).choose (Nat.log B (p-1))) :
    ∀ p : ℕ, p.Prime → p∣N → p-1 ∣ S.lcm e*indexMultiple K := by
  intro p hprime hdiv
  letI : Fact p.Prime := ⟨hprime⟩
  obtain ⟨hpow,hcap⟩ := hguard p hprime hdiv
  apply multiset_saturation S hS hp hB hpow _ hcap
  intro n hn
  let f := ZMod.castHom hdiv (ZMod p)
  have hh := congrArg f (lcm_certificate S e hcert n hn)
  simpa only [map_pow,map_natCast,map_one] using hh

end Factoring.Saturation
