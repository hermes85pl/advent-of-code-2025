import sys
from functools import reduce
from typing import Iterable


def input_banks():
    for line in sys.stdin:
        yield [int(x) for x in line.rstrip()]


def joltage(cells: Iterable[int]) -> int:
    return reduce(lambda a, b: a * 10 + b, cells)
