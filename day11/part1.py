from common import input_graph

graph = input_graph()


def count_paths(start_node: str) -> int:
    if start_node == "out":
        return 1

    neighbors = graph.get(start_node, [])
    return sum(count_paths(neighbor) for neighbor in neighbors)


total = count_paths("you")

assert total == 690
