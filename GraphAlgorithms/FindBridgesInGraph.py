from collections import defaultdict

edges = ['a b', 'a c', 'b c', 'b e', 'b f', ' c d', 'c g', 'c h', 'd e', 'd f', 'f g', 'h i', 'h j', 'i j', 'i k',
         'j l', 'k l', 'k m', 'm n', 'm o', 'n o']
vertexReference = dict()
intVertex = dict()
graph = defaultdict(set)
verticesCount = 0


def DFS(graph, s, parent):
    global visited, nodeStart, lowTime, time, dfsPath, bridgeEdges, intVertex
    if parent is not None:
        print(intVertex[parent], end=' ')
    else:
        print(None, end=' ')
    print(intVertex[s], end=' ')
    if visited[s]:
        print('Revisit Check')
        return
    print('First Visit')
    nodeStart[s] = time
    visited[s] = True
    time += 1
    dfsPath.append(s)
    for i in graph[s]:
        DFS(graph, i, s)


# ('a', 'c')
# ('n', 'm')
# ('m', 'k')
# ('l', 'j')
# ('i', 'h')
# ('h', 'c')
# ('c', 'd')
for edge in edges:
    u, v = map(str, edge.split())
    if u not in vertexReference:
        vertexReference[u] = verticesCount
        intVertex[verticesCount] = u
        verticesCount += 1
    if v not in vertexReference:
        vertexReference[v] = verticesCount
        intVertex[verticesCount] = v
        verticesCount += 1
    graph[vertexReference[u]].add(vertexReference[v])
    graph[vertexReference[v]].add(vertexReference[u])

global visited, nodeStart, bridgeEdges, time, dfsPath, lowTime, parent
dfsPath = []
visited = {i: False for i in intVertex}
parent = {i: -1 for i in intVertex}
nodeStart = {i: float('inf') for i in intVertex}
lowTime = {i: float('inf') for i in intVertex}
bridgeEdges = []
time = 1

DFS(graph, vertexReference['d'], None)
for i in intVertex:
    print(intVertex[i], nodeStart[i])
for i in bridgeEdges:
    print(i)
# print(intVertex)
# print(dfsPath)



# g1.addEdge('a', 'b')
# g1.addEdge('a', 'c')
# g1.addEdge('b', 'c')
# g1.addEdge('b', 'e')
# g1.addEdge('b', 'f')
# g1.addEdge('c', 'd')
# g1.addEdge('c', 'g')
# g1.addEdge('c', 'h')
# g1.addEdge('d', 'e')
# g1.addEdge('d', 'f')
# g1.addEdge('f', 'g')
# g1.addEdge('h', 'i')
# g1.addEdge('h', 'j')
# g1.addEdge('i', 'j')
# g1.addEdge('i', 'k')
# g1.addEdge('j', 'l')
# g1.addEdge('k', 'l')
# g1.addEdge('k', 'm')
# g1.addEdge('m', 'n')
# g1.addEdge('m', 'o')
# g1.addEdge('n', 'o')

