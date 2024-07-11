# https://dmoj.ca/problem/naq15g
# Ugly bitmask DP with optimizations
#
# TC: O(2^N * N^2)

import sys

sys.setrecursionlimit(100000)
n, *arr = list(map(int, input().split()))

MS = 1 << n
inf = 1 << 30
cache = [[inf] * MS for _ in range(2)]


def solve(send, cur):
    if cur.bit_count() == n:  # reached goal
        return 0
    if cache[send][cur] != inf:
        return cache[send][cur]

    ans = inf
    for i in range(n):
        for j in range(i, n):
            # move back: it is never optimal to bring 2 people back since you just wasted a move
            if i == j and cur & (1 << i) and cur & (1 << j) and not send:
                ans = min(ans, solve(send ^ 1, cur - (1 << i)) + arr[i])

            # send over: it is always optimal to send 2 people over (or else we can't bring cloak back)
            # UNLESS there is only 1 person left
            if ((i != j or (i == j and cur.bit_count() == n - 1)) and
                    (not cur & (1 << i)) and (not cur & (1 << j)) and send):
                ans = min(ans, solve(send ^ 1, cur | (1 << i) | (1 << j)) + max(arr[i], arr[j]))

    cache[send][cur] = ans
    return cache[send][cur]


print(solve(True, 0))
