# https://dmoj.ca/problem/dmopc14c5p4
# Classic knapsack with all values = 1 or 2
# We can use greedy instead, using sorting, PSA, and binary search

import sys
from itertools import accumulate
from bisect import bisect_left, bisect_right

input = sys.stdin.readline
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
ones = [cost for cost, val in arr if val == 1]
twos = [cost for cost, val in arr if val == 2]
ones.sort()  # consider the smallest ones first
twos.sort()

psa_one = [0] + list(accumulate(ones))
psa_two = [0] + list(accumulate(twos))

# try taking i from `ones` and as many as possible from `twos`
best = 0
for i in range(len(psa_one)):
    if psa_one[i] > M:  # doesn't fit
        break
    j = bisect_right(psa_two, M - psa_one[i]) - 1  # take as many as possible
    best = max(best, i + 2 * j)
print(best)
