# https://dmoj.ca/problem/art1
# simple implementation

n = int(input())
arr = list(map(int, input().split()))
mx = max(arr)

grid = [[] for _ in range(mx)]

trees = []
for h in arr:
    res = [[" "] * (h * 2 - 1) for _ in range(mx)]
    for i in range(h):
        for j in range(i, 2 * h - i, 2):
            res[i][j] = "^"

    for row in range(mx):
        grid[row].append("".join(res[row]))

for i in reversed(grid):
    print(" ".join(i))
