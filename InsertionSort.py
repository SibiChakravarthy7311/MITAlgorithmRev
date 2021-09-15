arr = [5, 2, 4, 6, 1, 3]
for i in range(1, len(arr)):
    for j in range(i, 0, -1):
        # print("i:", i)
        # print("arr:", arr)
        if arr[j] < arr[j - 1]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
        else:
            break
print(arr)
