# note: this problem is from a DMOJ mirror
# https://stroj.ca/problem/bobandsticks
# n <= 1000, a[i] <= 500, sum(a) <= 5000, is it possible to split into 3 sets of equal sum?
# Typical multi knapsack DP with bitmask optimization
#
# dp[index][set1 sum][set2 sum] = possible?

import sys

n = int(input())
arr = list(map(int, input().split()))

if sum(arr) % 3 != 0:
    print("No")
    sys.exit()

target = sum(arr) // 3
mask = (1 << (target + 1)) - 1

# todo: consider binary packaging

dp = [0] * (target + 1)  # dp[sum1][sum2], second state is a bitmask
dp[0] = 1  # can have nothing
for item in arr:
    new_dp = [0] * (target + 1)
    for i in range(target + 1):  # put in set 2
        new_dp[i] |= dp[i] << item
        new_dp[i] &= mask

    for i in reversed(range(item, target + 1)):  # put in set 1
        dp[i] |= dp[i - item]
        dp[i] |= new_dp[i]  # combine states

    # note that since we kept the old values, we considered putting in set 3 as well

    if dp[target] & (1 << target):  # short circuit
        print("Yes")
        sys.exit()

print("No")
