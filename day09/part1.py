from itertools import combinations

from common import Point, input_positions


def area(p1: Point, p2: Point) -> int:
    x1, y1 = p1
    x2, y2 = p2
    x_len = abs(x2 - x1) + 1
    y_len = abs(y2 - y1) + 1
    return x_len * y_len


max_area = max(area(p, q) for p, q in combinations(input_positions(), 2))

assert max_area == 4776487744
