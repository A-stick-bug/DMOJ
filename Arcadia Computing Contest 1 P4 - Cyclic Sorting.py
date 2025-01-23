# https://dmoj.ca/problem/ahscc1p4
# Keep track of indices where a[i] > a[i+1]
# If there is more than 1, we can't sort by cyclic shifting
# Otherwise, take the min of shifting forwards and backwards

import sys

input = sys.stdin.readline
N, Q = map(int, input().split())
arr = list(map(int, input().split()))

flips = {i for i in range(N) if arr[i] > arr[(i + 1) % N]}

for _ in range(Q):
    idx, val = map(int, input().split())
    idx -= 1  # 0-indexed
    arr[idx] = val

    flips.discard(idx)  # remove old
    flips.discard((idx - 1) % N)

    if arr[idx] > arr[(idx + 1) % N]:  # add new
        flips.add(idx)
    if arr[(idx - 1) % N] > arr[idx]:
        flips.add((idx - 1) % N)

    if len(flips) == 0:  # everything is equal
        print(0)
    elif len(flips) == 1:
        i = list(flips)[0]
        print(min(i + 1, N - i - 1))
    else:
        print(-1)
