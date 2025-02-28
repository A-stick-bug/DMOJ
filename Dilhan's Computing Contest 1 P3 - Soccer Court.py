# https://dmoj.ca/problem/dcc1p3
# Brute force vertical split lines
# 2D PSA + dict to find side that sums to 0
# TC: O(NM^2)

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

best = 0
for line in range(m - 1):  # [0, line], [line+1, m-1]
    sz = min(line + 1, (m - 1) - (line + 1) + 1)
    arr = [[0] * sz for _ in range(n)]
    for i in range(n):
        for sub in range(sz):  # merge left and right into 1
            arr[i][sub] = grid[i][line + 1 + sub] - grid[i][line - sub]

    # find rectangle that lines up against left wall and has sum of `0`
    # convert to 1-indexing
    for row in arr:
        row.insert(0, 0)
    arr.insert(0, [0] * (sz + 1))

    for j in range(1, sz + 1):  # find largest rectangle that sums to 0 for each column
        matching = {0: 0}
        for i in range(1, n + 1):
            arr[i][j] += arr[i - 1][j] + arr[i][j - 1] - arr[i - 1][j - 1]
            if arr[i][j] in matching:
                prev = matching[arr[i][j]]
                best = max(best, (i - prev) * j * 2)
            else:
                matching[arr[i][j]] = i

print(best)
