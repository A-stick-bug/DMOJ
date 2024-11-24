# https://dmoj.ca/problem/cheerio1s2
# greedy: build each classroom using the cheapest way possible

from heapq import heappop, heappush, heapify

N, A, B = map(int, input().split())

total = 0
pq = [(A * i + B, i, 1) for i in range(1, N + 1)]  # (cost, floor, room)
for _ in range(N):
    c, floor, room = heappop(pq)
    total += c
    heappush(pq, (A * floor + B * (room + 1), floor, room + 1))
print(total)
