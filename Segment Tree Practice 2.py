"""
https://dmoj.ca/problem/stp2
Range minimum query, also keep track of the index of the min
We use sqrt decomposition, which is much faster than segment tree
"""

from math import isqrt
import sys


class SqrtDecomp:
    def __init__(self, nums):
        self.width = isqrt(len(nums))  # width of a single block
        self.sqrtn = (len(nums) // self.width) + 1  # number of blocks
        self.blocks = [0] * self.sqrtn
        self.first = [0] * self.sqrtn
        self.nums = nums + [1 << 30] * self.width  # pad the end of the array to prevent index out of bounds
        for i in range(self.sqrtn):  # keep track of both the min and the first index of the min
            self.blocks[i] = min(self.nums[i * self.width: (i + 1) * self.width])
            self.first[i] = self.nums[i * self.width: (i + 1) * self.width].index(self.blocks[i]) + i * self.width

    def update(self, i, val):
        self.nums[i] = val
        block = i // self.width  # recompute this block
        self.blocks[block] = min(self.nums[block * self.width: (block + 1) * self.width])
        self.first[block] = self.nums[block * self.width: (block + 1) * self.width].index(self.blocks[block]) + block * self.width

    def query(self, i, j):
        first = (i // self.width) + 1
        last = (j // self.width) - 1
        smallest = float('inf')
        pos = -1
        if first > last:  # doesn't cover any full blocks
            for v in range(i, j+1):
                if self.nums[v] < smallest:
                    pos = v
                    smallest = self.nums[v]
            return smallest, pos

        for v in range(i, first * self.width):  # add value from individual cells
            if self.nums[v] < smallest:
                pos = v
                smallest = self.nums[v]
        for b in range(first, last + 1):  # add value from blocks
            if self.blocks[b] < smallest:
                pos = self.first[b]
                smallest = self.blocks[b]
        for v in range((last + 1) * self.width, j + 1):  # add value from trailing individual cells
            if self.nums[v] < smallest:
                pos = v
                smallest = self.nums[v]
        return smallest, pos


input = sys.stdin.readline
N, Q = map(int, input().split())
arr = list(map(int, input().split()))

sq = SqrtDecomp(arr)

for _ in range(Q):
    q, a, b = input().strip().split()
    a, b = int(a), int(b)
    if q == "U":
        sq.update(a - 1, b)
    else:
        smallest, index = sq.query(a - 1, b - 1)
        print(smallest, index+1)
