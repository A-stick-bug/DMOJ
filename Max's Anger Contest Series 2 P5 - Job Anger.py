# https://dmoj.ca/problem/macs2p5
# - sort by x
# - vertical line sweep from left to right
# - before processing each vertical line, update everything up to its x coordinate
# - Fenwick Tree for getting the number of intersections the current vertical line makes

import sys


# point update, range query
class FenwickTree:  # uses 1-indexing
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
n = int(input())
lines = [tuple(map(int, input().split())) for _ in range(n)]

# coordinate compression
py = set(line[1] for line in lines).union(set(line[3] for line in lines))
py = sorted(py)
compress = {py[i]: i + 1 for i in range(len(py))}

v_lines = []  # vertical lines, sweep at these lines
h_lines = []  # horizontal lines, we do point updates at their start and end
for x1, y1, x2, y2 in lines:
    if x1 == x2:
        v_lines.append((x1, y1, y2))
    else:
        h_lines.append((x1, y1, 1))  # similar to difference array
        h_lines.append((x2 + 1, y1, -1))  # +1 because lines covers inclusive range

v_lines.sort(key=lambda x: x[0])  # sort by x to sweep from left to right
h_lines.sort(key=lambda x: x[0])

total = 0
bit = FenwickTree(len(py))
i = 0
for x, y1, y2 in v_lines:  # line sweep
    while i < len(h_lines) and h_lines[i][0] <= x:  # update events up to current line
        bit.update(compress[h_lines[i][1]], h_lines[i][2])
        i += 1

    total += bit.query_range(compress[y1], compress[y2])

print(total)
