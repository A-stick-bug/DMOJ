"""
https://dmoj.ca/problem/dmopc22c1p2
swaps can be represented as a graph
d1[i] has the minimum and second minimum number of moves to get to color i from 1

if there is a 'conflict' where both people's shortest path lead to the same color, we need to
take the second-shortest path for one person
"""

import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

graph = [[] for _ in range(n)]  # create graph from input
for i in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append(b)
    graph[b].append(a)


def bfs(start, dist):
    d = [0] * n
    q = deque([start])

    while q:
        cur = q.popleft()
        color = arr[cur]
        if len(dist[color]) < 2:  # get both the shortest and second-shortest path
            dist[color].append((cur, d[cur]))

        for adj in graph[cur]:
            if d[adj] != 0:  # already visited
                continue
            q.append(adj)
            d[adj] = d[cur] + 1


d1 = [[] for _ in range(n + 1)]
d2 = [[] for _ in range(n + 1)]

bfs(0, d1)  # run bfs from 1 and n
bfs(n - 1, d2)

ans = float('inf')
for i in range(1, n + 1):
    for a, da in d1[i]:
        for b, db in d2[i]:
            if a != b:  # no conflict
                ans = min(ans, da + db)

if ans == float('inf'):
    print(-1)
else:
    print(ans)
