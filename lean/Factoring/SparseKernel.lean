import Factoring.Uniform
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.LinearAlgebra.Dimension.RankNullity

/-! The correction computed from a Krylov annihilating relation.
This is an algebraic verification theorem, not a proof of the randomized
preconditioner probability or of Berlekamp--Massey's complexity. -/
namespace Factoring.SparseKernel
open scoped BigOperators
variable {K V W : Type*} [Field K] [AddCommGroup V] [AddCommGroup W]
  [Module K V] [Module K W]

/-- Solve Bx=y from a verified recurrence with nonzero constant coefficient. -/
theorem krylov_solution (B : W→ₗ[K] W) (y : W) (c : ℕ→K) (n : ℕ)
    (hc : c 0≠0)
    (h : c 0 • y + ∑ i ∈ Finset.range n, c (i+1) • ((B^(i+1)) y)=0) :
    B (-(c 0)⁻¹ • (∑ i ∈ Finset.range n, c (i+1) • ((B^i) y)))=y := by
  rw [map_smul,map_sum]
  simp only [map_smul]
  have he : (∑ i ∈ Finset.range n, c (i+1) • B ((B^i) y)) =
      ∑ i ∈ Finset.range n, c (i+1) • ((B^(i+1)) y) := by
    apply Finset.sum_congr rfl
    intro i hi
    rw [pow_succ']
    rfl
  rw [he,eq_neg_of_add_eq_zero_right h,smul_neg,neg_smul,neg_neg,smul_smul,
    inv_mul_cancel₀ hc,one_smul]

/-- Correcting v by D x is a kernel vector whenever B=A∘D and Bx=Av. -/
theorem correction_mem_ker (A : V→ₗ[K] W) (D : W→ₗ[K] V) (v : V) (x : W)
    (h : (A.comp D) x=A v) : v-D x ∈ LinearMap.ker A := by
  rw [LinearMap.mem_ker,map_sub]
  change A v - (A.comp D) x=0
  rw [h,sub_self]

/-- A single recurrence polynomial valid on im A yields one linear lift,
so the correction is a surjective uniform kernel projection. -/
noncomputable def recurrenceLift (D : W→ₗ[K] V) (B : W→ₗ[K] W)
    (c : ℕ→K) (n : ℕ) : W→ₗ[K] V :=
  D.comp (-(c 0)⁻¹ • ∑ i ∈ Finset.range n, c (i+1) • B^i)

theorem lift_correct (A : V→ₗ[K] W) (D : W→ₗ[K] V)
    (c : ℕ→K) (n : ℕ) (hc : c 0≠0)
    (h : ∀ v : V, c 0 • A v +
      ∑ i ∈ Finset.range n, c (i+1) • (((A.comp D)^(i+1)) (A v))=0) :
    ∀ v, A (recurrenceLift D (A.comp D) c n (A v))=A v := by
  intro v
  have hh := krylov_solution (A.comp D) (A v) c n hc (h v)
  simpa [recurrenceLift, LinearMap.sum_apply] using hh

end Factoring.SparseKernel
