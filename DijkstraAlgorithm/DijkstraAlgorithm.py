vertices = ['R', 'Y', 'G', 'P', 'B']
# Q = vertices.copy()
# ext = float('inf')
# w = [0, ext, ext, ext, ext]
adj = dict()
l = dict()

adj['R'] = ['Y', 'P', 'B']
l['R'] = [4, 15, 13]
adj['Y'] = ['R', 'G', 'P']
l['Y'] = [4, 19, 11]
adj['G'] = ['Y', 'P']
l['G'] = [19, 7]
adj['P'] = ['R', 'Y', 'G', 'B']
l['P'] = [15, 11, 7, 5]
adj['B'] = ['R', 'P']
l['B'] = [13, 5]

graph = {'adj': adj, 'd': l, 'vert': vertices, 'pi': {'R': None}}


def Dijkstra(G, S, des):
    res = []
    Q = G['vert']
    path = []
    adjacent_nodes = {v: {} for v in Q}
    for u in Q:
        for ind, v in enumerate(G['adj'][u]):
            adjacent_nodes[u][v] = G['d'][u][ind]
    # print(adjacent_nodes)
    path_lengths = {v: float('inf') for v in Q}
    path_lengths[S] = 0
    temp_nodes = Q.copy()
    while temp_nodes:
        bounds = {v: path_lengths[v] for v in temp_nodes}
        u = min(bounds, key=bounds.get)

        res.append(u)
        temp_nodes.remove(u)
        for v, w_uv in adjacent_nodes[u].items():
            if path_lengths[v] > path_lengths[u]+w_uv:
                path_lengths[v] = path_lengths[u] + w_uv
                G['pi'][v] = u

    print(res)
    print(path_lengths)
    # print(G['pi'])
    while(des):
        path.append(des)
        des = G['pi'][des]
    path.reverse()
    print(path)


Dijkstra(graph, 'R', 'G')
