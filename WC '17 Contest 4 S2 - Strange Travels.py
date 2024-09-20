# https://dmoj.ca/problem/wc17c4s2
# the total distance travelled can be broken down into
# 1. the distance from node 1 to every node in `locs`
# 2. the distance from every node `locs` to node 1
#
# Both of these can be computed efficiently with bfs (although we need to reverse the graph for 2)

import sys
from collections import deque


def get_distances(graph, start):
    """Given a graph, return the distance to all nodes from a starting point"""
    q = deque([start])
    dist = [inf] * (N + 1)
    dist[start] = 0
    while q:
        cur = q.popleft()
        for adj in graph[cur]:
            if dist[adj] == inf:
                dist[adj] = dist[cur] + 1
                q.append(adj)
    return dist


input = sys.stdin.readline
inf = 1 << 60

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
rev_graph = [[] for _ in range(N + 1)]  # reversed graph
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    rev_graph[b].append(a)

K = int(input())
locs = list(map(int, input().split()))

d1 = get_distances(graph, 1)
d2 = get_distances(rev_graph, 1)
total = 0
for i in locs:  # back and forth distances to each node
    total += d1[i] + d2[i]

if total >= inf:
    print(-1)
else:
    print(total)
