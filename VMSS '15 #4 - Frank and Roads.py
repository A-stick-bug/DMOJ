# template sssp problem

import sys

input = sys.stdin.readline
inf = 1 << 60


def spfa(start):
    q = [0]
    dist = [inf] * (n + 1)
    dist[0] = 0
    in_q = [False] * (n + 1)
    for cur in q:
        in_q[cur] = False
        for adj, d in graph[cur]:
            new_d = dist[cur] + d
            if new_d < dist[adj]:
                dist[adj] = new_d
                if not in_q[adj]:
                    q.append(adj)
    return dist


t, n, m, g = map(int, input().split())
food = [int(input()) for _ in range(g)]

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, d = map(int, input().split())
    graph[a].append((b, d))

dist = spfa(0)
total = 0
for store in food:
    if dist[store] < t:
        total += 1
print(total)
