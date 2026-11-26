import Factoring.Saturation
import Mathlib.Data.Nat.Factorization.Basic
import Mathlib.Data.Fintype.BigOperators
import Mathlib.Data.Fintype.EquivFin
import Mathlib.Tactic.Ring

/-! A concrete way to count small distinct prime products: use disjoint
blocks of primes. It avoids ordered-tuple overcounting. -/
namespace Factoring.Saturation
open scoped BigOperators

theorem block_products_injective {k m : ℕ} (P : Fin k → Fin m → ℕ)
    (hp : ∀ i j, (P i j).Prime)
    (hinj : Function.Injective (fun x : Fin k×Fin m => P x.1 x.2)) :
    Function.Injective (fun f : Fin k → Fin m => ∏ i, P i (f i)) := by
  classical
  intro f g hfg
  funext i
  by_contra hne
  let q := P i (f i)
  have hleft : (∏ j, P j (f j)).factorization q = 1 := by
    rw [Nat.factorization_prod (fun j _ => (hp j (f j)).ne_zero), Finsupp.finset_sum_apply]
    simp_rw [(hp _ _).factorization, Finsupp.single_apply]
    rw [Finset.sum_eq_single i]
    · simp [q]
    · intro j _ hj
      have h : P j (f j) ≠ q := by
        intro he
        have ht := hinj (show P j (f j)=P i (f i) from he)
        exact hj (congrArg Prod.fst ht)
      simp [h,Ne.symm h]
    · simp
  have hright : (∏ j, P j (g j)).factorization q = 0 := by
    rw [Nat.factorization_prod (fun j _ => (hp j (g j)).ne_zero), Finsupp.finset_sum_apply]
    simp_rw [(hp _ _).factorization,Finsupp.single_apply]
    apply Finset.sum_eq_zero
    intro j _
    have h : P j (g j) ≠ q := by
      intro he
      have ht := hinj (show P j (g j)=P i (f i) from he)
      have hji := congrArg Prod.fst ht
      subst j
      exact hne (congrArg Prod.snd ht).symm
    simp [h,Ne.symm h]
  rw [hfg,hright] at hleft
  contradiction

/-- From k disjoint blocks of m successful primes at most B, obtain m^k
distinct positive annihilated products below p, hence a usable order multiple. -/
theorem block_saturation {p E K B k m : ℕ} [Fact p.Prime] (hm : 0<m)
    (P : Fin k → Fin m → ℕ) (hp : ∀ i j, (P i j).Prime)
    (hinj : Function.Injective (fun x : Fin k×Fin m => P x.1 x.2))
    (hB : ∀ i j, P i j ≤ B) (hpow : B^k<p)
    (hE : ∀ i j, (P i j : ZMod p)^E=1)
    (hK : p-1 ≤ K*m^k) :
    p-1 ∣ E*indexMultiple K := by
  classical
  let f := fun x : Fin k → Fin m => ∏ i, P i (x i)
  let S := Finset.univ.image f
  have hcard : S.card=m^k := by
    unfold S
    rw [Finset.card_image_of_injective _ (block_products_injective P hp hinj)]
    simp [Fintype.card_pi_const]
  apply small_products_saturation p E K S (Finset.card_pos.mp (by rw [hcard]; positivity))
  · intro n hn
    obtain ⟨x,_,rfl⟩ := Finset.mem_image.mp hn
    refine ⟨Finset.prod_pos fun i _ => (hp i (x i)).pos,?_⟩
    apply lt_of_le_of_lt _ hpow
    calc
      _ ≤ ∏ _ : Fin k, B := Finset.prod_le_prod' fun i _ => hB i (x i)
      _ = B^k := by simp
  · intro n hn
    obtain ⟨x,_,rfl⟩ := Finset.mem_image.mp hn
    simp only [f,Nat.cast_prod,Finset.prod_pow]
    simp [hE]
  · rwa [hcard]

/-- The blocks can be chosen from any finite successful-prime set with
at least k*m elements; no additional combinatorial assumption is needed. -/
theorem prime_set_saturation {p E K B k m : ℕ} [Fact p.Prime] (hm : 0<m)
    (S : Finset ℕ) (hcard : k*m ≤ S.card)
    (hp : ∀ n ∈ S, n.Prime) (hB : ∀ n ∈ S, n ≤ B)
    (hpow : B^k<p) (hE : ∀ n ∈ S, (n : ZMod p)^E=1)
    (hK : p-1 ≤ K*m^k) :
    p-1 ∣ E*indexMultiple K := by
  classical
  let e : Fin k×Fin m ↪ S := (Fintype.equivFin (Fin k×Fin m)).toEmbedding.trans
    ((Fin.castLEEmb (by simpa using hcard)).trans S.equivFin.symm.toEmbedding)
  let P (i : Fin k) (j : Fin m) := (e (i,j)).1
  exact block_saturation hm P
    (fun i j => hp _ (e (i,j)).2)
    (fun _ _ h => e.injective (Subtype.ext h))
    (fun i j => hB _ (e (i,j)).2) hpow
    (fun i j => hE _ (e (i,j)).2) hK

end Factoring.Saturation
