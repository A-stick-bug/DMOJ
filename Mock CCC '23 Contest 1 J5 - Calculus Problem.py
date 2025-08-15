# https://dmoj.ca/problem/mccc5j5
# Step by step iteration of bits + range query
# For each query, we find the valid `i`s and optimize with a segment tree
#
# TC: O(N + Q * log(m) * log(N))
# - This somehow runs faster than NlogN + Q*log(m) with a sparse table
# - The log(N) can probably be removed since the queries follow a specific structure

import sys
import math

input = sys.stdin.readline
log2 = lambda x: x.bit_length() - 1


def update(i, val):
    """update i-th element to val, 0-indexed"""
    i += size  # start from bottom
    seg[i] = val
    while i > 1:
        i //= 2
        seg[i] = max(seg[i * 2], seg[i * 2 + 1])


def query(left, right):
    right = min(N - 1, right)
    if left > right:
        return 0

    left += size
    right += size

    res_left = res_right = default
    while left < right:
        if left & 1:  # left is odd
            res_left = max(res_left, seg[left])
            left += 1
        if not right & 1:  # right is even
            res_right = max(seg[right], res_right)
            right -= 1
        left //= 2
        right //= 2
    if left == right:  # common segment at the top
        res_left = max(res_left, seg[left])
    return max(res_left, res_right)


N, Q = map(int, input().split())

arr = list(map(int, input().split()))  # arr[i]: difficulty i, gives arr[i] score

# build segment tree
default = 0
layers = math.ceil(math.log2(N))  # max depth of the seg tree, root has depth 0
size = 1 << layers
seg = [default] * (2 * size)  # 1-indexed, need an extra layer for the actual data
for i in range(N):  # base layer
    seg[size + i] = arr[i]
for i in reversed(range(1, size)):  # create other layers from base
    seg[i] = max(seg[i * 2], seg[i * 2 + 1])

ans = []
for _ in range(Q):
    m, k = map(int, input().split())
    cur = 0  # current value of `i`
    best = 0
    for bit in reversed(range(log2(max(m, k)) + 1)):
        b1, b2 = m & (1 << bit), k & (1 << bit)

        if not b2:  # b1 must also be 0
            cur |= b1
        elif b2:
            # if we put a 0, everything else can be anything
            # if we put a 1, we continue the loop
            if not b1:
                best = max(best, query(cur, cur + (1 << bit) - 1))  # stay at 0
                cur |= (1 << bit)
            elif b1:
                best = max(best, query(cur | (1 << bit), cur | (1 << bit) + (1 << bit) - 1))  # go to 0

    if cur < N:
        best = max(best, arr[cur])

    ans.append(best)

print("\n".join(map(str, ans)))
