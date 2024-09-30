# https://dmoj.ca/problem/dmopc21c7p1
# greedy: fill each cell with the minimum value possible
# compare with cell on top and to the left, similar to DP

import sys

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

if grid[0][0] == 0:  # only positive allowed
    grid[0][0] = 1

for i in range(N):
    for j in range(M):
        if i == 0 and j == 0:
            continue
        elif i == 0:
            mi = grid[i][j - 1] + 1
        elif j == 0:
            mi = grid[i - 1][j] + 1
        else:
            mi = max(grid[i - 1][j], grid[i][j - 1]) + 1
        if grid[i][j] != 0:
            if grid[i][j] < mi:
                print(-1)
                sys.exit()
        else:
            grid[i][j] = mi

for row in grid:
    print(" ".join(map(str, row)))
