# https://dmoj.ca/problem/dmpg15s5
# using a difference array (1 row at a time)

import sys

input = sys.stdin.readline

n, m = map(int, input().split())
rect = [[] for _ in range(n + 1)]  # a 2D array of bools takes too much memory
for _ in range(m):
    c, r, w, h = map(int, input().split())
    rect[r].append(c)  # note the places where the difference changes
    rect[r].append(c + w)
    rect[r + h].append(c)
    rect[r + h].append(c + w)

dif = [0 for _ in range(n + 1)]  # do 1 row at a time to save memory
res = 0
for i in range(n):
    for j in rect[i]:  # build the difference array for this row
        dif[j] ^= True

    cur = False
    for j in range(n):  # count black tiles
        cur ^= dif[j]
        res += cur

print(res)


# # TLE, O(mn + n^2), optimized code above
# import sys
#
# input = sys.stdin.readline
#
# n, m = map(int, input().split())
# diff = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
# for _ in range(m):
#     c, r, w, h = map(int, input().split())
#     for i in range(r, r +h):
#         diff[i][c] ^= True
#         diff[i][c+w] ^= True
#
# res = 0
# for i in range(n):
#     state = 0
#     for j in range(n):
#         state ^= diff[i][j]
#         res += state
#
# print(res)
