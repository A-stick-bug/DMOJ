# template BFS traversal in a grid, while keeping track of distance

from collections import deque
import sys

input = sys.stdin.readline

dir_4 = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def dist(rs, cs, re, ce):  # regular bfs
    q = deque([(rs, cs, 0)])
    vis = [[False] * COLS for _ in range(ROWS)]
    vis[rs][cs] = True

    while q:
        row, col, dist = q.popleft()
        if row == re and col == ce:
            return dist
        for dr, dc in dir_4:
            new_r = row + dr
            new_c = col + dc
            if 0 <= new_r < ROWS and 0 <= new_c < COLS and not vis[new_r][new_c] and graph[new_r][new_c] != "X":
                vis[new_r][new_c] = True
                q.append((new_r, new_c, dist + 1))
    return 1000  # infinity


for _ in range(int(input())):  # for each test case
    COLS, ROWS = map(int, input().split())
    graph = [list(input().strip()) for _ in range(ROWS)]
    for i in range(ROWS):
        for j in range(COLS):
            if graph[i][j] == "C":
                a, b = i, j
            elif graph[i][j] == "W":
                c, d = i, j

    d = dist(a, b, c, d)
    print(d if d < 60 else "#notworth")
