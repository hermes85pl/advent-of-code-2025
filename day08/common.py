import sys
from heapq import heapify, heappop
from itertools import combinations
from typing import Iterable, NamedTuple


class Position(NamedTuple):
    x: int
    y: int
    z: int

    def __sub__(self, other: "Position") -> float:
        dx = self.x - other.x
        dy = self.y - other.y
        dz = self.z - other.z
        return (dx**2 + dy**2 + dz**2) ** 0.5


def input_positions():
    for line in sys.stdin:
        yield Position(*(int(value) for value in line.rstrip().split(",")))


def sorted_by_distance(positions: Iterable[Position]):
    distances = [(b - a, a, b) for a, b in combinations(positions, 2)]
    heapify(distances)
    while distances:
        _, a, b = heappop(distances)
        yield a, b
