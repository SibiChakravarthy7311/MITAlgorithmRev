# # n = int(input())
# # vertices = set()
# # edj = []
# # pre = {}
# # adj = {}
# # for i in range(n-1):
# #     s = input().split()
# #     s = [int(x) for x in s]
# #     vertices.add(s[0])
# #     vertices.add(s[1])
# #     edj.append(s)
# # vertices = list(vertices)
# # for i in vertices:
# #     adj[i] = []
# # for i in edj:
# #     adj[i[0]].append(i[1])
# # level = int(input())
# # l = 1
# # s = [vertices[0]]
# # cnt = 0
# # print(vertices)
# # def nodeCount(lev, arr):
# #     global cnt
# #     if(lev == level):
# #         cnt += len(arr)
# #         print(arr)
# #     else:
# #         for i in arr:
# #             nodeCount(lev+1, adj[i])
# # nodeCount(1, s)
# # print(cnt)
#
# n = int(input())
# vertices = []
# edj = []
# pre = {}
# adj = {}
# for i in range(n-1):
#     s = input().split()
#     s = [int(x) for x in s]
#     if(s[0] not in pre):
#         pre[s[0]] = 0
#         vertices.append(s[0])
#     if(s[1] not in pre):
#         pre[s[1]] = 0
#         vertices.append(s[1])
#     edj.append(s)
# for i in vertices:
#     adj[i] = []
# for i in edj:
#     adj[i[0]].append(i[1])
# level = int(input())
# l = 1
# s = [vertices[0]]
# cnt = 0
# def nodeCount(lev, arr):
#     global cnt
#     if(lev == level):
#         cnt += len(arr)
#     else:
#         for i in arr:
#             nodeCount(lev+1, adj[i])
# nodeCount(1, s)
# print(cnt)


# print(15%4)
# print(4*(15/4 - 15//4))


###########################################################
# n = int(input())
#
#
# def userMod(a):
#     v = a - (a//10)*10
#     return v
#
#
# def power(a, b):
#     res = 1
#     while(b > 0):
#         res *= a
#         b -= 1
#     # print(res)
#     return res
#
#
# def checkIsArmstrong(num, pow):
#     res = 0
#     temp = num
#     while(temp):
#         res += power(userMod(temp), pow)
#         temp = temp//10
#     return res == num
#
#
# def findPower(num):
#     po = 0
#     while num:
#         po += 1
#         num = num//10
#     return po
#
#
# p = findPower(n)
#
# if checkIsArmstrong(n, p):
#     print(n, "is an armstrong number")
# else:
#     print(n, "is not an armstrong number")
###########################################################


###########################################################
# s = "My name is Sibi Chakravarthy P"
# res = ""
# temp = ''
# for i in range(len(s)-1, -1, -1):
#     if s[i] == ' ':
#         res = temp + ' ' + res
#         temp = ''
#     else:
#         temp += s[i]
# res = temp + ' ' + res
# print(res)
###########################################################


###########################################################
# arr = [6, 36, 21, 18, 42]
# factor_count = []
# for i in arr:
#     # print(int(i**(1/2)), end=' ')
#     sq = int(i ** (1 / 2))
#     no_of_factors = 1
#     for j in range(2, sq):
#         if not i % j:
#             no_of_factors += 2
#             # print(j, int(i/j))
#     if not i % sq:
#         no_of_factors += 1
#     factor_count.append(no_of_factors)
# print(arr)
# print(factor_count, end='\n\n')

# for i in range(len(factor_count)-1):
#     for j in range(0, len(factor_count)-i-1):
#         if factor_count[j] > factor_count[j+1]:
#             factor_count[j], factor_count[j + 1] = factor_count[j+1], factor_count[j]
#             arr[j], arr[j+1] = arr[j+1], arr[j]
# print(arr)
# print(factor_count)
###########################################################


###########################################################
# arr = [10, 3, 9, 6, 1, 5]


# def mergeSort(arr):
#     L = arr[0:len(arr) // 2]
#     R = arr[len(arr) // 2: ]
#     if(len(arr) <= 1):
#         return arr
#     a = []
#     if len(L) > 1:
#         L = mergeSort(L)
#     if len(R) > 1:
#         R = mergeSort(R)
#     l = 0
#     r = 0
#     while l < len(L) and r < len(R):
#         if(L[l] <= R[r]):
#             a.append(L[l])
#             l += 1
#         else:
#             a.append(R[r])
#             r += 1
#     if(l < len(L)):
#         a.extend((L[l:]))
#     elif(r < len(R)):
#         a.extend(R[r:])
#     # print(a)
#     return a


# def mergeSort(arr):
#     L = arr[0 : len(arr)//2]
#     R = arr[len(arr)//2:]
#     a = []
#     l = 0
#     r = 0
#     if len(L) > 1:
#         L = mergeSort(L)
#     if len(R) > 1:
#         R = mergeSort(R)
#     while l < len(L) and r < len(R):
#         if L[l] <= R[r]:
#             a.append(L[l])
#             l += 1
#         else:
#             a.append(R[r])
#             r += 1
#     if l < len(L):
#         a.extend(L[l:])
#     elif r < len(R):
#         a.extend(R[r:])
#     return a
#
#
# arr = mergeSort(arr)
# print(arr)


# def mergeSwap(arr, arrswap):
#     L = arr[:len(arr)//2]
#     Lswap = arrswap[:len(arrswap)//2]
#     R = arr[len(arr)//2:]
#     Rswap = arrswap[len(arrswap) // 2:]
#     l = 0
#     r = 0
#     a = []
#     aswap = []
#     if len(L) > 1:
#         L, Lswap = mergeSwap(L, Lswap)
#     if len(R) > 1:
#         R, Rswap = mergeSwap(R, Rswap)
#     while l < len(L) and r < len(R):
#         if L[l] <= R[r]:
#             a.append(L[l])
#             aswap.append(Lswap[l])
#             l += 1
#         else:
#             a.append(R[r])
#             aswap.append(Rswap[r])
#             r += 1
#     if l < len(L):
#         a.extend(L[l:])
#         aswap.extend(Lswap[l:])
#     elif r < len(R):
#         a.extend(R[r:])
#         aswap.extend(Rswap[r:])
#     return a, aswap


# def mergeswap(arr, arrswap):
#     L = arr[len(arr)//2:]
#     R = arr[:len(arr) // 2]
#     Lswap = arrswap[len(arr) // 2:]
#     Rswap = arrswap[:len(arr) // 2]
#     l = 0
#     r = 0
#     if len(L) > 1:
#         L, Lswap = mergeswap(L, Lswap)
#     if len(R) > 1:
#         R, Rswap = mergeswap(R, Rswap)
#     a = []
#     aswap = []
#     while l < len(L) and r < len(R):
#         if L[l] <= R[r]:
#             a.append(L[l])
#             aswap.append(Lswap[l])
#             l += 1
#         else:
#             a.append(R[r])
#             aswap.append(Rswap[r])
#             r += 1
#     if l < len(L):
#         a.extend(L[l:])
#         aswap.extend(Lswap[l:])
#     elif r < len(R):
#         a.extend(R[r:])
#         aswap.extend(Rswap[r:])
#     return a, aswap
#
#
# factor_count, arr = mergeswap(factor_count, arr)
# print(arr)
# print(factor_count)


# arm = int(input())
#
#
# def userMod(n):
#     return n - 10*(n//10)
#
#
# def findPower(num):
#     p = 0
#     while(num):
#         p += 1
#         num = num//10
#     return p
#
#
# def checkIsArmstrong(num, p):
#     temp = num
#     res = 0
#     while temp:
#         res += userMod(temp)**p
#         temp = temp//10
#     print(res)
#     return res == num
#
#
# p = findPower(arm)
# if checkIsArmstrong(arm, p):
#     print(arm, "is an armstrong number")
# else:
#     print(arm, "is not an armstrong number")


# s = input()
#
#
# def checkIfPalindrome(s):
#     l = len(s)-1
#     for i in range(l//2):
#         if s[i] != s[l-i]:
#             return False
#     return True
#
#
# if checkIfPalindrome(s):
#     print(s, "is a Palindrome")
# else:
#     print(s, "is not a Palindrome")


arr = [1, 2, 2]
num_count = {}

for i in arr:
    if i in num_count:
        num_count[i] += 1
    else:
        num_count[i] = 1


print(num_count.items())
for i, j in num_count.items():
    num_count.pop(i)
    print(num_count.items())

# def subs(arr, num_count):
#     for i in num_count.items():
#

res = [[]]

