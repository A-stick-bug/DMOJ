# https://dmoj.ca/problem/dmopc15c2p4
# Weighted task scheduling DP
#
# dp[i]: max happiness obtainable at the i-th anime's end time
# note that dp[i] is technically a prefix max array
# this way, we can just binary search to get the state to transition from

import sys
from bisect import bisect_left

input = sys.stdin.readline
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    arr[i][1] += arr[i][0] - 1
arr.sort(key=lambda x: x[1])  # sort by end, [l,r] intervals

dp = [0] * n
for i, (l, r, happy) in enumerate(arr):
    # find latest state to transition from
    left = bisect_left(arr, l, key=lambda x: x[1]) - 1
    if left < 0:
        dp[i] = max(dp[i - 1], happy)
    else:
        dp[i] = max(dp[i - 1], dp[left] + happy)

# print(arr)
# print(dp)
print(dp[-1])
