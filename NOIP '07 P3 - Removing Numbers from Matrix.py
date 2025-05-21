# https://dmoj.ca/problem/noip07p3
# Interval DP on `t` independent rows, sum the answers
# dp[l][r] = maximum score achievable without taking anything in [l,r]
# Key observation: you can figure out the power of 2 multiplier given your current available range
#
# TC: O(t * n^2)

t, n = map(int, input().split())

total = 0
for case in range(t):
    arr = list(map(int, input().split()))

    dp = [[0] * n for _ in range(n)]
    dp[0][n - 1] = 0  # base case: everything still there

    for le in reversed(range(1, n)):
        for l in range(n - le + 1):
            r = l + le - 1

            move = n - (r - l + 1)
            multiplier = 2 ** move
            if l != 0:  # taken from left
                dp[l][r] = max(dp[l][r], dp[l - 1][r] + arr[l - 1] * multiplier)
            if r != n - 1:
                dp[l][r] = max(dp[l][r], dp[l][r + 1] + arr[r + 1] * multiplier)

    best = 0
    for i in range(n):
        multiplier = 2 ** n
        best = max(best, dp[i][i] + arr[i] * multiplier)

    total += best

print(total)
