rows, cols = map(int, input().split())

grid = [list(input()) for _ in range(rows)]
dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
for i in range(rows):
    for j in range(cols):
        if grid[i][j] == "W":
            for dr, dc in dirs:
                ii = i + dr
                jj = j + dc
                if 0 <= ii < rows and 0 <= jj < cols and grid[ii][jj] == ".":
                    grid[ii][jj] = "C"

for row in grid:
    print(*row, sep="")
