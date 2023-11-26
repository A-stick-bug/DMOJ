# https://dmoj.ca/problem/stp1
# sqrt decomp beats seg tree on another template seg tree problem...

import sys
from math import sqrt

input = sys.stdin.readline


class SqrtDecomp:
    def __init__(self, nums):
        self.nums = nums
        self.width = int(sqrt(len(nums)))
        self.sqrtn = (len(nums) // self.width) + 1
        self.mins = [0] * self.sqrtn

        for i in range(len(nums)):
            self.mins[i // self.width] += nums[i]

    def update(self, i, val):
        diff = val - self.nums[i]
        self.nums[i] = val
        self.mins[i // self.width] += diff

    def get_range(self, i, j):
        first = (i // self.width) + 1
        last = (j // self.width) - 1

        if first > last:
            return sum(self.nums[i:j + 1])

        res = sum(self.mins[first:last + 1])
        res += sum(self.nums[i:first * self.width])
        res += sum(self.nums[(last + 1) * self.width:j + 1])
        return res


N, Q = map(int, input().split())
arr = list(map(int, input().split()))
sq = SqrtDecomp(arr)

for _ in range(Q):
    q = input().split()
    i, j = map(int, q[1:])
    if q[0] == "U":
        sq.update(i - 1, j)
    else:
        print(sq.get_range(i - 1, j - 1))
