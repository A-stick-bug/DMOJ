# https://dmoj.ca/problem/dmopc16c3p3
# Knapsack DP
# States: [index][ghosts killed] = max magic left
#
# TC: O(n^2)
# yes, putting it in a solve() actually increases the code speed, this is especially significant in DP problems

import sys


def solve():
    input = sys.stdin.readline
    n, m = map(int, input().split())

    dp = [-1] * (n + 1)
    dp[0] = m
    for _ in range(n):
        cost, val = map(int, input().split())
        for i in reversed(range(1, n + 1)):
            if cost <= dp[i - 1]:
                dp[i] = max(dp[i], dp[i - 1] + val - cost)

    # print(dp)

    for i in reversed(range(n + 1)):
        if dp[i] != -1:
            print(i, dp[i])
            break


solve()
