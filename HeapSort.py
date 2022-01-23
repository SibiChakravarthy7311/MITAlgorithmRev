arr = [16, 4, 10, 7, 8, 9, 3, 2, 14, 1]
arr1 = [2, 3, 1]
arr2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
arr3 = [48, 12, 24, 7, 8, -5, 24, 391, 24, 56, 2, 6, 8, 41]
arr4 = [-4, 5, 10, 8, -10, -6, -4, -2, -5, 3, 5, -4, -5, -1, 1, 6, -7, -6, -7, 8]
arr5 = [-7, 2, 3, 8, -10, 4, -6, -10, -2, -7, 10, 5, 2, 9, -9, -5, 3, 8]
arr6 = [427, 787, 222, 996, -359, -614, 246, 230, 107, -706, 568, 9, -246, 12, -764, -212, -484, 603, 934, -848, -646,
        -991, 661, -32, -348, -474, -439, -56, 507, 736, 635, -171, -215, 564, -710, 710, 565, 892, 970, -755, 55, 821,
        -3, -153, 240, -160, -610, -583, -27, 131]
arr7 = [991, -731, -882, 100, 280, -43, 432, 771, -581, 180, -382, -998, 847, 80, -220, 680, 769, -75, -817, 366, 956,
        749, 471, 228, -435, -269, 652, -331, -387, -657, -255, 382, -216, -6, -163, -681, 980, 913, -169, 972, -523,
        354, 747, 805, 382, -827, -796, 372, 753, 519, 906]
arr8 = [544, -578, 556, 713, -655, -359, -810, -731, 194, -531, -685, 689, -279, -738, 886, -54, -320, -500, 738, 445,
        -401, 993, -753, 329, -396, -924, -975, 376, 748, -356, 972, 459, 399, 669, -488, 568, -702, 551, 763, -90,
        -249, -45, 452, -917, 394, 195, -877, 153, 153, 788, 844, 867, 266, -739, 904, -154, -947, 464, 343, -312, 150,
        -656, 528, 61, 94, -581]
arr9 = [-823, 164, 48, -987, 323, 399, -293, 183, -908, -376, 14, 980, 965, 842, 422, 829, 59, 724, -415, -733, 356,
        -855, -155, 52, 328, -544, -371, -160, -942, -51, 700, -363, -353, -359, 238, 892, -730, -575, 892, 490, 490,
        995, 572, 888, -935, 919, -191, 646, -120, 125, -817, 341, -575, 372, -874, 243, 610, -36, -685, -337, -13, 295,
        800, -950, -949, -257, 631, -542, 201, -796, 157, 950, 540, -846, -265, 746, 355, -578, -441, -254, -941, -738,
        -469, -167, -420, -126, -410, 59]
arr10 = [3, 1, 2]


def maxHeapify(arr):
    for i in range((len(arr) - 1) // 2, -1, -1):
        parent = i
        left = parent * 2 + 1
        right = parent * 2 + 2
        while left <= len(arr):
            if right < len(arr):
                if arr[right] > arr[left]:
                    if arr[right] > arr[parent]:
                        arr[right], arr[parent] = arr[parent], arr[right]
                    parent = right
                else:
                    if arr[left] > arr[parent]:
                        arr[left], arr[parent] = arr[parent], arr[left]
                    parent = left
            elif left < len(arr):
                if arr[left] > arr[parent]:
                    arr[left], arr[parent] = arr[parent], arr[left]
                parent = left
            else:
                break
            left = parent * 2 + 1
            right = parent * 2 + 2

    return arr


def minHeapify(arr):
    for i in range((len(arr) - 1) // 2, -1, -1):
        parent = i
        left = parent * 2 + 1
        right = parent * 2 + 2
        while left < len(arr):
            if right < len(arr):
                if arr[right] < arr[left]:
                    if arr[right] < arr[parent]:
                        arr[right], arr[parent] = arr[parent], arr[right]
                    parent = right
                else:
                    if arr[left] < arr[parent]:
                        arr[left], arr[parent] = arr[parent], arr[left]
                    parent = left
            else:
                if arr[left] < arr[parent]:
                    arr[left], arr[parent] = arr[parent], arr[left]
                parent = left

            left = parent * 2 + 1
            right = parent * 2 + 2

    return arr


def checkMinHeap(arr):
    for i in range((len(arr) - 1) // 2):
        parent = i
        left = parent * 2 + 1
        right = parent * 2 + 2
        if right < len(arr):
            if arr[left] < arr[right]:
                child = left
            else:
                child = right
        else:
            child = left
        if arr[child] < arr[parent]:
            return False
    return True


def checkMaxHeap(arr):
    for i in range((len(arr) - 1) // 2):
        parent = i
        left = parent * 2 + 1
        right = parent * 2 + 2
        if right < len(arr):
            if arr[left] > arr[right]:
                child = left
            else:
                child = right
        else:
            child = left
        if arr[child] > arr[parent]:
            return False
    return True


def siftDownMax(arr, l):
    parent = 0
    left = parent * 2 + 1
    right = parent * 2 + 2
    if right < l:
        if arr[left] > arr[right]:
            child = left
        else:
            child = right
    else:
        child = left
    while arr[child] > arr[parent]:
        arr[child], arr[parent] = arr[parent], arr[child]
        parent = child
        left = parent * 2 + 1
        right = parent * 2 + 2
        if right < l:
            if arr[left] > arr[right]:
                child = left
            else:
                child = right
        else:
            child = left
        if left >= l:
            break
    return arr


def siftDownMin(arr, l):
    parent = 0
    left = parent * 2 + 1
    right = parent * 2 + 2
    if right < l:
        if arr[left] < arr[right]:
            child = left
        else:
            child = right
    else:
        child = left
    while arr[child] < arr[parent]:
        arr[child], arr[parent] = arr[parent], arr[child]
        parent = child
        left = parent * 2 + 1
        right = parent * 2 + 2
        if right < l:
            if arr[left] < arr[right]:
                child = left
            else:
                child = right
        else:
            child = left
        if left >= l:
            break
    return arr


def maxHeapSort(arr):
    arr = maxHeapify(arr)
    l = len(arr)
    for i in range(l - 1):
        arr[0], arr[l - 1 - i] = arr[l - 1 - i], arr[0]
        arr = siftDownMax(arr, l - 1 - i)
    arr[0], arr[1] = arr[1], arr[0]
    return arr


def minHeapSort(arr):
    arr = minHeapify(arr)
    l = len(arr)
    for i in range(1, l - 1):
        arr[0], arr[l - i] = arr[l - i], arr[0]
        arr = siftDownMin(arr, l - i)
    arr[0], arr[1] = arr[1], arr[0]
    return arr


print(maxHeapSort(arr9))
print()
print(minHeapSort(arr9))

