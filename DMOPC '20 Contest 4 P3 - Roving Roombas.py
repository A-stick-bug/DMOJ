# https://dmoj.ca/problem/dmopc20c4p3
# Fenwick Tree with offline queries, same method used in https://dmoj.ca/problem/dmopc14c2p6
# also need coordinate compression on x coordinates

import sys


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


input = sys.stdin.readline
n, m = map(int, input().split())
roomba = [list(map(int, input().split())) for _ in range(n)]
coord = [list(map(int, input().split())) for _ in range(m)]

# coordinate compression
all_x = {x[0] for x in roomba}.union({x[0] for x in coord})
all_x = sorted(all_x)
compress_x = {all_x[i]: i + 1 for i in range(len(all_x))}

coord.sort(key=lambda x:x[1], reverse=True)  # sort by y in reverse
roomba.sort(key=lambda x:x[1], reverse=True)

total = 0
bit = FenwickTree(len(all_x))
c_i = 0  # index of next coord to add

for x,y in roomba:
    x = compress_x[x]
    while c_i < m and coord[c_i][1] >= y:  # add x coordinate since the y will be bigger than our next roomba queries
        bit.update(compress_x[coord[c_i][0]], 1)
        c_i += 1

    # query coords tripped, the sorting and above code makes sure all coords we query have a greater or equal y value
    total += bit.query(x)

print(total)
