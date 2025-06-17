# https://dmoj.ca/problem/coi10p3
# Merging intervals and observation

import sys

input = sys.stdin.readline


def merge_all(intervals, sorted=False):
    if not intervals:
        return []
    if not sorted:
        intervals.sort()
    res = [intervals[0]]
    for l, r in intervals[1:]:
        if res[-1][1] >= l:
            res[-1] = (res[-1][0], max(res[-1][1], r))
        else:  # disjoint intervals
            res.append((l, r))
    return res


n, m = map(int, input().split())
arr = []
for _ in range(n):
    l, r = map(int, input().split())
    if l > r:
        arr.append((r, l))

total = m
for l, r in merge_all(arr):
    total += 2 * (r - l)
print(total)
