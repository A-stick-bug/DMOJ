# https://dmoj.ca/problem/mathp5
# Combinatorics solution: consider each possible sequence length independently

### MODULAR ARITHMETIC TEMPLATE START ###
MOD = 10 ** 9 + 7
MN = 10 ** 6 + 1

factorial = [1] * MN  # precompute factorials
for i in range(2, MN):
    factorial[i] = (factorial[i - 1] * i) % MOD

invfact = [1] * MN  # precompute mod inverse of factorials (for comb)
invfact[MN - 1] = pow(factorial[MN - 1], MOD - 2, MOD)
for i in range(MN - 1, 0, -1):
    invfact[i - 1] = (invfact[i] * i) % MOD

comb = lambda n, k: factorial[n] * invfact[k] * invfact[n - k] if n >= k >= 0 else 0  # N choose K
### MODULAR ARITHMETIC TEMPLATE END ###


n = int(input())

total = 0
for take in range(1, n + 1):
    objects = n - take + 1

    total += comb(objects - take + 1, take)
    total %= MOD

print(total)

"""
1
2
3
5
8
12
18
27
40
"""

# # observation based solution
# MOD = 10 ** 9 + 7
# n = int(input())
#
# if n < 3:
#     print([-1, 1, 2][n])
# else:
#     dp = [0] * (n + 1)
#     dp[0] = 0
#     dp[1] = 1
#     dp[2] = 1
#     for i in range(3, n + 1):
#         dp[i] = (dp[i - 1] + dp[i - 3]) % MOD
#
#     print(sum(dp) % MOD)
