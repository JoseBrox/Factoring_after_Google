import Factoring.Prefix
import Mathlib.Algebra.Order.BigOperators.Ring.Finset
import Mathlib.Analysis.SpecialFunctions.Exp
import Mathlib.Tactic

/-! Exact two-prefix L²-to-L¹ transfer and a terminal Euler-product
bound independent of any exceptional-conductor classification. -/
namespace Factoring.PrefixBounds
open scoped BigOperators

theorem unit_card {q : ℕ} [NeZero q] {I : Type*}
    (s : Finset I) (r : I→ZMod q) (hu : ∀ i∈s,IsUnit (r i))
    (hinj : Set.InjOn r (s:Set I)) : s.card≤q.totient := by
  classical
  let f : s → (ZMod q)ˣ := fun i => (hu i i.property).unit
  have hf : Function.Injective f := by
    intro a b he
    apply Subtype.ext
    apply hinj a.property b.property
    have h := congrArg (fun z : (ZMod q)ˣ => (z : ZMod q)) he
    simpa [f,IsUnit.unit_spec] using h
  have h := Fintype.card_le_of_injective f hf
  simpa [ZMod.card_units_eq_totient] using h

noncomputable def charSum {q : ℕ} [NeZero q] {I : Type*}
    (s : Finset I) (r : I→ZMod q) (w : I→ℂ) (χ : DirichletCharacter ℂ q) : ℂ :=
  ∑ i∈s,w i*χ (r i)

theorem prefix_L2 {q : ℕ} [NeZero q] {I : Type*}
    (s : Finset I) (r : I→ZMod q) (w : I→ℂ)
    (hu : ∀ i∈s,IsUnit (r i)) (hinj : Set.InjOn r (s:Set I))
    {M : ℝ} (hM : 0≤M) (hw : ∀ i∈s,‖w i‖≤M) :
    (∑ χ : DirichletCharacter ℂ q, ‖charSum s r w χ‖^2) ≤
      (q.totient:ℝ)^2*M^2 := by
  classical
  unfold charSum
  rw [Factoring.Prefix.prefix_parseval s r hu hinj w]
  have hc : (s.card:ℝ)≤q.totient := by exact_mod_cast unit_card s r hu hinj
  have hs : (∑ i∈s,‖w i‖^2)≤(s.card:ℝ)*M^2 := by
    calc
      _ ≤ ∑ _i∈s,M^2 := Finset.sum_le_sum fun i hi => by
        nlinarith [norm_nonneg (w i),mul_nonneg (sub_nonneg.mpr (hw i hi)) (add_nonneg hM (norm_nonneg (w i)))]
      _ = _ := by simp
  calc
    _ ≤ (q.totient:ℝ)*((s.card:ℝ)*M^2) :=
      mul_le_mul_of_nonneg_left hs (by positivity)
    _ ≤ (q.totient:ℝ)*((q.totient:ℝ)*M^2) :=
      mul_le_mul_of_nonneg_left (mul_le_mul_of_nonneg_right hc (sq_nonneg _)) (by positivity)
    _ = _ := by ring

/-- A shortest prefix's quotient before its last prime is less than q.
Multiplying those representatives by a fixed unit preserves injectivity. -/
theorem final_prime_inj {q : ℕ} [NeZero q] (s : Finset ℕ) (a : ZMod q)
    (ha : IsUnit a) (h : ∀ i∈s,i<q) :
    Set.InjOn (fun i:ℕ => a*(i:ZMod q)) (s:Set ℕ) := by
  intro i hi j hj he
  apply Factoring.Prefix.nat_prefix_injective s h hi hj
  obtain ⟨u,rfl⟩ := ha
  have he' := congrArg (fun z : ZMod q => (↑u⁻¹:ZMod q)*z) he
  simpa only [←mul_assoc,Units.inv_mul,one_mul] using he'

theorem two_prefix {q : ℕ} [NeZero q] {I J : Type*}
    (s : Finset I) (r : I→ZMod q) (w : I→ℂ)
    (t : Finset J) (v : J→ZMod q) (z : J→ℂ)
    (hu : ∀ i∈s,IsUnit (r i)) (hv : ∀ j∈t,IsUnit (v j))
    (hi : Set.InjOn r (s:Set I)) (hj : Set.InjOn v (t:Set J))
    {M N : ℝ} (hM : 0≤M) (hN : 0≤N)
    (hw : ∀ i∈s,‖w i‖≤M) (hz : ∀ j∈t,‖z j‖≤N) :
    (∑ χ : DirichletCharacter ℂ q,‖charSum s r w χ * charSum t v z χ‖)
        ≤ (q.totient:ℝ)^2*M*N := by
  classical
  let A := fun χ : DirichletCharacter ℂ q => ‖charSum s r w χ‖
  let B := fun χ : DirichletCharacter ℂ q => ‖charSum t v z χ‖
  have hA := prefix_L2 s r w hu hi hM hw
  have hB := prefix_L2 t v z hv hj hN hz
  have hcs := Finset.sum_mul_sq_le_sq_mul_sq Finset.univ A B
  have ha : 0≤∑ χ,A χ^2 := Finset.sum_nonneg fun _ _=>sq_nonneg _
  have hb : 0≤∑ χ,B χ^2 := Finset.sum_nonneg fun _ _=>sq_nonneg _
  have he : (∑ χ,A χ*B χ)^2≤((q.totient:ℝ)^2*M*N)^2 := by
    refine hcs.trans ?_
    calc
      _ ≤ ((q.totient:ℝ)^2*M^2)*((q.totient:ℝ)^2*N^2) :=
        mul_le_mul hA hB hb (by positivity)
      _ = _ := by ring
  have hpos : 0≤(q.totient:ℝ)^2*M*N := by positivity
  have hsum : (∑ χ,A χ*B χ)≤(q.totient:ℝ)^2*M*N := by
    by_contra! h
    nlinarith [mul_pos (sub_pos.mpr h) (add_pos_of_pos_of_nonneg (hpos.trans_lt h) hpos)]
  simpa only [A,B,norm_mul] using hsum

/-- The useful normalized form: the number of characters costs
q*φ(q), not q times another independent character count. -/
theorem normalized_two_prefix {q : ℕ} [NeZero q] {I J : Type*}
    (s : Finset I) (r : I→ZMod q) (w : I→ℂ)
    (t : Finset J) (v : J→ZMod q) (z : J→ℂ)
    (hu : ∀ i∈s,IsUnit (r i)) (hv : ∀ j∈t,IsUnit (v j))
    (hi : Set.InjOn r (s:Set I)) (hj : Set.InjOn v (t:Set J))
    {M N : ℝ} (hM : 0≤M) (hN : 0≤N)
    (hw : ∀ i∈s,‖w i‖≤M) (hz : ∀ j∈t,‖z j‖≤N) :
    (q:ℝ)/(q.totient:ℝ) *
      (∑ χ : DirichletCharacter ℂ q,‖charSum s r w χ * charSum t v z χ‖)
        ≤ (q:ℝ)^2*M*N := by
  have h := two_prefix s r w t v z hu hv hi hj hM hN hw hz
  have hp : 0<(q.totient:ℝ) := by exact_mod_cast Nat.totient_pos.mpr (NeZero.pos q)
  have hq : (q.totient:ℝ)≤q := by exact_mod_cast Nat.totient_le q
  calc
    _ ≤ (q:ℝ)/(q.totient:ℝ)*((q.totient:ℝ)^2*M*N) :=
      mul_le_mul_of_nonneg_left h (by positivity)
    _ = (q:ℝ)*(q.totient:ℝ)*M*N := by field_simp; ring
    _ ≤ _ := by
      rw [pow_two]
      exact mul_le_mul_of_nonneg_right
        (mul_le_mul_of_nonneg_right (mul_le_mul_of_nonneg_left hq (by positivity)) hM) hN

/-- No logarithm of a possibly zero local Euler factor is taken. -/
theorem terminal_bound {I : Type*} (s : Finset I) (z : I→ℂ) :
    Complex.normSq (∏ i∈s,(1+z i))≤
      Real.exp (2*(∑ i∈s,(z i).re)+∑ i∈s,Complex.normSq (z i)) := by
  have hlocal (x : ℂ) :
      Complex.normSq (1+x)≤Real.exp (2*x.re+Complex.normSq x) := by
    rw [add_comm,Complex.normSq_add]
    simp only [Complex.normSq_one, map_one, Complex.mul_re,Complex.one_re,Complex.one_im,
      mul_one,mul_zero,sub_zero]
    have h := Real.add_one_le_exp (2*x.re+Complex.normSq x)
    linarith
  rw [map_prod,Finset.mul_sum,←Finset.sum_add_distrib,Real.exp_sum]
  exact Finset.prod_le_prod (fun i _=>Complex.normSq_nonneg _) (fun i _=>hlocal (z i))

end Factoring.PrefixBounds

#print axioms Factoring.PrefixBounds.unit_card
#print axioms Factoring.PrefixBounds.prefix_L2
#print axioms Factoring.PrefixBounds.final_prime_inj
#print axioms Factoring.PrefixBounds.two_prefix
#print axioms Factoring.PrefixBounds.normalized_two_prefix
#print axioms Factoring.PrefixBounds.terminal_bound
