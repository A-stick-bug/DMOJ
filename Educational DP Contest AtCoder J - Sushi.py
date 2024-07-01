# https://dmoj.ca/problem/dpj
# All plates with X sushi are equivalent, we can group them together
# Used a lot of guessing...

import sys

sys.setrecursionlimit(200000)
n = int(input())
arr = list(map(int, input().split()))
dp = [-1] * 27000001


def solve(one, two, three):
    if one == two == three == 0:  # base case: finished
        return 0
    s = one * 90000 + two * 300 + three
    if dp[s] != -1:
        return dp[s]

    total = 0
    t = one + two + three
    if one != 0:
        total += (solve(one - 1, two, three) + n / t) * one / t
    if two != 0:
        total += (solve(one + 1, two - 1, three) + n / t) * two / t
    if three != 0:
        total += (solve(one, two + 1, three - 1) + n / t) * three / t

    dp[s] = total
    return dp[s]


print(solve(arr.count(1), arr.count(2), arr.count(3)))
