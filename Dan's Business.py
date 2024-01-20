# https://dmoj.ca/problem/oly21practice27
# find first order that cannot be served, if you cant serve everything up to i, you can't serve anything above i
# therefore, we can use binary search
# note: difference arrays can be used for the range updates, then check if anything is less than 0
#
# seg tree probably works too, but I'm afraid the constant factor might be too high for python

import sys
from itertools import accumulate

input = sys.stdin.readline
N, M = map(int, input().split())
arr = list(map(int, input().split()))
queries = [list(map(int, input().split())) for _ in range(M)]


def works(amt):
    """check if we can serve amt orders"""
    diff = [0] * (N + 1)
    for val, l, r in queries[:amt]:
        diff[l - 1] -= val  # convert to 0-indexing
        diff[r] += val
    diff = list(accumulate(diff))
    return all(diff[i] + arr[i] >= 0 for i in range(N))


# template binary search
low = 0
high = N
while low <= high:
    mid = low + (high - low) // 2
    if works(mid):
        low = mid + 1
    else:
        high = mid - 1

if low > N:  # can order all
    print(0)
else:
    print(-1)
    print(low)
