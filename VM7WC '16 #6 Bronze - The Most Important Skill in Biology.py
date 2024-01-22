# implementing a math formula

from math import ceil

n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
points = points[::-1]
points.append(points[0])

total = 0
for i in range(n):
    total += points[i][0] * points[i+1][1]
    total -= points[i][1] * points[i+1][0]

print(ceil(abs(total) / 2))
