# https://dmoj.ca/problem/bts16p5
# key point: we only get 1 cut, just get the sum of the weight and cherries of each subtree
#
# TC: O(n)

import sys

sys.setrecursionlimit(100000)
N, C, MAX = map(int, input().split())

# total cherries for cutting i's subtree, base case is just the individual node
cherry = [0] + list(map(int, input().split()))

graph = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

weight = [0] * (N + 1)  # total weight for cutting i's subtree


def get_subtrees(cur, prev, edge_cost):
    weight[cur] = edge_cost  # add cost of previous edge (which you cut to get the current subtree)
    for adj, w in graph[cur]:
        if adj == prev:
            continue
        get_subtrees(adj, cur, w)
        cherry[cur] += cherry[adj]
        weight[cur] += weight[adj]


get_subtrees(1, -1, 0)

total = 0
for i in range(2, N + 1):
    if weight[i] <= MAX and cherry[i] >= C:
        total += 1
print(total)
