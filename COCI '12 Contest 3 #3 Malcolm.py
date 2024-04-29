# simple data structure
# basically just store a bunch of queues

import sys
from collections import deque

input = sys.stdin.readline
N,K = map(int, input().split())

total = 0
length = [deque() for _ in range(21)]
for rank in range(N):
    name = input().strip()
    le = len(name)
    while length[le] and rank - length[le][0] > K:
        length[le].popleft()
    total += len(length[le])
    length[le].append(rank)

print(total)
