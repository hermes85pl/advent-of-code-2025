import sys
from itertools import takewhile


def input_ranges():
    for line in takewhile(lambda line: line != "\n", sys.stdin):
        a, _, b = line.rstrip().partition("-")
        yield int(a), int(b)


def input_values():
    for line in sys.stdin:
        yield int(line.rstrip())
