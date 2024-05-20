# https://dmoj.ca/problem/dmopc19c6p3
# Note that the queries only increase the number of set bits (decrease number of unset)
# We just store the unset bits in a SortedList and remove them when doing updates
# We can use binary search on the SortedList to find the unset bits in [l,r]
#
# TC: N*log^2(n), in practice it's not too slow since the SortedList only gets smaller
# Note:
# - the time limit is quite generous, so I can just use pow() and not precompute powers
# - the SortedList is equivalent to a C++ set

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
print = lambda x: sys.stdout.write(str(x) + "\n")
MOD = 10 ** 9 + 7

N, Q = map(int, input().split())
arr = list(map(int, input().strip()))

total = 0
for i in range(N):  # current value in base 10
    if arr[i]:
        total += pow(2, N - i - 1, MOD)

zeros = SortedList([i for i in range(N) if arr[i] == 0])  # index of unset bits
for _ in range(Q):
    l, r = map(lambda x: int(x) - 1, input().split())  # convert to 0-indexing
    l_idx = zeros.lower_bound(l)
    r_idx = zeros.upper_bound(r)
    for _ in range(r_idx - l_idx):  # remove zeros[l_idx, r_idx) and add their corresponding value
        total += pow(2, N - zeros[l_idx] - 1, MOD)
        total %= MOD
        zeros.pop(l_idx)

    print(total)
