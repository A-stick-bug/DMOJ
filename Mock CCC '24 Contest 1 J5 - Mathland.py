# Simple BFS but the grid has 4 states, and you switch between them
# Because of this, we will need to multiply our distances array by 4

from collections import deque
import sys

n, k = map(int, input().split())
grid = [list(input()) for _ in range(n)]

deepcopy = lambda x: [i.copy() for i in x]
rot = lambda d: (d // k) % 4
dir = [(0, 1), (1, 0), (-1, 0), (0, -1)]

q = deque()

for i in range(n):
    for j in range(n):
        if grid[i][j] == "E":
            q.append((i, j, 0))  # (i, j, distance)

        if grid[i][j] == "W":  # obstacle
            grid[i][j] = False
        elif grid[i][j] == "P":
            grid[i][j] = True

state = []
for i in range(4):  # create 3 other rotated grids
    state.append(deepcopy(grid))
    grid = list(map(list, list(zip(*grid[::-1]))))  # rotate 90 degrees clockwise

dist = [[[[-1] * n for _ in range(n)] for _ in range(4)] for _ in range(10)]  # dist[k][rotation][i][j]
while q:
    r, c, d = q.popleft()
    if state[rot(d)][r][c] == "X":  # reached end
        print(d)
        sys.exit()

    for dr, dc in dir:
        nr, nc = r + dr, c + dc
        new_dist = d + 1
        new_rot = rot(new_dist)
        if 0 <= nr < n and 0 <= nc < n and state[new_rot][nr][nc] and dist[new_dist % k][new_rot][nr][nc] == -1:
            dist[new_dist % k][new_rot][nr][nc] = new_dist
            q.append((nr, nc, new_dist))

print(-1)

"""
SPECIAL CASE:
THIS IS WHY WE NEED AN EXTRA DIMENSION (FOR EACH K) IN THE DISTANCE ARRAY

6 4
EPPPPP
PPPPPP
PPPPPP
PPPPPP
PPPPPP
XPPPPP

Output: 4

basically u can use the following moves
move1: right
move2: left
move3: right
move4: left, the end gets rotated so you are now standing on the end 

"""
