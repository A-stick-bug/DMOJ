# simple logic and thinking

N,K = map(int, input().split())
arr = [[0] * N for _ in range(N)]

num = N*N
for i in range(K):
    arr[i][i] = num
    num -= 1

for i in range(1,N):  # first col
    arr[i][0] = num
    num -= 1

for j in range(1, N):  # first row
    arr[0][j] = num
    num -= 1

for i in range(N):
    for j in range(N):
        if not arr[i][j]:
            arr[i][j] = num
            num -= 1

for row in arr:
    print(*row)
