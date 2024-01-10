# template coin change problem (knapsack DP)

pow2 = [1 << i for i in range(21)]
MOD = 10 ** 9 + 7

n = int(input())

dp = [0 for i in range(n + 1)]
dp[0] = 1

for p in pow2:  # note: we count combinations so reverse the order of the loops
    for i in range(n + 1):
        if i - p < 0:
            continue
        dp[i] += dp[i - p] % MOD

print(dp[-1] % MOD)
