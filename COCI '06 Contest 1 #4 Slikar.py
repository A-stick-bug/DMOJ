# https://dmoj.ca/problem/coci06c1p4
# 2 BFS, one keeping track of the water and one for the beavers
# water moves first, then the beavers, alternate after that

from collections import deque
import sys


def move_water():
    for _ in range(len(water)):
        r, c = water.popleft()
        for dr, dc in dir:
            nr = r + dr
            nc = c + dc
            if 0 <= nr < R and 0 <= nc < C and valid[nr][nc] and grid[nr][nc] != "D":  # destination can't get flooded
                valid[nr][nc] = False
                water.append((nr, nc))


R, C = map(int, input().split())
grid = [list(input()) for _ in range(R)]
valid = [[True] * C for _ in range(R)]  # cells that you can walk on
dir = [(0, 1), (1, 0), (-1, 0), (0, -1)]

water = deque()
q = deque()
for i in range(R):
    for j in range(C):
        if grid[i][j] == "*":  # water
            water.append((i, j))
            valid[i][j] = False
        elif grid[i][j] == "X":  # rock
            valid[i][j] = False
        elif grid[i][j] == "S":  # start
            q.append((0, i, j))
        elif grid[i][j] == "D":  # end
            goal = (i, j)

water_time = 0
while q:
    time, r, c = q.popleft()
    if time >= water_time:
        water_time += 1
        move_water()
    if (r, c) == goal:
        print(time)
        sys.exit()
    for dr, dc in dir:
        if 0 <= dr + r < R and 0 <= dc + c < C and valid[dr + r][dc + c]:
            q.append((time + 1, dr + r, dc + c))
            valid[dr + r][dc + c] = False

print("KAKTUS")
