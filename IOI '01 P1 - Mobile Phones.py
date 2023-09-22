"""
https://dmoj.ca/problem/ioi01p1
You can only submit this in c++ (check the other file)
python instantly MLEs

2D Fenwick tree with basic query and update operations
- queries are 0-indexed, change to 1-indexing

"""


class BIT_2D:  # uses 1-indexing
    def __init__(self, r, c):
        self.ROWS = r
        self.COLS = c
        self.bit = [[0] * (c + 1) for _ in range(r + 1)]

    def update(self, r, c, diff):
        while r <= self.ROWS:
            col = c
            while col <= self.COLS:
                self.bit[r][col] += diff
                col += col & (-col)
            r += r & (-r)

    def query(self, r, c):
        total = 0
        while r > 0:
            col = c
            while col > 0:
                total += self.bit[r][col]
                col -= col & (-col)
            r -= r & (-r)
        return total

    def query_range(self, r1, c1, r2, c2):
        return self.query(r2, c2) + \
            self.query(r1 - 1, c1 - 1) - \
            self.query(r1 - 1, c2) - \
            self.query(r2, c1 - 1)


_, N = map(int, input().split())
bit = BIT_2D(N, N)

while True:
    q = list(map(int, input().split()))
    if q[0] == 3:
        break

    if q[0] == 1:  # update operation
        r, c, diff = q[1:]
        bit.update(r + 1, c + 1, diff)

    elif q[0] == 2:
        r1, c1, r2, c2 = q[1:]
        print(bit.query_range(r1 + 1, c1 + 1, r2 + 1, c2 + 1))
