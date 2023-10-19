# https://dmoj.ca/problem/wc16c1s3
# note: the time taken is (distance of furthest house) + (T * houses visited)
# basically sliding window with a heapq to remove the smallest element

import heapq
import sys

input = sys.stdin.readline

# N houses, M ms total time, T ms per house
N, M, T = map(int, input().split())

houses = [tuple(map(int, input().split())) for _ in range(N)]  # (distance to start, candy)
houses.sort()  # sort by distance to start

pq = []
cur = res = 0

for i, (dist, candy) in enumerate(houses):
    heapq.heappush(pq, candy)
    cur += candy
    prev = 0 if i == 0 else houses[i - 1][0]  # previous house location
    M -= 2 * (dist - prev) + T  # additional time to get candy from this house

    # need to not visit some houses to make it back before midnight
    while M < 0 and pq:
        cur -= heapq.heappop(pq)  # don't visit the house that gives the least candy
        M += T  # saved time for not visiting house

    res = max(res, cur)

print(res)
