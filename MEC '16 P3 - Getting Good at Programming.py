"""
https://dmoj.ca/problem/mec16p3
slightly harder version of https://leetcode.com/problems/maximum-value-of-k-coins-from-piles

2D knapsack dp, using bottom up tabulation
Instead of choosing/not choosing an item, we can choose multiple variations of the item
States: dp[time remaining]
note: make sure you know what to loop forwards/reversed to prevent incorrect state transitions
      remember than this is like bounded knapsack DP

TC: O(LNT), ~O(N^3)
"""

from itertools import accumulate

N, T = map(int, input().split())
dp = [0] * (T + 1)

for _ in range(N):
    levels = list(map(int, input().split()))[1:]
    times = []
    gains = []
    for i in range(0, len(levels), 2):
        times.append(levels[i])
        gains.append(levels[i + 1])
    times = [0] + list(accumulate(times))  # make a psa, since the stuff we take must be in [0, x]
    gains = [0] + list(accumulate(gains))

    for t in reversed(range(T + 1)):
        for i in range(len(times)):  # many choices, transition from the states with larger t first
            if t - times[i] < 0:
                break
            dp[t] = max(dp[t], dp[t - times[i]] + gains[i])

print(dp[-1])
