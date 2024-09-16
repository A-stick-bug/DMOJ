# https://dmoj.ca/problem/bts24p3
# similarities with https://dmoj.ca/problem/cco13p2
# seg tree structure with swapping elements
# after a swap, at most log(n) nodes are touched

from math import log2, ceil


def update(i, val) -> None:
    """update i-th element to val, 0-indexed"""
    global underwhelm
    i += size  # start from bottom
    seg[i] = val
    while i > 1:
        i //= 2
        underwhelm += (seg[i * 2] - seg[i * 2 + 1]) ** 2
        underwhelm -= (prev[i * 2] - prev[i * 2 + 1]) ** 2

        seg[i] = max(seg[i * 2], seg[i * 2 + 1])
        prev[i * 2], prev[i * 2 + 1] = seg[i * 2], seg[i * 2 + 1]


N = int(input())
arr = list(map(int, input().split()))
missing = list(set(range(1, N + 1)).difference(set(arr)))[0]
arr.insert(0, missing)

ans = []

# tree
default = 0
layers = ceil(log2(N))  # max depth of the seg tree, root has depth 0
size = 1 << layers
seg = [default] * (2 * size)  # 1-indexed, need an extra layer for the actual data
underwhelm = 0

for i in range(N):  # base layer
    seg[size + i] = arr[i]
for i in reversed(range(1, size)):  # create other layers from base
    underwhelm += (seg[i * 2] - seg[i * 2 + 1]) ** 2
    seg[i] = max(seg[i * 2], seg[i * 2 + 1])

prev = seg.copy()

ans.append(underwhelm)
for i in range(N - 1):  # try inserting in i
    a, b = arr[i], arr[i + 1]
    update(i, b)
    update(i + 1, a)
    arr[i], arr[i + 1] = arr[i + 1], arr[i]
    ans.append(underwhelm)

print(" ".join(map(str, ans)))
