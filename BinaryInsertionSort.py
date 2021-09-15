arr = [5, 2, 4, 6, 1, 3]
for i in range(1, len(arr)):
    l = 0
    h = i
    while(h >= l):
        m = (h+l)//2
        if(arr[m] > arr[i]):
            h = m-1
        elif(arr[m] < arr[i]):
            l = m+1
        else:
            break
    # print("m:", m)
    if(arr[m] < arr[i]):
        m = m+1
    # print("mv:", m)
    var = arr[i]
    temp1 = arr[i+1:]
    temp = arr[m:i]
    arr = arr[0:m]
    arr.append(var)
    arr.extend(temp)
    arr.extend(temp1)
print(arr)