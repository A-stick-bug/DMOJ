N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

total = [0] * M

for i in range(N):
    for j in range(M):
        total[j] += grid[i][j]

total = [(val, i) for i, val in enumerate(total)]
total.sort(key=lambda x: (-x[0], x[1]))

print(*[j + 1 for i, j in total])
