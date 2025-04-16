# https://dmoj.ca/problem/dmopc16c1p3
# Standard sequence DP

inf = 1 << 30

n = int(input())
arr = [inf] + list(map(int, input().split()))

dp = [0.0] * (n + 1)
dp[0] = 0
for i in range(1, n + 1):
    dp[i] = dp[i - 1] + arr[i]
    if i > 1:  # group of 2
        dp[i] = min(dp[i], dp[i - 2] + max(arr[i], arr[i - 1]) + 0.5 * min(arr[i], arr[i - 1]))
    if i > 2:  # group of 3
        dp[i] = min(dp[i], dp[i - 3] + sum(arr[i - 2:i + 1]) - min(arr[i - 2:i + 1]))

print(f"{dp[n]:.1f}")  # 1 decimal place, with trailing 0 if needed
