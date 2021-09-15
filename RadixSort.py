arr = [432, 8, 530, 90, 88, 231, 11, 45, 677, 199]
m = max(arr)
it = len(str(m))
arrc = arr.copy()
base = 10
arrm = [0 for i in range(base)]
arrt = [0 for i in range(base)]
modc = [0 for i in range(base)]
for times in range(it):
    count = [0 for i in range(base)]
    for i in range(len(arr)):
        rem = arrc[i]%10
        arrc[i] = arrc[i]//10
        count[rem] += 1
        arrm[i] = rem

    # print("Count:", count)
    for i in range(1, len(count)):
        count[i] = count[i]+count[i-1]

    # print("CountMod:", count)
    # print(arrm)
    for i in range(len(arr)-1, -1, -1):
        count[arrm[i]] -= 1
        ind = count[arrm[i]]
        arrt[ind] = arr[i]
        modc[ind] = arrc[i]

    # print(modc)
    arr = arrt.copy()
    arrc = modc.copy()

print(arr)
