import Mathlib.LinearAlgebra.Matrix.PosDef
import Mathlib.Data.Matrix.Hadamard
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring
import Mathlib.Tactic.FieldSimp

/-!
# Finite linear algebra behind the sparse Gram argument

We prove the local nonnegative outer-product decompositions, the real Schur
product theorem, preservation of the stronger all-ones lower bound, and the
finite averaging step. These are universal matrix statements, allowing repeated
local classes. Identifying their entries with quadratic ideal-character
coefficients and proving the analytic estimates are separate obligations.
-/

open scoped BigOperators Matrix ComplexOrder

namespace Factoring.Gram

variable {ι κ : Type*} [Fintype ι]

/-- An outer product, not the diagonal matrix associated with `v`. -/
def outer (v : ι → ℝ) : Matrix ι ι ℝ := fun i j => v i * v j

theorem outer_posSemidef (v : ι → ℝ) : (outer v).PosSemidef := by
  convert Matrix.posSemidef_conjTranspose_mul_self (fun (_ : Unit) i => v i) using 1
  ext i j
  simp [outer, Matrix.mul_apply, Matrix.conjTranspose_apply]

theorem nonneg_smul {A : Matrix ι ι ℝ} (hA : A.PosSemidef)
    {c : ℝ} (hc : 0 ≤ c) : (c • A).PosSemidef := by
  constructor
  · apply Matrix.IsHermitian.ext
    intro i j
    simpa using congrArg (fun x : ℝ => c * x) (hA.1.apply i j)
  · intro x
    simpa only [Matrix.smul_mulVec_assoc, dotProduct_smul, smul_eq_mul]
      using mul_nonneg hc (hA.2 x)

theorem sum_posSemidef (s : Finset κ) (A : κ → Matrix ι ι ℝ)
    (hA : ∀ k ∈ s, (A k).PosSemidef) : (∑ k ∈ s, A k).PosSemidef := by
  classical
  induction s using Finset.induction_on with
  | empty => simpa using (Matrix.PosSemidef.zero : (0 : Matrix ι ι ℝ).PosSemidef)
  | @insert k s hk ih =>
    rw [Finset.sum_insert hk]
    exact (hA k (Finset.mem_insert_self _ _)).add
      (ih fun j hj => hA j (Finset.mem_insert_of_mem hj))

omit [Fintype ι] in
/-- The odd-exponent local block; the identity holds for arbitrary real vectors. -/
theorem odd_block_identity (e : ℝ) (u v : ι → ℝ) :
    ((e - 1) / 2) • outer (u + v) + ((e + 1) / 2) • outer (u - v) =
      fun i j => e * (u i * u j + v i * v j) - (u i * v j + v i * u j) := by
  ext i j
  simp [outer]
  ring

theorem odd_block_posSemidef {e : ℝ} (he : 1 ≤ e) (u v : ι → ℝ) :
    (((e - 1) / 2) • outer (u + v) +
      ((e + 1) / 2) • outer (u - v)).PosSemidef :=
  (nonneg_smul (outer_posSemidef _) (by linarith)).add
    (nonneg_smul (outer_posSemidef _) (by linarith))

theorem even_block_posSemidef {e : ℝ} (he : 0 ≤ e) (u v : ι → ℝ) :
    (e • (outer u + outer v)).PosSemidef :=
  nonneg_smul ((outer_posSemidef u).add (outer_posSemidef v)) he

/-- Schur's theorem, proved by expressing one factor as a Gram matrix. -/
theorem schur {A B : Matrix ι ι ℝ} (hA : A.PosSemidef) (hB : B.PosSemidef) :
    (A ⊙ B).PosSemidef := by
  classical
  obtain ⟨C, rfl⟩ := Matrix.posSemidef_iff_eq_transpose_mul_self.mp hA
  have h := sum_posSemidef Finset.univ
    (fun k => (Matrix.diagonal (C k))ᴴ * B * Matrix.diagonal (C k))
    (fun k _ => hB.conjTranspose_mul_mul_same (Matrix.diagonal (C k)))
  convert h using 1
  ext i j
  rw [Matrix.hadamard_apply, Matrix.mul_apply, Finset.sum_mul, Matrix.sum_apply]
  apply Finset.sum_congr rfl
  intro k _
  rw [Matrix.diagonal_conjTranspose]
  simp only [star_trivial, Matrix.mul_diagonal, Matrix.diagonal_mul,
    Matrix.conjTranspose_apply]
  ring

/-- The all-ones matrix is the identity for entrywise multiplication. -/
def ones : Matrix ι ι ℝ := fun _ _ => 1

theorem ones_posSemidef : (ones : Matrix ι ι ℝ).PosSemidef := by
  convert outer_posSemidef (fun _ : ι => (1 : ℝ)) using 1
  ext i j
  simp [outer, ones]

theorem schur_above_ones {A B : Matrix ι ι ℝ}
    (hA : (A - ones).PosSemidef) (hB : (B - ones).PosSemidef) :
    (A ⊙ B - ones).PosSemidef := by
  have h := (hA.add hB).add (schur hA hB)
  convert h using 1
  ext i j
  simp [Matrix.hadamard_apply, ones]
  ring

/-- Prime-power factors are combined entrywise; the empty product is `ones`. -/
def entryProduct : List (Matrix ι ι ℝ) → Matrix ι ι ℝ
  | [] => ones
  | A :: rest => A ⊙ entryProduct rest

theorem entryProduct_posSemidef (factors : List (Matrix ι ι ℝ))
    (h : ∀ A ∈ factors, A.PosSemidef) : (entryProduct factors).PosSemidef := by
  induction factors with
  | nil => exact ones_posSemidef
  | cons A rest ih =>
    exact schur (h A (by simp)) (ih fun B hB => h B (by simp [hB]))

theorem entryProduct_above_ones (factors : List (Matrix ι ι ℝ))
    (h : ∀ A ∈ factors, (A - ones).PosSemidef) :
    (entryProduct factors - ones).PosSemidef := by
  induction factors with
  | nil => simpa [entryProduct] using
      (Matrix.PosSemidef.zero : (0 : Matrix ι ι ℝ).PosSemidef)
  | cons A rest ih =>
    exact schur_above_ones (h A (by simp)) (ih fun B hB => h B (by simp [hB]))

theorem total_nonneg {A : Matrix ι ι ℝ} (hA : A.PosSemidef) :
    0 ≤ ∑ i, ∑ j, A i j := by
  simpa [dotProduct, Matrix.mulVec] using hA.2 (fun _ => 1)

theorem total_ge_card_sq {A : Matrix ι ι ℝ} (hA : (A - ones).PosSemidef) :
    (Fintype.card ι : ℝ) ^ 2 ≤ ∑ i, ∑ j, A i j := by
  have h := total_nonneg hA
  simp [ones, Finset.sum_sub_distrib, pow_two] at h ⊢
  linarith

/-- Summing the strengthened lower bound over the distinguished (smooth)
indices, and nonnegativity over every other index. -/
theorem sum_total_lower_bound [DecidableEq κ] (terms good : Finset κ)
    (hsub : good ⊆ terms) (B : κ → Matrix ι ι ℝ)
    (hB : ∀ k ∈ terms, (B k).PosSemidef)
    (hgood : ∀ k ∈ good, (B k - ones).PosSemidef) :
    (Fintype.card ι : ℝ) ^ 2 * good.card ≤ ∑ k ∈ terms, ∑ i, ∑ j, B k i j := by
  have hterm : ∀ k ∈ terms,
      (if k ∈ good then (Fintype.card ι : ℝ) ^ 2 else 0) ≤ ∑ i, ∑ j, B k i j := by
    intro k hk
    split_ifs with hg
    · exact total_ge_card_sq (hgood k hg)
    · exact total_nonneg (hB k hk)
  have h := Finset.sum_le_sum hterm
  simpa [Finset.sum_ite_mem, Finset.inter_eq_right.mpr hsub, mul_comm] using h

/-- The pigeonhole step, stated without any analytic input. -/
theorem exists_ge_average (s : Finset κ) (hs : s.Nonempty) (f : κ → ℝ)
    (b : ℝ) (hb : (s.card : ℝ) * b ≤ ∑ i ∈ s, f i) :
    ∃ i ∈ s, b ≤ f i := by
  apply Finset.exists_le_of_sum_le hs
  simpa using hb

/-- The exact off-diagonal averaging inequality. Here `A` can be the sum of
the matrices indexed by integers up to a cutoff. No distinctness of their
edge labels is required. The analytic diagonal bound is an explicit input. -/
theorem off_diagonal_average (A : Matrix ι ι ℝ) (P D : ℝ)
    (hc : 1 < Fintype.card ι) (hP : 0 ≤ P)
    (htotal : (Fintype.card ι : ℝ) ^ 2 * P ≤ ∑ i, ∑ j, A i j)
    (hdiag : (∑ i, A i i) ≤ (Fintype.card ι : ℝ) * D) :
    ∃ i j, i ≠ j ∧ P - D / ((Fintype.card ι : ℝ) - 1) ≤ A i j := by
  classical
  let H : ℝ := Fintype.card ι
  let off := (Finset.univ : Finset ι).offDiag
  have hH : 1 < H := by dsimp [H]; exact_mod_cast hc
  have hcard : (off.card : ℝ) = H * (H - 1) := by
    simp only [off, Finset.offDiag_card, Finset.card_univ]
    rw [Nat.cast_sub (Nat.le_mul_self _), Nat.cast_mul]
    dsimp [H]
    ring
  have hpos : 0 < (off.card : ℝ) := by
    rw [hcard]
    exact mul_pos (by linarith) (by linarith)
  have hnonempty : off.Nonempty := Finset.card_pos.mp (by exact_mod_cast hpos)
  have hsum : (∑ i, ∑ j, A i j) =
      (∑ i, A i i) + ∑ p ∈ off, A p.1 p.2 := by
    rw [← Finset.sum_product', ← Finset.diag_union_offDiag,
      Finset.sum_union (Finset.disjoint_diag_offDiag _)]
    simp [off]
  obtain ⟨⟨i, j⟩, hij, hlarge⟩ := exists_ge_average off hnonempty
    (fun p => A p.1 p.2) (P - D / (H - 1)) (by
      rw [hcard]
      have heq : H * (H - 1) * (P - D / (H - 1)) = H ^ 2 * P - H * P - H * D := by
        field_simp [ne_of_gt (sub_pos.mpr hH)]
        ring
      rw [heq]
      have hHP : 0 ≤ H * P := mul_nonneg (by linarith) hP
      change H ^ 2 * P ≤ _ at htotal
      change (∑ i, A i i) ≤ H * D at hdiag
      linarith)
  exact ⟨i, j, (Finset.mem_offDiag.mp hij).2.2, hlarge⟩

/-- The finite sparse Gram inequality, with all matrix and diagonal hypotheses
visible. Arithmetic constructions must prove these hypotheses separately. -/
theorem sparse_average [DecidableEq κ] (terms good : Finset κ)
    (hsub : good ⊆ terms) (B : κ → Matrix ι ι ℝ) (D : ℝ)
    (hc : 1 < Fintype.card ι)
    (hB : ∀ k ∈ terms, (B k).PosSemidef)
    (hgood : ∀ k ∈ good, (B k - ones).PosSemidef)
    (hdiag : (∑ i, ∑ k ∈ terms, B k i i) ≤ (Fintype.card ι : ℝ) * D) :
    ∃ i j, i ≠ j ∧
      (good.card : ℝ) - D / ((Fintype.card ι : ℝ) - 1) ≤ ∑ k ∈ terms, B k i j := by
  have htotal : (Fintype.card ι : ℝ) ^ 2 * good.card ≤
      ∑ i, ∑ j, (∑ k ∈ terms, B k) i j := by
    calc
      _ ≤ ∑ k ∈ terms, ∑ i, ∑ j, B k i j :=
        sum_total_lower_bound terms good hsub B hB hgood
      _ = _ := by
        simp only [Matrix.sum_apply]
        rw [Finset.sum_comm]
        apply Finset.sum_congr rfl
        intro i _
        rw [Finset.sum_comm]
  simpa only [Matrix.sum_apply] using
    off_diagonal_average (∑ k ∈ terms, B k) good.card D hc (by positivity) htotal
      (by simpa only [Matrix.sum_apply] using hdiag)

end Factoring.Gram
