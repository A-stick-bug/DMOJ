# https://dmoj.ca/problem/scb24p4
# Check C++ code for explanations

import sys

input = sys.stdin.readline
exp = 1 << 12
n, m, k = map(int, input().split())
cnt = [0] * (exp)
for _ in range(n):
    cnt[int(input(), 2)] += 1

best = 0
for ans in range(exp):
    cur = 0
    for mask in range(exp):
        if (ans ^ mask).bit_count() <= m - k:
            cur += cnt[mask]
    best = max(best, cur)
print(best)
