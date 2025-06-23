# TLE IN PYTHON, CHECK C++ CODE
#
# https://dmoj.ca/problem/ddrp6
# Optimize linear DP transitions by representing them with a matrix and using matrix exponentiation
# The previous 3 moves affect what the next one can be
#
# TC: O(64^3 * log(N))

import sys


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


def encode(s):
    res = 0
    for i in range(len(s)):
        res += int(s[i]) * (4 ** i)
    return res


MOD = 10 ** 9 + 7
n = int(input())

if n < 10:  # precompute small values to avoid edge cases
    precomp = [None, 4, 16, 64, 248, 968, 3776, 14728, 57448, 224080, 874040]
    print(precomp[n])
    sys.exit()

n -= 3

states = ['000', '001', '002', '003', '010', '011', '012', '013', '020', '021', '022', '023', '030', '031', '032',
          '033', '100', '101', '102', '103', '110', '111', '112', '113', '120', '121', '122', '123', '130', '131',
          '132', '133', '200', '201', '202', '203', '210', '211', '212', '213', '220', '221', '222', '223', '230',
          '231', '232', '233', '300', '301', '302', '303', '310', '311', '312', '313', '320', '321', '322', '323',
          '330', '331', '332', '333']

mat = [[0] * 64 for _ in range(64)]
for cur in states:  # encode valid transitions in matrix
    for added in "0123":
        nxt = cur + added
        if nxt in "0123012,0321032":  # disallowed
            continue
        nxt = nxt[-3:]
        mat[encode(cur)][encode(nxt)] += 1

transition = matrix_exp(mat, n)  # transition `n` times

start = [[0] * 64 for _ in range(64)]  # apply transitions to starting state
for cur in states:
    start[encode(cur)][0] += 1
res = multiply(transition, start)

print(sum(sum(row) for row in res) % MOD)

# # Brute force DP code, O(N * large constant)
# bad = "0123012,0321032"
#
# n = int(input())
#
# ending = Counter()  # number of sequences ending with ending[i]
# ending[""] = 1
# for i in range(n):
#     state = Counter()
#     for cur in "0123":
#         for prev in ending:
#             nxt = prev + cur
#             nxt = nxt[-4:]  # only check last 4 char
#             if len(nxt) != 4 or nxt not in bad:  # valid transition
#                 nxt = nxt[-3:]  # only store last 3 chars
#                 state[nxt] += ending[prev]
#             state[nxt] %= MOD
#
#     ending = state
#
# # print(ending)
# print(sum(ending.values()) % MOD)
