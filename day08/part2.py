from common import input_positions, pairs_sorted_by_distance

nodes = list(input_positions())

closest_nodes = pairs_sorted_by_distance(nodes)

node_to_cluster_map = {n: {n} for n in nodes}

product = None

for a, b in closest_nodes:
    cluster_a, cluster_b = node_to_cluster_map[a], node_to_cluster_map[b]
    if cluster_a & cluster_b:
        continue
    joint_cluster = cluster_a | cluster_b
    if len(joint_cluster) == len(nodes):
        product = a[0] * b[0]
        break
    for node in joint_cluster:
        node_to_cluster_map[node] = joint_cluster

assert product == 169521198
