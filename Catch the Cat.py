import sys
from collections import deque

start, end = map(int, input().split())

vis = set()
vis.add(start)
q = deque([(start, 0)])
MAX = 10 ** 5

while q:
    cur, moves = q.popleft()
    if cur == end:
        print(moves)
        break

    if cur + 1 not in vis and cur + 1 <= MAX:
        q.append((cur + 1, moves + 1))
        vis.add(cur + 1)

    if cur - 1 not in vis and cur - 1 >= 0:
        q.append((cur - 1, moves + 1))
        vis.add(cur - 1)

    if cur * 2 not in vis and cur * 2 <= MAX:
        q.append((cur * 2, moves + 1))
        vis.add(cur * 2)
