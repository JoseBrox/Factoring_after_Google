import Factoring.ChainCost
import Mathlib.Tactic.Linarith

/-! Candidate executable little-endian bit arithmetic. The second component
counts adder cells and multiplier shift steps. It is not a certificate for
Lean's Nat implementation, division, gcd, or the full factoring program. -/
namespace Factoring.BitArithmetic

def bit (b : Bool) : ℕ := if b then 1 else 0

def value : List Bool → ℕ
  | [] => 0
  | b :: bs => bit b + 2 * value bs

def headBit : List Bool → Bool
  | [] => false
  | b :: _ => b

def xorBit (a b : Bool) : Bool := if a then !b else b

def fullAdder (a b c : Bool) : Bool × Bool :=
  (xorBit (xorBit a b) c, (a && b) || ((a || b) && c))

theorem fullAdder_spec (a b c : Bool) :
    bit (fullAdder a b c).1 + 2 * bit (fullAdder a b c).2 =
      bit a + bit b + bit c := by
  cases a <;> cases b <;> cases c <;> decide

theorem value_uncons (xs : List Bool) :
    value xs = bit (headBit xs) + 2 * value xs.tail := by
  cases xs <;> simp [value, headBit, bit]

theorem value_lt (xs : List Bool) : value xs < 2^xs.length := by
  induction xs with
  | nil => decide
  | cons b xs ih =>
    cases b <;> simp [value, bit, pow_succ] <;> omega

/-- Fuel is the maximum input length, with one final output carry.
The cost counts a full-adder cell for each fuel step and the final carry. -/
def addAux : ℕ → List Bool → List Bool → Bool → List Bool × ℕ
  | 0, _, _, c => ([c], 1)
  | n+1, xs, ys, c =>
    let s := fullAdder (headBit xs) (headBit ys) c
    let r := addAux n xs.tail ys.tail s.2
    (s.1 :: r.1, r.2 + 1)

theorem addAux_value (n : ℕ) (xs ys : List Bool) (c : Bool)
    (hx : xs.length ≤ n) (hy : ys.length ≤ n) :
    value (addAux n xs ys c).1 = value xs + value ys + bit c := by
  induction n generalizing xs ys c with
  | zero =>
    cases xs <;> cases ys <;> simp_all [addAux, value]
  | succ n ih =>
    have hxs : xs.tail.length ≤ n := by cases xs <;> simp_all <;> omega
    have hys : ys.tail.length ≤ n := by cases ys <;> simp_all <;> omega
    let s := fullAdder (headBit xs) (headBit ys) c
    change bit s.1 + 2 * value (addAux n xs.tail ys.tail s.2).1 =
      value xs + value ys + bit c
    rw [ih xs.tail ys.tail s.2 hxs hys]
    have hs : bit s.1 + 2 * bit s.2 = bit (headBit xs) + bit (headBit ys) + bit c :=
      fullAdder_spec _ _ _
    have hvx := value_uncons xs
    have hvy := value_uncons ys
    omega

theorem addAux_length_cost (n : ℕ) (xs ys : List Bool) (c : Bool) :
    (addAux n xs ys c).1.length = n+1 ∧ (addAux n xs ys c).2 = n+1 := by
  induction n generalizing xs ys c with
  | zero => simp [addAux]
  | succ n ih =>
    let s := fullAdder (headBit xs) (headBit ys) c
    have h := ih xs.tail ys.tail s.2
    change (addAux n xs.tail ys.tail s.2).1.length + 1 = n+1+1 ∧
      (addAux n xs.tail ys.tail s.2).2+1 = n+1+1
    omega

def addBits (xs ys : List Bool) : List Bool × ℕ :=
  addAux (max xs.length ys.length) xs ys false

theorem add_value (xs ys : List Bool) :
    value (addBits xs ys).1 = value xs + value ys := by
  unfold addBits
  rw [addAux_value _ _ _ _ (le_max_left _ _) (le_max_right _ _)]
  simp [bit]

theorem add_length (xs ys : List Bool) :
    (addBits xs ys).1.length = max xs.length ys.length+1 :=
  (addAux_length_cost _ _ _ _).1

theorem add_cost (xs ys : List Bool) :
    (addBits xs ys).2 = max xs.length ys.length+1 :=
  (addAux_length_cost _ _ _ _).2

/-- Schoolbook binary multiplication, evaluating a Horner recurrence on
the little-endian multiplier. No unbounded integer multiplication is
used in the digit computation; it occurs only in the specification. -/
def mulBits : List Bool → List Bool → List Bool × ℕ
  | [], _ => ([], 0)
  | a :: xs, ys =>
    let r := mulBits xs ys
    let shifted := false :: r.1
    if a then
      let s := addBits shifted ys
      (s.1, r.2+s.2+1)
    else (shifted, r.2+1)

theorem mul_value (xs ys : List Bool) :
    value (mulBits xs ys).1 = value xs * value ys := by
  induction xs with
  | nil => simp [mulBits, value]
  | cons a xs ih =>
    cases a <;> simp [mulBits, value, bit, add_value, ih] <;> ring

theorem mul_length (xs ys : List Bool) :
    (mulBits xs ys).1.length ≤ 2*xs.length+ys.length := by
  induction xs with
  | nil => simp [mulBits]
  | cons a xs ih =>
    cases a with
    | false =>
      change (mulBits xs ys).1.length+1 ≤ 2*(xs.length+1)+ys.length
      omega
    | true =>
      change (addBits (false :: (mulBits xs ys).1) ys).1.length ≤
        2*(xs.length+1)+ys.length
      rw [add_length, List.length_cons]
      have hm : max ((mulBits xs ys).1.length+1) ys.length ≤
          2*xs.length+ys.length+1 := max_le (by omega) (by omega)
      omega

theorem mul_cost_le (xs ys : List Bool) :
    (mulBits xs ys).2 ≤ xs.length*(2*xs.length+ys.length+2) := by
  induction xs with
  | nil => simp [mulBits]
  | cons a xs ih =>
    cases a with
    | false =>
      change (mulBits xs ys).2+1 ≤
        (xs.length+1)*(2*(xs.length+1)+ys.length+2)
      nlinarith [Nat.zero_le xs.length, Nat.zero_le ys.length]
    | true =>
      change (mulBits xs ys).2+(addBits (false :: (mulBits xs ys).1) ys).2+1 ≤
        (xs.length+1)*(2*(xs.length+1)+ys.length+2)
      rw [add_cost,List.length_cons]
      have hL := mul_length xs ys
      have hm : max ((mulBits xs ys).1.length+1) ys.length ≤
          2*xs.length+ys.length+1 := max_le (by omega) (by omega)
      nlinarith [Nat.zero_le xs.length, Nat.zero_le ys.length]

end Factoring.BitArithmetic

#print axioms Factoring.BitArithmetic.fullAdder_spec
#print axioms Factoring.BitArithmetic.value_lt
#print axioms Factoring.BitArithmetic.add_value
#print axioms Factoring.BitArithmetic.add_length
#print axioms Factoring.BitArithmetic.add_cost
#print axioms Factoring.BitArithmetic.mul_value
#print axioms Factoring.BitArithmetic.mul_length
#print axioms Factoring.BitArithmetic.mul_cost_le
