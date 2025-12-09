import sys

Point = tuple[int, int]


def input_positions():
    for line in sys.stdin:
        x, _, y = line.rstrip().partition(",")
        yield int(x), int(y)
