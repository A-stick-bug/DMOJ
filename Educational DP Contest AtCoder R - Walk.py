# https://dmoj.ca/problem/dpr
# Matrix exponentiation
# this should not be dynamic programming
# TC: O(N^3 * log(K))

def multiply(m2, m1):
    n = len(m1)
    m3 = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):  # j -> idx -> i
            m3[i][j] = sum(m1[idx][j] * m2[i][idx] for idx in range(n)) % MOD
    return m3


def matrix_exp(original_mat, p):
    n = len(original_mat)
    base = [row.copy() for row in original_mat]
    res = [[0] * n for _ in range(n)]  # identity matrix
    for i in range(n):
        res[i][i] = 1
    while p > 0:
        if p % 2 == 1:
            res = multiply(base, res)
        base = multiply(base, base)
        p //= 2

    return res


MOD = 10 ** 9 + 7
N, K = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(N)]

res = matrix_exp(mat, K)
print(sum(sum(row) for row in res) % MOD)
