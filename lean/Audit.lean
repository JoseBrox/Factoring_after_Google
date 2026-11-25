import Factoring
import Lean.Util.CollectAxioms

/-!
Audit every logical declaration in our imported modules, including private and
generated proofs. Lean's unsafe compiler objects are not logical declarations;
they are counted separately. The dependency traversal itself is unfiltered.
Reject additional axioms (including `sorryAx` and native decision axioms).
The three allowed axioms are Lean's standard classical basis.
-/

open Lean Elab Command in
run_cmd do
  let env ← getEnv
  let allowed := #[``propext, ``Classical.choice, ``Quot.sound]
  let mut declarations := 0
  let mut theorems := 0
  let mut runtimeObjects := 0
  let entries := env.constants.toList.mergeSort (fun a b => Name.lt a.1 b.1)
  for (name, info) in entries do
    let some idx := env.getModuleIdxFor? name | continue
    let mod := env.header.moduleNames[idx.toNat]!
    unless mod == `Factoring || mod.toString.startsWith "Factoring." do continue
    if info.isUnsafe then
      runtimeObjects := runtimeObjects + 1
      continue
    declarations := declarations + 1
    if info.isAxiom then throwError "Project axiom: {name}"
    let axioms ← collectAxioms name
    for ax in axioms do
      unless allowed.contains ax do throwError "Unapproved axiom {ax} used by {name}"
    if info.isTheorem then
      theorems := theorems + 1
      logInfo m!"{name}: {axioms.qsort Name.lt |>.toList}"
  if theorems == 0 then throwError "No project theorems were audited"
  logInfo m!"PASS: {declarations} declarations, including {theorems} theorems; only propext, Classical.choice, Quot.sound are allowed."
  logInfo m!"INFO: {runtimeObjects} unsafe compiler runtime objects excluded as audit roots; logical proof dependencies are traversed without filtering."
