"""
https://dmoj.ca/problem/bfs17p6

Related problems (recommended to do these first)
- (15p) DPQ: https://dmoj.ca/problem/dpq
- (~12p) LC 354: https://leetcode.com/problems/russian-doll-envelopes/

1. IMPORTANT: Make the length always >= than the width
2. sort everything by height to get reduce from 3D to 2D LIS problem, similar to LC 354
3. use a Fenwick tree, similar to DPQ, but 2D to get the best option we can stack the current block on

Note: this problem requires NON-DECREASING order, so you can have equal heights
"""

import sys


class MAX_BIT_2D:  # 1-indexed
    def __init__(self, r, c):
        self.M, self.N = r, c
        self.BIT = [[(0, 0)] * (self.N + 1) for _ in range(self.M + 1)]  # 1-indexed

    def update(self, row, col, val):
        """change index (row, col) to val"""
        while row <= self.M:
            c = col
            while c <= self.N:
                self.BIT[row][c] = max(val, self.BIT[row][c])
                c += c & (-c)
            row += row & (-row)

    def query(self, row, col):
        """get max of numbers from (1,1) to (row,col)"""
        res = (0, 0)
        while row:
            c = col
            while c:
                res = max(res, self.BIT[row][c])
                c -= c & (-c)
            row -= row & (-row)
        return res


input = sys.stdin.readline
MN = 5001

n = int(input())

# (length, width, height, people, index)
arr = [list(map(int, input().split())) + [i + 1] for i in range(n)]  # keep track of indices to restore LIS
for i in range(n):  # swap length and width if width > length
    arr[i][0], arr[i][1] = max(arr[i][0], arr[i][1]), min(arr[i][0], arr[i][1])

bit = MAX_BIT_2D(MN, MN)
arr.sort(key=lambda x: (x[2], x[0], x[1]))  # sort by height, length, and width
prev = [0] * (n + 1)

# find the LIS based on length and width
for l, w, _, ppl, i in arr:
    prev_best, prev_i = bit.query(l, w)  # find best option for the layer below
    bit.update(l, w, (prev_best + ppl, i))  # add current block
    prev[i] = prev_i  # keep track of previous term in sequence

fit_ppl, block_i = bit.query(MN, MN)  # get longest sequence
res = []
while block_i != 0:  # restore sequence to output it
    res.append(block_i)
    block_i = prev[block_i]

print(fit_ppl)
print(len(res))
print(" ".join(map(str, res)))
