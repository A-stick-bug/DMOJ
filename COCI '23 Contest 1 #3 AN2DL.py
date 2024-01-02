# TLE, PYTHON IS TOO SLOW, CHECK C++ CODE
# https://dmoj.ca/problem/coci23c1p3
# create N monotonic queues for each row
# we can shift the columns in O(1)
# we can also get the max from the rows in O(n)
#
# mostly implementation

from collections import deque
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
r, c = map(int, input().split())


def fill_start(row):
    """beginning state of queues for each column"""
    q = deque()
    for i, v in enumerate(row[:c]):
        while q and row[q[-1]] <= v:
            q.pop()
        q.append(i)
    return q


def solve_col(max_i):
    """solves an entire column, given the max in each grid[r][col] for all r"""
    max_vals = [grid[rr][i] for rr, i in enumerate(max_i)]
    q = deque()
    res = [0] * (N - r + 1)
    for i, v in enumerate(max_vals):
        left = i - r + 1
        while q and max_vals[q[-1]] <= v:
            q.pop()
        q.append(i)

        if left >= 0:  # full window, start filling values
            res[left] = max_vals[q[0]]

        if q[0] == left:  # left side exits window
            q.popleft()

    return res


# fill up starting state of column queues
maxs = [fill_start(grid[i]) for i in range(N)]  # deques are decreasing as we want to get the largest element

total_res = []
total_res.append(solve_col(list(map(lambda q: q[0], maxs))))

for j in range(c, M):
    for i in range(N):  # shift each col queue forward by 1
        row = grid[i]
        q = maxs[i]
        if q[0] == j - c:  # left element exits
            q.popleft()

        while q and grid[i][j] >= row[q[-1]]:
            q.pop()
        q.append(j)

    total_res.append(solve_col(list(map(lambda q: q[0], maxs))))  # get the rows max based on columns max

for i in list(zip(*total_res)):  # row <-> col
    print(" ".join(map(str, i)))
