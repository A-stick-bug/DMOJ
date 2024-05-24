# modular math

import sys

input = sys.stdin.readline
N, D = map(int, input().split())

loc = 0  # current location
time = 0  # current time elapsed

for _ in range(N):
    l, r, g = map(int, input().split())
    time += l - loc  # move to light
    loc = l

    t = time % (r + g)  # wait for green light
    time += max(0, r - t)

print(time + (D - loc))  # extra distance to school
