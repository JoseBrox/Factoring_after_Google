import OAI.NumberTheory.Ostmann.ZeroDensity.ComplexDensityProof

/-! A deliberately narrow adapter for the near-one conductor deletion.
The imported zero enumeration is the actual faithful enumeration, not a
new structure whose density is an axiom. -/
open scoped BigOperators
open OAI.Ostmann

namespace Factoring.Density

/-- The precise bound needed here is a uniform constant multiplying
1-σ in the exponent; the Montgomery–Inoue exponent is at most 3(1-σ). -/
theorem near_one_exponent {σ : ℝ} (hσ : σ ≤ 1) :
    3*(1-σ)/(2-σ) ≤ 3*(1-σ) :=
  div_le_self (by linarith) (by linarith)

theorem uniform_near_one_count :
    ∃ C : ℝ, 0 < C ∧ ∀ (Q : ℕ), 1 ≤ Q → ∀ (T σ : ℝ), 2 ≤ T →
      1/2 ≤ σ → σ ≤ 1 → ∀ F : Finset PrimitiveComplexCharacter,
      (∀ χ ∈ F, χ.modulus ≤ Q) →
      (∑ χ ∈ F, ((actualCharacterZeros χ).count σ T : ℝ)) ≤
        C * ((Q:ℝ)^2*T)^(3*(1-σ)) * (Real.log ((Q:ℝ)*T))^13 := by
  obtain ⟨C,hC,h⟩ := publishedComplexZeroDensity
  refine ⟨C,hC,?_⟩
  intro Q hQ T σ hT hσ hσ1 F hF
  have hq : (1:ℝ)≤Q := by exact_mod_cast hQ
  have hB : 1≤(Q:ℝ)^2*T := by nlinarith
  exact (h Q hQ T σ hT hσ hσ1 F hF).trans (by
    gcongr
    exact Real.rpow_le_rpow_of_exponent_le hB (near_one_exponent hσ1))

/-- Every character carrying one enumerated zero contributes at least one
to the density sum, so the same bound holds for the number of bad
characters. Conductors can subsequently be counted by their image. -/
theorem bad_character_count :
    ∃ C : ℝ, 0 < C ∧ ∀ (Q : ℕ), 1 ≤ Q → ∀ (T σ : ℝ), 2 ≤ T →
      1/2 ≤ σ → σ ≤ 1 → ∀ F : Finset PrimitiveComplexCharacter,
      (∀ χ ∈ F, χ.modulus ≤ Q) →
      (∀ χ ∈ F, ∃ i, |((actualCharacterZeros χ).zeros i).im| ≤ T ∧
        σ ≤ ((actualCharacterZeros χ).zeros i).re) →
      (F.card:ℝ) ≤ C*((Q:ℝ)^2*T)^(3*(1-σ))*(Real.log ((Q:ℝ)*T))^13 := by
  obtain ⟨C,hC,h⟩ := uniform_near_one_count
  refine ⟨C,hC,?_⟩
  intro Q hQ T σ hT hσ hσ1 F hF hbad
  classical
  calc
    (F.card:ℝ) = ∑ _χ∈F,(1:ℝ) := by simp
    _ ≤ ∑ χ∈F,((actualCharacterZeros χ).count σ T:ℝ) := by
      apply Finset.sum_le_sum
      intro χ hχ
      obtain ⟨i,hi,hσi⟩ := hbad χ hχ
      have hp : 0<(actualCharacterZeros χ).count σ T := by
        apply Finset.card_pos.mpr
        exact ⟨i,Finset.mem_filter.mpr ⟨(ComplexZeroEnumeration.mem_heightIndices _ _ _).mpr hi,hσi⟩⟩
      exact_mod_cast hp
    _ ≤ _ := h Q hQ T σ hT hσ hσ1 F hF

end Factoring.Density

#print axioms OAI.Ostmann.actualCharacterZeros_respectsMultiplicity
#print axioms OAI.Ostmann.publishedComplexZeroDensity
#print axioms Factoring.Density.near_one_exponent
#print axioms Factoring.Density.uniform_near_one_count
#print axioms Factoring.Density.bad_character_count
