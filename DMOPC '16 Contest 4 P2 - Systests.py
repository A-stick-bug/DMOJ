# 7/7 in DMOJ, binary search, slightly tricky

from bisect import bisect_left, bisect_right

n_batches = int(input())

batches = []  # (start, end, point)
max_points = 0
for i in range(n_batches):
    start, end, points = map(int, input().split())
    batches.append((start, end, points))
    max_points += points  # instead of deducting from max possible, we can just start at 0 and add the batches that passed

n_wrong = int(input())
wrong = [int(input()) for _ in range(n_wrong)]
wrong.sort()

for start, end, points in batches:
    cut_start = bisect_left(wrong, start)
    cut_end = bisect_right(wrong, end)
    if cut_start != cut_end:  # there is a wrong test case in this range
        max_points -= points  # deduct points from this batch

print(max_points)
