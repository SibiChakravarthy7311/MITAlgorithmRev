# def BFSWeight(vertices, edges, s):
#     adjacentVertices = {}
#     visitedEdge = {}
#     pathWeight = {}
#     parent = {s: None}
#     for v in vertices:
#         adjacentVertices[v] = {}
#         pathWeight[v] = float("inf")
#         visitedEdge[v] = {}
#     pathWeight[s] = 0
#     for (u, v), w in edges.items():
#         adjacentVertices[u][v] = w
#         visitedEdge[u][v] = False
#     queue = [s]
#
#     while queue:
#         u = queue.pop(0)
#         for v, w in adjacentVertices[u].items():
#             if visitedEdge[u][v]:
#                 continue
#             if (pathWeight[u] + w) < pathWeight[v]:
#                 pathWeight[v] = pathWeight[u] + w
#                 parent[v] = u
#             visitedEdge[u][v] = True
#             queue.append(v)
#     return parent, pathWeight
#
#
# def findPath(parent, vertex):
#     path = []
#     while parent[vertex]:
#         vertex = parent[vertex]
#         path.append(vertex)
#     return path[::-1]
#
#
# def showPathAndWeight(pathWeight, parent, vertex):
#     path = findPath(parent, vertex)
#     for i in path:
#         print(i, end=" -> ")
#     print(vertex)
#     print("Minimum path weight of", vertex, ":", pathWeight[vertex])
#
#
# vertices = ['S', 'A', 'B', 'C', 'D', 'E', 'F']
# edges = {('S', 'A'): 1, ('S', 'B'): 2, ('A', 'B'): 3, ('A', 'C'): 5, ('A', 'E'): 2, ('B', 'A'): 1, ('B', 'D'): 1,
#          ('C', 'E'): 3, ('D', 'C'): 2, ('D', 'F'): 1, ('E', 'D'): 1, ('E', 'F'): 4}
# parent, pathWeight = BFSWeight(vertices, edges, 'S')
# print(parent, pathWeight)
# showPathAndWeight(pathWeight, parent, 'F')
from collections import deque


def BFSWeight(vertices, edges, s):
    adjacentVertices = {}
    visitedEdge = {}
    pathWeight = {}
    queueVertices = {s: True}
    parent = {s: None}
    for v in vertices:
        adjacentVertices[v] = {}
        pathWeight[v] = float("inf")
        visitedEdge[v] = {}
    pathWeight[s] = 0
    for (u, v), w in edges.items():
        adjacentVertices[u][v] = w
        visitedEdge[u][v] = False
    queue = deque()
    queue.append(s)

    while queue:
        u = queue.popleft()
        del queueVertices[u]
        for v, w in adjacentVertices[u].items():
            if (pathWeight[u] + w) < pathWeight[v]:
                pathWeight[v] = pathWeight[u] + w
                parent[v] = u
                if v not in queueVertices:
                    queueVertices[v] = True
                    queue.append(v)
            print(u, v, list(queue), pathWeight)
    return parent, pathWeight


def findPath(parent, vertex):
    path = []
    while parent[vertex]:
        vertex = parent[vertex]
        path.append(vertex)
    return path[::-1]


def showPathAndWeight(pathWeight, parent, vertex):
    path = findPath(parent, vertex)
    for i in path:
        print(i, end=" -> ")
    print(vertex)
    print("Minimum path weight of", vertex, ":", pathWeight[vertex])


vertices = ['S', 'A', 'B', 'C', 'D', 'E', 'F']
edges = {('S', 'A'): 1, ('S', 'B'): 2, ('A', 'B'): 3, ('A', 'C'): 5, ('A', 'E'): 2, ('B', 'A'): 1, ('B', 'D'): 1,
         ('C', 'E'): 3, ('D', 'C'): 2, ('D', 'F'): 1, ('E', 'D'): 1, ('E', 'F'): 4}
parent, pathWeight = BFSWeight(vertices, edges, 'S')
# print(parent, pathWeight)
showPathAndWeight(pathWeight, parent, 'F')
