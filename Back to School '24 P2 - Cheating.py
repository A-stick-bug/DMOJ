# https://dmoj.ca/problem/bts24p2
# how can we use non-decreasing property of A?
# scores will be monotonic after applying cyclic shifts
# max element will always be the last value in range update

from itertools import accumulate

N, M = map(int, input().split())
a = list(map(int, input().split()))  # points
b = list(map(int, input().split()))  # give to b[i] students

max_idx = -1
updates = []
for amt, sz in zip(a, b):
    l = (max_idx + 1) % M
    r = (l + sz - 1) % M

    if l <= r:
        updates.append((l, r, amt))
    else:
        updates.append((l, M - 1, amt))
        updates.append((0, r, amt))

    max_idx = r

diff = [0] * (M + 1)
for l, r, amt in updates:
    diff[l] += amt
    diff[r + 1] -= amt
score = list(accumulate(diff))[:-1]
print(" ".join(map(str, score)))
