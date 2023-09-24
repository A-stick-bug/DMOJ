"""
https://dmoj.ca/problem/segtree
tfw you use sqrt decomposition on a segment tree problem

I was just trolling around with square root decomposition and I decided to test it on this problem
Fastest Python 3 and PYPY3 solution as of 2023/9/23 :)
Update: O(1)
Query: O(sqrt(n))
"""

import sys
from math import sqrt

input = sys.stdin.readline


class SqrtDecomp:
    def __init__(self, nums):
        self.nums = nums
        self.width = int(sqrt(len(nums)))
        self.sqrtn = (len(nums) // self.width) + 1
        self.mins = [float('inf')] * self.sqrtn

        for i in range(len(nums)):
            self.mins[i // self.width] = min(self.mins[i // self.width], nums[i])

    def update(self, i, val):
        self.nums[i] = val
        block_num = i // self.width

        start = block_num * self.width
        end = min(start + self.width, len(self.nums))
        self.mins[block_num] = min(self.nums[start:end])

    def get_range(self, i, j):
        first = (i // self.width) + 1
        last = (j // self.width) - 1

        if first > last:
            return min(self.nums[i:j + 1])

        res = min(self.mins[first:last + 1])
        res = min(res, min(self.nums[i:first * self.width]))
        res = min(res, min(self.nums[(last + 1) * self.width:j + 1]))
        return res


N, Q = map(int, input().split())
arr = [int(input()) for _ in range(N)]
sq = SqrtDecomp(arr)

for _ in range(Q):
    q = input().split()
    i, j = map(int, q[1:])
    if q[0] == "M":
        sq.update(i, j)
    else:
        print(sq.get_range(i, j))
