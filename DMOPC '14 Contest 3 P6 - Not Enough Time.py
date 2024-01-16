# https://dmoj.ca/problem/dmopc14c3p6
# Template knapsack DP with extra options other than take/don't take

import sys

input = sys.stdin.readline
N, T = map(int, input().split())

dp = [0] * (T + 1)  # template 0/1 knapsack but we are given more options than take/don't take
for _ in range(N):
    vals = list(map(int, input().split()))
    for t in reversed(range(T + 1)):
        for i in range(0, 6, 2):  # consider bad, average, and good
            cost, value = vals[i], vals[i + 1]
            if t - cost >= 0:
                dp[t] = max(dp[t], dp[t - cost] + value)

print(dp[T])
