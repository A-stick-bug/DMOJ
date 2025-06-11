# https://dmoj.ca/problem/mathp4
# Calculus practice problem
# Due to symmetry, we print out the x values instead of y and only use a semicircle

from math import pi, sqrt, asin

eps = 1e-11


def f(x):  # semicircle
    return sqrt(1 - x * x)


def F(x):  # integral of f(x)
    return 0.5 * (x * sqrt(1 - x * x) + asin(x))


n = int(input())
each = pi / n / 2

for i in range(1, n):
    area = i * each

    # find x where F(x) = area
    # Newton's method
    x = 0.0  # initial guess
    for _ in range(100):
        fx = (F(x) - F(-1)) - area
        dfx = f(x)
        if abs(fx) < eps:
            print(x)
            break
        x -= fx / dfx

    # # binary search approach
    # low = -1
    # high = 1
    # while low < high:
    #     mid = (low + high) / 2d
    #     cur = F(mid) - F(-1)
    #     if area - eps < cur < area + eps:
    #         print(mid)
    #         break
    #     if cur < area:
    #         low = mid
    #     else:
    #         high = mid
