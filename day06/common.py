from functools import reduce
from operator import add, mul
from typing import Callable, Iterable

NumberGroup = list[int]
OperatorFunction = Callable[[int, int], int]

OPERATORS: dict[str, OperatorFunction] = {"+": add, "*": mul}


def grand_total(
    operators: Iterable[OperatorFunction], number_groups: Iterable[NumberGroup]
) -> int:
    return sum(reduce(op, num) for op, num in zip(operators, number_groups))
