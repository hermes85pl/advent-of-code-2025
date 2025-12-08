from functools import reduce
from heapq import nlargest
from itertools import islice

from common import PositionClusterer, input_positions, pairs_sorted_by_distance

nodes = list(input_positions())
clusterer = PositionClusterer(nodes)
closest_nodes = pairs_sorted_by_distance(nodes)
for a, b in islice(closest_nodes, 1000):
    clusterer.join_if_disjoint(a, b)

product = reduce(
    lambda a, b: a * b, nlargest(3, (len(c) for c in clusterer.clusters()))
)

assert product == 164475
