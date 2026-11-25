# Implemented routines

`factoring_after_google/quadratic_relations.py` implements the auxiliary quadratic-ring exponentiation, one-shot relation, and complete relation-chain splitting routines. It uses exact integer arithmetic and has no external dependencies.

Run `python3 examples/quadratic_relation_example.py` from the repository root. To import the package in an experiment, add `src` to your Python path; the example shows the complete setup.

This directory does not contain a complete implementation of the general deterministic factorer, the sparse Gram splitter, the prime nonresidue constructor, or the conditional randomized factorer. Their exact mathematical specifications and cost arguments are in the corresponding manuscripts. In particular, the relation-chain routine does not construct its mixed-sign parameter or supplied exponent for a general input.
