"""
https://dmoj.ca/problem/sac22cc5p4
Q: given N intervals and Q queries, for each query [l, r], check if everything in [l,r] is covered by the N intervals
A: Merge all intervals, binary search the position for each query and check if it is fully covered by a interval

Note: we can also use difference array + coordinate compression and PSA, but that's more work
"""

import sys
from bisect import bisect_right


def merge_all(intervals, sorted=False):
    if not intervals:
        return []
    if not sorted:
        intervals.sort()
    res = [intervals[0]]
    for l, r in intervals[1:]:
        if res[-1][1] >= l - 1:  # left overlaps with right, we can combine
            res[-1] = (res[-1][0], max(res[-1][1], r))
        else:  # disjoint intervals
            res.append((l, r))
    return res


input = sys.stdin.readline
print = lambda x: sys.stdout.write(x + "\n")
inf = 1 << 30

N, Q = map(int, input().split())
intervals = merge_all([tuple(map(int, input().split())) for _ in range(N)])

for _ in range(Q):
    l, r = map(int, input().split())
    pos = bisect_right(intervals, (l, inf)) - 1  # position of interval

    if intervals[pos][0] <= l and r <= intervals[pos][1]:  # fully covered
        print('Y')
    else:
        print('N')
