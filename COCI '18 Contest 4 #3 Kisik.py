# TLE, PYTHON IS TOO SLOW, CHECK C++ CODE FOR EXPLANATIONS
# https://dmoj.ca/problem/coci18c4p3

import sys
from bisect import bisect_left as lower_bound
from bisect import bisect_right as upper_bound


class FenwickTree:
    def __init__(self, x):
        bit = self.bit = list(x)
        size = self.size = len(bit)
        for i in range(size):
            j = i | (i + 1)
            if j < size:
                bit[j] += bit[i]

    def update(self, idx, x):
        """updates bit[idx] += x"""
        while idx < self.size:
            self.bit[idx] += x
            idx |= idx + 1

    def __call__(self, end):
        """calc sum(bit[:end])"""
        x = 0
        while end:
            x += self.bit[end - 1]
            end &= end - 1
        return x

    def find_kth(self, k):
        """Find largest idx such that sum(bit[:idx]) <= k"""
        idx = -1
        for d in reversed(range(self.size.bit_length())):
            right_idx = idx + (1 << d)
            if right_idx < self.size and self.bit[right_idx] <= k:
                idx = right_idx
                k -= self.bit[idx]
        return idx + 1, k


class SortedList:
    block_size = 700

    def __init__(self, iterable=()):
        self.macro = []
        self.micros = [[]]
        self.micro_size = [0]
        self.fenwick = FenwickTree([0])
        self.size = 0
        for item in iterable:
            self.insert(item)

    def insert(self, x):
        i = lower_bound(self.macro, x)
        j = upper_bound(self.micros[i], x)
        self.micros[i].insert(j, x)
        self.size += 1
        self.micro_size[i] += 1
        self.fenwick.update(i, 1)
        if len(self.micros[i]) >= self.block_size:
            self.micros[i:i + 1] = self.micros[i][:self.block_size >> 1], self.micros[i][self.block_size >> 1:]
            self.micro_size[i:i + 1] = self.block_size >> 1, self.block_size >> 1
            self.fenwick = FenwickTree(self.micro_size)
            self.macro.insert(i, self.micros[i + 1][0])

    def pop(self, k=-1):
        i, j = self._find_kth(k)
        self.size -= 1
        self.micro_size[i] -= 1
        self.fenwick.update(i, -1)
        return self.micros[i].pop(j)

    def __getitem__(self, k):
        i, j = self._find_kth(k)
        return self.micros[i][j]

    def count(self, x):
        return self.upper_bound(x) - self.lower_bound(x)

    def __contains__(self, x):
        return self.count(x) > 0

    def lower_bound(self, x):
        i = lower_bound(self.macro, x)
        return self.fenwick(i) + lower_bound(self.micros[i], x)

    def upper_bound(self, x):
        i = upper_bound(self.macro, x)
        return self.fenwick(i) + upper_bound(self.micros[i], x)

    def _find_kth(self, k):
        return self.fenwick.find_kth(k + self.size if k < 0 else k)

    def __len__(self):
        return self.size

    def __iter__(self):
        return (x for micro in self.micros for x in micro)

    def __repr__(self):
        return str(list(self))


input = sys.stdin.readline
inf = 1 << 60
N, K = map(int, input().split())

arr = [tuple(map(int, input().split())) for _ in range(N)]
width = sum(i for i, _ in sorted(arr)[:K])

by_h = sorted(arr, key=lambda x: x[1], reverse=True)  # sort by height, descending
arr = SortedList(arr)
arr.insert((inf, inf))

best = inf
for i in range(N - K + 1):
    idx = arr.lower_bound(by_h[i])
    if idx >= K:
        best = min(best, (width - arr[K - 1][0] + by_h[i][0]) * by_h[i][1])
    else:
        best = min(best, width * by_h[i][1])
        width -= by_h[i][0]
        width += arr[K][0]
    arr.pop(idx)
print(best)

# # brute force code for reference
# N, K = map(int, input().split())
# arr = [tuple(map(int, input().split())) for _ in range(N)]
#
# arr.sort(key=lambda x: x[0])  # by width
# best = 1 << 60
# by_h = sorted(arr, key=lambda x: x[1], reverse=True)  # sort by height
#
# for i in range(N-K+1):
#     arr.remove(by_h[i])
#     best = min(best, (sum(i for i,_ in arr[:K-1])+by_h[i][0]) * by_h[i][1])
# print(best)
