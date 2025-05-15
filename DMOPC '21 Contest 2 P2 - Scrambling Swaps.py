# https://dmoj.ca/problem/dmopc21c2p2
# Looking at constraints, we see that we can do O(1) work for type 1,2 and O(nlogn) work for type 3
# Treat a sequence of swaps as a bijective function mapping [0,n-1] to [0,n-1]
# TC: O(Q + 3000N), amortized

import sys

input = sys.stdin.readline

N, Q = map(int, input().split())
arr = list(range(N))

pre_swap = []  # swaps added to beginning
for _ in range(Q):
    q = input().split()
    if q[0] == "B":  # swap to beginning
        x, y = map(lambda x: int(x) - 1, q[1:])
        pre_swap.append((x, y))

    elif q[0] == "E":  # swap to end, do it manually
        x, y = map(lambda x: int(x) - 1, q[1:])
        arr[x], arr[y] = arr[y], arr[x]

    else:  # only 3000 of these, do O(n) work
        target = list(map(lambda x: int(x) - 1, q[1:]))

        # merge arr and prefix
        prefix = list(range(N))
        for x, y in reversed(pre_swap):
            prefix[x], prefix[y] = prefix[y], prefix[x]
        arr = [prefix[i] for i in arr]
        pre_swap.clear()

        # find sequence that result in target after applying arr, in other words, apply the inverse of arr
        origin = [0] * N
        for i in range(N):
            origin[arr[i]] = target[i]

        print(" ".join(map(lambda x: str(x + 1), origin)))
