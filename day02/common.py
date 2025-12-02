import sys


def ranges():
    for s in sys.stdin.read().split(","):
        a, _, b = s.partition("-")
        yield int(a), int(b)


def values():
    for start, end in ranges():
        yield from range(start, end + 1)
