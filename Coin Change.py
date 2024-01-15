# https://dmoj.ca/problem/cchange
# template unbounded knapsack problem

from sys import stdin

input = stdin.readline
x = int(input())
n = int(input())
coins = [int(input()) for _ in range(n)]

inf = 1 << 31
dp = [inf] * (x + 1)
dp[0] = 0  # need 0 coins to have nothing

for i in range(x+ 1):
    for coin in coins:
        if i - coin < 0:
            continue
        dp[i] = min(dp[i], dp[i-coin] + 1)

print(dp[x])
