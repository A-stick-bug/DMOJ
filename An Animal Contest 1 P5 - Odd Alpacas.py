# https://dmoj.ca/problem/aac1p5
# Tree rerooting DP (slightly overkill)
# Minimize difference between number of even and odd paths, flip at most 1 edge
# - first, count the number of even paths
# - then, for each edge, we try flipping its parity and check the new number of even paths
#
# TC: O(N)

import sys

input = sys.stdin.readline
sys.setrecursionlimit(300001)

n = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b, c = map(int, input().split())
    c %= 2
    graph[a].append((b, c))
    graph[b].append((a, c))

parity = [[0, 0] for _ in range(n + 1)]  # number of path of parity j in i's subtree
even = 0  # total even paths


def solve(cur, prev):
    global even
    parity[cur] = [1, 0]  # length 0 path

    for adj, w in graph[cur]:
        if adj == prev:
            continue
        solve(adj, cur)
        even += parity[cur][0] * parity[adj][w] + parity[cur][1] * parity[adj][w ^ 1]
        parity[cur][0] += parity[adj][w]
        parity[cur][1] += parity[adj][w ^ 1]


def reroot(cur, prev, up_parity):
    global best
    for adj, w in graph[cur]:
        if adj == prev:
            continue

        # parity of paths in cur's "above" subtree
        cur0 = up_parity[0] + parity[cur][0] - parity[adj][w]
        cur1 = up_parity[1] + parity[cur][1] - parity[adj][w ^ 1]

        # try flipping this edge
        delta = cur0 * parity[adj][w] + cur1 * parity[adj][w ^ 1]  # even -> odd
        delta_plus = cur0 * parity[adj][w ^ 1] + cur1 * parity[adj][w]  # odd -> even
        ne = even - delta + delta_plus
        no = n * (n - 1) // 2 - ne
        best = min(best, abs(ne - no))

        # reroot towards adj
        new_parity = [cur0, cur1]
        if w:
            new_parity.reverse()
        reroot(adj, cur, new_parity)


solve(1, -1)

odd = n * (n - 1) // 2 - even
best = abs(even - odd)  # flip no edges

reroot(1, -1, [0, 0])

print(best)
