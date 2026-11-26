import Factoring.Prefix
import Factoring.MultisetSaturation
import Mathlib.Data.List.Permutation
import Mathlib.Data.List.OfFn
import Mathlib.Algebra.BigOperators.Fin
import Mathlib.Algebra.BigOperators.Ring.Finset

/-! Ordered prime tuples, not just distinct products. The moment estimate
uses the number of permutations of a list, allowing repeated primes. -/
namespace Factoring.CharacterMoments
open scoped BigOperators
open Factoring.Saturation Factoring.Prefix

def tupleProduct {k : ℕ} {S : Finset ℕ} (x : Fin k → S) : ℕ :=
  ∏ i, (x i).val

theorem tuple_list_perm {k : ℕ} {S : Finset ℕ}
    (hp : ∀ a∈S,a.Prime) (x y : Fin k → S)
    (he : tupleProduct x=tupleProduct y) :
    (List.ofFn (fun i => (x i).val)).Perm (List.ofFn (fun i => (y i).val)) := by
  let a := List.ofFn (fun i => (x i).val)
  let b := List.ofFn (fun i => (y i).val)
  have ha : ∀ n∈(a : Multiset ℕ),n.Prime := by
    intro n hn
    change n∈a at hn
    obtain ⟨i, rfl⟩ := (List.mem_ofFn' _ _).mp hn
    exact hp _ (x i).property
  have hb : ∀ n∈(b : Multiset ℕ),n.Prime := by
    intro n hn
    change n∈b at hn
    obtain ⟨i, rfl⟩ := (List.mem_ofFn' _ _).mp hn
    exact hp _ (y i).property
  have hprod : (a : Multiset ℕ).prod=(b : Multiset ℕ).prod := by
    change a.prod=b.prod
    simpa [a,b,List.prod_ofFn,tupleProduct] using he
  apply Multiset.coe_eq_coe.mp
  apply Multiset.ext'
  intro q
  rw [←prime_prod_factorization _ ha,←prime_prod_factorization _ hb,hprod]

/-- A fibre of the ordered prime-product map has at most k! elements.
Its lists are contained in the permutations of any representative. -/
theorem tuple_fibre_le {k : ℕ} (S : Finset ℕ)
    (hp : ∀ a∈S,a.Prime) (n : ℕ) :
    (Finset.univ.filter (fun x : Fin k → S => tupleProduct x=n)).card ≤ k.factorial := by
  classical
  let T := Finset.univ.filter (fun x : Fin k → S => tupleProduct x=n)
  by_cases hT : T.Nonempty
  · obtain ⟨x,hx⟩ := hT
    let a := List.ofFn (fun i => (x i).val)
    have hx' : tupleProduct x=n := (Finset.mem_filter.mp hx).2
    have hi : T.card ≤ a.permutations.toFinset.card := by
      apply Finset.card_le_card_of_injOn (fun y => List.ofFn (fun i => (y i).val))
      · intro y hy
        apply List.mem_toFinset.mpr
        apply List.mem_permutations.mpr
        exact tuple_list_perm hp y x ((Finset.mem_filter.mp hy).2.trans hx'.symm)
      · intro y hy z hz he
        have hh := List.ofFn_injective he
        funext i
        exact Subtype.ext (congrFun hh i)
    calc
      T.card ≤ a.permutations.toFinset.card := hi
      _ ≤ a.permutations.length := List.toFinset_card_le _
      _ = k.factorial := by simp [a,List.length_permutations]
  · have he : T=∅ := Finset.not_nonempty_iff_eq_empty.mp hT
    change T.card≤k.factorial
    simp [he]

/-- A collision bound for the exact character moment. The only
assumptions are unit residues and injectivity of distinct products.
The phases can be arbitrary unit complex numbers, hence also p^(it). -/
theorem weighted_moment {q k : ℕ} [NeZero q] (S : Finset ℕ)
    (hp : ∀ a∈S,a.Prime) (w : S→ℂ) (hw : ∀ a, ‖w a‖=1)
    (hu : ∀ a : S, IsUnit (a.val : ZMod q))
    (hsmall : ∀ x : Fin k → S, tupleProduct x < q) :
    (∑ χ : DirichletCharacter ℂ q,
        ‖(∑ a:S,w a*χ (a.val:ZMod q))^k‖^2) ≤
      (q.totient:ℝ)*(k.factorial:ℝ)*(S.card:ℝ)^k := by
  classical
  let f : (Fin k → S) → ℕ := tupleProduct
  let T := Finset.univ.image f
  let C (n : ℕ) := Finset.univ.filter (fun x : Fin k → S => f x=n)
  let W (n : ℕ) : ℂ := ∑ x∈C n, ∏ i, w (x i)
  have hmap : (Finset.univ : Finset (Fin k → S)).toSet.MapsTo f T :=
    fun _ _ => Finset.mem_image_of_mem _ (Finset.mem_univ _)
  have hunit : ∀ n∈T, IsUnit (n:ZMod q) := by
    intro n hn
    obtain ⟨x,_,rfl⟩ := Finset.mem_image.mp hn
    change IsUnit ((↑(∏ i, (x i).val)):ZMod q)
    rw [Nat.cast_prod]
    exact IsUnit.prod_univ_iff.mpr (fun i => hu (x i))
  have hinj := nat_prefix_injective (q:=q) T (by
    intro n hn
    obtain ⟨x,_,rfl⟩ := Finset.mem_image.mp hn
    exact hsmall x)
  have hexp (χ : DirichletCharacter ℂ q) :
      (∑ a:S,w a*χ (a.val:ZMod q))^k =
        ∑ n∈T,W n*χ (n:ZMod q) := by
    rw [Fintype.sum_pow]
    simp_rw [Finset.prod_mul_distrib, ← map_prod, ← Nat.cast_prod]
    change (∑ x:Fin k→S,(∏ i,w (x i))*χ (f x:ZMod q)) = _
    rw [← Finset.sum_fiberwise_of_maps_to hmap]
    apply Finset.sum_congr rfl
    intro n hn
    unfold W
    rw [Finset.sum_mul]
    apply Finset.sum_congr rfl
    intro x hx
    rw [(Finset.mem_filter.mp hx).2]
  simp_rw [hexp]
  rw [prefix_parseval T (fun n => (n:ZMod q)) hunit hinj W]
  have hW (n : ℕ) : ‖W n‖ ≤ (C n).card := by
    calc
      ‖W n‖ ≤ ∑ x∈C n, ‖∏ i,w (x i)‖ := norm_sum_le _ _
      _ = (C n).card := by simp [norm_prod,hw]
  have hC (n : ℕ) : (C n).card ≤ k.factorial := tuple_fibre_le S hp n
  have hcard : ∑ n∈T,(C n).card = S.card^k := by
    have h := Finset.card_eq_sum_card_image f Finset.univ
    rw [Finset.card_univ,Fintype.card_pi_const] at h
    simpa [T,C] using h.symm
  have hs : (∑ n∈T,((C n).card:ℝ)) = (S.card:ℝ)^k := by exact_mod_cast hcard
  calc
    _ ≤ (q.totient:ℝ)*(∑ n∈T,(k.factorial:ℝ)*((C n).card:ℝ)) := by
      apply mul_le_mul_of_nonneg_left _ (by positivity)
      apply Finset.sum_le_sum
      intro n hn
      have hc : ((C n).card:ℝ)≤k.factorial := by exact_mod_cast hC n
      have hn0 : 0≤‖W n‖ := norm_nonneg _
      have hc0 : 0≤((C n).card:ℝ) := by positivity
      nlinarith [hW n, mul_le_mul_of_nonneg_right (hW n) hn0,
        mul_le_mul_of_nonneg_left (hW n) hc0,
        mul_le_mul_of_nonneg_right hc hc0]
    _ = _ := by rw [← Finset.mul_sum,hs]; ring

end Factoring.CharacterMoments

#print axioms Factoring.CharacterMoments.tuple_list_perm
#print axioms Factoring.CharacterMoments.tuple_fibre_le
#print axioms Factoring.CharacterMoments.weighted_moment
