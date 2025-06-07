# https://dmoj.ca/problem/fibonacci2
# Fast computation of the n-th fibonacci number, fib(n), specifically mod 1e9+7
# Matrix exponentiation + observing cycles
#
# Note: apparently observing cycles is well known in math: https://en.wikipedia.org/wiki/Pisano_period
#
# TC: O(log(n)), dominated by input reading and modding (not matrix exponentiation)

import sys

sys.set_int_max_str_digits(0)  # allows for reading large integers from input
MOD = 10 ** 9 + 7


def multiply(m2, m1):
    n = len(m1)
    m3 = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):  # j -> idx -> i
            m3[i][j] = sum([m1[idx][j] * m2[i][idx] for idx in range(n)]) % MOD
    return m3


def matrix_exp(original_mat, p):
    base = [row.copy() for row in original_mat]
    res = [[1, 0], [0, 1]]  # identity matrix
    while p > 0:
        if p % 2 == 0:
            base = multiply(base, base)
            p //= 2
        else:
            res = multiply(base, res)
            p -= 1
    return res


n = int(input()) % 2000000016
A = [[0, 1], [1, 1]]

res = matrix_exp(A, n + 1)  # 1-index
print(res[0][0])

"""
# Observing the cycles, here is my thought process:
# - there are only 4 cells, and 2 of them represent the same thing, so we have at most mx:=(1e9+7)^3 matrices
# - thus, we must have some cycle after at most mx times due to the pigeonhole principle
# - the cycle length is probably around some multiple or power of our mod value so we search around those

A = [[0, 1], [1, 1]]
MOD = 10 ** 9 + 7

# general area to search around, try a bunch of different areas
search = MOD * 2
for n in range(search - 1000, search + 1000):
    if matrix_exp(A, n + 1) == A:  # cycle found
        print("cycle repeats every", n)
        break
"""
