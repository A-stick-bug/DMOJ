"""
https://dmoj.ca/problem/ds3
Segment tree template for min and gcd queries

The most important part of the code is combining the GCD segments
It uses the fact that the gcd of a range is at least as small as the min element
to keep track of counts
"""

import sys
from math import log2, ceil, gcd


def gcd_combine(left, right):
    gcd1, cnt1 = left
    gcd2, cnt2 = right
    res = gcd(gcd1, gcd2)
    if res == gcd1 == gcd2:  # equal gcd, we can combine the counts
        return res, cnt1 + cnt2
    elif gcd1 == res:
        return res, cnt1
    elif gcd2 == res:
        return res, cnt2
    else:  # since gcd is <= the min, we know that it doesn't exist in either segments
        return res, 0


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
inf = 1 << 30

N, Q = map(int, input().split())
arr = list(map(int, input().split()))

min_tree = SegTree(arr, min, inf)
gcd_tree = SegTree([(i, 1) for i in arr], gcd_combine, (0, 1))  # (gcd, count of gcd)

for _ in range(Q):
    q = input().split()
    a, b = map(int, q[1:])

    if q[0] == "C":  # change element value
        min_tree.update(a - 1, b)
        gcd_tree.update(a - 1, (b, 1))

    elif q[0] == "M":  # get min
        print(min_tree.query_range_iterative(a - 1, b - 1))

    elif q[0] == "G":  # get gcd
        print(gcd_tree.query_range_iterative(a - 1, b - 1)[0])

    else:  # get element occurrences
        print(gcd_tree.query_range_iterative(a - 1, b - 1)[1])
