# https://dmoj.ca/problem/tsoc16c1p6
# Extension of Edit Distance DP, operations now include: remove/insert 1, 2, or 3, replace 1
# note how the base cases are written differently from template edit distance

input()
s = input() + "."  # add common trailing character like all Edit Distance DP
t = input() + "."
n, m = len(s), len(t)

# dp[i][j] minimum cost to match up to s[i] and t[j]
# extra padding to prevent index out of bounds
dp = [[1 << 30] * (m + 3) for _ in range(n + 3)]
for i in range(1, 4):
    for j in range(1, 4):  # base cases
        dp[-i][-j] = 0

for i in reversed(range(n)):  # iterate in reverse since we are accessing dp[i+1][j+1]
    for j in reversed(range(m)):
        if s[i] == t[j]:  # same character, no cost
            dp[i][j] = dp[i + 1][j + 1]
        else:
            dp[i][j] = 1 + min(dp[i + 1][j + 1],  # replace to make characters match
                               dp[i + 1][j],  # remove 1,2,3
                               dp[i + 2][j],
                               dp[i + 3][j],
                               dp[i][j + 1],  # add 1,2,3
                               dp[i][j + 2],
                               dp[i][j + 3])

print(dp[0][0])
