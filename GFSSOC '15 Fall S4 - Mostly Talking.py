# 50/100 TLE, PYTHON IS TOO SLOW, CHECK C++ CODE
# shortest path from 1 to N, you are given some special edges, and you can only take 1 special edge in total

import sys
from heapq import heappop, heappush

input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]  # (destination, distance, special)
for _ in range(M):
    a, b, d = map(int, input().split())
    graph[a].append((b, d, False))

S = int(input())
for _ in range(S):
    a, b, d = map(int, input().split())
    graph[a].append((b, d, True))

inf = 1 << 50

# dist[i][t/f] is the shortest path to node i passing or without passing through a special node
dist = [[inf, inf] for _ in range(N + 1)]
dist[1] = [0, 0]

pq = [(0, 1, False)]
while pq:
    d, cur, special = heappop(pq)
    if cur == N:
        print(d)
        sys.exit()

    for adj, adj_dist, adj_special in graph[cur]:
        new_dist = adj_dist + d
        new_special = special + adj_special
        if new_special > 1:  # can't take more than 1 special path
            continue

        if dist[adj][new_special] > new_dist:
            dist[adj][new_special] = new_dist
            heappush(pq, (new_dist, adj, new_special))

print(-1)
