from functools import cache

from common import input_graph

graph = input_graph()

VISITED_DAC = 1 << 0
VISITED_FFT = 1 << 1
VISITED_ALL = VISITED_DAC | VISITED_FFT


@cache
def count_paths(start_node: str, visited_flags: int = 0) -> int:
    if start_node == "out":
        return 1 if visited_flags == VISITED_ALL else 0

    if start_node == "dac":
        visited_flags |= VISITED_DAC
    elif start_node == "fft":
        visited_flags |= VISITED_FFT

    neighbors = graph.get(start_node, [])
    return sum(count_paths(neighbor, visited_flags) for neighbor in neighbors)


total = count_paths("svr")

assert total == 557332758684000
