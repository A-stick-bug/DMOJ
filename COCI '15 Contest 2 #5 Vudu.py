# TLE, PYTHON IS TOO SLOW, CHECK C++ CODE
# https://dmoj.ca/problem/coci15c2p5
#
# Count subarrays with average > N
# In other words, count subarrays with sum > 0 if we minus every element by P
# use a Fenwick Tree to optimize to O(nlogn)
# - for every element, we count the numbers of indices i where psa[cur] - psa[i] > 0
# - note that we also need to consider removing nothing (just add a 0 to the BIT)

from itertools import accumulate


class FenwickTree:  # point update, range query, uses 1-indexing
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


N = int(input())
arr = list(map(int, input().split()))
P = int(input())
arr = list(map(lambda x: x - P, arr))

ss = sorted(set(accumulate(arr)).union({0}))  # coordinate compression
compress = {ss[i]: i + 1 for i in range(len(ss))}

bit = FenwickTree(len(ss))
bit.update(compress[0], 1)
total = 0
cur_sum = 0  # sum of everything up to current index

for cur in arr:
    cur_sum += cur
    total += bit.query(compress[cur_sum])
    bit.update(compress[cur_sum], 1)
print(total)
