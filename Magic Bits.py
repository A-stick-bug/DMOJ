# https://dmoj.ca/problem/magicbits
# Observe some bitwise stuff

import sys

input = sys.stdin.readline

MX = 62


def solve(x, y):
    if x > y:
        return -1
    if x == y:
        return 0
    if x | y == y:
        return 1

    for i in reversed(range(MX)):
        msk = (1 << i) - 1
        if y & msk > x & msk:
            msb_x = i
        else:
            break
    diff = (1 << (msb_x - 1)) - x & ((1 << msb_x) - 1)
    if x + diff == y:
        return diff
    return diff + 1


for _ in range(int(input())):
    print(solve(*map(int, input().split())))

"""
1
5 94
"""

# # fast-slow code for verification
# def brute_force(x,y):
#     if x > y:
#         return(-1)
#
#     # sanity check
#     for i in range(x, y + 1):
#         if i | y == y:
#             diff = i -x
#             if x + diff == y:
#                 return(diff)
#             else:
#                 return(diff+1)
#
# t = 9999999
# from random import randint
# for _ in range(t):
#     x,y = randint(1, 5), randint(6, 10)
#
#     a = brute_force(x,y)
#     b=solve(x,y)
#     if a != b:
#         print("fail", _)
#         print(f"{x=}, {y=}, {a=}, {b=}")
#         break
