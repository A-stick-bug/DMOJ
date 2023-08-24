# https://dmoj.ca/problem/dmopc15c1p5
# Using 2D prefix sum and brute forcing

# find how many dragons can be collected from a rectangle of l*w by brute forcing
def max_dragon(l, w) -> int:
    res = 0
    for r1 in range(1, ROWS - l + 2):
        for c1 in range(1, COLS - w + 2):
            r2, c2 = r1 + l - 1, c1 + w - 1
            res = max(res, psa[r2][c2] - psa[r1 - 1][c2] - psa[r2][c1 - 1] + psa[r1 - 1][c1 - 1])
    return res


COLS, ROWS, N = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(ROWS)]

psa = [[0] * (COLS + 1) for _ in range(ROWS + 1)]  # rows and cols are shifted 1 right and down
for i in range(1, ROWS + 1):
    for j in range(1, COLS + 1):
        psa[i][j] = psa[i - 1][j] + psa[i][j - 1] + a[i - 1][j - 1] - psa[i - 1][j - 1]

res = 0
for l in range(1, N + 1):
    w = min(COLS, N // l)  # for each possible row length, use the maximum column length possible (no negative values)
    res = max(res, max_dragon(l, w))  # update max

print(res)
