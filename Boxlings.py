# https://dmoj.ca/problem/boxl
# line sweep using Fenwick Tree for range update and point query
# for every rectangle's start/end, process all points to the left and update with Fenwick tree

import sys


class FenwickTree2:  # 1-indexed (range update, point query)
    def __init__(self, n):
        self.bit = [0] * (n + 1)

    def add(self, i, val):
        while i < len(self.bit):
            self.bit[i] += val
            i += i & -i

    def update(self, l, r, diff):
        """range update [l, r] by difference"""
        self.add(l, diff)
        self.add(r + 1, -diff)

    def query(self, i):
        """ get the value at the i-th element"""
        ret = 0
        while i > 0:
            ret += self.bit[i]
            i -= i & -i
        return ret


input = sys.stdin.readline
N, M = map(int, input().split())

rects = []
py = set()  # contains every y coordinate used
for _ in range(N):
    x1, y1, x2, y2 = map(int, input().split())
    py.add(y1)
    py.add(y2)
    rects.append((x1, y1, y2, 1))
    rects.append((x2 + 1, y1, y2, -1))  # +1 since the rectangle covers inclusive area

points = [tuple(map(int, input().split())) for _ in range(M)]
py.update(tuple(map(lambda x: x[1], points)))  # add y-coordinates of points

rects.sort(key=lambda x: x[0])  # sort by x for vertical line sweep
points.sort(key=lambda x: x[0])

py = sorted(py)
compress = {py[i]: i + 1 for i in range(len(py))}  # coordinate compression

bit = FenwickTree2(len(py) + 1)
i = 0  # current point
total = 0

for x, y1, y2, diff in rects:
    while i < M and points[i][0] < x:  # process everything before current line
        if bit.query(compress[points[i][1]]):  # check if y is covered
            total += 1
        i += 1

    cy1, cy2 = compress[y1], compress[y2]
    bit.update(cy1, cy2, diff)

print(total)
