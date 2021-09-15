# a - s   d - f
# |   | / | / |
# z   x - c - v
#
# vertices = ['a', 's', 'd', 'f', 'z', 'x', 'c', 'v']
# adj = dict()
# adj['a'] = ['s', 'z']
# adj['s'] = ['a', 'x']
# adj['d'] = ['x', 'c', 'f']
# adj['f'] = ['d', 'c', 'v']
# adj['z'] = ['a']
# adj['x'] = ['s', 'd', 'c']
# adj['c'] = ['x', 'd', 'f', 'v']
# adj['v'] = ['c', 'f']

vertices = ['a', 'b', 'c', 'd', 'e', 'f']
adj = dict()
adj['a'] = ['b', 'd']
adj['b'] = ['e']
adj['c'] = ['e', 'f']
adj['d'] = ['b']
adj['e'] = ['d']
adj['f'] = ['f']

# parent = {'s': None}
# V = 0

parent = {}


def DFS_visit(V, adj, s):
    # global V
    global parent
    for v in adj[s]:
        if v not in parent:
            print(v, end=' ')
            parent[v] = s
            DFS_visit(V, adj, v)
        # else:
        #     print("D"+v, end=' ')
        # V += 1


def DFS(V, adj):
    global parent
    for s in V:
        if s not in parent:
            print(s, end=' ')
            parent[s] = None
            DFS_visit(V, adj, s)


DFS(vertices, adj)
# print('\n', V)
print()
start = 'a'
parent = {start: None}
print(start, end=' ')
DFS_visit(vertices, adj, start)
