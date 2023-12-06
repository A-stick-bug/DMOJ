# for question like these, you should validate your answer first before submitting and try a bunch of cases

dir = [(1, 2), (2, 1), (-1, 2), (2, -1), (1, -2), (-2, 1), (-1, -2), (-2, -1)]


def validate(arr):
    global used
    used = 0
    marked = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if arr[i][j]:
                used += 1
                for dr, dc in dir:
                    nr, nc = i + dr, j + dc
                    if 0 <= nr < n and 0 <= nc < n:
                        marked[nr][nc] = 1
                marked[i][j] = 1
    return sum(sum(row) for row in marked) == n * n


def solve():
    for i in range(2, n, 5):  # filling columns
        for j in range(n):
            arr[j][i] = 1
    if n % 5 == 2:  # last columns needs extra fill
        for j in range(n):
            arr[j][-1] = 1


def solve2():
    """solving with n%5 == 1 requires extra optimization"""
    for i in range(2, n, 5):  # filling columns
        for j in range(n):
            arr[j][i] = 1
    for i in range(1, n - 1, 4):
        arr[i][-3] = 1
        arr[i + 1][-3] = 1
    for i in range(1, 4):
        arr[-i][-3] = 1


n = int(input())

# for n in range(8, 1000):
arr = [[0] * n for _ in range(n)]
if n % 5 == 1:  # 11 special case
    solve2()
else:
    solve()

# print(n)

for row in arr:
    print(*row)
    # assert validate(arr)
    # assert used < (n*n+3*n)//2
