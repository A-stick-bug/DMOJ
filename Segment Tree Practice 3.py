# https://dmoj.ca/problem/stp3
# Sqrt decomposition
# Q: query max sum starting at left and ending somewhere in (L, R]
# compute both the sum (covers entire range) and the max prefix sum (not to be confused with PSA) for each block
# for each block, we either take -everything- or -all blocks before the current block + current max prefix sum-

import sys

input = sys.stdin.readline
inf = 1 << 30


def max_prefix(arr):
    highest = -inf
    total = 0
    for i in arr:
        total += i
        highest = max(highest, total)
    return highest


class SqrtDecomp:
    def __init__(self, nums):
        self.width = 400  # width of a single block (optimal)
        self.sqrtn = (len(nums) // self.width) + 1  # number of blocks
        self.total = [0] * self.sqrtn
        self.prefix = [0] * self.sqrtn
        self.nums = nums + [0] * self.width  # pad the end of the array to prevent index out of bounds

        for i in range(self.sqrtn):  # keep track of both the sum and max prefix sum
            self.total[i] = sum(self.nums[i * self.width: (i + 1) * self.width])
            self.prefix[i] = max_prefix(self.nums[i * self.width: (i + 1) * self.width])

    def update(self, i, val):
        self.nums[i] = val
        i //= self.width  # recompute this block
        self.total[i] = sum(self.nums[i * self.width: (i + 1) * self.width])
        self.prefix[i] = max_prefix(self.nums[i * self.width: (i + 1) * self.width])

    def query(self, i, j):
        first = (i // self.width) + 1
        last = (j // self.width) - 1
        if first > last:  # doesn't cover any full blocks, compute normally
            return max_prefix(self.nums[i:j + 1])

        highest = max_prefix(self.nums[i: first * self.width])  # elements before blocks
        total = sum(self.nums[i: first * self.width])

        for b in range(first, last + 1):  # precomputed values from blocks
            highest = max(highest, total, total + self.prefix[b])
            total += self.total[b]

        # consider adding elements after blocks
        highest = max(highest, total + max_prefix(self.nums[(last + 1) * self.width: j + 1]))
        return highest


N, Q = map(int, input().split())
arr = list(map(int, input().split()))
sq = SqrtDecomp(arr)

for _ in range(Q):
    op, a, b = input().split()
    a, b = int(a), int(b)
    if op == "P":  # query
        print(sq.query(a - 1, b - 1))
    else:  # update
        sq.update(a - 1, b)
