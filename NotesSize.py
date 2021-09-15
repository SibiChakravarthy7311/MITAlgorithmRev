from collections import defaultdict
import math
from itertools import permutations
import xlrd
import pandas as pd
import os
import numpy as np

file1 = open('MIT Algorithm Notes.txt', 'r')
s1 = file1.read()
file1.close()
s1 = s1.split()
# print(s1)
print(len(s1))
# for i in s1:
#     print(i)


# s = "0032"
# s1 = "2147483648"
# s2 = "2147483649"
# num = 2**32
# # print(int(s))
# # print(num)
# print(s1 > s2)

# s = "42"
# s = s.strip()
# n = ''
# num = 2**31
# bound = [str(num),str(num-1)]
# sign = '+'
# if(s[0] == '-' or s[0] == '+'):
#     sign = s[0]
#     s = s[1:]
# for i in range(len(s)):
#     if(48 <= ord(s[i]) <= 57):
#         n += s[i]
# n = n.zfill(len(bound[0]))
# if(sign == '-'):
#     if(n > bound[0]):
#         n = bound[0]
#     sign = -1
# else:
#     if(n > bound[1]):
#         n = bound[1]
#     sign = 1
# print(sign*int(n))
# print(s)

# target = 9
# nums = [2, 7, 9, 11]
# res = []
# for i in range(len(nums)):
#
#     rem = target - nums[i]
#     print(rem)
#     if(rem in nums and nums.index(rem) != i):
#         res.append(i)
#         res.append(nums.index(rem))
#         break
# print(res)
# # nums = nums.sort()
# nums.sort()
# print(nums)
# st = 0
# end = len(nums)-1
# while(st < end):
#     s = nums[st]+nums[end]
#     if(s > target):
#         end -= 1
#     elif s < target:
#         st += 1
#     else:
#         res = [st, end]
#         break

# target = 6
# nums = [3, 3]
# compdict1 = {}
# for i in range(len(nums)):
#     if(nums[i] in compdict1.keys()):
#         res.append(compdict1[nums[i]])
#         res.append(i)
#         print([compdict1[nums[i]], i])
#         break
#     rem = target - nums[i]
#     compdict1[rem] = i
#
# print(compdict1)
# print(res)
#
# if 3 in compdict1:
#     print(True)

# numbers = [3, 3]
# target = 6
# st = 0
# end = len(numbers)-1
# while(st < len(numbers) and end >=0):
#     s = numbers[st]+numbers[end]
#     if(s < target):
#         st += 1
#     elif(s > target):
#         end -= 1
#     else:
#         res = [st, end]
#         res.sort()
#         print(res)
#         break

# while(st < end):
#     s = nums[st]+nums[end]
#     if(s > target):
#         end -= 1
#     elif s < target:
#         st += 1
#     else:
#         res = [st, end]
#         break
# print(res)

# cnt = 0
# for i in range(len(nums)):
#     s = 0
#     for j in range(i, len(nums)):
#         s += nums[j]
#         if(s == k):
#             cnt += 1
# return cnt

# nums = [100, 1, 2, 100, 2, 100, 1, 1, 1, 100, 2]
# k = 3
# nums = [1, 1, 1]
# k = 2
# for i in range(len(nums)):
#     sumdict = {}
#     sumdict[0] = -1
#     s = 0
#     for j in range(i, len(nums)):
#         s += nums[j]
#         rem = s-k
#         # print("s:", s)
#         # print(rem)
#         if (rem in sumdict):
#             cnt += 1
#             print("sumdict:", sumdict)
#             print("rem:", rem, " sum:", s)
#             print([sumdict[rem], j])
#         sumdict[s] = j

nums = [-92, -63, 75, -86, -58, 22, 31, -16, -66, -67, 420]
k = 100


# k = 0
# sumdict = {}
# sumdict[0] = 1
# s = 0
# for j in range(len(nums)):
#     s += nums[j]
#     rem = s - k
#     # print("s:", s)
#     # print(rem)
#     if (rem in sumdict):
#         cnt += sumdict[rem]
#         print("sumdict:", sumdict)
#         print("rem:", rem, " sum:", s)
#         print([sumdict[rem], j])
#     if(s in sumdict):
#         sumdict[s] += 1
#     else:
#         sumdict[s] = 1
# print(cnt)
# print(s)

# nums = [23, 2, 4, 6, 6]
# k = 7
# nums = [5, 0, 0, 0]
# k = 3
# dictsum = {0: -1}
# s = 0
# for i in range(len(nums)):
#     fac = nums[i]%k
#     s += fac
#     rem = s%k
#     print(rem, end=" ")
#     if(rem in dictsum):
#         if(i > dictsum[rem]+1):
#             print(True)
#             break
#     else:
#         dictsum[rem] = i
# # print(dictsum)
# print("|")

# cumsum = 0
# seen = {0 :-1}
# for i in range(len(nums)):
#     cumsum += nums[i]
#     mod = cumsum % k
#     print(mod, end=" ")
#
#     if mod in seen:
#         if i - seen[mod] > 1:
#             print(True)
#             break
#     else:
#         seen[mod] = i
# print(False)


# nums = [1, -1, 7]
# s = sum(nums)
# cumsum = 0
# if(s == nums[0]):
#     print(0)
# for i in range(1, len(nums)):
#     cumsum += nums[i-1]
#     if(cumsum == s-nums[i]-cumsum):
#         print(i)
#         break


# nums = [1, 1, 1, 2, 2, 3, 4, 4, 5, 6, 7, 7, 8, 8, 8]
# temp = nums[0]
# end = 1
# for i in range(1, len(nums)):
#     if(nums[i] != temp):
#         nums[end] = nums[i]
#         temp = nums[end]
#         end += 1
#         print(end)
# print(nums[:end])

# nums = [1, 2, 3, 4]
# queries = [[1, 0], [-3, 1], [-4, 0], [2, 3]]
# s = 0
# for i in range(len(nums)):
#     if (not nums[i] % 2):
#         s += nums[i]
# res = []
# for i in range(len(queries)):
#     val = queries[i][0]
#     index = queries[i][1]
#     if (not nums[index] % 2):
#         s = s - nums[index]
#         nums[index] += val
#         if (not val % 2):
#             s += nums[index]
#     else:
#         nums[index] += val
#         if (val % 2):
#             s += nums[index]
#     res.append(s)
# print(res)

# nums = [3, 2, 2, 3]
# val = 3
# cnt = 0
# end = len(nums)-1
# for i in range(len(nums)):
#     if(len(nums)-i <= cnt):
#         break
#     if(nums[i] == val):
#         nums = nums[:i]+nums[i+1:]
#         nums.append(val)
#         cnt += 1
# print(cnt)
# print(nums)
# i = 0

# forw = [1, 2]
# rev = [2, 1]
# print(forw == rev)


# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#
#
# head = ListNode(1)
# head.next = ListNode(2)
# head.next.next = ListNode(2)
# head.next.next.next = ListNode(1)
#
#
# def isPalindrome(head):
#     curr = head
#     nxt = None
#     prev = None
#     forw = []
#     rev = []
#     while (curr):
#         forw.append(curr.val)
#         nxt = curr.next
#         curr.next = prev
#         prev = curr
#         curr = nxt
#     curr = prev
#     # while (curr):
#     #     if(forw.pop(0) == curr.val):
#     #         curr = curr.next
#     #     else:
#     #         return False
#     for i in range(len(forw)//2):
#         if (forw.pop(0) == curr.val):
#             curr = curr.next
#         else:
#             return False
#     return True
#
#
# print(isPalindrome(head))


# nums = [0, 1, 0, 3, 12]
# i = 0
# for j in range(len(nums)):
#     if(nums[j]):
#         nums[i] = nums[j]
#         i += 1
# arr = [0]*(len(nums)-i)
# nums = nums[:i]
# nums.extend(arr)
# print(arr)
# print(nums)


# s = "A man, a plan, a canal: Panama"
# s = s.lower()
# s = list(s)
# pal = ""
# for i in s:
#     val = ord(i)
#     if(97 <= val <= 122):
#         pal += i
# print(pal == pal[::-1])


# matrix =  [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# a =  [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
# a = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
# result =  [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
# # sample = [[0, 0, 0], [0, 1, 0], [1, 1, 1]]
# # sample1 = [[1, 1, 1], [0, 1, 0], [0, 0, 0]]
# mat = [[1, 1], [0, 1]]
# target = [[1, 1], [1, 0]]
#
def printMat(mat):
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            print(mat[i][j], end=" ")
        print()


#
# def findRotation(mat, target):
#     if (mat == target):
#         return True
#     n = len(mat) - 1
#     for k in range(3):
#         for i in range(len(mat) // 2):
#             for j in range(i, n - i):
#                 # 1 mat[i][j]
#                 # 2 mat[n-j][i]
#                 # 3 mat[n-i][n-j]
#                 # 4 mat[j][n-i]
#                 temp = mat[i][j]
#                 mat[i][j] = mat[n - j][i]
#                 mat[n - j][i] = mat[n - i][n - j]
#                 mat[n - i][n - j] = mat[j][n - i]
#                 mat[j][n - i] = temp
#         printMat(mat)
#         print()
#         printMat(target)
#         print("\n")
#         if (mat == target):
#             return True
#     return mat == target
#
#
# print(findRotation(mat, target))
# n = len(matrix)-1
# for i in range(len(matrix)//2):
#     for j in range(i, n-i):
#         temp = matrix[i][j]
#         matrix[i][j] = matrix[n - j][i]
#         matrix[n - j][i] = matrix[n - i][n - j]
#         matrix[n - i][n - j] = matrix[j][n - i]
#         matrix[j][n - i] = temp
# printMat(matrix)
# printMat(a)
#
# for i in range(n//2):
#     for j in range(i, n-i):
#         print(n-i, n-j)


# arr = [1, 2, 3]
# def checkArraySortRotate(nums):
#     # i = 0
#     # while (i < len(nums)):
#     #     if (nums[i] < nums[i - 1]):
#     #         break
#     #     i += 1
#     # if(i >= len(nums)):
#     #     return True
#     # print(i)
#     # ind = i
#     # arr = nums[ind:]
#     # arr.extend(nums[:ind])
#     # chk = arr.copy()
#     # arr.sort()
#     # print(chk)
#     # print(arr)
#     # return arr == chk
#     i = 0
#     pt = 1
#     while (i < len(nums) - 1):
#         if (nums[i] > nums[i + 1]):
#             pt -= 1
#         if (pt < 0):
#             return False
#         i += 1
#     # if(i >= len(nums)-1):
#     #     return True
#     # i += 1
#     # arr = nums[i:]
#     # arr.extend(nums[:i])
#     # chk = arr.copy()
#     # arr.sort()
#     # return arr == chk
#     if (pt == 1):
#         return True
#     if (nums[-1] <= nums[0]):
#         return True
#     return False
#
#
# print(checkArraySortRotate(arr))


nums = [[1, 2, 3, 4, 5], [6, 7], [8], [9, 10, 11], [12, 13, 14, 15, 16]]
# m = 0
# for i in nums:
#     if(len(i) > m):
#         m = len(i)
#
# if(len(nums) > m):
#     m = len(nums)
#
# for i in nums:
#     if(len(i) < m):
#         fill = [0]*(m-len(i))
#         i.extend(fill)
#
# res = []
# for k in range(len(nums)):
#     i = k
#     j = 0
#     while(j <= k):
#         if(nums[i][j]):
#             res.append(nums[i][j])
#         j += 1
#         i -= 1
#
# for k in range(len(nums)-2, -1, -1):
#     i = len(nums)-1
#     j = i-k
#     while (j <= len(nums)-1):
#         if (nums[i][j]):
#             res.append(nums[i][j])
#         j += 1
#         i -= 1
#
# print(res)
# # printMat(nums)

# nums = [[1,2,3,4,5,6]]
# m = 0
# for i in nums:
#     if(len(i) > m):
#         m = len(i)
# if(len(nums) > m):
#     m = len(nums)
# k = [[] for j in range(2*m-1)]
# for i, r in enumerate(nums):
#     print(i, r)
#     for j, val in enumerate(r):
#         print(j, val)
#         k[i+j] = [val]+k[i+j]
#     print()
#
# res = []
# for i in k:
#     res.extend(i)
# print(k)
# print(res)


# arr = [1, 2, 3, 4, 5, 10, 6, 7, 8, 9]
# k = 5
# # arr = [1, 2, 3, 4, 5, 6]
# # k = 10
# # arr = [1, 2, 3, 4, 5, 6]
# # k = 7
# # arr = [-4, -7, 5, 2, 9, 1, 10, 4, -8, -3]
# # k = 3
#
# dictsum = {}
#
# # for i in range(len(arr)):
# #     fac = arr[i] % k
# #     if (fac in dictsum):
# #         dictsum.pop(fac)
# #     else:
# #         dictsum[fac] = i
# # print(not dictsum)
# # print(dictsum)
# dictdef = defaultdict(int)
#
#
# for i in range(len(arr)):
#     fac = k - arr[i] % k
#     rem = arr[i]%k
#     if (rem in dictsum):
#         if(dictsum[rem] == 1):
#             dictsum.pop(rem)
#         else:
#             dictsum[rem] -= 1
#     else:
#         if(rem == 0):
#             dictsum[rem] = 1
#         else:
#             if(fac in dictsum):
#                 dictsum[fac] += 1
#             else:
#                 dictsum[fac] = 1
#     # print(arr[i])
#     # print(dictsum)
# print(not dictsum)
#
#
# count = 0
# for i in range(len(arr)):
#     fac = arr[i]%k
#     m = fac if fac==0 else k-fac
#     if(dictdef[m] > 0):
#         dictdef[m] -= 1
#         count += 2
#     else:
#         dictdef[fac] += 1
# print(len(arr) == count)
#
# # arr = [1, 2, 3, 4, 5, 6]


# arr = [0, 2, 1, -6, 6, -7, 9, 1, 2, 0, 1]
# arr = [0, 0, 0, 0]
# s = sum(arr)
# if(s%3):
#     print(False)
# cs = 0
# cnt = 0
# for i in range(len(arr)):
#     cs += arr[i]
#     if(cs == s/3):
#         cs = 0
#         cnt += 1
# if(cnt >= 3):
#     print(True)
# else:
#     print(False)


# nums = [1, 2, 3, 1, 1, 3]
# res = 0
# s = set(nums)
# for i in s:
#     cnt = nums.count(i)
#     if(cnt > 1):
#         res += math.comb(cnt, 2)
# print(res)


# cardPoints = [1, 2, 3, 4, 5, 6, 1]
# k = 3
#
# cardPoints = [32, 69, 37, 79, 4, 33, 29, 33, 45, 1, 99, 90, 56, 24, 76]
# k = 10
# if k == len(cardPoints):
#     print(sum(cardPoints))
# rem = k
# start = 0
# res = 0
# end = len(cardPoints)
# while(rem):
#     print("Rem:", rem)
#     print("Beginning Sum:", sum(cardPoints[:rem]))
#     print("Ending Sum:", sum(cardPoints[-rem:]))
#     if(sum(cardPoints[start:start+rem]) >= sum(cardPoints[end-rem:end])):
#         res += cardPoints[start]
#         start += 1
#         rem -= 1
#     else:
#         res += cardPoints[end-1]
#         end -= 1
#         rem -= 1
#     print("Result:", res)
#     print("Resultant Array:", cardPoints[start:end+1])
# print(res)
#
# rem = k
# startp = 0
# endp = 0
# start = 0
# res = 0
# end = len(cardPoints)
# first = sum(cardPoints[:k])
# last = sum(cardPoints[-k:])
# print(cardPoints[:])
# while (rem):
#     print("Rem:", rem)
#     print("Beginning Sum:", first)
#     print("Ending Sum:", last)
#     if (first >= last):
#         res += cardPoints[start]
#         first -= cardPoints[start]
#         last -= cardPoints[end - rem]
#         start += 1
#         rem -= 1
#         startp += 1
#     else:
#         res += cardPoints[end-1]
#         last -= cardPoints[end-1]
#         first -= cardPoints[start + rem - 1]
#         end -= 1
#         rem -= 1
#         endp += 1
#     print("Result:", res)
#     print("Resultant Array:", cardPoints[start:end + 1])
# print(res)
#
# print("Start:", startp)
# print("Endp:", endp)


# nums = [5, 4, 0, 3, 1, 6, 2]
# nums = [0, 1, 2]
# visited = {}
# length = {}
# m = 0
# for i in range(len(nums)):
#     if i not in length:
#         length[i] = 1
#     visited = {}
#     visited[i] = True
#     while (True):
#         curr = nums[i]
#         if (curr in visited):
#             break
#         visited[curr] = True
#         if (curr in length):
#             length[i] += length[curr]
#             if (length[i] > m):
#                 m = length[i]
#             break
#         length[i] += 1
# print(m)



# To open Workbook
# loc = "C:/Sibi/DadFiles/2018 batch Mini project Review Sheet.xlsx"
# wb = xlrd.open_workbook(loc)
# sheet = wb.sheet_by_index(0)

# # For row 0 and column 0
# print(sheet.cell_value(0, 0))
#
# # Extracting number of rows
# print(sheet.nrows)
#
# # Extracting number of columns
# print(sheet.ncols)
#
# # Extracting all column names
# for i in range(sheet.ncols):
#     print(sheet.cell_value(6, i), end = " ")
#
# # Extracting First Column
# for i in range(sheet.nrows):
#     print(sheet.cell_value(i, 0))

# #Extracting All Data
# for i in range(sheet.nrows):
#     for j in range(sheet.ncols):
#         print(str(sheet.cell_value(i, j)).ljust(20), end = " ")
#     print()


####################################################################################

# # pd.read_excel("C:/Sibi/DadFiles/2018 batch Mini project Review Sheet.xlsx")
# df1 = pd.read_excel(
#      "C:/Sibi/DadFiles/2018 batch Mini project Review Sheet.xlsx",
#      engine='openpyxl',
# )
#
# df2 = pd.read_excel(
#      "C:/Sibi/DadFiles/2018batchMiniprojectReviewSheet.xlsx",
#      engine='openpyxl',
# )
#
# comparison_values = df1.values == df2.values
# # print (comparison_values)
#
# rows, cols = np.where(comparison_values == False)
# # for item in zip(rows,cols):
# #     df1.iloc[item[0], item[1]] = '{} --> {}'.format(df1.iloc[item[0], item[1]],df2.iloc[item[0], item[1]])
#
# for item in zip(rows,cols):
#     df1.iloc[item[0], item[1]] = ''.format(df1.iloc[item[0], item[1]],df2.iloc[item[0], item[1]])
#
# df1.to_excel('./Excel_diff.xlsx', index=False, header=True)

####################################################################################

# arr = [1,3,7,11,12,14,18]
# cnt = 0
# a = 0
# b = 1
# c = 0
# b1 = False
# b2 = False
# fl = False
# for i in range(len(arr)):
#     if(arr[i] == 1 or cnt):
#         s = 1
#         ind = i+1
#         cnt += 1
#         # fl = True
#         break
#     a = 1
#     b = 1
#     c = 0
#     while(c < arr[i]):
#         c = a+b
#         b = a
#         a = c
#         if(arr[i] == c):
#             cnt += 1
#             s = c
#             ind = i+1
#             # fl = True
#             print(arr[i], end=" ")
#             break
# if(not cnt):
#     print(0)
# elif(s == 1):
#     print("s:", s)
#     while(ind < len(arr)):
#         print("ind:", ind, "len(arr):", len(arr))
#         if(arr[ind] == 1):
#             cnt += 1
#             b1 = False
#             print(arr[ind], end=" ")
#             break
#         elif(arr[ind] == 2):
#             cnt += 1
#             b2 = False
#             print(arr[ind], end=" ")
#             break
#         ind += 1
#     if(b2):
#         s = 3
#         b = 2
#     elif(b1):
#         s = 2
#         b = 1
#     while(ind < len(arr)):
#         if(arr[ind] == s):
#             cnt += 1
#             temp = s
#             s += b
#             b = temp
#             print(arr[ind], end=" ")
#         ind += 1
# else:
#     while(ind < len(arr)):
#         if(arr[ind] == s):
#             cnt += 1
#             temp = s
#             s += b
#             b = temp
#             print(arr[ind], end=" ")
#         ind += 1
# print(cnt)
# print("count:", cnt)
# for i in range(len(arr)):
#     print("i:", i)
#     print("c:", c)
#     print("arr[i]:", arr[i])
#     if(c == arr[i]):
#         print("c:", c)
#         print("arr[i]:", arr[i])
#         cnt += 1
#         print("countIf:", cnt)
#         continue
#     while(c < arr[i]):
#         c = a+b
#         a = b
#         b = c
#         if(c == arr[i]):
#             print("c:", c)
#             print("arr[i]:", arr[i])
#             cnt += 1
#             print("countWhile:", cnt)
#             break
# # print("a:", a)
# # print("b:", b)
# #
# print("count:", cnt)


# This problem is yet unsolved and requires dynamic programming approach to be implemented for a feasible solution
# arr = [1, 3, 7, 11, 12, 14, 18]
# cnt = 2
# m = 2
# a = arr[0]
# b = arr[1]
# for i in range(len(arr)-2):
#     a = arr[i]
#     for j in range(i+1, len(arr)-1):
#         # print(cnt)
#         m = max(m, cnt)
#         cnt = 2
#         b = arr[j]
#         c = a + b
#         dum = a
#         k = j
#         while(c <= arr[-1] and k < len(arr)-1):
#             if(c in arr[k:]):
#                 cnt += 1
#                 k = arr.index(c)
#                 dum = b
#                 b = c
#                 c += dum
#                 print("i, j, c, arr[k], cnt:", i, j, c, arr[k], cnt)
#                 k += 1
#             else:
#                 print("i, j, c, arr[k], cnt:", i, j, c, arr[k], cnt)
#                 c -= arr[k]
#                 k += 1
#                 c += arr[k]
# print(m)
