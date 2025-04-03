# https://dmoj.ca/problem/dmopc18c4p2
# Easy version of https://dmoj.ca/problem/cco08p5 (no binary packaging)
# Knapsack subset sum problem, 1/32 optimized with bitmask/bitset

n = int(input())
arr = list(map(int, input().split()))
K = sum(arr)

dp = 1
for i in arr:
    dp |= dp << i

best = 1 << 30
dp = bin(dp)[2:]
for i in range(K // 2 + 1):
    if dp[i] == "1":
        best = min(best, K - 2 * i)
print(best)

"""
6
4 2 3 1 1 999
"""
