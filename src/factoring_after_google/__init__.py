"""Executable auxiliary routines accompanying Factoring after Google.

The asymptotic general factorers are specified in the manuscripts. This package
implements the quadratic relation subroutine only.
"""

from .quadratic_relations import chain_split, one_shot_split, quadratic_power

__all__ = ["chain_split", "one_shot_split", "quadratic_power"]
