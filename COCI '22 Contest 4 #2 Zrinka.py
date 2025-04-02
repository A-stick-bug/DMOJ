# https://dmoj.ca/problem/coci22c4p2
# Dynamic programming
# dp[index in a1][index in a2] = minimum possible max value
# Note this code uses Python negative indexing to automatically avoid index errors

n, *a1 = map(int, input().split())
m, *a2 = map(int, input().split())
a1.insert(0, -1)  # 1-indexed
a2.insert(0, -1)

inf = 1 << 30
dp = [[inf] * (m + 1) for _ in range(n + 1)]
dp[0][0] = 0  # ensures all transitions result in a positive integer

for i in range(n + 1):
    for j in range(m + 1):
        # transition with a1
        # extra cost of 1 if the parity of the previous max is the same
        dp[i][j] = min(dp[i][j], dp[i - 1][j] + 1 + (a1[i] % 2 == dp[i - 1][j] % 2))

        # transition with a2
        dp[i][j] = min(dp[i][j], dp[i][j - 1] + 1 + (a2[j] % 2 == dp[i][j - 1] % 2))

print(dp[n][m])
