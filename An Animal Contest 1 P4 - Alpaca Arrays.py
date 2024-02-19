# https://dmoj.ca/problem/aac1p4
# uses some math (factoring)
# then, it's just range frequency queries (we can use binary search and dict)

from collections import defaultdict
from bisect import bisect_left, bisect_right
import sys


def factors(num):
    res = []
    for i in range(1, int(num ** 0.5) + 1):  # note: we ignore perfect squares here since they must be distinct
        if num % i == 0:
            res.append((i, num // i))
    return res


input = sys.stdin.readline
N, Q = map(int, input().split())
arr = list(map(int, input().split()))

freq = defaultdict(list)
for i, val in enumerate(arr):
    freq[val].append(i)
query = lambda val, l, r: 0 if val not in freq else bisect_right(freq[val], r) - bisect_left(freq[val], l)

for _ in range(Q):
    l, r, val = map(int, input().split())
    l -= 1
    r -= 1
    found = False
    for a, b in factors(val):
        if a != b and query(a, l, r) > 0 and query(b, l, r) > 0:
            found = True
            break

    if found:
        print("YES")
    else:
        print("NO")
