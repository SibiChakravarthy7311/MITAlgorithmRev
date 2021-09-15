arr = [3, 8, 5, 2, 4, 8, 5, 1, 4, 2, 5, 0, 9, 5, 8, 9, 0, 4, 1]
m = max(arr)

# method 1
l = [[] for i in range(m+1)]
for i in range(len(arr)):
    # print(arr[i], end=" ")
    l[arr[i]].append(arr[i])
    # print(l)
# for i in range(len(arr)):
#     print(l[arr[i]], end=" ")
output = []
for i in range(m+1):
    output.extend(l[i])
# print(l)
print(output)


# method 2
# arr = [2, 1, 1, 0, 2, 5, 4, 0, 2, 8, 7, 7, 9, 2, 0, 1, 9]
cn = [0 for i in range(m+1)]
# print(cn)
for i in range(len(arr)):
    cn[arr[i]] += 1
output1 = []
for i in range(m+1):
    output1.extend([i]*cn[i])
print(output1)