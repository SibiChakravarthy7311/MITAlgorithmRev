def dijkstra(nodes, edges, source_index=0):
    path_lengths = {v: float('inf') for v in nodes}
    path_lengths[source_index] = 0
    res = []

    adjacent_nodes = {v: {} for v in nodes}
    for (u, v), w_uv in edges.items():
        adjacent_nodes[v][u] = w_uv
        adjacent_nodes[u][v] = w_uv

    temporary_nodes = nodes.copy()
    while len(temporary_nodes):
        upper_bounds = {v: path_lengths[v] for v in temporary_nodes}
        u = min(upper_bounds, key=upper_bounds.get)

        res.append(u)
        temporary_nodes.remove(u)
        for v, w_uv in adjacent_nodes[u].items():
            if path_lengths[v] > path_lengths[u] + w_uv:
                path_lengths[v] = path_lengths[u] + w_uv

    print(res)
    print(path_lengths)


node = [0, 1, 2, 3, 4, 5]
edge = {(0, 1): 1, (0, 2): 1.5, (0, 3): 2, (1, 3): 0.5, (1, 4): 2.5, (2, 3): 1.5, (3, 5): 1}

dijkstra(node, edge)
