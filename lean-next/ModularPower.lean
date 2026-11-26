import Factoring.ModularBits

/-! Binary modular exponentiation with an explicit digit-list algorithm.
The per-bit cost is composed from the certified modular multiplication
cell budget. The tape implementation of loop counters and gcd remains
a distinct obligation. -/
namespace Factoring.BitArithmetic

def powModBits (modulus base : List Bool) : List Bool → List Bool
  | [] => remainderBits modulus [true]
  | b :: es =>
    let r := powModBits modulus base es
    let sq := mulModBits modulus r r
    if b then mulModBits modulus sq base else sq

theorem powModBits_spec (modulus base es : List Bool) (hm : 0<value modulus) :
    (powModBits modulus base es).length=modulus.length ∧
      value (powModBits modulus base es)=value base ^ value es % value modulus := by
  induction es with
  | nil =>
    simpa [powModBits,value,bit] using remainderBits_spec modulus [true] hm
  | cons b es ih =>
    let r := powModBits modulus base es
    let sq := mulModBits modulus r r
    have hs := mulModBits_spec modulus r r hm
    have hsval : value sq = value base ^ (2*value es) % value modulus := by
      change value (mulModBits modulus r r) = _
      rw [hs.2,show value r=value base^value es%value modulus from ih.2]
      rw [←Nat.mul_mod, Nat.mul_comm 2 (value es),pow_mul,pow_two]
    have hslen : sq.length=modulus.length := hs.1
    cases b with
    | false =>
      change sq.length=modulus.length ∧ value sq=value base ^ (bit false+2*value es)%value modulus
      exact ⟨hslen,by simpa [bit] using hsval⟩
    | true =>
      change (mulModBits modulus sq base).length=modulus.length ∧
        value (mulModBits modulus sq base)=value base^(bit true+2*value es)%value modulus
      have hh := mulModBits_spec modulus sq base hm
      refine ⟨hh.1,?_⟩
      rw [hh.2,hsval,Nat.mul_mod (value base ^ (2*value es)%value modulus) (value base),Nat.mod_mod,←Nat.mul_mod]
      simp only [bit,if_true,pow_add,pow_one]
      rw [mul_comm]

def powModCost (modulus base : List Bool) : List Bool → ℕ
  | [] => remainderCost modulus.length 1
  | b :: es =>
    let r := powModBits modulus base es
    let sq := mulModBits modulus r r
    powModCost modulus base es + mulModCost modulus r r +
      if b then mulModCost modulus sq base else 0

theorem powModCost_le (modulus base es : List Bool) (hm : 0<value modulus)
    (hb : base.length≤modulus.length) :
    powModCost modulus base es ≤ remainderCost modulus.length 1+
      2*es.length*(16*modulus.length^2+27*modulus.length) := by
  let n := modulus.length
  let C := 16*n^2+27*n
  induction es with
  | nil => simp [powModCost]
  | cons b es ih =>
    let r := powModBits modulus base es
    let sq := mulModBits modulus r r
    have hr : r.length=n := (powModBits_spec modulus base es hm).1
    have hs : sq.length=n := (mulModBits_spec modulus r r hm).1
    have h1 : mulModCost modulus r r ≤ C := mulModCost_le modulus r r (by omega) (by omega)
    have h2 : mulModCost modulus sq base ≤ C := mulModCost_le modulus sq base (by omega) hb
    have hi : powModCost modulus base es≤remainderCost n 1+2*es.length*C := ih
    change powModCost modulus base es+mulModCost modulus r r+
      (if b then mulModCost modulus sq base else 0)≤remainderCost n 1+2*(es.length+1)*C
    cases b <;> simp only [Bool.false_eq_true,if_false,if_true] <;> nlinarith

end Factoring.BitArithmetic

#print axioms Factoring.BitArithmetic.powModBits_spec
#print axioms Factoring.BitArithmetic.powModCost_le
