"""
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
"""

from __future__ import annotations

import itertools
import logging
from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Any, Iterator

from sympy import Not, Or
from sympy.logic.boolalg import BooleanFalse, BooleanFunction
from sympy.logic.inference import satisfiable

from cfnlint.conditions._utils import get_hash
from cfnlint.context.conditions._condition import Condition
from cfnlint.context.conditions._utils import (
    build_instance_from_scenario,
    get_conditions_from_property,
)
from cfnlint.context.conditions.exceptions import Unsatisfiable

if TYPE_CHECKING:
    from cfnlint.context.context import Context, Parameter

# Add logger
LOGGER = logging.getLogger(__name__)

# Global condition cache to avoid recreating identical conditions
_condition_cache: dict[str, Condition] = {}
_condition_cache_hits = 0
_condition_cache_misses = 0
_MAX_CONDITION_CACHE_SIZE = 10000


def _get_or_create_condition(
    instance: Any, all_conditions: dict[str, Any]
) -> Condition:
    """Get a condition from cache or create a new one"""
    global _condition_cache, _condition_cache_hits, _condition_cache_misses

    # Create a cache key from the instance and relevant all_conditions
    cache_key = get_hash((instance, all_conditions))

    if cache_key in _condition_cache:
        _condition_cache_hits += 1
        return _condition_cache[cache_key]

    _condition_cache_misses += 1
    try:
        condition = Condition.create_from_instance(instance, all_conditions)
    except ValueError:
        # Skip malformed conditions
        raise ValueError(f"Invalid condition: {instance}")

    # Limit cache size to prevent memory issues
    if len(_condition_cache) < _MAX_CONDITION_CACHE_SIZE:
        _condition_cache[cache_key] = condition

    return condition


@dataclass(frozen=True)
class Conditions:
    # Template level condition management
    conditions: dict[str, Condition] = field(init=True, default_factory=dict)
    cnf: BooleanFunction | None = field(init=True, default=None)
    _max_scenarios: int = field(init=False, default=128)
    # Class variable for caching satisfiability results
    _satisfiable_cache: dict[str, bool] = field(default_factory=dict, init=False)

    @classmethod
    def create_from_instance(
        cls, conditions: Any, rules: dict[str, dict], parameters: dict[str, "Parameter"]
    ) -> "Conditions":
        obj: dict[str, Condition] = {}
        if not isinstance(conditions, dict):
            raise ValueError("Conditions must be a object")
        for k, v in conditions.items():
            try:
                other_conditions = conditions.copy()
                del other_conditions[k]
                # Use the cached condition creation
                obj[k] = _get_or_create_condition(v, other_conditions)
            except ValueError:
                # Skip malformed conditions
                LOGGER.debug("Skipping malformed condition: %s", k)
                continue

        cnf = None
        for p_k, p_v in parameters.items():

            if not p_v.allowed_values:
                continue
            allowed_values = p_v.allowed_values.copy()
            equals_cnfs = []
            for _, c_v in obj.items():
                for i in c_v.equals:
                    if i.right.hash == get_hash({"Ref": p_k}):
                        if not isinstance(i.left.instance, str):
                            continue
                        equals_cnfs.append(i.cnf)
                        if i.left.instance in allowed_values:
                            allowed_values.remove(i.left.instance)

            if not allowed_values:
                if cnf is None:
                    cnf = Or(*equals_cnfs)
                else:
                    cnf = cnf & Or(*equals_cnfs)

        return cls(conditions=obj, cnf=cnf)

    def evolve(self, status: dict[str, bool]) -> "Conditions":
        cls = self.__class__

        # Quick check - if status is empty, return self
        if not status:
            return self

        # Check if we're trying to set the same status
        all_same = True
        for condition, value in status.items():
            if (
                condition in self.conditions
                and self.conditions[condition].status != value
            ):
                all_same = False
                break
        if all_same:
            return self

        # Cache for evolved conditions to avoid recreating the same condition
        # multiple times
        evolved_cache: dict[tuple[str, bool | None], Condition] = {}

        conditions: dict[str, Condition] = {}
        cnf = self.cnf

        # First pass - evolve all conditions and collect them
        for condition, condition_obj in self.conditions.items():
            s = status.get(condition, condition_obj.status)
            try:
                # Use cache if this condition was already evolved with the same status
                cache_key = (condition, s)
                if cache_key in evolved_cache:
                    conditions[condition] = evolved_cache[cache_key]
                else:
                    conditions[condition] = condition_obj.evolve(status=s)
                    evolved_cache[cache_key] = conditions[condition]
            except ValueError as e:
                raise Unsatisfiable(
                    new_status=status,
                    current_status=self.status,
                ) from e

        # Second pass - build CNF formula
        for condition, condition_obj in conditions.items():
            s = status.get(condition, condition_obj.status)
            if s is not None:
                if cnf:
                    cnf = cnf & condition_obj.cnf if s else cnf & Not(condition_obj.cnf)
                else:
                    cnf = condition_obj.cnf if s else Not(condition_obj.cnf)

        # Cache satisfiability results
        if cnf is not None:
            # Use a simple hash of the CNF as cache key
            cnf_hash = get_hash(str(cnf))

            # Check if we've already tested this CNF
            if hasattr(cls, "_satisfiable_cache"):
                if cnf_hash in cls._satisfiable_cache:
                    if not cls._satisfiable_cache[cnf_hash]:
                        raise Unsatisfiable(
                            new_status=status,
                            current_status=self.status,
                        )
            else:
                # Initialize cache if it doesn't exist
                cls._satisfiable_cache = {}

            # Only check satisfiability if we haven't seen this CNF before
            if cnf_hash not in cls._satisfiable_cache:
                is_sat = satisfiable(cnf)
                cls._satisfiable_cache[cnf_hash] = bool(is_sat)

                # Limit cache size
                if len(cls._satisfiable_cache) > 1000:
                    # Remove a random item (first one)
                    cls._satisfiable_cache.pop(next(iter(cls._satisfiable_cache)))

                if not is_sat:
                    raise Unsatisfiable(
                        new_status=status,
                        current_status=self.status,
                    )

        return cls(
            conditions=conditions,
            cnf=cnf,
        )

    def _build_conditions(self, conditions: set[str]) -> Iterator["Conditions"]:
        scenarios_attempted = 0
        for product in itertools.product([True, False], repeat=len(conditions)):
            params = dict(zip(conditions, product))
            try:
                yield self.evolve(params)
            except Unsatisfiable:
                pass

            scenarios_attempted += 1
            # On occassions people will use a lot of non-related conditions
            # this is fail safe to limit the maximum number of responses
            if scenarios_attempted >= self._max_scenarios:
                return

    def evolve_from_instance(
        self, instance: Any, context: "Context"
    ) -> Iterator[tuple[Any, "Conditions"]]:

        conditions = get_conditions_from_property(instance)

        for scenario in self._build_conditions(conditions):
            yield build_instance_from_scenario(
                instance,
                scenario.status,
                is_root=True,
                context=context,
            ), scenario

    @property
    def status(self) -> dict[str, bool]:
        obj = {}
        for name, c in self.conditions.items():
            if c.status is not None:
                obj[name] = c.status

        return obj
