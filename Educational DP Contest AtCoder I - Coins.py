"""
https://dmoj.ca/problem/dpi
Probability DP
Need iterative (bottom-up) or else TLE
"""


def solve():
    n = int(input())
    coins = list(map(float, input().split()))  # heads: p, tails: 1-p
    max_tails = n // 2  # to have more heads than tails, we can have at most this many tails

    dp = [0] * (max_tails + 1)  # dp[j] is probability of having j tails after flipping the current coin
    dp[0] = 1  # default is 0 tails since no coins have been flipped

    for p in coins:
        for j in reversed(range(1, max_tails + 1)):  # iterate in reverse to prevent overlap (similar to knapsack)
            dp[j] = dp[j - 1] * (1 - p) + dp[j] * p
        dp[0] *= p  # to stay at 0 tails, it must land on a head

    print(sum(dp))


solve()
