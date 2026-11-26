import Mathlib.RingTheory.DedekindDomain.Factorization
import Mathlib.NumberTheory.NumberField.Basic
import Mathlib.Tactic

/-! Integral-normalized valuations of actual principal fractional ideals.
This formalizes the exact cancellation of the nonmonic offset, then
recovers an integral unit when all prime-ideal valuations vanish. -/
namespace Factoring.IdealCancellation
open IsDedekindDomain
open scoped nonZeroDivisors BigOperators

variable {R K : Type*} [CommRing R] [Field K] [Algebra R K]
  [IsFractionRing R K] [IsDedekindDomain R]

noncomputable def principal : K →* FractionalIdeal R⁰ K where
  toFun := FractionalIdeal.spanSingleton R⁰
  map_one' := FractionalIdeal.spanSingleton_one
  map_mul' x y := (FractionalIdeal.spanSingleton_mul_spanSingleton x y).symm

theorem principal_ne_zero (x : K) (hx : x≠0) :
    principal (R:=R) x≠0 :=
  FractionalIdeal.spanSingleton_ne_zero_iff.mpr hx

noncomputable def val (v : HeightOneSpectrum R) (x : K) : ℤ :=
  FractionalIdeal.count K v (principal (R:=R) x)

theorem val_mul (v : HeightOneSpectrum R) {x y : K}
    (hx : x≠0) (hy : y≠0) : val v (x*y)=val v x+val v y := by
  unfold val
  rw [map_mul,FractionalIdeal.count_mul K v
    (principal_ne_zero x hx) (principal_ne_zero y hy)]

theorem principal_zpow (x : K) (n : ℤ) :
    principal (R:=R) (x^n) = (principal (R:=R) x)^n := by
  cases n with
  | ofNat n => simp only [Int.ofNat_eq_coe,zpow_natCast,map_pow]
  | negSucc n =>
    have he : Int.negSucc n = -((n+1:ℕ):ℤ) := by omega
    rw [he,zpow_neg,zpow_neg,zpow_natCast,zpow_natCast]
    change FractionalIdeal.spanSingleton R⁰ ((x^(n+1))⁻¹) =
      ((principal (R:=R) x)^(n+1))⁻¹
    rw [← FractionalIdeal.spanSingleton_inv]
    change ((principal (R:=R) (x^(n+1)))⁻¹) = _
    rw [map_pow]

theorem val_zpow (v : HeightOneSpectrum R) (x : K) (n : ℤ) :
    val v (x^n)=n*val v x := by
  unfold val
  rw [principal_zpow,FractionalIdeal.count_zpow]

theorem val_prod {I : Type*} (v : HeightOneSpectrum R) (s : Finset I) (x : I→K)
    (hx : ∀ i∈s,x i≠0) : val v (∏ i∈s,x i)=∑ i∈s,val v (x i) := by
  unfold val
  rw [map_prod]
  exact FractionalIdeal.count_prod K v s _ (fun i hi => principal_ne_zero _ (hx i hi))

/-- All valuations vanish exactly when the actual nonzero principal
fractional ideal is the unit ideal. -/
theorem principal_eq_one (x : K) (hx : x≠0)
    (h : ∀ v : HeightOneSpectrum R,val v x=0) :
    principal (R:=R) x=1 := by
  rw [← FractionalIdeal.finprod_heightOneSpectrum_factorization' K (principal_ne_zero x hx)]
  simp_rw [← show ∀ v : HeightOneSpectrum R,
    val v x=FractionalIdeal.count K v (principal (R:=R) x) from fun _=>rfl,h,zpow_zero]
  simp

theorem unit_of_zero (x : K) (hx : x≠0)
    (h : ∀ v : HeightOneSpectrum R,val v x=0) :
    ∃ u : Rˣ, algebraMap R K (u:R)=x := by
  have he : FractionalIdeal.spanSingleton R⁰ (1:K)=FractionalIdeal.spanSingleton R⁰ x := by
    rw [FractionalIdeal.spanSingleton_one]
    exact (principal_eq_one x hx h).symm
  obtain ⟨u,hu⟩ := FractionalIdeal.spanSingleton_eq_spanSingleton.mp he
  change (u:R) • (1:K)=x at hu
  exact ⟨u,by simpa [Algebra.smul_def] using hu⟩

noncomputable def adjusted (v : HeightOneSpectrum R) (θ x : K) : ℤ :=
  val v x-min 0 (val v θ)

/-- The top row of the valuation matrix cancels the nonmonic offset.
The target p-power may be any field element; the clean-label
identifications with rational-prime valuations remain separate. -/
theorem offset_cancel {I : Type*} [Fintype I]
    (θ p : K) (hp : p≠0) (x : I→K) (hx : ∀ i,x i≠0) (c : I→ℤ)
    (E : ℕ) (htop : ∑ i,c i=0)
    (h : ∀ v : HeightOneSpectrum R,
      ∑ i,c i*adjusted v θ (x i)=-(E:ℤ)*val v p) :
    ∃ u : Rˣ, algebraMap R K (u:R)=p^E*(∏ i,x i^c i) := by
  have hx' : ∀ i : I,x i^c i≠0 := fun i=>zpow_ne_zero _ (hx i)
  have hprod : (∏ i,x i^c i)≠0 :=
    Finset.prod_ne_zero_iff.mpr fun i _=>hx' i
  apply unit_of_zero _ (mul_ne_zero (pow_ne_zero _ hp) hprod)
  intro v
  rw [val_mul v (pow_ne_zero _ hp) hprod,val_prod v _ _ (fun i _=>hx' i)]
  simp_rw [val_zpow]
  have hpow : val v (p^E)=(E:ℤ)*val v p := by
    simpa only [zpow_natCast] using val_zpow v p (E:ℤ)
  rw [hpow]
  have he := h v
  unfold adjusted at he
  simp_rw [mul_sub] at he
  rw [Finset.sum_sub_distrib,←Finset.sum_mul,htop,zero_mul,sub_zero] at he
  rw [he]
  ring

end Factoring.IdealCancellation

