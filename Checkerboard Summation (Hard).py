"""
https://dmoj.ca/problem/checkerhard
Simpler problem using 2D prefix sums here: https://dmoj.ca/problem/checkereasy

(Queries are 1-indexed)

The parity of (row + col) determines whether it is on a white or black tile
- white: add value
- black: minus value

"""

import sys

input = sys.stdin.readline


class BIT_2D(object):
    def __init__(self, r, c):
        self.M, self.N = r, c
        self.mat = [[0] * self.N for _ in range(self.M)]  # 0-indexed
        self.BIT = [[0] * (self.N + 1) for _ in range(self.M + 1)]  # 1-indexed

    def update(self, row, col, val):
        """change (row, col) to val"""
        diff = val - self.mat[row - 1][col - 1]
        self.mat[row - 1][col - 1] = val
        while row <= self.M:
            c = col
            while c <= self.N:
                self.BIT[row][c] += diff
                c += c & (-c)
            row += row & (-row)

    def query(self, row, col):
        res = 0
        while row:
            c = col
            while c:
                res += self.BIT[row][c]
                c -= c & (-c)
            row -= row & (-row)
        return res

    def query_range(self, row1, col1, row2, col2):
        # query in the same way as 2D prefix sum
        return self.query(row2, col2) + \
            self.query(row1 - 1, col1 - 1) - \
            self.query(row1 - 1, col2) - \
            self.query(row2, col1 - 1)


ROWS, COLS = map(int, input().split())
bit = BIT_2D(ROWS, COLS)

while True:
    query = list(map(int, input().split()))
    if query[0] == 0:
        break

    elif query[0] == 1:
        r, c, val = query[1:]
        if (r + c) % 2 == 1:  # odd cells are negative
            val = -val
        bit.update(r, c, val)

    else:
        r1, c1, r2, c2 = query[1:]
        total = bit.query_range(r1, c1, r2, c2)
        if (r1 + c1) % 2 == 1:  # if the first cell is odd, we take the negative value
            total = -total
        print(total)
