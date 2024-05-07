# https://dmoj.ca/problem/macs2p3
# template PSA + binary search
# why do these 2 topics always go together...

import sys
from itertools import accumulate

input = sys.stdin.readline
N, Q = map(int, input().split())
arr = [0] + list(map(int, input().split()))  # 1-indexed

psa = list(accumulate(arr))

for _ in range(Q):
    l, s = map(int, input().split()[1:])
    low = 1
    high = N
    while low <= high:
        mid = (low + high) // 2
        if psa[mid] - psa[l - 1] < s:
            low = mid + 1
        else:
            high = mid - 1

    print(min(N, low))
