import Factoring.ChainSuccess
import Mathlib.Data.Fintype.BigOperators
import Mathlib.NumberTheory.LegendreSymbol.QuadraticChar.Basic

/-! The exact successful-residue lower bound for the mixed-prime chain.
The finite probability is represented by the cardinality of the successful
subset of Fin N; this does not assume independent choices of the prime
components or require N to be squarefree. -/
open scoped BigOperators
namespace Factoring.Quadratic

/-- The hyperbola (a-y)(a+y)=b, parametrized by a nonzero first factor. -/
def hyperbolaEquiv {F : Type*} [Field F] (b : F) (hb : b ≠ 0) (h2 : (2:F) ≠ 0) :
    {z : F × F // z.2^2=z.1^2-b} ≃ Fˣ where
  toFun z := Units.mk0 (z.1.1-z.1.2) (by
    intro hz
    have hh := sub_eq_zero.mp hz
    have he := z.2
    rw [← hh] at he
    apply hb
    linear_combination he)
  invFun t := ⟨(((t:F)+b/(t:F))/2,(b/(t:F)-(t:F))/2), by
    have ht : (t:F) ≠ 0 := Units.ne_zero t
    field_simp [ht,h2]; ring⟩
  left_inv z := by
    have hprod : (z.1.1-z.1.2)*(z.1.1+z.1.2)=b := by
      linear_combination -z.2
    have ht : z.1.1-z.1.2 ≠ 0 := by
      intro h
      apply hb
      simpa [h] using hprod.symm
    have hd : b/(z.1.1-z.1.2)=z.1.1+z.1.2 :=
      (div_eq_iff ht).mpr (by rw [_root_.mul_comm]; exact hprod.symm)
    apply Subtype.ext
    apply Prod.ext
    · change (z.1.1-z.1.2+b/(z.1.1-z.1.2))/2=z.1.1
      rw [hd]
      apply (div_eq_iff h2).mpr
      ring
    · change (b/(z.1.1-z.1.2)-(z.1.1-z.1.2))/2=z.1.2
      rw [hd]
      apply (div_eq_iff h2).mpr
      ring
  right_inv t := by
    apply Units.ext
    change ((t:F)+b/(t:F))/2-(b/(t:F)-(t:F))/2=(t:F)
    field_simp [h2]; ring

def sigmaHyperbola {F : Type*} [Field F] (b : F) :
    (Σ a : F, {y : F // y^2=a^2-b}) ≃ {z : F×F // z.2^2=z.1^2-b} where
  toFun z := ⟨(z.1,z.2.1),z.2.2⟩
  invFun z := ⟨z.1.1,⟨z.1.2,z.2⟩⟩
  left_inv := by rintro ⟨a,y,hy⟩; rfl
  right_inv := by rintro ⟨⟨a,y⟩,hy⟩; rfl

/-- A good residue has either zero norm or nonsquare norm.
The complement is written this way so that counting uses subtype complements. -/
def Good {F : Type*} [Field F] (b a : F) : Prop :=
  ¬(a^2-b ≠ 0 ∧ IsSquare (a^2-b))

/-- Exactly (|F|+3)/2 residues are guaranteed to succeed at the split prime. -/
theorem good_count {F : Type*} [Field F] [Fintype F] (b r : F)
    (hr : r^2=b) (hr0 : r ≠ 0) (h2 : (2:F) ≠ 0) (hchar : ringChar F ≠ 2) :
    2*Nat.card {a : F // Good b a}=Fintype.card F+3 := by
  classical
  have hb : b ≠ 0 := by rw [← hr]; exact pow_ne_zero _ hr0
  let bad (a:F) := a^2-b ≠ 0 ∧ IsSquare (a^2-b)
  let zeroNorm (a:F) := a^2-b=0
  have hsum : (∑ a:F, Fintype.card {y:F // y^2=a^2-b})=Fintype.card F-1 := by
    simpa only [Fintype.card_sigma,Fintype.card_units] using
      Fintype.card_congr ((sigmaHyperbola b).trans (hyperbolaEquiv b hb h2))
  have hterm (a:F) : Fintype.card {y:F // y^2=a^2-b} =
      (if bad a then 2 else 0)+(if zeroNorm a then 1 else 0) := by
    have hc := quadraticChar_card_sqrts hchar (a^2-b)
    have hc' : (Fintype.card {y:F // y^2=a^2-b} : ℤ) = quadraticChar F (a^2-b)+1 := by
      rw [Fintype.card_subtype]
      simpa only [Set.toFinset_setOf] using hc
    by_cases hz : a^2-b=0
    · have hh : quadraticChar F (a^2-b)=0 := by rw [hz,quadraticChar_zero]
      rw [hh] at hc'
      simp [bad,zeroNorm,hz]
    · by_cases hs : IsSquare (a^2-b)
      · rw [(quadraticChar_one_iff_isSquare hz).mpr hs] at hc'
        simp [bad,zeroNorm,hz,hs] <;> omega
      · rw [quadraticChar_neg_one_iff_not_isSquare.mpr hs] at hc'
        simp [bad,zeroNorm,hz,hs] <;> omega
  have hsum' : (∑ a:F, Fintype.card {y:F // y^2=a^2-b}) =
      2*Fintype.card {a:F // bad a}+Fintype.card {a:F // zeroNorm a} := by
    calc
      _ = ∑ a:F, ((if bad a then 2 else 0)+(if zeroNorm a then 1 else 0)) :=
        Finset.sum_congr rfl fun a _ => hterm a
      _ = _ := by
        rw [Finset.sum_add_distrib, ← Finset.sum_filter, ← Finset.sum_filter]
        rw [Fintype.card_subtype, Fintype.card_subtype]
        simp [Nat.mul_comm]
  have hrneg : r ≠ -r := fun hh => hr0 ((Ring.eq_self_iff_eq_zero_of_char_ne_two hchar).mp hh.symm)
  have hzset : Finset.univ.filter zeroNorm = ({r,-r}:Finset F) := by
    ext a
    simp only [zeroNorm,Finset.mem_filter,Finset.mem_univ,true_and,sub_eq_zero,← hr,
      sq_eq_sq_iff_eq_or_eq_neg,Finset.mem_insert,Finset.mem_singleton]
  have hzcard : Fintype.card {a:F // zeroNorm a}=2 := by
    rw [Fintype.card_subtype,hzset,Finset.card_pair hrneg]
  have hcomp := Fintype.card_subtype_compl bad
  have hle := Fintype.card_subtype_le bad
  have hpos : 0 < Fintype.card F := Fintype.card_pos
  have hcg : Nat.card {a:F // ¬bad a} = Fintype.card {a:F // ¬bad a} :=
    Nat.card_eq_fintype_card
  change 2*Nat.card {a:F // ¬bad a}=Fintype.card F+3
  rw [hcg]
  omega

/-- The actual uniform trial on Fin N, counted by injecting every good residue
and every representative in its fibre into the program's successful inputs. -/
theorem mixed_success_count {N b u steps p q : ℕ} [NeZero N] [Fact p.Prime] [Fact q.Prime]
    (hp : p ∣ N) (hq : q ∣ N) (hpodd : p%2=1)
    (hp2 : (2 : ZMod p) ≠ 0) (hq2 : (2 : ZMod q) ≠ 0)
    (r : ZMod p) (hr : r*r=(b : ZMod p)) (hr0 : r ≠ 0)
    (hnonsquare : ∀ x : ZMod q, x*x ≠ (b : ZMod q))
    (hu : Odd u) (hdiv : p-1 ∣ 2^steps*u) :
    2*p*Nat.card {a : Fin N // split N b a.val u steps ≠ none} ≥ (p+3)*N := by
  classical
  obtain ⟨k,hk⟩ := hp
  have hp : p ∣ N := ⟨k,hk⟩
  let S := {a : ZMod p // Good (b : ZMod p) a}
  let T := {a : Fin N // split N b a.val u steps ≠ none}
  have hcast (a : ZMod p) (i : Fin k) :
      ((a.val+p*i.val : ℕ) : ZMod p)=a := by
    simp [Nat.cast_add,Nat.cast_mul,ZMod.natCast_zmod_val]
  let f : S×Fin k → T := fun ai =>
    let a := ai.1.1
    let i := ai.2
    ⟨⟨a.val+p*i.val, by
      rw [hk]
      calc
        _ < p+p*i.val := Nat.add_lt_add_right a.val_lt _
        _ = p*(i.val+1) := by ring
        _ ≤ p*k := Nat.mul_le_mul_left _ (Nat.succ_le_of_lt i.isLt)⟩, by
      have hgood : a*a-(b : ZMod p)=0 ∨ ¬IsSquare (a*a-(b : ZMod p)) := by
        by_cases hz : a*a-(b : ZMod p)=0
        · exact Or.inl hz
        · right
          intro hs
          exact ai.1.2 ⟨by simpa [pow_two] using hz,by simpa [pow_two] using hs⟩
      obtain ⟨d,hd,_⟩ := mixed_success (a := a.val+p*i.val) hp hq hpodd hp2 hq2
        r hr hr0 hnonsquare hu hdiv (by rw [hcast]; exact hgood)
      change split N b (a.val+p*i.val) u steps ≠ none
      rw [hd]
      simp⟩
  have hf : Function.Injective f := by
    intro x y he
    have hval : x.1.1.val+p*x.2.val=y.1.1.val+p*y.2.val :=
      congrArg (fun z:T => z.1.val) he
    have ha : x.1.1=y.1.1 := by
      have hh := congrArg (fun n : ℕ => (n : ZMod p)) hval
      dsimp only at hh
      simpa only [hcast] using hh
    have hi : x.2.val=y.2.val := by
      rw [ha] at hval
      exact mul_left_cancel₀ (Fact.out : p.Prime).ne_zero (Nat.add_left_cancel hval)
    exact Prod.ext (Subtype.ext ha) (Fin.ext hi)
  have hle : Nat.card S*k ≤ Nat.card T := by
    rw [Nat.card_eq_fintype_card,Nat.card_eq_fintype_card]
    simpa only [Fintype.card_prod,Fintype.card_fin] using Fintype.card_le_of_injective f hf
  have hgood := good_count (b : ZMod p) r (by rw [pow_two,hr]) hr0 hp2
    (by rw [ZMod.ringChar_zmod_n]; omega)
  rw [ZMod.card] at hgood
  change 2*Nat.card S=p+3 at hgood
  change (p+3)*N ≤ 2*p*Nat.card T
  rw [hk, ← hgood]
  calc
    _ = 2*p*(Nat.card S*k) := by ring
    _ ≤ _ := Nat.mul_le_mul_left _ hle

end Factoring.Quadratic
