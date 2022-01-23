from collections import defaultdict
import heapq


class Graph:
    def __init__(self):
        self.graph = defaultdict(set)
        self.verticesCount = 0
        self.vertexReference = {}
        self.intVertex = {}
        self.edgeDict = defaultdict(dict)

    def addEdge(self, edge):
        u, v, w = map(str, edge.split())
        w = int(w)
        if v == u:
            return
        if u not in self.vertexReference:
            self.vertexReference[u] = self.verticesCount
            self.intVertex[self.verticesCount] = u
            self.verticesCount += 1
        if v not in self.vertexReference:
            self.vertexReference[v] = self.verticesCount
            self.intVertex[self.verticesCount] = v
            self.verticesCount += 1
        if v in self.edgeDict[u]:
            if w > self.edgeDict[u][v]:
                return
        self.edgeDict[self.vertexReference[u]][self.vertexReference[v]] = w

    def union(self, parent, x, y):
        parent[x] = y

    def findParent(self, parent, i):
        if parent[i] == -1:
            return i
        return self.findParent(parent, parent[i])

    def isCyclic(self):
        parent = [-1]*self.verticesCount

        for i in self.edgeDict:
            for j in self.edgeDict[i]:
                x = self.findParent(parent, i)
                y = self.findParent(parent, j)
                if x == y:
                    return True
                self.union(parent, x, y)

    def findMSTKruskal(self):
        edges = []
        mst = []
        parent = [-1] * self.verticesCount
        cost, source, dest = 0, 1, 2
        for i in self.edgeDict:
            for j in self.edgeDict[i]:
                heapq.heappush(edges, (self.edgeDict[i][j], i, j))
        while edges and len(mst) < self.verticesCount - 1:
            edge = heapq.heappop(edges)
            x = self.findParent(parent, edge[source])
            y = self.findParent(parent, edge[dest])
            if x == y:
                continue
            mst.append(edge)
            self.union(parent, x, y)
        return mst


edgeList = ['a b 5', 'a b 10', 'a c 3', 'a f 7', ' b c 6', 'b d 2', 'b e 4', 'c d 3', 'c f 8', 'd e 2']
g = Graph()
for edge in edgeList:
    g.addEdge(edge)
mst = g.findMSTKruskal()
print(mst)
