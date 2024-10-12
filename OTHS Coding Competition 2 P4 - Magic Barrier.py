# https://dmoj.ca/problem/othscc2p4
# Precomputation and using dict
# Explanation found here: https://dmoj.ca/problem/othscc2p4/editorial
#
# Precompute: store the (row, col) coordinate for every value in a dict
# Query: access the (row, col) coordinate in O(1) and check if it's in the query range
#
# TC: O(NM + Q)

import sys

input = sys.stdin.readline  # fast input
N, M, Q = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

loc = {}
for i in range(N):  # store the location (r,c) of each value, 1-indexed
    for j in range(M):
        loc[grid[i][j]] = (i + 1, j + 1)  # +1 to account for 1-indexing

for _ in range(Q):
    k, r1, c1, r2, c2 = map(int, input().split())
    if k not in loc:  # value is not in grid
        print("no")
        continue
    r, c = loc[k]
    if r1 <= r <= r2 and c1 <= c <= c2:  # check if value is in range
        print("yes")
    else:
        print("no")
