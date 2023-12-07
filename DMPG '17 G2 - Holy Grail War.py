# TLE, PYTHON IS TOO SLOW, CHECK C++ CODE
# https://dmoj.ca/problem/dmpg17g2
# I chose to use a segment tree for this one because it's easier to combine 2 segments than sqrt blocks
# template range query, point update segment tree, requires some thinking for the combine function

from math import ceil, log2
import sys


def combine(left, right):
    """combine left and right segment"""
    total_l, prefix_l, suffix_l, inside_l = left  # unpack
    total_r, prefix_r, suffix_r, inside_r = right
    return (total_l + total_r,  # total
            max(prefix_l, total_l + prefix_r),  # prefix max
            max(suffix_r, suffix_l + total_r),  # suffix max
            max(inside_l, inside_r, suffix_l + prefix_r))  # max inside of segment


class SegTree:
    # create 1-indexed segment tree from 0-indexed array
    def __init__(self, arr, f, default) -> None:
        self.f = f  # function used to combine segments
        self.default = default
        self.seg = [default] * (1 << (layers + 1))  # 1-indexed, need an extra layer for the root
        self.size = 1 << layers
        for i in range(N):  # base layer
            self.seg[self.size + i] = (arr[i],) * 4
        for i in reversed(range(1, self.size)):  # create other layers from base
            self.seg[i] = f(self.seg[i * 2], self.seg[i * 2 + 1])

    # update i-th element to val, 0-indexed
    def update(self, i, val) -> None:
        i += self.size  # start from bottom
        self.seg[i] = (val,) * 4
        while i > 1:
            i //= 2
            self.seg[i] = self.f(self.seg[i * 2], self.seg[i * 2 + 1])

    # query left to right inclusive
    def query(self, i, l, r, cur_l, cur_r) -> int:
        if cur_l > r or cur_r < l:
            return self.default
        if l <= cur_l and cur_r <= r:
            return self.seg[i]
        mid = (cur_l + cur_r) // 2
        return self.f(self.query(i * 2, l, r, cur_l, mid),
                      self.query(i * 2 + 1, l, r, mid + 1, cur_r))

    def query_range(self, l, r):
        return self.query(1, l, r, 0, N - 1)


input = sys.stdin.readline
inf = 1 << 30

N, Q = map(int, input().split())
arr = list(map(int, input().split()))

layers = ceil(log2(N))  # max depth of the seg tree, root has depth 0
seg = SegTree(arr, combine, (-inf,) * 4)
N = 1 << layers

for _ in range(Q):
    q = input().split()
    if q[0] == "S":
        i, v = map(int, q[1:])
        seg.update(i - 1, v)  # 0-indexed updates
    else:
        l, r = map(int, q[1:])
        print(seg.query_range(l - 1, r - 1)[3])  # 0-indexed queries
