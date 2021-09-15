arr = [5, 2, 4, 6, 1, 3]
arr1 = [8, 5, 2, 9, 5, 6, 3]
arr2 = [4, 9, 8, 4, 3]


def mergeSort(arr):
    L = arr[0: len(arr) // 2]
    R = arr[len(arr) // 2:]
    a = []
    lp = 0
    rp = 0
    if len(L) > 1:
        L = mergeSort(L)
    if len(R) > 1:
        R = mergeSort(R)
    while lp < len(L) and rp < len(R):
        if L[lp] <= R[rp]:
            a.append(L[lp])
            lp += 1
        else:
            a.append(R[rp])
            rp += 1
    if lp < len(L):
        a.extend(L[lp:])
    elif rp < len(R):
        a.extend(R[rp:])
    # print(a)
    return a


print(mergeSort(arr2))
