# https://dmoj.ca/problem/tsoc15c2p6
# Min sqrt decomp with range updates
# for this problem the optimal block size is 600 instead of sqrt(n) for some reason

import sys


class SqrtDecomp2:  # with lazy propagation
    def __init__(self, nums):
        self.width = 600  # optimal size for this problem
        self.nums = nums + [float('inf')] * self.width  # pad with extra elements to prevent out of bounds
        self.bn = (len(nums) // self.width) + 1
        self.blocks = [float('inf')] * self.bn
        self.lazy = [0] * self.bn  # an additional lazy[block] is added when querying elements in block
        for i in range(self.bn):  # precompute min in blocks
            self.blocks[i] = min(self.nums[i * self.width: (i + 1) * self.width])

    def update(self, i, j, diff):
        first = (i // self.width) + 1
        last = (j // self.width) - 1
        if first > last:  # doesn't cover any blocks, update every element
            first -= 1
            last += 1
            for v in range(i, j + 1):
                self.nums[v] += diff

            # recalculate the min after updating elements
            self.blocks[first] = min(self.nums[first * self.width:(first + 1) * self.width])
            self.blocks[last] = min(self.nums[last * self.width:(last + 1) * self.width])
            return

        for b in range(first, last + 1):  # blocks in the middle, update min directly
            self.lazy[b] += diff
            self.blocks[b] += diff

        for v in range(i, first * self.width):  # update block before the first full one normally
            self.nums[v] += diff
        self.blocks[first - 1] = min(self.nums[i:first * self.width])

        for v in range((last + 1) * self.width, j + 1):  # update block after the last one normally
            self.nums[v] += diff
        self.blocks[last + 1] = min(self.nums[(last + 1) * self.width:j + 1])

    def query(self, i, j):
        first = (i // self.width) + 1
        last = (j // self.width) - 1
        res = float('inf')

        if first > last:  # doesn't cover any blocks
            for v in range(i, j + 1):
                res = min(res, self.nums[v] + self.lazy[v // self.width])
            return res

        res = min(self.blocks[first:last + 1])  # get min from blocks
        for v in range(i, first * self.width):  # add value from individual cells
            res = min(res, self.nums[v] + self.lazy[v // self.width])
        for v in range((last + 1) * self.width, j + 1):
            res = min(res, self.nums[v] + self.lazy[v // self.width])
        return res


input = sys.stdin.readline
N, Q = map(int, input().split())
arr = list(map(int, input().split()))
sq = SqrtDecomp2(arr)

for _ in range(Q):
    l, r, diff = map(int, input().split())
    sq.update(l - 1, r - 1, -diff)  # remove elements from the range

    # query min, can't have negative enemies
    print(max(0, sq.query(l - 1, r - 1)), max(0, min(sq.blocks)))
