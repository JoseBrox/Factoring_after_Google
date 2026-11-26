import Mathlib.Data.Int.GCD
import Mathlib.Data.ZMod.Basic
import Mathlib.Tactic

/-! The primitive rational-root linear fibre, over integers and over
arbitrary residue rings. The cardinality theorem applies to qp² even
when a coefficient is divisible by p. -/
namespace Factoring.PrimitiveFibre

/-- The unimodular Bezout change of coordinates gives every fibre
exactly one free coordinate; no coefficient need be a unit. -/
def fibreEquiv {R : Type*} [CommRing R] (a b u v z : R)
    (h : a*u+b*v=1) : {p : R×R // a*p.2-b*p.1=z} ≃ R where
  toFun p := u*p.val.1+v*p.val.2
  invFun t := ⟨(a*t-v*z,b*t+u*z),by dsimp; linear_combination z*h⟩
  left_inv p := by
    apply Subtype.ext
    apply Prod.ext
    · change a*(u*p.val.1+v*p.val.2)-v*z=p.val.1
      linear_combination p.val.1*h+v*p.property
    · change b*(u*p.val.1+v*p.val.2)+u*z=p.val.2
      linear_combination p.val.2*h-u*p.property
  right_inv t := by
    change u*(a*t-v*z)+v*(b*t+u*z)=t
    linear_combination t*h

/-- Any primitive integer pair gives the requisite Bezout identity. -/
theorem bezout (a b : ℤ) (h : a.gcd b=1) :
    a*(a.gcdA b)+b*(a.gcdB b)=1 := by
  simpa [h] using (Int.gcd_eq_gcd_ab a b).symm

/-- Two integer points in the same fibre differ by an integral multiple
of the primitive direction. This is the actual rational-root fibre
used in the second-moment argument. -/
theorem integer_fibre (a b x y x' y' : ℤ) (h : a.gcd b=1)
    (he : a*y-b*x=a*y'-b*x') :
    ∃ t : ℤ, x'=x+a*t ∧ y'=y+b*t := by
  let u := a.gcdA b
  let v := a.gcdB b
  have hb : a*u+b*v=1 := bezout a b h
  refine ⟨u*(x'-x)+v*(y'-y),?_ ,?_⟩
  · linear_combination -(x'-x)*hb+v*he
  · linear_combination -(y'-y)*hb-u*he

/-- The exact size of a primitive linear congruence fibre modulo any
positive modulus, including a composite modulus with repeated primes. -/
theorem residue_fibre_card (m : ℕ) [NeZero m] (a b : ℤ) (h : a.gcd b=1)
    (z : ZMod m) :
    Fintype.card {p : ZMod m×ZMod m //
      (a:ZMod m)*p.2-(b:ZMod m)*p.1=z}=m := by
  classical
  have hb : (a:ZMod m)*(a.gcdA b:ZMod m)+(b:ZMod m)*(a.gcdB b:ZMod m)=1 := by
    exact_mod_cast bezout a b h
  have hc := Fintype.card_congr (fibreEquiv (a:ZMod m) (b:ZMod m)
    (a.gcdA b:ZMod m) (a.gcdB b:ZMod m) z hb)
  simpa using hc

end Factoring.PrimitiveFibre

#print axioms Factoring.PrimitiveFibre.bezout
#print axioms Factoring.PrimitiveFibre.integer_fibre
#print axioms Factoring.PrimitiveFibre.residue_fibre_card
