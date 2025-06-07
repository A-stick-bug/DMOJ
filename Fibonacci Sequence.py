# https://dmoj.ca/problem/fibonacci
# Fast computation of the n-th fibonacci number, fib(n)
# Matrix exponentiation
#
# TC: O(log(n))

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


n = int(input())
A = [[0, 1], [1, 1]]

res = matrix_exp(A, n + 1)  # 1-index
print(res[0][0])
