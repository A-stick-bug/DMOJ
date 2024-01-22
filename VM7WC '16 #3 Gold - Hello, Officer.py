# https://dmoj.ca/problem/vmss7wc16c3p3
# classic SSSP problem, note: we start from the end to precompute all distances to there and avoid running
# dijkstra's for every query

import sys
from heapq import heappop, heappush

input = sys.stdin.readline
inf = 1 << 60

n, m, end, q = map(int, input().split())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))


def dijkstra(start):
    dist = [inf] * (n + 1)
    dist[start] = 0
    pq = [(0, start)]
    while pq:
        d, cur = heappop(pq)
        if dist[cur] < d:  # already visited
            continue
        for adj, adj_d in graph[cur]:
            new_d = d + adj_d
            if new_d < dist[adj]:
                dist[adj] = new_d
                heappush(pq, (new_d, adj))
    return dist


dist = dijkstra(end)  # start from the end

for _ in range(q):
    node = int(input())
    if dist[node] == inf:
        print(-1)
    else:
        print(dist[node])
