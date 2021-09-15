# arr = [6, 36, 42, 21, 4]
#
# factors = []
#
# for i in arr:
#     sq = int(i**(1/2))
#     no_of_factors = 2
#     for j in range(2, sq):
#         if not i%j:
#             no_of_factors += 2
#     if not i%sq:
#         if sq**2 == i:
#             no_of_factors += 1
#         else:
#             no_of_factors += 2
#     factors.append(no_of_factors)
#
# print(arr)
# print(factors)
#
#
# def mergeswap(arr, arrswap):
#     L = arr[:len(arr)//2]
#     Lswap = arrswap[:len(arr) // 2]
#     R = arr[len(arr) // 2:]
#     Rswap = arrswap[len(arr) // 2:]
#     l = 0
#     r = 0
#     a = []
#     aswap = []
#     if len(L) > 1:
#         L, Lswap = mergeswap(L, Lswap)
#     if len(R) > 1:
#         R, Rswap = mergeswap(R, Rswap)
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
# arr, factors = mergeswap(arr, factors)
# print(arr)
# print(factors)


# arr = [6, 36, 42, 21, 4]
#
# factors = []
#
# for i in arr:
#     sq = int(i ** (1/2))
#     no_of_factors = 2
#     for j in range(2, sq):
#         if not i % j:
#             no_of_factors += 2
#     if not i % sq:
#         if sq**2 == i:
#             no_of_factors += 1
#         else:
#             no_of_factors += 2
#     factors.append(no_of_factors)
#
# print(arr)
# print(factors)
#
#
# def mergeswap(arr, arrswap):
#     L = arr[:len(arr)//2]
#     R = arr[len(arr) // 2:]
#     Lswap = arrswap[:len(arr) // 2]
#     Rswap = arrswap[len(arr) // 2:]
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
# arr, factors = mergeswap(arr, factors)
# print(arr)
# print(factors)


# s = input()
#
#
# def checkIsPalindrome(s):
#     l = len(s)-1
#     for i in range(len(s)//2):
#         if s[i] != s[l-i]:
#             return False
#     return True
#
#
# if checkIsPalindrome(s):
#     print(s, "is a palindrome")
# else:
#     print(s, "is a not palindrome")


# def fibonacci(num):
#     if not num:
#         return
#     if num == 1:
#         print(0, end=" ")
#         return
#     if num == 2:
#         print(0, 1, end=" ")
#         return
#     if num > 2:
#         print(0, 1, end=" ")
#         fibonaccihelper(0, 1, num-2)
#
#
# def fibonaccihelper(l, h, check):
#     if not check:
#         return
#     print(l+h, end=" ")
#     fibonaccihelper(h, l+h, check-1)
#
#
# fibonacci(5)


# num = 5
# l = 0
# h = 1
# if num >= 1:
#     print(l, end = " ")
# if num >= 2:
#     print(h, end = " ")
# num -= 2
# while num:
#     print(l+h, end = " ")
#     l, h = h, l+h
#     num -= 1

# arr = [6, 36, 42, 21, 4]
# factors = []
#
# for i in arr:
#     sq = int(i ** (1/2))
#     no_of_factors = 2
#     for j in range(2, sq):
#         if not i%j:
#             no_of_factors += 2
#     if not i%sq:
#         if sq**2 == i:
#             no_of_factors += 1
#         else:
#             no_of_factors += 2
#     factors.append(no_of_factors)
#
# print(arr)
# print(factors)


# def merge(arr, arrs):
#     L = arr[0:len(arr)//2]
#     R = arr[len(arr) // 2:]
#     Ls = arrs[0:len(arr) // 2]
#     Rs = arrs[len(arr) // 2:]
#
#     l = 0
#     r = 0
#     a = []
#     aswap = []
#
#     if len(L) > 1:
#         L, Ls = merge(L, Ls)
#     if len(R) > 1:
#         R, Rs = merge(R, Rs)
#     while l < len(L) and r < len(R):
#         if L[l] <= R[r]:
#             a.append(L[l])
#             aswap.append(Ls[l])
#             l += 1
#         else:
#             a.append(R[r])
#             aswap.append(Rs[r])
#             r += 1
#
#     if l < len(L):
#         a.extend(L[l:])
#         aswap.extend(Ls[l:])
#     elif r < len(R):
#         a.extend(R[r:])
#         aswap.extend(Rs[r:])
#     return a, aswap
#
#
# # factors, arr = merge(factors, arr)
#
# for i in range(len(arr)-1):
#     for j in range(len(arr)-1-i):
#         if arr[j] > arr[j+1]:
#             temp = arr[j]
#             arr[j] = arr[j+1]
#             arr[j+1] = temp
#             # arr[j], arr[j+1] = arr[j+1], arr[j]
#
# # print(arr)
# # print(factors)

# arr = [6, 36, 42, 21, 4]
# factors = []
# for i in arr:
#     sq = int(i**(1/2))
#     no_of_factors = 2
#     for j in range(2, sq):
#         if not i % j:
#             no_of_factors += 2
#     if not i % sq:
#         if sq ** 2 == i:
#             no_of_factors += 1
#         else:
#             no_of_factors += 2
#     factors.append(no_of_factors)
#
# print(arr)
# print(factors)
#
# for i in range(len(factors)-1):
#     for j in range(len(factors)-1-i):
#         if factors[j] > factors[j+1]:
#             temp = factors[j]
#             factors[j] = factors[j+1]
#             factors[j+1] = temp
#             temp1 = arr[j]
#             arr[j] = arr[j+1]
#             arr[j+1] = temp1
#
# print()
# print(arr)
# print(factors)


# arr = [6, 36, 42, 21, 4]
#
# factors = []
#
# for i in arr:
#     sq = int(i ** (1/2))
#     no_of_factors = 2
#     for j in range(2, sq):
#         if not i % j:
#             no_of_factors += 2
#     if not i % sq:
#         if sq**2 == i:
#             no_of_factors += 1
#         else:
#             no_of_factors += 2
#     factors.append(no_of_factors)
#
# print(arr)
# print(factors)
#
#
# def merge(arr, arrswap):
#     L = arr[:len(arr)//2]
#     R = arr[len(arr) // 2:]
#     Lswap = arrswap[:len(arr) // 2]
#     Rswap = arrswap[len(arr) // 2:]
#     a = []
#     aswap = []
#     l = 0
#     r = 0
#     if len(L) > 1:
#         L, Lswap = merge(L, Lswap)
#     if len(R) > 1:
#         R, Rswap = merge(R, Rswap)
#
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
# factors, arr = merge(factors, arr)
# print()
# print(arr)
# print(factors)


# arr = [6, 36, 42, 21, 4]
#
# factors = []
#
# for i in arr:
#     sq = int(i ** (1/2))
#     no_of_factors = 2
#     for j in range(2, sq):
#         if not i%j:
#             no_of_factors += 2
#     if not i%sq:
#         if sq**2 == i:
#             no_of_factors += 1
#         else:
#             no_of_factors += 2
#     factors.append(no_of_factors)
#
# print(arr)
# print(factors)
#
#
# def merge(arr, arrswap):
#     L = arr[:len(arr)//2]
#     Lswap = arrswap[:len(arr) // 2]
#     R = arr[len(arr) // 2:]
#     Rswap = arrswap[len(arr) // 2:]
#     if len(L) > 1:
#         L, Lswap = merge(L, Lswap)
#     if len(R) > 1:
#         R, Rswap = merge(R, Rswap)
#     a = []
#     aswap = []
#     l = 0
#     r = 0
#
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
# factors, arr = merge(factors, arr)
# print()
# print(arr)
# print(factors)


# def GCD(a, b):
#     # if not b:
#     #     return a
#     # return GCD(b, a%b)
#     while b:
#         # temp = a
#         # a = b
#         # b = temp%b
#         a, b = b, a%b
#     return a
#
#
# print(GCD(77, 121))


# n = int(input())
# t = 2*n -1
# l = 1
# inc = True
# for i in range(1, t+1):
#     for j in range(l):
#         print(j+1, end=" ")
#     print()
#     if l >= n:
#         inc = False
#     if inc:
#         l += 1
#     else:
#         l -= 1


# arr = [6, 36, 42, 21, 4]
#
# factors = []
# for i in arr:
#     sq = int(i ** (1/2))
#     no_of_factors = 2
#     for j in range(2, sq):
#         if not i%j:
#             no_of_factors += 2
#     if not i%sq:
#         if sq**2 == i:
#             no_of_factors += 1
#         else:
#             no_of_factors += 2
#     factors.append(no_of_factors)
#
# print(arr)
# print(factors, end="\n\n")
#
#
# def merge(arr, arrswap):
#     L = arr[:len(arr)//2]
#     Lswap = arrswap[:len(arr) // 2]
#     R = arr[len(arr) // 2:]
#     Rswap = arrswap[len(arr) // 2:]
#     l = 0
#     r = 0
#     a = []
#     aswap = []
#     if len(L) > 1:
#         L, Lswap = merge(L, Lswap)
#     if len(R) > 1:
#         R, Rswap = merge(R, Rswap)
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
# factors, arr = merge(factors, arr)
# print(arr)
# print(factors)


# arr = [6, 36, 42, 21, 4]
# factors = []
#
# for i in arr:
#     sq = int(i**(1/2))
#     no_of_factors = 2
#     for j in range(2, sq):
#         if not i % j:
#             no_of_factors += 2
#     if not i%sq:
#         if sq**2 == i:
#             no_of_factors += 1
#         else:
#             no_of_factors += 2
#     factors.append(no_of_factors)
#
# print(arr)
# print(factors, end = "\n\n")
#
#
# def merge(arr, arrswap):
#     L = arr[:len(arr)//2]
#     R = arr[len(arr) // 2:]
#     Lswap = arrswap[:len(arr) // 2]
#     Rswap = arrswap[len(arr) // 2:]
#
#     if len(L) > 1:
#         L, Lswap = merge(L, Lswap)
#     if len(R) > 1:
#         R, Rswap = merge(R, Rswap)
#
#     l = 0
#     r = 0
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
#         aswap.extend(Lswap[l:])
#         a.extend(L[l:])
#     elif r < len(R):
#         aswap.extend(Rswap[r:])
#         a.extend(R[r:])
#     return a, aswap
#
#
# factors, arr = merge(factors, arr)
# print(arr)
# print(factors)


# def factorial(num):
#     res = 1
#     while num:
#         res *= num
#         num -= 1
#     return res
#
#
# def comb(a, b):
#     return int(factorial(a)/(factorial(b)*factorial(a-b)))
#
#
# n = int(input("Enter the no. of rows of pascal triangle to print: "))
#
# for i in range(0, n):
#     s = ' '*(n-i)
#     print(s, end=" ")
#     for j in range(i+1):
#         print(comb(i, j), end=" ")
#     print()


# n = int(input("Enter the no. of pattern lines to print: "))
# l = 2*n - 1
# t = 1
# inc = True
#
# for i in range(l):
#     s = ' '*(n-t)
#     print(s, end=' ')
#     for j in range(t):
#         print(j+1, end=" ")
#     print()
#     if t >= 4:
#         inc = False
#     if inc:
#         t += 1
#     else:
#         t -= 1


# Hollow Half pyramid
# n = int(input("Enter no. of lines to print: "))
#
# for i in range(1, n+1):
#     print(i, end=' ')
#     if 2 <= i <= n-1:
#         s = '  '*(i - 2)
#         print(s, end='')
#         print(i, end='')
#     elif i == n:
#         for j in range(2, n+1):
#             print(j, end=' ')
#     print()


# Hollow Inverted Half pyramid
# n = int(input("Enter no. of lines to print: "))
# for i in range(n, 0, -1):
#     print(1, end=' ')
#     if i == n:
#         for j in range(2, n+1):
#             print(j, end=' ')
#     elif 2 <= i <= n-1:
#         s = '  '*(i-2)
#         print(s, end='')
#         print(i, end='')
#     print()


# Hollow Full pyramid
# n = int(input("Enter no. of lines to print: "))
# for i in range(n):
#     s = ' '*(n-i)
#     print(s, end='')
#     print(1, end=' ')
#     if 1 <= i < n-1:
#         s = '  '*(i-1)
#         print(s, end='')
#         print(i+1, end='')
#     elif i == n-1:
#         # print(' ', end='')
#         for j in range(2, n+1):
#             print(j, end=' ')
#     print()


# Hollow diamond inscribed in a rectangle
# n = int(input("Enter no. of lines to print: "))
# l = 2*n
# t = 5
# dec = True
# for i in range(l):
#     p = '*'*(t)
#     print(p, end=' ')
#     s = '  '*(n - t)
#     print(s, end='')
#     print(p, end='')
#     if dec:
#         t -= 1
#     else:
#         t += 1
#     if not t:
#         t += 1
#         dec = False
#     print()


# Butterfly Pattern
# n = int(input("Enter no. of lines to print: "))
# l = 2*n
# t = 1
# inc = True
# for i in range(l):
#     p = '*'*t
#     print(p, end='')
#     s = '  '*(n-t)
#     print(s, end='')
#     print(p, end='')
#     if inc:
#         t += 1
#     else:
#         t -=1
#     if t > n:
#         t -= 1
#         inc = False
#     print()


# Armstrong number
# def userMod(num):
#     return num - 10*(num//10)
#
#
# def power(a, b):
#     res = 1
#     for i in range(b):
#         res *= a
#     return res
#
#
# def findPower(n):
#     p = 0
#     while n:
#         p += 1
#         n = n//10
#     return p
#
#
# def checkIsArmstrong(num):
#     p = findPower(num)
#     temp = num
#     res = 0
#     while temp:
#         res += power(userMod(temp), p)
#         temp = temp//10
#     return res == num
#
#
# num = 14
#
# if checkIsArmstrong(num):
#     print(num, "is an armstrong number")
# else:
#     print(num, "is not an armstrong number")


# Check if a string is Palindrome
# s = 'malayalam'
#
#
# def checkPalindrome(s):
#     l = len(s)-1
#     for i in range(len(s)//2):
#         if s[i] != s[l-i]:
#             return False
#     return True
#
#
# if checkPalindrome(s):
#     print(s, 'is a palindrome')
# else:
#     print(s, 'is not a palindrome')


#  Sum of integers upto n
# n = int(input())
#
# def findNaturalSum(n):
#     return int(n*(n+1)/2)
#
# print('Sum of integers upto', n, ":", findNaturalSum(n) )


# Factor count sorting
# arr = [6, 36, 42, 21, 4]
# factors = []
#
# for i in arr:
#     sq = int(i ** (1/2))
#     no_of_factors = 2
#     for j in range(2, sq):
#         if not i%j:
#             no_of_factors += 2
#     if not i%sq:
#         if sq**2 == i:
#             no_of_factors +=1
#         else:
#             no_of_factors += 2
#     factors.append(no_of_factors)
#
# print(arr)
# print(factors)
#
#
# def merge(arr, arrswap):
#     L = arr[:len(arr)//2]
#     R = arr[len(arr) // 2:]
#     Lswap = arrswap[:len(arr) // 2]
#     Rswap = arrswap[len(arr) // 2:]
#     a = []
#     aswap = []
#     l = 0
#     r = 0
#     if len(L)  > 1:
#         L, Lswap = merge(L, Lswap)
#     if len(R) > 1:
#         R, Rswap = merge(R, Rswap)
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
# factors, arr = merge(factors, arr)
# print()
# print(arr)
# print(factors)


# half pyramid with number variation
# n = int(input("Enter no. of lines to print: "))
#
# for i in range(1, n+1):
#     for j in range(1, i+1):
#         print(j, end=' ')
#     print()


# Full pyramid with asterisk
# n = int(input("Enter no. of lines to print: "))
#
# for i in range(n):
#     s = '  ' * (n - i)
#     print(s, end='')
#     for j in range(i+1):
#         print('*', end='   ')
#     print()


# ***** *****
# ****   ****
# ***     ***
# **       **
# *         *
# *         *
# **       **
# ***     ***
# ****   ****
# ***** *****
# Diamond inscribed in a rectangle
n = int(input("Enter the size of diamond: "))
l = 2*n
t = n
dec = True
for i in range(l):
    p = '*'*t
    print(p, end='')
    s = '  '*(5-t)
    print(s, end='')
    print(p)
    if dec:
        t -= 1
    else:
        t += 1
    if not t:
        t += 1
        dec = False
