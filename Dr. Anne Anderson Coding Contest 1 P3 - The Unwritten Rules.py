# https://dmoj.ca/problem/daacc1p3
# painful implementation and some math

import sys

N, m = map(int, input().split())
M = 2 * m

bus = []
cur = 1
for i in range(N):
    row1 = []
    for _ in range(m):
        row1.append(cur)
        cur += 1
    row2 = []
    for _ in range(m):
        row2.append(cur)
        cur += 1
    bus.append([row1, row2[::-1]])

ROWS = list(range(N))[::-1]

for _ in range(N * M):
    num = int(input())
    r = (num - 1) // M
    c = (num - 1) % M

    if c < m:  # left
        if ROWS[-1] != r or bus[r][0].pop() != num:
            print("no")
            sys.exit()
    else:
        if ROWS[-1] != r or bus[r][1].pop() != num:
            print("no")
            sys.exit()

    if not bus[r][0] and not bus[r][1]:
        ROWS.pop()

print("yes")
