# https://dmoj.ca/problem/bsspc22c1p6
# 0/1 knapsack variation, take or don't take, whichever is more optimal
# we also arrange the items in a specific order (descending order by A)

n, m = map(int, input().split())
options = [tuple(map(int, input().split())) for _ in range(n)]
options.sort(reverse=True)  # not sure why this works but all other sorted methods are WA

# dp[j]: currently considering the i-th character, already have j characters
inf = 1 << 60
dp = [inf] * (m + 1)
dp[0] = 0  # base case: 0 cost to have nothing

for a, b in options:
    for j in reversed(range(1, m + 1)):
        dp[j] = min(dp[j], dp[j - 1] + a * (j - 1) + b)  # typical knapsack

print(dp[m])
