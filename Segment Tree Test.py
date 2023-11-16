"""
TLE: 65/100
Check c++ version for code that passes

https://dmoj.ca/problem/ds3
Segment tree for min and gcd queries
Sqrt decomposition for frequency queries (number of elements equal to x in a range)
"""

import sys
from math import log2, ceil, gcd, isqrt
from collections import Counter


class SegTree:
    # create segment tree from array
    def __init__(self, arr, f, default) -> None:
        self.f = f
        self.default = default
        self.seg = [default] * (1 << (layers + 1))  # 1-indexed, need an extra layer for the root
        p2 = 1 << layers
        for i in range(N):  # base layer
            self.seg[p2 + i] = arr[i]
        for i in reversed(range(1, p2)):  # create other layers from base
            self.seg[i] = f(self.seg[i * 2], self.seg[i * 2 + 1])

    # update i-th element to val, 0-indexed
    def update(self, i, val) -> None:
        i += 1 << layers  # start from bottom
        self.seg[i] = val
        while i > 1:
            i //= 2
            self.seg[i] = self.f(self.seg[i * 2], self.seg[i * 2 + 1])

    # query left to right inclusive
    def query(self, i, l, r, tl, tr) -> int:
        if l > r:
            return self.default
        if l == tl and r == tr:
            return self.seg[i]
        tm = (tl + tr) // 2
        return self.f(self.query(i * 2, l, min(r, tm), tl, tm),
                      self.query(i * 2 + 1, max(l, tm + 1), r, tm + 1, tr))


class Freq:
    def __init__(self, nums):
        self.nums = nums
        self.width = isqrt(len(nums))
        self.block_count = (len(nums) // self.width) + 1
        self.blocks = [Counter() for _ in range(self.block_count)]
        for i in range(len(nums)):
            self.blocks[i // self.width][nums[i]] += 1

    def update(self, i, val):
        block_num = i // self.width
        self.blocks[block_num][self.nums[i]] -= 1
        self.nums[i] = val
        self.blocks[block_num][val] += 1

    def get_count(self, i, j, x):
        first = (i // self.width) + 1
        last = (j // self.width) - 1
        count = 0
        if first > last:
            count += self.nums[i:j + 1].count(x)
        else:
            count += sum(block[x] for block in self.blocks[first:last + 1])
            count += self.nums[i:first * self.width].count(x)
            count += self.nums[(last + 1) * self.width:j + 1].count(x)
        return count


input = sys.stdin.readline
inf = 1 << 30

N, Q = map(int, input().split())
arr = list(map(int, input().split()))

layers = ceil(log2(N))  # max depth of the seg tree, root has depth 0
min_tree = SegTree(arr, min, inf)
gcd_tree = SegTree(arr, gcd, 0)
N = 1 << layers

freq = Freq(arr)

for _ in range(Q):
    q = input().split()
    a, b = map(int, q[1:])

    if q[0] == "C":  # change element value
        min_tree.update(a - 1, b)
        gcd_tree.update(a - 1, b)
        freq.update(a-1, b)

    elif q[0] == "M":  # get min
        print(min_tree.query(1, a - 1, b - 1, 0, N - 1))

    elif q[0] == "G":  # get gcd
        print(gcd_tree.query(1, a - 1, b - 1, 0, N - 1))

    else:  # get element occurrences
        val = gcd_tree.query(1, a - 1, b - 1, 0, N - 1)
        print(freq.get_count(a - 1, b - 1, val))
