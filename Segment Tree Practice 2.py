"""
https://dmoj.ca/problem/stp2
Range minimum query, also keep track of the index of the min
"""

import sys
from math import log2, ceil


class SegTree:
    def __init__(self, arr, f, default) -> None:
        """create 1-indexed segment tree from 0-indexed array"""
        self.f = f  # function used to combine segments
        self.default = default
        self.layers = ceil(log2(N))  # max depth of the seg tree, root has depth 0
        self.size = 1 << self.layers
        self.seg = [default] * (2 * self.size)  # 1-indexed, need an extra layer for the actual data

        for i in range(N):  # base layer
            self.seg[self.size + i] = arr[i]
        for i in reversed(range(1, self.size)):  # create other layers from base
            self.seg[i] = f(self.seg[i * 2], self.seg[i * 2 + 1])

    def update(self, i, val) -> None:
        """update i-th element to val, 0-indexed"""
        i += self.size  # start from bottom
        self.seg[i] = val
        while i > 1:
            i //= 2
            self.seg[i] = self.f(self.seg[i * 2], self.seg[i * 2 + 1])

    def query(self, i, l, r, cur_l, cur_r) -> int:
        """query [left, right]"""
        if cur_r < l or r < cur_l:  # fully outside segment
            return self.default
        if l <= cur_l and cur_r <= r:  # fully inside segment
            return self.seg[i]
        mid = (cur_l + cur_r) // 2  # traverse down further
        return self.f(self.query(i * 2, l, r, cur_l, mid),
                      self.query(i * 2 + 1, l, r, mid + 1, cur_r))

    def query_range(self, l, r):
        return self.query(1, l, r, 0, self.size - 1)

    def query_range_iterative(self, left, right):
        """faster iterative query, no idea how this works, just use it when the recursive one is too slow"""
        left += self.size
        right += self.size + 1

        res_left = res_right = self.default
        while left < right:
            if left & 1:  # left is odd
                res_left = self.f(res_left, self.seg[left])
                left += 1
            if right & 1:
                right -= 1
                res_right = self.f(self.seg[right], res_right)
            left //= 2
            right //= 2
        return self.f(res_left, res_right)


input = sys.stdin.readline
N, Q = map(int, input().split())
arr = [(x, i + 1) for i, x in enumerate(map(int, input().split()))]

seg = SegTree(arr, f=min, default=(1 << 30, -1))

for _ in range(Q):
    q, a, b = input().strip().split()
    a, b = int(a), int(b)
    if q == "U":
        seg.update(a - 1, (b, a))
    else:
        print(*seg.query_range_iterative(a - 1, b - 1))
