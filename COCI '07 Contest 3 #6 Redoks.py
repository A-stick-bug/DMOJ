# MLE, PYTHON USES TOO MUCH MEMORY, CHECK C++ CODE
# https://dmoj.ca/problem/coci07c3p6
# Segment tree with lazy propagation
# - For each segment, we keep track of the occurrences of each digit
# - To update (and push down), we shift the digits 1 to the right, mod 10
# - To answer queries, we can get the sum of the digits using hte frequencies

import sys
from math import log2, ceil

shift = lambda arr, amt: arr[-(amt % 10):] + arr[:-(amt % 10)]  # [1,2,3,4], 2 --> [3,4,1,2]
combine = lambda a1, a2: [i + j for i, j in zip(a1, a2)]  # [1,1,1], [1,2,1] --> [2,3,1]  (adds digit count)


class LazySegTree:
    def __init__(self, arr, f, default) -> None:
        """create 1-indexed segment tree from 0-indexed array"""
        self.f = f  # function used to combine segments
        self.default = default
        layers = ceil(log2(N))  # max depth of the seg tree, root has depth 0
        self.size = 1 << layers
        self.seg = [default.copy() for _ in range(2 * self.size)]  # 1-indexed, need an extra layer for the actual data
        self.lazy = [0] * (2 * self.size)

        for i in range(N):  # base layer
            self.seg[self.size + i][arr[i]] += 1
        for i in reversed(range(1, self.size)):  # create other layers from base
            self.seg[i] = f(self.seg[i * 2], self.seg[i * 2 + 1])

    def push_down(self, i, segment_size):
        """transfer lazy tag from parent to children"""
        if self.lazy[i] == 0:
            return
        self.lazy[i * 2] += self.lazy[i]  # transfer lazy tags
        self.lazy[i * 2 + 1] += self.lazy[i]
        self.seg[i * 2] = shift(self.seg[i * 2], self.lazy[i])  # update value of segments
        self.seg[i * 2 + 1] = shift(self.seg[i * 2 + 1], self.lazy[i])
        self.lazy[i] = 0

    def update(self, i, l, r, cur_l, cur_r, diff) -> None:
        """add diff to [left, right]"""
        if cur_r < l or r < cur_l:  # fully outside segment
            return
        mid = (cur_l + cur_r) // 2
        if l <= cur_l and cur_r <= r:  # fully inside segment: update lazily
            self.lazy[i] += diff
            self.seg[i] = shift(self.seg[i], diff)
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
N, Q = map(int, input().split())
arr = list(map(int, list(input().strip())))

seg = LazySegTree(arr, f=combine, default=[0] * 10)

for _ in range(Q):
    l, r = map(lambda x: int(x) - 1, input().split())  # convert to 0-indexing
    freq = seg.query_range(l, r)
    print(sum(freq[i] * i for i in range(10)))  # sum of numbers on dials

    seg.update_range(l, r, 1)
