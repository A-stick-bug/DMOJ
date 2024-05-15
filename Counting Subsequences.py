# https://dmoj.ca/problem/dp1p4

s = "." + input()
n = len(s) - 1
MOD = 10_007

dp = [0] * (n + 2)  # dp[i]: number of distinct subsequences of s[:i]
dp[0] = 1  # empty string
prev = [-1] * 999

for i in range(1, n + 1):
    dp[i] = dp[i - 1] * 2  # 2 options, take current letter or don't take
    dp[i] -= dp[prev[ord(s[i])]]  # remove overlap
    dp[i] %= MOD
    prev[ord(s[i])] = i - 1

print((dp[n] - 1) % MOD)  # minus empty subsequence
