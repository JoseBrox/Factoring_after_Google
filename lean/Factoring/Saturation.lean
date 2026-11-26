import Mathlib.FieldTheory.Finite.Basic
import Mathlib.GroupTheory.Index
import Mathlib.Algebra.GCDMonoid.Finset
import Lean.Elab.Tactic.Omega

/-! The finite-group saturation step in the deterministic exponent construction.
The count of distinct small products is an input to the last theorem;
the group/index step does not require knowing the factorization. -/
namespace Factoring.Saturation

variable {G : Type*} [CommGroup G]

def annihilator (E : ℕ) : Subgroup G where
  carrier := {x | x ^ E = 1}
  one_mem' := one_pow _
  mul_mem' := by
    intro a b ha hb
    change (a * b) ^ E = 1
    rw [mul_pow, show a ^ E = 1 from ha, show b ^ E = 1 from hb, one_mul]
  inv_mem' := by
    intro a ha
    change a⁻¹ ^ E = 1
    rw [inv_pow, show a ^ E = 1 from ha, inv_one]

theorem closure_annihilated (s : Set G) (E : ℕ)
    (hs : ∀ x ∈ s, x ^ E = 1) :
    Subgroup.closure s ≤ annihilator E :=
  (Subgroup.closure_le _).mpr hs

def indexMultiple (K : ℕ) : ℕ := (Finset.range (K + 1) |>.erase 0).lcm id

theorem dvd_indexMultiple {i K : ℕ} (hi : 0 < i) (hK : i ≤ K) :
    i ∣ indexMultiple K := by
  unfold indexMultiple
  apply Finset.dvd_lcm
  simp
  omega

theorem index_saturation [Finite G] [IsCyclic G] (H : Subgroup G) (E K : ℕ)
    (hE : H ≤ annihilator E) (hK : H.index ≤ K) :
    Nat.card G ∣ E * indexMultiple K := by
  obtain ⟨g, hg⟩ := IsCyclic.exists_ofOrder_eq_natCard (α := H)
  have hp : g ^ E = 1 := by
    apply Subtype.ext
    exact hE g.property
  have hd : Nat.card H ∣ E := by
    rw [← hg]
    exact orderOf_dvd_of_pow_eq_one hp
  have hi : 0 < H.index := Nat.pos_of_ne_zero H.index_ne_zero_of_finite
  rw [← H.card_mul_index]
  exact Nat.mul_dvd_mul hd (dvd_indexMultiple hi hK)

/-- A lower bound on the subgroup size gives an index cap without division. -/
theorem saturation_from_count [Finite G] [IsCyclic G] (H : Subgroup G) (E K C : ℕ)
    (hE : H ≤ annihilator E) (hC : 0 < C) (hcount : C ≤ Nat.card H)
    (hcap : Nat.card G ≤ K * C) :
    Nat.card G ∣ E * indexMultiple K := by
  apply index_saturation H E K hE
  have hmul : H.index * C ≤ Nat.card G := by
    rw [← H.index_mul_card]
    exact Nat.mul_le_mul_left _ hcount
  exact Nat.le_of_mul_le_mul_right (hmul.trans hcap) hC

/-- Distinct positive integer representatives below p give distinct units.
This is the bridge from an actual set of successful products to saturation. -/
theorem small_products_saturation (p E K : ℕ) [Fact p.Prime]
    (S : Finset ℕ) (hS : S.Nonempty)
    (hsmall : ∀ n ∈ S, 0 < n ∧ n < p)
    (hann : ∀ n ∈ S, (n : ZMod p) ^ E = 1)
    (hcap : p - 1 ≤ K * S.card) :
    p - 1 ∣ E * indexMultiple K := by
  classical
  let H : Subgroup (ZMod p)ˣ := annihilator E
  let f : S → H := fun n =>
    ⟨Units.mk0 (n.1 : ZMod p) (by
        intro hz
        have hz' := (ZMod.natCast_zmod_eq_zero_iff_dvd n.1 p).mp hz
        exact (not_le_of_gt (hsmall n.1 n.2).2)
          (Nat.le_of_dvd (hsmall n.1 n.2).1 hz')),
      by
        change (Units.mk0 (n.1 : ZMod p) _) ^ E = 1
        apply Units.ext
        simpa using hann n.1 n.2⟩
  have hf : Function.Injective f := by
    intro a b hab
    apply Subtype.ext
    have hv : (a.1 : ZMod p) = (b.1 : ZMod p) :=
      congrArg (fun z : H => ((z.1 : (ZMod p)ˣ) : ZMod p)) hab
    have hv' := congrArg ZMod.val hv
    simpa only [ZMod.val_natCast_of_lt (hsmall a.1 a.2).2,
      ZMod.val_natCast_of_lt (hsmall b.1 b.2).2] using hv'
  have hcount : S.card ≤ Nat.card H := by
    rw [Nat.card_eq_fintype_card]
    simpa using Fintype.card_le_of_injective f hf
  have hc : 0 < S.card := Finset.card_pos.mpr hS
  have hcard : Nat.card (ZMod p)ˣ = p - 1 := by
    rw [Nat.card_eq_fintype_card, ZMod.card_units]
  have hh := saturation_from_count H E K S.card le_rfl hc hcount (by rw [hcard]; exact hcap)
  rwa [hcard] at hh

end Factoring.Saturation
