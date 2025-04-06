# https://dmoj.ca/problem/dmopc20c6p3
# Extension of topological sort
# - A node will always end up at a leaf if it is not in a cycle, topo sort can detect this
# - Police nodes don't have this restriction
# - Start topo sort from all leaves, bypass the indegree restriction at police nodes
# - Note: since police nodes don't follow the indegree rule, we need a visited array
#   to prevent them from being added many times

import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
arr = [-1] + list(map(int, input().split()))

rev_graph = [[] for _ in range(n + 1)]
out_degree = [0] * (n + 1)
for _ in range(m):
    a, b = map(int, input().split())
    rev_graph[b].append(a)
    out_degree[a] += 1

leafs = [i for i in range(1, n + 1) if out_degree[i] == 0]

vis = [False] * (n + 1)
works = [0] * (n + 1)
for node in leafs:
    works[node] = 1
    vis[node] = True

q = deque(leafs)

while q:
    cur = q.popleft()
    for adj in rev_graph[cur]:
        if vis[adj]:
            continue
        out_degree[adj] -= 1
        if out_degree[adj] == 0 or arr[adj]:
            works[adj] = 1
            vis[adj] = True
            q.append(adj)

print(" ".join(map(str, works[1:])))

"""
6 6
0 0 0 0 0 0
1 2
1 3
2 4
2 5
3 5
3 6
"""
