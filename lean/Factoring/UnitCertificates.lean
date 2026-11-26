import Mathlib.NumberTheory.NumberField.Units.Regulator
import Mathlib.RingTheory.AdjoinRoot
import Mathlib.RingTheory.Localization.Basic
import Mathlib.Data.ZMod.Basic
import Mathlib.Tactic.Ring
import Mathlib.Algebra.BigOperators.Group.Finset.Basic

/-! Number-field and localization bridges. Dirichlet's unit theorem,
the unit lattice, and its torsion kernel are imported from mathlib,
rather than rebuilt. This does not yet construct the valuation and
logarithmic relations or bound their reconstruction cost. -/
open scoped NumberField BigOperators
namespace Factoring.UnitCertificates

open NumberField NumberField.InfinitePlace NumberField.Units
open NumberField.Units.dirichletUnitTheorem

/-- One real embedding suffices: a unit in the kernel of the
logarithmic embedding is a square root of one. -/
theorem log_zero_square {K : Type*} [Field K] [NumberField K]
    (σ : K →+* ℝ) (u : (𝓞 K)ˣ)
    (hu : logEmbedding K (Additive.ofMul u) = 0) : u^2=1 := by
  have ht := logEmbedding_eq_zero_iff.mp hu
  let φ : K →+* ℂ := Complex.ofRealHom.comp σ
  have h := (NumberField.Units.mem_torsion K).mp ht (InfinitePlace.mk φ)
  change ‖φ (u : K)‖ = 1 at h
  have habs : |σ (u : K)|=1 := by
    simpa [φ, Real.norm_eq_abs] using h
  apply NumberField.Units.coe_injective K
  apply σ.injective
  change σ ((u^2 : (𝓞 K)ˣ) : K) = σ ((1 : (𝓞 K)ˣ) : K)
  rw [NumberField.Units.coe_pow,NumberField.Units.coe_one,map_pow,map_one]
  have hh := congrArg (fun x : ℝ => x^2) habs
  simpa [sq_abs] using hh

/-- The actual unit logarithms span the full log space. -/
theorem full_unit_lattice (K : Type*) [Field K] [NumberField K] :
    Submodule.span ℝ (unitLattice K : Set (logSpace K)) = ⊤ :=
  unitLattice_span_eq_top K

/-- The regulator is nonzero without assuming that the fields have
a particular signature. -/
theorem regulator_positive (K : Type*) [Field K] [NumberField K] :
    0 < regulator K := regulator_pos K

section Localize

variable {R S T : Type*} [CommRing R] [CommRing S] [CommRing T]

/-- A polynomial root modulo N gives an evaluation map on the polynomial
order, not on the entire number field. No order-index coprimality is required. -/
def orderEvaluation (f : Polynomial R) (i : R →+* T) (m : T)
    (hm : f.eval₂ i m=0) : AdjoinRoot f →+* T :=
  AdjoinRoot.lift i m hm

theorem orderEvaluation_linear (f : Polynomial R) (i : R →+* T) (m : T)
    (hm : f.eval₂ i m=0) (a : R) :
    orderEvaluation f i m hm (AdjoinRoot.of f a-AdjoinRoot.root f)=i a-m := by
  simp [orderEvaluation,AdjoinRoot.lift_root]

/-- Inverting only elements that evaluate to units extends the evaluation
map by the localization universal property. -/
noncomputable def localizedEvaluation (D : Submonoid R) [Algebra R S]
    [IsLocalization D S] (f : R→+*T) (h : ∀ d:D, IsUnit (f d)) : S→+*T :=
  IsLocalization.lift h

theorem localizedEvaluation_apply (D : Submonoid R) [Algebra R S]
    [IsLocalization D S] (f : R→+*T) (h : ∀ d:D, IsUnit (f d)) (x:R) :
    localizedEvaluation (S:=S) D f h (algebraMap R S x)=f x :=
  IsLocalization.lift_eq h x

/-- In the actual localized polynomial order, a linear relation factor
maps to the common modular value a-m. -/
theorem localized_order_linear (f : Polynomial R) (D : Submonoid (AdjoinRoot f))
    [Algebra (AdjoinRoot f) S] [IsLocalization D S]
    (i : R→+*T) (m:T) (hm:f.eval₂ i m=0)
    (hD : ∀ d:D, IsUnit (orderEvaluation f i m hm d)) (a:R) :
    localizedEvaluation (S:=S) D (orderEvaluation f i m hm) hD
      (algebraMap (AdjoinRoot f) S (AdjoinRoot.of f a-AdjoinRoot.root f)) = i a-m := by
  rw [localizedEvaluation_apply,orderEvaluation_linear]

end Localize

/-- The exact two-field cancellation. The equal products of modular
relation factors give p^E times a square-trivial unit in field 1, and
a square-trivial unit in field 2. This version works over any
commutative group of units, and does not use a factorization of N. -/
theorem order_from_two_products {G : Type*} [CommGroup G]
    (p γ₁ γ₂ v : G) (E : ℕ) (h₁ : γ₁^2=1) (h₂ : γ₂^2=1)
    (hprod₁ : p^E*γ₁=v) (hprod₂ : γ₂=v) :
    p^(2*E)=1 := by
  have h := congrArg (fun x:G => x^2) (hprod₁.trans hprod₂.symm)
  change (p^E*γ₁)^2=γ₂^2 at h
  rw [mul_pow,h₁,h₂,mul_one,←pow_mul, Nat.mul_comm E 2] at h
  exact h

/-- Cancellation after mapping actual products of integer powers
from the two localized unit groups. -/
theorem two_field_certificate {G A B I : Type*}
    [CommGroup G] [CommGroup A] [CommGroup B] [Fintype I]
    (φ : A→*G) (ψ : B→*G) (x : I→A) (y : I→B) (c : I→ℤ)
    (p γ₁ : A) (γ₂ : B) (E : ℕ)
    (hmap : ∀ i, φ (x i)=ψ (y i))
    (hu₁ : γ₁^2=1) (hu₂ : γ₂^2=1)
    (h₁ : p^E*γ₁=∏ i, x i ^ c i) (h₂ : γ₂=∏ i, y i ^ c i) :
    (φ p)^(2*E)=1 := by
  have hA := congrArg φ h₁
  have hB := congrArg ψ h₂
  simp only [map_mul,map_pow,map_prod,map_zpow] at hA hB
  simp_rw [hmap] at hA
  exact order_from_two_products (φ p) (φ γ₁) (ψ γ₂) _ E
    (by rw [←map_pow,hu₁,map_one]) (by rw [←map_pow,hu₂,map_one]) hA hB

end Factoring.UnitCertificates
