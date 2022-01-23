import heapq

mst = []
# edgeList = ['a b 7', 'a c 8', 'b c 3', 'b d 6', 'b d 8', 'c d 4', 'c e 3', 'd e 2', 'd f 5', 'e f 2', 'f f 1']
edgeList = ['1 2 1', '3 2 150', '4 3 99', '1 4 100', '3 1 200']
start = 0
numVertices = 4
# usedVertices = set()
usedVertices = {start}
edges = [[] for i in range(numVertices)]
intVertex = {}
vertexReference = {}
ct = 0
for i in edgeList:
    u, v, w = map(str, i.split())
    if v == u:
        continue
    if v not in vertexReference:
        vertexReference[v] = ct
        intVertex[ct] = v
        ct += 1
    if u not in vertexReference:
        vertexReference[u] = ct
        intVertex[ct] = u
        ct += 1
    heapq.heappush(edges[vertexReference[v]], (int(w), vertexReference[u]))
    heapq.heappush(edges[vertexReference[u]], (int(w), vertexReference[v]))

cost, dest = 0, 1
while len(usedVertices) < numVertices:
    vertexWithSmallestEdge = start
    for vertex in usedVertices:
        while len(edges[vertex]) > 0 and edges[vertex][0][dest] in usedVertices:
            heapq.heappop(edges[vertex])

        if len(edges[vertex]) == 0:
            continue

        if len(edges[vertexWithSmallestEdge]) == 0 or edges[vertex][0][cost] < edges[vertexWithSmallestEdge][0][cost]:
            vertexWithSmallestEdge = vertex

    edge = heapq.heappop(edges[vertexWithSmallestEdge])
    usedVertices.add(edge[dest])
    # usedVertices.add(vertexWithSmallestEdge)
    mst.append((vertexWithSmallestEdge, edge[dest], edge[cost]))

print(mst)
result = 0
for i in mst:
    result += i[2]
print('\n{}'.format(result))
