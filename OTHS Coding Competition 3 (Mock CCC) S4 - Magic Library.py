# https://dmoj.ca/problem/othscc3p4
# Sqrt decomposition

import sys


class LazySqrtDecomp:
    def __init__(self, nums):
        self.nums = nums
        self.width = int(len(nums) ** 0.5)
        bn = (len(nums) // self.width) + 1
        self.blocks = [[0] * MX for _ in range(bn)]
        self.lazy = [-1] * bn
        for i in range(len(nums)):
            self.blocks[i // self.width][nums[i]] += 1

    def _propagate(self, block):
        if self.lazy[block] == -1:
            return
        self.blocks[block] = [0] * MX
        self.blocks[block][self.lazy[block]] = self.width
        self.nums[self.width * block:self.width * (block + 1)] = [self.lazy[block]] * self.width
        self.lazy[block] = -1

    def update(self, i, j, new_val):
        """add diff to every value in [i, j]"""
        first = (i // self.width) + 1
        last = (j // self.width) - 1

        self._propagate(first - 1)
        self._propagate(last + 1)

        if first > last:  # doesn't cover any blocks
            for v in range(i, j + 1):
                self.blocks[v // self.width][self.nums[v]] -= 1
                self.nums[v] = new_val
                self.blocks[v // self.width][self.nums[v]] += 1
            return

        for b in range(first, last + 1):  # blocks in the middle
            self.lazy[b] = new_val
        for v in range(i, first * self.width):  # individual cells
            self.blocks[first - 1][self.nums[v]] -= 1
            self.nums[v] = new_val
            self.blocks[first - 1][self.nums[v]] += 1
        for v in range((last + 1) * self.width, j + 1):
            self.blocks[last + 1][self.nums[v]] -= 1
            self.nums[v] = new_val
            self.blocks[last + 1][self.nums[v]] += 1

    def query(self, i, j, val):
        """count the number of occurrences of val in [i, j]"""
        first = (i // self.width) + 1
        last = (j // self.width) - 1

        self._propagate(first - 1)
        self._propagate(last + 1)

        res = 0
        if first > last:  # doesn't cover any blocks
            for v in range(i, j + 1):
                res += (val == self.nums[v])
            return res

        for b in range(first, last + 1):  # add value from blocks
            if self.lazy[b] != -1:
                res += self.width * (self.lazy[b] == val)
            else:
                res += self.blocks[b][val]
        for v in range(i, first * self.width):  # add value from individual cells
            res += (val == self.nums[v])
        for v in range((last + 1) * self.width, j + 1):
            res += (val == self.nums[v])
        return res


input = sys.stdin.readline
MX = 501

N, Q = map(int, input().split())
arr = list(map(int, input().split()))

ans = []
sq = LazySqrtDecomp(arr)

for _ in range(Q):
    t, l, r, val = map(int, input().split())
    if t == 1:
        sq.update(l - 1, r - 1, val)
    else:
        a = sq.query(l - 1, r - 1, val)
        print(a)
