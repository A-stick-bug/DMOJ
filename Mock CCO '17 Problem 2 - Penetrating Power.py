# TLE, python is too slow, check c++ code
# https://dmoj.ca/problem/mcco17d1p2
# max seg tree with range updates
# each element has the sum of [i, i+K-1], so we need to update every range that covers this element

import sys
from math import log2, ceil


class LazySegTree:
    def __init__(self, f=lambda x, y: x + y, default=0) -> None:
        """create empty segment tree"""
        self.f = f  # function used to combine segments
        self.default = default
        layers = ceil(log2(N))  # max depth of the seg tree, root has depth 0
        self.size = 1 << layers
        self.seg = [default] * (2 * self.size)  # 1-indexed, need an extra layer for the actual data
        self.lazy = [default] * (2 * self.size)

    def push_down(self, i, segment_size):
        """transfer lazy tag from parent to children"""
        if self.lazy[i] == self.default:
            return
        self.lazy[i * 2] += self.lazy[i]  # transfer lazy tags
        self.lazy[i * 2 + 1] += self.lazy[i]
        self.seg[i * 2] += self.lazy[i]  # update value of segments
        self.seg[i * 2 + 1] += self.lazy[i]
        self.lazy[i] = self.default

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


input = sys.stdin.readline
N, K, Q = map(int, input().split())  # N elements, range of K, Q queries

seg = LazySegTree(f=max)

for _ in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 0:
        i, diff = map(int, q[1:])
        seg.update_range(max(0, i - K + 1), i, diff)  # 0-indexed updates, prevent index out of bounds
    else:
        l, r = map(int, q[1:])
        print(seg.query_range(l, r))  # 0-indexed queries

"""
N=8 K=4 Q=8
4 0 10 0 0 0 15 0
|----------|
"""
