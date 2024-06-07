# https://dmoj.ca/problem/dmopc15c7p5
# Good thinking question
# Explanation is in the comments below
# Tree path length queries with binary lifting and euler tour

import sys

sys.setrecursionlimit(100000)
log2 = lambda x: x.bit_length() - 1
input = sys.stdin.readline
print = lambda x: sys.stdout.write(str(x) + "\n")


class EulerTour:  # copy of my LCA template without the sparse table
    def __init__(self):
        self.first = [0] * (N + 1)
        self.euler = []
        self.dfs(1, -1)

    def dfs(self, u, prev):
        self.first[u] = len(self.euler)
        self.euler.append(u)
        for v in graph[u]:
            if v != prev:
                self.dfs(v, u)
                self.euler.append(u)


class BinaryLifting:
    def __init__(self):
        """compute powers of 2 ancestors"""
        self.parent = [-1] * (N + 1)
        self.depth = [0] * (N + 1)
        self.dfs(1, -1)

        LOG = log2(N) + 1
        self.table = [[-1] * (N + 2) for _ in range(LOG)]
        for i in range(1, N + 1):
            self.table[0][i] = self.parent[i]

        for layer in range(1, LOG):  # compute powers of 2
            for i in range(1, N + 1):  # get the parent of the parent for each node
                ancestor1 = self.table[layer - 1][i]
                ancestor2 = self.table[layer - 1][ancestor1]
                self.table[layer][i] = ancestor2

    def dfs(self, cur, prev):
        """run dfs on the graph to get each node's parent, could also be used to compute distances"""
        stack = [(cur, prev)]
        while stack:
            cur, prev = stack.pop()
            for adj in graph[cur]:
                if adj == prev:
                    continue
                self.depth[adj] = self.depth[cur] + 1
                self.parent[adj] = cur
                stack.append((adj, cur))

    def kth_ancestor(self, node: int, k: int) -> int:
        """answers queries on the k-th ancestor of a node"""
        while k > 0:
            jump = log2(k)
            node = self.table[jump][node]
            k -= 2 ** jump
        return node

    def lca(self, a, b):
        """get the LCA of node a and b"""
        if self.depth[a] > self.depth[b]:
            a, b = b, a
        b = self.kth_ancestor(b, self.depth[b] - self.depth[a])  # bring to same depth
        if a == b:
            return a
        # similar to binary search, to get node right below their LCA
        for jump in reversed(range(log2(N) + 1)):
            if self.table[jump][a] != self.table[jump][b]:
                a = self.table[jump][a]
                b = self.table[jump][b]
        return self.table[0][a]


def get_sizes(cur):
    """get subtree sizes"""
    for adj in graph[cur]:
        get_sizes(adj)
        size[cur] += size[adj]


N = int(input())
graph = [[]] + [list(map(int, input().split()))[1:] for _ in range(N)]
tree = EulerTour()
bl = BinaryLifting()
size = [1] * (N + 1)
get_sizes(1)

Q = int(input())
for _ in range(Q):
    a, b = map(int, input().split())
    anc = bl.lca(a, b)

    # A is before B in the euler tour, we can treat their LCA as the root
    # Length: Euler tour distance from LCA to B minus direct distance from A to LCA
    if tree.first[a] < tree.first[b]:
        print((tree.first[b] - tree.first[anc]) - (bl.depth[a] - bl.depth[anc]))

    # A is after B in euler tour
    else:
        # after going from A to LCA, we just take the euler tour from LCA to B
        anc_to_b = tree.first[b] - tree.first[anc]

        if anc == a:  # already at LCA
            print(anc_to_b)

        # To get to LCA, we need to traverse all edges in LCA's children that contain A
        # Since edges = nodes - 1, traversing all edges both ways is (2 * (nodes - 1))
        # Once again we subtract the distance going directly from A to LCA since we only take
        # this path once (on the way up)
        else:
            anc_child = bl.kth_ancestor(a, bl.depth[a] - bl.depth[anc] - 1)
            up_path = bl.depth[a] - bl.depth[anc] - 1  # account for distance from LCA's children to LCA
            print(anc_to_b + (2 * (size[anc_child] - 1) - up_path + 1))

"""
10
2 2 3
3 4 5 8
2 6 7
1 9
0
1 10
0
0
0
0
1
6 5
ans: 12
"""
