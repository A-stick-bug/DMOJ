# https://dmoj.ca/problem/dpx
# Knapsack DP, build tower top to bottom
#
# First use an exchange argument to order the blocks:
# - there always exists an optimal solution where the blocks are stacked in
#   order of w+s (from top to bottom)
# - if we had an optimal solution that doesn't follow this order, we can use a
#   series of swapping adjacent blocks while still satisfying the strength condition
#   until it does satisfy the order
#
# - within the same w+s group, any adjacent swaps keeps the structure valid
#   so any arbitrary order there is fine (since there will exist an optimal
#   solution with that order)
#
# Once we finish the ordering, the state is dp[w] = max value using a weight of w
# Transition from dp[prev_w]+v -> dp[w] if prev_w <= s (i.e. new block can fully
# support the existing structure when we put it at the bottom)

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

arr.sort(key=lambda x: (x[0] + x[1], x[0] - x[1]))

MS = 20_001
dp = [0] * MS  # dp[w] = max value with sum of weight = w

for w, s, val in arr:
    # transition from weights <= s
    for w_idx in reversed(range(MS)):
        prev_w = w_idx - w
        if 0 <= prev_w <= s:
            dp[w_idx] = max(dp[w_idx], dp[prev_w] + val)
print(max(dp))
