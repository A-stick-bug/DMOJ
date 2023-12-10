# use union by size disjoint set since you need to get the size of a friend's group

import sys


class DisjointSet:
    def __init__(self, N):
        self.parent = [i for i in range(N + 1)]  # disjoint set stuff
        self.size = [1] * (N + 1)
        self.paper = paper

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
        self.paper[root_a] += self.paper[root_b]


input = sys.stdin.readline
N, Q = map(int, input().split())
paper = list(map(int, input().split()))

ds = DisjointSet(N)

for _ in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        a, b = q[1:]
        a -= 1
        b -= 1
        ds.union(a, b)  # add friend

    elif q[0] == 2:
        print(ds.size[ds.find(q[1] - 1)])  # get group size

    else:
        print(ds.paper[ds.find(q[1] - 1)])
