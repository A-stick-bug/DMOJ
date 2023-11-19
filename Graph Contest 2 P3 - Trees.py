# https://dmoj.ca/problem/graph2p3
# Turning a graph into a tree/forest, this is basically a simpler version of the minimum spanning tree problem
# We can still use a disjoint set to construct the tree because there must not be any cycles

class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1] * size

    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1


n = int(input())
uf = UnionFind(n)

total = 0
edges = 0

for i in range(n):
    row = list(map(int, input().split()))
    for j in range(i + 1, n):  # start at i+1 because the graph is undirected (edges are duplicated)
        if not row[j]:  # no connection
            continue
        total += 1
        if uf.find(i) != uf.find(j):  # add edge to tree/forest
            uf.union(i, j)
            edges += 1

print(total - edges)
