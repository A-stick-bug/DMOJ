# https://dmoj.ca/problem/dmopc15c4p4
# Classic problem, range sum query and range frequency query
# RSQ: use psa
# RFQ: store indices of occurrences of each element and use binary search
#   - alternate sol: use sqrt decomp for RFQ
#
# TC: O(Q*log(N))

import sys
from itertools import accumulate
from collections import defaultdict
from bisect import bisect_right, bisect_left

input = sys.stdin.readline
N, K, Q = map(int, input().split())
arr = list(map(int, input().split()))

psa = [0] + list(accumulate(arr))
locs = defaultdict(list)  # locs[x] contains all indices where x appears
for i in range(N):
    locs[arr[i]].append(i + 1)


def range_freq_query(x, l, r):
    """count how many times x appears in [l,r], 1-indexed"""
    if x not in locs:
        return 0
    return bisect_right(locs[x], r) - bisect_left(locs[x], l)


for _ in range(Q):
    a, b, l, r = map(int, input().split())
    if psa[r] - psa[l - 1] > K and range_freq_query(a, l, r) and range_freq_query(b, l, r):
        print("Yes")
    else:
        print("No")
