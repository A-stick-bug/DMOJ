"""
https://dmoj.ca/problem/nccc2s4
For every node, check the frequencies of adjacent edge values
- If 2 or more edges have equal value, we mark their subtrees as bad as it is impossible
  to get through the current node without duplicating adjacent values

Corner case: Entire tree is marked as bad except 1 node
- in this case, we must check the rest of tree again to check if the leftover
  node is good
- a simple way of handling this is simply allowing each node to be marked as twice

TC: O(n)
"""

import sys
from collections import defaultdict

sys.setrecursionlimit(100000)
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

bad = [0] * (N + 1)


def prune(cur, prev):
    """marks every node in cur's subtree as bad"""
    if bad[cur] >= 2:  # each node is marked as bad at most twice
        return
    bad[cur] += 1
    for adj, _ in graph[cur]:
        if adj == prev:
            continue
        prune(adj, cur)


for cur in range(1, N + 1):
    if bad[cur] < 2:
        freq = defaultdict(int)
        for adj, val in graph[cur]:  # collect edge value frequencies
            freq[val] += 1
        for adj, val in graph[cur]:  # mark subtrees as bad if needed
            if freq[val] >= 2:
                prune(adj, cur)

print(sum(i == 0 for i in bad) - 1)
for i in range(1, N + 1):
    if bad[i] == 0:
        print(i)
