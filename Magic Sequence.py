# https://dmoj.ca/problem/magicseq
# find the number of subsequences that satisfy certain conditions
# bitwise go brrr
# note: the array is 1-indexed

n = int(input())

dp = [0] * (n + 1)
dp[0] = 1  # base case: 1 way to have nothing

for i in range(1, n + 1):
    for j in range((i & 1) ^ 1, i, 2):  # build current sequence from previous ones, previous must be different parity
        dp[i] += dp[j]

print(sum(dp) - 1)
