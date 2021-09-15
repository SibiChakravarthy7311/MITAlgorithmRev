# A - - B
# | \   | \
# |  \  |  E
# |   \ | /
# C - - D - |
#       | _ |

vertices = ['A', 'B', 'C', 'D', 'E']
adj = dict()
adj['A'] = ['B', 'C']
adj['B'] = ['A', 'D', 'E']
adj['C'] = ['A', 'D']
adj['D'] = ['A', 'B', 'C', 'D', 'E']
adj['E'] = ['B', 'E']

for i in vertices:
    print(adj[i])

adj_mat = [[0, 1, 1, 0, 0],
           [1, 0, 0, 1, 1],
           [1, 0, 0, 1, 0],
           [1, 1, 1, 1, 1],
           [0, 1, 0, 0, 1]]

map_vert = {0:'A', 1:'B', 2:'C', 3:'D', 4:'E'}

for i in range(len(adj_mat)):
    print('[', end="")
    for j in range(len(adj_mat[i])):
        if adj_mat[i][j]:
            print(map_vert[j], end=" ")
    print(']')
