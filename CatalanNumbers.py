arr = [1, 1]
n = int(input("Enter no. of catalan numbers to find: "))

for i in range(2, n):
    sum = 0
    for j in range(i):
        sum += arr[i-j-1]*arr[j]
        # print(i-j-1, j)
    arr.append(sum)
print(arr)
