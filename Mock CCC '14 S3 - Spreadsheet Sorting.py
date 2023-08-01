# simple sorting and use of 'key=' in the sort() function

rows, cols = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(rows)]

n = int(input())
for _ in range(n):
    col = int(input())
    grid.sort(key=lambda x: x[col - 1])  # sort by column, -1 because the question uses 1-indexing

for r in grid:
    print(*r)  # split using spaces
