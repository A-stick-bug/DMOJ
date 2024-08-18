# https://dmoj.ca/problem/oly11c1g1
# Q: Find number of subarrays with median >=L
# Simplification: We call elements >=L `1` and everything else `-1`
# The problem now becomes find the number of non-negative subarrays

import sys


# point update, range query, uses 1-indexing
class FenwickTree:
    def __init__(self, size):
        """Create empty Fenwick Tree"""
        self.bit = [0] * (size + 1)

    def update(self, i: int, diff: int) -> None:
        """Add diff to self.bit[i]"""
        while i < len(self.bit):
            self.bit[i] += diff
            i += i & (-i)

    def query(self, i: int):
        """Get the sum up to the i-th element (inclusive)"""
        total = 0
        while i > 0:
            total += self.bit[i]
            i -= i & (-i)
        return total

    def query_range(self, left, right):
        """Query the sum of elements from left to right, inclusive"""
        return self.query(right) - self.query(left - 1)


input = sys.stdin.readline
N, L = map(int, input().split())
arr = [int(input()) for _ in range(N)]
arr = list(map(lambda x: 1 if x >= L else -1, arr))

cur_sum = 0
OFFSET = N + 1  # ensure only positive values in the BIT
bit = FenwickTree(2 * N + 2)
bit.update(OFFSET, 1)

total = 0
for i in arr:
    cur_sum += i
    total += bit.query(cur_sum + OFFSET)
    bit.update(cur_sum + OFFSET, 1)

print(total)
