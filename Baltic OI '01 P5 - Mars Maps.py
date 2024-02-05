"""
https://dmoj.ca/problem/btoi01p5
Q: find total area covered by at least 1 tile
A: Line sweep with rectangles + Sqrt Decomp for range query

- sort by x, vertical line sweep from left to right
- for every event, process everything before it and update current range
- Area = L*W, W=(current x - previous x), L=(number of non-zero elements)
  - we can use sqrt decomposition to find the number of elements equal to 0, then
    use complementary counting: (total - number of 0)

TC: O(N*sqrt(MN))
"""

import sys
from collections import defaultdict


class LazySqrtDecomp:
    def __init__(self, nums):
        self.nums = nums
        self.width = int(len(nums) ** 0.5)
        bn = (len(nums) // self.width) + 1
        self.blocks = [defaultdict(int) for _ in range(bn)]
        self.lazy = [0] * bn  # an additional lazy[block] is added when querying elements in block
        for i in range(len(nums)):
            self.blocks[i // self.width][nums[i]] += 1

    def update(self, i, j, diff):
        """add diff to every value in [i, j]"""
        first = (i // self.width) + 1
        last = (j // self.width) - 1
        if first > last:  # doesn't cover any blocks
            for v in range(i, j + 1):
                self.blocks[v // self.width][self.nums[v]] -= 1
                self.nums[v] += diff
                self.blocks[v // self.width][self.nums[v]] += 1
            return

        for b in range(first, last + 1):  # blocks in the middle
            self.lazy[b] += diff
        for v in range(i, first * self.width):  # individual cells
            self.blocks[first - 1][self.nums[v]] -= 1
            self.nums[v] += diff
            self.blocks[first - 1][self.nums[v]] += 1
        for v in range((last + 1) * self.width, j + 1):
            self.blocks[last + 1][self.nums[v]] -= 1
            self.nums[v] += diff
            self.blocks[last + 1][self.nums[v]] += 1

    def query(self, i, j, val):
        """count the number of occurrences of val in [i, j]"""
        first = (i // self.width) + 1
        last = (j // self.width) - 1
        res = 0

        if first > last:  # doesn't cover any blocks
            for v in range(i, j + 1):
                res += (self.nums[v] == val - self.lazy[v // self.width])
            return res

        for b in range(first, last + 1):  # add value from blocks
            res += self.blocks[b][val - self.lazy[b]]
        for v in range(i, first * self.width):  # add value from individual cells
            res += (self.nums[v] == val - self.lazy[first - 1])
        for v in range((last + 1) * self.width, j + 1):
            res += (self.nums[v] == val - self.lazy[last + 1])
        return res


input = sys.stdin.readline
n = int(input())
MN = 30000
events = []
for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    events.append((x1, y1, y2, 1))  # rectangle start
    events.append((x2, y1, y2, -1))  # rectangle end
events.sort(key=lambda x: x[0])  # sort by x

total = 0
sq = LazySqrtDecomp([0] * (MN + 1))
prev_x = 0
for x, y1, y2, diff in events:
    zero = sq.query(0, MN, val=0)  # count number of 0
    total += (x - prev_x) * ((MN + 1) - zero)  # area covered between current and previous event
    sq.update(y1, y2 - 1, diff)
    prev_x = x

print(total)
