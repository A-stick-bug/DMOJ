"""
https://dmoj.ca/problem/cpc21c1p4
First maximize X, then maximize Y
Reverse the graph and start at maximum Y, going down and marking nodes with the largest Y
Once a node has been marked with a Y, we know it is the largest pair (X,Y) that contains Y
"""

import sys
from collections import deque

input = sys.stdin.readline
N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]  # reversed graph
for _ in range(M):
    a, b = map(int, input().split())
    graph[b].append(a)
vis = [-1] * (N + 1)


def search(start):
    q = deque([start])
    while q:
        cur = q.popleft()
        for adj in graph[cur]:
            if vis[adj] != -1:  # already have a better answer for this node
                continue
            if start > adj:  # we start from the end, so if the node is less than the end, it does not form a valid path
                vis[adj] = start
                q.append(adj)


for i in reversed(range(1, N + 1)):  # search from every Y
    search(i)

for i in reversed(range(1, N + 1)):  # highest visited index (maximum X)
    if vis[i] != -1:
        print(i, vis[i])
        sys.exit()
print(-1)
