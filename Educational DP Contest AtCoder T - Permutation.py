# https://dmoj.ca/problem/dpt
# Sequence DP with PSA optimization
# states: [index][# of elements in remaining sequence < current]
#
# TC: O(n^2)

from itertools import accumulate


def solve():
    MOD = 10 ** 9 + 7
    n = int(input())
    s = input()

    dp = [[0] * n for _ in range(n)]

    for i in range(n):  # base case
        dp[-1][i] = 1

    for idx in reversed(range(n - 1)):
        prev_row = dp[idx + 1]
        psa = [0] + list(accumulate(prev_row))
        query = lambda l, r: psa[r + 1] - psa[l]

        for lo in range(n):
            if s[idx] == "<":  # going up
                dp[idx][lo] += query(lo, n - idx - 2)

            else:  # going down
                dp[idx][lo] += query(0, lo - 1)

            dp[idx][lo] %= MOD

    print(sum(dp[0]) % MOD)


solve()

# # reference O(n^3) brute force
# @cache
# def solve(idx, rem):
#     if idx == n - 1:  # base case
#         return 1
#
#     total = 0
#     if s[idx] == "<":  # going up
#         lo, hi = rem
#         for take in range(1, hi + 1):
#             lf = take - 1
#             rt = hi - take
#             total += solve(idx + 1, (lo + lf, rt))
#     else:  # going down
#         lo, hi = rem
#         for take in range(1, lo + 1):
#             lf = take - 1
#             rt = lo - take
#             total += solve(idx + 1, (lf, hi + rt))
#     return total
#
# total = 0
# for start in range(1, n + 1):
#     total += solve(0, (start - 1, n - start))
# print(total%MOD)
