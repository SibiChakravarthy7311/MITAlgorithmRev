from collections import defaultdict

edges = ['0 1', '0 3', '1 2', '2 3', '4 5', '6 7', '6 8', '7 8']
global connectedComponents, visited, intVertex, vertexReference, verticesCount, tempConnected
verticesCount = 0
intVertex = {}
vertexReference = {}
connectedComponents = []
tempConnected = []
graph = defaultdict(set)


def DFSUtil(graph, s):
    global visited, connectedComponents, tempConnected, intVertex
    if visited[s]:
        return
    visited[s] = True
    tempConnected.append(intVertex[s])
    if s in graph:
        for i in graph[s]:
            DFSUtil(graph, i)


def DFS(graph):
    global tempConnected, connectedComponents
    for i in graph:
        DFSUtil(graph, i)
        if tempConnected:
            connectedComponents.append(tempConnected)
            tempConnected = []


for edge in edges:
    u, v = map(int, edge.split())
    if v == u:
        continue
    if u not in vertexReference:
        vertexReference[u] = verticesCount
        intVertex[verticesCount] = u
        verticesCount += 1
    if v not in vertexReference:
        vertexReference[v] = verticesCount
        intVertex[verticesCount] = v
        verticesCount += 1
    if vertexReference[v] in graph[vertexReference[u]]:
        continue
    graph[vertexReference[u]].add(vertexReference[v])

visited = {i: False for i in intVertex}
DFS(graph)
print(connectedComponents)
