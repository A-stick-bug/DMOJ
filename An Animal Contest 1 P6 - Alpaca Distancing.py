# https://dmoj.ca/problem/aac1p6
# take or don't take DP with data structures (fun!)
#
# similar to LIS, we can use a Fenwick Tree to get the best previous best answer
# unlike LIS DP, we don't add the current item as an option right away, instead we wait for the next
# item's location to get out of the current one's radius (we can do this quickly with a heap)

import sys
from heapq import heappush, heappop


class MaxFenwickTree:  # uses 1-indexing
    def __init__(self, size):
        """Create empty Fenwick Tree"""
        self.bit = [0] * (size + 1)

    def update(self, i: int, val: int) -> None:
        """Set self.bit[i] to val"""
        while i < len(self.bit):
            self.bit[i] = max(self.bit[i], val)
            i += i & (-i)

    def query(self, i: int):
        """Get the sum up to the i-th element (inclusive)"""
        total = 0
        while i > 0:
            total = max(total, self.bit[i])
            i -= i & (-i)
        return total


input = sys.stdin.readline
n = int(input())
arr = [tuple(map(int, input().split())) for _ in range(n)]
arr.sort()

# coordinate compression, add all necessary points
ordered = []
for loc, r in arr:
    ordered.append(loc)
    ordered.append(loc - r)
    ordered.append(loc + r)
ordered = sorted(set(ordered))
compress = {ordered[i]: i + 1 for i in range(len(ordered))}

bit = MaxFenwickTree(len(ordered))
pending = []  # (when to add, place to add at, value to add)

for loc, dist in arr:
    while pending and compress[loc] >= pending[0][0]:  # current location exited the previous one's radius
        bit.update(pending[0][1], pending[0][2])
        heappop(pending)

    prev = compress[loc - dist]
    best = bit.query(prev)  # get previous best
    heappush(pending, (compress[loc + dist], compress[loc], best + 1))  # don't add current one right away

# add leftover items
while pending:
    bit.update(pending[0][1], pending[0][2])
    heappop(pending)
print(bit.query(len(ordered)))

"""
4
1 2
3 2
5 3
5 2

Output: 3
"""
