# using bitwise operators, MLE

n, m = map(int, input().split())
dif = [[False for _ in range(n + 2)] for _ in range(n + 2)]

for _ in range(m):
    c, r, w, h = map(int, input().split())
    r += 1
    c += 1
    dif[r][c] ^= True  # inverse bit, equivalent to not arr[y][x]
    dif[r][c + w] ^= True
    dif[r + h][c] ^= True
    dif[r + h][c + w] ^= True

count = 0
for i in range(1, n + 1):
    for j in range(1, n + 1):
        dif[i][j] ^= dif[i - 1][j] ^ dif[i][j - 1] ^ dif[i - 1][j - 1]
        count += dif[i][j]

print(count)
