# https://dmoj.ca/problem/dmopc21c10p2
# CASEWORK, that's literally it
# yet another stupid question that requires you to code many solutions...
# could've at least gave us another sample

import sys

n = int(input())
arr = list(map(int, input().split()))

if n == 1:
    print(1)
    sys.exit()


def solve1(arr):  # strategy 1: put the right numbers AFTER 1
    arr = arr * 2  # double the array as it is circular
    arr = arr[arr.index(1):]  # put the 1 at the front for lex min
    for i in range(n):
        if arr[i] == i + 1:  # account for 1-indexing
            continue
        else:
            missing_pos = arr.index(i + 1)
            arr[i], arr[missing_pos] = arr[missing_pos], arr[i]
            break
    return arr[:n]


def solve2(arr):  # strategy 2: move the one in front of the 2
    two_pos = arr.index(2)
    one_pos = arr.index(1)
    arr[two_pos - 1], arr[one_pos] = 1, arr[two_pos - 1]
    return arr[arr.index(1):] + arr[:arr.index(1)]


def solve3(arr):  # strategy 3: (corner case) swap the 1 and 2 if 1 appears right after 2
    arr = arr[arr.index(2):] + arr[:arr.index(2)]
    if arr[1] == 1:
        arr[0] = 1  # swap
        arr[1] = 2
        return arr
    else:
        return arr  # nothing to do


print(*min(solve1(arr.copy()), solve2(arr.copy()), solve3(arr.copy())))

"""
Corner case you may be looking for:
6
1 3 6 5 4 2

1 2 3 6 5 4
"""
