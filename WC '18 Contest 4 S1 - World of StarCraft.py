import sys


class DisjointSet:
    def __init__(self, N):
        self.parent = [i for i in range(N + 1)]  # disjoint set stuff
        self.size = [1] * (N + 1)

    def find(self, node):
        if self.parent[node] != node:  # go up until we reach the root
            # attach everything on our way to the root (path compression)
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)
        if self.size[root_b] > self.size[root_a]:  # join the smaller to the larger
            root_a, root_b = root_b, root_a  # swap
        self.parent[root_b] = root_a
        self.size[root_a] += self.size[root_b]


input = sys.stdin.readline
N, M, K = map(int, input().split())
team = input().strip()

ds = DisjointSet(N)
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    if team[a] == team[b]:
        ds.union(a, b)

total = 0
for _ in range(K):
    a, b = map(int, input().split())
    total += ds.find(a - 1) == ds.find(b - 1)

print(total)
