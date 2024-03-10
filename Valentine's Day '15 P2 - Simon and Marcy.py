# https://dmoj.ca/problem/valday15p2
# reading comprehension + template knapsack dp

N, M = map(int, input().split())
dp = [0] * (M + 1)

for _ in range(N):
    val, weight = map(int, input().split())
    for i in reversed(range(weight, M + 1)):
        dp[i] = max(dp[i], dp[i - weight] + val)

print(dp[-1])
