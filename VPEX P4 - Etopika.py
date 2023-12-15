# TLE, python is too slow, check c++ code
#
# https://dmoj.ca/problem/vpex1p4
# DP + LCA
# use LCA to get the distance between 2 nodes
# use DP to get the min distance as we have 2 choices on each day, add the min of the 2 to the total distance

from math import log2
import sys


class LCA:
    def __init__(self):
        self.depth = [0] * N
        self.first = [0] * N
        self.dist = [0] * N

        self.euler = []
        self.st = [[(0, 0)] * 18 for _ in range(2 * N)]

        self.dfs(0, -1)
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
        for adj, cost in graph[u]:
            if adj != prev:
                self.depth[adj] = self.depth[u] + 1
                self.dist[adj] = self.dist[u] + cost
                self.dfs(adj, u)
                self.euler.append(u)

    def lca(self, u, v):
        left = min(self.first[u], self.first[v])
        right = max(self.first[u], self.first[v])
        k = int(log2(right - left + 1))
        return min(self.st[left][k], self.st[right - (1 << k) + 1][k])[1]

    def distance(self, u, v):
        return self.dist[u] + self.dist[v] - 2 * self.dist[self.lca(u, v)]


input = sys.stdin.readline
N, D = map(int, input().split())

graph = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b, c = map(int, input().split())
    graph[a - 1].append((b - 1, c))
    graph[b - 1].append((a - 1, c))

tree = LCA()
prev1 = prev2 = 0  # 2 possible choices for the previous node, store both and take the min (kind of like DP)
total1 = total2 = 0  # minimum distance travelled if the node we are current at is A or B

for _ in range(D):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    mid = tree.distance(a, b)  # distance we must travel, from A to B

    # first go to B and end up at A or first go to A and end up at B
    total1, total2 = min(total1 + tree.distance(prev1, b), total2 + tree.distance(prev2, b)) + mid, \
                     min(total1 + tree.distance(prev1, a), total2 + tree.distance(prev2, a)) + mid

    prev1 = a
    prev2 = b

print(min(total1, total2))
