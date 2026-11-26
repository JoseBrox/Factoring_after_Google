import Factoring.BitArithmetic

/-! Binary long remainder using ripple-borrow cells. All computation on
the digits is Boolean; Nat arithmetic in the proof is a specification.
The cost model charges a linear number of bit cells per input digit,
including the fixed-width select and truncation passes. -/
namespace Factoring.BitArithmetic

def fullSub (a b c : Bool) : Bool × Bool :=
  (xorBit (xorBit a b) c, (!a && (b || c)) || (b && c))

theorem fullSub_spec (a b c : Bool) :
    bit a + 2 * bit (fullSub a b c).2 = bit b + bit c + bit (fullSub a b c).1 := by
  cases a <;> cases b <;> cases c <;> decide

def subAux : ℕ → List Bool → List Bool → Bool → List Bool × Bool
  | 0, _, _, c => ([], c)
  | n+1, xs, ys, c =>
    let s := fullSub (headBit xs) (headBit ys) c
    let r := subAux n xs.tail ys.tail s.2
    (s.1 :: r.1, r.2)

theorem subAux_length (n : ℕ) (xs ys : List Bool) (c : Bool) :
    (subAux n xs ys c).1.length = n := by
  induction n generalizing xs ys c with
  | zero => rfl
  | succ n ih =>
    simp [subAux, ih]

theorem subAux_spec (n : ℕ) (xs ys : List Bool) (c : Bool)
    (hx : xs.length ≤ n) (hy : ys.length ≤ n) :
    value xs + 2^n * bit (subAux n xs ys c).2 =
      value ys + bit c + value (subAux n xs ys c).1 := by
  induction n generalizing xs ys c with
  | zero => cases xs <;> cases ys <;> simp_all [subAux, value]
  | succ n ih =>
    have hxs : xs.tail.length ≤ n := by cases xs <;> simp_all
    have hys : ys.tail.length ≤ n := by cases ys <;> simp_all
    let s := fullSub (headBit xs) (headBit ys) c
    let r := subAux n xs.tail ys.tail s.2
    have hi : value xs.tail + 2^n * bit r.2 =
        value ys.tail + bit s.2 + value r.1 := ih _ _ _ hxs hys
    have hs : bit (headBit xs) + 2 * bit s.2 =
        bit (headBit ys) + bit c + bit s.1 := fullSub_spec _ _ _
    change value xs + 2^(n+1)*bit r.2 =
      value ys + bit c + (bit s.1 + 2*value r.1)
    rw [value_uncons xs, value_uncons ys, pow_succ]
    rw [show (2^n*2)*bit r.2=2*(2^n*bit r.2) by ring]
    omega

theorem value_take_drop (n : ℕ) (xs : List Bool) :
    value xs = value (xs.take n) + 2^n * value (xs.drop n) := by
  induction n generalizing xs with
  | zero => simp [value]
  | succ n ih =>
    cases xs with
    | nil => simp [value]
    | cons b xs =>
      simp only [List.take_succ_cons, List.drop_succ_cons, value, pow_succ]
      have h := ih xs
      rw [h]
      ring

theorem value_take_of_lt (n : ℕ) (xs : List Bool) (h : value xs < 2^n) :
    value (xs.take n) = value xs := by
  have he := value_take_drop n xs
  have hz : value (xs.drop n)=0 := by
    by_contra hn
    have hh : 2^n*1 ≤ 2^n*value (xs.drop n) := Nat.mul_le_mul_left _ (by omega)
    omega
  rw [hz,mul_zero,add_zero] at he
  exact he.symm

theorem value_zeros (n : ℕ) : value (List.replicate n false) = 0 := by
  induction n with
  | zero => rfl
  | succ n ih => simp [List.replicate_succ,value,bit,ih]

/-- One step of long remainder. If the subtraction borrows, keep the
shifted residue. Otherwise use the difference. The final take removes
only the redundant top bit under the remainder invariant. -/
def remainderStep (modulus r : List Bool) (b : Bool) : List Bool :=
  let shifted := b :: r
  let d := subAux (modulus.length+1) shifted modulus false
  (if d.2 then shifted else d.1).take modulus.length

theorem remainderStep_spec (modulus r : List Bool) (b : Bool)
    (hr : value r<value modulus)
    (hlen : r.length=modulus.length) :
    (remainderStep modulus r b).length=modulus.length ∧
    value (remainderStep modulus r b)=(bit b+2*value r)%value modulus := by
  let n := modulus.length
  let s := b :: r
  let d := subAux (n+1) s modulus false
  have hSlen : s.length=n+1 := by simp [s,n,hlen]
  have hDlen : d.1.length=n+1 := subAux_length _ _ _ _
  have hD : value s + 2^(n+1)*bit d.2 = value modulus + value d.1 := by
    simpa [bit] using subAux_spec (n+1) s modulus false (by omega) (by simp [n])
  have hs : value s=bit b+2*value r := rfl
  have hb : bit b≤1 := by cases b <;> decide
  have hsmall : value s<2*value modulus := by omega
  have hmod : value modulus<2^n := value_lt _
  have hdiff : value d.1<2^(n+1) := by simpa only [hDlen] using value_lt d.1
  change ((if d.2 then s else d.1).take n).length = n ∧
    value ((if d.2 then s else d.1).take n) = (bit b+2*value r)%value modulus
  cases hborrow : d.2 with
  | false =>
    rw [if_neg (by simp [hborrow]), List.length_take, hDlen]
    have hde : value s=value modulus+value d.1 := by simpa [hborrow,bit] using hD
    have hdl : value d.1<value modulus := by omega
    constructor
    · omega
    · rw [value_take_of_lt n _ (hdl.trans hmod), ← hs, hde, Nat.add_mod]
      simp [Nat.mod_eq_of_lt hdl]
  | true =>
    rw [if_pos (by simp [hborrow]), List.length_take, hSlen]
    have hde : value s+2^(n+1)=value modulus+value d.1 := by simpa [hborrow,bit] using hD
    have hsl : value s<value modulus := by omega
    constructor
    · omega
    · rw [value_take_of_lt n _ (hsl.trans hmod), ← hs, Nat.mod_eq_of_lt hsl]

def remainderBits (modulus : List Bool) : List Bool → List Bool
  | [] => List.replicate modulus.length false
  | b :: xs => remainderStep modulus (remainderBits modulus xs) b

theorem remainderBits_spec (modulus xs : List Bool) (hm : 0<value modulus) :
    (remainderBits modulus xs).length=modulus.length ∧
      value (remainderBits modulus xs)=value xs%value modulus := by
  induction xs with
  | nil => simp [remainderBits,value_zeros,value]
  | cons b xs ih =>
    have hr : value (remainderBits modulus xs)<value modulus := by
      rw [ih.2]
      exact Nat.mod_lt _ hm
    have h := remainderStep_spec modulus (remainderBits modulus xs) b hr ih.1
    constructor
    · exact h.1
    · change value (remainderStep modulus (remainderBits modulus xs) b) =
        (bit b+2*value xs)%value modulus
      rw [h.2,ih.2]
      have he : (bit b+2*(value xs%value modulus))%value modulus =
          (bit b+2*value xs)%value modulus := by
        rw [Nat.add_mod (bit b) (2*(value xs%value modulus)), Nat.add_mod (bit b) (2*value xs)]
        rw [Nat.mul_mod 2 (value xs%value modulus), Nat.mul_mod 2 (value xs)]
        rw [Nat.mod_mod]
      exact he

/-- Bit-cell accounting: zero initialization plus one full fixed-width
subtraction, shift, selection and truncation per input bit. This charges
the loops over digit lists, not the compiler's Nat implementation. -/
def remainderCost (width input : ℕ) : ℕ := width+input*(4*width+8)

theorem remainderCost_succ (width input : ℕ) :
    remainderCost width (input+1)=remainderCost width input+(4*width+8) := by
  unfold remainderCost
  ring

/-- A modular multiplication program using the certified schoolbook
multiply and the long remainder, with fixed-width output. -/
def mulModBits (modulus xs ys : List Bool) : List Bool :=
  remainderBits modulus (mulBits xs ys).1

theorem mulModBits_spec (modulus xs ys : List Bool) (hm : 0<value modulus) :
    (mulModBits modulus xs ys).length=modulus.length ∧
    value (mulModBits modulus xs ys)= (value xs*value ys)%value modulus := by
  simpa [mulModBits,mul_value] using remainderBits_spec modulus (mulBits xs ys).1 hm

def mulModCost (modulus xs ys : List Bool) : ℕ :=
  (mulBits xs ys).2 + remainderCost modulus.length (mulBits xs ys).1.length

theorem mulModCost_le (modulus xs ys : List Bool)
    (hx : xs.length≤modulus.length) (hy : ys.length≤modulus.length) :
    mulModCost modulus xs ys ≤ 16*modulus.length^2+27*modulus.length := by
  let n := modulus.length
  have hL := mul_length xs ys
  have hC := mul_cost_le xs ys
  have hlen : (mulBits xs ys).1.length≤3*n := by omega
  have hmul : (mulBits xs ys).2≤n*(3*n+2) := by
    apply hC.trans
    exact Nat.mul_le_mul hx (by omega)
  have hrem : (mulBits xs ys).1.length*(4*n+8)≤(3*n)*(4*n+8) :=
    Nat.mul_le_mul_right _ hlen
  unfold mulModCost remainderCost
  change (mulBits xs ys).2+(n+(mulBits xs ys).1.length*(4*n+8))≤16*n^2+27*n
  nlinarith

end Factoring.BitArithmetic

#print axioms Factoring.BitArithmetic.fullSub_spec
#print axioms Factoring.BitArithmetic.subAux_length
#print axioms Factoring.BitArithmetic.subAux_spec
#print axioms Factoring.BitArithmetic.value_take_drop
#print axioms Factoring.BitArithmetic.value_take_of_lt
#print axioms Factoring.BitArithmetic.value_zeros
#print axioms Factoring.BitArithmetic.remainderStep_spec
#print axioms Factoring.BitArithmetic.remainderBits_spec
#print axioms Factoring.BitArithmetic.remainderCost_succ
#print axioms Factoring.BitArithmetic.mulModBits_spec
#print axioms Factoring.BitArithmetic.mulModCost_le
