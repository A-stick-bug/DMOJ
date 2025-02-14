# MLE, CHECK C++ CODE FOR AC
#
# https://dmoj.ca/problem/coci15c5p4
# Greedy constructive question
# Maximum construction: X [everything else] X-1
#
# If we don't need the maximum, we can put some columns at the start
# in ascending order, so they will have no water above them

import sys

N, X = map(int, input().split())
mx = (N - 1) * (N - 2) // 2

if mx < X:
    print(-1)
    sys.exit()

excluded = []
included = []
to_remove = mx - X
for i in range(1, N - 1):
    stored_water = (N - 1) - i
    if to_remove >= stored_water:
        excluded.append(i)
        to_remove -= stored_water
    else:
        included.append(i)

res = excluded + [N] + included + [N - 1]
print(" ".join(map(str, res)))
