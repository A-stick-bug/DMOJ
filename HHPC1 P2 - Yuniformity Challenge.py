# https://dmoj.ca/problem/hhpc1p2
# O(1) queries
# YES if:
# - all the same (static freq query)
# - there is 0  (static freq query)
# - we can make a 0 using positive-negative pair (dict + prefix max)


import sys
from collections import defaultdict
from bisect import bisect_left, bisect_right

input = sys.stdin.readline
print = sys.stdout.write

N, Q = map(int, input().split())
arr = list(map(int, input().split()))

# precompute static freq queries
freq = defaultdict(list)
for i, v in enumerate(arr):
    freq[v].append(i)
cnt = lambda x, l, r: bisect_right(freq[x], r) - bisect_left(freq[x], l)

# store the latest possible negative before the current
loc = {}
prev = [-1] * N
for i, v in enumerate(arr):
    if -v in loc:
        prev[i] = loc[-v]
    loc[v] = i

# get the prefix maximum at each index
m = -1
pma = [-1] * N
for i in range(N):
    pma[i] = max(pma[i - 1], prev[i])

# answer queries
for _ in range(Q):
    l, r = map(lambda x: int(x) - 1, input().split())

    if cnt(0, l, r) > 0 or (r - l + 1) == cnt(arr[l], l, r) or (pma[r] != -1 and l <= pma[r]):
        print("YES" + "\n")
    else:
        print("NO" + "\n")
