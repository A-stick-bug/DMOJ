# https://dmoj.ca/problem/olyq2p1
# binary search, similar to search insert position and first bad version from LC
# it is always optimal to place greedily in the first available position

import sys

input = sys.stdin.readline
N, M = map(int, input().split())  # N people, M available positions
pos = sorted([int(input()) for _ in range(N)])  # available positions


def works(dist):
    """check if a distance of at least dist between everyone fits"""
    to_place = M - 1  # number of students that still need a seat (first student always goes in first seat)
    prev = cur = 0
    while to_place:
        while pos[cur] - pos[prev] < dist:
            if cur == N - 1:  # out of seats
                return False
            cur += 1
        prev = cur
        to_place -= 1
    return True


low = 0
high = max(pos) // M  # slight optimization: upper bound is if there is equal distance between everyone
while low <= high:
    mid = low + (high - low) // 2
    if works(mid):
        low = mid + 1
    else:
        high = mid - 1

print(low - 1)  # low is the first distance that doesn't work so the one less than it works
