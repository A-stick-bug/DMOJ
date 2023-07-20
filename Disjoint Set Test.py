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


# edges are already sorted, so we just ignore them (we only need the vertices in the MST, not the cost)
V, E = map(int, input().split())
graph = UnionFind(V+1)
edges = []

for i in range(E):
    node1, node2 = map(int, input().split())
    edges.append((node1, node2))

mst = set()
e = 1
res = []
for u, v in edges:
    if graph.find(u) != graph.find(v):
        graph.union(u, v)
        mst.add(u)
        mst.add(v)
        res.append(e)
    e += 1

if len(mst) == V:
    for i in res:
        print(i)
else:
    print("Disconnected Graph")
