import sys


def input_ranges():
    for s in sys.stdin.read().split(","):
        a, _, b = s.partition("-")
        yield int(a), int(b)


def input_values():
    for start, end in input_ranges():
        yield from range(start, end + 1)
