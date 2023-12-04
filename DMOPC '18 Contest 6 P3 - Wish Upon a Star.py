# Q: check if we can turn graph into forest by removing one edge
# solution: create a forest from graph (using kruskal-like method) and check if it only has 1 edge difference from graph

import sys


class DisjointSet:
    def __init__(self, N):
        self.parent = [i for i in range(N + 1)]  # disjoint set stuff
        self.size = [1] * (N + 1)

    def find(self, node):
        if self.parent[node] != node:  # go up until we reach the root
            self.parent[node] = self.find(
                self.parent[node])  # attach everything on our way to the root (path compression)
        return self.parent[node]

    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)
        if self.size[root_b] > self.size[root_a]:  # join the smaller to the larger
            root_a, root_b = root_b, root_a  # swap
        self.parent[root_b] = root_a
        self.size[root_a] += self.size[root_b]


input = sys.stdin.readline
N, M = map(int, input().split())

edges = [list(map(int, input().split())) for _ in range(M)]
forest_edges = 0  # number of edges in our constructed forest
uf = DisjointSet(N + 1)

for a, b in edges:  # similar to kruskal's algorithm but there are no costs so we take any edge
    if uf.find(a) != uf.find(b):
        uf.union(a, b)
        forest_edges += 1

if len(edges) - 1 <= forest_edges:
    print("YES")
else:
    print("NO")
