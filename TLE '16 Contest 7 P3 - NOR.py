# https://dmoj.ca/problem/tle16c7p3
# not associative -> no segment tree :(
# observe stuff, then a bunch of casework

import sys
from itertools import accumulate

input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))

psa = [0] + list(accumulate(arr))
query = lambda l, r: psa[r + 1] - psa[l]

Q = int(input())
for _ in range(Q):
    l, r = map(int, input().split())
    l -= 1  # 0-indexing
    r -= 1

    zeros = 0
    low = 0
    high = (r - l + 1)
    while low <= high:
        mid = (low + high) // 2
        if query(r - mid + 1, r) == 0:
            low = mid + 1
            zeros = mid
        else:
            high = mid - 1

    if zeros == (r - l + 1):  # all 0
        if zeros % 2 == 0:
            print(1)
        else:
            print(0)
    else:
        if zeros + 1 == (r - l + 1):  # all 0 except first one is 1
            if zeros % 2 == 0:
                print(1)
            else:
                print(0)
        else:
            zeros += 1
            if zeros % 2 == 0:
                print(1)
            else:
                print(0)

"""
2
1 0
1
1 2
"""
