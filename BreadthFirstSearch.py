# a - s   d - f
# |   | / | / |
# z   x - c - v

vertices = ['a', 's', 'd', 'f', 'z', 'x', 'c', 'v']
adj = dict()
adj['a'] = ['s', 'z']
adj['s'] = ['a', 'x']
adj['d'] = ['x', 'c', 'f']
adj['f'] = ['d', 'c', 'v']
adj['z'] = ['a']
adj['x'] = ['s', 'd', 'c']
adj['c'] = ['x', 'd', 'f', 'v']
adj['v'] = ['c', 'f']

parent = {'s': None}
level = {'s': 0}
frontier = ['s']
l = 1
while frontier:
    nex = []
    for u in frontier:
        for v in adj[u]:
            if v not in level:
                parent[v] = u
                level[v] = l
                nex.append(v)
    frontier = nex
    l += 1

print(level)
print(parent)

node = 'v'
path = []
while node:
    path.append(node)
    node = parent[node]

path.reverse()
print(path)

for i in range(len(path)-1):
    print(path[i], end=' -> ')
print(path[-1])


vertexStackDict = {}
vertexStack = []
visited = {}
topologicalOrder = []


def DFS(vertices, adj, s):
    topologicalOrder.append(s)
    DFSVisit(adj, s)
    for i in vertices:
        if i not in visited:
            if DFSVisit(adj, s):
                print()
            

def DFSVisit(adj, s):
    if s in visited:
        return True
    print(s, end=" -> ")
    visited[s] = True
    if s not in vertexStackDict:
        vertexStackDict[s] = len(vertexStack)
        vertexStack.append(s)
    # print(vertexStack, vertexStackDict)
    for i in adj[s]:
        # if i in vertexStackDict:
        #     return True
        if DFSVisit(adj, i):
            continue
        vertexStack.pop()
        topologicalOrder.append(i)
        del vertexStackDict[i]
        # print(vertexStack, vertexStackDict)


DFS(vertices, adj, 's')
print(topologicalOrder)
