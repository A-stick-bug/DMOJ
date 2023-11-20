# https://dmoj.ca/problem/graph3p3
# Template MST using kruskal's algorithm
# when sorting edges, we prioritize the non-dangerous cables, then prioritize cost

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


N, M = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(M)]
edges.sort(key=lambda x: (x[3], x[2]))  # prioritize danger over cost

uf = UnionFind(N + 1)
mst_edges = 0
cost = 0
danger = 0

for a, b, c, d in edges:
    if mst_edges == N - 1:  # full mst
        break
    if uf.find(a) != uf.find(b):
        uf.union(a, b)
        mst_edges += 1
        cost += c
        danger += d

print(danger, cost)
