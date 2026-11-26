import Mathlib.RingTheory.Norm.Basic
import Mathlib.RingTheory.Polynomial.ScaleRoots
import Mathlib.NumberTheory.NumberField.Norm
import Mathlib.Tactic

/-! Actual field norm of a linear factor for a power basis, and an
integral monic polynomial for the scaled root of a nonmonic polynomial.
These establish the norm part of the nonmonic valuation construction,
without assuming a power-order index is coprime to a rational prime. -/
namespace Factoring.NumberFieldNorm
open Polynomial Matrix
open scoped BigOperators

/-- The integral polynomial for the scaled generator a_d θ:
a_d^{-1} scaleRoots(f,a_d), formed without division. -/
noncomputable def scaledMonic (f : ℤ[X]) : ℤ[X] :=
  X^f.natDegree + ∑ i∈Finset.range f.natDegree,
    monomial i (f.coeff i * f.leadingCoeff^(f.natDegree-1-i))

theorem scaled_coeff (f : ℤ[X]) (i : ℕ) :
    (scaledMonic f).coeff i =
      if i=f.natDegree then 1 else
      if i<f.natDegree then f.coeff i*f.leadingCoeff^(f.natDegree-1-i) else 0 := by
  classical
  unfold scaledMonic
  rw [coeff_add,coeff_X_pow,finset_sum_coeff]
  simp only [coeff_monomial]
  by_cases hi : i<f.natDegree
  · have hn : i≠f.natDegree := ne_of_lt hi
    rw [Finset.sum_eq_single i]
    · simp [hi,hn]
    · intro j _ hj
      simp [hj]
    · simp [hi]
  · rw [Finset.sum_eq_zero]
    · simp [hi]
    · intro j hj
      have hne : j≠i := by simp only [Finset.mem_range] at hj; omega
      simp [hne,Ne.symm hne]

theorem scaledMonic_monic (f : ℤ[X]) : (scaledMonic f).Monic := by
  apply monic_of_natDegree_le_of_coeff_eq_one f.natDegree
  · apply natDegree_le_iff_coeff_eq_zero.mpr
    intro i hi
    rw [scaled_coeff,if_neg (by omega),if_neg (by omega)]
  · simp [scaled_coeff]

theorem scaledMonic_degree (f : ℤ[X]) :
    (scaledMonic f).natDegree=f.natDegree := by
  apply natDegree_eq_of_le_of_coeff_ne_zero
  · apply natDegree_le_iff_coeff_eq_zero.mpr
    intro i hi
    rw [scaled_coeff,if_neg (by omega),if_neg (by omega)]
  · simp [scaled_coeff]

theorem scaleRoots_eq (f : ℤ[X]) :
    f.scaleRoots f.leadingCoeff = C f.leadingCoeff * scaledMonic f := by
  ext i
  rw [coeff_scaleRoots,coeff_C_mul,scaled_coeff]
  by_cases hi : i=f.natDegree
  · subst i
    change f.leadingCoeff * f.leadingCoeff^(f.natDegree-f.natDegree) = _
    simp only [if_true,if_pos rfl,Nat.sub_self,pow_zero,mul_one]
  · rw [if_neg hi]
    by_cases hlt : i<f.natDegree
    · rw [if_pos hlt,show f.natDegree-i=(f.natDegree-1-i)+1 by omega,pow_succ]
      ring
    · rw [if_neg hlt,coeff_eq_zero_of_natDegree_lt (by omega)]
      simp

theorem scaled_integral {K : Type*} [Field K] [CharZero K]
    (f : ℤ[X]) (hf : f≠0) (θ : K) (hθ : aeval θ f=0) :
    IsIntegral ℤ (algebraMap ℤ K f.leadingCoeff*θ) := by
  refine ⟨scaledMonic f,scaledMonic_monic f,?_⟩
  have h := scaleRoots_aeval_eq_zero (r:=f.leadingCoeff) hθ
  rw [scaleRoots_eq,map_mul,aeval_C] at h
  have hne : algebraMap ℤ K f.leadingCoeff≠0 :=
    Int.cast_ne_zero.mpr (leadingCoeff_ne_zero.mpr hf)
  exact (mul_eq_zero.mp h).resolve_left hne

/-- The norm of a-θ is the evaluation of the actual minimal
polynomial. The proof is a determinant of the left multiplication
matrix, whose characteristic polynomial mathlib identifies. -/
theorem norm_sub_gen {K L : Type*} [Field K] [Field L] [Algebra K L]
    (pb : PowerBasis K L) (a : K) :
    Algebra.norm K (algebraMap K L a-pb.gen) = (minpoly K pb.gen).eval a := by
  rw [Algebra.norm_eq_matrix_det pb.basis,←charpoly_leftMulMatrix pb,
    Matrix.charpoly,Matrix.eval_det,Matrix.matPolyEquiv_eval_eq_map]
  congr 1
  rw [map_sub,(Algebra.leftMulMatrix pb.basis).commutes]
  ext i j
  by_cases hij : i=j
  · subst j
    simp [Matrix.charmatrix_apply_eq,Matrix.map_apply,Matrix.sub_apply,
      Matrix.algebraMap_matrix_apply]
  · simp [Matrix.charmatrix_apply_ne,Matrix.map_apply,Matrix.sub_apply,
      Matrix.algebraMap_matrix_apply,hij]

/-- For an irreducible nonmonic defining polynomial over the base
field, this is the precise leading coefficient correction. -/
theorem norm_nonmonic {K L : Type*} [Field K] [Field L] [Algebra K L]
    (pb : PowerBasis K L) (f : K[X]) (hf : Irreducible f)
    (hθ : aeval pb.gen f=0) (a : K) :
    f.leadingCoeff*Algebra.norm K (algebraMap K L a-pb.gen)=f.eval a := by
  rw [norm_sub_gen,←minpoly.eq_of_irreducible hf hθ,eval_mul,eval_C]
  have hn : f.leadingCoeff≠0 := leadingCoeff_ne_zero.mpr hf.ne_zero
  field_simp

end Factoring.NumberFieldNorm

