# https://dmoj.ca/problem/sssp
# standard SPFA implementation
# Dijkstra's works as well

from collections import deque
import sys

inf = 1 << 50
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, w = map(int, input().split())
    graph[a].append((b, w))
    graph[b].append((a, w))

in_q = [False] * (n + 1)
q = deque([1])
dist = [1 << 50] * (n + 1)
dist[1] = 0

while q:
    cur = q.popleft()
    in_q[cur] = False

    for adj, w in graph[cur]:
        new_d = dist[cur] + w
        if dist[adj] > new_d:
            dist[adj] = new_d
            if not in_q[adj]:  # prevent useless duplicates in the queue
                dist[adj] = new_d
                q.append(adj)
                in_q[adj] = True

for i in dist[1:]:
    if i == inf:
        print(-1)
    else:
        print(i)
