# https://dmoj.ca/problem/yac3p2
# Extending median observation to tree, relates to centroid
# Complementary counting is used a lot
#
# Given 3 points, we can find the (unique) meeting point by first drawing the path from A to B, then from C to the path
# We reverse engineer this to make a combinatorics solution to find where to place A,B,C by casework

import sys

input = sys.stdin.readline
sys.setrecursionlimit(200001)

n = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

total = 0
sz = [1] * (n + 1)  # subtree size (including self)
ans = [-1] * (n + 1)


def solve(cur, prev):
    global total
    adj_sizes = []
    for adj in graph[cur]:
        if adj == prev:
            continue
        solve(adj, cur)
        sz[cur] += sz[adj]
        adj_sizes.append(sz[adj])
    if cur != 1:
        adj_sizes.append(n - sz[cur])  # stuff above current node

    total = 0

    # sum^3 - 2 same - 3 same
    total += (n - 1) ** 3
    total -= sum(i * i * (n - 1 - i) * 3 for i in adj_sizes)  # remove, 2 at same subtree
    total -= sum(i ** 3 for i in adj_sizes)  # remove, 3 at same subtree

    # one on `cur`, 2 on different subtrees
    total += 3 * (n - 1) ** 2
    total -= 3 * sum(i ** 2 for i in adj_sizes)  # remove, both on same subtree

    # two on `cur`, one on different subtree
    total += 3 * (n - 1)

    # all on `cur`
    total += 1

    ans[cur] = total


solve(1, -1)
print(" ".join(map(str, ans[1:])))
