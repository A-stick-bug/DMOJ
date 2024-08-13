# https://dmoj.ca/problem/stp4
# Template Mo's algorithm
# Basically put the queries in a certain order such that you can
# go from 1 query to another in amortized sqrt(N) time
#
# TC: O(NsqrtN), assuming N=Q
# note: there's probably a more efficient method that I didn't think of

import sys

input = sys.stdin.readline
SQRT = 400  # group size

N, Q = map(int, input().split())
arr = [0] + list(map(int, input().split()))  # 1-indexed
queries = [list(map(int, input().split())) + [i] for i in range(Q)]
ans = [-1] * Q

freq = [0] * (N + 1)
once = 0


def add_element(val):
    global once, freq
    if freq[val] == 0:  # 0 -> 1
        once += 1
    elif freq[val] == 1:  # 1 -> 2
        once -= 1
    freq[val] += 1


def remove_element(val):
    global once, freq
    if freq[val] == 1:  # 1 -> 0
        once -= 1
    elif freq[val] == 2:  # 2 -> 1
        once += 1
    freq[val] -= 1


queries.sort()  # sort and group by left
prev_r = 0
prev_l = 1
for i in range(0, Q, SQRT):
    group = queries[i:i + SQRT]
    if i & 1 == 0:  # ascending/descending optimization
        group.sort(key=lambda x: x[1])  # sort individual group by right
    else:
        group.sort(key=lambda x: x[1], reverse=True)

    for l, r, idx in group:
        while prev_r < r:
            prev_r += 1
            add_element(arr[prev_r])
        while prev_r > r:
            remove_element(arr[prev_r])
            prev_r -= 1
        while prev_l < l:
            remove_element(arr[prev_l])
            prev_l += 1
        while prev_l > l:
            prev_l -= 1
            add_element(arr[prev_l])

        ans[idx] = once

print("\n".join(map(str, ans)))