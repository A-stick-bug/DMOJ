import sys

input = sys.stdin.readline
n = int(input())
arr = [0, 0] + [int(input()) for _ in range(n)]

dp = [0] * (n + 2)
for i in range(2, n + 2):
    dp[i] = max(dp[i - 1], arr[i] + dp[i - 2])
print(dp[-1])
