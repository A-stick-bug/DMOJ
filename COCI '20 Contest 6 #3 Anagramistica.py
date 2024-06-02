"""
https://dmoj.ca/problem/coci20c6p3
Knapsack DP with math (combinatorics and modular arithmetic)
1. For each anagram group, get its frequency, (aab, aba, baa) -> anagram group of size 3
2. For each anagram group we treat it as 1 knapsack item with X possible transitions
   where X is the group size (since we can select X items from this group)
3. Now just run classic 'number of ways' knapsack with this alternate transition

TC: O(NK)
- for each anagram group, its number of transitions is equal to its size
- therefore, we have N transitions total, times K since you're doing it for every state

Note: N is small, so you can also just use Pascal's triangle for the combinations
"""

import sys
from collections import defaultdict

input = sys.stdin.readline

### MODULAR ARITHMETIC TEMPLATE START ###
MOD = 10 ** 9 + 7
MN = 2001

factorial = [1] * MN  # precompute factorials
for i in range(2, MN):
    factorial[i] = (factorial[i - 1] * i) % MOD

mod_div = lambda p, r: (p * pow(r, MOD - 2, MOD)) % MOD
comb = lambda n, k: mod_div(factorial[n], (factorial[k] * factorial[n - k])) if n >= k else 0  # N choose K
### MODULAR ARITHMETIC TEMPLATE END ###

N, K = map(int, input().split())
freq = defaultdict(int)  # anagram frequencies
for _ in range(N):
    freq["".join(sorted(input()))] += 1

dp = [0] * (K + 1)  # number of ways to get i anagrams
dp[0] = 1
for cnt in freq.values():
    for state in reversed(range(K + 1)):  # fill in reverse to prevent state overlap
        # multiple transitions for each 'knapsack item'
        # we can use any number from [1, group size] items from this anagram group
        for items in range(1, cnt + 1):
            anagrams = comb(items, 2)  # using this many items, we get this many anagram pairs
            ways = comb(cnt, items)  # there are this many ways of selecting these items
            if state - anagrams < 0:  # invalid transition
                break
            dp[state] = (dp[state] + dp[state - anagrams] * ways) % MOD

print(dp[K])
