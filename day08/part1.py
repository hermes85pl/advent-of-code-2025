from functools import reduce
from heapq import nlargest
from itertools import islice

from common import input_positions, pairs_sorted_by_distance

nodes = list(input_positions())

closest_nodes = pairs_sorted_by_distance(nodes)

node_to_cluster_map = {n: {n} for n in nodes}

for a, b in islice(closest_nodes, 1000):
    cluster_a, cluster_b = node_to_cluster_map[a], node_to_cluster_map[b]
    if cluster_a & cluster_b:
        continue
    joint_cluster = cluster_a | cluster_b
    for node in joint_cluster:
        node_to_cluster_map[node] = joint_cluster

clusters = {frozenset(c) for c in node_to_cluster_map.values()}

product = reduce(lambda a, b: a * b, nlargest(3, (len(c) for c in clusters)))

assert product == 164475
