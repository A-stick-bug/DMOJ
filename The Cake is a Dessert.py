# https://dmoj.ca/problem/cake
# first use a 2D difference array for O(1) range update
# then, convert to a 2D PSA for O(1) range query

ROWS, COLS, K = map(int, input().split())
diff = [[0] * (COLS + 2) for _ in range(ROWS + 2)]

for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    diff[x1 - 1][y1 - 1] += 1
    diff[x2][y2] += 1
    diff[x2][y1 - 1] -= 1
    diff[x1 - 1][y2] -= 1

# convert to regular array
arr = [[0] * (COLS + 1) for _ in range(ROWS + 1)]
for i in range(ROWS):
    for j in range(COLS):
        arr[i + 1][j + 1] = arr[i + 1][j] + arr[i][j + 1] + diff[i][j] - arr[i][j]

# convert to PSA
psa = [[0] * (COLS + 1) for _ in range(ROWS + 1)]
for i in range(1, ROWS+1):
    for j in range(1, COLS+1):
        psa[i][j] = psa[i-1][j] + psa[i][j-1] + arr[i][j] - psa[i-1][j-1]

Q = int(input())
for _ in range(Q):
    x1, y1, x2, y2 = map(int, input().split())
    print(psa[x2][y2] - psa[x1-1][y2] - psa[x2][y1-1] + psa[x1-1][y1-1])

