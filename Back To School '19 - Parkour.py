# https://dmoj.ca/problem/bts19p2
# Math observation and line intersections
# Note: this code can probably be optimized to log(n) or even O(1)

import sys


# thanks to stack overflow: https://stackoverflow.com/questions/3838329/how-can-i-check-if-two-segments-intersect
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


X, Y, H, V = map(int, input().split())
max_time = int(input())

# lines between 4 corners of the school
a, b, c, d = [(X, Y), (X, Y + V - 1), (X + H - 1, Y), (X + H - 1, Y + V - 1)]
bounds = [(a, b), (a, c), (d, b), (d, c)]

for t in range(1, max_time):
    top = (t, 2 * t)
    bottom = (2 * t, t)
    diagonal = (top, bottom)
    if any(intersects(diagonal, bound_line) for bound_line in bounds):
        print("YES")
        sys.exit()
print("NO")
