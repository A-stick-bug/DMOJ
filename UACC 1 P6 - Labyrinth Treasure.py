"""
https://dmoj.ca/problem/uacc1p6
Using LCA template with dijkstra's template
The amount of variables makes the question quite complex (though not much harder)

Strategy:
- first make an LCA to get distance between 2 nodes in O(1)
- then run dijkstra's algorithm on the BOXES, not the graph nodes, using the lca to get distance
"""

import sys
from math import log2
from heapq import heappop, heappush

sys.setrecursionlimit(100000)


class LCA:
    def __init__(self):
        self.depth = [0] * (N + 1)
        self.first = [0] * (N + 1)
        self.dis = [0] * (N + 1)

        self.euler = []
        self.st = [[(0, 0)] * 18 for _ in range(2 * N + 2)]

        self.dfs(1, -1)
        M = len(self.euler)
        LOG = int(log2(M))
        for i in range(M):
            self.st[i][0] = (self.depth[self.euler[i]], self.euler[i])
        for k in range(1, LOG + 1):
            for i in range(M - (1 << k) + 1):
                self.st[i][k] = min(self.st[i][k - 1], self.st[i + (1 << k - 1)][k - 1])

    def dfs(self, u, prev):
        self.first[u] = len(self.euler)
        self.euler.append(u)
        for v, w in graph[u]:
            if v != prev:
                self.depth[v] = self.depth[u] + 1
                self.dis[v] = self.dis[u] + w
                self.dfs(v, u)
                self.euler.append(u)

    def lca(self, u, v):
        left = min(self.first[u], self.first[v])
        right = max(self.first[u], self.first[v])
        k = int(log2(right - left + 1))
        return min(self.st[left][k], self.st[right - (1 << k) + 1][k])[1]

    def dist(self, u, v):
        return self.dis[u] + self.dis[v] - 2 * self.dis[self.lca(u, v)]


input = sys.stdin.readline
inf = 1 << 40  # use big number, float("inf") is quite slow
MN = 100009  # max bounds for both M and N (with padding)

############# START TAKING INPUT ##############
N = int(input())

graph = [[] for _ in range(MN)]
for _ in range(N - 1):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

M, T = map(int, input().split())  # M boxes, box T is treasure
room = [-1] + list(map(int, input().split()))  # box i is in room[i]

opens = [[] for _ in range(MN)]  # adjacency list, i unlocks/leads to opens[i]
for i in range(1, M + 1):
    opens[i] = list(map(int, input().split()))[1:]

key_start = int(input())
keys = list(map(int, input().split()))
############### END TAKING INPUT ###################

lca = LCA()
dist = [inf] * MN

pq = []  # (time from start, current box)
for key in keys:  # use the keys we already have
    heappush(pq, (lca.dist(1, room[key]), key))
    dist[key] = lca.dist(1, room[key])

# dijsktra's algorithm
while pq:
    d, cur = heappop(pq)
    if cur == T:  # got treasure
        print(d)
        sys.exit()

    if dist[cur] != d:  # already visited
        continue

    for unlock in opens[cur]:
        new_d = lca.dist(room[cur], room[unlock]) + d  # use distance between the box's nodes
        if new_d < dist[unlock]:  # found shorter path
            dist[unlock] = new_d
            heappush(pq, (new_d, unlock))

print(-1)
