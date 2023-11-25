# unlimited knapsack problem with restrictions on what item you take

N, C = map(int, input().split())
dp = [[[0] * 2 for _ in range(C + 1)] for _ in range(2)]

prev = 0
cur = 1
for i in range(1, N + 1):
    a, b, c, d = map(int, input().split())
    for j in range(1, C + 1):
        dp[cur][j][0] = dp[cur][j][1] = max(dp[prev][j][0], dp[prev][j][1])
        if j >= a:
            dp[cur][j][0] = max(dp[cur][j][0], dp[cur][j - a][1] + b)  # previous one is diff type
        if j >= c:
            dp[cur][j][1] = max(dp[cur][j][1], dp[cur][j - c][0] + d)
    prev, cur = cur, prev

print(max(dp[prev][C]))
