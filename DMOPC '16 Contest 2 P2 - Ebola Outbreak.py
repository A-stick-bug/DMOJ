# https://dmoj.ca/problem/dmopc16c2p2
# Person 1 is infected, anyone in 1's class is also infected,
# then people who share classes with those people are infected
# We can use a disjoint set to quickly join infected classes together, O(1)

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


N, M = map(int, input().split())  # number of people, number of classes
uf = DisjointSet(N + 1)

for _ in range(M):
    group = list(map(int, input().split()))[1:]  # join classes together
    for i in range(1, len(group)):
        uf.union(group[i], group[i - 1])

root = uf.find(1)
sick = []
for i in range(1, N + 1):  # find number of people in same joined class as 1
    if uf.find(i) == root:
        sick.append(i)

print(len(sick))
print(*sorted(sick))
