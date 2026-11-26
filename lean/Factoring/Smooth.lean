import Factoring.MultisetSaturation
import Mathlib.NumberTheory.SmoothNumbers

/-! A certified lower bound for the actual smooth-integer counting function,
including the exclusion of rational primes dividing a modulus. -/
namespace Factoring.Smooth
open scoped BigOperators
open Factoring.Saturation

def coprimeSmooth (X Y q : ℕ) : Finset ℕ :=
  (Nat.smoothNumbersUpTo X (Y+1)).filter fun n => Nat.Coprime n q

/-- Products of k primes (repetition allowed) give the manuscript's
stars-and-bars count. This counts actual positive integers, not tuples. -/
theorem multiset_lower {X Y q k : ℕ} (S : Finset ℕ)
    (hp : ∀ a∈S,a.Prime) (hY : ∀ a∈S,a≤Y)
    (hc : ∀ a∈S,Nat.Coprime a q) (hpow : Y^k≤X) :
    (S.card+k-1).choose k ≤ (coprimeSmooth X Y q).card := by
  classical
  let f (x : Sym S k) : ℕ := ((x:Multiset S).map Subtype.val).prod
  have hpr (x : Sym S k) : ∀ a∈(x:Multiset S).map Subtype.val,a.Prime := by
    intro a ha
    obtain ⟨n,_,rfl⟩ := Multiset.mem_map.mp ha
    exact hp n.1 n.2
  have hf : Function.Injective f := by
    intro x y he
    apply Sym.ext
    apply Multiset.map_injective (f := (Subtype.val : S→ℕ)) Subtype.val_injective
    apply Multiset.ext'
    intro a
    rw [←prime_prod_factorization _ (hpr x),←prime_prod_factorization _ (hpr y)]
    exact congrArg (fun n:ℕ => n.factorization a) he
  have hmem (x : Sym S k) : f x∈coprimeSmooth X Y q := by
    apply Finset.mem_filter.mpr
    constructor
    · apply Nat.mem_smoothNumbersUpTo.mpr
      constructor
      · apply le_trans _ hpow
        have hh := multiset_product_bound ((x:Multiset S).map Subtype.val) Y (by
          intro a ha
          obtain ⟨n,_,rfl⟩ := Multiset.mem_map.mp ha
          exact hY n.1 n.2)
        simpa only [f,Multiset.card_map,Sym.card_coe] using hh
      · apply Nat.mem_smoothNumbers'.mpr
        intro a ha hd
        have hpos : f x ≠ 0 := (prime_prod_pos _ (hpr x)).ne'
        have hh := (ha.dvd_iff_one_le_factorization hpos).mp hd
        change 1≤(((x:Multiset S).map Subtype.val).prod).factorization a at hh
        rw [prime_prod_factorization _ (hpr x)] at hh
        have ham := Multiset.count_pos.mp (by omega : 0<((x:Multiset S).map Subtype.val).count a)
        obtain ⟨n,_,rfl⟩ := Multiset.mem_map.mp ham
        exact Nat.lt_succ_of_le (hY n.1 n.2)
    · have haux (t : Multiset ℕ) (ht:∀ a∈t,Nat.Coprime a q) : Nat.Coprime t.prod q := by
        induction t using Multiset.induction_on with
        | empty => simp
        | cons a t ih =>
          rw [Multiset.prod_cons]
          exact (ht a (by simp)).mul_left (ih fun n hn=>ht n (by simp [hn]))
      exact haux _ (by
        intro a ha
        obtain ⟨n,_,rfl⟩ := Multiset.mem_map.mp ha
        exact hc n.1 n.2)
  have hcard : Fintype.card (Sym S k) ≤ (coprimeSmooth X Y q).card := by
    let g : Sym S k → coprimeSmooth X Y q := fun x => ⟨f x,hmem x⟩
    simpa using Fintype.card_le_of_injective g
      (fun _ _ h => hf (congrArg Subtype.val h))
  rw [Sym.card_sym_eq_choose] at hcard
  simpa using hcard

theorem quantitative_lower {X Y q k : ℕ} (S : Finset ℕ)
    (hk : 0<k) (hS : S.Nonempty)
    (hp : ∀ a∈S,a.Prime) (hY : ∀ a∈S,a≤Y)
    (hc : ∀ a∈S,Nat.Coprime a q) (hpow : Y^k≤X) :
    ((S.card:ℝ)/k)^k ≤ ((coprimeSmooth X Y q).card:ℝ) :=
  (multichoose_lower (Finset.card_pos.mpr hS) hk).trans
    (by exact_mod_cast multiset_lower S hp hY hc hpow)

end Factoring.Smooth
