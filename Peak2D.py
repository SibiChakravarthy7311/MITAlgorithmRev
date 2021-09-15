arr = [[12, 13, 12, 13],
       [11, 12, 13,  9],
       [ 7,  3, 14, 10],
       [10,  9, 15, 12]]

rl = rgl = 0
rh = rgh = len(arr[0])-1
cl = 0
ch = len(arr)-1

while rgl <= rgh:
       rm = (rgl+rgh)//2
       ind = arr[rm].index(max(arr[rm]))
       # print("rgl:", rgl)
       # print("rgh:", rgh)
       # print("rm:", rm)
       # print("ind:", ind)

       l = []
       if(rm == 0):
              l.append(1)
       elif(arr[rm-1][ind] < arr[rm][ind]):
              l.append(1)
       else:
              rgh = rm-1
       if (rm == rh):
              l.append(1)
       elif (arr[rm + 1][ind] < arr[rm][ind]):
              l.append(1)
       else:
              rgl = rm+1
       if(len(l) == 2):
              print(arr[rm][ind])
              break