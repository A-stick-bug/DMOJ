# TLE, PYTHON IS TOO SLOW, CHECK C++ CODE
# https://dmoj.ca/problem/coci19c5p4
# Tree LCA + difference array on tree
# from A -> B, split it into A -> LCA -> B, we add 1 to every edge on this path
# We can efficiently add 1 to the edges using a difference array on nodes and do a prefix sum
# on the tree starting from the bottom

import sys

sys.setrecursionlimit(100000)
log2 = lambda x: x.bit_length() - 1

input = sys.stdin.readline
N = int(input())
graph = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b, c1, c2 = map(int, input().split())
    graph[a].append((b, c1, c2))
    graph[b].append((a, c1, c2))


class LCA:
    def __init__(self):
        self.depth = [0] * (N + 1)
        self.first = [0] * (N + 1)
        self.euler = []

        self.dfs(1, -1)
        M = len(self.euler)
        layers = log2(M) + 1
        self.st = [[(0, 0)] * layers for _ in range(2 * N)]

        for i in range(M):
            self.st[i][0] = (self.depth[self.euler[i]], self.euler[i])
        for k in range(1, layers):
            for i in range(M - (1 << k) + 1):
                self.st[i][k] = min(self.st[i][k - 1], self.st[i + (1 << k - 1)][k - 1])

    def dfs(self, u, prev):
        self.first[u] = len(self.euler)
        self.euler.append(u)
        for v, _, _ in graph[u]:
            if v != prev:
                self.depth[v] = self.depth[u] + 1
                self.dfs(v, u)
                self.euler.append(u)

    def lca(self, u, v):
        left = min(self.first[u], self.first[v])
        right = max(self.first[u], self.first[v])
        k = int(log2(right - left + 1))
        return min(self.st[left][k], self.st[right - (1 << k) + 1][k])[1]


tree_lca = LCA()
diff = [0] * (N + 1)
for i in range(1, N):
    ancestor = tree_lca.lca(i, i + 1)
    diff[ancestor] -= 2
    diff[i] += 1
    diff[i + 1] += 1

total = 0


def solve(cur, prev):
    global total
    c_sum = 0
    for adj, c1, c2 in graph[cur]:
        if adj == prev:
            continue
        sub = solve(adj, cur)
        c_sum += sub
        total += min(c2, c1 * sub)
    return c_sum + diff[cur]


solve(1, -1)
print(total)
