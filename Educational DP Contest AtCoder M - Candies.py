"""
https://dmoj.ca/problem/dpm

Similar to knapsack DP where we find the number of ways to add to a number with constraints.
Since for each person, we can transition from many previous states, we need a data structure.

Note: Python is too slow, so we can't just use a range query data structure like Fenwick Tree to store dp states.
      Instead, we can make a PSA and rebuild it after processing every item

TC: O(NK)
"""

from itertools import accumulate

query = lambda l, r: psa[r + 1] - psa[l]
MOD = 10 ** 9 + 7

N, K = map(int, input().split())
arr = list(map(int, input().split()))

dp = [0] * (K + 1)  # dp[i]: number of ways to spend i candy
dp[0] = 1
for m in arr:
    psa = [0] + list(accumulate(dp))  # rebuild PSA

    for rem in reversed(range(K + 1)):  # similar to knapsack: reverse to prevent overlap
        dp[rem] = (dp[rem] + query(max(rem - m, 0), rem - 1)) % MOD

# print(dp)
print(dp[K])

# # brute force code, O(NK^2)
# @cache
# def solve(i, rem):
#     if i == N:  # check if distribution is valid
#         return rem == 0
#     if rem < 0:  # out of candy
#         return 0
#     total = 0
#     for take in range(min(arr[i], rem) + 1):
#         total += solve(i + 1, rem - take)
#     return total
#
#
# print(solve(0, K))
