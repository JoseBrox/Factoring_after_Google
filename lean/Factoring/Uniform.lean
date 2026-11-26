import Mathlib.Algebra.Group.Subgroup.Basic
import Mathlib.Data.Fintype.Card
import Mathlib.LinearAlgebra.Dimension.RankNullity
import Mathlib.Tactic.Abel

/-! Uniform fibres and kernel projections: the exact algebraic mechanism
behind the blind-sign and sparse-kernel arguments. -/
namespace Factoring.Uniform

/-- A nonempty fibre of a group homomorphism is equivalent to its kernel. -/
def fibreEquivKer {G H : Type*} [Group G] [Group H] (f : G →* H) (g : G) :
    {x : G // f x = f g} ≃ f.ker where
  toFun x := ⟨g⁻¹*x.1, by
    rw [MonoidHom.mem_ker, map_mul, map_inv, x.property, inv_mul_cancel]⟩
  invFun x := ⟨g*x.1, by
    rw [map_mul, MonoidHom.mem_ker.mp x.property, mul_one]⟩
  left_inv x := by apply Subtype.ext; simp
  right_inv x := by apply Subtype.ext; simp

theorem fibre_card {G H : Type*} [Group G] [Group H] (f : G →* H) (g : G) :
    Nat.card {x : G // f x = f g} = Nat.card f.ker :=
  Nat.card_congr (fibreEquivKer f g)

theorem all_fibres_equal {G H : Type*} [Group G] [Group H] (f : G →* H)
    {a b : H} (ha : a ∈ Set.range f) (hb : b ∈ Set.range f) :
    Nat.card {x : G // f x = a} = Nat.card {x : G // f x = b} := by
  obtain ⟨g,rfl⟩ := ha
  obtain ⟨h,rfl⟩ := hb
  rw [fibre_card, fibre_card]

section Linear

variable {K V W : Type*} [Field K] [AddCommGroup V] [AddCommGroup W]
  [Module K V] [Module K W]

/-- A linear map L that lifts the image of A defines an actual projection
onto ker A. In the sparse algorithm L is built from the diagonal
preconditioner and the inverse on the image. -/
def kernelProjection (A : V →ₗ[K] W) (L : W →ₗ[K] V)
    (h : ∀ v, A (L (A v)) = A v) : V →ₗ[K] LinearMap.ker A :=
  (LinearMap.id - L.comp A).codRestrict (LinearMap.ker A) (by
    intro v
    change A (v-L (A v)) = 0
    rw [map_sub,h,sub_self])

theorem projection_on_kernel (A : V →ₗ[K] W) (L : W →ₗ[K] V)
    (h : ∀ v, A (L (A v)) = A v) (v : LinearMap.ker A) :
    kernelProjection A L h v.1 = v := by
  apply Subtype.ext
  change v.1-L (A v.1)=v.1
  rw [LinearMap.mem_ker.mp v.property,map_zero,sub_zero]

theorem projection_surjective (A : V →ₗ[K] W) (L : W →ₗ[K] V)
    (h : ∀ v, A (L (A v)) = A v) :
    Function.Surjective (kernelProjection A L h) :=
  fun v => ⟨v.1,projection_on_kernel A L h v⟩

/-- Every fibre of the projection has the same size; this gives uniformity
for uniform finite-domain input without assuming independent verification. -/
theorem projection_fibres_equal (A : V →ₗ[K] W) (L : W →ₗ[K] V)
    (h : ∀ v, A (L (A v)) = A v) (x y : LinearMap.ker A) :
    Nat.card {v : V // kernelProjection A L h v = x} =
      Nat.card {v : V // kernelProjection A L h v = y} := by
  let f := kernelProjection A L h
  let e : {v : V // f v = x} ≃ {v : V // f v = y} :=
    { toFun := fun v => ⟨v.1-x.1+y.1, by
        rw [map_add,map_sub,v.property,projection_on_kernel A L h x,
          projection_on_kernel A L h y,sub_self,zero_add]⟩
      invFun := fun v => ⟨v.1-y.1+x.1, by
        rw [map_add,map_sub,v.property,projection_on_kernel A L h y,
          projection_on_kernel A L h x,sub_self,zero_add]⟩
      left_inv := fun v => by apply Subtype.ext; dsimp; abel
      right_inv := fun v => by apply Subtype.ext; dsimp; abel }
  exact Nat.card_congr e

end Linear
end Factoring.Uniform
