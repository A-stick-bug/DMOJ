# https://dmoj.ca/problem/mcco19c1d2p3
# Similar to convex hull, print line segments that are the maximum at some point

def intersect(l1, l2):
    a, b = l1
    c, d = l2  # ax + b = cx + d
    x_int = (d - b) / (a - c)  # slope must not be equal
    return x_int


inf = 1 << 60
n = int(input())
arr = [tuple(map(int, input().split())) + (i + 1,) for i in range(n)]  # (slope, y-int, id)

# U-shaped hull, ignore parallel lines except for top one
arr.sort(key=lambda x: (x[0], -x[1]))

prev = arr[0][0]
hull = [(0, -inf)]  # (line index `i`, is maximum starting from `x`)
for i in range(1, n):
    a, b, _ = arr[i]
    if a == prev:  # parallel to previous, ignore
        continue

    while intersect((a, b), arr[hull[-1][0]][:2]) <= hull[-1][1]:
        hull.pop()
    intersection = intersect((a, b), arr[hull[-1][0]][:2])
    hull.append((i, intersection))
    prev = a

# print(hull)

ans = sorted(arr[i][2] for i, _ in hull)  # id of lines
print(" ".join(map(str, ans)))
