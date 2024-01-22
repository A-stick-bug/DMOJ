# https://dmoj.ca/problem/dmopc15c3p4
# using 1-indexing
# note: we don't create the actual graph, just get the distances during dijkstra's

import sys
from heapq import heappush, heappop
from bisect import bisect_right

input = sys.stdin.readline
print = lambda x: sys.stdout.write(str(x) + "\n")
inf = 1 << 60
distance = lambda a, b: (a[0] - b[0]) * (a[0] - b[0]) + (a[1] - b[1]) * (a[1] - b[1])

n = int(input())
loc = [tuple(map(int, input().split())) for _ in range(n)]
start = int(input()) - 1  # 0-indexing


# def dijkstra(start):  # with heap (EXTRA LOG FACTOR IS TOO SLOW)
#     dist = [inf] * n
#     dist[start] = 0
#     pq = [(0, start)]
#
#     while pq:
#         d, cur = heappop(pq)
#         if dist[cur] < d:  # already visited
#             continue
#         for adj in range(n):
#             new_d = distance(loc[cur], loc[adj]) + d
#             if new_d < dist[adj]:
#                 dist[adj] = new_d
#                 heappush(pq, (new_d, adj))
#
#     return dist

def dijkstra(start):  # without heap
    dist = [inf] * n
    dist[start] = 0
    vis = [False] * n

    for _ in range(n):  # n nodes in total, find shortest path to all of them
        min_distance = inf
        for i in range(n):
            if not vis[i] and dist[i] < min_distance:
                u = i
                min_distance = dist[i]
        vis[u] = True
        for k in range(n):
            d = distance(loc[u], loc[k])
            if not vis[k] and d and dist[u] + d < dist[k]:
                dist[k] = dist[u] + d

    return dist


dist = dijkstra(start)
dist.sort()
for _ in range(int(input())):  # answer queries
    time = int(input())
    print(bisect_right(dist, time))
