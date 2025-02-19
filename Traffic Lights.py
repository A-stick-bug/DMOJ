from collections import deque
import sys

M, N = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

arr = [(0, 0)] + [tuple(map(int, input().split())) for _ in range(N)]

in_q = [False] * (N + 1)
in_q[1] = True
q = deque([1])
dist = [1 << 30] * (N + 1)
dist[1] = 0

while q:
    cur = q.popleft()
    in_q[cur] = False

    for adj, w in graph[cur]:
        arrival = dist[cur] + w
        s = arr[adj][0] + arr[adj][1]
        if s != 0:
            m = arrival % s
            if m >= arr[adj][0]:
                arrival = (arrival // s + 1) * s
        if arrival < dist[adj]:
            dist[adj] = arrival
            if not in_q[adj]:
                in_q[adj] = True
                q.append(adj)

print(dist[N])
