# template knapsack DP
# constraints are so low you can probably just brute force

H = int(input())
n = int(input())
arr = [int(input()) for _ in range(n)]

dp = [1 << 30] * (H + 1)
dp[0] = 0
for amt in arr:
    for i in reversed(range(amt, H + 1)):
        dp[i] = min(dp[i], dp[i - amt] + 1)

if dp[H] != 1 << 30:
    print(dp[H])
else:
    print(0)
