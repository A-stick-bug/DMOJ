# https://dmoj.ca/problem/noi04p1
# TLE, 70/100, seems impossible to pass in python even with optimizations such as map and filter
# Brute force (binary search), intended solution is probably a data structure like order statistic tree or segment tree

import sys
from bisect import insort

input = sys.stdin.readline
N, M = map(int, input().split())

left = 0
wages = []

for _ in range(N):
    cmd, val = input().split()
    val = int(val)

    if cmd == 'I':  # add new person
        if val < M:  # left immediately
            continue
        insort(wages, val)

    elif cmd == 'F':
        if val > len(wages):  # not enough people
            print(-1)
            continue
        print(wages[-val])

    elif cmd == 'A':
        wages = list(map(lambda x: x + val, wages))

    else:
        wages = list(map(lambda x: x - val, wages))
        old = len(wages)
        wages = list(filter(lambda x: x >= M, wages))
        left += old - len(wages)

print(left)
