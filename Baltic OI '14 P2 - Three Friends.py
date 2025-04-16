# https://dmoj.ca/problem/btoi14p2
# No brain solution: hashing to brute force all possible indices
#
# Smarter solution: consider casework
# - extra character is inside A
# - extra character is inside B

import sys


def works(s, t):
    """returns if `t` can be turned into `s` by removing 1 character"""
    s += "."  # common character
    t += "."
    i = 0
    moves = 0
    for j in range(len(t)):
        if s[i] == t[j]:
            i += 1
        else:
            moves += 1
    return moves == 1


s = input()
n = len(s) // 2

ans = ""
if works(s[:n], s[n:]):  # extra in B
    ans = s[:n]
if works(s[n + 1:], s[:n + 1]):  # extra in A
    if ans and ans != s[n + 1:]:
        print("NOT UNIQUE")  # can't be both A and B
        sys.exit()
    else:
        ans = s[n + 1:]

if ans:
    print(ans)
else:
    print("NOT POSSIBLE")
