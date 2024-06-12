# https://dmoj.ca/problem/dmopc20c5p2
# simple logic and math (finding intersections)

import sys


def intersects(a, b):
    p = [b[0][0] - a[0][0], b[0][1] - a[0][1]]
    q = [a[1][0] - a[0][0], a[1][1] - a[0][1]]
    r = [b[1][0] - b[0][0], b[1][1] - b[0][1]]

    t = (q[1] * p[0] - q[0] * p[1]) / (q[0] * r[1] - q[1] * r[0]) \
        if (q[0] * r[1] - q[1] * r[0]) != 0 \
        else (q[1] * p[0] - q[0] * p[1])
    u = (p[0] + t * r[0]) / q[0] \
        if q[0] != 0 \
        else (p[1] + t * r[1]) / q[1]

    return 0 <= t <= 1 and 0 <= u <= 1


print_pair = lambda x, y: sys.stdout.write(str(x) + " " + str(y) + "\n")
N, M = map(int, input().split())

diagonal = (0, 0), (N, M)
i = j = 1
res = []
while i <= N and j <= M:
    res.append((i, j))
    right_line = (i, j), (i - 1, j)
    top_line = (i, j), (i, j - 1)

    rt = intersects(diagonal, right_line)
    tt = intersects(diagonal, top_line)
    if rt and tt:  # line touches the tip
        i += 1
        j += 1
    elif rt:  # line touches right side
        j += 1
    else:  # line touches top side
        i += 1

print(len(res))
for i, j in res:
    print_pair(i, j)
