# TLE, python is too slow, check c++ code
# https://dmoj.ca/problem/goode
# similar to https://dmoj.ca/problem/bsfast but uses lazy propagation
# use lazy segment tree to update range, traverse tree to get index of L-th broken line

import sys
from math import log2, ceil


class LazySegTree:
    def __init__(self, arr, f=lambda x, y: x + y, default=0) -> None:
        """create 1-indexed segment tree from 0-indexed array"""
        self.f = f  # function used to combine segments
        self.default = default
        layers = ceil(log2(N))  # max depth of the seg tree, root has depth 0
        self.size = 1 << layers
        self.seg = [default] * (2 * self.size)  # 1-indexed, need an extra layer for the actual data
        self.lazy = [default] * (2 * self.size)

        for i in range(N):  # base layer
            self.seg[self.size + i] = arr[i]
        for i in reversed(range(1, self.size)):  # create other layers from base
            self.seg[i] = f(self.seg[i * 2], self.seg[i * 2 + 1])

    def push_down(self, i, segment_size):
        """transfer lazy tag from parent to children"""
        if self.lazy[i] & 1 == 0:  # check if even because 2 updates cancel out
            return
        self.lazy[i * 2] += self.lazy[i]  # transfer lazy tags
        self.lazy[i * 2 + 1] += self.lazy[i]
        self.seg[i * 2] = segment_size - self.seg[i * 2]  # update value of segments
        self.seg[i * 2 + 1] = segment_size - self.seg[i * 2 + 1]
        self.lazy[i] = self.default

    def update(self, i, l, r, cur_l, cur_r, diff) -> None:
        """add diff to [left, right]"""
        if cur_r < l or r < cur_l:  # fully outside segment
            return
        mid = (cur_l + cur_r) // 2
        if l <= cur_l and cur_r <= r:  # fully inside segment: update lazily
            self.lazy[i] += diff
            self.seg[i] = (cur_r - cur_l + 1) - self.seg[i]
            return
        self.push_down(i, cur_r - mid)  # partial covers, recurse deeper
        self.update(i * 2, l, r, cur_l, mid, diff)
        self.update(i * 2 + 1, l, r, mid + 1, cur_r, diff)
        self.seg[i] = self.f(self.seg[i * 2], self.seg[i * 2 + 1])

    def query(self, i, l, r, cur_l, cur_r, broken) -> int:
        """query [left, right]"""
        if self.seg[i] < broken:  # fully outside segment or didn't break yet
            return -1
        if cur_l == cur_r:  # reached leaf
            return cur_l

        mid = (cur_l + cur_r) // 2  # traverse down further
        self.push_down(i, cur_r - mid)
        left = self.query(i * 2, l, r, cur_l, mid, broken)
        if left != -1:  # go right, minus te broken ones in the left
            return left
        return self.query(i * 2 + 1, l, r, mid + 1, cur_r, broken - self.seg[i * 2])

    def query_range(self, l, r, broken):
        return self.query(1, l, r, 0, self.size - 1, broken)

    def update_range(self, l, r, diff):
        return self.update(1, l, r, 0, self.size - 1, diff)


input = sys.stdin.readline
N, M, L = map(int, input().split())
arr = [1] * N

seg = LazySegTree(arr)

for _ in range(M):
    l, r = map(int, input().split())
    seg.update_range(l - 1, r - 1, 1)  # 0-indexed updates
    broke = seg.query_range(0, N - 1, L)  # 0-indexed queries
    if broke == -1:
        print("AC?")
    else:
        print(broke + 1)

"""
4 2 1
1 4
1 3

AC?
1
"""
