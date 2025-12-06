from operator import add, mul
from typing import Callable

NumberGroup = list[int]
OperatorFunction = Callable[[int, int], int]

OPERATORS: dict[str, OperatorFunction] = {"+": add, "*": mul}
