from collections import deque
# BFS
v = [0, 1, 2, 3, 4, 5, 6]
edges = [(0, 1), (0, 3), (1, 0), (1, 3), (1, 2), (1, 5), (1, 6), (2, 1), (2, 3), (2, 4), (2, 5), (3, 0), (3, 2),
         (3, 4), (4, 2), (4, 3), (4, 6), (5, 1), (5, 2), (6, 1), (6, 4)]
adj = {i: [] for i in v}
for i, j in edges:
    adj[i].append(j)


def BFS(adj, s):
    visited = {}
    res = [s]
    for key, value in adj.items():
        visited[key] = False
    visited[s] = True
    q = deque()
    q.append(s)
    while q:
        vertex = q.popleft()
        for i in adj[vertex]:
            if not visited[i]:
                visited[i] = True
                q.append(i)
                res.append(i)
    return res


bfsPath = BFS(adj, 0)
print(bfsPath)


#
#
#
#
#
#
# DFS
def DFS(adj, s):
    visited = {}
    res = []
    for key, value in adj.items():
        visited[key] = False
    stack = [s]
    while stack:
        # print(stack)
        vertex = stack.pop()
        if visited[vertex]:
            continue
        res.append(vertex)
        visited[vertex] = True
        l = adj[vertex][::-1]
        for i in l:
            if not visited[i]:
                stack.append(i)
    return res


print()
dfsPath = DFS(adj, 0)
print(dfsPath)


#
#
#
#
#
#
# DFS Recursive
global recursiveVisit, result
recursiveVisit = {i: False for i in v}
result = []


def DFSRecursive(adj, s):
    global recursiveVisit, result
    if recursiveVisit[s]:
        return
    recursiveVisit[s] = True
    result.append(s)
    for i in adj[s]:
        DFSRecursive(adj, i)


print()
DFSRecursive(adj, 0)
print(result)


#
#
#
#
#
#
# DFS Recursive Classification
global recursiveVisited, resultDFS, nodeStart, nodeEnd, time, vertexStack, treeEdge, backEdge, forwardEdge
recursiveVisited = {i: False for i in v}
nodeStart = {}
nodeEnd = {}
time = 1
resultDFS = []
vertexStack = [0]
treeEdge = []
backEdge = []
forwardEdge = []


def DFSRecursiveNode(adj, s):
    global recursiveVisited, resultDFS, nodeStart, nodeEnd, time, vertexStack, treeEdge, backEdge, forwardEdge
    nodeStart[s] = time
    recursiveVisited[s] = True
    resultDFS.append(s)
    time += 1
    for i in adj[s]:
        if not recursiveVisited[i]:
            vertexStack.append(i)
            treeEdge.append((s, i))
            DFSRecursiveNode(adj, i)
        elif i in vertexStack:
            backEdge.append((s, i))
        elif nodeStart[s] < nodeStart[i]:
            forwardEdge.append((s, i))
    vertexStack.pop()
    time += 1
    nodeEnd[s] = time


print()
DFSRecursiveNode(adj, 0)
print('DFSPath:', resultDFS)
print('TreeEdge:', treeEdge)
print('BackEdge:', backEdge)
print('Node Start Time: {}\nNode End Time: {}'.format(nodeStart, nodeEnd))
print(forwardEdge)
