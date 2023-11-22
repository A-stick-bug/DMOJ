"""
https://dmoj.ca/problem/dph
Q: Number of ways to get from top left to bottom right corner, with obstacles and only moving down and right
Template grid dp problem
Number of ways to get to current = ways to get to cell above current + ways to get to cells left of current
"""

ROWS, COLS = map(int, input().split())
grid = [list(input()) for _ in range(ROWS)]

dp = [[0] * COLS for _ in range(ROWS)]
for i in range(ROWS):  # base case: top row
    if grid[i][0] == "#":
        break
    dp[i][0] = 1
for j in range(COLS):  # base case: left column
    if grid[0][j] == "#":
        break
    dp[0][j] = 1

for i in range(1, ROWS):
    for j in range(1, COLS):
        if grid[i][j] == "#":
            dp[i][j] = 0
        else:
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

print(dp[-1][-1] % 1_000_000_007)
