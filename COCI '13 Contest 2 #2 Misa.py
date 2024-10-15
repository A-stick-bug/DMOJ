import sys

dir_8 = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]


def count_adj(i, j, tt):
    if grid[i][j] == "." and tt == 0:
        return 0
    elif grid[i][j] == "o" and tt == 1:
        return 0
    t = 0
    for di, dj in dir_8:
        ni, nj = i + di, j + dj
        t += grid[ni][nj] == "o"
    return t


R, C = map(int, input().split())
grid = [['.'] * (C + 2)] + [list('.' + input() + '.') for _ in range(R)] + [['.'] * (C + 2)]

mx = max(count_adj(i, j, 1) for i in range(1, R + 1) for j in range(1, C + 1))
for i in range(1, R + 1):
    for j in range(1, C + 1):
        if count_adj(i, j, 1) == mx and grid[i][j] == ".":
            grid[i][j] = "o"

            print(sum(count_adj(i, j, 0) for i in range(1, R + 1) for j in range(1, C + 1)) // 2)
            sys.exit()
print(sum(count_adj(i, j, 0) for i in range(1, R + 1) for j in range(1, C + 1)) // 2)
