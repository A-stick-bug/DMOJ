# https://dmoj.ca/problem/wossoly23s2
# all in 1 intervals question
# tests you on most concepts of keeping track of intervals

def remove_range(intervals, rl, rr):
    res = []
    for a, b in intervals:
        if a < rl - 1:
            res.append((a, min(b, rl)))
        if b > rr + 1:
            res.append((max(a, rr), b))
    return res


def merge_all(intervals):
    if not intervals:
        return []
    # intervals.sort()
    res = [intervals[0]]
    for l, r in intervals[1:]:
        if res[-1][1] >= l:  # left overlaps with right, we can combine
            res[-1] = (res[-1][0], max(res[-1][1], r))
        else:  # disjoint intervals
            res.append((l, r))
    return res


N, M, K = map(int, input().split())

prev = -1
arr = [(0, 0)]  # valid intervals [l, r]

for _ in range(M):
    left, right, time = map(int, input().split())

    # expand intervals
    for i in range(len(arr)):
        arr[i] = (max(0, arr[i][0] - K * (time - prev)), min(N, arr[i][1] + K * (time - prev)))

    arr = merge_all(remove_range(arr, left, right))
    prev = time

if arr:
    print("YES")
else:
    print("NO")
