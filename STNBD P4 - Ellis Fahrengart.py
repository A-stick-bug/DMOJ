# TLE, PYTHON IS TOO SLOW, CHECK C++ CODE
# https://dmoj.ca/problem/stnbd4
# - Mo's algorithm (sqrt decomp on queries)
# - Maintain a Fenwick Tree of the frequency of elements on the current range
#   to update inversion count in log(n)
#
# TC: O(N*sqrt(N)*log(N)), assuming N=Q

import sys


# point update, range query, uses 1-indexing
class FenwickTree:
    def __init__(self, size):
        """Create empty Fenwick Tree"""
        self.bit = [0] * (size + 1)

    def update(self, i: int, diff: int) -> None:
        """Add diff to self.bit[i]"""
        while i < len(self.bit):
            self.bit[i] += diff
            i += i & (-i)

    def query(self, i: int):
        """Get the sum up to the i-th element (inclusive)"""
        total = 0
        while i > 0:
            total += self.bit[i]
            i -= i & (-i)
        return total

    def query_range(self, left, right):
        """Query the sum of elements from left to right, inclusive"""
        return self.query(right) - self.query(left - 1)


input = sys.stdin.readline
SQRT = 70  # group size

N = int(input())
arr = list(map(int, input().split()))
ordered = sorted(set(arr))  # coordinate compress
compress = {ordered[i]: i + 1 for i in range(len(ordered))}
arr = list(map(lambda x: compress[x], arr))

Q = int(input())
queries = [list(map(int, input().split())) + [i] for i in range(Q)]
ans = [-1] * Q

# information on the current range
M = len(compress)
bit = FenwickTree(M)
inversions = 0

queries.sort()  # sort and group by left
prev_r = 0
prev_l = 1
for i in range(0, Q, SQRT):
    group = queries[i:i + SQRT]
    if i & 1 == 0:  # ascending/descending optimization
        group.sort(key=lambda x: x[1])  # sort individual group by right
    else:
        group.sort(key=lambda x: x[1], reverse=True)

    for l, r, idx in group:
        l -= 1  # 0-indexed
        r -= 1
        while prev_r < r:  # extend right side
            prev_r += 1
            bit.update(arr[prev_r], 1)
            inversions += bit.query_range(arr[prev_r] + 1, M)
        while prev_r > r:  # shrink right side
            bit.update(arr[prev_r], -1)
            inversions -= bit.query_range(arr[prev_r] + 1, M)
            prev_r -= 1
        while prev_l < l:  # shrink left side
            bit.update(arr[prev_l], -1)
            inversions -= bit.query(arr[prev_l] - 1)
            prev_l += 1
        while prev_l > l:  # extend left side
            prev_l -= 1
            bit.update(arr[prev_l], 1)
            inversions += bit.query(arr[prev_l] - 1)

        ans[idx] = inversions

print("\n".join(map(str, ans)))
