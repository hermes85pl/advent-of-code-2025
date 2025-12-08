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


class PositionClusterer:
    _pos_to_cluster_map: dict[Position, set[Position]]

    def __init__(self, positions: Iterable[Position]) -> None:
        self._pos_to_cluster_map = {p: {p} for p in positions}

    def join_if_disjoint(self, a: Position, b: Position) -> int:
        cluster_a, cluster_b = self._pos_to_cluster_map[a], self._pos_to_cluster_map[b]
        if cluster_a & cluster_b:
            return 0
        joint_cluster = cluster_a | cluster_b
        for node in joint_cluster:
            self._pos_to_cluster_map[node] = joint_cluster
        return len(joint_cluster)

    def clusters(self) -> set[frozenset[Position]]:
        return {frozenset(c) for c in self._pos_to_cluster_map.values()}


def input_positions():
    for line in sys.stdin:
        yield Position(*(int(value) for value in line.rstrip().split(",")))


def pairs_sorted_by_distance(positions: Iterable[Position]):
    distances = [(b - a, a, b) for a, b in combinations(positions, 2)]
    heapify(distances)
    while distances:
        _, a, b = heappop(distances)
        yield a, b
