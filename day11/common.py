import sys


def input_edges():
    for line in sys.stdin:
        parts = line.rstrip().split()
        yield parts[0][:-1], parts[1:]


def input_graph():
    return {node: neighbors for node, neighbors in input_edges()}
