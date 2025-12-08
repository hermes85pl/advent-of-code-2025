from common import PositionClusterer, input_positions, pairs_sorted_by_distance

product = None

nodes = list(input_positions())
clusterer = PositionClusterer(nodes)
closest_nodes = pairs_sorted_by_distance(nodes)
for a, b in closest_nodes:
    if clusterer.join_if_disjoint(a, b) == len(nodes):
        product = a[0] * b[0]
        break

assert product == 169521198
