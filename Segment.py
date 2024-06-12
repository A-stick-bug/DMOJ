# https://dmoj.ca/problem/oly18novp1
# intuitively, it makes sense to do the tasks that end first
# so you have the most time available to do other tasks

import sys

input = sys.stdin.readline
n = int(input())
ranges = [tuple(map(int, input().split())) for _ in range(n)]
ranges.sort(key=lambda x: x[1])

cnt = 0
cur_end = -1
for l, r in ranges:
    if l >= cur_end:
        cur_end = r
        cnt += 1
print(cnt)
