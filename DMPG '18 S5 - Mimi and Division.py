# TLE, python is too slow, check c++ code
# https://dmoj.ca/problem/dmpg18s5
# sqrt decomposition
# init: for each number, add its divisors to the corresponding block
# update: remove divisors of old number and add new
# query: divisors in blocks + number of divisible numbers outside of blocks

import sys
import math


def divisors(n):
    divisors = []
    for i in range(1, math.isqrt(n) + 1):
        if n % i == 0:
            divisors.append(i)
            if i * i != n:
                divisors.append(n // i)
    return divisors


class SqrtDecomp:
    def __init__(self, nums):
        self.width = 450  # width of a single block
        self.sqrtn = (len(nums) // self.width) + 1  # number of blocks
        self.blocks = [[0] * 200001 for _ in range(self.sqrtn)]
        self.nums = nums

        for i in range(len(nums)):
            for div in divisors(self.nums[i]):  # add divisors
                self.blocks[i // self.width][div] += 1

    def update(self, i, val):
        block = i // self.width  # recompute this block
        for div in divisors(self.nums[i]):  # remove old
            self.blocks[block][div] -= 1
        self.nums[i] = val
        for div in divisors(val):  # add new
            self.blocks[block][div] += 1

    def query(self, i, j, d):
        first = (i // self.width) + 1
        last = (j // self.width) - 1
        total = 0
        if first > last:  # doesn't cover any full blocks
            for v in range(i, j + 1):
                total += self.nums[v] % d == 0
            return total

        for v in range(i, first * self.width):  # add value from individual cells
            total += self.nums[v] % d == 0
        for b in range(first, last + 1):  # add value from blocks
            total += self.blocks[b][d]
        for v in range((last + 1) * self.width, j + 1):  # add value from trailing individual cells
            total += self.nums[v] % d == 0
        return total


input = sys.stdin.readline
N, Q = map(int, input().split())
arr = list(map(int, input().split()))

sq = SqrtDecomp(arr)

for _ in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:  # query
        print(sq.query(q[1] - 1, q[2] - 1, q[3]))

    else:
        sq.update(q[1] - 1, q[2])
