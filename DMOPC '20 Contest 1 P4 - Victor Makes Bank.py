# TLE, CHECK C++ CODE
# https://dmoj.ca/problem/dmopc20c1p4
# TC: O(T^3 * logN)

def multiply(m2, m1):
    n = len(m1)
    m3 = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):  # j -> idx -> i
            m3[i][j] = sum([m1[idx][j] * m2[i][idx] for idx in range(n)]) % MOD
    return m3


def matrix_exp(original_mat, p):
    base = [row.copy() for row in original_mat]
    res = [[0] * (T + 1) for _ in range(T + 1)]  # identity matrix
    for i in range(T + 1):
        res[i][i] = 1
    while p > 0:
        if p % 2 == 0:
            base = multiply(base, base)
            p //= 2
        else:
            res = multiply(base, res)
            p -= 1
    return res


MOD = 10 ** 9 + 7
N, mul, T, C = map(int, input().split())

A = [[0] * (T + 1) for _ in range(T + 1)]
for i in range(1, T + 1):
    A[i][i - 1] = 1
A[0][T] = mul
A[T][T] = 1

A_n = matrix_exp(A, N - 1)

big = A_n[T][T] * C
small = sum(A_n[i][T] for i in range(T)) * C

print((2 * big + small) % MOD)
