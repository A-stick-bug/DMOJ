# https://dmoj.ca/problem/graph3p2
# Template SPFA algorithm

from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

inf = 1 << 30
q = deque([1])
in_q = [False] * (n + 1)
in_q[1] = True
dist = [inf] * (n + 1)
dist[1] = 0
while q:
    cur = q.popleft()
    in_q[cur] = False
    for adj, w in graph[cur]:
        new_d = dist[cur] + w
        if new_d < dist[adj]:
            dist[adj] = new_d
            if not in_q[adj]:
                q.append(adj)
                in_q[adj] = True

print(dist[n])
