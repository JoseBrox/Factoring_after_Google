import Factoring.ModularBits
import Mathlib.Data.Nat.GCD.Basic

/-! Fixed-width binary Euclidean algorithm. Each nonterminal round
performs two long remainders and halves the bound on the second operand.
All zero tests inspect bits. The cost is charged in the same cell model
as ModularBits. -/
namespace Factoring.BitArithmetic

def isZeroBits : List Bool → Bool
  | [] => true
  | b :: bs => !b && isZeroBits bs

theorem isZeroBits_spec (xs : List Bool) :
    isZeroBits xs = true ↔ value xs = 0 := by
  induction xs with
  | nil => simp [isZeroBits,value]
  | cons b bs ih =>
    cases b <;> simp [isZeroBits,value,bit,ih]

theorem two_remainders_lt {a b k : ℕ} (hb : 0<b) (hr : 0<a%b)
    (h : b<2^(k+1)) : b%(a%b)<2^k := by
  let r := a%b
  have hlt : r<b := Nat.mod_lt _ hb
  have hr' : 0<r := hr
  have hmod := Nat.mod_lt b hr'
  rw [pow_succ] at h
  by_cases hhalf : r<2^k
  · exact hmod.trans hhalf
  · have he : b%r=b-r := by
      rw [Nat.mod_eq_sub_mod (by omega : r≤b)]
      exact Nat.mod_eq_of_lt (by omega)
    rw [he]
    omega

/-- At a zero second operand, stop immediately; at a zero first
remainder, stop after one division. Otherwise perform two divisions.
Fuel counts pairs of Euclidean steps, not individual divisions. -/
def gcdBitsAux : ℕ → List Bool → List Bool → List Bool
  | 0, a, _ => a
  | k+1, a, b =>
    if isZeroBits b then a else
      let r := remainderBits b a
      if isZeroBits r then b else gcdBitsAux k r (remainderBits r b)

theorem gcdBitsAux_spec (k : ℕ) (a b : List Bool)
    (h : value b<2^k) (hlen : a.length=b.length) :
    value (gcdBitsAux k a b)=Nat.gcd (value a) (value b) ∧
      (gcdBitsAux k a b).length=a.length := by
  induction k generalizing a b with
  | zero =>
    have hb : value b=0 := by simpa using h
    simp [gcdBitsAux,hb]
  | succ k ih =>
    by_cases hz : isZeroBits b=true
    · have hb := (isZeroBits_spec b).mp hz
      simp [gcdBitsAux,hz,hb]
    · have hb : 0<value b := by
        by_contra h0
        exact hz ((isZeroBits_spec b).mpr (by omega))
      let r := remainderBits b a
      have hr := remainderBits_spec b a hb
      change value (if isZeroBits b then a else
        if isZeroBits r then b else gcdBitsAux k r (remainderBits r b)) =
          Nat.gcd (value a) (value b) ∧
        (if isZeroBits b then a else
        if isZeroBits r then b else gcdBitsAux k r (remainderBits r b)).length=a.length
      rw [if_neg hz]
      by_cases hz' : isZeroBits r=true
      · rw [if_pos hz']
        have h0 := (isZeroBits_spec r).mp hz'
        have hmod : value a % value b = 0 := hr.2.symm.trans h0
        constructor
        · rw [Nat.gcd_comm (value a), Nat.gcd_rec, hmod, Nat.gcd_zero_left]
        · exact hlen.symm
      · rw [if_neg hz']
        have hp : 0<value r := by
          by_contra h0
          exact hz' ((isZeroBits_spec r).mpr (by omega))
        let s := remainderBits r b
        have hs := remainderBits_spec r b hp
        have hsmall : value s<2^k := by
          rw [show value s=value b%value r from hs.2, show value r=value a%value b from hr.2]
          exact two_remainders_lt hb (hr.2 ▸ hp) h
        have hi := ih r s hsmall hs.1.symm
        constructor
        · calc
            _ = Nat.gcd (value r) (value s) := hi.1
            _ = Nat.gcd (value b % value r) (value r) := by rw [show value s=value b%value r from hs.2, Nat.gcd_comm]
            _ = Nat.gcd (value r) (value b) := (Nat.gcd_rec (value r) (value b)).symm
            _ = Nat.gcd (value a % value b) (value b) := by rw [show value r=value a%value b from hr.2]
            _ = Nat.gcd (value b) (value a) := (Nat.gcd_rec (value b) (value a)).symm
            _ = _ := Nat.gcd_comm _ _
        · exact hi.2.trans (hr.1.trans hlen.symm)

/-- Zero-extend both operands to a common width. -/
def padBits (n : ℕ) (xs : List Bool) : List Bool :=
  xs ++ List.replicate (n-xs.length) false

theorem padBits_length (n : ℕ) (xs : List Bool) (h : xs.length≤n) :
    (padBits n xs).length=n := by simp [padBits]; omega

theorem value_append (a b : List Bool) :
    value (a++b)=value a+2^a.length*value b := by
  induction a with
  | nil => simp [value]
  | cons a as ih =>
    simp only [List.cons_append,value,List.length_cons,pow_succ,ih]
    ring

theorem padBits_value (n : ℕ) (xs : List Bool) :
    value (padBits n xs)=value xs := by
  simp [padBits,value_append,value_zeros]

def gcdBits (a b : List Bool) : List Bool :=
  let n := max a.length b.length
  gcdBitsAux n (padBits n a) (padBits n b)

theorem gcdBits_spec (a b : List Bool) :
    value (gcdBits a b)=Nat.gcd (value a) (value b) ∧
      (gcdBits a b).length=max a.length b.length := by
  let n := max a.length b.length
  have ha := padBits_length n a (le_max_left _ _)
  have hb := padBits_length n b (le_max_right _ _)
  have h := value_lt (padBits n b)
  rw [hb] at h
  have hs := gcdBitsAux_spec n (padBits n a) (padBits n b) h (ha.trans hb.symm)
  simpa [gcdBits,padBits_value,ha,n] using hs

/-- Charge two zero tests and up to two actual long remainder calls
per round, with fixed-width lists. This recursive counter follows
the same branch structure as the executable gcd. -/
def gcdBitsCostAux : ℕ → List Bool → List Bool → ℕ
  | 0, _, _ => 0
  | k+1, a, b =>
    b.length + if isZeroBits b then 0 else
      let r := remainderBits b a
      remainderCost b.length a.length + r.length +
        if isZeroBits r then 0 else
          remainderCost r.length b.length + gcdBitsCostAux k r (remainderBits r b)

theorem gcdBitsCostAux_le (k : ℕ) (a b : List Bool)
    (hlen : a.length=b.length) (h : value b<2^k) :
    gcdBitsCostAux k a b ≤ k*(2*remainderCost a.length a.length+2*a.length) := by
  induction k generalizing a b with
  | zero => simp [gcdBitsCostAux]
  | succ k ih =>
    by_cases hz : isZeroBits b=true
    · simp [gcdBitsCostAux,hz,← hlen]
      nlinarith [Nat.zero_le (remainderCost a.length a.length)]
    · have hb : 0<value b := by
        by_contra h0
        exact hz ((isZeroBits_spec b).mpr (by omega))
      let r := remainderBits b a
      have hr := remainderBits_spec b a hb
      have hrl : r.length=a.length := hr.1.trans hlen.symm
      by_cases hz' : isZeroBits r=true
      · change b.length+(if isZeroBits b then 0 else
          remainderCost b.length a.length+r.length+(if isZeroBits r then 0 else
            remainderCost r.length b.length+gcdBitsCostAux k r (remainderBits r b)))≤_
        rw [if_neg hz,if_pos hz',← hlen,hrl]
        nlinarith [Nat.zero_le (remainderCost a.length a.length)]
      · have hp : 0<value r := by
          by_contra h0
          exact hz' ((isZeroBits_spec r).mpr (by omega))
        let s := remainderBits r b
        have hs := remainderBits_spec r b hp
        have hsmall : value s<2^k := by
          rw [show value s=value b%value r from hs.2,show value r=value a%value b from hr.2]
          exact two_remainders_lt hb (hr.2 ▸ hp) h
        have hi := ih r s hs.1.symm hsmall
        rw [hrl] at hi
        change b.length+(if isZeroBits b then 0 else
          remainderCost b.length a.length+r.length+(if isZeroBits r then 0 else
            remainderCost r.length b.length+gcdBitsCostAux k r s))≤_
        rw [if_neg hz,if_neg hz',← hlen,hrl]
        nlinarith

def gcdBitsCost (a b : List Bool) : ℕ :=
  let n := max a.length b.length
  2*n+gcdBitsCostAux n (padBits n a) (padBits n b)

theorem gcdBitsCost_le (a b : List Bool) :
    gcdBitsCost a b≤8*(max a.length b.length)^3+
      20*(max a.length b.length)^2+2*(max a.length b.length) := by
  let n := max a.length b.length
  have ha := padBits_length n a (le_max_left _ _)
  have hb := padBits_length n b (le_max_right _ _)
  have hh := value_lt (padBits n b)
  rw [hb] at hh
  have hc := gcdBitsCostAux_le n (padBits n a) (padBits n b) (ha.trans hb.symm) hh
  rw [ha,remainderCost] at hc
  change 2*n+gcdBitsCostAux n (padBits n a) (padBits n b)≤8*n^3+20*n^2+2*n
  nlinarith

end Factoring.BitArithmetic

#print axioms Factoring.BitArithmetic.isZeroBits_spec
#print axioms Factoring.BitArithmetic.two_remainders_lt
#print axioms Factoring.BitArithmetic.gcdBitsAux_spec
#print axioms Factoring.BitArithmetic.padBits_length
#print axioms Factoring.BitArithmetic.value_append
#print axioms Factoring.BitArithmetic.padBits_value
#print axioms Factoring.BitArithmetic.gcdBits_spec
#print axioms Factoring.BitArithmetic.gcdBitsCostAux_le
#print axioms Factoring.BitArithmetic.gcdBitsCost_le
