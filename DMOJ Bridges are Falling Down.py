# https://dmoj.ca/problem/olyabc120p4
# Notice that it is much easier to iterate in reverse
# then we can use a Disjoint set to keep track of component sizes and combine efficiently
#
# At first there are NC2 disconnected pairs (everything is disconnected)
# Lets say we connect a component of size 3 with a component with size 4
# We can apply the following update to the number of disconnected pairs:
# - add (3+4)C2 since all pairs inside this new component of size 7 will be reachable
# - minus 3C2 and 4C2 since the components of size 3 and 4 no longer exist

import sys
from math import comb

input = sys.stdin.readline


class DisjointSet:
    def __init__(self, N):
        self.parent = [i for i in range(N + 1)]  # disjoint set stuff
        self.size = [1] * (N + 1)

    def find(self, node):
        if self.parent[node] != node:  # go up until we reach the root
            # attach everything on our way to the root (path compression)
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, a, b) -> int:  # MODIFIED UNION FUNCTION
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a == root_b:
            return 0
        if self.size[root_b] > self.size[root_a]:  # join the smaller to the larger
            root_a, root_b = root_b, root_a  # swap
        self.parent[root_b] = root_a
        size_a, size_b = self.size[root_a], self.size[root_b]
        self.size[root_a] += self.size[root_b]

        # apply changes to # of disconnected pairs
        return -comb(size_a + size_b, 2) + comb(size_a, 2) + comb(size_b, 2)


N, M = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(M)]

disconnected = comb(N, 2)  # current number of disconnected pairs
ans = [0] * M
ds = DisjointSet(N + 1)
for i, (a, b) in enumerate(reversed(edges)):
    ans[i] = disconnected
    disconnected += ds.union(a, b)

print("\n".join(map(str, reversed(ans))))
