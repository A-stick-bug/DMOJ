# https://dmoj.ca/problem/dpw
# TLE in Python, see equivalent C++ version
#
# Sequence DP, with line sweep and lazy seg tree to help with transitions
# - Let dp[i] be the optimal answer with the last `1` at index i
# - Transition j -> i, value is dp[j] + sum of intervals that start after j and cover i, since those are the new intervals we take
# - The seg tree stores the cost of all transitions, and we can query for the max
# - At index i, we first update seg to add the intervals that start after all previous indices and cover i
# - We also remove the contribution of intervals that no longer cover i

import sys
from math import log2, ceil

input = sys.stdin.readline


class LazySegTree:  # update by difference
    def __init__(self, arr, f=lambda x, y: x + y, default=0) -> None:
        """create 1-indexed segment tree from 0-indexed array"""
        self.f = f  # function used to combine segments
        self.default = default
        layers = ceil(log2(N))  # max depth of the seg tree, root has depth 0
        self.size = 1 << layers
        self.seg = [default] * (2 * self.size)  # 1-indexed, need an extra layer for the actual data
        self.lazy = [0] * (2 * self.size)

        for i in range(N):  # base layer
            self.seg[self.size + i] = arr[i]
        for i in reversed(range(1, self.size)):  # create other layers from base
            self.seg[i] = f(self.seg[i * 2], self.seg[i * 2 + 1])

    def push_down(self, i, segment_size):
        """transfer lazy tag from parent to children"""
        if self.lazy[i] == 0:
            return
        self.lazy[i * 2] += self.lazy[i]  # transfer lazy tags
        self.lazy[i * 2 + 1] += self.lazy[i]
        self.seg[i * 2] += self.lazy[i]
        self.seg[i * 2 + 1] += self.lazy[i]
        self.lazy[i] = 0

    def update(self, i, l, r, cur_l, cur_r, diff) -> None:
        """add diff to [left, right]"""
        if cur_r < l or r < cur_l:  # fully outside segment
            return
        mid = (cur_l + cur_r) // 2
        if l <= cur_l and cur_r <= r:  # fully inside segment: update lazily
            self.lazy[i] += diff
            self.seg[i] += diff
            return
        self.push_down(i, cur_r - mid)  # partial covers, recurse deeper
        self.update(i * 2, l, r, cur_l, mid, diff)
        self.update(i * 2 + 1, l, r, mid + 1, cur_r, diff)
        self.seg[i] = self.f(self.seg[i * 2], self.seg[i * 2 + 1])

    def query(self, i, l, r, cur_l, cur_r) -> int:
        """query [left, right]"""
        if cur_r < l or r < cur_l:  # fully outside segment
            return self.default
        if l <= cur_l and cur_r <= r:  # fully inside segment
            return self.seg[i]

        mid = (cur_l + cur_r) // 2  # traverse down further
        self.push_down(i, cur_r - mid)
        return self.f(self.query(i * 2, l, r, cur_l, mid),
                      self.query(i * 2 + 1, l, r, mid + 1, cur_r))

    def query_range(self, l, r):
        return self.query(1, l, r, 0, self.size - 1)

    def update_range(self, l, r, diff):
        return self.update(1, l, r, 0, self.size - 1, diff)


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)]

# line sweep
events = []
for l, r, amt in arr:
    events.append((l, amt))
    events.append((r + 1, -amt, l))  # need to keep track of the start
events.sort(key=lambda x: x[0])

dp = [0] * (N + 1)

# seg[i] stores dp[i] + sum of intervals satisfying (starts after i) AND (covers j, i.e. ends >=j)
seg = LazySegTree([0] * (N + 1), f=max, default=-(1 << 60))

idx = 0  # sweep index
for i in range(1, N + 1):
    while idx < len(events) and events[idx][0] <= i:  # interval with either endpoint at i
        amt = events[idx][1]
        if len(events[idx]) == 2:  # start of interval
            seg.update_range(0, i - 1, amt)
        else:  # end of interval
            left = events[idx][2]  # start of this interval
            seg.update_range(0, left - 1, amt)
        idx += 1

    dp[i] = seg.query_range(0, i - 1)
    seg.update_range(i, i, dp[i])

print(max(dp))
