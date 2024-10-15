# https://dmoj.ca/problem/coci13c2p1
# reading comprehension test

import sys

cur = int(input()) - 1
n = int(input())

time = 3 * 60 + 30
for _ in range(n):
    time_taken, t = input().split()
    time_taken = int(time_taken)

    if time_taken >= time:
        print(cur + 1)
        sys.exit()

    time -= time_taken
    if t == "T":
        cur = (cur + 1) % 8
