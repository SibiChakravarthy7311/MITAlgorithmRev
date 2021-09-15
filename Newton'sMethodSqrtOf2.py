x = 1
xi = -1
temp = 1
a = 2


def y(x, a):
    return x**2 - a


while y(xi, a) and x-xi:
    temp = xi
    xi = (xi + a/xi)/2
    x = temp
    print("x =", x)
print(x**2)
# y = f(xi) + f'(xi).(x-xi)
#
# xi + 1 = xi - (f(xi) / f'(xi))
#
# if f(x) = x ^ 2 - a,
# xi+1 = xi - ((xi ^ 2 - a) / 2 * xi)
# xi+1 = (xi ^ 2 + a) / 2 * xi
# xi+1 = (xi + a / xi) / 2
# If a is 2, then sqrt of 2 can be approximated

