"""
https://dmoj.ca/problem/graph3p1

Problem is trivial because "You may assume that there are at least N salesmen at each company office"
We can just use standard BFS by putting all nodes with salesmen into the queue

"""

from collections import deque

NODES, EDGES = map(int, input().split())
graph = [[] for _ in range(NODES + 1)]
for _ in range(EDGES):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)  # bidirectional edges

vis = [False] * (NODES + 1)
n_salesmen = int(input())
max_dist = 0  # time taken to reach the most recent node

q = deque([])
for _ in range(n_salesmen):   # put all nodes with salesmen inside the queue (node, dist)
    node = int(input())
    vis[node] = True
    q.append((node, 0))

while q:
    cur, dist = q.popleft()
    max_dist = dist  # dist is guaranteed to be >= max_dist
    for adj in graph[cur]:
        if vis[adj]:
            continue
        vis[adj] = True
        q.append((adj, dist + 1))

print(max_dist)