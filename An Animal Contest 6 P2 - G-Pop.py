# TLE in python, check C++ code
#
# https://dmoj.ca/problem/aac6p2
# Line sweep with Fenwick Tree to maintain MEX

import sys


class OrderStatisticsTree:
    def __init__(self, nums: list[int]):
        self.size = len(nums)
        psa = [0] * (len(nums) + 1)
        for i in range(1, len(nums) + 1):
            psa[i] = psa[i - 1] + nums[i - 1]
        self.tree = [0] * (len(nums) + 1)
        for i in range(1, len(nums) + 1):
            self.tree[i] = psa[i] - psa[i - (i & -i)]

    def update(self, i, diff):
        while i <= self.size:
            self.tree[i] += diff
            i += i & -i

    def p_query(self, i):
        res = 0
        while i:
            res += self.tree[i]
            i -= i & (-i)
        return res

    def query(self, l, r):
        return self.p_query(r) - self.p_query(l - 1)

    def select(self, k):  # get k-th smallest element
        i = 0
        bl = self.size.bit_length()
        for p in range(bl, -1, -1):
            if i + (1 << p) <= self.size and self.tree[i + (1 << p)] < k:
                i += 1 << p
                k -= self.tree[i]
        return i + 1


input = sys.stdin.readline
N, Q = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(Q)]
events = []
for l, r in arr:
    events.append((l, l, 1))
    events.append((r + 1, l, -1))
events.sort()

res = [1] * (N + 1)
cur = OrderStatisticsTree([1] * N)
restrict = OrderStatisticsTree([0] * N)

idx = 0
for i in range(1, N + 1):
    while idx < len(events) and events[idx][0] == i:
        time, prev, t = events[idx]
        idx += 1
        if t == 1:  # start restriction
            restrict.update(i, 1)
        else:  # end restriction
            if restrict.select(1) == prev:
                end_r = min(i, restrict.select(2)) if restrict.p_query(N) > 1 else i
                for j in range(restrict.select(1), end_r):
                    if cur.query(res[j], res[j]) == 0:
                        cur.update(res[j], 1)

            restrict.update(prev, -1)

    choice = res[i - 1] if (i != 0 and cur.query(res[i - 1], res[i - 1])) else cur.select(1)
    if restrict.p_query(N):
        cur.update(choice, -1)
    res[i] = choice

print(max(res))
print(" ".join(map(str, res[1:])))

"""
12 5
1 3
5 6
3 8
8 10
11 12

10 2
1 3
6 7

"""
