# Removing one edge from the ST will make it disconnected
# Includes all the edges the original graph of the spanning tree contains
# Adding one edge will make it cyclic / create a loop
# Out of all the possible spanning trees, the total edge weight of the MST is the minimal
# For a graph with edges of distinct weights the MST is unique

# Prims Algorithm
from collections import defaultdict
graph = defaultdict(dict)
adj = defaultdict(list)
v = ['a', 'b', 'c', 'd', 'e', 'f']
edges = ['a b 7', 'a c 8', 'b c 3', 'b d 6', 'b d 8', 'c d 4', 'c e 3', 'd e 2', 'd f 5', 'e f 2', 'f f 1']

# Construct graph using edges removing loops and parallel edges
for i in edges:
    u, v, w = map(str, i.split())
    if v == u:
        continue
    if v in graph[u]:
        if graph[u][v] < int(w):
            continue
    graph[u][v] = int(w)
    adj[u].append(v)

# Choose a root node, here 'a'
listedEdges = []
result = []
for vertex, edges in adj.items():
    weight = float('inf')
    for edge in edges:
        listedEdges.append((vertex, edge))
    start, end = listedEdges[0][0], listedEdges[0][1]
    for i in listedEdges:
        if graph[i[0]][i[1]] < weight:
            weight = graph[i[0]][i[1]]
            start = i[0]
            end = i[1]
    listedEdges.remove((start, end))
    result.append((start, end))
print(listedEdges)
print(result)
