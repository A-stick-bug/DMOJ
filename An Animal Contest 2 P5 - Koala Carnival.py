# https://dmoj.ca/problem/aac2p5
# - For each l, precompute the maximum possible r that has no duplicates
# - This array will be monotonic
# - For each query, the left must be <=l and the right must be >=r
# - Binary search for the leftmost possible and rmq for max length

import sys
from bisect import bisect_left

log2 = lambda x: x.bit_length() - 1


class SparseTable:  # 0-indexed
    def __init__(self, arr, f=max, default=0):
        N = len(arr)
        self.layers = log2(len(arr)) + 1
        self.table = [[default] * self.layers for _ in range(len(arr))]
        self.f = f
        for i in range(len(arr)):  # base layer
            self.table[i][0] = arr[i]  # column 1: base cases

        for k in range(1, self.layers):  # build the rest of the table
            for i in range(N - (1 << k) + 1):
                self.table[i][k] = f(self.table[i][k - 1], self.table[i + (1 << (k - 1))][k - 1])

    def query(self, l, r):
        k = log2(r - l + 1)
        return self.f(self.table[l][k], self.table[r - (1 << k) + 1][k])


input = sys.stdin.readline
N, Q = map(int, input().split())
arr = list(map(int, input().split()))

loc = [N + 1] * (N + 1)  # closest index of `arr[i]` to the right
right = [-1] * N  # how far you can extend to the right from `i`
mx = N - 1
for i in reversed(range(N)):
    mx = min(mx, loc[arr[i]] - 1)  # check next occurrence of arr[i]
    right[i] = mx
    loc[arr[i]] = i

length = [r - i + 1 for i, r in enumerate(right)]  # length of longest valid range starting from `i`
length_st = SparseTable(length)  # for O(1) max queries

ans = 0
for _ in range(Q):
    l, r = map(lambda x: (int(x) ^ ans) - 1, input().split())

    leftmost = bisect_left(right, r)  # leftmost possible starting point
    best = length_st.query(leftmost, l)  # max of all valid starting points

    print(best)
    ans = best

"""
12 0
4 5 6 1 4 3 2 7 6 8 5 7
"""
