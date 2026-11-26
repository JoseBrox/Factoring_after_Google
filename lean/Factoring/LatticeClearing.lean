import Mathlib.NumberTheory.NumberField.Units.Regulator
import Mathlib.LinearAlgebra.Matrix.Adjugate

/-! Candidate: exact determinant clearing in the actual mathlib unit lattice.
This file is deliberately outside the audited 4.19 core until CI succeeds.
No claim about effective determinant, generator-height, or bit-cost bounds. -/

namespace Factoring.LatticeClearing
open scoped BigOperators
open Matrix

variable {ι : Type*} [Fintype ι] [DecidableEq ι]
variable {V : Type*} [AddCommGroup V]

noncomputable def coordMatrix (B : Basis ι ℤ V) (v : ι → V) :
    Matrix ι ι ℤ :=
  fun i j => B.equivFun (v j) i

theorem det_multiple (B : Basis ι ℤ V) (v : ι → V) (b : V) :
    ∑ j, Matrix.cramer (coordMatrix B v) (B.equivFun b) j • v j =
      (coordMatrix B v).det • b := by
  apply B.equivFun.injective
  funext i
  have h := congrFun (Matrix.mulVec_cramer (coordMatrix B v) (B.equivFun b)) i
  simp only [map_sum, map_zsmul, Finset.sum_apply, Pi.smul_apply, smul_eq_mul]
  simpa only [Matrix.mulVec, dotProduct, coordMatrix, Pi.smul_apply, smul_eq_mul, mul_comm] using h

theorem positive_multiple (B : Basis ι ℤ V) (v : ι → V) (b : V)
    (h : (coordMatrix B v).det ≠ 0) :
    ∃ D : ℤ, 0 < D ∧ ∃ c : ι → ℤ, ∑ j, c j • v j = D • b := by
  let A := coordMatrix B v
  let c := Matrix.cramer A (B.equivFun b)
  have he : ∑ j, c j • v j = A.det • b := det_multiple B v b
  rcases lt_or_gt_of_ne h with hn | hp
  · refine ⟨-A.det, neg_pos.mpr hn, fun j => -c j, ?_⟩
    simpa only [neg_zsmul, Finset.sum_neg_distrib] using congrArg (fun x : V => -x) he
  · exact ⟨A.det, hp, c, he⟩

open NumberField NumberField.Units

theorem unit_lattice_multiple (K : Type*) [Field K] [NumberField K]
    (v : Fin (rank K) → unitLattice K)
    (b : unitLattice K)
    (h : (coordMatrix (basisUnitLattice K) v).det ≠ 0) :
    ∃ D : ℤ, 0 < D ∧ ∃ c : Fin (rank K) → ℤ, ∑ j, c j • v j = D • b :=
  positive_multiple (basisUnitLattice K) v b h


end Factoring.LatticeClearing
