"""
https://dmoj.ca/problem/dmopc15c6p3
Difference array + ((PSA + binary search) or (sliding window))

1. Use difference array and rebuild with PSA to get the number of potatoes remaining in each row
2. The problem now becomes, find the shortest length subarray with a sum of >=K (all values are non-negative)
    - approach: O(n), use sliding window (I will be using this method)
    - alternate approach: O(nlogn), make a PSA of rows and use binary search to find W
"""

from itertools import accumulate

N, M, K = map(int, input().split())

diff = [0] * (N + 2)
for _ in range(M):
    l, r = map(lambda x: int(x) - 1, input().split())
    diff[l] -= 1  # minus 1 from every row in [l, r]
    diff[r + 1] += 1
rows = list(accumulate(diff))
rows = list(map(lambda x: M + x, rows))  # the i-th row has rows[i] potatoes

shortest = 1 << 30
cur = 0  # current sum of [left, right]
left = 0
for right in range(N):
    cur += rows[right]
    while cur - rows[left] >= K:  # try to move left as much as possible
        cur -= rows[left]
        left += 1
    if cur >= K:  # current window has high enough sum
        shortest = min(shortest, right - left + 1)

if shortest == 1 << 30:
    print(-1)
else:
    print(shortest)
