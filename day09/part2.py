from itertools import chain, combinations, pairwise

from common import Point, input_positions


class Rectangle:
    x_min: int
    x_max: int
    y_min: int
    y_max: int

    def __init__(self, p1: Point, p2: Point) -> None:
        x1, y1 = p1[0], p1[1]
        x2, y2 = p2[0], p2[1]
        self.x_min, self.x_max = min(x1, x2), max(x1, x2)
        self.y_min, self.y_max = min(y1, y2), max(y1, y2)

    def overlaps_with(self, other: "Rectangle") -> bool:
        return not (
            self.x_max <= other.x_min
            or other.x_max <= self.x_min
            or self.y_max <= other.y_min
            or other.y_max <= self.y_min
        )

    def area(self) -> int:
        x_len = self.x_max - self.x_min + 1
        y_len = self.y_max - self.y_min + 1
        return x_len * y_len


nodes = list(input_positions())

edges = [Rectangle(p, q) for p, q in chain(pairwise(nodes), [(nodes[-1], nodes[0])])]

max_area = max(
    rectangle.area()
    for rectangle in (Rectangle(p, q) for p, q in combinations(nodes, 2))
    if not any(rectangle.overlaps_with(edge) for edge in edges)
)

assert max_area == 1560299548
