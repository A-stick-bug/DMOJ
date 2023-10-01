from collections import deque
import sys

ROWS, COLS = map(int, input().split())
dir_4 = [(1, 0), (0, 1), (-1, 0), (0, -1)]
grid = [list(input()) for _ in range(ROWS)]

# get start
for i in range(ROWS):
    for j in range(COLS):
        if grid[i][j] == "s":
            q = deque([(0, i, j)])
        elif grid[i][j] == "e":
            end = (i, j)

while q:
    dist, row, col = q.popleft()
    if (row, col) == end:
        print(dist - 1)  # question requires -1 for some reason
        sys.exit()

    for dr, dc in dir_4:
        new_r, new_c = row + dr, col + dc
        if 0 <= new_r < ROWS and 0 <= new_c < COLS and grid[new_r][new_c] != "X":
            grid[new_r][new_c] = "X"
            q.append((dist + 1, new_r, new_c))

print(-1)
