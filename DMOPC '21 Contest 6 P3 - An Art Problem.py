# TLE, check c++ version for code that passes with exact same logic

# https://dmoj.ca/problem/dmopc21c6p3
# BFS flood fill, multiple starting points
# sort to start by filling with the smaller numbers

from collections import deque
import sys

input = sys.stdin.readline

ROWS, COLS, K = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(ROWS)]
dir = [(0, 1), (1, 0), (-1, 0), (0, -1)]

q = []
for i in range(ROWS):
    for j in range(COLS):
        if graph[i][j]:
            q.append((i, j, graph[i][j], 1))

q.sort(key=lambda x: x[2])
q = deque(q)
while q:
    row, col, color, time = q.popleft()
    if time > K:
        break
    for dr, dc in dir:
        new_r = row + dr
        new_c = col + dc
        if 0 <= new_r < ROWS and 0 <= new_c < COLS and not graph[new_r][new_c]:
            graph[new_r][new_c] = color
            q.append((new_r, new_c, color, time + 1))

for row in graph:
    print(*row)
