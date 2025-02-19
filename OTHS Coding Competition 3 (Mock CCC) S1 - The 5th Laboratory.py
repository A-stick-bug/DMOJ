# https://dmoj.ca/problem/othscc3p1
# 3D math

from math import dist

x, y, z = map(int, input().split())
n = int(input())

best = float('inf')
for _ in range(n):
    a, b, c = map(int, input().split())
    if c <= z:  # climb then walk
        best = min(best, dist((x, y), (a, b)) / 2 + (z - c))

    elif c > z:
        diff_z = c - z
        diff_xy = dist((x, y), (a, b))

        glide_x = diff_z * 3 / 4
        if glide_x > diff_xy:
            best = min(best, diff_z / 4)
        else:
            diff_xy -= glide_x
            best = min(best, diff_xy / 2 + diff_z / 4)

print(best)
