N, M = map(int, input().split())
grid = [[0] * M for _ in range(N)]

if M == 1:
    for i in range(N):
        grid[i][0] = i % 2 + 1
else:
    for i in range(N):
        if i % 2 == 0:
            for j in range(0, M, 2):
                grid[i][j] = 1
            for j in range(1, M, 2):
                grid[i][j] = 2
        else:
            for j in range(0, M, 2):
                grid[i][j] = 3
            for j in range(1, M, 2):
                grid[i][j] = 4

print(max(max(row) for row in grid))
for row in grid:
    print(" ".join(map(str, row)))
