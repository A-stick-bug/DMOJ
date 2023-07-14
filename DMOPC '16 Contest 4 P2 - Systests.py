# 7/7 in DMOJ, binary search, slightly tricky

from bisect import bisect_left, bisect_right

n_batches = int(input())

batches = []  # (start, end, point)
for i in range(n_batches):
    start, end, points = map(int, input().split())
    batches.append((start, end, points))

n_wrong = int(input())
wrong = [int(input()) for _ in range(n_wrong)]
wrong.sort()

res = 0
for start, end, points in batches:
    if bisect_left(wrong, start) == bisect_right(wrong, end):  # all cases in this batch passes
        res += points  # add points from this batch

print(res)
