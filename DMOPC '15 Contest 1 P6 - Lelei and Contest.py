# https://dmoj.ca/problem/dmopc15c1p6
# using Fenwick Tree for range update and range sum query
# Time complexity for both update and query: log(n)
# 100/100 with PYPY3 because it has a lower constant factor than segment trees

import sys

input = sys.stdin.readline


class FenwickTree:
    def __init__(self, size):
        self.size = size
        self.BIT1 = [0] * (size + 1)
        self.BIT2 = [0] * (size + 1)

    def update(self, BIT, i, val):
        while i <= self.size:
            BIT[i] += val
            i += i & -i

    def range_update(self, l, r, val):
        self.update(self.BIT1, l, val)
        self.update(self.BIT1, r + 1, -val)
        self.update(self.BIT2, l, val * (l - 1))
        self.update(self.BIT2, r + 1, -val * r)

    def sum(self, BIT, i):
        total = 0
        while i > 0:
            total += BIT[i]
            i -= i & -i
        return total

    def prefix_sum(self, i):
        return self.sum(self.BIT1, i) * i - self.sum(self.BIT2, i)

    def range_sum(self, l, r):
        return self.prefix_sum(r) - self.prefix_sum(l - 1)


M, N, Q = map(int, input().split())
arr = list(map(int, input().split()))

bit = FenwickTree(N)
for i in range(N):  # fill BIT with original array elements
    bit.range_update(i + 1, i + 1, arr[i])

for _ in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        bit.range_update(q[1], q[2], q[3])
    else:
        print(bit.range_sum(q[1], q[2]) % M)


# # Alternate solution using sqrt decomposition + lazy propagation
# # Time complexity for both operations: O(sqrt(n))
# # slower, but still 100/100 with PYPY3
#
# from math import isqrt
# import sys
#
# input = sys.stdin.readline
#
#
# class SqrtDecomp2:  # with lazy propagation
#     def __init__(self, nums):
#         self.nums = nums
#         self.width = isqrt(len(nums))
#         self.bn = (len(nums) // self.width) + 1
#         self.blocks = [0] * self.bn
#         self.lazy = [0] * self.bn  # an additional lazy[block] is added when querying elements in block
#         for i in range(len(nums)):
#             self.blocks[i // self.width] += nums[i]
#
#     def update(self, i, j, diff):
#         first = (i // self.width) + 1
#         last = (j // self.width) - 1
#         if first > last:  # doesn't cover any blocks
#             for v in range(i, j + 1):
#                 self.nums[v] += diff
#                 self.blocks[v // self.width] += diff
#             return
#
#         for b in range(first, last + 1):  # blocks in the middle
#             self.lazy[b] += diff
#             self.blocks[b] += diff * self.width
#         for v in range(i, first * self.width):  # individual cells
#             self.nums[v] += diff
#             self.blocks[v // self.width] += diff
#         for v in range((last + 1) * self.width, j + 1):
#             self.nums[v] += diff
#             self.blocks[v // self.width] += diff
#
#     def query(self, i, j):
#         first = (i // self.width) + 1
#         last = (j // self.width) - 1
#         res = 0
#
#         if first > last:  # doesn't cover any blocks
#             for v in range(i, j + 1):
#                 res += self.nums[v] + self.lazy[v // self.width]
#             return res
#
#         for b in range(first, last + 1):  # add value from blocks
#             res += self.blocks[b]
#         for v in range(i, first * self.width):  # add value from individual cells
#             res += self.nums[v] + self.lazy[v // self.width]
#         for v in range((last + 1) * self.width, j + 1):
#             res += self.nums[v] + self.lazy[v // self.width]
#         return res
#
#
# M, N, Q = map(int, input().split())
# arr = list(map(int, input().split()))
# decomp = SqrtDecomp2(arr)
#
# for _ in range(Q):
#     q = list(map(int, input().split()))
#     if q[0] == 1:  # range update
#         decomp.update(q[1] - 1, q[2] - 1, q[3])
#     else:
#         print(decomp.query(q[1] - 1, q[2] - 1) % M)
