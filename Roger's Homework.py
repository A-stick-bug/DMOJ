# TLE 70/100, use c++ to pass
# make negative for max heap

import heapq
import sys

input = sys.stdin.readline
n = int(input())

hw = [tuple(map(int, input().split())) for _ in range(n)]
hw.sort(reverse=True)  # sort by deadline

days = [0] * (hw[0][0] + 1)  # the most points you can earn on day i

pq = []
i = 0
for time in reversed(range(1, hw[0][0] + 1)):
    while i < n and hw[i][0] >= time:
        heapq.heappush(pq, -hw[i][1])  # prioritize points, make negative for max heap
        i += 1
    if pq:
        days[time] = -heapq.heappop(pq)

print(sum(days))
