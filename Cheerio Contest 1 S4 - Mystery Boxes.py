# TLE, CHECK C++ CODE FOR EXPLANATIONS AS WELL

from functools import cache
from bisect import bisect_left
import sys

sys.setrecursionlimit(200000)
N, M = map(int, input().split())
arr = list(map(int, input().split()))

locs = [[] for _ in range(M + 1)]
for i, v in enumerate(arr):
    locs[v].append(i)
inf = 1 << 50
cache = [-1] * N


def solve(idx):  # current location
    if cache[idx] != -1:
        return cache[idx]
    if arr[idx] == M:
        return 0
    nxt = arr[idx] + 1
    mid = bisect_left(locs[nxt], idx)
    if mid >= len(locs[nxt]):
        right = inf
        left = locs[nxt][mid - 1]
    else:
        right = locs[nxt][mid]
        left = locs[nxt][mid - 1]
    ans = inf
    if 0 <= left < N:
        ans = min(ans, solve(left) + abs(idx - left))
    if 0 <= right < N:
        ans = min(ans, solve(right) + abs(idx - right))

    cache[idx] = ans
    return cache[idx]


start = locs[1][0]
print(start + solve(start) + 1)
