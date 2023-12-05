# https://dmoj.ca/problem/coci22c4p5
# get median using an order statistic tree (implemented using Fenwick Tree)
# this has a better constant factor (therefore faster) than a segment tree

from math import ceil
import sys


class OST:
    def __init__(self, size):
        self.size = size
        self.tree = [0] * (size + 1)

    def update(self, i, diff):
        while i <= self.size:
            self.tree[i] += diff
            i += i & -i

    def query(self, i):
        res = 0
        while i:
            res += self.tree[i]
            i -= i & (-i)
        return res

    def select(self, k):  # get k-th smallest element
        i = 0
        bl = self.size.bit_length()
        for p in range(bl, -1, -1):
            if i + (1 << p) <= self.size and self.tree[i + (1 << p)] < k:
                i += 1 << p
                k -= self.tree[i]
        return i + 1


input = sys.stdin.readline
n = int(input())
queries = [list(map(int, input().split())) for _ in range(n)]

# coordinate compression
decompress = sorted(set(list(map(lambda x: x[0], queries))))
compress = {val: i + 1 for i, val in enumerate(decompress)}

ost = OST(len(decompress) + 1)  # have enough spots for every height
people = 0
for a, b in queries:
    a = compress[a]
    ost.update(a, b)  # b people with a height get added
    people += b

    print(decompress[ost.select(ceil(people / 2)) - 1])  # decompress to get original value
