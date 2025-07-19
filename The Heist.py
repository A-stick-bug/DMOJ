# https://dmoj.ca/problem/heist
# Circular house robber DP, extension of https://leetcode.com/problems/house-robber-ii
# states: dp[idx][# of consecutive taken] = max money
#
# Try K+1 indices as split points since at least one of them is guaranteed to be off in the optimal solution
# due to the pigeonhole principle (can't have K+1 consecutive all on)
# After splitting, do regular linear house robber since the first won't affect the last
#
# TC: O(N * K^2)

def solve():
    def solve_linear(N, K, arr):  # non circular
        prev = [0] * (K + 1)
        for i in range(len(arr)):
            dp = [0] * (K + 1)
            dp[0] = max(prev)
            for taken in range(1, K + 1):
                dp[taken] = prev[taken - 1] + arr[i]
            prev = dp
        return max(prev)

    N, K = map(int, input().split())

    arr = list(map(int, input().split())) * 2
    arr = [max(0, i) for i in arr]

    if N == K:
        print(sum(arr) // 2)  # edge case: take all
        return

    best = 0
    for i in range(K + 1):  # at least 1 in these that is off
        sub = arr[i:i + N - 1]
        best = max(best, solve_linear(N, K, sub))
    print(best)


t = int(input())
for _ in range(t):
    solve()
