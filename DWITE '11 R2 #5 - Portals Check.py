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


for _ in range(5):
    n = int(input())
    ds = DisjointSet(n + n + 1)
    table = {}
    c = 0

    for _ in range(n):
        cmd, a, b = input().split()
        if a not in table:
            table[a] = c
            c += 1
        if b not in table:
            table[b] = c
            c += 1

        a = table[a]
        b = table[b]
        if cmd == "p":
            ds.union(a, b)
        else:
            if ds.find(a) == ds.find(b):
                print("connected")
            else:
                print("not connected")
