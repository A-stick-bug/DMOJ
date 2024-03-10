# https://dmoj.ca/problem/dmopc13c3p5
# 2D template knapsack DP

MT, MU, N = map(int, input().split())
dp = [[0] * (MU + 1) for _ in range(MT + 1)]

for _ in range(N):
    val, t, u = map(int, input().split())
    for i in reversed(range(t, MT + 1)):
        for j in reversed(range(u, MU + 1)):
            dp[i][j] = max(dp[i][j], dp[i - t][j - u] + val)

print(dp[-1][-1])
