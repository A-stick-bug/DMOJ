# https://dmoj.ca/problem/aaaa1p3

import sys


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


def get_heights(arr):
    freq = [[] for _ in range(n + 1)]
    for i in range(n):
        freq[arr[i]].append(i)

    res = [0] * (n + 1)
    ds = DisjointSet(n + 1)
    vis = [False] * n
    cur = 0
    for h in reversed(range(1, n + 1)):
        cur += len(freq[h])  # height i now visible
        for i in freq[h]:
            vis[i] = True
        for i in freq[h]:
            if i != 0 and vis[i - 1] and ds.find(i) != ds.find(i - 1):
                cur -= 1
                ds.union(i, i - 1)
            if i != n - 1 and vis[i + 1] and ds.find(i) != ds.find(i + 1):
                cur -= 1
                ds.union(i, i + 1)
        res[h] = cur

    return res


t = int(input())
n = int(input())
arr = list(map(int, input().split()))

if t == 1:
    res = get_heights(arr)
    print(" ".join(map(str, res[1:])))
else:

    res = [0] * n
    prev = 0
    last_i = -2
    last_j = -1
    for i in reversed(range(n)):
        diff = arr[i] - prev
        if diff > 0:  # new islands
            for _ in range(diff):
                last_i += 2
                if last_i >= n:
                    print(-1)
                    sys.exit()
                res[last_i] = i + 1
        else:
            diff = -diff  # join islands
            for _ in range(diff):
                last_j += 2

                if last_j > last_i or last_j >= n or (last_j == n - 1 and n % 2 == 0):
                    print(-1)
                    sys.exit()
                res[last_j] = i + 1
        prev = arr[i]

    print(" ".join(map(str, res)))
    assert get_heights(res)[1:] == arr
