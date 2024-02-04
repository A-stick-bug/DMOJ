# https://dmoj.ca/problem/dmopc18c2p3
# shortest path with mandatory node
# take the min of dist(start -> mid + mid -> end)
# do this quickly by computing all distances from the start and end and trying all values of mid in O(1)

import sys

input = sys.stdin.readline
N, M, K, A, B = map(int, input().split())
special = tuple(map(int, input().split()))  # must pass through one of these

graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def bfs(start):
    """get distance from start to all other nodes"""
    q = [start]
    dist = [-1] * (N + 1)
    dist[start] = 0
    for cur in q:
        for adj in graph[cur]:
            if dist[adj] == -1:
                dist[adj] = dist[cur] + 1
                q.append(adj)
    return dist


from_start = bfs(A)
from_end = bfs(B)

res = float('inf')
for s in special:
    res = min(res, from_start[s] + from_end[s])
print(res)
