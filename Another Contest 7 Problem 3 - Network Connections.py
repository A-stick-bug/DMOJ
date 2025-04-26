# https://dmoj.ca/problem/acc7p3
# Kruskal's algorithm (MST)
# Note that "arr[i] < arr[j] given i < j" reduces the amount of implementation :)
# You will only ever connect 2 nodes if their node number are adjacent

import sys

input = sys.stdin.readline


class DisjointSet:
    def __init__(self, N):
        self.parent = [i for i in range(N)]
        self.size = [1] * N

    def find(self, node):
        if self.parent[node] != node:  # go up until we reach the root
            # attach everything on our way to the root (path compression)
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a == root_b:
            return
        if self.size[root_b] > self.size[root_a]:  # join the smaller to the larger
            root_a, root_b = root_b, root_a  # swap
        self.parent[root_b] = root_a
        self.size[root_a] += self.size[root_b]


N, M = map(int, input().split())
arr = [-1] + list(map(int, input().split()))

ds = DisjointSet(N + 1)
for _ in range(M):  # add free edges
    a, b = map(int, input().split())
    ds.union(a, b)

edges = [(i, i + 1, arr[i + 1] - arr[i]) for i in range(1, N)]  # adjacent edges
edges.sort(key=lambda x: x[2])  # by weight

total = 0
for a, b, c in edges:
    if ds.find(a) != ds.find(b):
        ds.union(a, b)
        total += c

print(total)
