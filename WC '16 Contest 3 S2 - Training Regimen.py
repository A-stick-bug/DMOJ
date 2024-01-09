"""
PYTHON TAKES TOO MUCH MEMORY, MLE, CHECK C++ CODE

https://dmoj.ca/problem/wc16c3s2
Graph theory, similar to MST

Ignore time to travel between nodes -> MST-like algorithm
Store all possible edges we can visit next in a heap, keep take the one that requires minimum level and upgrade
to that level, we may be able to get a faster training time there, even if we don't we don't lose anything

Note: we use a visited array like normal to prevent revisiting nodes/infinite loop
"""

import sys
from heapq import heappop, heappush, heapify

input = sys.stdin.readline
n, m = map(int, input().split())

train = [-1] + [int(input()) for _ in range(n)]
fastest = train[1]
cur_lvl = 1

graph = [[] for _ in range(n + 1)]  # create graph
for _ in range(m):
    a, b, lvl = map(int, input().split())
    graph[a].append((lvl, b))
    graph[b].append((lvl, a))

time = 0
pq = graph[1]
heapify(pq)
vis = [False] * (n + 1)
vis[1] = True

while pq:
    lvl, cur = heappop(pq)  # take reachable path with minimum lvl requirement

    diff = max(0, lvl - cur_lvl)  # level up (if needed) to access cheapest edge
    cur_lvl = max(cur_lvl, lvl)
    time += diff * fastest
    fastest = min(fastest, train[cur])  # we may have accessed a faster training town

    if cur == n:  # reached destination
        print(time)
        sys.exit()

    for adj in graph[cur]:  # add adjacent edges that we can now reach
        if not vis[adj[1]]:
            heappush(pq, adj)
            vis[adj[1]] = True

print(-1)
