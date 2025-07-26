# https://dmoj.ca/problem/ioi05p3
# Observation based question, monotonic property is key
# Note: can't store all N elements in an array since it would MLE
# Instead, keep track of the valid interval of numbers [l,r] at each step

import sys


def solve():
    input = sys.stdin.readline
    inf = 1 << 60

    n = int(input())

    t1 = int(input())
    low = -inf
    high = t1
    for _ in range(1, n):
        t2 = int(input())

        low, high = t1 + (t1 - high), t1 + (t1 - low)

        low = max(low, t1)
        high = min(high, t2)

        if low > high:
            print(0)
            sys.exit()

        t1 = t2

    print(high - low + 1)


solve()