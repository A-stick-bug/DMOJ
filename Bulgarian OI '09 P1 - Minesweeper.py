# https://dmoj.ca/problem/bgoi09p1
# Standard convex hull + math observation
# Same as https://dmoj.ca/problem/cco99p4
# TC: O(nlogn)

from fractions import Fraction
from math import pi

inf = 1 << 30


def slope(p1, p2):  # todo: use cross multiplication to compare slopes
    dy = (p2[1] - p1[1])
    dx = (p2[0] - p1[0])
    if dx == 0:  # temporary fix, assumes duplicate points have slope -inf between them
        return inf if dy > 0 else -inf
    return Fraction(dy, dx)


def dist(p1, p2):
    return ((p2[1] - p1[1]) ** 2 + (p2[0] - p1[0]) ** 2) ** 0.5


n, radius = map(int, input().split())
arr = [tuple(map(int, input().split())) for _ in range(n)]  # (x,y)

arr.sort()

# solve upper hull
hull1 = []  # index of hull points
for cur in arr:
    while len(hull1) >= 2 and slope(hull1[-2], cur) <= slope(hull1[-1], cur):
        hull1.pop()
    hull1.append(cur)

# solve lower hull
hull2 = []
# arr = sorted(arr, key=lambda x: (x[0], x[1]))
for cur in arr:
    while len(hull2) >= 2 and slope(hull2[-2], cur) >= slope(hull2[-1], cur):
        hull2.pop()
    hull2.append(cur)

hull = hull1 + hull2[::-1]

# print(hull)

total = sum(dist(hull[i], hull[i - 1]) for i in range(1, len(hull)))
total += 2 * pi * radius

print(total)
