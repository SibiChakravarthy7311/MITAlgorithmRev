from collections import defaultdict
import heapq


# Method 1
global visited, resultDFS, nodeStart, nodeEnd, time


def DFSRecursive(graph, s):
    global visited, resultDFS, nodeStart, nodeEnd, time
    if visited[s]:
        return
    visited[s] = True
    resultDFS.append(s)
    nodeStart[s] = time
    time += 1
    for i in graph[s]:
        DFSRecursive(graph, i)
    time += 1
    nodeEnd[s] = time


edges = ['1 2', '1 4', '2 3', '2 4', '4 3', '4 5']
verticesCount = 0
graph = defaultdict(list)
vertexReference = {}
intVertex = {}

for edge in edges:
    u, v = map(int, edge.split())
    if u not in vertexReference:
        vertexReference[u] = verticesCount
        intVertex[verticesCount] = u
        verticesCount += 1
    if v not in vertexReference:
        vertexReference[v] = verticesCount
        intVertex[verticesCount] = v
        verticesCount += 1
    graph[vertexReference[u]].append(vertexReference[v])


visited = {i: False for i in intVertex}
time = 0
nodeStart = dict()
nodeEnd = dict()
resultDFS = []

DFSRecursive(graph, 0)

topologicalOrder = []
for node, time in nodeEnd.items():
    heapq.heappush(topologicalOrder, (-1 * time, node))
while topologicalOrder:
    print(intVertex[heapq.heappop(topologicalOrder)[1]], end=' ')
print()


# Method 2
inDegree = {i: 0 for i in intVertex}
degreeList = defaultdict(set)
resultTopological = []

for vertex in graph:
    for adj in graph[vertex]:
        inDegree[adj] += 1

for vertex, degree in inDegree.items():
    degreeList[degree].add(vertex)

while degreeList[0]:
    vertex = degreeList[0].pop()
    resultTopological.append(vertex)
    for adj in graph[vertex]:
        prev = inDegree[adj]
        degreeList[prev].remove(adj)
        inDegree[adj] -= 1
        curr = inDegree[adj]
        degreeList[curr].add(adj)

for i in resultTopological:
    print(intVertex[i], end=' ')


