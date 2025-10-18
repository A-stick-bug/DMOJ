"""
https://dmoj.ca/problem/dmopc21c9p3

Interesting ad hoc graph question

Observations:
- Bounds strongly suggest getting all pairs shortest path

Consider the following strategy:
- Let A,B be the 2 new nodes you are connecting
- First, put A at U and B at V
- With the 'extra' distance allowed in U <-> V, pull A and B towards S and T (or flip to T and S)
- If the extra distance is enough to bring S and T close enough to A and B, it works
- Notice how when pulling A,B towards S,T, it's always along the shortest path from U to S and V to T (or swap)
  - there's no reason not to move along the shortest path since A-B is fixed at distance 1


Pitfalls:
- attempting to do precomputation on A and B beforehand
- trying to actually find the nodes A and B

TC: O(N(N+M) + Q), n*bfs + O(1) queries
"""

import sys
from collections import deque

input = sys.stdin.readline
fast_print = lambda x: sys.stdout.write(x + "\n")

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dist = [[-1] * (n + 1) for _ in range(n + 1)]


def bfs(start):
    q = deque([start])
    dist[start][start] = 0
    while q:
        cur = q.popleft()
        for adj in graph[cur]:
            if dist[start][adj] == -1:
                dist[start][adj] = dist[start][cur] + 1
                q.append(adj)


for i in range(1, n + 1):
    bfs(i)

for _ in range(int(input())):
    s, t, x, u, v, y = map(int, input().split())
    if dist[s][t] <= x or dist[u][v] <= y:  # trivial case, connect the 2 nodes that are not already close enough
        fast_print("YES")
        continue

    # assume we connect U-V
    # this is how far we can pull A and B away from U and V
    leftover = y - 1

    if min(dist[s][u] + dist[t][v], dist[t][u] + dist[s][v]) - leftover + 1 <= x:
        fast_print("YES")
    else:
        fast_print("NO")
