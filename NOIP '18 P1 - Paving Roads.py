# https://dmoj.ca/problem/noip18p1
# Divide and conquer
# Split at smallest elements

import sys

sys.setrecursionlimit(110000)
inf = 1 << 30
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


def solve(l, r, sub):
    if l == r:
        return arr[l] - sub
    elif l > r:
        return 0
    mi, idx = seg.query(l, r)

    delta = mi - sub
    total = delta
    for c_l, c_r in [(l, idx - 1), (idx + 1, r)]:
        total += solve(c_l, c_r, sub + delta)
    return total


n = int(input())
arr = list(map(int, input().split()))

seg = SparseTable([(val, i) for i, val in enumerate(arr)], f=min, default=(inf, inf))

print(solve(0, n - 1, 0))
