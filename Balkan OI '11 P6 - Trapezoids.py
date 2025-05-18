# https://dmoj.ca/problem/bkoi11p6
# MLE in python, check C++ code for explanations

import sys
from heapq import heappush, heappop, heapify
from math import log2, ceil

input = sys.stdin.readline
MOD = 30013


def comb(l, r):
    if l[0] == r[0]:  # combine frequencies
        return l[0], (l[1] + r[1]) % MOD
    else:
        return max(l, r)


class SegTree:
    def __init__(self, arr, f, default) -> None:
        """create 1-indexed segment tree from 0-indexed array"""
        self.f = f  # function used to combine segments
        self.default = default
        self.layers = ceil(log2(m))  # max depth of the seg tree, root has depth 0
        self.size = 1 << self.layers
        self.seg = [default] * (2 * self.size)  # 1-indexed, need an extra layer for the actual data

        for i in range(m):  # base layer
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

    def query(self, left, right):
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


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

arr.sort(key=lambda x: x[0])

ordered = []
for _, _, c, d in arr:
    ordered.append(c)
    ordered.append(d)
ordered = sorted(set(ordered))
m = len(ordered)
compress = {ordered[i]: i for i in range(m)}

pending = []  # (b, c, d, value, frequency)

seg = SegTree([(0, 0) for _ in range(m + 2)], f=comb, default=(0, 0))
for a, b, c, d in arr:
    while pending and pending[0][0] < a:
        pb, pc, pd, val, freq = heappop(pending)
        seg.update(compress[pd], (val, freq))

    best, freq = seg.query(0, compress[c])
    freq = max(1, freq)
    heappush(pending, (b, c, d, best + 1, freq))

while pending:  # clear up remainder trapezoids
    pb, pc, pd, val, freq = heappop(pending)
    freq = max(1, freq)
    seg.update(compress[pd], (val, freq))

print(*seg.query(0, m + 1))
