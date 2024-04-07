# https://dmoj.ca/problem/coci22c3p2
# Q: Given queries that swap elements, print if you can cut the array into 2 sorted parts
#
# Watch out for the corner cases

import sys

input = sys.stdin.readline
print = sys.stdout.write

N, Q = map(int, input().split())
arr = [-2] + list(map(int, input().split())) + [-2]

loc = [-1] * (N + 3)  # stores the index of number n in arr
for i, val in enumerate(arr):
    loc[val] = i

get_score = lambda i: arr[i] + 1 == arr[i + 1]

cur = sum(get_score(i) for i in range(1, N))
for _ in range(Q):
    a, b = map(int, input().split())

    if abs(loc[a] - loc[b]) == 1:  # stupid corner case
        if loc[a] > loc[b]:
            a, b = b, a
        cur -= get_score(loc[b])
        cur -= get_score(loc[a]) + get_score(loc[a] - 1)
        arr[loc[a]] = b
        arr[loc[b]] = a
        loc[a], loc[b] = loc[b], loc[a]
        cur += get_score(loc[b]) + get_score(loc[b] - 1)
        cur += get_score(loc[a])
    else:
        cur -= get_score(loc[a]) + get_score(loc[a] - 1)
        cur -= get_score(loc[b]) + get_score(loc[b] - 1)
        arr[loc[a]] = b
        arr[loc[b]] = a
        loc[a], loc[b] = loc[b], loc[a]
        cur += get_score(loc[a]) + get_score(loc[a] - 1)
        cur += get_score(loc[b]) + get_score(loc[b] - 1)

    if cur >= N - 2:
        print("DA\n")
    else:
        print("NE\n")
