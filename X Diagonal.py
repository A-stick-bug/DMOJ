# https://dmoj.ca/problem/xdiagonal
# First problem that I created
# intended solution: calculate intersection using algebra, parity checks also work

def intersect(a, b):
    """
    :param a: y = x + a (/ diagonal)
    :param b: y = -x + b (\ diagonal)
    :return: (x,y): the point of intersection
    """
    x = (b - a) // 2
    if x == (b - a) / 2:  # is on a lattice point
        y = x + a
        assert x + a == b - x  # make sure they actually intersect
        if (1 <= x <= n) and (n <= y < 2 * n):  # intersects within the matrix
            return x, y
    return -1, -1  # not a valid intersection point, the value at mat[0][0] is always 0


n = int(input())
nums = [list(map(int, input().split())) for _ in range(n)]

size = n * 2 - 1
diagonals = [0] * size

for i in range(n):
    for j in range(n):
        diagonals[i + j] += nums[i][j]

diagonals2 = [0] * size
for i in range(n):
    for j in range(n):
        if i < j:
            diagonals2[i - j + size] += nums[i][j]
        else:
            diagonals2[i - j] += nums[i][j]

diagonals = list(reversed(diagonals))  # matches y=intercept, y=x+a
diagonals2[:n] = list(reversed(diagonals2[:n]))
diagonals2[n:] = list(reversed(diagonals2[n:]))

best = 0
for i in range(size):
    for j in range(size):
        x, y = intersect(i, j + n + 1)
        cur = diagonals[i] + diagonals2[j]
        if x != -1:  # minus intersection
            cur -= nums[n - (y - n) - 1][x - 1]
        best = max(best, cur)

print(best)
