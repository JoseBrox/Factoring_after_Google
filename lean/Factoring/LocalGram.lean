import Factoring.Gram
import Lean.Elab.Tactic.Omega
import Mathlib.Tactic.Abel

/-! Finite local-coefficient matrices for ramified and unramified primes.
The arithmetic identification of local squareclasses and ideal-character
values is not assumed proved here; the finite matrix implications are. -/
namespace Factoring.Gram
open scoped BigOperators Matrix
variable {ι κ : Type*} [Fintype ι] [Fintype κ] [DecidableEq κ]

def indicator (c : ι → κ) (s : ι → Bool) (t : κ) (b : Bool) (i : ι) : ℝ :=
  if c i=t ∧ s i=b then 1 else 0

/-- Small-prime local Euler coefficients: split e+1, inert 0/1,
ramified 1. c labels the coset of the unramified subgroup, s its two classes. -/
def localCoeff (c : ι → κ) (s : ι → Bool) (e : ℕ) : Matrix ι ι ℝ :=
  fun i j => if c i=c j then
    if s i=s j then (e:ℝ)+1 else if e%2=0 then 1 else 0
  else 1

/-- The explicit sum of local coset blocks. -/
theorem block_sum (c : ι → κ) (s : ι → Bool) (a b : ℝ) :
    (∑ t : κ, (fun i j =>
      a*(indicator c s t false i*indicator c s t false j+
        indicator c s t true i*indicator c s t true j)+
      b*(indicator c s t false i*indicator c s t true j+
        indicator c s t true i*indicator c s t false j) : Matrix ι ι ℝ)) =
      fun i j => if c i=c j then if s i=s j then a else b else 0 := by
  classical
  ext i j
  rw [Matrix.sum_apply]
  rw [Finset.sum_eq_single (c i)]
  · by_cases h : c i=c j
    · cases hi : s i <;> cases hj : s j <;> simp [indicator,h,hi,hj,← h]
    · cases hi : s i <;> cases hj : s j <;> simp [indicator,h,Ne.symm h,hi,hj]
  · intro t _ ht
    simp [indicator,Ne.symm ht]
  · simp

/-- Every small-prime local matrix dominates the all-ones matrix in PSD order,
including arbitrary ramification and repeated classes. -/
theorem localCoeff_above_ones (c : ι → κ) (s : ι → Bool) (e : ℕ) :
    (localCoeff c s e - ones).PosSemidef := by
  classical
  let u := fun t => indicator c s t false
  let v := fun t => indicator c s t true
  by_cases he : e%2=0
  · have hpsd := sum_posSemidef Finset.univ
      (fun t : κ => (e:ℝ) • (outer (u t)+outer (v t)))
      (fun t _ => even_block_posSemidef (by positivity) (u t) (v t))
    convert hpsd using 1
    have h := block_sum c s (e:ℝ) 0
    have heq : (∑ t:κ, (e:ℝ) • (outer (u t)+outer (v t))) =
        (∑ t:κ, (fun i j =>
          (e:ℝ)*(indicator c s t false i*indicator c s t false j+
            indicator c s t true i*indicator c s t true j)+
          0*(indicator c s t false i*indicator c s t true j+
            indicator c s t true i*indicator c s t false j) : Matrix ι ι ℝ)) := by
      apply Finset.sum_congr rfl
      intro t _
      ext i j
      simp [u,v,outer]
    rw [heq,h]
    ext i j
    by_cases hc : c i=c j <;> by_cases hs : s i=s j <;>
      simp [localCoeff,ones,he,hc,hs]
  · have he' : 1≤(e:ℝ) := by exact_mod_cast (show 1≤e by omega)
    have hpsd := sum_posSemidef Finset.univ
      (fun t : κ => (((e:ℝ)-1)/2) • outer (u t+v t)+
        (((e:ℝ)+1)/2) • outer (u t-v t))
      (fun t _ => odd_block_posSemidef he' (u t) (v t))
    convert hpsd using 1
    have h := block_sum c s (e:ℝ) (-1)
    have heq : (∑ t:κ, (((e:ℝ)-1)/2) • outer (u t+v t)+
        (((e:ℝ)+1)/2) • outer (u t-v t)) =
        (∑ t:κ, (fun i j =>
          (e:ℝ)*(indicator c s t false i*indicator c s t false j+
            indicator c s t true i*indicator c s t true j)+
          (-1)*(indicator c s t false i*indicator c s t true j+
            indicator c s t true i*indicator c s t false j) : Matrix ι ι ℝ)) := by
      apply Finset.sum_congr rfl
      intro t _
      rw [odd_block_identity]
      ext i j
      simp [u,v]
      ring
    rw [heq,h]
    ext i j
    by_cases hc : c i=c j <;> by_cases hs : s i=s j <;>
      simp [localCoeff,ones,he,hc,hs]

theorem localCoeff_psd (c : ι → κ) (s : ι → Bool) (e : ℕ) :
    (localCoeff c s e).PosSemidef := by
  convert (localCoeff_above_ones c s e).add ones_posSemidef using 1
  abel

/-- Compatible edge signs on a complete splitting class have a rank-one
representation. A single pivot suffices, including a class of size one. -/
theorem triangle_rank_one {I : Type*} (α : I→I→ℝ)
    (hsq : ∀ i j, (α i j)^2=1)
    (htri : ∀ i j k, α i j*α j k*α i k=1) (k : I) :
    ∀ i j, α i j=α i k*α j k := by
  intro i j
  have h := htri i j k
  have hs : (α i k*α j k)^2=1 := by rw [mul_pow,hsq,hsq,one_mul]
  calc
    α i j = α i j*(α i k*α j k)^2 := by rw [hs,mul_one]
    _ = (α i j*α j k*α i k)*(α i k*α j k) := by ring
    _ = _ := by rw [h,one_mul]

end Factoring.Gram
