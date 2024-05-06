# https://dmoj.ca/problem/oly19practice18
# Interval DP
# TC: O(n^3)

s = input()
n = len(s)
inf = 301

dp = [[inf] * n for _ in range(n)]
for i in range(n):  # base cases
    dp[i][i] = 1
for i in range(n - 1):
    if (s[i] == "(" and s[i+1] == ")") or (s[i] == "[" and s[i+1] == "]"):
        dp[i][i+1] = 0

for length in range(2, n + 1):  # start filling smaller intervals firsts so we can transition properly
    for i in range(n - length + 1):
        j = i + length - 1  # [i,j] inclusive interval

        for m in range(i, j):  # standard transition from smaller intervals
            dp[i][j] = min(dp[i][j], dp[i][m] + dp[m + 1][j])

        # interval is surrounded by bracket pair: no cost
        if (s[i] == "(" and s[j] == ")") or (s[i] == "[" and s[j] == "]"):
            dp[i][j] = min(dp[i][j], dp[i + 1][j - 1])

print(dp[0][n - 1])
