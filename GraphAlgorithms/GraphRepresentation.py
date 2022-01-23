v = [1, 2, 3, 4, 5]
vertex = {i: v[i] for i in range(len(v))}
vertexIndex = {v[i]: i for i in range(len(v))}

edges = [(1, 2), (1, 4), (2, 1), (2, 3), (2, 4), (3, 2), (3, 4), (3, 5), (4, 1), (4, 2), (4, 3), (4, 5), (5, 3), (5, 4)]

adjMat = [[0 for i in range(len(v))] for j in range(len(v))]

adj = {i: [] for i in v}
for i, j in edges:
    adj[i].append(j)
    adjMat[vertexIndex[i]][vertexIndex[j]] = 1

for key, value in adj.items():
    print(key, value)

print()
for i in adjMat:
    print(i)
