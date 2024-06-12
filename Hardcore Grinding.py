# https://dmoj.ca/problem/grind
# simple greedy with heap
# note: an alternate solution is just using a difference array and taking the max

from heapq import heappop, heappush
import sys

input = sys.stdin.readline
n = int(input())
tasks = [tuple(map(int, input().split())) for _ in range(n)]
tasks.sort(key=lambda x: x[0])  # sort by start time

cnt = 0
machines = []
for s, e in tasks:
    while machines and machines[0] <= s:
        heappop(machines)
    heappush(machines, e)
    cnt = max(cnt, len(machines))

print(cnt)
