# almost template dijkstra's algorithm
# (start -> alex -> end) is (start -> alex) + (alex -> end)
# to get the max, we first compute every (start -> alex) and every (end -> alex)
# then take the max possible for every node

import sys

input = sys.stdin.readline
inf = 1 << 60

n, m = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))


def spfa(start):
    dist = [inf] * n
    dist[start] = 0
    in_q = [False] * n
    q = [start]
    for cur in q:
        in_q[cur] = False
        for adj, d in graph[cur]:
            new_d = dist[cur] + d
            if new_d < dist[adj]:
                dist[adj] = new_d
                if not in_q[adj]:
                    in_q[adj] = True
                    q.append(adj)
    return dist


from_start = spfa(0)
from_end = spfa(n - 1)

print(max(from_end[i] + from_start[i] for i in range(n)))
