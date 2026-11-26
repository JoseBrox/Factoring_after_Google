import Mathlib.Data.Real.Basic
import Mathlib.Algebra.Order.BigOperators.Group.Finset
import Mathlib.Algebra.Order.BigOperators.Ring.Finset
import Mathlib.Tactic

/-! The finite weighted estimates used after the analytic lattice-fibre
and local-moment lemmas. These do not assert the missing probabilistic
hypotheses for the concrete factoring ensemble. -/
namespace Factoring.Readiness
open scoped BigOperators

/-- Exact finite sum version of the conditioning argument. The original
weights sum to one; the restricted weights before renormalization have
mass at most 3ε on the exceptional set. Good weights change relatively
by at most ε. -/
theorem expectation_numerator {I : Type*} (good bad : Finset I)
    (a b f : I→ℝ) {ε : ℝ}
    (hε : 0≤ε) (ha : ∀ i, 0≤a i) (hb : ∀ i, 0≤b i)
    (hf : ∀ i, 0≤f i ∧ f i≤1)
    (hgood : ∀ i∈good, |b i-a i|≤ε*a i)
    (habad : ∑ i∈bad,a i ≤ ε) (hbbad : ∑ i∈bad,b i ≤ 3*ε) :
    |(∑ i∈good,b i*f i)+(∑ i∈bad,b i*f i)-
       ((∑ i∈good,a i*f i)+(∑ i∈bad,a i*f i))|
       ≤ ε*(∑ i∈good,a i*f i)+4*ε := by
  have h1 : |(∑ i∈good,b i*f i)-(∑ i∈good,a i*f i)|
      ≤ ε*(∑ i∈good,a i*f i) := by
    rw [← Finset.sum_sub_distrib]
    calc
      _ ≤ ∑ i∈good, |b i*f i-a i*f i| := Finset.abs_sum_le_sum_abs _ _
      _ ≤ ∑ i∈good, ε*(a i*f i) := by
        apply Finset.sum_le_sum
        intro i hi
        rw [←sub_mul,abs_mul,abs_of_nonneg (hf i).1]
        exact (mul_le_mul_of_nonneg_right (hgood i hi) (hf i).1).trans_eq (by ring)
      _ = _ := (Finset.mul_sum _ _ _).symm
  have ha0 : 0≤∑ i∈bad,a i*f i :=
    Finset.sum_nonneg fun i _=>mul_nonneg (ha i) (hf i).1
  have hb0 : 0≤∑ i∈bad,b i*f i :=
    Finset.sum_nonneg fun i _=>mul_nonneg (hb i) (hf i).1
  have ha1 : ∑ i∈bad,a i*f i ≤ ε := (Finset.sum_le_sum
    (fun i _=>mul_le_of_le_one_right (ha i) (hf i).2)).trans habad
  have hb1 : ∑ i∈bad,b i*f i ≤ 3*ε := (Finset.sum_le_sum
    (fun i _=>mul_le_of_le_one_right (hb i) (hf i).2)).trans hbbad
  have h2 : |(∑ i∈bad,b i*f i)-(∑ i∈bad,a i*f i)|≤4*ε := by
    apply abs_le.mpr
    constructor <;> linarith
  have h3 := abs_add_le ((∑ i∈good,b i*f i)-(∑ i∈good,a i*f i))
    ((∑ i∈bad,b i*f i)-(∑ i∈bad,a i*f i))
  rw [show (∑ i∈good,b i*f i)+(∑ i∈bad,b i*f i)-
       ((∑ i∈good,a i*f i)+(∑ i∈bad,a i*f i))=
       ((∑ i∈good,b i*f i)-(∑ i∈good,a i*f i))+
       ((∑ i∈bad,b i*f i)-(∑ i∈bad,a i*f i)) by ring]
  linarith

/-- The finite renormalization error, with the manuscript's relative
normalizer estimate. -/
theorem renormalize {a b z ε : ℝ} (hε : 0≤ε) (hε1 : ε<1)
    (ha : 0≤a) (hz : |z-1|≤ε) (hab : |b-a|≤ε*a+4*ε) :
    |b/z-a|≤(2*ε*a+4*ε)/(1-ε) := by
  have hz0 : 0<z := by have h := (abs_le.mp hz).1; linarith
  have hz1 : 1-ε≤z := by have h := (abs_le.mp hz).1; linarith
  have h := abs_add_le (b-a) (a*(1-z))
  rw [abs_mul,abs_of_nonneg ha,abs_sub_comm 1 z] at h
  have hm := mul_le_mul_of_nonneg_left hz ha
  have hnum : |b-a*z|≤2*ε*a+4*ε := by
    rw [show b-a*z=(b-a)+a*(1-z) by ring]
    linarith
  rw [show b/z-a=(b-a*z)/z by field_simp; ring,abs_div,abs_of_pos hz0]
  exact (div_le_div_of_nonneg_right hnum hz0.le).trans
    (div_le_div_of_nonneg_left (by positivity) (by linarith) hz1)

/-- Backwards propagation through a finite nonnegative transition kernel.
Rows are not required to be probability distributions: the weighted
local bound may have total mass greater than one. -/
noncomputable def propagate {I : Type*} [Fintype I]
    (K : I→I→ℝ) (f : I→ℝ) : ℕ→I→ℝ
  | 0, i => f i
  | n+1, i => ∑ j, K i j * propagate K f n j

theorem propagate_bound {I : Type*} [Fintype I]
    (K : I→I→ℝ) (f : I→ℝ) {C p : ℝ}
    (hC : 0≤C) (hp : 0≤p) (hK : ∀ i j, 0≤K i j)
    (hrow : ∀ i, ∑ j,K i j≤C) (hf : ∀ i,f i≤p) :
    ∀ n i, propagate K f n i≤C^n*p := by
  intro n
  induction n with
  | zero => intro i; simpa [propagate] using hf i
  | succ n ih =>
    intro i
    calc
      propagate K f (n+1) i = ∑ j,K i j*propagate K f n j := rfl
      _ ≤ ∑ j,K i j*(C^n*p) := Finset.sum_le_sum fun j _=>
        mul_le_mul_of_nonneg_left (ih j) (hK i j)
      _ = (∑ j,K i j)*(C^n*p) := (Finset.sum_mul _ _ _).symm
      _ ≤ C*(C^n*p) := mul_le_mul_of_nonneg_right (hrow i) (by positivity)
      _ = C^(n+1)*p := by rw [pow_succ]; ring

end Factoring.Readiness

