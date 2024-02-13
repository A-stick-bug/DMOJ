# https://dmoj.ca/problem/dpo
# bitmask DP

MOD = 10 ** 9 + 7
n = int(input())
match = [list(map(int, input().split())) for _ in range(n)]
states = 1 << n

dp = [0] * states
dp[0] = 1  # no pairs at the start

for s in range(states):
    for w in range(n):
        if not s & (1 << w) and match[bin(s).count("1")][w]:
            dp[s | (1 << w)] = (dp[s] + dp[s | (1 << w)]) % MOD

print(dp[-1])  # get state for all bits set to 1 (all pairs matched)
