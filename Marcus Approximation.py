# https://dmoj.ca/problem/approximation
# Approximate a function with a polynomial
# First find the degree using a log-log plot, then estimate coefficients using a regression

def exact(h):  # the function that we are trying to approximate
    t = 0
    for a in range(1, h):  # try all values of `a`, binary search for maximum `b`
        low = 0
        high = h - 1
        ans = 0
        while low <= high:
            mid = (low + high) // 2
            if a ** 2 + mid ** 2 <= h ** 2:
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        t += ans

    return t


def approximate(h):
    a = 0.7853981797520097  # computed with the code below
    b = -1.0036577767145425
    c = -35.63998603820801
    return a * h ** 2 + b * h + c


for _ in range(int(input())):
    h = int(input())
    if h < 10 ** 5:
        print(exact(h))
    else:
        print(approximate(h))

# from math import log
# import matplotlib.pyplot as plt
#
# # the following log-log plot shows a line, thus we have a power function
# mn = 100_000
# idx = []
# res = []
# for t in range(2, mn, 10000):
#     idx.append(log(t))
#     res.append(log(exact(t)))
#     print(t)
# plt.plot(idx, res)
# plt.show()
#
# # slope in log-log plot is the power
# p1 = (log(10 ** 5), log(exact(10 ** 5)))
# p2 = (log(10 ** 6), log(exact(10 ** 6)))
# print((p2[1] - p1[1]) / (p2[0] - p1[0]))  # 2.000004991 -> probably a quadratic
#
#
# # try fitting a quadratic through some points
# # note: probably should've added regularization
# from sklearn import linear_model
# model = linear_model.LinearRegression()
# X = []
# Y = []
# for i in range(0, 10**5, 200):
#   t = exact(i)
#   X.append([i, i**2])
#   Y.append(t)
# model.fit(X, Y)
#
# print("Coefficients:", model.coef_.tolist())
# print("Intercept:", model.intercept_)
