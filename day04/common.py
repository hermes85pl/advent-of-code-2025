import sys
from typing import Iterable, Iterator

RawGrid = list[list[str]]
Point = tuple[int, int]

DIRECTIONS = ((0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1))

LIMIT = 4
PAPER = "@"
WHERE_PAPER_USED_TO_BE = "x"


def input_raw_grid() -> RawGrid:
    return [list(line.rstrip()) for line in sys.stdin]


class Grid:
    def __init__(self, raw_grid: RawGrid) -> None:
        self._grid = raw_grid
        self._hlen = len(raw_grid)
        self._wlen = len(raw_grid[0])

    def __iter__(self) -> Iterator[Point]:
        for y in range(self._hlen):
            for x in range(self._wlen):
                yield x, y

    def __getitem__(self, pos: Point) -> str:
        x, y = pos
        return self._grid[y][x]

    def __setitem__(self, pos: Point, value: str) -> None:
        x, y = pos
        self._grid[y][x] = value

    def neighbors(self, pos: Point) -> Iterable[Point]:
        x, y = pos
        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self._wlen and 0 <= ny < self._hlen:
                yield nx, ny

    def neighbor_count(self, pos: Point, value: str) -> int:
        return sum(self[p] == value for p in self.neighbors(pos))
