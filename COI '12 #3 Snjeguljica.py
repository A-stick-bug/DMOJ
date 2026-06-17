# https://dmoj.ca/problem/gfsscc21p4

import sys
from math import log2, ceil

input = sys.stdin.readline

class SegTree:
    def __init__(self, arr, f=lambda x, y: x + y, default=0) -> None:
        """create 1-indexed segment tree from 0-indexed array"""
        N = len(arr)
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

    def __str__(self):
        return "\n".join(
            " ".join(
                map(str, [self.seg[j] for j in range(2 ** i, 2 * 2 ** i)])).center(50)
            for i in range(self.layers))


N,Q = map(int, input().split())
arr = [-1] + list(map(int, input().split()))
loc = [-1] * (N+1)
for i in range(1, N + 1):
    loc[arr[i]] = i

seg = SegTree(loc, min, default=1<<60)
seg2 = SegTree(loc, max, default=-(1<<60))

for _ in range(Q):
    t,a,b = list(map(int, input().split()))
    if t == 1:
        # swap
        arr[a],arr[b] = arr[b],arr[a]
        loc[arr[a]] = a
        loc[arr[b]] = b
        seg.update(arr[a], loc[arr[a]])
        seg.update(arr[b], loc[arr[b]])
        seg2.update(arr[a], loc[arr[a]])
        seg2.update(arr[b], loc[arr[b]])
    else:
        mi = seg.query(a,b)
        mx = seg2.query(a,b)
        if mx - mi == b - a:
            print("YES")
        else:
            print("NO")
