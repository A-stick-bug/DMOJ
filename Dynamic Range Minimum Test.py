"""
https://dmoj.ca/problem/segtree
tfw you use sqrt decomposition on a segment tree problem

I was just trolling around with square root decomposition and I decided to test it on this problem
Fastest Python 3 and PYPY3 solution as of 2023/9/23 :)
Update: O(sqrt(n))
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

# # boring way using segment tree
# # root is at 1, children of node i is seg[i*2] and seg[i*2+1], parent of node i is seg[i//2]
#
# import sys
# from math import log2, ceil
#
#
# # create segment tree from array
# def create() -> None:
#     p2 = 1 << layers
#     for i in range(N):  # base layer
#         seg[p2 + i] = arr[i]
#     for i in reversed(range(1, p2)):  # create other layers from base
#         seg[i] = min(seg[i * 2], seg[i * 2 + 1])
#
#
# # update i-th element to val, 0-indexed
# def update(i, val) -> None:
#     i += 1 << layers  # start from bottom
#     seg[i] = val
#     while i > 1:
#         i //= 2
#         seg[i] = min(seg[i * 2], seg[i * 2 + 1])
#
#
# # query left to right inclusive
# def query(i, l, r, tl, tr) -> int:
#     if l > r:
#         return inf
#     if l == tl and r == tr:
#         return seg[i]
#     tm = (tl + tr) // 2
#     return min(query(i * 2, l, min(r, tm), tl, tm),
#                query(i * 2 + 1, max(l, tm + 1), r, tm + 1, tr))
#
#
# input = sys.stdin.readline
# inf = 1 << 30
#
# N, Q = map(int, input().split())
# arr = [int(input()) for _ in range(N)]
#
# layers = ceil(log2(N))  # max depth of the seg tree, root has depth 0
# seg = [inf] * (1 << (layers + 1))  # 1-indexed, need an extra layer for the root
# create()
# N = 1 << layers
# # print(seg)
#
# for _ in range(Q):
#     q = input().split()
#     if q[0] == "M":
#         i, v = map(int, q[1:])
#         update(i, v)
#     else:
#         l, r = map(int, q[1:])
#         print(query(1, l, r, 0, N - 1))
#     # print(seg)
