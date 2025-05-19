# https://dmoj.ca/problem/scb24p5
# 2-way Dijkstra's
# Start from (1,1) and also start from (R,C)
# We can use these distances to compute the optimal row to mow

import sys
from heapq import heappop, heappush

inf = 1 << 60
input = sys.stdin.readline
R, C = map(int, input().split())

grid = [[inf] * (C + 2)] + [[inf] + list(map(int, input().split())) + [inf] for _ in range(R)] + [[inf] * (C + 2)]

dp = [[inf] * (C + 2) for _ in range(R + 2)]
dp2 = [[inf] * (C + 2) for _ in range(R + 2)]  # reversed
dp[1][1] = grid[1][1]
dp2[R][C] = grid[R][C]

pq = [(grid[1][1], 1, 1)]
while pq:
    d, r, c = heappop(pq)
    for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        nr, nc = r + dr, c + dc
        if 1 <= nr <= R and 1 <= nc <= C:
            nd = d + grid[nr][nc]
            if nd < dp[nr][nc]:
                dp[nr][nc] = nd
                heappush(pq, (nd, nr, nc))

pq = [(grid[R][C], R, C)]
while pq:
    d, r, c = heappop(pq)
    for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        nr, nc = r + dr, c + dc
        if 1 <= nr <= R and 1 <= nc <= C:
            nd = d + grid[nr][nc]
            if nd < dp2[nr][nc]:
                dp2[nr][nc] = nd
                heappush(pq, (nd, nr, nc))

best = 1 << 60
rows = []

dp[0] = [0] * (C + 2)
dp2[-1] = [0] * (C + 2)

for i in range(1, R + 1):
    cost = min(dp[i - 1][1:-1]) + min(dp2[i + 1][1:-1])
    if cost < best:
        rows = [i]
        best = cost
    elif cost == best:
        rows.append(i)

print(best, len(rows))
print(" ".join(map(str, rows)))
