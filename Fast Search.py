# PYTHON IS TOO SLOW SO TLE, CHECK C++ CODE
# https://dmoj.ca/problem/bsfast
# find index of first element strictly less than K
# traverse down the seg tree in log(n) to do this
# first check if we can go down the left path because it is earlier

import sys
from math import log2, ceil


class SegTree:  # general purpose segment tree for point update and range query
    # create segment tree from array (1-indexed)
    def __init__(self, arr, f=lambda x, y: x + y, default=0) -> None:
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

    # find first index less than k, traverse down the tree
    def query(self, i, l, r, cur_l, cur_r, k) -> int:
        if cur_r < l or r < cur_l or self.seg[i] >= k:  # fully outside or greater than number
            return -1
        if cur_l == cur_r:  # reached leaf
            return cur_l

        mid = (cur_l + cur_r) // 2
        left = self.query(i * 2, l, r, cur_l, mid, k)  # try going left
        if left != -1:
            return left
        return self.query(i * 2 + 1, l, r, mid + 1, cur_r, k)  # have to go right

    def query_range(self, l, r, k):
        return self.query(1, l, r, 0, N - 1, k)


input = sys.stdin.readline
inf = 1 << 30

N, Q = map(int, input().split())
arr = list(map(int, input().split()))

layers = ceil(log2(N))  # max depth of the seg tree, root has depth 0
seg = SegTree(arr, f=min, default=inf)  # min tree
N = 1 << layers

ans = 0
for _ in range(Q):
    q = list(map(int, input().split()))
    q[1:] = list(map(lambda x: x ^ ans, q[1:]))
    if q[0] == 1:  # update
        i, val = q[1:]
        seg.update(i - 1, val)
    else:
        l, r, k = q[1:]
        ans = seg.query_range(l - 1, r - 1, k) + 1
        print(ans)

# # alternate sqrt decomp method, also TLE
# import sys
# from math import isqrt
#
# class SqrtDecomp:
#     def __init__(self, nums):
#         self.width = isqrt(len(nums))  # width of a single block
#         self.sqrtn = (len(nums) // self.width) + 1  # number of blocks
#         self.blocks = [0] * self.sqrtn
#         self.nums = nums + [1 << 30] * self.width  # pad the end of the array to prevent index out of bounds
#         for i in range(self.sqrtn):
#             self.blocks[i] = min(self.nums[i * self.width: (i + 1) * self.width])
#
#     def update(self, i, val):
#         self.nums[i] = val
#         block = i // self.width  # recompute this block
#         self.blocks[block] = min(self.nums[block * self.width: (block + 1) * self.width])
#
#     def query(self, i, j, val):
#         first = (i // self.width) + 1
#         last = (j // self.width) - 1
#
#         if first > last:  # doesn't cover any full blocks
#             for v in range(i, j + 1):
#                 if self.nums[v] < val:
#                     return v
#
#         for v in range(i, first * self.width):  # add value from individual cells
#             if self.nums[v] < val:
#                 return v
#         for b in range(first, last + 1):  # add value from blocks
#             if self.blocks[b] < val:  # look inside block
#                 for v in range(b * self.width, (b + 1) * self.width):
#                     if self.nums[v] < val:
#                         return v
#         for v in range((last + 1) * self.width, j + 1):  # add value from trailing individual cells
#             if self.nums[v] < val:
#                 return v
#
#
# input = sys.stdin.readline
# inf = 1 << 30
#
# N, Q = map(int, input().split())
# arr = list(map(int, input().split()))
#
# seg = SqrtDecomp(arr)
#
# ans = 0
# for _ in range(Q):
#     q = list(map(int, input().split()))
#     q[1:] = list(map(lambda x: x ^ ans, q[1:]))
#     if q[0] == 1:  # update
#         i, val = q[1:]
#         seg.update(i - 1, val)
#     else:
#         l, r, k = q[1:]
#         ans = seg.query(l - 1, r - 1, k) + 1
#         print(ans)
